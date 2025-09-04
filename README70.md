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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8800d291-0e9d-3de7-853e-bd49bcbe94d8 | -10.0639 | -58.39305 | 2025-09-04 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f30675d-dcd4-3dd8-b104-1b1426ee6f39 | -14.59699 | -54.58963 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fb75ab7-1460-3dab-839d-2ba493820125 | -11.63648 | -52.18286 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 041e6648-d100-3b98-9e20-7183325373d2 | -14.56395 | -49.13827 | 2025-09-04 04:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f49a1c8-8c26-3927-9e8e-2391d5ff70f8 | -14.3957 | -51.6741 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 930a4926-7962-30d5-8f8e-8aa3ada9daf1 | -12.97918 | -54.78004 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732417cb-ebab-3f3c-a46f-6b788252c8c2 | -8.70065 | -62.39774 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a16acd-0ef0-3676-8331-d9e03aac1d36 | -12.91087 | -56.99684 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24fcda3c-ceb8-3ad3-a7a4-fce2820359ea | -15.46584 | -53.01395 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 806ffcf9-b75f-3a02-946a-afcf8ebab6a9 | -13.44706 | -46.93972 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4fe2b00b-9833-35d6-8e48-05792d1559c9 | -15.04231 | -50.07199 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12477363-1e6d-3b39-ad42-d75b3d3cfbd6 | -13.44669 | -46.92804 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4efdc3a3-41e4-356c-ad58-85faec1888a9 | -14.56029 | -48.07102 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 259eb6c7-bea2-31ac-8fd9-0e69bde30b4b | -14.78792 | -48.13611 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2981770d-01e8-3e7e-b728-c560805c70ea | -13.75337 | -46.9393 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f0ca05d-8f72-3cd7-9b38-7779248b7276 | -12.91145 | -56.93802 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff455372-8311-3214-875b-38170adc2304 | -14.56887 | -54.52999 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cb9026c-e9e1-3183-acd6-9bbb8156b0ba | -12.8922 | -56.94322 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9face014-3625-37ee-adda-fdd4a09e0453 | -15.13494 | -48.17386 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c904efb-d3a9-3ea7-aabf-752e96fdcada | -12.88506 | -56.94198 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2981e09f-2be9-3075-894e-582a79aa1ea1 | -12.50393 | -53.83546 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad18bc13-0928-34df-8bd0-06bb94cac0bd | -16.53351 | -55.08908 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c1ce1be6-5688-3b40-b358-a8eb49b30289 | -13.10326 | -57.11036 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f56c681-e29b-360c-a2e6-6576dd0dc398 | -15.53171 | -48.34603 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed4a8332-89f1-3854-9d95-809cde5adcc9 | -10.57926 | -55.41687 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6324366c-4d97-3720-b5dc-7ea6294c9741 | -11.87604 | -51.54268 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fd6db5c-4c3d-3190-98ab-947ae5be738d | -9.11433 | -61.48695 | 2025-09-04 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1e82afb-f87d-323c-8dba-cc111ba8c738 | -15.03576 | -48.11084 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f2c5edb-4b33-38ac-ba6e-821c5fab99d2 | -11.57807 | -52.15544 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2f39fdf-1039-3cc6-9757-9d1647d54aaf | -15.15494 | -52.37193 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 311fdbad-ab64-31f5-af42-a2a773de4d52 | -17.15618 | -46.24702 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f537f0c-9ece-3f36-ac47-5cf5e2b8a8dd | -12.17702 | -53.89482 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 282134f3-c0d7-35c3-ad82-68bb71407a5e | -9.49577 | -57.82096 | 2025-09-04 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f66dca0-75a9-3a18-beed-5db520142073 | -13.10702 | -57.11811 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 711d5a67-c8b5-3082-a717-5c5706509881 | -12.48729 | -53.83274 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ab784a-bc11-37a5-8ded-980f9aea192a | -12.46189 | -48.08216 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f32fed11-1c92-3b34-940a-a711b10b2c46 | -14.77364 | -48.14277 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10082244-90a2-3a5f-a60a-c86cbd35b265 | -11.08877 | -52.02443 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63353eac-ed2f-31c1-8ad8-9822ab34af7b | -10.96449 | -49.74699 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb176878-9ac7-3f9c-9b64-09e7fbed64f8 | -15.02801 | -48.10126 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5170ed1-67f2-3d6c-a9d9-c64611d6dddb | -11.58431 | -52.16022 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a833f46-623d-3d59-9a53-2675e199927c | -10.98589 | -50.92072 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31b11991-aee8-3944-956a-6aa138a08553 | -18.20208 | -49.72364 | 2025-09-04 04:55:00 | NPP-375D | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3fae76e-c41e-3c46-b761-b8ae59bb221f | -11.63993 | -52.20611 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 810d3a26-cdf1-3674-8f26-007eeb909ec7 | -14.47945 | -56.47916 | 2025-09-04 04:55:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 555423f0-778d-394a-9c5a-95ee3b44f19e | -10.4772 | -53.62677 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2a592b6-0007-31ed-9e22-42805b30604b | -12.89508 | -56.94798 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2f5ff59f-aee5-38e5-956e-172ad67bc1f1 | -12.50061 | -53.83492 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 432bd397-e7f1-3871-9520-ff2915fedbe5 | -14.57223 | -48.08205 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8467a85b-c43c-39b7-8674-3c7f4ead5e96 | -12.92019 | -57.00698 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81d86942-003b-3466-8435-57c113b7b416 | -14.58457 | -53.01195 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0aaa637-36c5-3411-917e-c20ac975ec2e | -10.1145 | -54.79855 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e32d6068-df80-303b-9d9b-d7faa249f607 | -15.05157 | -48.36574 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f9fef40-b1f6-39c9-b0e0-1c8c94cdbcfe | -11.61923 | -47.77477 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01b29276-a99c-3d5a-a874-aad0ffe74247 | -11.67622 | -57.34764 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4de8409a-a22d-30f0-922c-bbc5f4b1f3b3 | -11.64049 | -52.20242 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628cbf77-b20d-37f4-9519-95d3e0084aea | -9.49662 | -57.81597 | 2025-09-04 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c00792-77d1-37b3-badb-00a814589cf3 | -13.50649 | -46.92087 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c2b5f23-bbf8-32d7-91b1-e0a67f5afe16 | -15.05405 | -50.0448 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 682678be-4727-351c-b83c-e68790470cbf | -17.14589 | -46.24572 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2671d66c-ba23-3887-b1d7-9c7f4051fbc1 | -11.53717 | -54.49133 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7bcf8de-d67b-3207-912a-5aa8199e199b | -14.57245 | -48.07546 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d8aa3eb-816e-3a42-8ebf-0a3ac779f83b | -17.16859 | -46.2294 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9713f1dd-3d5f-396d-b38e-115d9380f544 | -12.91231 | -57.00991 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb026a59-b159-3955-9f25-30bcf8f93ad6 | -14.59301 | -48.01907 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2458a0c1-e0da-30f2-80dc-b90157f3778c | -12.91076 | -56.94217 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e05c34ec-0d31-3b8d-beaf-316dc621d5d5 | -11.59678 | -52.14703 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f411f9d-069f-3e5e-8fbe-c7a2514507e4 | -12.97584 | -54.77948 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ec33c0-f949-3f5d-8055-7cf2ec2a11dc | -16.81336 | -51.32761 | 2025-09-04 04:55:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cf5610d-fdf5-38cf-8980-55a02d739f88 | -12.97134 | -54.78607 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e687602-5e9a-3d76-9222-05e66f3368c0 | -15.17736 | -52.35043 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 840dd9c4-7318-37b2-b601-e2e52d29be0d | -8.70127 | -62.39431 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e6b259-f196-3f21-a394-f95f0fb98c5b | -12.9748 | -54.76462 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53f9bcb-3dc5-3762-9619-0854d3f8c98d | -13.57555 | -48.12493 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24e56c7f-8a3f-31df-bd37-88e070760882 | -11.96628 | -45.78333 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cf63dea-b062-32db-81ac-5e553e712bff | -11.20024 | -55.01984 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 202d08d5-2c39-365b-931e-e109f3f4b16b | -15.24816 | -53.79908 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fb48041-1396-3f6b-96e2-f9d2ab098579 | -15.02691 | -48.10984 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6f9684e-9d23-3ae5-b7d2-5b2333565759 | -12.89647 | -56.93968 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8ba1d85-335f-3cec-a518-fca154640d86 | -10.09333 | -54.75761 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecce549-ef1c-31eb-a050-17123d8a363c | -11.6495 | -54.53172 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43134b06-0021-3d60-a435-c3e7ca7100bc | -13.85928 | -47.97495 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bea420b4-8dbf-3d4e-870e-f97d50dc24db | -11.87662 | -51.53881 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 046c11e4-2826-3a3f-b5ef-b15d8a9c394e | -10.49161 | -53.64349 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 304a77fb-4522-3074-b697-4b634d715f12 | -11.63029 | -52.20084 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8483ec3-4a11-3985-a908-73547e758a64 | -17.16098 | -46.25082 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a7a3624-92b1-3b84-9e4e-0d637becd8a3 | -11.09613 | -52.04457 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fb863b6-420f-357b-b5d5-1720ee1da62e | -12.46617 | -48.08259 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eac917ff-8d39-31c2-9355-323183504f42 | -11.32064 | -55.22499 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60f3f609-d2c1-304e-b2b7-a52fa9e0ecb9 | -12.92701 | -48.06953 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceecf7a1-b6a4-3f0f-9a79-76c255fef126 | -10.58269 | -55.41746 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90b56af1-4085-3551-bc94-448f378e98ad | -15.18429 | -52.35166 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcc770c5-3780-38eb-aceb-7f4179c2b82a | -10.45115 | -53.61896 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87cfeb0f-cdd9-37da-a5f1-149d81a42841 | -10.48828 | -53.64295 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82122c0c-3f98-33d8-b606-a97f14317d39 | -12.89151 | -56.94736 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9dc7f74a-fdc6-36c2-916e-ba9036987556 | -12.47901 | -48.08394 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e51b5cfe-375c-39bf-8fc1-e1dbfb18d35a | -13.8153 | -56.60728 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df410024-5664-3020-9f4a-bb7e66cc2657 | -15.30522 | -52.76156 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a652eff5-dcc2-38bd-a54a-57ebe43aba25 | -12.48865 | -48.07687 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a0fa8c1-519c-3edf-ba91-02b27c2eb752 | -10.06791 | -58.39382 | 2025-09-04 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README71.md)
