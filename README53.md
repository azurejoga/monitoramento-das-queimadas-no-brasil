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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78d3b539-9d25-30ce-8012-15160ee7f251 | -16.3051 | -52.92219 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3fd2fb25-0f22-36ea-ad63-0e5da182ffee | -19.46711 | -47.16193 | 2025-08-15 04:53:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ec035a1-a601-343a-97cc-9ef3d2e4766e | -16.38082 | -50.90538 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da62a6e-e98e-3eb6-83a5-e62ed9c4370f | -17.49684 | -47.83985 | 2025-08-15 04:53:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49a3cfb2-7e8a-3eed-b7e1-e0de2525ee5d | -16.30278 | -52.91407 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1802e51f-fde9-39cb-acd2-361c859853df | -17.05282 | -51.79324 | 2025-08-15 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1e52359-3d6c-336c-8a51-ae998c9f97bf | -15.96676 | -59.51502 | 2025-08-15 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09e7a589-5500-300a-9488-076e7d01d140 | -16.3821 | -50.89581 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03eb93a1-a5ac-3ad8-9d3c-9adae8bb981a | -17.64863 | -44.49159 | 2025-08-15 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b715b8-9661-3dac-b4e1-4099115e2c0e | -16.31887 | -52.92011 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31ca3e40-5323-3fbb-a6be-ebc384a8e79d | -18.00677 | -49.39799 | 2025-08-15 04:53:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16c7ba1d-896e-3de4-8021-41b86dd3170e | -15.96976 | -59.52065 | 2025-08-15 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07840dc9-0b38-3911-af12-ddb52a41bf30 | -17.56851 | -52.53217 | 2025-08-15 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d95287dd-e02a-309b-889f-e4ef22272ece | -16.69034 | -49.37014 | 2025-08-15 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b6aefd2-a527-3a67-a4b3-fae211c35f76 | -16.47501 | -51.98107 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 669f712b-ffa8-3ab8-8cb5-874f5658affc | -15.97063 | -59.51574 | 2025-08-15 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67abd247-fc40-3bb2-bbd7-d1bd7bbc1193 | -17.05585 | -51.79809 | 2025-08-15 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21c7208d-e1cc-3273-b98f-bf1504bbdcdf | -16.47856 | -51.98183 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37dfcd30-b5b4-3add-8e80-501dab684bcd | -15.58044 | -47.32416 | 2025-08-15 04:53:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ca4753-7135-3a90-9f0c-0edb54a42cff | -18.52997 | -45.45066 | 2025-08-15 04:53:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c7a9b43-9e87-3cce-8d82-b1c45f878e4b | -16.39092 | -50.91628 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d299aef9-f9cc-3467-9c0a-7b4dc2ca0b5d | -19.552 | -44.83954 | 2025-08-15 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c6333ac-dd95-310e-9b43-a5fbb12aa44d | -15.66581 | -56.38154 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7946dcc-c23d-358b-8942-8ff44d23a72a | -17.5691 | -52.528 | 2025-08-15 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f637e12a-5a78-3503-a2df-02a5f32c6955 | -15.39592 | -55.77891 | 2025-08-15 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d803da5-6ea2-3785-a452-6bc173acdf3a | -15.32563 | -51.5134 | 2025-08-15 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7960c385-53d8-3286-9074-4fa5b5da3ab2 | -17.64757 | -44.50185 | 2025-08-15 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f8ec6a8-7aa1-31e1-8b33-0a04981f18a7 | -17.36168 | -44.13795 | 2025-08-15 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cce67693-1f7d-38b0-8181-0a0f02befda9 | -16.30166 | -52.92162 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| abd1f6e0-1a2a-36c8-a059-24a563cc249f | -16.37732 | -50.90298 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90a4e98f-f3f2-3adf-a574-c3fab2f9e206 | -17.64825 | -44.49526 | 2025-08-15 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51ade7dd-021f-3812-8ca3-5f8c912177c1 | -18.96857 | -49.50308 | 2025-08-15 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f38f7d1-a3a1-3c22-9a89-163860dede2b | -15.3839 | -59.82304 | 2025-08-15 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d48d974-e3bd-3865-9253-36edce0aebc8 | -15.89141 | -50.17198 | 2025-08-15 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9d68d194-6dee-3021-9fb0-d4664b7bf56a | -20.47815 | -53.67468 | 2025-08-15 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa1062c6-dccc-3c69-8116-09ceac9e3be3 | -15.67026 | -56.38178 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e386dbc-7a05-3af8-bc44-9f003c61f22b | -19.67267 | -44.60403 | 2025-08-15 04:53:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0fbf643a-9d41-36ba-8ddf-de8e910c2513 | -16.90909 | -52.55051 | 2025-08-15 04:53:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d0d8211-6dc6-3b97-9695-48354777c0a5 | -16.31252 | -52.91954 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27dbae2e-3bc4-3f17-9360-d0a5286c1446 | -16.37357 | -50.90224 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e6a39b5-132f-3e38-a17f-87dc9af03705 | -16.30453 | -52.92598 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 77e4617f-7a44-30d9-bdd3-8fe033ef77df | -20.40136 | -45.40396 | 2025-08-15 04:53:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a7e1dede-b887-36d8-8c98-d0741646bd2d | -16.32231 | -52.92067 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a5e4920-f8fd-3eeb-ab09-50bc91fe088c | -18.53503 | -45.45126 | 2025-08-15 04:53:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 155827de-d4df-3b14-adab-df06c4d69ee7 | -16.31544 | -52.91954 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b66c8692-d601-3da2-b024-121369e634c3 | -16.30622 | -52.91462 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9dee34e-e9cc-3783-bca6-e6ee3f67acd3 | -15.57572 | -47.32364 | 2025-08-15 04:53:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc850cbe-f972-35e0-91c0-441301a4693d | -16.17442 | -53.62929 | 2025-08-15 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3c55eef-e33f-3608-837d-87a453fce187 | -18.87207 | -51.9983 | 2025-08-15 04:53:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c06384-051c-33f4-8d31-c1a832b28319 | -15.67764 | -56.37921 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51149f06-6b18-33e8-9534-d8536ff93788 | -17.06011 | -51.79419 | 2025-08-15 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b3e4038-5311-3767-8f88-99e7da032981 | -15.93025 | -48.15492 | 2025-08-15 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7ebeb5e-d471-39ea-9062-e2b96edc0ed0 | -18.50923 | -50.6511 | 2025-08-15 04:53:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| d6123800-e2be-3b47-b5fd-5bf993546f7d | -18.69737 | -48.18262 | 2025-08-15 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8db9b1c9-d108-3898-ae7a-f20219da531b | -18.5355 | -45.45143 | 2025-08-15 04:53:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb8ee21-86c2-34d6-81cd-ead295130b7a | -16.47382 | -51.98946 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83f943fb-c2c1-362b-ad4a-bd81572462f4 | -17.55752 | -49.41885 | 2025-08-15 04:53:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88bb7ec8-56b4-34b6-9f5f-169c89b7a216 | -15.68039 | -56.38353 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaefc20e-3ce7-3c1f-aa18-e1891b9f70af | -15.32504 | -51.51136 | 2025-08-15 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7b5c0ec-95c1-3197-9434-bfef015dfcee | -16.31488 | -52.92332 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fdb75eb-c6fa-3df1-8c5e-6bf1dd7b94b6 | -15.89074 | -50.17694 | 2025-08-15 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee57e325-e967-3569-af2b-f68ab4f564ca | -14.91163 | -55.09182 | 2025-08-15 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 254cdf1e-8eab-3c02-bc3d-8be5155e315b | -17.36122 | -44.14248 | 2025-08-15 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa9d010f-d278-3772-ae1d-3125d31e8a86 | -16.3011 | -52.92543 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9da99f1d-59aa-3a35-9f8e-d1a96953819a | -16.39155 | -50.91166 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee275a8b-d1ab-36c2-b8ff-ce62cf5e5bd0 | -15.15023 | -53.51339 | 2025-08-15 04:53:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 552bd03b-d045-3781-b298-be71781233a1 | -14.37897 | -53.37358 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6e28a2-549a-31af-bfce-511fb8b0dde8 | -16.30566 | -52.9184 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fc29306-62d8-33ce-9693-b083de2b58b4 | -14.37283 | -53.36884 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40f11fe1-1ac0-3b2b-81ab-330c5339cd84 | -16.31309 | -52.91575 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb504e1c-0df6-338b-873f-690a67d63365 | -15.67426 | -56.37862 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e49aef7-b9c4-3a0d-b0e4-10737c56e48c | -19.47544 | -43.62074 | 2025-08-15 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a9500be-d61b-3546-ae03-551d5233adc7 | -19.65866 | -49.3735 | 2025-08-15 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d794d342-76f4-38be-a76c-477723569aa5 | -18.29747 | -49.5485 | 2025-08-15 04:53:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f5402ba2-1a44-339f-a457-f74fc04f3862 | -14.86716 | -57.56738 | 2025-08-15 04:53:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22a0d5cc-f63f-33c4-b1c3-c5dd56079bc6 | -16.39114 | -50.91452 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c70c93c-0a51-3d38-986d-96b9df467aff | -21.19162 | -45.68898 | 2025-08-15 04:53:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 822b69b5-505e-301a-ad3a-49173c13ac68 | -16.29665 | -51.73811 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1072c51e-b394-35a3-842b-32762cbf76ae | -16.38423 | -50.90879 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01c36e3e-7bbf-3918-9822-f4e674265125 | -14.37004 | -53.36462 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae63bda8-60fb-3eb5-865a-5dd946178a13 | -19.47206 | -43.61895 | 2025-08-15 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76a2d4cd-de80-381f-be1e-4b72719025f0 | -16.68356 | -49.3571 | 2025-08-15 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36f176d-269a-3b43-9dec-951e9def9386 | -15.25115 | -51.71716 | 2025-08-15 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8efccda6-473a-357a-9bf9-fdb8c60607ad | -21.20683 | -46.69022 | 2025-08-15 04:53:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3858bd1d-5e8d-39cd-b5aa-f616cc063316 | -17.64283 | -44.49062 | 2025-08-15 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58aa021d-6dc0-3ce6-a1f4-93ac5cfe0026 | -22.68284 | -50.4769 | 2025-08-15 04:55:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dfe029a-0f43-3bef-acce-9561e4091e20 | -21.57871 | -47.00743 | 2025-08-15 04:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b5c952d-5356-3667-adc9-547c1b64a607 | -22.71475 | -47.32888 | 2025-08-15 04:55:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cdd35f-d085-39ab-afcb-034a47efdfc1 | -23.26987 | -51.20536 | 2025-08-15 04:55:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 677c5e77-50e0-3981-bc69-f5863a9ebe4e | -23.40841 | -47.11695 | 2025-08-15 04:55:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e1d3be4-77b6-34fc-96d2-c773e2c4d207 | -23.20415 | -46.74607 | 2025-08-15 04:55:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 554a6cbd-5b79-35cc-88a2-666abc191d00 | -21.17 | -50.24537 | 2025-08-15 04:55:00 | NOAA-20 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f6a91ac6-c3e0-3472-bef3-0fd9ac28dfb6 | -24.32216 | -51.31043 | 2025-08-15 04:55:00 | NOAA-20 | RIO BRANCO DO IVAÍ | PARANÁ | Brasil | 4122172 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d8ff3f9-0ebc-3801-89dd-8024dcc0a68f | -22.95426 | -47.1531 | 2025-08-15 04:55:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 702637d4-4960-381b-8ca9-20e37ef8a859 | -23.26939 | -51.20931 | 2025-08-15 04:55:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6883bbc6-32de-3ed2-8fc1-82bbfd931712 | -21.44034 | -54.57677 | 2025-08-15 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ce158a1-13db-36a5-8dd8-73a943103ec7 | -23.35391 | -46.91717 | 2025-08-15 04:55:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca0ae484-7c11-345e-bb67-fdb2166aa1d8 | -22.68332 | -50.47271 | 2025-08-15 04:55:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f10e3391-c116-3b01-9843-bce615f9a66f | -22.68308 | -50.47374 | 2025-08-15 04:55:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6275772-ce7f-3ed5-9cc1-18324866a45b | -28.73014 | -50.91396 | 2025-08-15 04:57:00 | NOAA-20 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README54.md)
