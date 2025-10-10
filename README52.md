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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e11ab25-53db-388a-b820-ce331624802a | -14.8433 | -48.4665 | 2025-10-10 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a6a0a29c-6f21-3292-8d2d-3fa3e94cbfa1 | -13.3488 | -47.7388 | 2025-10-10 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 887be4e8-18ab-30ca-8e7c-6e84e69fb322 | -13.8491 | -45.8454 | 2025-10-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 27b53fbb-906d-3117-9347-351b33dc240d | -15.3933 | -47.3166 | 2025-10-10 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8dc249e9-f8fe-31f6-bf5f-411bf6db70a7 | -13.8496 | -45.8223 | 2025-10-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 288245b1-239a-3599-8e13-bf33ba638ebd | -10.1898 | -44.5934 | 2025-10-10 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 9844d809-83e1-373e-ad50-e00ed42fa0dd | -14.4253 | -48.0199 | 2025-10-10 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1cf5b261-36bc-3fa4-9fb2-d0d01b1886d5 | -11.7782 | -43.3105 | 2025-10-10 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 2ae395a9-b735-3b85-b018-51d5705273f6 | -14.9372 | -46.7591 | 2025-10-10 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6e74a4f5-7e79-37e5-92ba-2a0025f1db6f | -13.3295 | -47.7417 | 2025-10-10 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d9625c19-da76-3068-9775-2989615c0790 | -11.7589 | -43.3136 | 2025-10-10 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 415.8 |
| 76b795f8-08be-3282-94f6-6f4042a0f5f2 | -8.5027 | -46.177 | 2025-10-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0d94fdf5-2b95-39b4-af22-35c8f3be2261 | -8.4844 | -46.134 | 2025-10-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2722cc40-18aa-3c62-8d8b-f1bb54fe464a | -11.7585 | -43.3374 | 2025-10-10 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 17f44f3d-e0f0-3a05-b4eb-db5545adb036 | -8.5029 | -46.1545 | 2025-10-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f1fb3c16-f2a8-3a16-9859-fb561e12413d | -13.8302 | -45.8255 | 2025-10-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 06514751-308a-3099-b2c6-add8b812eed2 | -13.8311 | -45.7793 | 2025-10-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| c659b0d0-0a8b-3bd2-b83a-e7ebbb4aadf3 | -13.8307 | -45.8024 | 2025-10-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 57c20a96-9841-3fe1-bd7c-426fe110d589 | -11.323 | -47.5287 | 2025-10-10 13:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 06705b7e-ae58-3214-afc8-a6a3b983cfbd | -12.3592 | -47.2335 | 2025-10-10 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2e5cc84d-ac03-31dc-b7ae-523657cf1c55 | -13.0036 | -51.041 | 2025-10-10 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 69abf9a3-988e-3903-87d0-c07329e60e81 | -14.8628 | -48.4634 | 2025-10-10 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1dc9b0a4-11c0-37e4-b4c7-f325538cc832 | -14.4258 | -47.9974 | 2025-10-10 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| b2ce6fa2-80e6-34d1-ae6b-751cee589c8c | -8.5032 | -46.1321 | 2025-10-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 4304fe15-5146-33ee-a978-936873ee9f3d | -9.0022 | -45.4693 | 2025-10-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ef2da3f9-70a9-3669-84ed-0254bd8bed16 | -11.7589 | -43.3136 | 2025-10-10 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 414.2 |
| dee45656-bced-346f-96dd-91ddf86ae7a3 | -13.0036 | -51.041 | 2025-10-10 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5203a375-d148-3b4d-8f3b-02eaec1393f9 | -13.3057 | -47.9906 | 2025-10-10 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| eeedd9f2-5850-3d3c-a80f-b85ae592a3fd | -11.7782 | -43.3105 | 2025-10-10 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 941e68a2-55eb-3da3-8593-a6dc8413e1c1 | -9.0019 | -45.4921 | 2025-10-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d18367a5-7663-3996-9032-dc75f8e69c61 | -13.8307 | -45.8024 | 2025-10-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| ab92bfa6-92f9-3beb-81f0-81b52743ace2 | -10.1517 | -44.5984 | 2025-10-10 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6645d89c-dd14-3324-860c-29180ec7c6fe | -13.8311 | -45.7793 | 2025-10-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 9bf5fae5-f815-3a69-8498-6afeb4eba3ef | -13.8496 | -45.8223 | 2025-10-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| d41665b5-6ce8-3a1a-a235-4a143dacf319 | -11.7585 | -43.3374 | 2025-10-10 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4a5ed1a7-1f66-3997-9275-ea5c232b73fd | -11.6852 | -47.5263 | 2025-10-10 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6241fe35-dd84-3463-92e2-5d0617869a3d | -10.8542 | -47.0977 | 2025-10-10 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| dc01c454-a700-33e1-98ba-a68cda1ee8dc | -13.3295 | -47.7417 | 2025-10-10 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 4a2ca830-a76f-34bd-b901-82633c4b4b66 | -14.9372 | -46.7591 | 2025-10-10 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4aa48371-dfd5-3c14-916f-b963e1164f4a | -15.0962 | -46.6167 | 2025-10-10 13:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 117.1 |
| dc057100-ea27-3af2-98a7-5dbd0555da22 | -13.3488 | -47.7388 | 2025-10-10 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 0cf61198-4353-3b1c-abcb-8bd0ad2b276f | -13.8491 | -45.8454 | 2025-10-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 199daa01-5640-325a-b593-91b49d35d9f4 | -12.6873 | -43.0884 | 2025-10-10 13:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| d2b49eae-b427-3980-b35a-7edf625014ff | -14.8884 | -47.2226 | 2025-10-10 13:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| aa7b365e-9fd5-3851-8f09-b365cb7ea5df | -14.4258 | -47.9974 | 2025-10-10 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d33e61c9-02dc-3970-81aa-ad75c47b1b13 | -8.4844 | -46.134 | 2025-10-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 152b05df-1c43-3638-bd37-d4a01d4b6926 | -12.3592 | -47.2335 | 2025-10-10 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0e0cebe6-26fd-3080-a35b-4a8af0e2f698 | -14.8433 | -48.4665 | 2025-10-10 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| de214d01-bbf9-3205-9070-dd0aadeb6a55 | -10.6516 | -46.6753 | 2025-10-10 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 70cca3b5-c143-37ed-b144-73097c62de82 | -10.1898 | -44.5934 | 2025-10-10 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 39f98ca5-652f-3567-958c-5ca9a5845162 | -10.1707 | -44.5959 | 2025-10-10 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 63a79653-4238-3165-a3a0-dbb2136d5624 | -17.284 | -58.0793 | 2025-10-10 13:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| f55572cb-26b0-35fc-bfbf-d7dacb54ac42 | -14.8628 | -48.4634 | 2025-10-10 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 56e98bfb-bed9-3180-bb09-b8f9e1933ece | -8.5029 | -46.1545 | 2025-10-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7c821a02-d739-3255-95dd-82a5b3c42206 | -11.323 | -47.5287 | 2025-10-10 13:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 01eeeb38-d883-3a2b-9571-b3aa32de37db | -12.6873 | -43.0884 | 2025-10-10 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 116.8 |
| f4096ee1-d5d4-37bb-b0b6-52c9f6d163c2 | -13.8496 | -45.8223 | 2025-10-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3f59c09b-ba43-34be-8655-46cd8a5b7e94 | -10.1707 | -44.5959 | 2025-10-10 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0b25c144-cc53-3202-aee0-4e7e1da0a8f4 | -13.3295 | -47.7417 | 2025-10-10 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| b26b9641-d23c-306f-813c-d27acb644743 | -10.1898 | -44.5934 | 2025-10-10 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f86306d6-07a9-35f6-bb50-75cd14eb9f96 | -8.9005 | -46.0233 | 2025-10-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 66690b5d-ae66-3396-ae94-71820a753a19 | -8.9008 | -46.0007 | 2025-10-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9426e075-1923-3d36-a9dc-388766c5345a | -11.7585 | -43.3374 | 2025-10-10 13:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f7c00e38-1013-340d-9e59-5bcd442cbca1 | -8.2071 | -44.2032 | 2025-10-10 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 13bd07d3-51ec-3b2b-ab46-04bfa362b219 | -12.3592 | -47.2335 | 2025-10-10 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e4832ced-a0dd-3ae0-8a04-c32a778c9079 | -10.8919 | -47.1153 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d42097d9-89a1-3658-90fc-ccf2ee6cd277 | -8.4844 | -46.134 | 2025-10-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 5417b406-60d0-347d-a84d-cf56de94ce50 | -13.3488 | -47.7388 | 2025-10-10 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 3cab684c-eae0-3288-96ab-4a579e67b191 | -17.284 | -58.0793 | 2025-10-10 13:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 0d50b9fe-3d9f-3e95-8fcb-4b912464ae56 | -13.3681 | -47.7359 | 2025-10-10 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 04aaac6b-fd3e-32ab-a3c0-45d6cc4734b1 | -8.5032 | -46.1321 | 2025-10-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 77b16b83-06bf-3ddf-933b-de3d2fee784f | -10.8538 | -47.1201 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f3f12997-4fad-3b60-aefc-f086d1ab6db4 | -12.5541 | -48.1419 | 2025-10-10 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 102f5989-f5c2-3617-819b-7c9a4d883be2 | -14.8884 | -47.2226 | 2025-10-10 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c9ac29b4-18e1-3bf6-a975-cf9e98f6d137 | -9.0022 | -45.4693 | 2025-10-10 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 9ee3b5b2-13a9-3c06-8c1b-844ce697681b | -11.323 | -47.5287 | 2025-10-10 13:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 961a0f44-d654-305b-9a81-18517a33b97d | -13.8491 | -45.8454 | 2025-10-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| b004cc44-0456-30de-82e0-eab71fc15683 | -10.8545 | -47.0753 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9690cb82-6ad3-3890-9cf5-731a550b5a1f | -11.7589 | -43.3136 | 2025-10-10 13:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 462.6 |
| d99cd6c0-8112-3a24-950c-4ed19647851a | -13.0036 | -51.041 | 2025-10-10 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 8ef7a422-fde3-3fd2-b972-43d4ae4b5c77 | -14.4258 | -47.9974 | 2025-10-10 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3e0f1e97-77fd-3771-a790-5f30409f680b | -13.3484 | -47.7612 | 2025-10-10 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c1ae1bfa-7bd4-3487-90d5-b0cc46e11985 | -8.5029 | -46.1545 | 2025-10-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| d64e641b-8379-363b-990f-d3362f437d8a | -10.8732 | -47.0953 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 72a3f379-c240-3e15-8837-d4b8bfc978bb | -10.8729 | -47.1177 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7c51a825-a23b-38f1-8420-529123155b9f | -10.8735 | -47.073 | 2025-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 353a937c-0cc4-3b79-ad70-811b47a46532 | -10.1517 | -44.5984 | 2025-10-10 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 806b6970-e598-3f12-b1a6-75719470a06e | -10.6513 | -46.6978 | 2025-10-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 35c08f6e-6cd2-35e4-a6c0-0857f5a583cd | -8.9008 | -46.0007 | 2025-10-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a2e68945-ea51-3f6d-9caa-0048e5bb33e2 | -13.3295 | -47.7417 | 2025-10-10 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 25df818a-3a78-3a8f-b22a-a16817fca4dc | -9.2973 | -46.0026 | 2025-10-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fcb33467-28eb-30fc-bc90-459a4c99b5e5 | -13.8491 | -45.8454 | 2025-10-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 9f60afad-c88f-315e-9cf3-eb8974321e48 | -8.5052 | -45.9744 | 2025-10-10 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| fc16f42f-c0b5-3210-9b75-7f8f8220a119 | -8.5027 | -46.177 | 2025-10-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| bcc24e80-ae79-3e59-b20b-579a88a1f129 | -14.8628 | -48.4634 | 2025-10-10 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9ded5b53-f451-3540-96a4-2fc8b3a3649e | -13.0033 | -51.0624 | 2025-10-10 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ca952ca6-0e8d-3d31-97a2-6b89529d6121 | -10.8919 | -47.1153 | 2025-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c76f5b5e-3ede-3b46-af0f-8eded807e9f8 | -10.8735 | -47.073 | 2025-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ad977223-5b3a-384a-8b05-6daeb9de5fc7 | -12.3592 | -47.2335 | 2025-10-10 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 652aab46-ff19-3d83-8eb1-e79bace207bb | -10.1517 | -44.5984 | 2025-10-10 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README53.md)
