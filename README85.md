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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25db8128-cbb4-393f-a4c4-cdca2a2b48d2 | -14.31268 | -46.51984 | 2025-10-28 05:06:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e15bfa30-305c-3ad3-bddd-250caa73b77e | -14.76773 | -44.96964 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 707d8024-9410-3c31-a5bf-c256fbf37dd0 | -14.41067 | -47.91917 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1dbe6eb-fb5b-385b-a50d-9ed16e51dca1 | -13.737 | -48.41928 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d30398b5-b496-3738-a67c-25002212cf30 | -14.30715 | -46.51534 | 2025-10-28 05:06:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89693ab3-c091-37a3-ac39-52be387d2abd | -14.54816 | -47.98351 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b145720d-b7ed-394f-8b38-5626b00a1a69 | -13.87334 | -48.48767 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4ddd5ba-ccf4-32a6-a2e0-93afdde295f0 | -14.76304 | -44.9609 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40b92f4-8f90-3fa6-a752-20ad8a4541a4 | -14.42548 | -49.42678 | 2025-10-28 05:06:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e35d9e9a-9776-36d0-9f4c-e1058f5cdcc0 | -14.54045 | -48.00181 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662364cc-f03d-32ff-be14-2adf40ff05ce | -14.53749 | -47.98075 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 319876a1-9260-36ca-adf9-468aa76340e3 | -15.20695 | -47.21753 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8460356e-9f06-318a-ba08-9fda7a7995a9 | -18.78688 | -44.3375 | 2025-10-28 05:06:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a793036-4e93-3f01-b397-d1b65db43be9 | -14.81492 | -46.71375 | 2025-10-28 05:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a4f0e6e-a3f0-352b-a782-d1443d935de1 | -14.47702 | -47.9329 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdaabac9-e450-3b62-99e7-faf187003d7a | -13.87804 | -48.49244 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e771130-9f00-3f69-9969-227f37a25bba | -13.73511 | -48.43443 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7beb391c-d0be-3dc0-85be-fcee8c67774d | -14.5314 | -48.00094 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2575791-213a-38ec-b078-726ba12725aa | -14.65987 | -48.42033 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f90f9341-b42d-3352-93f6-c275ad94cf82 | -18.78216 | -44.34319 | 2025-10-28 05:06:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 397c289f-5066-3683-b7ff-3efac0a581ff | -14.56384 | -48.0056 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b2784b2-87dc-3afd-8aa9-0208dc1528e4 | -14.53223 | -47.97877 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d4d8e50-e391-3238-aa4e-9858629392f8 | -15.17093 | -47.22732 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1278f39d-5aa2-3e23-ac60-4ce881d99a77 | -14.62621 | -48.43333 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c129a1ba-d7ac-3416-816d-cacbb3f93920 | -14.72864 | -47.36392 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b75babb-8f1c-3b83-8f9b-30b0e9adb519 | -14.3131 | -46.51603 | 2025-10-28 05:06:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 634e348d-04e8-352b-8c49-f7a3839a5993 | -14.80902 | -46.71294 | 2025-10-28 05:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab6ec46d-34a2-39b7-84bc-2fad3d5e6def | -13.79136 | -48.50248 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d1c68a0-cac8-3d32-a52f-ee689b05294a | -15.16401 | -47.22406 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9256b309-0874-3ba6-a116-5a40ceda97f6 | -14.41844 | -47.85373 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3f10e89-fac7-30d0-8b6c-e69f9bdcffa7 | -13.73819 | -48.41727 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b04e36d3-3db2-3896-8491-b37f1cd9714d | -14.52978 | -47.99907 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3508822-35c3-35e0-9abe-5931754edd12 | -13.88741 | -48.50224 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6618c43-9716-3376-81fb-834eebd3d3f3 | -17.3771 | -45.35955 | 2025-10-28 05:06:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad94cd74-3625-3786-b10a-169597287cbb | -14.72911 | -47.35994 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac41b22e-6b93-3832-8551-8de51eb301fe | -13.72105 | -51.46156 | 2025-10-28 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc9892f-bbf7-3b74-a72d-7dbc213e99aa | -14.66025 | -48.41711 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd8f6ff7-f33e-3b4c-b811-71017358c269 | -14.54236 | -47.98602 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd629fd2-0b33-3669-83de-aa79009c13c2 | -15.20071 | -47.22129 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2d9e9dc-1ee1-3ef7-8473-5df488cc6ac1 | -14.41108 | -47.91571 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c00d2813-d920-3839-b69b-1613a25fd098 | -14.81542 | -46.7091 | 2025-10-28 05:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cefef384-c09f-3979-8b98-8385d141781e | -14.53672 | -48.00248 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a4644d9-a21b-30cb-b14a-da5628091656 | -13.91542 | -48.48906 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ec75bc7-4a4c-32c8-960c-dda9d7852971 | -14.53095 | -47.98941 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99cbcf86-3b05-38e4-8bda-01d5713ab273 | -14.76232 | -44.95721 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c40169e6-d694-3948-b144-8cc96f784b18 | -13.73604 | -48.43558 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 884be6f4-7d32-3b64-b828-876c033ad7ee | -13.86418 | -48.5201 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c4edb2d-1eec-3499-89fa-fef01c6096eb | -15.15647 | -46.60118 | 2025-10-28 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b15b4255-c5b9-3574-b3a9-45146100986b | -14.53284 | -47.9882 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cba669c-da34-31ed-b6fe-0df6bd495148 | -14.62254 | -48.41899 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca90e31c-a813-3d84-9133-9666c777171c | -15.20732 | -47.21421 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa28ef0-31ad-3bfd-8ec6-d172e57d1b7a | -15.14998 | -46.60526 | 2025-10-28 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74c2ffd1-e907-307a-80df-47461fc6e299 | -15.23066 | -47.9486 | 2025-10-28 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc626a0b-88a8-3efa-94ec-9d599a8fe7ca | -13.88286 | -48.49625 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 789d6488-3815-32fe-9692-b802ac46cee6 | -14.72298 | -47.36324 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10eb67be-cb90-37c5-96ad-3bec1036fca5 | -13.73547 | -48.43154 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63e5e0b6-305b-3f61-92b2-bab00c1e62ec | -13.72529 | -51.46215 | 2025-10-28 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 249855ec-7c4e-36c9-9229-e35c6ad3d4bc | -13.8645 | -48.51744 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71cb09fc-6e7b-303f-ab45-1fa12e6e71a8 | -14.53056 | -47.99263 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c6fa4fb-4045-3f45-b799-9a22334216a7 | -14.53706 | -47.99954 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc2250df-a5b2-3c55-b0ea-52869393eb1c | -15.156 | -46.60551 | 2025-10-28 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e99fa08b-7467-3a30-8442-bfc651a81ca6 | -14.4166 | -47.86923 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d8070b-b137-3da4-8e01-f8640e722049 | -13.85901 | -48.51926 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd8a20ee-c0be-3b5b-a4c9-c33f42447219 | -15.15549 | -46.61018 | 2025-10-28 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15fbfef6-aaf4-36f1-9763-562041c586c8 | -13.87763 | -48.49587 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 115b3029-eeae-330c-95eb-5af83b5eb58a | -14.49762 | -47.8983 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afab046b-55f3-3694-abec-7cf7c88a9202 | -14.75646 | -44.96023 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 679cdb5a-2c64-3299-8ae1-11285d92c5d4 | -14.53135 | -47.98603 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 663e450f-91b9-3996-83ad-fc54760342f6 | -13.73745 | -48.42365 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f4183ad-8916-3fa2-a345-fd2033fa546d | -13.85933 | -48.51659 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55eac04d-5e10-3b6a-b748-8cc3853fd926 | -14.769 | -44.96741 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19b0b958-98aa-3abb-8d86-53d805e6d862 | -13.87727 | -48.4989 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b4c6baa-cae6-33ec-8d7e-44435b6c0d77 | -14.5443 | -47.98423 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79aa2813-e82c-34fa-bc9d-fe195054d3f9 | -18.78632 | -44.34471 | 2025-10-28 05:06:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46fecc82-3f70-3be1-9d4a-dab41ed069b8 | -14.41763 | -47.86051 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef18219b-8ece-39d6-ac17-fd0793a83894 | -14.75574 | -44.95653 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d3f0d8a-f69d-334f-8cf5-2a7cbdbb4d2e | -14.73207 | -47.36019 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46ea08ae-e49c-3be3-9b8b-130008b1e986 | -14.76242 | -44.96667 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bd5f943-672e-325a-9809-4336136915f4 | -14.56072 | -47.98499 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45145b46-d598-3579-9bb2-f288213e1538 | -13.73638 | -48.43267 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea8378be-d2fc-3164-b1c3-69a5a003982a | -13.73741 | -48.41604 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc443d3f-437f-371b-b2c7-91cfa9bd5d57 | -13.93966 | -48.42128 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26dd51b2-f063-3aa8-a6e4-61e43ee71923 | -14.53248 | -47.99142 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22919d26-2bb1-3973-a5b6-b5b53b2d8b3d | -14.50368 | -47.89383 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72cec223-e4a3-3a4a-9163-90b5ae6dec7b | -14.62659 | -48.43007 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2cc3085-457b-32f7-bd28-8f79fcebb115 | -14.76173 | -44.9631 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84838edf-d0e2-346d-a43a-3ddca5bfbfd8 | -14.72641 | -47.3595 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dd086ec-ebe7-3c46-a242-f93c19b79b69 | -14.62291 | -48.41582 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ceabac1-d4b8-37c2-b1e6-799b76a35523 | -15.23028 | -47.95194 | 2025-10-28 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ca94ea-2597-3f33-91d8-df9d413d69f4 | -15.1692 | -47.22946 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 176fda5d-1f94-36ff-b99b-5ac008c2f695 | -14.54472 | -47.98054 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e1cc80-6893-3090-976e-766c7f9b9b9e | -14.56958 | -48.00356 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5f1690-6f04-3149-a2e7-5bad60e4d929 | -13.73672 | -48.42981 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 913a67d6-4355-3cd8-a056-ed48126c7f9f | -15.23106 | -47.94513 | 2025-10-28 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46148811-3a12-3cb6-a3ad-4b31433fe82f | -14.56034 | -47.98822 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 550991d4-9996-3f62-8ac0-5388b2c7b53d | -17.37507 | -45.36011 | 2025-10-28 05:06:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce9b38d4-dcba-36c0-bebf-441ab00d0024 | -13.73708 | -48.42674 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df102fb0-92db-33d9-a7ec-801527127061 | -14.43013 | -47.84867 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a62b9e7-c85d-31fd-b9e9-d00f7fed82df | -15.1652 | -47.22651 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2026fe97-7484-35f3-a5b0-84c8ed313dfb | -14.55009 | -47.98172 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README86.md)
