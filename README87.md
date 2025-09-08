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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5ba52dc-c918-34b2-a963-c886c3ef83d7 | -16.28875 | -58.12096 | 2025-09-08 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 495060b1-099b-3a47-9f36-194339124209 | -14.51328 | -48.79906 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 000af85c-30c6-3f08-a3f4-5d6fb0a8dd2c | -15.24251 | -52.35895 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3bc1d61-c3ae-3640-99d4-8ca472337c67 | -15.38434 | -53.94902 | 2025-09-08 05:23:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1164ecb7-f394-3bdb-960d-7c699f01c773 | -12.86839 | -62.11275 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0690f944-5e36-3a9e-9bb5-a896d1a07224 | -20.95 | -48.46032 | 2025-09-08 05:23:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 758535f3-2653-359f-97c7-a55a307cf019 | -14.70668 | -60.25357 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad324f33-ca9e-3972-8f89-b7e48dc9ca81 | -15.7625 | -53.55735 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88800d6e-0a88-3180-8f74-b6eb4132f83c | -15.68962 | -58.72564 | 2025-09-08 05:23:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ff37c419-abf0-3a87-ae56-e9e01a832c52 | -15.24708 | -53.82728 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89311ea9-3138-3f4d-b5ac-3ff1be864ff7 | -15.07828 | -50.10618 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c4ac702-dff4-380b-a6a8-bfc9624ee1ce | -14.09149 | -46.6067 | 2025-09-08 05:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cc51e26-0795-32e2-84a2-a0a83a745cc0 | -12.87584 | -62.11017 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b467dc7-12be-3b84-8952-2f2fbd60e580 | -16.33437 | -52.93116 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f7dc15f-c1cb-335c-9f70-2a1e456ad92d | -16.33454 | -52.92726 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fefdb02-40ae-36ce-8780-f2644887e6eb | -15.07876 | -50.10184 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ff53c54-c3e3-37ab-84f0-e3c80f99d7b1 | -14.4607 | -48.79451 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7ad4859-ab3d-3487-aecb-4a686ffecf4b | -15.76724 | -53.55801 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43646465-5c27-331c-aede-60852e11aeeb | -15.19027 | -47.98445 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5c95af8a-b9c5-3d45-8d6e-4f77f2d4a111 | -14.51807 | -48.75442 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ad8f9fa-b6cd-3f3c-a346-5c836185d542 | -12.87646 | -62.10643 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16f2e914-9052-36d4-a8bf-8fd1540e3016 | -15.82572 | -52.26712 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be04edbc-899b-30c9-a09c-fb6beb9359db | -14.8084 | -48.24106 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ee6524-4d7f-3706-bcb6-cc3ec420bc87 | -14.50535 | -48.81307 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a5b7df3-94dd-3081-8d75-b116fb7682b4 | -15.24761 | -52.35971 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02f41979-86b8-3360-a786-f8b5ac4e9a94 | -15.66912 | -53.86762 | 2025-09-08 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95fadbd8-1c9b-3529-9e14-1d767417153a | -17.58449 | -49.80269 | 2025-09-08 05:23:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adb1ac9b-ba8e-364a-8ca6-af563a59c83d | -15.08253 | -50.06702 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7463bde-433f-35ba-a12b-63200e1e74e3 | -18.02893 | -47.10538 | 2025-09-08 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a5fe6c4-2fb3-3de0-8d65-639cd61c8289 | -16.34249 | -52.94595 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b72856f8-5e7f-3e51-b0a2-3fb26b51addb | -12.79426 | -60.18553 | 2025-09-08 05:23:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be4aa4a-39fa-3470-ade5-be631c0104cc | -14.87846 | -55.81927 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838c2f8d-b7c2-3d14-a2ba-6c0973f3b2d4 | -14.52291 | -48.76942 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2f4f18a-f9e0-36a4-84cf-2c06b89e5e6c | -15.25396 | -53.80117 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9eadaa23-2bc8-3ea1-8451-28e2eaeafbae | -15.08212 | -50.07074 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9190d46-30b6-3c49-bf3a-d115f01ec8cf | -15.27016 | -52.38782 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a92ea7c4-80be-352c-816d-56364e4210c3 | -15.26578 | -52.38115 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a4f7497-2f4c-365c-a81d-787f8069e24c | -16.33863 | -52.93765 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2a380e9-8168-3703-8e2f-767a3b43ea3e | -15.76593 | -53.56869 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1753e24c-8a76-31e4-b203-8fde08bf3e34 | -15.8333 | -52.29182 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 979520bd-5f0b-32aa-82c2-b47db361d20b | -15.75499 | -53.53996 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2094b21a-bbda-3c90-ab42-15c547e59ddc | -15.18133 | -47.9578 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06e286e1-d26b-33d9-849c-672e79c51ed5 | -14.5883 | -48.08831 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fea8500-af5a-312e-b736-01dd2f830f83 | -14.52178 | -48.77991 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b002dff8-624e-34a2-a7a0-2d578522428e | -13.18392 | -60.82004 | 2025-09-08 05:23:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9acbc64e-8beb-3e7b-a8de-7c6960dd5c65 | -15.84116 | -52.26975 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2504e1f4-6eff-30a8-b34d-bb8660defd04 | -16.34816 | -52.94065 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0f93166-7954-36e6-bf4f-7171958472ee | -15.23781 | -52.35485 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b881f1d-7488-3c4d-b50d-a5fc26e6bbff | -16.29467 | -49.556 | 2025-09-08 05:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f85ea18f-a087-3b04-8d8a-b68fb58ff615 | -15.75692 | -56.4252 | 2025-09-08 05:23:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62496ad8-dab3-3f38-88f9-168f97e7cac0 | -15.19241 | -47.98347 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7005177b-9358-30aa-b36b-c0c81128ab91 | -15.19219 | -47.96626 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e5ad965-6d3a-304d-92b1-155c50b8a03d | -14.80226 | -48.23594 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 126f7680-7097-3d89-959a-f1ced382477d | -14.4585 | -56.80982 | 2025-09-08 05:23:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cffe34ed-1ecc-363e-89d6-59b613c072e3 | -12.42498 | -63.89348 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4b1b9f-e485-31e9-9721-d2ac03d010bc | -15.85179 | -52.31262 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9673f177-42c6-3da0-ad1b-7817b2460b77 | -15.09551 | -50.11266 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95082d9f-9718-3f34-a188-02204eb7b5ca | -14.59407 | -52.12478 | 2025-09-08 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c8248c5-7642-3072-b7eb-7d0cf04a1c2c | -16.33885 | -52.93372 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a7eae34-9f83-3745-b8b3-1fd6ab7fcafe | -15.83635 | -52.26605 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff919554-e25c-3b4f-8e2d-2510fc31ecfd | -14.881 | -55.83058 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 459103dc-a862-3130-a52e-24a75137f5fe | -14.08432 | -46.60568 | 2025-09-08 05:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51da04b9-0a9e-3b90-8017-246071de9d1a | -15.82923 | -52.28189 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90d8f2e-9677-3896-ad37-1f67acbf624f | -15.00116 | -48.00982 | 2025-09-08 05:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec53cefd-853c-3b40-8bdd-e3433436471b | -15.19299 | -47.97765 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c0b6a49b-13ca-359f-ac3f-e48cee6d24eb | -15.82603 | -52.26448 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea61c290-b3da-3543-ba41-3f2b7c91a870 | -14.51276 | -48.80402 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6541135-5e16-3659-95d9-b77661267757 | -15.7414 | -53.53266 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a7f3b77-f1a6-334a-b0dd-5d48534eecac | -15.27053 | -52.3847 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f729888e-2bd8-308a-980c-bad29c9ef312 | -16.33953 | -52.92783 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aa729a3-3af2-3622-b743-b5c8e252c835 | -15.25297 | -53.81807 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d5752ae-4640-30db-855b-ec41fbdd3dc6 | -14.70026 | -55.91592 | 2025-09-08 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c819e2a-6a53-3ad8-98bb-ef37411c1db2 | -12.42129 | -63.89282 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de1b498e-2caf-3ee2-a00f-a63c978805c3 | -18.02087 | -47.11411 | 2025-09-08 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 15f4cdc3-febe-3bc2-877d-31938f3ea449 | -15.26503 | -52.38745 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb5714b1-b87c-3fa6-92cb-3e37773de403 | -11.90729 | -64.97021 | 2025-09-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5191536-8dd5-34f0-8dc7-693fd376ebdc | -16.44413 | -49.28694 | 2025-09-08 05:23:00 | NPP-375D | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| decc3312-9939-3982-b16b-c2c94a20c3db | -15.25099 | -53.82566 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 120e25b9-f1e9-3e61-ab8f-bfca403e9fd1 | -20.95694 | -48.46083 | 2025-09-08 05:23:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7793902a-1c5b-32e0-9360-24ffd3982750 | -15.07285 | -50.10117 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 074e931e-a796-3749-a1c8-9fba40bd143c | -15.73224 | -53.56873 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e5d5fe2-1018-3908-a462-8662c85eeccf | -15.08961 | -50.112 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db51a5c7-d870-3b2b-9fd7-6ea3dea54427 | -16.43778 | -49.28663 | 2025-09-08 05:23:00 | NPP-375D | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e44c4555-4008-388c-99e5-97d755876925 | -15.82991 | -52.27612 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7444702-2490-3cd6-9d38-7742ab6005c9 | -14.51222 | -48.80896 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad6fac8b-caf3-310d-9966-7b9c3aff859a | -18.02188 | -47.10211 | 2025-09-08 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84a15db6-d93d-3cc9-a9b7-c09ee252d2f7 | -15.66448 | -53.86709 | 2025-09-08 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41fc34a4-d8dc-3e14-a1a0-49eecf09710d | -11.90061 | -64.98509 | 2025-09-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c297a5da-8176-36a8-ba97-4525d3e58cc8 | -15.75367 | -53.55074 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cb08975-b7e5-3f8b-80bf-694350dbd95b | -15.0738 | -50.10817 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5aea1ba6-4bd0-3283-9b21-43d68f3c08a2 | -14.99514 | -48.00227 | 2025-09-08 05:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd4f1cb-9d8b-3cbd-831c-1da1a7a9414c | -14.58899 | -48.08166 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 680215b0-a706-3eeb-8ac7-27aaeb3f6a20 | -16.34749 | -52.94636 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35f522a2-6eae-34c0-a4b5-383826ea8a7e | -15.50293 | -52.76906 | 2025-09-08 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c19b9a63-3ad5-3028-bb2e-d3e8aee2a97d | -11.89971 | -64.99026 | 2025-09-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64285b97-6ab0-3187-8ce8-9d37a6fe9c8a | -14.34918 | -60.31372 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5ea5baf-54f2-37cf-9514-78181a7d1ffb | -16.32893 | -52.93206 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00c40431-d422-37b7-8589-3fdd4e3a1d93 | -19.53129 | -47.89117 | 2025-09-08 05:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46c01f0c-7ab8-35bd-9280-af557550f248 | -15.07431 | -50.1037 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77c0bde5-d442-3d48-9bc1-1464cf8d3704 | -12.35621 | -63.63868 | 2025-09-08 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
