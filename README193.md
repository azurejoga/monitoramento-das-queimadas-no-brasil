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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0db52680-d3bc-3029-a8bd-90c2dfcce658 | -10.88651 | -63.89206 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3746249a-a26e-36fc-b44d-5ef0d1b3a43a | -10.87745 | -63.88396 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd916cac-fcf2-3ae2-acd1-c9d1603beef9 | -10.8686 | -63.88265 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cd4d3ac9-8b17-3536-93d3-0fbf96631d32 | -7.28759 | -64.65803 | 2024-10-02 06:27:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f43aff13-a02b-3fa4-892d-c3210b9e7515 | -9.29788 | -65.33819 | 2024-10-02 06:27:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f622bf6f-4825-3ebe-a08b-c6be3ffe5874 | -8.95099 | -64.35466 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3606bd85-0416-305d-bc24-b67df348b448 | -9.9488 | -64.89561 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0b6792c3-6def-346e-850e-c95dda4a563d | -9.94735 | -64.90502 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 06a8cd7f-c7f3-3908-aa99-7cf958b4a1da | -9.94591 | -64.91444 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8911b479-f448-3a97-a31a-38a769461bbf | -9.93973 | -64.89423 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f0ce7245-d8dd-36f6-860e-91bd48d89ce1 | -9.93828 | -64.90363 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b98e966d-b9ca-367b-a23f-b6b966b92650 | -9.93684 | -64.91303 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a100df48-1a63-3117-9e84-c20d4d96b6e7 | -11.67829 | -64.9957 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5816c622-209e-3214-aefc-3ba2f346b071 | -11.67687 | -65.00497 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 59505fa4-e917-34c3-99bc-dccd0adb8770 | -11.65746 | -65.01143 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 78030039-7e05-36fd-9224-a4579427ee8b | -11.64703 | -65.01933 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7527f06f-aa27-3511-aa73-5f80800e5a7f | -11.61525 | -64.98875 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7050ca9a-1b01-3c7b-bb9c-9041e244b970 | -11.28452 | -65.27439 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 928b1da8-c19f-3128-8d50-4544534b2ec0 | -11.25021 | -65.02128 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba19d5b2-e40d-3561-91e5-17d932253b00 | -11.66788 | -65.00356 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 01db981d-65bf-3d50-9419-b30dea47b39a | -11.66175 | -64.98361 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 080376a5-790a-36f4-8e5e-445d85f12378 | -11.65569 | -65.20255 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 64dbdc6c-d83b-3b81-8598-64be06d94f4e | -11.65276 | -64.98221 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5790aa1c-51d2-3a31-9fe7-235098cb5d1a | -11.61383 | -64.99803 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 819d7976-f8cd-312f-818f-9e3c1042859a | -11.58194 | -65.14597 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f7d79b93-8ac0-3528-961e-d4b5e5620a4a | -11.28599 | -65.26485 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 429ccf3e-7697-31c1-9354-1920da1bcd0f | -10.86191 | -69.4826 | 2024-10-02 06:27:00 | AQUA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2ddb6fb3-52c6-3c2f-b7a3-d3fe9bede2d0 | -10.85898 | -69.49993 | 2024-10-02 06:27:00 | AQUA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 15b5d7e9-1cb1-3ed0-b164-51731fc168f7 | -10.69346 | -69.38747 | 2024-10-02 06:27:00 | AQUA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9164e47d-5f00-3cd7-9a19-3e91d8eeba7b | -10.53401 | -69.31187 | 2024-10-02 06:27:00 | AQUA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0a035b53-2015-3c9b-8bdc-a6c92d68ee30 | -12.86712 | -62.52209 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3c038523-fcee-3940-bd92-59a6d4f54db6 | -12.75096 | -62.87898 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcc78c54-b3b3-362e-853c-0460ec8a8380 | -12.81598 | -62.5582 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f7efae8b-32b5-3589-a67a-7fdac456d7cf | -12.86574 | -62.53177 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ec5475b2-61df-3ea3-a7a6-e5df7e7444c6 | -12.83071 | -62.52092 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| aff0c956-3f7a-3d05-9fe3-999b1662e19c | -12.8587 | -62.77525 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 45c6c835-2f20-3127-b72f-6bcd4f2b6989 | -12.83646 | -62.80103 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0b23031e-548a-35a3-8b99-4c98216713a7 | -12.85796 | -62.52076 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 8068aebf-1971-36f6-a56d-bfc094a3b3f0 | -12.85816 | -62.84285 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6c39401-eda7-33b3-99f9-0435adaf399a | -12.85384 | -62.54977 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3a8d83be-bf8e-3d45-878d-0e2860a9ba0c | -12.85679 | -62.85229 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 809c02a4-e589-3b20-b3e6-b22b0589cabd | -9.26794 | -67.5956 | 2024-10-02 06:27:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0ba2b7ea-2864-306e-ac27-356d9ac4f487 | -9.53782 | -67.71355 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d936f330-5b8a-3d6e-9536-5bcb77b46661 | -10.32911 | -67.74814 | 2024-10-02 06:27:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ec450d6b-0d5a-34bb-b5c8-544d8f99c64b | -10.31628 | -67.75981 | 2024-10-02 06:27:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0453eaf4-e8db-3e1b-9c07-429502691d9f | -15.36522 | -55.83026 | 2024-10-02 06:27:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| cafecf8e-38b4-382f-8c89-ecf127e4064d | -10.61977 | -55.87837 | 2024-10-02 06:27:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 06b61c82-8a92-3e3d-ab0c-bffe47ee5652 | -11.48754 | -56.78417 | 2024-10-02 06:27:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| fd5ef53e-d4e3-3f62-b85d-8b75e45a5a30 | -15.887 | -57.16399 | 2024-10-02 06:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 21ee36c2-da23-3b8b-8d6d-798835dec3bd | -15.88135 | -57.15826 | 2024-10-02 06:27:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 166565be-7ec4-377f-af02-0672f97cc929 | -15.55153 | -56.86483 | 2024-10-02 06:27:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 40282f6a-0830-31a4-99dd-ff9c368da5c2 | -15.54839 | -56.89221 | 2024-10-02 06:27:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 12d23144-0d46-3001-9621-cf24d276a8f0 | -15.53395 | -56.89241 | 2024-10-02 06:27:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 5c8f2a86-f03f-3910-9cb8-15b133d273f2 | -9.39314 | -61.04434 | 2024-10-02 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 047c77ca-188d-3ae8-ab35-f7babb608684 | -11.25431 | -60.5942 | 2024-10-02 06:27:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 425e1380-0b1b-3905-8987-cd4cd17658e5 | -11.24283 | -60.6036 | 2024-10-02 06:27:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ea0ac554-3dfa-34dd-bd6c-88f5653f5804 | -11.2444 | -60.59236 | 2024-10-02 06:27:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ef515f25-4dcc-3dcd-a81d-caac2995af5a | -12.9794 | -62.70236 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1597a225-b1d9-3cc5-a621-7fc10017d40c | -12.94299 | -62.69701 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cd7d667b-221a-3d89-b0fe-be507b7cb26d | -12.8749 | -62.53311 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| d9879ec2-f2a0-3171-99ac-062f0e08313c | -9.585 | -66.50167 | 2024-10-02 06:27:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bba38f0f-d8e1-3787-a4fc-b24b85410a87 | -7.63819 | -67.19367 | 2024-10-02 06:27:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2ddf81cf-14f4-385e-9e6a-6c64691cd316 | -9.27913 | -67.82819 | 2024-10-02 06:27:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3c42aced-2c2f-30e3-987a-e8aab875e1d6 | -10.10755 | -67.89243 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20118951-6d4e-33e5-91e6-eecbea78e252 | -10.12208 | -68.40864 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeec8008-2fb7-316e-a82c-fd9410207b1a | -10.27139 | -68.76637 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc35415c-615e-3674-8ba3-93e37e8ca8c6 | -10.10218 | -67.89162 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f664dd8-3197-3a22-8611-73270fc77819 | -10.05513 | -68.58457 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f27ef02-28cd-3936-aad7-3aa49f8df9d8 | -10.05472 | -68.58768 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d3e5de7-53dd-3a39-9ecd-f3313314b28e | -10.12249 | -68.4054 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1539e0ed-ed43-306c-91e2-6283bd313477 | -10.12861 | -67.8989 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b728baa2-09b6-32e0-861b-e22b9d313a4f | -10.13354 | -67.90307 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1bbe0a0-c85d-3249-a435-cbfabe206a37 | -10.13399 | -67.89964 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5c7054a-e68f-38c9-b04c-be0768111664 | -10.2718 | -68.76334 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55599d48-970d-3dd6-bed6-aef93d02ec1f | -10.27507 | -68.76808 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f070f812-53c1-3a00-97c7-f3e9881dbc8a | -10.27545 | -68.76505 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d9629f-d603-3352-97f7-8bf2b41df8ef | -10.27606 | -68.77011 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f70bd8-17d7-3133-b48b-deffa22a3ff4 | -10.27647 | -68.76711 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c7c225-d80a-39c8-a013-e3e67d1e2227 | -10.30441 | -68.02568 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c005202e-556a-3766-9f1e-5d699553b9ea | -10.30679 | -69.19039 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 914de61a-ab39-3719-b516-c9391123b22e | -10.31478 | -67.7691 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f3a4d20-e856-3f9e-8162-0ef8226941ed | -10.31522 | -67.76559 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44fdaeb9-2393-3b58-b610-bbb3b4bf6509 | -10.3202 | -67.76997 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c50a1e27-f7e5-3769-858f-171a70b18572 | -10.32065 | -67.76641 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15df8d9d-f356-34cb-9747-de6a04a8d167 | -10.32109 | -67.76282 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84fcc65c-72bb-35a2-b0bd-72e9b26ce1e5 | -10.32607 | -67.76733 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0dd7e58-f77b-3bc3-8cfa-15842d024a44 | -10.32651 | -67.76378 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 416149cb-ba0c-3f7a-940d-a2aa93ba4049 | -10.33195 | -67.76456 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a424c342-6ff9-3dcb-ae8b-c43d3b34a884 | -10.33328 | -67.754 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6d7729c-8096-31be-bcfe-dddf321f7f4e | -10.33372 | -67.75044 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92f79d5c-0018-3702-82b0-f38d3b3ca668 | -10.33917 | -67.75117 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 435d0cf8-d569-35b8-81ad-27bd462bba32 | -10.37444 | -69.10767 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e55818a-db48-304d-a5ea-4ae2f17e75bb | -10.38194 | -68.17353 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24642a06-ea3f-3bc1-9092-85c74506a5df | -10.38236 | -68.17021 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d2ec5a9-9ea7-3014-951e-b380ab982289 | -10.38579 | -68.22802 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d5557a-65e1-38e9-91cf-fd8bf4179294 | -10.38617 | -68.14009 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6b1c2b-13d2-39f4-b0cf-a17bc2769f87 | -10.38621 | -68.2247 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf36a57d-531e-34bd-bb41-1d94fc298c2d | -10.38659 | -68.13676 | 2024-10-02 06:27:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8924062-6f1b-3522-9c1f-dad68c10da92 | -10.39275 | -67.95775 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f143bb43-0f9d-3e91-a697-b6e06ef3485d | -10.39319 | -67.95427 | 2024-10-02 06:27:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README194.md)
