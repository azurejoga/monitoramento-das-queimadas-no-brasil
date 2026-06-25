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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f89fa72-4f96-307c-aa8d-f16eb858f79c | -11.63712 | -52.8642 | 2026-06-25 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b22e9c8-0b8f-30b9-a7f8-208208a4210e | -10.47581 | -54.56607 | 2026-06-25 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec99f11f-935b-31ab-825b-d37f5e6e197e | -12.21683 | -55.49874 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde45152-e3d7-3df7-aecd-29f483bfde3c | -11.64164 | -52.85997 | 2026-06-25 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c08944d-ae81-3d3f-96d6-daff589ca98d | -10.12614 | -52.10808 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68429cb9-cb15-3bd7-be2e-0378c4b5dca7 | -10.90576 | -54.13495 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1c419ae-705c-3d1e-aa73-3ef3f1479c43 | -10.36595 | -47.34103 | 2026-06-25 05:10:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66b10a88-37a8-384e-b709-27dc954e1154 | -9.79017 | -56.94536 | 2026-06-25 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22cf42f2-5230-368a-ae54-519a824aaea3 | -10.38273 | -56.72298 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b32f4c22-046e-3271-b010-92ed235af545 | -12.74438 | -44.46981 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51e1ed59-1745-3ed7-9ab8-ad76ebf461a8 | -13.83143 | -47.02147 | 2026-06-25 05:10:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 972cd2df-d8d4-3b9f-8867-7d2217ba1b26 | -12.55377 | -54.59087 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c109cb1-20a4-3ce9-80ad-aa88776a0333 | -12.83506 | -44.35421 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bea259b7-c99d-35aa-af66-80da161d25ee | -11.57749 | -54.71227 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe0b06b-4c1f-3dd2-b2bb-78f26c4a68d4 | -10.57988 | -57.32109 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 295ed093-7831-33ef-9e90-beab593daf3a | -12.21997 | -55.50666 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3290fedd-04b8-3224-a5d7-a3cfc82929e9 | -11.24809 | -43.32727 | 2026-06-25 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0399d0f6-9112-3543-aa5f-03735f4501e9 | -13.19897 | -48.32034 | 2026-06-25 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 320d7060-0242-3cbd-a09d-1775f0bf195e | -10.90637 | -54.13094 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05492889-3b44-341c-bac5-8d973f14e54b | -11.86824 | -51.75436 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1934ed82-f8ef-30af-a699-ecb2de0ed021 | -12.2256 | -55.49236 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0805a64d-923e-33b5-be7b-276163bdc940 | -10.39607 | -56.76807 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9713a294-f3d1-3aac-959a-a03684ed77f7 | -12.2174 | -55.49504 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e86a1cc-bc84-31af-afe9-ead95b4ceba4 | -12.31324 | -46.7397 | 2026-06-25 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b16eb30-2ba4-341a-b2f5-28047eb03775 | -11.88004 | -51.75978 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1a79654-ed34-361c-8ea0-5e6027fe3a36 | -11.79064 | -56.99378 | 2026-06-25 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 885f0e5a-01b0-3f19-acf3-e8d1f35e1e8b | -11.87593 | -51.75919 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a7a72b8-1106-3980-bfd5-9444161618e3 | -11.94324 | -57.70045 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c3b1db5-9538-3040-b83c-b77e6e306ccd | -11.50568 | -54.50103 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5a26fa-e578-3ebe-8248-2a4bfe6f850d | -10.1254 | -52.11155 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49526fd1-708a-3829-93c3-c71e396ef3bd | -11.94268 | -57.70398 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89707ec2-bfe2-3f9e-a55f-e732f78102ac | -13.07219 | -53.35381 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6047d4ac-f205-3a96-bcff-ba9af81ee2fb | -11.87235 | -51.75494 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 40edc4f6-c449-3ece-a363-a38c510d9dc6 | -11.2535 | -43.32631 | 2026-06-25 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 94eeb935-4f3b-3bbf-9ea7-dbc9b0bb5c14 | -10.37138 | -47.34171 | 2026-06-25 05:10:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e901bf84-f9a6-3785-97f3-12be45d10b77 | -12.5579 | -54.58737 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92fa751c-ef02-31f0-ab14-85ceb293012c | -10.12931 | -52.11213 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26effe14-abfb-3db3-b5b1-dd5c6e394bd8 | -12.22732 | -55.50402 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39f96d54-32cf-365b-8c92-16458be98839 | -11.49622 | -52.92773 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd66024b-46c2-3ba7-a0a0-6cb4adc7a14c | -10.12934 | -52.11368 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c97210c-05ef-31b6-9362-05c01afe2798 | -10.16028 | -56.62608 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc21ee2c-98e1-311e-8c42-b75e10dc67c5 | -11.30683 | -54.47684 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4829e27-db9d-303a-ab4f-83ea9dd2e852 | -12.67473 | -54.57981 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84f6076f-04ad-340f-952d-a308e6b6a7d8 | -11.57933 | -54.7117 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71866847-c03f-3201-80a1-5b6ae126ae2d | -11.49691 | -52.92303 | 2026-06-25 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc346c1e-cd0d-3776-ae99-3525916e9b4c | -10.12543 | -52.1131 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05fe43fd-1138-343a-a7b8-9613d1b22c5c | -11.25511 | -43.32824 | 2026-06-25 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 37f0fc7c-a6a5-3ab8-a2fa-480c9e3f597c | -10.772 | -54.11172 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41d7e772-3ef3-3a57-9196-9e2915129fde | -12.22053 | -55.50295 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 563ab96b-a6d0-307e-aaa0-0bc212243b96 | -10.38715 | -56.71653 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49a3b0d9-08ed-3812-af39-376565958927 | -12.22022 | -55.49929 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ed138b2-78d6-3f76-9bf7-3415e09f690b | -12.21569 | -55.50616 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a26f0df3-6bca-3d09-a00e-fd69b27d9d44 | -10.77554 | -54.11227 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cbd0e96-ef8a-33a5-be5b-9bede4395edc | -10.93607 | -56.85553 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 479c97eb-87eb-3843-b44f-b7ce97a95991 | -10.61802 | -47.12198 | 2026-06-25 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53d668dd-64e5-337d-be28-9a18295ca06d | -11.58096 | -54.71281 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623e4abb-a556-3d6f-b946-08b88fc8af46 | -12.22504 | -55.49607 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d08b69-23c4-3af3-ac16-1e0a1e07e586 | -12.13943 | -48.26028 | 2026-06-25 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28acd3bc-42f0-352c-842c-1f8892ad096b | -11.94211 | -57.7075 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf487b7-c739-33c7-a6e8-9a3583c4f58a | -10.9367 | -54.09689 | 2026-06-25 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0e17e54d-df01-314a-a42c-d05fade25298 | -12.54882 | -57.20374 | 2026-06-25 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf3485b-3cd1-31f1-9d0e-e05b1e893d71 | -13.0353 | -49.93689 | 2026-06-25 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27f1eebc-3d08-3e92-a03c-18b28774baa1 | -11.36274 | -55.81915 | 2026-06-25 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91e07c22-d907-31f4-9aa0-ed0965b4637f | -12.74504 | -44.46384 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c83214ef-5fad-3b7b-bb5e-c2afe6facd70 | -12.84179 | -44.35509 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64248b54-8f09-3fbf-82f6-5039f0903956 | -11.2017 | -49.41852 | 2026-06-25 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d95385ce-3785-3da8-9be2-ec9f7d6555f6 | -9.49294 | -57.31712 | 2026-06-25 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e66585-6bba-3255-aed1-f9c6dbdab193 | -11.88107 | -51.75246 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 05010a85-a896-3589-b0da-d22174ea291d | -12.84527 | -44.35942 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03eb3ae5-c300-3ef2-928a-33e40254d9b7 | -12.75173 | -44.46463 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7537b75-2325-3065-b551-21f3dc2756fd | -11.90953 | -43.40504 | 2026-06-25 05:10:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2121735f-eeda-3b69-abea-01c21b976952 | -12.21966 | -55.50299 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f23985-ad23-3640-9b6d-ca16df6bb16f | -12.7457 | -44.45784 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f352dc58-9e86-3347-baa2-79b1e8bc747a | -10.93938 | -56.85606 | 2026-06-25 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6bfe3e1-229b-3753-8ca7-6e1631fcd7f7 | -10.61715 | -47.17312 | 2026-06-25 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f73df0e1-5968-33ff-972f-9ebdce5cac0c | -10.38329 | -56.71949 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db58765e-0cb4-3155-93af-ab1beb19a887 | -12.73834 | -44.46302 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 12692fb0-3a4f-33d4-bb08-5fb1891140c0 | -10.39772 | -56.7576 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bb0179c1-69d2-39d0-80e8-a41934a0352b | -11.28325 | -53.94898 | 2026-06-25 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10881f46-684d-3073-8488-3d3450db5e25 | -12.22448 | -55.49978 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fe635b3-f678-3673-85a7-37bd34a03457 | -9.88298 | -52.43772 | 2026-06-25 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13d01417-7ae0-3fc3-aa0f-a9a1636436b9 | -10.40103 | -56.75814 | 2026-06-25 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 56c68fe8-9e46-3b39-a611-3ea1d58ac29e | -12.83441 | -44.36024 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b497e41-0ee2-37ee-b480-9ef62dc27f31 | -12.55497 | -54.58283 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b6444e-25e5-33cb-b39b-eb8c5b82e274 | -10.53233 | -48.15938 | 2026-06-25 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d97f68aa-410d-3a5e-a8a8-005aa6cc46e8 | -12.55317 | -54.5949 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 759e9029-80b5-31a8-85d8-b057458de47e | -12.13866 | -48.26665 | 2026-06-25 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 261dc185-c414-3114-ab99-332f6b15fd6a | -14.21672 | -45.63535 | 2026-06-25 05:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a6a42ce-adb2-3278-934c-08c2f336bdec | -12.6712 | -54.57928 | 2026-06-25 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e28df965-7fad-3410-a29e-1931d3c4378b | -13.66469 | -53.91571 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4284f71c-53d1-31f3-9b39-8dba689459de | -13.06397 | -53.35734 | 2026-06-25 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 652c5f3c-3f65-382d-92c1-d448138c465d | -11.78852 | -57.34976 | 2026-06-25 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d89ce47b-a144-37d7-8893-5289bece3c30 | -12.22109 | -55.49924 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbdc0269-7482-347a-b356-8b77fd61c993 | -11.36664 | -55.81608 | 2026-06-25 05:10:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dac09fa-9cfc-3b01-80ba-cf8445926cd7 | -12.13841 | -48.26238 | 2026-06-25 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cc8203c6-9345-368f-b587-32596870271a | -10.61672 | -47.17654 | 2026-06-25 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9671d6d-977a-31ac-82f0-7768061fa67f | -11.86927 | -51.74703 | 2026-06-25 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 17e89deb-f6b4-3576-a41d-ef840de5cfb1 | -11.58656 | -47.44436 | 2026-06-25 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58c33244-1bd8-314c-b08a-062c0962804b | -12.83853 | -44.3586 | 2026-06-25 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f05bf67-2351-3d06-a875-7ab7e6c4b7b1 | -12.22392 | -55.50349 | 2026-06-25 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
