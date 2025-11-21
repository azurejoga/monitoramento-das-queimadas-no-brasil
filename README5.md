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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7be34193-c600-34d4-b0f5-b89f20e16b13 | -14.41052 | -48.2662 | 2025-11-21 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f448562d-78c2-3b3f-91c8-ac1f12b0c210 | -14.40506 | -48.2654 | 2025-11-21 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e16c610a-ae70-3cb3-9179-29581d452c9c | -13.73791 | -48.45128 | 2025-11-21 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c5eec6c-0b6d-3ac7-bc02-70fd9910b719 | -14.41523 | -48.27076 | 2025-11-21 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b3703f0-81b4-3f91-961f-7f94185d1cab | -14.52851 | -49.34203 | 2025-11-21 03:53:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 656c817c-2b09-3684-9eaa-7b4e5d73a834 | -13.78936 | -49.58426 | 2025-11-21 03:53:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee142274-856d-312c-90df-a81eaf0e2e32 | -19.68571 | -43.54909 | 2025-11-21 03:55:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fa6be9-212c-32df-80d2-b205e3eaee8b | -17.72194 | -48.07764 | 2025-11-21 03:55:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60fabac3-55d2-39ab-a512-4d418b669fe5 | -17.58161 | -46.67848 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1ea14a2-8284-38b8-a3ba-17b2affdb339 | -18.763 | -45.28289 | 2025-11-21 03:55:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa26b7f0-4017-3951-bd43-991732e8d3c4 | -20.31758 | -53.98913 | 2025-11-21 03:55:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb61025-ec89-3776-b2d2-7ca862ca9824 | -17.07366 | -46.60055 | 2025-11-21 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8194b9b-ae57-30d1-968e-75a249c00827 | -17.81135 | -44.31028 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f297c665-f2f3-378a-b536-2dce97d58fa0 | -18.27634 | -42.37862 | 2025-11-21 03:55:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a908eb3-5b3f-3845-a553-d75acff3f601 | -20.88847 | -52.34882 | 2025-11-21 03:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7b62a30-e74c-32e0-a415-9b1c80bc11e3 | -17.83224 | -46.99767 | 2025-11-21 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ae690ae-157e-3057-a8ee-85e3716ce5fe | -19.68801 | -43.54719 | 2025-11-21 03:55:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e978729-c1ff-338f-8b67-509a3481983d | -17.58621 | -46.67943 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5a54296-620e-36f1-9be8-486609566af0 | -15.23763 | -50.2117 | 2025-11-21 03:55:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9be33d01-54b7-3924-b4f5-8c1588f3d784 | -22.18934 | -46.9354 | 2025-11-21 03:55:00 | NPP-375D | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14df6511-05eb-39a5-93e4-62e95d46a472 | -17.40168 | -44.47747 | 2025-11-21 03:55:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af8e0d6f-2bc4-3264-809d-376085016919 | -20.18323 | -50.3851 | 2025-11-21 03:55:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef94a511-f3f8-367e-bcc0-a907b3996a60 | -17.5871 | -46.68342 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a412e22-be3d-3c9e-b47a-cef6afdd74ab | -21.24534 | -44.08678 | 2025-11-21 03:55:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c038b465-e447-39aa-8370-5d0ec61103b8 | -17.81507 | -44.34593 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 610286cc-56d8-3022-802a-3a1a53974d71 | -16.63363 | -51.30577 | 2025-11-21 03:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d77d7daf-9d45-38f0-a6aa-41e51b6dbacf | -19.21884 | -43.12555 | 2025-11-21 03:55:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7e31ae75-d9db-38d0-8bfa-27f03c4e135a | -20.17951 | -50.38121 | 2025-11-21 03:55:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41489a1b-3683-3a68-a2d5-1ec72824732e | -17.61914 | -54.20155 | 2025-11-21 03:55:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69b6d22d-0a87-3c61-ac7b-554edf4d5267 | -16.41337 | -43.12581 | 2025-11-21 03:55:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afdcbbf0-b8b5-339b-af60-158115f7ac9f | -17.238 | -48.11792 | 2025-11-21 03:55:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d94508f-673e-3850-bc19-a04a1b74aebc | -21.14844 | -45.82343 | 2025-11-21 03:55:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3d05cd4-d189-3d5d-8552-6aae92ff1406 | -17.79214 | -44.98819 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff45ad48-575f-33e0-afee-52b60629f78c | -17.59081 | -46.68036 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82576305-da94-32cf-9707-5a4b02504016 | -18.61213 | -44.26002 | 2025-11-21 03:55:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc6779ba-f6d4-34de-950b-8ef9f2381c5b | -20.18411 | -50.38115 | 2025-11-21 03:55:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f09dc7d0-b5ad-34ad-aa65-b45102332a8a | -20.32437 | -53.99061 | 2025-11-21 03:55:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d84e11d8-445e-39b9-ae84-d734c8f10117 | -21.04571 | -48.56148 | 2025-11-21 03:55:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8f9fd7c9-2e1b-3f13-a552-665b87a0c869 | -21.24252 | -44.08129 | 2025-11-21 03:55:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| be50364d-7fa8-35bd-a3fa-9adaf53426cf | -17.07826 | -46.60155 | 2025-11-21 03:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c52842b-e399-3e23-b5f6-8ac312222f7f | -17.80534 | -44.31048 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae05603b-e3fa-3417-8894-170a15a0d200 | -21.04212 | -48.55442 | 2025-11-21 03:55:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 43fd5aad-5d8d-3dac-a8de-a63fb208b884 | -21.15145 | -48.59937 | 2025-11-21 03:55:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 04e35c26-09c7-386d-9892-3e00ece52b2d | -17.6172 | -52.99891 | 2025-11-21 03:55:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c95aa2d-ba13-38d8-9922-02ee97872b09 | -17.6138 | -54.1922 | 2025-11-21 03:55:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12f8ff76-5db5-36a1-a427-425c421715f4 | -19.21832 | -43.12745 | 2025-11-21 03:55:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e4453077-e130-31e9-b4e3-8b19d93c65f8 | -19.27706 | -44.93056 | 2025-11-21 03:55:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2616f0d6-9f05-362d-8971-733e68361dcd | -17.79456 | -44.98769 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3595d51e-e52d-3f4e-a307-c765bb822c45 | -17.58981 | -46.68535 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f82003f7-7014-32ad-bffb-3da608f49ad6 | -18.27706 | -42.37451 | 2025-11-21 03:55:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 384cdc95-fafe-37de-a7f6-80df3897b254 | -19.8562 | -46.31095 | 2025-11-21 03:55:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a8392d-93da-330f-b477-01c2a4539f97 | -16.51833 | -43.54032 | 2025-11-21 03:55:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54823bd3-3c74-3f34-8b9e-0e5a1e3eb10d | -18.9181 | -47.17852 | 2025-11-21 03:55:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1840e6b-d1a4-377f-bbc2-e25a9f3172a4 | -17.4023 | -44.47413 | 2025-11-21 03:55:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feeb977f-b6cc-3a88-a0d4-01abccad55ec | -19.68936 | -43.54996 | 2025-11-21 03:55:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e6bc568-8b19-3499-8b4b-5297186ddfbf | -19.69164 | -43.54818 | 2025-11-21 03:55:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c1b1ce-5ade-3b28-985a-442507d60d31 | -18.76227 | -45.28674 | 2025-11-21 03:55:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7e89063-51aa-3f54-91e1-70a26bd03a18 | -16.73684 | -47.83846 | 2025-11-21 03:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8ab1de9-65ec-3c8b-9a0a-ab087471a167 | -18.10987 | -54.5221 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a01b7f5-656d-3a75-89a6-a88780c89ffe | -22.4169 | -44.22074 | 2025-11-21 03:55:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d5f0023-c4f7-3cde-a199-8198607d8d68 | -18.52719 | -44.62042 | 2025-11-21 03:55:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d74f23ab-ca4c-33db-bbce-a5813d5b994d | -17.61052 | -52.99716 | 2025-11-21 03:55:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67bd2f97-0dbf-35fb-96ff-0554e948d6c2 | -18.10266 | -54.52028 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45fcf44c-3d23-331b-8879-13f0f22fe25e | -21.04091 | -48.56016 | 2025-11-21 03:55:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60d14c31-fd67-3e4c-a25a-2300974054b7 | -17.64731 | -43.88278 | 2025-11-21 03:55:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6842d417-b1c1-3b89-8950-1b0afae656ab | -17.65025 | -43.88862 | 2025-11-21 03:55:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6c8305a-aa8f-3b9b-aa87-54a2e4754961 | -16.73187 | -47.83711 | 2025-11-21 03:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42b1af1f-99ac-375e-a256-2ecd45037a75 | -18.10911 | -54.52916 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f7e6e2e-8608-3db9-b9a0-2855a402711e | -18.10074 | -54.52821 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0dcbd2e8-71c4-3bb1-8bb0-bfd80075dac3 | -18.10193 | -54.52724 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd9ebb42-6f59-3b6d-97d8-bd57e3729147 | -20.88725 | -52.35405 | 2025-11-21 03:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fede724d-fa33-3026-b385-c2fbd6b27ef2 | -19.85705 | -46.30662 | 2025-11-21 03:55:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70f18a0e-291b-3ece-b8ea-d71a2126eb51 | -18.94038 | -46.9028 | 2025-11-21 03:55:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e09f915e-2c7a-3a81-ac31-314bf1e04f9a | -17.57887 | -46.67651 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cb5700f9-efaa-324f-9da6-72a42d08ac8b | -17.57703 | -46.6775 | 2025-11-21 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c065863-22b2-361a-82a8-59fd7e063e64 | -21.2499 | -44.08282 | 2025-11-21 03:55:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb504914-a9d5-34ef-9943-d8bb53558ec3 | -22.03538 | -47.18896 | 2025-11-21 03:55:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1617b4ff-8054-3fd9-8f12-71d817e08843 | -19.85273 | -46.30584 | 2025-11-21 03:55:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 855263ad-bdb3-3757-840b-9c49d4e5f1c2 | -16.45394 | -46.07352 | 2025-11-21 03:55:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72d7bbaa-6d92-335f-9969-f860ab544433 | -17.80927 | -44.31131 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb5385d-3b76-3731-b40a-0ca40cc16fa1 | -17.62112 | -54.19327 | 2025-11-21 03:55:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bf080bd-49b4-3350-9b37-293c071afb43 | -17.80742 | -44.30944 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e52e3b-a9aa-3e5a-9525-d01751e8ad37 | -22.86568 | -42.3946 | 2025-11-21 03:55:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3473d91d-4911-3928-b03c-67e51ba2dcbe | -20.76644 | -43.20807 | 2025-11-21 03:55:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dcbdf656-7d75-3ea6-8661-1590192568b8 | -20.88248 | -52.34686 | 2025-11-21 03:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ef1091a-210a-39ba-b206-31eda179679a | -18.88668 | -45.54834 | 2025-11-21 03:55:00 | NPP-375D | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e813c243-0a01-30b6-9716-5dcf65848c7f | -17.81642 | -44.35031 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8be8afa3-ab4d-3684-b51c-d380097d3981 | -17.6464 | -43.88785 | 2025-11-21 03:55:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5dae4ef-d0dd-3f21-9134-98df00d7cf27 | -22.89692 | -43.65514 | 2025-11-21 03:55:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 898483c0-ed18-392e-a3b4-6895fe03c720 | -17.83351 | -47.00025 | 2025-11-21 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f11b8e79-0992-3e41-a733-bb3092aa1d9a | -17.23862 | -48.11489 | 2025-11-21 03:55:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72405735-fae9-3aa5-84ce-034ca1c9a4b4 | -18.1039 | -54.51929 | 2025-11-21 03:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e554c4a-0547-3bcc-a110-111a208bef26 | -20.0663 | -40.84436 | 2025-11-21 03:55:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a93a80f-1f99-3490-91e1-e1877d6df989 | -17.81407 | -44.35125 | 2025-11-21 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b07609a4-6991-31ce-bbfb-8213d23592d2 | -16.73128 | -47.84 | 2025-11-21 03:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48eab09-8afb-3be2-9fc7-76f9fcecc103 | -16.29582 | -46.58961 | 2025-11-21 03:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6cc2f0-b815-3bc9-b84e-1310549eeae5 | -21.3732 | -48.6032 | 2025-11-21 03:55:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d2a7784c-f5d2-3df4-900a-2e757f5ed654 | -17.64254 | -43.88709 | 2025-11-21 03:55:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04071090-f00c-396a-9499-ab343d194204 | -17.39767 | -44.47672 | 2025-11-21 03:55:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81c12e3e-f137-3b02-8235-2e461041706c | -20.18503 | -50.3825 | 2025-11-21 03:55:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
