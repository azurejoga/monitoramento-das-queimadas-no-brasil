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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1baf331-eaa4-34f5-a6e9-2e01f4dc838c | -13.74061 | -47.93311 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fd1218f-c40f-3bb1-8991-66971fb3fdff | -11.82374 | -48.06813 | 2025-10-04 03:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 105b8074-95c4-3e74-bbf2-7d50dc274836 | -12.08133 | -45.16193 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cf2fc02-3180-3a1b-b6e0-ed62354ef251 | -17.08956 | -46.24529 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0403d4b4-7421-3028-bcfa-e6001bfa00b0 | -16.09311 | -51.06826 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9afa5a44-f377-3c7b-9bf2-1464e3593413 | -11.54411 | -47.66529 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ade7cfcd-d91f-3dc8-9236-ea1a6c83a0e3 | -15.73654 | -46.26871 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e74efb0-32a1-36d2-93ce-66a27694773e | -11.85632 | -44.95142 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a5d44f-8ba1-368e-8dad-fb137e7645a9 | -12.02123 | -45.20461 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a00c7bb-2481-322e-a08a-5b44028798be | -13.29903 | -47.57411 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2e210a-171b-367f-9e8a-9bee029aeae6 | -12.70532 | -48.57286 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| acc5cb51-e61e-39e8-9e23-576de0ad8ed5 | -14.44178 | -46.11786 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018e4465-2bfd-36a6-b75a-c3749dd73fe4 | -12.64952 | -46.97443 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f71c6b0b-ba3a-30d1-be84-d14baf7943ff | -12.03505 | -45.20718 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 63af0ce1-798c-3472-9eeb-0f7deed0ac56 | -14.20232 | -46.65731 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96977408-8891-3878-bfdd-610b3a40a43a | -13.26468 | -46.48081 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33f179eb-4911-3daa-a8e2-20427087af26 | -14.92777 | -46.88271 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5420dd30-337e-35ff-b04f-bc7b6bae8f1e | -15.58812 | -52.46564 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bfffdee3-318e-3706-a1c9-e286f1ca4796 | -11.5113 | -46.74431 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8729b98e-fb0a-3bc8-94c6-bddd81714f4a | -16.73228 | -46.21341 | 2025-10-04 03:53:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee593e2b-66a6-3c79-8571-7c140abf2722 | -16.35938 | -49.40125 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 445d5260-79b3-395a-994b-1c3cd8ab8728 | -12.08759 | -45.15349 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 680226b8-098a-3450-b62f-c7dcc9694c1e | -11.28091 | -47.80218 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd7c14c5-4fad-30c0-8617-8ad615b0d453 | -17.957 | -44.25896 | 2025-10-04 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a43eff6-09fe-3e3c-8438-e2850473ae03 | -16.27841 | -47.10067 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8171d62-83ef-35b9-bc4f-f6820f9bd865 | -15.32596 | -46.30106 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 233c2097-c75f-37ac-a3ac-ec45d70ae5c1 | -14.30625 | -45.86864 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17854f84-1771-36e6-b7f6-fbd8eebacba1 | -17.08014 | -43.35777 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab8aebd7-0ec5-34c0-a471-6219245c6dd3 | -13.31729 | -48.1154 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d3f0835e-7a0f-3d36-ab71-249488c77417 | -12.42097 | -45.15408 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c560bbd-708a-319e-a367-9431f0ae8993 | -11.79596 | -45.02748 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30f88871-b8d9-3fbc-a61c-42896d0a432c | -14.88898 | -48.29582 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05941824-72a2-3a6a-95c3-69384399924b | -12.52636 | -45.9743 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f498bcec-50b8-3ad9-a01b-5618b3ef7b0a | -13.93222 | -48.16652 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cded16c-f62c-31d3-8f0d-595b7821ab20 | -15.72052 | -46.27714 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f50efd6a-afd7-3c8a-a952-3951f375c349 | -11.85547 | -44.95607 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdda8cbd-e805-3eda-aec8-374f47b58fe6 | -12.65034 | -46.99767 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22eea34c-7123-3895-a760-4accc6e0351a | -14.65786 | -48.28744 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85f5c907-dd07-3e54-93a4-a6590f51d760 | -14.21653 | -44.80025 | 2025-10-04 03:53:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16bd20d4-d5f9-3664-97ab-36909ed3c2f7 | -12.54847 | -41.30494 | 2025-10-04 03:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e9392894-9643-38c2-8cea-ac9bce43d4c7 | -13.55172 | -47.25133 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a2e71d-21eb-35ed-872e-adebf8c82c41 | -13.88438 | -46.51828 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7ee18feb-3f5e-3a4f-bda3-094dc59c5254 | -14.93781 | -46.85739 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c3a37d0e-1ab6-386d-a6ee-2e2bef6901ab | -13.29934 | -47.82649 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c2b65f4-995b-31e6-9c34-85635a0ba211 | -13.72906 | -47.92154 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 869d6732-d6d4-3c3b-b131-b53685cae5ee | -14.66871 | -48.26147 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7970bffe-6c30-3146-8aab-7d62fd7b64ad | -12.04053 | -45.20325 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| c2c3575c-1b24-3143-9266-d763d8c6183c | -11.93154 | -46.34672 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a1c2c5e-41a8-3ba4-88ae-da57362a3d02 | -11.87838 | -44.98505 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d24618c9-913a-3179-ab3b-b8ccfa086a66 | -13.11013 | -47.90136 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2717d910-48d1-39da-b5b3-3b32090a6c2e | -12.71196 | -48.56904 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b60ab2d4-a7f2-3bbf-a536-0084839215fb | -13.51941 | -47.30245 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c091afc-b08c-379a-8fde-6da2ce37e6ec | -12.70949 | -48.55173 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7fdbbff2-e26d-3fb5-bacb-6402a6c2096a | -15.03071 | -49.45184 | 2025-10-04 03:53:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf96647c-c232-33fa-b272-8976ae6365dd | -13.23147 | -48.48931 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 649b5529-d8f8-3afb-adf4-d9a194803c0b | -12.39758 | -46.51736 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2df64c8-a70e-337e-b62a-2194e8635bf1 | -14.6607 | -48.24591 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56b1e68c-75a8-3ec6-9490-b79c17793c15 | -13.26955 | -46.48191 | 2025-10-04 03:53:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 327f03cd-a30d-3cfd-8318-ce2e2564c2ee | -13.9335 | -48.16016 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfdbc35d-561a-3cec-94c4-2d77beadde16 | -13.88541 | -46.51279 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79a42281-a8bd-3df1-87fa-391d7457ac69 | -14.57997 | -52.49193 | 2025-10-04 03:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35dd913e-24c8-3dfb-b4d4-6a27209b0ad4 | -14.38637 | -45.94299 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6deb9b5-c3e8-3cf7-b6b5-d0f9c990dead | -14.44272 | -46.11298 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4526ab1-dd9a-3b94-9e91-c528f4e95b88 | -12.81162 | -46.85686 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89290b2-5c73-3b54-a8b0-6cc001e89454 | -13.39295 | -47.28596 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 169feba8-eec3-32e4-98f5-fb86f21612c2 | -13.50903 | -47.24526 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea623b38-cc7d-37b1-a9d2-0d932226aeac | -14.94269 | -46.85832 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 920d5102-d2f2-39aa-bfab-78ab735a52ed | -14.64411 | -48.30003 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8919a56d-cf1f-3bf1-9a27-1ce6db9fe202 | -15.35335 | -46.25832 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1705a5c8-b5be-3b59-b156-645bacb4f131 | -14.20036 | -46.06955 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 83058c8b-7222-380f-9051-0bcd8f4e9b0f | -15.32102 | -46.37843 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc333633-33a6-3008-b3cc-0f1d78463fe3 | -12.04141 | -45.19847 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 82caac11-d875-3ebb-b740-962480aec632 | -13.96779 | -48.18562 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc23d1f2-ee9c-36eb-b3cc-f994d79ed0f2 | -11.69378 | -47.50898 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9a7aca2-8d86-3204-bfa4-bc3e54065fa0 | -15.5774 | -46.91028 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dca51827-aba9-305b-86d7-701ef6b90d67 | -11.24141 | -47.79845 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 860496f2-9b6b-3647-b016-8430851b69f7 | -11.54676 | -47.68087 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bce5a18-d261-3778-84a5-029e108adbd2 | -13.67172 | -47.30071 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83746e0b-61b5-354f-9797-aa61f48bc4c7 | -12.94065 | -50.98658 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f512b0ba-2c9b-38ef-93eb-a14f0debd5bf | -13.21276 | -47.81446 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41acd3ba-8ccd-3c08-a8de-bd2ba7e79047 | -13.28279 | -47.18817 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d2ef8d4-a374-3566-932c-bd095eda7df8 | -12.29321 | -45.3605 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 863b85d0-bd99-3405-af27-0c493d84ba85 | -11.91741 | -46.36696 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 55865441-4cd5-3166-8002-639ea0c8cdc6 | -17.08414 | -46.24902 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b9c71c-18f9-3f73-94f9-e7e68e873af2 | -12.42092 | -45.1571 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82bd9474-18e5-383c-b1b5-4dfc32ca8b08 | -16.0859 | -51.07161 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f3de99-6fdf-3d2c-b2bd-1b6ef7d7e79e | -13.65038 | -47.3007 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 956324f6-5c4e-3463-a979-edb0bec5439b | -12.87219 | -44.62428 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1539dd52-4f56-3a39-b03f-8698fcee6266 | -11.86732 | -44.96834 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d569e13c-478f-3cef-ba6b-3000c820414e | -11.28163 | -47.79832 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c4357e9-8d3e-38b4-b0ec-4186ecd528e3 | -13.97778 | -48.19199 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3623960-729f-3562-a154-434db47862a3 | -13.33937 | -47.19871 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b690ea9c-eb3b-3d29-9b60-0ee80c488ac4 | -11.92939 | -46.35818 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29f19519-e3ab-34c6-a9be-87866b744c66 | -15.52597 | -46.82586 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe8bd48a-578e-33b1-8a92-2115ec57dfcd | -11.90845 | -46.24797 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 715d2f06-a4ed-39e8-a87d-e147f66da801 | -16.07988 | -51.06938 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eba0175b-2319-3f85-989c-16fe5dcd4e04 | -15.03592 | -49.45469 | 2025-10-04 03:53:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dd3d04c-349e-32d6-8ccd-e3ea862775da | -12.93122 | -45.06478 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aa02259-d07e-3366-9bfe-d8906e845da0 | -15.32025 | -46.30564 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6d1012-4bec-32c9-abc4-1c1b500e0e7a | -13.63264 | -48.669 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
