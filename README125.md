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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e86b6892-02f6-3f65-ad62-a42a2e279922 | -17.30828 | -49.35124 | 2025-10-04 05:08:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52a65ec4-f3e3-38f4-92ea-58065aa7829b | -17.94159 | -47.02357 | 2025-10-04 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a00c2ea4-a644-3ae1-bf55-76028f6e0c01 | -17.63431 | -44.4487 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e8010d4-b2a9-3e01-84ba-c64379381963 | -18.34785 | -52.01914 | 2025-10-04 05:08:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f21166-184a-3cf5-966c-4833eeff929c | -18.2027 | -53.36134 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0683937-f9b5-3ca7-9fa5-db27b905a95a | -19.61736 | -46.69547 | 2025-10-04 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22738348-dde8-39bf-b40b-823c0ddb600c | -18.46551 | -49.44762 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31e6627e-5c13-32a6-bb72-7d0f7df15657 | -18.6392 | -50.678 | 2025-10-04 05:08:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9cbf98b9-eabb-33d5-a0a2-732c4be55703 | -21.20061 | -45.1522 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 89eccd1e-2bf1-31d5-b2fe-156720e95ef2 | -22.28763 | -46.76097 | 2025-10-04 05:08:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 5d544312-fe31-36f9-b49b-cef83ff83323 | -21.68601 | -50.06519 | 2025-10-04 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 892623b7-f1a6-31f1-8ad0-fc3ff3c16b50 | -17.07962 | -46.23964 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd326322-2b72-31e3-b1e2-79c17f5833a7 | -18.34344 | -52.01857 | 2025-10-04 05:08:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9753a46b-0d3a-3f76-9767-43bb84c5cc19 | -18.64405 | -50.67833 | 2025-10-04 05:08:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb729a96-e3e0-3f2d-bb94-63ff53357a95 | -16.39085 | -52.16182 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 105ee649-13a1-3ca9-80f8-029bc2962e3c | -18.23734 | -53.37842 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e85c0ce-e22a-3911-8ca1-b8e6df48c1c6 | -16.94058 | -52.67075 | 2025-10-04 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52449437-4d12-358d-bbbd-7198664c5e34 | -21.19953 | -45.14981 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| d19e6f02-0e7f-3185-9822-a86db9a42430 | -21.69022 | -50.076 | 2025-10-04 05:08:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 05af31dc-ea00-37fc-9959-ba55ba2bb7f3 | -16.94293 | -52.67339 | 2025-10-04 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a9e7246-9c64-38d5-ac53-c598bd760a8b | -18.59643 | -51.17427 | 2025-10-04 05:08:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8a1f08-2bd8-38d3-83e6-46c9cefb2c7d | -20.142 | -46.42196 | 2025-10-04 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eb3ab8ed-d0b9-3289-adf5-38f433e0eb49 | -17.16057 | -47.04292 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e36ecb45-97e4-312b-ac55-2acbb67c97fe | -17.95624 | -57.56256 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ab931705-9f75-3916-9f4b-735a27e97bb0 | -17.2962 | -49.27056 | 2025-10-04 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c79e5274-e6e1-3197-9a09-2eb5af872160 | -17.08493 | -46.25057 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47077fb6-0aa9-3c97-8554-3987160a41f6 | -17.58088 | -44.49578 | 2025-10-04 05:08:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c315ba3b-0be7-3c7a-b581-af5ad5da58ed | -17.98494 | -45.00909 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102a3592-4f19-3260-a284-d49dc92dcc1c | -18.19937 | -53.29124 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e496cd56-2266-3341-b352-363ef04ca43f | -17.08642 | -46.23516 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36e11c63-46bb-3ab9-9451-1010873eaee8 | -21.69679 | -50.06309 | 2025-10-04 05:08:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16bf6321-a126-393a-9e08-a877e06d4ac3 | -20.47805 | -44.82752 | 2025-10-04 05:08:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4fc2a55c-730b-3711-9d8e-a5f4dc60ed28 | -17.15244 | -47.02957 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d6dabf7-94cc-3361-947a-84cdd6820b28 | -18.23478 | -53.36673 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7339db79-4331-3aee-9d0b-39ab28a71881 | -21.78515 | -45.33853 | 2025-10-04 05:08:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 78f04b1a-c455-39c3-a8e5-00f3d38062c6 | -17.61908 | -44.46141 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42fc32fc-549d-3d36-afc0-df1a1760df08 | -16.35996 | -51.46882 | 2025-10-04 05:08:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 090c0bd1-6391-3f9b-9cb3-f6b2129c83f0 | -17.99105 | -51.63897 | 2025-10-04 05:08:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71c01d8d-e2a1-34b0-b6fe-a0e201d94430 | -18.19914 | -53.35712 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92ac363c-0cf0-33f2-aaf6-3ded6a478c80 | -22.28157 | -46.75542 | 2025-10-04 05:08:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e30f2a30-91ba-3b2c-b2e5-adfa629751b3 | -16.16159 | -57.58492 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e22796be-69e3-3ffd-b7e3-8a3811e0f167 | -17.99135 | -45.01485 | 2025-10-04 05:08:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e869da8-ba49-3e64-9bd6-ded55c7f84f2 | -17.00537 | -49.15224 | 2025-10-04 05:08:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f73af402-106f-311d-817b-dcdc35c30888 | -17.72093 | -56.77294 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cbbf9f85-047c-3f8e-9b7d-cd15b3310452 | -18.38475 | -48.79186 | 2025-10-04 05:08:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ca39bde8-664b-387b-a118-2e06b3c5936b | -18.19487 | -53.29428 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60dfc51a-9471-3cdd-a694-8eb817f56cb9 | -18.45542 | -49.443 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98564720-b8c0-37e2-9181-d0976fee3db9 | -18.20362 | -53.35413 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f7af67c-efac-362d-89b5-da0b0feda772 | -18.19512 | -53.35652 | 2025-10-04 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da7de650-fc53-34e7-b18b-4403ad95be6b | -17.07912 | -46.24481 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408ba38f-7057-334d-86bd-86d0b1935ca8 | -18.46095 | -49.44077 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a4faea9-681a-3abf-ae47-9657bff10c8e | -16.43305 | -52.16922 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a9c657f-792a-3066-9da0-6c88ae34b68a | -17.29656 | -49.26738 | 2025-10-04 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c08f6fd2-38cb-3b83-b13b-1c5d5a85d988 | -17.84828 | -46.51322 | 2025-10-04 05:08:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16b1c8b9-1e68-3cbb-9215-739ebb205ffb | -16.15883 | -57.58082 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 39045b76-ba5b-3575-b441-03d9d5f1431d | -18.17891 | -53.3552 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c423b83-3de1-3af5-aeb6-d760467c401b | -18.18298 | -53.35538 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd607e44-96bd-3bcc-ba1c-aa292a642821 | -18.17483 | -53.35508 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7450bb2-f743-3cf9-9bab-4784f98b4c40 | -18.46584 | -49.44451 | 2025-10-04 05:08:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70974e74-ef95-3221-9f56-e9ef35fb2c77 | -21.19415 | -45.14452 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 34de3cfb-1e2a-3afb-8b99-e0ee7d0f288a | -17.16702 | -47.03929 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f66df60-1612-36f8-8b35-a8245fefe7fc | -17.95678 | -57.55898 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b74b3e54-118f-39a6-bbdf-10e056df47a1 | -18.64892 | -50.67862 | 2025-10-04 05:08:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15e5b588-6e12-332b-818b-1a8ef509d9be | -19.81748 | -46.07043 | 2025-10-04 05:08:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27cb987d-8e04-3b85-9c6d-3fa6f6b87fdb | -21.19306 | -45.14164 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6216b301-0148-3c17-9f18-1a6b9b2c8d57 | -18.17582 | -53.34723 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a16b3d48-2f7f-35d3-969c-9175a429d160 | -17.08542 | -46.24546 | 2025-10-04 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4d9a7a1-868e-3a26-9e0d-fc88d5e732a2 | -17.15454 | -47.0425 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 676d7879-9955-34e8-b5c6-5c6a05bb1c82 | -17.01061 | -49.15278 | 2025-10-04 05:08:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b78ab5f-893b-3c0d-9b21-f8cbad90cbe6 | -18.18346 | -53.35162 | 2025-10-04 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04903455-56e3-3ed5-b5f8-39cf587cb522 | -17.30191 | -50.59037 | 2025-10-04 05:08:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32ca63ec-780f-3c8b-b5a7-3df3926ca3bb | -15.96362 | -57.23561 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c93c3f3-fef4-30df-8746-fd2585fa9ccf | -17.70623 | -56.75501 | 2025-10-04 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ee54f58a-f376-3637-9704-e7705c4319e3 | -21.69713 | -50.05969 | 2025-10-04 05:08:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b2d111f-8698-3e11-a031-a2f129bea7f0 | -16.39608 | -52.15454 | 2025-10-04 05:08:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1804b8ab-184e-396d-af8d-a941c2514260 | -17.99613 | -51.63468 | 2025-10-04 05:08:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed9cd39b-9ebf-3a8a-9dcf-068e18fd24fb | -21.68634 | -50.06181 | 2025-10-04 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 059deaf3-831e-3efa-a738-6c55e8e3ba7d | -19.57382 | -48.01913 | 2025-10-04 05:08:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9515ae98-6e28-31aa-99f0-e5b93d5180af | -15.96638 | -57.2398 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 386f1a22-f48a-3537-b9a2-b0015b29bdb9 | -17.71147 | -47.09032 | 2025-10-04 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd32b35-8c35-3a67-9aa2-87e852e36cc3 | -21.20113 | -45.14532 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e9a2687-9ae3-371a-bf60-ea6af276bec4 | -20.13557 | -46.42122 | 2025-10-04 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ff007a5-42ee-3f55-a480-9f31e4cdf3bd | -21.18659 | -45.13318 | 2025-10-04 05:08:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb41c295-8f24-3954-a670-ec8840b8abd7 | -17.69941 | -47.08913 | 2025-10-04 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3e6bb1b-6ac9-379c-9b77-a268827cbba4 | -16.18916 | -57.60412 | 2025-10-04 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2b1bcc15-f87f-3268-a4fc-b2bb68d3adb2 | -17.01098 | -49.14948 | 2025-10-04 05:08:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7eef9274-32f0-303a-83eb-1bfbff371388 | -17.15763 | -47.03874 | 2025-10-04 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a543368d-0025-384b-b392-b181b7194084 | 0.4675 | -60.43661 | 2025-10-04 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a77c731-0fe6-3520-8a49-765fbfe2d9c7 | 0.46085 | -60.43764 | 2025-10-04 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25e344e5-e9b2-37dd-b005-68ba942aa467 | 1.54796 | -55.83495 | 2025-10-04 05:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0fbb4c0-4606-3b45-8f74-0ffe47c12753 | 0.5017 | -50.77896 | 2025-10-04 05:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bb3ddf3-4d3c-3b8b-8edb-e02cf588fc06 | 1.0351 | -60.43273 | 2025-10-04 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9569ea8d-f20f-394f-b8ac-37f9669508c8 | 0.50733 | -50.77808 | 2025-10-04 05:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2e8ed5b-8e2d-3380-a048-d171396ab5bb | 0.46418 | -60.43713 | 2025-10-04 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0bc2eb1-6506-3dbc-a7be-766bca8e31e8 | 4.56401 | -60.64784 | 2025-10-04 05:29:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d25ba2a-f91f-3e48-9549-aff023fd6455 | -3.44216 | -43.33714 | 2025-10-04 05:31:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| edaeaeea-678e-3c35-aa8f-eb5d918dfb8f | -3.8486 | -41.56881 | 2025-10-04 05:31:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 114463a6-2bbd-3e9b-8605-741190dcd285 | -3.84716 | -41.57824 | 2025-10-04 05:31:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2afbf444-5596-3c4d-8034-67f6d6444b14 | -3.44484 | -43.33076 | 2025-10-04 05:31:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d458ac66-258a-3755-87a1-60866bbcadd7 | -3.45229 | -43.33866 | 2025-10-04 05:31:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README126.md)
