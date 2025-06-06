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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 334c6331-906b-3bd6-b689-5d17023d3152 | -12.95956 | -46.78242 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 121b16be-c818-3577-bb34-272be48392e4 | -12.96704 | -46.77977 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d65c4f7-c658-3169-8d1a-669d5b31b646 | -11.68664 | -54.55761 | 2025-06-06 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d4a27ec-154b-3591-8434-6419c54b4383 | -10.49673 | -53.65715 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7652dfa8-94f7-3dab-8aa3-7f1e43b8fca6 | -10.49539 | -53.66414 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 262b9138-14e6-3ede-9499-467fa7ec9ada | -13.88825 | -54.68175 | 2025-06-06 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2e0ff75-b69d-3d25-b77f-795a9a1ce46a | -14.736 | -45.09065 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd001beb-786d-3fcd-bd1a-b4a7b01dab87 | -13.08156 | -49.24223 | 2025-06-06 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ff14c32-deab-3151-8057-f6fb91f28209 | -13.64539 | -44.44764 | 2025-06-06 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e089df59-8c86-38e3-b835-1eb9c4335c34 | -13.07596 | -49.2515 | 2025-06-06 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcc2668-3a92-3866-ba25-2e01b5b849c1 | -14.12626 | -44.83425 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 806648fb-7a1f-3e28-9150-a8b1a34747ea | -14.0261 | -55.13219 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8014e081-a037-39b6-8e4b-59cf92244863 | -11.37863 | -54.35066 | 2025-06-06 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4960a948-8e50-3d53-9097-c141c867f9db | -13.07769 | -49.24155 | 2025-06-06 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11e9b4f9-7e55-35f0-b5e0-c5b17a5bcb8f | -11.53057 | -56.45621 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1640b93-af13-3693-bfc6-20a92cbb3a28 | -14.74149 | -45.09883 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d024671-b1c0-3530-958c-765aff8369f6 | -11.38436 | -56.5497 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a30d090-6866-39bd-bd6e-5a2de78dbb06 | -10.50146 | -53.6616 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58735441-2cef-3fdb-8bf0-f2c3cd498369 | -14.29956 | -47.99083 | 2025-06-06 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244b9e64-41c2-356d-a8a0-dff103ff12e5 | -11.3822 | -56.56042 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84611206-c70e-32b5-abb1-482c52860deb | -12.96082 | -46.77474 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24bf0534-6c45-3d49-9a84-8334dc014c39 | -17.78306 | -48.63108 | 2025-06-06 04:17:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98fec8ec-e4ed-340c-bf90-83cbbca8199e | -14.73269 | -45.09011 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25c695c3-72c9-399b-a430-c006545cce5b | -11.13535 | -54.2209 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4909824e-8cfc-36e5-b75a-45cf7ef9b014 | -12.66311 | -58.21637 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 729e6adc-5edf-3168-aeec-1ff9ce6b2091 | -10.49606 | -53.66063 | 2025-06-06 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e14dd797-0163-3277-8f76-99581c71b80b | -14.29526 | -47.99465 | 2025-06-06 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95336bf4-6289-3903-bf56-c3c1639cbb42 | -11.9469 | -46.63075 | 2025-06-06 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc7d5fdf-4378-3a76-8a4f-a89c16c35f6f | -11.14295 | -53.94265 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6943404-432d-3f81-ad49-6a6152364050 | -14.2208 | -45.48868 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6486e43-88b1-3e7e-b56b-7f2ac4bc4571 | -10.47311 | -51.89096 | 2025-06-06 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bdb5ee3-1471-366a-9320-530f511854a2 | -15.14608 | -45.51157 | 2025-06-06 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97bc7b06-14f2-3b07-b11a-9fa318161cd3 | -13.51677 | -56.55909 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb75d12a-8dc2-356e-966e-60482f6392ca | -10.81641 | -56.95965 | 2025-06-06 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90aa1d32-97e3-39d6-adbc-3593ee954cc6 | -14.74093 | -45.10237 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ca6b45-f8d3-37f1-8cdb-fad6fd485aad | -14.30029 | -47.98644 | 2025-06-06 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb4ae372-fb94-382d-bb9d-5a432e9c6e25 | -16.06605 | -43.65567 | 2025-06-06 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d738e9a-5046-32a2-bc2c-5eb0bd063d53 | -11.14226 | -53.94625 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b766526-72f8-35ce-b6c1-eee85636911c | -13.52193 | -56.56501 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bd47819-43b3-3e26-a9d3-3cd315dceb91 | -11.57088 | -44.87697 | 2025-06-06 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2ea4723-55c6-3976-99bd-895f66dee06a | -12.82237 | -47.37203 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9572a2c2-293b-34fa-bdde-d2487e43dd93 | -15.00522 | -56.06296 | 2025-06-06 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81ef91d0-c735-3aac-a643-4e7b4f002962 | -12.83439 | -47.38657 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dfdb402-1e0d-3777-9452-21ce4f728c20 | -12.38455 | -47.31696 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66957b8b-060b-3853-b94e-f278779499b4 | -14.74368 | -45.10646 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40700c04-d009-3ae4-a5b8-d286a138b020 | -17.6629 | -46.6793 | 2025-06-06 04:17:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7687f0b-79fe-3b10-aa6f-a62cf9ca9fd3 | -15.5694 | -47.85677 | 2025-06-06 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b39a56b5-6c4d-3bde-89a5-745eb65718fa | -13.71486 | -57.48101 | 2025-06-06 04:17:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b28a8e8f-9c7e-3364-bacd-bc3bf7d355dd | -11.92562 | -54.81988 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ec513626-4a2e-3b80-b0ff-7e85097e3714 | -13.64145 | -52.1829 | 2025-06-06 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ae02a99-415c-38fb-a758-60d6cc76e99f | -12.10076 | -49.4778 | 2025-06-06 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bfdb0d2-9d55-3572-86bc-57aba4b4146a | -14.03646 | -55.13823 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cc7998c-5058-309f-b634-7268ef6ac649 | -16.13555 | -42.32971 | 2025-06-06 04:17:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1583d892-f81d-32fa-8490-a299664ade48 | -10.68443 | -57.59565 | 2025-06-06 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 482b8a6d-418f-3ef8-b9a4-3f24562dacff | -17.59516 | -43.19948 | 2025-06-06 04:17:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36290588-a4a8-3df5-92ba-39b153680b1a | -15.15268 | -45.51268 | 2025-06-06 04:17:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d08eb8-d578-3961-8310-ce9afa57048c | -14.23072 | -45.49032 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2e5be49-9acd-358f-b54c-5ea78a2fd504 | -15.01124 | -56.06196 | 2025-06-06 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbc8632a-ac2b-3261-8339-631d3d392b37 | -15.52855 | -48.50507 | 2025-06-06 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd9f5410-8394-3431-ad38-5dfe1d88f873 | -14.22741 | -45.48977 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d262690e-153b-36a0-a906-c646d4c49af0 | -12.95334 | -46.7774 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a484f2d6-8a63-37bd-bcbc-273620112a61 | -11.57194 | -47.44185 | 2025-06-06 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c480c2-f303-301c-91ef-a90ec6db1b02 | -9.52537 | -54.77198 | 2025-06-06 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c7f4ca-8715-39f7-9946-2fcfa8fc6323 | -11.37692 | -56.55384 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f64972a8-f1c0-35ca-ade7-78f7449f934c | -14.22298 | -45.49633 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 212c573e-2f6e-304a-be7a-1112a0c3832e | -19.88484 | -44.07219 | 2025-06-06 04:19:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2d15d6af-1262-3f4a-85bf-8c6bb964425f | -19.53717 | -44.07987 | 2025-06-06 04:19:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7b56a76-4f98-3c54-8272-204f23a822d2 | -19.43072 | -54.77893 | 2025-06-06 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c9c0219b-8af8-3573-bd88-b552010e1a43 | -19.93137 | -47.26655 | 2025-06-06 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 705299a2-a6ec-3afb-be66-34a71de1ea8e | -19.45524 | -45.30873 | 2025-06-06 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5faab174-55aa-3f91-af02-89142ae5108f | -19.93197 | -47.26284 | 2025-06-06 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 82b9ecdc-68c8-3ab6-b65f-91ca039042f3 | -17.91315 | -54.11561 | 2025-06-06 04:19:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca778cef-2a56-3179-8c04-d349bd5d4e1a | -19.43188 | -54.77332 | 2025-06-06 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fa96e476-d2e8-3d48-87bd-8f5d181bc318 | -20.09246 | -41.34162 | 2025-06-06 04:19:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77ae38a6-91c8-3d53-8e1a-e40663d24491 | -19.43677 | -54.77446 | 2025-06-06 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dfcda236-b100-3d0d-a511-08815f5fd12b | -21.19456 | -44.93834 | 2025-06-06 04:19:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 566ad344-e65c-3fb8-a70a-4011df40dab2 | -25.40548 | -52.40815 | 2025-06-06 04:19:00 | NOAA-21 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db113e9d-d3f6-3a45-b13a-ebf9c50b8739 | -19.85111 | -43.84607 | 2025-06-06 04:19:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7f1669b-c078-375e-8fab-0e4b835d5955 | -20.41665 | -43.5536 | 2025-06-06 04:19:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e5493da-726e-397c-abed-b00bb1be66d0 | -19.83344 | -40.11408 | 2025-06-06 04:19:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a452dde-be91-3aaa-9e63-23398e6db4d9 | -19.42581 | -54.77783 | 2025-06-06 04:19:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb13a385-b561-326c-9612-c40438a610ab | -19.88081 | -44.051 | 2025-06-06 04:19:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa86c420-0188-3e8e-a7dd-39205474938c | -20.89951 | -43.81959 | 2025-06-06 04:19:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7cbcc4a2-d9c7-343d-9c73-57bd9f76c136 | -19.05264 | -53.45701 | 2025-06-06 04:19:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1730a1f2-b0a6-3468-bd5c-78a05a60f462 | -25.40167 | -52.40731 | 2025-06-06 04:19:00 | NOAA-21 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9ab9247-4778-38d9-a340-e5135b8a08a0 | -19.71905 | -40.35369 | 2025-06-06 04:19:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 344625e1-0344-3480-b328-c2748d216342 | -7.0169 | -44.5954 | 2025-06-06 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8c13890b-cf1e-3e8b-bc90-f3dd67151ab8 | -7.0166 | -44.6184 | 2025-06-06 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 18fc0edb-862b-35e4-a238-cd9bbb85c8cd | -7.0169 | -44.5954 | 2025-06-06 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 05a14969-6652-33c0-8002-b80ac3ce76b6 | -7.0166 | -44.6184 | 2025-06-06 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c808bc34-b9dd-3f79-96b3-ebd77ca5652e | -7.05065 | -45.72924 | 2025-06-06 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a406af3c-6366-3ec8-94db-b76be63c7b7d | -9.07584 | -47.1457 | 2025-06-06 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe090de9-f5a3-32d9-948a-21ad5f69e567 | -7.28588 | -49.28307 | 2025-06-06 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bd48ae9-bc82-3136-a2f0-4afc68893acd | -7.86094 | -47.88982 | 2025-06-06 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 299134b9-4f4c-3d4a-9fc7-d7c2260bb5e0 | -8.94468 | -47.29744 | 2025-06-06 04:40:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d22e9939-eb04-30f7-9f78-a714cd53e22c | -7.90051 | -50.36272 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5acc4ba1-b714-3293-9543-db926854a413 | -4.97362 | -47.81483 | 2025-06-06 04:40:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01737dad-42f9-3886-8db7-b74495fa4457 | -6.20134 | -48.54262 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 705d203e-c71e-339a-bc0a-8aa544f1c572 | -8.47403 | -49.60271 | 2025-06-06 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e9974d8-7944-3272-b9f3-5f4a920d57da | -8.73151 | -47.98855 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
