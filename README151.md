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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9518f0df-f2cc-38cf-b95b-0429aaf90c3b | -12.66768 | -54.65904 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc0f8eeb-2343-3af7-b035-8ba004a0628d | -12.66617 | -54.66866 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e3840639-1264-341a-a69a-3acd1e07383d | -12.66465 | -54.6783 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| efbd4bfb-f208-3c01-9ac5-17e8cf6d9bfa | -12.6556 | -54.68096 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cde79ea8-7a20-3497-b9e5-b1831e54231b | -12.60059 | -53.16601 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ae4418fc-4767-3852-a7bd-cf3877f7be4d | -12.59924 | -53.17502 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5880c385-c58c-3b71-9fb0-94b8767600b6 | -12.59173 | -53.16465 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5e02645c-5f34-3e14-826d-5719c46d293e | -12.58288 | -53.1633 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 20f89010-aa60-3b09-a24a-2a6819389e70 | -12.57402 | -53.16195 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 98fd2458-74a9-3227-b2b1-16e5caee43ae | -12.5386 | -53.15652 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 53aae738-6a2a-35e4-9989-6646bc05b818 | -12.53724 | -53.16554 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 26d256b2-2d32-3346-9811-7f7c00fb5eec | -12.5325 | -53.49762 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 630307a4-6b3c-3903-a2b9-7ae8d6346282 | -12.53113 | -53.50668 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 415ccba9-0952-3ac3-b56d-d8db421fe486 | -12.5141 | -53.18387 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5022e5f7-5f90-3c2c-8fa5-18b26082d5de | -12.50927 | -48.92683 | 2024-09-26 05:42:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2c7d6530-1aab-3165-9c64-698bcfa00704 | -12.50041 | -48.91219 | 2024-09-26 05:42:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 76ed7d2d-ffdc-354f-b479-58f15cddeeca | -12.49868 | -48.9254 | 2024-09-26 05:42:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 732d4b37-98b0-3d31-b993-970f43369845 | -12.49698 | -53.49213 | 2024-09-26 05:42:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 28f477e8-e2d3-394f-94f1-0217dd36d2fe | -12.48981 | -48.91072 | 2024-09-26 05:42:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 25e2ab34-e10d-3977-8a30-45d8206ec079 | -12.48809 | -48.92391 | 2024-09-26 05:42:00 | AQUA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c950ff04-6b6e-3058-a52c-41d2e6d25b94 | -11.95261 | -60.3642 | 2024-09-26 05:42:00 | AQUA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| dde0a9b4-52f8-312c-b8f6-b5d95e0e5cd1 | -11.84539 | -49.61497 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4a111e1b-c7ca-3b42-947c-3dfdf73153eb | -11.6675 | -54.44519 | 2024-09-26 05:42:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8a19ef3d-8125-36e1-b3b8-50640693b21c | -11.60136 | -60.34736 | 2024-09-26 05:42:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| b4fdf90b-a210-33dd-96fa-2487deddf7c7 | -11.48636 | -56.77222 | 2024-09-26 05:42:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c5e0cb15-ef52-3db0-a3b3-6c3093a320dd | -11.28521 | -57.52067 | 2024-09-26 05:42:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 395a30cb-0515-3859-91ba-04e3fc415d5c | -11.28472 | -57.51503 | 2024-09-26 05:42:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9efaf8b9-7ced-345a-a304-11f13ea7582d | -11.2186 | -51.15342 | 2024-09-26 05:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f6a113e1-5d32-3a9d-8465-9ac98b6bde19 | -11.20964 | -54.77038 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a0b3f4cc-52c9-3357-9ded-bba86dd2b297 | -11.20947 | -51.15209 | 2024-09-26 05:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 11c399dc-031e-3d29-b9a7-fd875f019c20 | -11.20806 | -54.78044 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 05035ed5-c06d-31e4-8b34-2e68ee80918b | -11.20189 | -54.7589 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 768034a2-a4ed-3294-a3e2-8bb19927ca0e | -11.20032 | -54.76889 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 4bbd2087-527b-3218-86ab-3cbb1f6e2649 | -11.19874 | -54.77892 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| d723e609-9f3c-34b3-af35-0b3e323aac38 | -11.19727 | -53.89822 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cd7b7dfb-a54c-33e2-8070-ca53b7f1f401 | -11.19716 | -54.78899 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5c761c66-6feb-378d-9520-1fefb4258b68 | -11.19585 | -53.90751 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 221bc09e-9e26-3b55-8148-82542d21d85c | -11.19257 | -54.75745 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 76567936-89bf-3b53-a762-afd843a8b286 | -11.191 | -54.76741 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 62de27e7-e2f5-3076-bbed-a8395201eb66 | -11.18942 | -54.77742 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 96675f32-00aa-3731-ac09-91b18b0073c1 | -11.18167 | -54.76595 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b2295fdb-46d8-3025-8d13-d71d3e8bffa4 | -11.01493 | -53.94338 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c1defff6-f467-3de6-9ed2-5856db11721f | -11.0135 | -53.95273 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3b1c628-e94b-36db-9e14-af2e20e16c1f | -11.00732 | -53.93265 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a96f6df9-8f12-3d68-9352-adf483f6dff7 | -11.00589 | -53.94197 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3d2e45d-fe3c-3e34-a5d9-16f2bd4ebb8b | -10.95798 | -55.77044 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 575a2132-4918-3b6d-bf1a-229cdfc477f0 | -10.92765 | -54.26933 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 888599ac-b1c1-32b1-8854-b35cb5a86ce2 | -10.88502 | -57.42133 | 2024-09-26 05:42:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 10a985df-0ba7-3f07-938c-86927e26e66a | -10.86653 | -57.46368 | 2024-09-26 05:42:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| babccf19-5e7c-373d-b9d6-a21317c042a5 | -10.85777 | -51.16375 | 2024-09-26 05:42:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0188f718-2ab7-3cba-a7bd-da5ef5dad7fc | -10.84867 | -51.16243 | 2024-09-26 05:42:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 91670d6c-a7b0-35e6-a6c8-17c8d1994700 | -10.60575 | -51.11877 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c78c10c-473b-3222-8c64-9716ed18c4ce | -10.58162 | -54.23925 | 2024-09-26 05:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74f4cf27-98e2-3740-b9c2-a55b3074669e | -10.53159 | -51.11808 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68e0cb45-d0d7-367b-b143-8c808ae545e6 | -10.51708 | -51.15454 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 376444eb-4ca9-3f6c-b7b0-d233664b3f4c | -10.50627 | -51.22992 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b2bba1a-3d7e-39e1-9b35-8dd7e1460c58 | -10.46386 | -50.76312 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b43d7ad7-1fa2-3e2c-8b97-3976a0a71577 | -10.46246 | -50.7728 | 2024-09-26 05:42:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b381e3ba-4084-3aec-ba3b-43061dfd0d34 | -10.45583 | -53.30519 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 226f151f-9912-3fcb-bb0d-f2846ece04a1 | -10.45445 | -53.31428 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 66256596-14a7-390b-9159-791c9c5f5427 | -10.44691 | -53.30381 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9e7ab9ab-dc78-3049-a138-841d10bc6098 | -10.44554 | -53.31289 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e75676a8-3271-3f51-a8e3-c3c79875860d | -10.4153 | -53.69879 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed0b2080-2d92-3a54-8bb6-634338b00744 | -10.4114 | -52.93174 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5ee72467-f4c6-3f40-b26f-ca9f31e9ebde | -10.39091 | -58.88499 | 2024-09-26 05:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d3e786d8-7e45-30db-bb61-1a3d5674a38f | -10.37625 | -58.89445 | 2024-09-26 05:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 97993490-24cd-3dcf-80c0-529f53ea57b6 | -10.36655 | -53.77105 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 910c7c2c-dd24-3913-8750-2bc370f726e4 | -10.35752 | -53.7697 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b2be58e4-1276-3ecc-b72b-1fdc2b79709d | -10.35609 | -53.77901 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 95b8a695-acd1-3ae5-85e6-a9c8ea9df08f | -10.31464 | -56.76094 | 2024-09-26 05:42:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8780af14-22df-364d-856d-9fd6ffadb028 | -10.28465 | -53.03555 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a9a79032-13f9-37db-86dd-b0a0d5043e9b | -10.1258 | -50.01246 | 2024-09-26 05:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 81bc7d0a-297e-3ac7-8d67-03c6c9cbebb5 | -10.12128 | -50.01579 | 2024-09-26 05:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ba84dca-73a0-352e-8e7c-d18ffcca2bb3 | -10.04465 | -53.46014 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d29b5f1-ea7b-31ec-b375-d8a38f075ba9 | -10.04325 | -53.4693 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6862557e-f4bc-34aa-aa86-038613543f4d | -10.03709 | -53.44957 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 72fe4b6e-7386-3871-8a73-2b40ef236316 | -10.03569 | -53.45874 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 686.7 |
| 9e8325c1-2aff-39a5-8360-4f5b790c6492 | -10.03429 | -53.46792 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 891.2 |
| 01026a79-8e7d-3373-9820-5e2fda0d994b | -10.03288 | -53.4771 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bae3c51e-4d7b-30c8-8162-f1f455ab1a39 | -10.03148 | -53.48627 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 37ea9453-9fdc-3327-af43-307006321ba8 | -10.03008 | -53.49545 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 136d829b-1fd3-3855-8767-d0b2271c18cd | -10.02812 | -53.44821 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8d9c9068-e043-34cc-ae02-537c29c805cb | -10.02672 | -53.45736 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 190.0 |
| bafb2020-ee94-3d83-a9ed-786136d27e94 | -10.02533 | -53.46651 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 342.4 |
| 109c9aba-d0bc-3162-933d-e135057460fd | -10.02252 | -53.48488 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c87c0b62-3b57-315b-aec8-9df9f50bb636 | -10.01777 | -53.45597 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 21dee971-555c-3ebf-b26b-740e70e571d1 | -14.83774 | -48.90617 | 2024-09-26 05:42:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 93f52840-dfe6-35b3-8220-17865f3ac998 | -13.81678 | -48.02849 | 2024-09-26 05:42:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 136f2e0b-6081-3f41-998c-69b72b0e5110 | -13.30907 | -46.3237 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 231db816-72b0-3fd3-a06b-a2a67979f458 | -13.29592 | -46.32178 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1c0eeb1e-613d-36e0-968a-67f33053d01b | -13.27371 | -50.14712 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b95bd2d7-117d-3411-bc9b-271da9f75258 | -13.19614 | -45.62835 | 2024-09-26 05:42:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 228fcb2d-a13a-3a58-9ec4-80f661d47e06 | -13.19328 | -45.65262 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 5e15bc28-7177-37af-8740-8fd829d7a2c4 | -12.97471 | -45.3079 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1ca25fa0-b5f8-3fea-b11b-ee47f0342529 | -12.96347 | -45.28072 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 911e9bb8-640d-3952-830d-119f0ce0be2f | -12.96077 | -45.27291 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 5c5ac37c-6411-3fdf-82d8-f845f4e72094 | -12.96049 | -45.30618 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2320.5 |
| 3c61ea69-ddee-3771-bfa0-c34fb84ec221 | -12.95761 | -45.29837 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2213.9 |
| ae5a00d9-0384-30f3-9b45-9cb9a65f1e35 | -12.95752 | -45.33154 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| edb74b47-8128-353f-a75c-f581d49c2b0c | -12.95447 | -45.32372 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 775.7 |


[Clique aqui para ver as próximas entradas](README152.md)
