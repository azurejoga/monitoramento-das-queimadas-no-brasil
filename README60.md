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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3041f6-f326-3470-aef5-3e527ca48634 | -10.76312 | -68.66191 | 2024-10-16 05:25:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93e2a5e3-9a3a-3e67-89dc-633b664bfcd9 | -10.7605 | -68.31024 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 197eb580-ace3-321d-9693-5b6f424857f3 | -10.73086 | -68.86256 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 249732d5-409a-33dc-89a9-fda3fff2dd75 | -10.7098 | -68.56504 | 2024-10-16 05:25:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1533db-0c9c-32b6-a25f-e5c4ad222f57 | -10.67005 | -68.57496 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b02846-2aa3-333b-8fc4-c10c556cc889 | -10.66607 | -68.57201 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4ffdc42-4564-35a8-9db3-3b6b8eb225ad | -10.66547 | -68.57417 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4920a321-1412-3da2-adc1-9392303eb1d5 | -10.6652 | -68.57673 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 559151bd-4339-3b97-a953-747410e29786 | -10.66464 | -68.5789 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb2eba95-96b9-3a84-ae69-8bef2e6e70f2 | -10.66062 | -68.57595 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 788d04ec-60bd-34e3-b6ac-218cb0e46abc | -10.65233 | -68.85479 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5017d19-454a-3346-9dec-8441fbf46998 | -10.58063 | -68.1512 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be4b9aba-602a-3ac0-b745-6965f98c46cb | -10.5786 | -68.7679 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b12a1e41-d504-3097-891b-c239c738ddf0 | -10.57771 | -68.77281 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a01b894-5c7d-3093-94f2-4542c783b913 | -10.56105 | -68.57692 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf0999c9-f0bd-3346-9c57-e79b0d7fd730 | -10.56061 | -68.57938 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47f7c056-9a6e-355c-be97-89b837099559 | -10.54776 | -68.72705 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f68b2c4-c5c5-329f-a9cf-1ecadcd38181 | -10.48983 | -69.04207 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 801172e4-5dfe-37a9-9dc0-60a4fae25177 | -10.48511 | -69.04115 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f093a571-03aa-307d-81e0-f4cc8a841860 | -10.3544 | -68.07151 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa83029-43bc-3674-9159-66760c91712e | -10.19674 | -68.31747 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f331cf15-e28e-3b8f-b2f4-589f8f55fbe5 | -10.19221 | -68.31664 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f24d8896-7774-3cd0-8230-8d203933040f | -10.11676 | -68.39233 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05170389-66d3-3fb8-81f8-641daa68a027 | -10.11304 | -68.38683 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe1b304-56ef-3569-81d7-4507e0541ebe | -10.08276 | -68.29437 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba346fc-712f-3d1f-8c0e-b5f2f82cff90 | -10.07546 | -68.36054 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6102c91c-1018-34c2-898e-403a7373533d | -10.07125 | -68.06207 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29556dc8-2178-3cc2-86ce-d58ccd8c35db | -10.63224 | -67.83627 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6f8d01c-6cba-368b-aca4-86b4d1a00186 | -10.63147 | -67.84056 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d7df2252-625a-32c9-bff2-73c83bfca75e | -10.62712 | -67.83976 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5b16fbd-0e2b-3e37-a769-9fbd94d234e0 | -10.61842 | -67.83817 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4029108e-6d0e-3633-8eef-60abca42cde4 | -10.57555 | -67.77005 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43a7d25d-45ca-3e26-b393-afcd838751c7 | -10.55667 | -67.77564 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f7e2941-0915-3964-b157-2929f10cd85f | -10.5429 | -67.77753 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1f50e5f-31ee-32cd-87e0-4da473d0194b | -10.47026 | -67.85297 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26637537-2acd-3766-8bb3-2612105f2b3a | -10.46667 | -67.85181 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27bedb04-6b98-37d5-9397-388b430a6ff1 | -10.40473 | -67.91738 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30d93a54-7d5f-352a-9d8b-d6934b248a79 | -10.39182 | -67.96444 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c93d56c-782b-31e1-acb9-6e404ab193e8 | -10.3851 | -67.90041 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ada12acf-6292-3b97-8b03-6df83850be9d | -10.38432 | -67.90477 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62397827-8a76-3161-be00-a32c3704df1a | -10.35501 | -67.96673 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b94573d5-821a-340f-be27-92c2155559dd | -10.34451 | -67.92434 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa5405e2-2048-362f-abd8-a9a98ebc0586 | -10.34449 | -67.92579 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4205aa3f-9752-3811-b0e9-f88a56085560 | -10.34372 | -67.92869 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 034f40a2-3f14-3b2b-b854-73da39b6f4c2 | -10.33474 | -67.95567 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6621de4b-2dba-37c9-972f-5959b671c1f8 | -10.33453 | -67.95415 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf9cb39-15eb-3232-9e6d-d458100c6fa7 | -10.32802 | -67.96811 | 2024-10-16 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7aa773c-8804-315c-865a-1f978fa9fc81 | -9.95121 | -68.3659 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27fd8dfa-b4f3-354c-883e-828fd6cc953d | -9.9512 | -68.36832 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f428f54e-ef6b-32d1-84c9-6e4ba710afac | -9.89581 | -67.59405 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7457ff-cd0c-348c-8da2-2a0b8dee53a8 | -9.83418 | -67.60549 | 2024-10-16 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 074b4f9e-331c-368b-bf7b-771e341c2621 | -9.78032 | -67.94042 | 2024-10-16 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 657e020b-bdfd-34c1-b92d-40fddf822524 | -9.77953 | -67.94495 | 2024-10-16 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ab5269e-6ee7-34f6-a324-1e25308bb2be | -9.71241 | -67.47641 | 2024-10-16 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc5a3cb-efdd-3b7d-8d3a-29708879bdee | -9.68366 | -67.58865 | 2024-10-16 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3a4159-6182-3015-8373-78fecbb55180 | -9.64426 | -68.96604 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53dfb81-6acc-30e2-81f8-f961293a3f1a | -9.6381 | -68.61343 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3d9ee2-d9b9-34a1-bee9-0d5ecf16e589 | -9.60591 | -68.55186 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcc5fbd9-9abb-376e-93b0-746650d0b68f | -9.59911 | -67.52721 | 2024-10-16 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aca4bdb-aac4-364e-8d4b-e986d31a70b7 | -9.5975 | -68.54531 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9eb735f6-9b81-3298-ae82-fe5aef8f3415 | -9.59172 | -68.50616 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c840233-8f93-3609-9166-24ed4cb7a1ed | -9.58983 | -68.50855 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c2b40cf-f0af-38e0-899a-18ab09547553 | -9.57561 | -67.816 | 2024-10-16 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d54bb4-3e9a-35bb-a342-34fd51b2d2c1 | -9.4871 | -68.50237 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67b11e14-7c6c-3159-9c48-4a794e19bd04 | -9.47383 | -68.47734 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7104b127-725c-3591-a2a0-16c2f1c946b7 | -9.46919 | -68.47655 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1b73700-b650-3b03-9d8d-359dc9018ed8 | -9.46747 | -68.48634 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 746829a5-559b-3e79-87f7-188748ccae90 | -9.45971 | -68.53043 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f4a0f38-0bbe-3733-b2e4-823219d650e2 | -10.95669 | -68.25027 | 2024-10-16 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0c9588c-024c-356d-b36b-c330f1d052d5 | -6.90177 | -47.31807 | 2024-10-16 05:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fcd2b1ef-5a2a-3a40-b95d-842d94ffafc9 | -6.9009 | -47.32476 | 2024-10-16 05:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 45785c26-10ac-3415-bf7f-ab9786dd91f1 | -11.7357 | -48.65649 | 2024-10-16 05:25:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef1c743f-3249-39a0-b9eb-67f133a80da8 | -11.73114 | -48.65404 | 2024-10-16 05:25:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 328436c4-50ea-34c5-8e7a-8b39c52eee65 | -11.73047 | -48.66026 | 2024-10-16 05:25:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cced1501-b124-323f-885d-f4b781b6e099 | -11.72891 | -48.65564 | 2024-10-16 05:25:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 522acd4f-2920-312d-9ecd-0b08301379a1 | -11.7282 | -48.66185 | 2024-10-16 05:25:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ed67e035-3221-386a-a8b9-ba2b46a3650f | -5.22797 | -47.9581 | 2024-10-16 05:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9495b660-dd18-32b7-85be-064e8e095386 | -16.81616 | -53.93674 | 2024-10-16 05:25:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9671aec-134d-3f02-89f0-80e9f5f36c90 | -16.81579 | -53.94006 | 2024-10-16 05:25:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecfcdab-fa1f-3105-8989-03ea93389ee4 | -4.31265 | -53.71249 | 2024-10-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6276996-4916-3ea9-ab32-a46f5949025e | -15.92259 | -56.30991 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6444f470-4393-39a1-9674-a8fa31afcb01 | -15.92147 | -56.31861 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3353755-608c-30e5-be5d-b9d40eabf0fc | -15.91877 | -56.30497 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a86e5959-de37-355e-b414-abb378a5eea3 | -15.91822 | -56.3093 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2b4ecc8-46d2-30c7-8925-28bc61dbf102 | -15.91766 | -56.31365 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94a0e940-58a3-3a94-b852-85034269beb8 | -15.9171 | -56.31804 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4165b97-af3a-3e6c-8a9c-7aa68a543879 | -15.91385 | -56.30872 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e56ecca-a6dd-32fa-9855-df4ebe0c55f3 | -15.90947 | -56.30816 | 2024-10-16 05:25:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9763369-b8c4-3fd2-a9b5-730f17876a06 | -15.3654 | -56.32222 | 2024-10-16 05:25:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0945e6f4-3ccb-398b-a7e5-39828b6c70d1 | -17.04049 | -56.00331 | 2024-10-16 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1afe3fda-9423-3d56-ab7e-3297d637d986 | -17.03596 | -56.00269 | 2024-10-16 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4e02fd65-bfde-3ce5-be3e-5ac2d81691d3 | -4.22867 | -54.96127 | 2024-10-16 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc23a5f-2c7c-3753-a25c-cc176cbc36ae | -4.22814 | -54.96479 | 2024-10-16 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51fa5634-6dd2-3245-9d1e-0de18f225ebd | -4.35693 | -54.77448 | 2024-10-16 05:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c96232f-0d04-3871-8505-db0a2a0e944d | -4.2327 | -54.96191 | 2024-10-16 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ba6801-26ed-331b-9d25-55fac6a38dd9 | -16.83805 | -56.69064 | 2024-10-16 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b5d9e6bc-629b-33bd-846f-d35993618235 | -16.84021 | -56.67356 | 2024-10-16 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| a6ef7712-0246-3daf-b530-8ff5fd72d987 | -16.83859 | -56.68638 | 2024-10-16 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 255cf295-8197-3366-a6ec-bdd50092c0ef | -4.24169 | -55.51304 | 2024-10-16 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 625a0c8b-8145-3877-9dd8-d6734a308ef6 | -16.31128 | -58.60484 | 2024-10-16 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README61.md)
