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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acca06df-3640-38a8-8ef6-0e984eb76d60 | -10.74977 | -50.35478 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e9986ab-fff7-3ef8-9e77-eec6bd5f5e95 | -16.86339 | -43.2351 | 2026-08-20 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88b36bbc-5b6f-35e2-9ef1-ea5b4b30c6e4 | -9.75554 | -43.31487 | 2026-08-20 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1cc2af00-025a-3000-b6b2-69e8cb7bad5c | -12.8152 | -48.42702 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c41d178-5a37-373f-a09a-808eb4c6a27f | -10.74215 | -50.35892 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c12e39d8-a69d-39a2-8562-9bf5c2482e2e | -15.17893 | -48.76525 | 2026-08-20 04:02:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43c340cd-ce95-3091-ae54-91cbff7b47ad | -15.53378 | -40.85678 | 2026-08-20 04:02:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57d91c6c-8940-3b7b-81b8-2f4e9ca71292 | -12.77655 | -48.41752 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9dd3829d-44d6-3fb7-b43a-27259826767b | -13.4785 | -51.44373 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06dc6127-7258-3722-9ec4-fec56930ed80 | -14.27516 | -51.89273 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ee495951-c938-3020-9f8d-8ec504788649 | -12.24688 | -43.17296 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a2b377e4-2c2a-3144-80b2-0ad5587943d9 | -15.58784 | -43.74089 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| af223c2a-0dae-3ba6-b307-8d3bc7fceedb | -10.79225 | -50.3121 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d63a52a4-4e74-3f79-ad58-1a607c3afc61 | -10.78579 | -50.31074 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2c23cb0-4390-32db-8941-5f0bb5b87b98 | -12.24787 | -43.16745 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9fd8de4e-3817-3c7d-8605-d6b8eb185c28 | -16.53832 | -43.31807 | 2026-08-20 04:02:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ef31348-c805-319a-bc3d-efd6fe1ee552 | -14.7135 | -47.14853 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa3accd6-c865-318f-8f81-71ef11064ddb | -10.75019 | -50.35621 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd8136c5-a53f-3e1b-b17d-fc1489330d54 | -12.85005 | -48.42644 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a563945-43b1-3398-a7be-adbd3f5bf49a | -16.42948 | -42.63446 | 2026-08-20 04:02:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a817f134-3a08-3c2d-89bf-05be403c0365 | -14.20301 | -52.88471 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8671b229-421e-3e8b-88d1-ec2d736cfda4 | -12.80333 | -48.42848 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0862f9cf-e1c4-3b25-a244-af1e8d49054a | -13.44893 | -51.43669 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70b27326-a5dc-3ad1-92ea-729442cab7f1 | -15.56297 | -43.43768 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 808bcd3f-cb1b-385d-ac74-43e4d0ddd6d1 | -14.27901 | -51.8884 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16115ae4-51ec-3389-9c11-b11f448626e9 | -14.11782 | -44.38419 | 2026-08-20 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8933f9c-f578-3931-863a-ae9717ffca3c | -14.45749 | -45.62185 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5813e73-5577-343e-a8e8-ceaea363f3f5 | -16.53937 | -43.31631 | 2026-08-20 04:02:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ac09c7c-b5bc-37af-b50a-0a1bcd26083f | -10.25621 | -46.99408 | 2026-08-20 04:02:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8f287df-b691-3ceb-8180-340d420660fa | -10.4173 | -48.33416 | 2026-08-20 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f78bf1-9967-35cb-955f-3158a06a4302 | -11.31493 | -45.20552 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a335cdf-5dbb-3bd5-8d5c-98d523ea8adb | -15.7115 | -47.80666 | 2026-08-20 04:02:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 246e60e6-d506-3dde-999b-35586e8dcf17 | -11.31631 | -45.20752 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d59aa3d1-2859-341a-859e-9c7e54f1ec83 | -14.45214 | -45.62553 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b82cbaec-c4d2-3af7-9f27-0f4b0c671e0b | -13.5453 | -52.22687 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de0272e2-e084-3339-a2fd-193ba5848ba8 | -13.45015 | -51.43087 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ecfecef-eac7-383e-b2bf-eb742bb20851 | -12.24537 | -43.13544 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab215016-ab7f-3f1a-a50b-0cf87722a256 | -11.43184 | -47.25264 | 2026-08-20 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e343628d-9ee3-30d0-ae84-d0174021cec6 | -17.73792 | -40.09827 | 2026-08-20 04:02:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b16382f9-c22a-365b-b71c-555932dfa847 | -11.42718 | -47.24825 | 2026-08-20 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb2862d9-bba0-3b92-afab-557e735293a2 | -14.94597 | -44.32034 | 2026-08-20 04:02:00 | NPP-375D | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd670105-68e2-3e58-94ed-15850f007bd0 | -11.14088 | -49.04306 | 2026-08-20 04:02:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1be1b49c-14fa-342c-ae7f-22f5bf94e1dd | -12.25281 | -43.16286 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fe69d23e-b8aa-30a0-81cf-59903204f179 | -14.453 | -45.62089 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2fb0120c-23f4-368b-ae70-fab1e4c5e727 | -11.37688 | -46.37315 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9054cf3-c66c-3611-a7d3-0c99d0e2586d | -14.44401 | -45.61909 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8dfb86d-e6c0-38e5-bc06-49766ff61739 | -8.7172 | -49.61023 | 2026-08-20 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 147a0f7b-62b0-39ef-9189-89cd772cbe93 | -12.77361 | -48.41526 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8394660-b0bd-346c-8001-2c9ff2b02a10 | -12.82328 | -48.4155 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3794c232-684c-3d19-8171-f5fca1c42463 | -14.08249 | -40.96054 | 2026-08-20 04:02:00 | NPP-375D | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3c245fe-8adc-30a7-9001-bd6368db2f9d | -14.27234 | -51.88697 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 538b754e-d246-38c4-8f21-4a17be89a1dd | -12.81232 | -48.44159 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab15123d-1929-34f9-ba10-61c65bc07362 | -14.44314 | -45.62372 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cd894d3-174c-39c7-b6d8-c9618f05622f | -10.42386 | -48.33115 | 2026-08-20 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d0e5ecf-ce42-31be-a844-ffc56d9098aa | -15.48641 | -48.43478 | 2026-08-20 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d57f7056-e994-3b49-835c-7b91aa1eb7f1 | -15.58533 | -43.73872 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c46f71e1-4ce2-3f40-85bb-4bdc4f4c938f | -12.8507 | -48.4231 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf2bceec-1175-33c9-a2b6-4cbbd7d9fadd | -11.32006 | -45.21326 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36f2fa57-03a7-3eeb-817e-4d5a0e7a7043 | -14.44488 | -45.61446 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c27e784-042e-3b2f-90a3-44a82b4c31a3 | -12.77208 | -48.41096 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d37d851-3e25-3b21-bf40-f44a2e499cb1 | -13.35603 | -41.67493 | 2026-08-20 04:02:00 | NPP-375D | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0e94d567-0c8c-3195-aea5-bbf01a5c8c53 | -13.56641 | -51.67554 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0721f65c-c23f-3741-a968-9cbe259db31c | -14.27767 | -51.89444 | 2026-08-20 04:02:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a04f7a0-baea-3552-bd32-336e1bde03bc | -12.82887 | -48.41647 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 269df702-1ded-3e32-8219-abf36c77eaaa | -9.64461 | -47.80965 | 2026-08-20 04:02:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1d1e92-3561-317d-9030-3f66847310e9 | -10.75738 | -50.35063 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6457aaec-8806-3834-b1e9-a77a1a23b3b3 | -12.80243 | -48.43301 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc37f032-cfab-392f-b63b-a9b7cbcddbbe | -12.2443 | -43.13399 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bbb98d0-f49a-310c-9c2a-17334cc1bf28 | -10.74863 | -50.36029 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28697aef-7b55-3dbf-bbc2-21e086023c09 | -15.56682 | -43.43841 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc999479-6058-3cb6-836a-be41996fafdc | -12.80891 | -48.42956 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6deff74b-883d-3f7f-9aaa-c984a569d8ed | -10.74909 | -50.36173 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91f823d3-8ac2-3656-9347-1bb4d7145e60 | -15.56387 | -43.43272 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ea2f24-3682-3c44-9c19-b40f46c77ffc | -14.73275 | -47.15469 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7945985-0909-3cc4-a80e-1a784b64eb08 | -13.51624 | -43.81653 | 2026-08-20 04:02:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2d11a02-f9e6-32ff-bb44-07b3deddd1e6 | -13.15692 | -42.41302 | 2026-08-20 04:02:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 298028eb-e32d-37cc-b905-1b2c9ccd2d3f | -12.82207 | -48.42157 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c01cec6b-2c20-3e6a-9d82-8be6712798d9 | -12.84349 | -48.43038 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c80850a5-c86d-3976-9a6c-49614d628827 | -11.81523 | -44.81054 | 2026-08-20 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 00042ba2-64b8-380a-8469-b6b2257d1faf | -14.45024 | -45.61074 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d20fd85-77ab-3958-af88-c283aadc9e43 | -16.61074 | -43.37098 | 2026-08-20 04:02:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf1e7ba-37b5-3b05-a79f-fd533919710a | -14.45387 | -45.61626 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 80519203-603a-365d-84f7-07d18799d6ff | -14.21751 | -52.90039 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 22ceaf1d-e6ed-3956-948e-835bde8c3d28 | -13.44689 | -51.43033 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 931f1b50-8b55-3f19-b0eb-f3ae9f9e108a | -14.30583 | -47.17525 | 2026-08-20 04:02:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a2f243b-7f4d-3a1b-866c-06a022707e84 | -11.38181 | -46.3745 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68b3d8fe-46ed-3c88-be50-5b11c5e19886 | -12.79342 | -48.42009 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd8317e1-eb01-37b2-b611-c95e8b190b50 | -13.44002 | -43.84246 | 2026-08-20 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19cd1024-d9ac-3cec-89ec-9ac3514c1c15 | -12.78275 | -48.41553 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62ec65b4-15de-3772-a434-b82645006dde | -11.38676 | -46.3757 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40d6729c-2124-3aa0-b527-8944d1e70535 | -15.36762 | -52.78263 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d64be5b-0f48-3a6e-8855-daefb5fe734f | -12.25032 | -43.13077 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9fa1e078-ec45-38fe-975d-9a6abc2d262a | -10.41702 | -48.33203 | 2026-08-20 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b949ff0e-047f-34fc-88d3-9108226ad211 | -12.25676 | -43.16375 | 2026-08-20 04:02:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 94866040-7fd4-3768-a249-f4e6d3feaf9a | -11.28402 | -45.79247 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8833c5a9-4654-345d-b0e8-59e05455e25e | -12.80146 | -48.43788 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f14a0b0b-8770-335e-af6f-6b74ab9cd10e | -12.84567 | -48.41928 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d740d0d7-996a-3a4f-b8c2-336cd13dde84 | -15.36092 | -52.78032 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7dd2b137-4bef-3306-bce3-dcc864043b3c | -13.4407 | -43.83868 | 2026-08-20 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 11ebd48a-c748-3ad1-8b27-fd80bbb62186 | -14.73328 | -47.1527 | 2026-08-20 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
