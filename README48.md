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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0e6854b-6d5b-30c4-a78a-4786b420e426 | -12.55956 | -46.96716 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 8dc2673d-dbee-3b39-8c12-b8ee40098e11 | -13.56563 | -46.9574 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 942100c3-090b-39fa-aabb-37e18e17ab52 | -9.3935 | -60.54747 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb0b699-5849-3591-b6a1-ca53ab75d440 | -12.56362 | -46.96382 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33008760-d808-38ca-92ec-7938473d7d1b | -12.47179 | -44.68932 | 2025-08-16 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd691341-6651-3dbc-b948-981037437579 | -13.11926 | -57.1378 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97a2a08a-cb7b-3c0d-a2ea-9f7ba488cdf1 | -11.65633 | -51.62293 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2d1f00-1b06-3d0b-b256-5848a23f2c6b | -11.07415 | -48.36106 | 2025-08-16 04:34:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e339677-0c03-3ae1-bffe-90512567b4d0 | -12.82704 | -46.0195 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f4de40a-e441-39d9-b5ff-b022d825834a | -12.56477 | -46.95613 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05d864ee-f0b7-3a43-a4bc-7ae3af6a3e7f | -18.12136 | -44.99886 | 2025-08-16 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc7cd36c-334d-328d-b421-b4c729b9c175 | -13.61598 | -46.90828 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| eee246a7-c2df-3b60-8d95-d3ff959f9b15 | -14.5347 | -48.5808 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89defbed-786d-350e-96e3-7ad3a6c0da49 | -10.8618 | -48.48292 | 2025-08-16 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e48033e-6c5b-3a0a-abb4-66b39178c7df | -8.66414 | -62.46039 | 2025-08-16 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 950d89d6-19f4-312a-85cd-f3c7fd1dcf73 | -12.48837 | -47.50848 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 088d4028-dee7-37ec-9a77-bfa162a032f9 | -13.41626 | -57.03268 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e1e85d7-b0c4-3337-a9cd-291485cf90a4 | -12.6052 | -46.9572 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bae02c06-3aad-3de9-b9e9-b1ae1bd53c32 | -8.97865 | -60.50406 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 02a5849c-331e-3d44-8e18-715d308ab7a2 | -14.95485 | -54.73533 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0c1bf54c-65e8-33cb-9b1d-f7b6b4430c0d | -12.80553 | -45.98653 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 998f68d4-b556-3122-aaba-b8d560e4888d | -11.25914 | -50.4732 | 2025-08-16 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 16f4fafc-5414-3a95-aac6-5ff61306193f | -8.97798 | -60.54139 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc6328b7-175b-3f31-b8d4-31a830f5f781 | -12.1336 | -54.66803 | 2025-08-16 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265c29d3-402b-3c5e-b9a7-206a38d5483b | -17.21577 | -49.59251 | 2025-08-16 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a0dabe5-cb7c-3ccb-8113-cf60ae0a46a2 | -12.53173 | -46.96279 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78cb71e6-704e-38df-bba5-70a0e3190bdb | -12.29839 | -50.01077 | 2025-08-16 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6ebc514-822e-390a-8687-5be850d1a733 | -15.18172 | -53.85093 | 2025-08-16 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0074cafb-2068-3d82-aa47-66c8b8fafbfb | -17.61045 | -46.68604 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| deec700f-14c3-3f09-96c7-43f0c6da68af | -12.55836 | -46.95136 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5a0eb1a3-485e-38c1-af17-484b8a5b56ba | -13.25071 | -50.13124 | 2025-08-16 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42a9d666-15ca-3eb4-8357-00f7afd60e25 | -13.13897 | -57.16383 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88128c55-5eb7-3a3b-8e14-66eb782a8a33 | -12.79712 | -45.96734 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a43134b-cb4c-3aa5-a0e0-16d34469b481 | -8.98129 | -60.55823 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e102cf51-fc9c-3cca-8603-0ddbf9af061b | -17.86947 | -46.14356 | 2025-08-16 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95cc3e54-53b8-3b74-8775-b9970db40a8a | -7.94907 | -61.75833 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b67fb79-881b-32e4-9697-a20c32802e8a | -15.62319 | -49.27172 | 2025-08-16 04:34:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c43995fb-bbad-3e13-bd91-a24e04cf94de | -10.00982 | -59.22044 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef37ff3c-c92b-36d6-a48a-b377201f9de9 | -12.56652 | -46.96824 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bcf8c2d-df76-3f4e-8d47-a08c24260a13 | -16.81395 | -49.35869 | 2025-08-16 04:34:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e83f0491-a417-31b0-8728-59be25302cee | -13.61893 | -46.91275 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd072886-4d31-31b7-ad4d-33d767f97faa | -11.72713 | -47.56398 | 2025-08-16 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e610ea7-86b1-374f-9ee9-c4051ee5e070 | -12.62775 | -45.23717 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5083dc14-bdfc-3b92-a0e8-bacdba71fef3 | -16.78221 | -44.7552 | 2025-08-16 04:34:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78a3d78a-51ec-36a5-9bc1-b099c8fbd36e | -16.24381 | -51.12935 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1ab2b35-da33-3cae-b574-8cc4cf0c2952 | -9.50007 | -60.51974 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7b7a137-4512-3c6b-bd7c-1ee58b05fe5b | -9.21679 | -59.66662 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45db4785-b3bb-3dfd-bbf7-297af52f70c2 | -8.99322 | -60.49642 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e85e99dd-00f1-3035-b7d5-073d0fe951e9 | -13.56505 | -46.96141 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2359ee31-c92a-399a-b3b9-75072540611f | -15.89269 | -48.31917 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12257c58-c2c0-357b-ad86-383261cd8764 | -14.52913 | -48.59486 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d1bf92a-1736-3422-93a1-e24bb6b1a87d | -12.60456 | -46.93734 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f4d8d65e-ebe1-3e59-a233-ce8ec904c4b0 | -13.87177 | -45.55376 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe0d26e2-5716-3c58-827c-c64ff511f072 | -12.56769 | -46.96045 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f9b2565-f5db-330d-9440-23185b98d61c | -15.89334 | -48.40827 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34651be3-958d-3bf6-9343-898ecc7e83fd | -11.35542 | -55.42376 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 323f60c2-3dac-33e9-b7e9-4df0212b43ef | -12.59826 | -46.98016 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b55d9e-cd41-3f82-b78f-ed64c2fdfcce | -12.84095 | -46.05257 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364b3064-72b2-3ca4-bfa9-8f53420ca182 | -12.83855 | -46.04334 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cc1699d-e9a7-3677-b0b5-61d31baa472a | -11.35387 | -55.43242 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 515693f4-cc0b-34f7-b259-6ee036de81aa | -14.94698 | -54.73399 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| f229d12f-4cc2-3536-8bc0-00f5c90a1cd1 | -15.88993 | -48.40774 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9095013-72f3-3936-b0d3-6885b218bd61 | -17.60362 | -46.68028 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b33e493d-47df-31b4-8dfb-b10d56a247d5 | -22.77653 | -49.15748 | 2025-08-16 04:36:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 357f7629-8487-3985-83d3-0208fb2f2b24 | -19.64346 | -46.09637 | 2025-08-16 04:36:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8457e282-fe00-3d1a-800e-127542d1e240 | -20.15222 | -48.91805 | 2025-08-16 04:36:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea6d96e0-f110-3f60-8352-312c679e38bc | -19.53179 | -43.62833 | 2025-08-16 04:36:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74e0cbf6-703f-39e2-ac05-2d4c215a3307 | -22.53919 | -46.89032 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b081139-1cc1-35a9-a484-3092cd26ed29 | -20.39786 | -46.49242 | 2025-08-16 04:36:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd1356ae-bcb0-3540-bfaa-0dfd65f477e1 | -23.14406 | -47.08647 | 2025-08-16 04:36:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8a4f0b8-6cd1-3ac3-a011-c4a193b5e3f6 | -20.39325 | -46.49725 | 2025-08-16 04:36:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3db901de-a204-3bb4-bcde-d1ac4ba00112 | -19.53229 | -43.62403 | 2025-08-16 04:36:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff2b645b-b215-36c4-93f0-50b7c0ef4b2b | -21.12328 | -56.15211 | 2025-08-16 04:36:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb7db247-989f-320f-b139-e7f38ab1f80c | -20.39684 | -46.56031 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d4e23aa-1b3b-3360-8768-678803f55a88 | -20.46162 | -46.20785 | 2025-08-16 04:36:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 983f8aed-420b-368a-b2bd-39440befc42c | -20.07804 | -49.42516 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3505db5a-e9b0-3d80-84ae-f16a9d171db9 | -20.41979 | -46.53675 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee7d5c68-a66f-332c-9f08-4700bf5206ab | -20.08144 | -49.42573 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| ca6664d5-1fba-3444-8ff2-8ae428646047 | -19.53642 | -43.62895 | 2025-08-16 04:36:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3e6bbed-f5ad-32ee-8c2e-7683dacaf0ee | -20.08484 | -49.4263 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 7d0aeaba-d6ea-387e-8300-6fe716e5d0c0 | -20.41943 | -46.54347 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63df76bf-cee7-3e66-8199-01c8db02339a | -20.4628 | -46.21223 | 2025-08-16 04:36:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d757348-6e60-3ab3-a938-cb49b7b651da | -22.53576 | -46.8883 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0c812dbd-c122-331b-900a-0dc3fdda7009 | -20.08201 | -49.42188 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| b3201a50-3541-3abb-806c-0b7bf566c901 | -20.41912 | -46.54181 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce14dfb8-0e54-31d0-a27b-ba5c5b95b072 | -21.06549 | -50.30288 | 2025-08-16 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6376104a-f9a2-381f-bb2a-779f1a90dce0 | -20.0854 | -49.42245 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| bfdeb613-f2ad-34a5-a3f4-2ec222104a14 | -20.0519 | -44.63105 | 2025-08-16 04:36:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6c834b1-dcfc-3079-b4a5-14f4ffad00d5 | -21.06492 | -50.30666 | 2025-08-16 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67a42152-347e-3f2e-92fc-ac82d906cd2c | -23.18029 | -46.75554 | 2025-08-16 04:36:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8130e88d-1b4b-3d8b-884b-d72feba0f4d3 | -20.66695 | -49.3907 | 2025-08-16 04:36:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fab7e21-7684-3a61-96b3-61b1a7e8d6e0 | -19.29773 | -46.21269 | 2025-08-16 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa1e779d-55b2-3423-a823-d6063e289db6 | -20.40662 | -46.54627 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131d8d3d-6ae1-3541-8f27-4a194b66b7dd | -18.46107 | -54.06902 | 2025-08-16 04:36:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fcedf78-7aca-31eb-a8f6-c2b93735ef13 | -20.42008 | -46.53835 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fcbb84f7-e225-36c7-a6d2-e8d7f215c8b0 | -20.40268 | -46.54612 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c483bdba-9cea-3644-adce-7be75b27f710 | -22.53592 | -46.88445 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3551a3be-f00d-3649-8894-802e78ee908d | -18.48124 | -50.42849 | 2025-08-16 04:36:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50129526-2542-33aa-a1ce-2ed2be13440c | -23.69755 | -51.78122 | 2025-08-16 04:36:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1324e22c-3350-3989-84a0-ca2dd89338f1 | -20.42044 | -46.53186 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README49.md)
