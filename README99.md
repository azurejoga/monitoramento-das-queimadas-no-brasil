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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5970ec5-c00a-3739-925f-3a693e3823e1 | -14.2543 | -58.6082 | 2025-08-25 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c33f4746-a7c0-3582-94f2-250d3152c252 | -21.4089 | -47.621 | 2025-08-25 14:30:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e3647bab-1668-30ba-95be-0896b964e0d6 | -10.7209 | -47.1142 | 2025-08-25 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 41eef7ac-8ea9-3bb1-8373-c40929a0c056 | -21.4303 | -47.5922 | 2025-08-25 14:30:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1016.8 |
| c8713e9f-71ed-3e8c-b2ad-23f91ec940c7 | -8.1304 | -62.8763 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b94afa30-10d5-3c64-a452-0d9bf9c270f4 | -11.5722 | -46.2844 | 2025-08-25 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a8e22242-5830-3881-baf7-d6d2cd56ba61 | -8.2129 | -61.3739 | 2025-08-25 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| dde35e5c-be5c-34e6-a6bd-85c577e47d4d | -8.5946 | -62.5936 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 930a78b2-4daa-353e-9629-e7e89971b719 | -6.782 | -59.6519 | 2025-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c05aef57-0c8d-3248-9333-6ffd748b801f | -6.5776 | -45.3611 | 2025-08-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e4008587-d46a-3cff-86f3-f68fd27f1734 | -8.5944 | -62.6126 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b403c3f5-5a50-3f2c-8e1c-154d27bc573b | -14.3722 | -51.932 | 2025-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 791f8b9c-3068-3568-9da2-44417bd57d2f | -8.6313 | -62.649 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 203.9 |
| a4123123-8f59-3148-ba92-5df3672ecdb0 | -7.586 | -47.4835 | 2025-08-25 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 434.7 |
| edc12f26-fc9b-3fb7-adff-63775842feba | -6.8201 | -59.4386 | 2025-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 8be9266f-24d6-3440-802c-208661926cfd | -8.7586 | -49.9353 | 2025-08-25 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 205.6 |
| b9d0105d-c79c-31af-8578-e9bb7aa4d5a8 | -11.6803 | -51.5777 | 2025-08-25 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| ce88d9ea-e7f6-3e58-9a1e-2d239d16510a | -14.5072 | -51.9354 | 2025-08-25 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 16ba45e2-61ae-33f0-a71d-f6579cc6536c | -6.9061 | -44.4217 | 2025-08-25 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 177.0 |
| e6ab4a13-9130-3bfa-8289-df453345a414 | -10.7206 | -47.1365 | 2025-08-25 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 46a45c5a-b80e-3d5b-b8a2-4fb2581c2683 | -8.5943 | -62.6315 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a35ec25e-390a-341d-9706-627d698441f7 | -8.6617 | -63.8558 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 908d17f3-be87-3d19-a119-9e43b8e0a02e | -10.7015 | -47.1388 | 2025-08-25 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 284.9 |
| 0bca78c1-0e36-309f-8449-bf528797b571 | -8.5759 | -62.6133 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3db876c3-f73d-35cb-bad1-966a93ca2e58 | -12.6745 | -47.8366 | 2025-08-25 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| abaedfb4-d8ec-3d8c-b3ef-fc945ce63a05 | -11.2697 | -44.9781 | 2025-08-25 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| b8c9dc85-1f39-3068-bd45-8f704ac18eb7 | -18.715 | -45.1684 | 2025-08-25 14:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 143.1 |
| eea75ed7-e5d0-3b81-9aa5-cf5e24cf0f05 | -10.2572 | -59.1081 | 2025-08-25 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 634d853e-30a1-384a-808b-4eb6673eecd2 | -6.8062 | -45.0019 | 2025-08-25 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e21ed310-5d1b-3f1c-afb0-4e984e432fea | -8.7584 | -49.9566 | 2025-08-25 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 387.4 |
| f8a1560d-f8aa-3087-ae65-919728e4699c | -9.1813 | -60.7747 | 2025-08-25 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 96d4a205-0429-3cf6-8b9f-d5970d93b1cc | -5.6817 | -45.1347 | 2025-08-25 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8be06a23-fdac-343d-9468-eb501c9bc4b1 | -7.605 | -47.4599 | 2025-08-25 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e61b8025-526a-39cc-9df6-cdfe9d595c25 | -10.7096 | -50.5359 | 2025-08-25 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 379e2015-f35d-3740-8d0b-2833981eb6ec | -8.5758 | -62.6323 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 168.0 |
| ab622ecd-4bda-32bb-833a-aca572990be8 | -8.6314 | -62.63 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0233df25-fc16-34ce-8187-071856801d8c | -11.5913 | -46.2818 | 2025-08-25 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 6c053252-3821-3ac8-896a-4f8a670da95d | -18.7359 | -45.1396 | 2025-08-25 14:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 4185bc9d-edfd-37dd-a857-3c14e0bb46de | -6.8202 | -59.4194 | 2025-08-25 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 67714011-0d00-3f76-acbb-14068fa47a88 | -11.2701 | -44.955 | 2025-08-25 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| e319b7c9-85b8-38c5-94bf-d6dc828442dd | -10.797 | -47.1048 | 2025-08-25 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| a07180a5-6066-3ebe-b289-f7903ef73b83 | -10.8167 | -48.3192 | 2025-08-25 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d87480b1-07ff-3934-9163-8b85f690faf0 | -9.5513 | -48.1744 | 2025-08-25 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 42edcebc-071f-32ba-b6d0-86fb2d280039 | -8.6498 | -62.6482 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 1c960723-7e82-38a4-b237-5f0429da93e7 | -9.181 | -60.8131 | 2025-08-25 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 05aa0954-e609-3227-aa02-a3d90884fcc9 | -9.2076 | -59.7129 | 2025-08-25 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 07794f5c-ffb9-3413-89b7-8d97cea4abbf | -14.9051 | -45.5439 | 2025-08-25 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 866ee105-f4ac-3ca8-8238-d0037f9b3f94 | -8.2313 | -61.3922 | 2025-08-25 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6a00cd50-606a-38ce-9ec5-6c04a018ed14 | -6.1377 | -44.3711 | 2025-08-25 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6059415e-76af-39cc-993b-0225aaa3eb08 | -11.68 | -51.5989 | 2025-08-25 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| de16e1a5-13c9-3ab1-9363-c450f41bd2d9 | -8.1119 | -62.877 | 2025-08-25 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 710ed244-6751-3183-ade9-011a1532490f | -11.9277 | -46.7322 | 2025-08-25 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e1e1e07b-3926-365e-8930-4e200a76da7a | -14.9247 | -45.5403 | 2025-08-25 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 453e0a9a-ae5f-338e-afd4-c94f067b4d7d | -9.1998 | -60.793 | 2025-08-25 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1c04f859-e145-3d82-9c74-95bb136acbc4 | -11.5917 | -46.2591 | 2025-08-25 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| e0d77b05-e676-31d4-9479-0877cd8c4c7c | -11.6089 | -46.3699 | 2025-08-25 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2bfaeed1-9122-305b-89b4-68474b8ed6de | -8.1119 | -62.877 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2d65eef7-519e-3538-96be-72fe8a653bc9 | -8.5759 | -62.6133 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.4 |
| b11c0cb5-c1b2-3c59-9fdd-e2fe774256e0 | -8.0652 | -44.9989 | 2025-08-25 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 44fcf4e8-f8c2-3491-9849-240676abf92b | -8.6313 | -62.649 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 218.8 |
| 56fa34b8-07fa-3cdb-b0be-67b2b7798afa | -5.8612 | -43.8858 | 2025-08-25 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 07bab094-674f-307f-a686-84ee967b844a | -8.5943 | -62.6315 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4fe7cea3-2ded-331d-9579-fb512d191146 | -6.782 | -59.6519 | 2025-08-25 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0ec5c324-25da-34d8-bfed-a35eec2e65fd | -8.5946 | -62.5936 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f8206a08-c5ae-36eb-b23b-1e29f20ff1d8 | -6.5776 | -45.3611 | 2025-08-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f50ed679-5cb0-308b-bfda-541b1d8492e5 | -14.3722 | -51.932 | 2025-08-25 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a01d47d7-bf72-3a90-9dbb-4aaa42381cdd | -6.8201 | -59.4386 | 2025-08-25 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e0c68ed9-3b62-317e-910b-eea02013a30a | -6.2576 | -47.6082 | 2025-08-25 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ea892d41-e8ba-3066-ba34-382a325f8c9b | -8.5758 | -62.6323 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 963f7313-cafa-3463-8cd6-9d687785208d | -8.7586 | -49.9353 | 2025-08-25 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| f2db99bb-50fc-3a9c-a3e9-efb55d8208e9 | -6.0267 | -44.2189 | 2025-08-25 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| bcd15cb8-4e1e-383e-98ca-908b6b271b67 | -6.3319 | -47.6467 | 2025-08-25 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6ab99efd-6163-345a-85eb-f50eeba4ec87 | -9.1812 | -60.7939 | 2025-08-25 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 210.5 |
| bf3cd0ed-3d9b-35cc-b20b-3755826d9bee | -11.9277 | -46.7322 | 2025-08-25 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a8307580-6487-3887-b02c-1738548c9698 | -11.6093 | -46.3472 | 2025-08-25 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f326182f-191a-38a0-b4bc-87cf2d8c7fd7 | -8.5944 | -62.6126 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f57a39cc-20fd-3e0c-9172-4710521fd1cf | -5.6443 | -45.1373 | 2025-08-25 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e97ce45e-456d-3ebb-be65-c8463034faea | -6.1377 | -44.3711 | 2025-08-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e0404669-d1f6-321c-a2dc-c19b795dff0b | -6.2575 | -47.63 | 2025-08-25 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a7e5d545-556e-37f4-9987-e84a6fa38c4f | -12.6937 | -47.8339 | 2025-08-25 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| d2b2f792-5520-348a-a78a-c165dac3a803 | -6.8202 | -59.4194 | 2025-08-25 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| e634acee-4ff1-3d97-bf0c-8b7f07b2631f | -8.2314 | -61.3732 | 2025-08-25 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4d45a046-0846-3a98-a6bd-5df99fffa107 | -8.7584 | -49.9566 | 2025-08-25 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 300.0 |
| f157e75b-bd58-37f4-8d1a-5d69e58c13f4 | -9.1813 | -60.7747 | 2025-08-25 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 881ee150-e274-3524-866a-f4c5ac185c9a | -10.2572 | -59.1081 | 2025-08-25 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 84235b04-ef2f-3d98-80b0-c52e088fd0f4 | -10.7096 | -50.5359 | 2025-08-25 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c8dff26f-03cc-3986-a71b-17edcdf66efa | -10.4054 | -64.3911 | 2025-08-25 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6bf2855f-6fa8-3c02-8f7a-fd344e4d5bee | -13.4393 | -47.0287 | 2025-08-25 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2ee38320-9fa2-361f-9918-1471336b9664 | -9.1998 | -60.793 | 2025-08-25 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2b2f6a41-5aca-3c8b-b35d-8092ac83317a | -7.586 | -47.4835 | 2025-08-25 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 127b04fa-1e48-31a6-ba69-6b662297f906 | -7.4224 | -60.6236 | 2025-08-25 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 882c2bc9-3d25-3656-a889-4a97a547b01e | -7.5862 | -47.4615 | 2025-08-25 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| f4d73827-c297-379d-9baa-9ed739058d7c | -5.4364 | -60.1779 | 2025-08-25 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 21b1afd1-8714-3725-9ad9-8d8e2d4614ba | -10.7093 | -50.5572 | 2025-08-25 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 3204d50f-b44b-3360-9c6a-5dde7f419e2f | -8.7582 | -49.978 | 2025-08-25 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 6d11dd72-63b2-3ef0-9742-36d678e63832 | -9.181 | -60.8131 | 2025-08-25 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| cffe3fd9-b7cf-3279-be1c-7efdb87cebf2 | -8.1304 | -62.8763 | 2025-08-25 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| cbc9b3e0-1cdc-391d-9fd5-da0c922ebfa7 | -6.9063 | -44.3987 | 2025-08-25 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 152cb718-bd10-37a1-8f14-d63b2f6a0c98 | -8.2313 | -61.3922 | 2025-08-25 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 73ae00f8-3108-3ce4-bbe7-90db5357da1f | -8.3532 | -49.3071 | 2025-08-25 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 199.5 |


[Clique aqui para ver as próximas entradas](README100.md)
