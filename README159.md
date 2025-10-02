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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97feca38-643d-3594-976a-cd3e86108775 | -7.5744 | -46.8222 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a0b5fcb9-f4c7-39a9-9455-8367d17dc3dd | -6.0997 | -42.4865 | 2025-10-02 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 312cfc00-1b7c-39eb-a682-47517fe32317 | -12.7623 | -50.5782 | 2025-10-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0d5b9fb7-d860-3a9c-a859-41c16f36a8b8 | -9.9186 | -43.6978 | 2025-10-02 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 8ca22190-3952-371e-aeea-0dd98fad0f38 | -14.4947 | -48.4329 | 2025-10-02 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| b25935be-e225-36d3-9f4c-bdbe89e3c5eb | -10.1845 | -50.2487 | 2025-10-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 08125bd8-9e9e-38e4-a6f9-1993b1d23ec8 | -9.4086 | -47.5521 | 2025-10-02 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 14706b07-9589-3c03-ab5c-a8a4b7689cba | -14.3114 | -45.9967 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0bf679bb-9aee-39de-8605-8f383b35d860 | -9.4275 | -47.5501 | 2025-10-02 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fc282ed7-f6f9-3c64-b185-ecbd2a7e898c | -11.6314 | -45.0646 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| a9260db8-ba35-3785-b9dc-fec7a9a85fe8 | -15.2865 | -45.0986 | 2025-10-02 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 15b44629-4f78-362b-bd1e-3537f35545e5 | -14.2924 | -45.977 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 61bf9d1b-e2e6-38b1-a69d-b7e28f62a3a4 | -6.1981 | -43.9286 | 2025-10-02 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 51511ddb-7c48-3806-af17-1ca7c48d974f | -12.5001 | -50.2453 | 2025-10-02 14:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 169.1 |
| a05ff796-e8c5-3c3a-b023-cc6080c4a769 | -6.1796 | -43.907 | 2025-10-02 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 39080406-b4ef-3a91-afac-234a1c29f9f3 | -8.5201 | -47.8386 | 2025-10-02 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 3117fce8-bee8-360f-9a7f-78ba834c652d | -11.157 | -47.1935 | 2025-10-02 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3469dfe4-2ede-30aa-9a00-949333d2efa6 | -11.8242 | -44.9901 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8663a7ff-5764-3777-8eaa-627a4a9836df | -9.9376 | -43.6953 | 2025-10-02 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 15f04c17-e3cb-38d4-87c2-6af42961afa5 | -9.336 | -45.9305 | 2025-10-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d91694de-9adc-3787-bccc-6f5ab707608c | -11.8101 | -51.7957 | 2025-10-02 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ae1c5ed2-d4e4-3d49-8258-92143a8cc37b | -5.3193 | -43.7636 | 2025-10-02 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cc7e01af-6a03-3f44-ba32-014a949fa0d7 | -7.7944 | -42.5132 | 2025-10-02 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 212.1 |
| cbb4c3ca-db7c-3855-8f55-2940f90cf098 | -6.7814 | -45.5929 | 2025-10-02 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 75e7efaa-239f-37cf-bb9a-6d825940e21a | -8.8929 | -46.6072 | 2025-10-02 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| c937019e-7855-3acb-aba7-f225614d5f70 | -15.7905 | -43.7155 | 2025-10-02 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 06dd66d3-3548-340d-ab4f-b32f9bb2a1f6 | -14.4055 | -46.1414 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 622299bf-b6d0-3d4b-aeb9-2e876ce8bf9d | -10.9561 | -46.6594 | 2025-10-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 9c0d308d-8d2f-3268-b7a5-39fefc636167 | -6.679 | -42.8136 | 2025-10-02 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 3046350f-93d1-33d9-945f-0b3dd66460db | -12.7627 | -50.5567 | 2025-10-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| fb714b0d-af2d-3052-ac28-e564498caf73 | -11.843 | -45.0104 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| db2a9b11-7ed1-3e84-b1b6-dbb3602edba7 | -9.9182 | -43.7212 | 2025-10-02 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 241.6 |
| 632f1091-ada5-3ca9-aef0-50fc194b1c8b | -11.1746 | -47.2805 | 2025-10-02 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ffacf909-89a2-3120-8d16-da01715a3d7f | -11.8291 | -51.7937 | 2025-10-02 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ee622273-f718-31d6-b8c0-6f4411d49e5d | -8.5272 | -47.2437 | 2025-10-02 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7c85160e-beb9-3290-84e8-01062b457df4 | -9.8896 | -46.9226 | 2025-10-02 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 6d52ada2-3af4-37f1-978f-109d3ecd2fe8 | -11.0897 | -47.846 | 2025-10-02 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 6bdaa136-ee1b-39f3-8b80-0ba0320ee0f8 | -12.4998 | -50.2668 | 2025-10-02 14:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 837ea591-f06f-3159-9106-1940e1315fc3 | -11.6318 | -45.0415 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d07d8f88-8ecb-33a4-8f1d-e2a79d8e8588 | -10.9748 | -46.6794 | 2025-10-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 48f45cea-b025-3bda-befd-39fd58573ddd | -8.527 | -47.2658 | 2025-10-02 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ef6f0878-cf20-3a59-b541-2d1eebab68cf | -10.6802 | -48.5758 | 2025-10-02 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fe8f1356-061f-341f-88a9-6a61cf1938c8 | -10.2217 | -50.2876 | 2025-10-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 350f2cb4-a766-3eb9-ba65-026588511ab3 | -9.3392 | -45.7039 | 2025-10-02 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 43f8131c-11b8-3de3-8ea8-505d4c73ac54 | -8.1702 | -44.1377 | 2025-10-02 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 6a42b758-5b49-3440-b725-cfb9372b8635 | -11.1175 | -49.806 | 2025-10-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5203f0dc-8dfc-3dee-b192-dd7e86373d0f | -15.2738 | -49.3073 | 2025-10-02 14:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8154a5d2-5b3e-34c6-99ac-51fb9ea9fad4 | -14.3309 | -45.9933 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 270ffe0a-2b48-3da9-b0de-d8d1e6666168 | -10.2028 | -50.2895 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9892a0b0-4dfe-3122-ab49-e2192fe92131 | -7.8405 | -48.2053 | 2025-10-02 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 4eacda47-7bbe-323e-bfff-df53e588067f | -11.8104 | -51.7746 | 2025-10-02 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b45df0a0-7f9d-3359-8a45-ca9e944e6cf1 | -9.9031 | -45.978 | 2025-10-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3f75e7c8-e9de-3f22-8819-7066fdf0b07c | -9.08 | -46.7215 | 2025-10-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| cfb97d0a-4eba-39ab-88de-5d98f00b13c4 | -18.2171 | -53.3392 | 2025-10-02 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 262.5 |
| c5cb2773-f5bc-381d-b136-0034d9574bba | -10.2212 | -50.3303 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 385e9a30-f103-30e6-9ae0-39266b8f0684 | -9.336 | -45.9305 | 2025-10-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| edcc45ed-a322-352d-9a49-cef69652da98 | -14.1727 | -46.1354 | 2025-10-02 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 155.8 |
| b329a899-c681-38f0-ac36-5540c61e1b3e | -10.6802 | -48.5758 | 2025-10-02 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 47b321f1-3347-3626-991c-ba1a2c0cbe42 | -6.6978 | -42.8118 | 2025-10-02 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| d7a7e9f2-9548-3ee2-be44-2e95d9cfa58e | -6.679 | -42.8136 | 2025-10-02 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 57aee4c3-aea8-35c3-9bd8-b7c5a01c7989 | -6.4945 | -44.2962 | 2025-10-02 14:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 05595d33-e95f-37a6-848c-7eeddade8d03 | -11.8238 | -45.0132 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| e9707f7c-b9e0-3a76-a09b-957e1bf9f2e3 | -5.7223 | -42.6826 | 2025-10-02 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 3052dfc0-69d7-3638-acd0-4e7b752be3c5 | -6.2411 | -45.3198 | 2025-10-02 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 49fc29b0-7280-31f1-8574-54523f51b9bc | -9.9186 | -43.6978 | 2025-10-02 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| f0261bc8-451e-39f6-be5b-503702d8ebb2 | -11.6318 | -45.0415 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 1770045c-ada6-3286-b377-254589cd2706 | -11.8242 | -44.9901 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9a1fae87-fe08-32fb-aeb6-be60a8892287 | -15.7905 | -43.7155 | 2025-10-02 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 417.0 |
| 11fc84ed-69d4-3dd8-a0a5-09b11bc5f708 | -14.407 | -46.0722 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 82324b95-df36-3cad-b6b6-cf7c36ad4873 | -9.8896 | -46.9226 | 2025-10-02 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| c10a37bf-1f3b-30aa-a71f-aff0a41a9eac | -6.7163 | -44.6216 | 2025-10-02 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 43a46cd3-85e9-3598-9f69-1d3e7a6fe690 | -15.3067 | -45.0713 | 2025-10-02 14:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 89adbd1b-5c70-3895-84cd-ef580bde642b | -13.3611 | -48.1159 | 2025-10-02 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0a6a027d-a7aa-3818-b6ba-cf1e6de11b5c | -13.3089 | -47.8118 | 2025-10-02 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| a5baee02-9a59-34e2-a805-f70a0b2cb679 | -6.7656 | -45.3004 | 2025-10-02 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5ac60eaf-9bb8-30e3-9ec4-5d54dc99029b | -6.1794 | -43.9302 | 2025-10-02 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 25e828d1-e5dd-391d-8050-b967b50b423d | -12.5005 | -50.2237 | 2025-10-02 14:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6294b901-448d-3173-b2b3-87b1f71269fa | -7.8692 | -47.3048 | 2025-10-02 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2aed30b8-4fc0-3315-b64b-98ad4217a69b | -14.2924 | -45.977 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 5766eb63-5e21-3e1e-8e23-82326d1a1544 | -11.8349 | -47.7067 | 2025-10-02 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8fd9b87a-19b3-3221-9f13-0330642372b3 | -9.564 | -45.8594 | 2025-10-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 8f9f88c8-abed-308f-bb26-3e6a5c931f4e | -13.7873 | -51.2189 | 2025-10-02 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4fc55fc2-0965-38be-9f45-9f9e48424b1f | -14.4255 | -46.115 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 831f4abe-a314-367e-930e-5d1b09add299 | -10.1839 | -50.2914 | 2025-10-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| dd5bddb9-5b6f-3eb7-abf0-686d8e16a7ed | -8.1513 | -44.1397 | 2025-10-02 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 89f2640b-d6a7-34b1-9d7a-34c8e9576f39 | -11.1175 | -49.806 | 2025-10-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3440f772-879e-3296-a907-3d5b91cdacce | -14.3309 | -45.9933 | 2025-10-02 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 164fc609-7721-3455-b6e6-35fe9267beda | -18.1968 | -53.3638 | 2025-10-02 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 8bf6e5aa-66a3-39c2-9ca4-e06f662eefab | -13.7962 | -47.5362 | 2025-10-02 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6d6f9d9d-c1ce-3de2-8394-8cf7a8c2e5f4 | -18.1972 | -53.3423 | 2025-10-02 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 62c660c1-6699-31c0-8b49-c8680e040450 | -13.7684 | -51.2 | 2025-10-02 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 056fe3a5-e721-3517-8eae-96d146783a30 | -8.1917 | -47.0101 | 2025-10-02 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e3d45d06-19c2-3b49-a5e1-475feeee29ba | -9.9369 | -43.7422 | 2025-10-02 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 177.1 |
| 1a5fd383-3ca3-35e1-8f3b-360998856e2b | -9.3392 | -45.7039 | 2025-10-02 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 3d6993f0-66c5-33a4-bc4c-d673c71a673a | -11.0238 | -51.0767 | 2025-10-02 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9dd0d4b1-2162-3cec-bfee-d7138f5b0606 | -15.7899 | -43.7397 | 2025-10-02 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| c9a34a6c-b904-3d5b-b435-a444f0597469 | -11.6126 | -45.0443 | 2025-10-02 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 81bba198-f164-3280-8356-0ad6cceb97d1 | -9.583 | -45.8572 | 2025-10-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1874e50b-2473-39fb-8b06-35aca5cf17a4 | -11.8291 | -51.7937 | 2025-10-02 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e42ff1bf-cafe-30ed-baf2-c798cfd53f4e | -7.8092 | -47.6399 | 2025-10-02 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |


[Clique aqui para ver as próximas entradas](README160.md)
