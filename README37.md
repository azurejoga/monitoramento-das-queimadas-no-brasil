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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9021dbf-99df-34ff-9134-bc63066384c2 | -18.21844 | -45.57784 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25a6726f-2c5b-3b64-bd87-645c72a550bb | -20.13035 | -41.80272 | 2025-08-29 03:51:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ee2e31f-868a-3a90-853a-96cef54d8d3a | -24.17216 | -49.56653 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3caf2dce-f6ff-302a-8797-3ec519b760cc | -23.37553 | -51.97217 | 2025-08-29 03:51:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c60e2570-d36f-3c5e-9e0d-9425a050f5ad | -20.98665 | -43.18129 | 2025-08-29 03:51:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 72b27c93-1ec5-3992-97ba-1a0dcc20e4f1 | -20.28455 | -41.30291 | 2025-08-29 03:51:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7864f861-c5b7-3010-a661-2d0b7267cd64 | -19.9467 | -45.08979 | 2025-08-29 03:51:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed8f69a0-7b3a-3254-a46e-4f6d0d379cdd | -18.57548 | -44.01684 | 2025-08-29 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34f095a9-eb80-372f-a8df-c9547a537d21 | -19.16666 | -46.58884 | 2025-08-29 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab8ec115-d297-346c-a93c-7ab4e2210a96 | -24.16293 | -49.57791 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 84c9c528-4743-3104-8325-17409fd12d15 | -19.80539 | -45.13067 | 2025-08-29 03:51:00 | NOAA-20 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e030ee80-2945-3a6a-9601-9893249e83ac | -24.17101 | -49.57193 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ccd6eb37-93b6-3fa3-b07d-8177a22cbee3 | -21.4157 | -41.9502 | 2025-08-29 03:51:00 | NOAA-20 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fcfff81-7856-3282-8123-5c9cc8ea1327 | -22.41957 | -45.43478 | 2025-08-29 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 66a90d81-54ad-3531-8a16-cd504aaaa25b | -18.5726 | -44.01094 | 2025-08-29 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e18215fd-58bb-329b-bfe0-84d9af2e8537 | -18.08714 | -44.72203 | 2025-08-29 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb4648c8-896b-320f-9b0f-1e3f5f7cff20 | -19.16229 | -46.58773 | 2025-08-29 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 177997df-a6a3-3341-b8f6-fed42d069913 | -24.16775 | -49.57903 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 63958b76-4c02-3fc7-b747-5cf8c50fd45d | -18.24998 | -45.15378 | 2025-08-29 03:51:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f07b5246-827e-3adc-8c40-104d125fe0e3 | -16.28366 | -53.62302 | 2025-08-29 03:51:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f935d43-ffdd-3914-b007-f4c60521616e | -23.67408 | -51.82074 | 2025-08-29 03:51:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f9f01446-eb84-39a7-bcc5-77c47f1b9862 | -22.54985 | -42.35007 | 2025-08-29 03:51:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4752b5f5-3ea9-366b-95fb-0619c3593b87 | -18.21923 | -45.57375 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c7b7b33-009c-33e4-8094-dad25799e947 | -24.17023 | -49.56773 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1aa404d9-ca07-3be9-bb7f-61af102378e1 | -21.29937 | -41.17035 | 2025-08-29 03:51:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c21565c6-a620-3585-b35b-150bf8920306 | -20.14019 | -44.86942 | 2025-08-29 03:51:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6effbaf0-bcd2-387b-85da-54ea380592e1 | -21.07148 | -45.58846 | 2025-08-29 03:51:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42c4214a-b880-3114-b55c-6557de2cea32 | -20.9874 | -43.177 | 2025-08-29 03:51:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bbea2b2d-52a4-3e4e-8bc1-417eb376c787 | -18.21685 | -45.58608 | 2025-08-29 03:51:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c72d6ec0-a6c7-317b-b458-38c49e0c7b7a | -19.52755 | -43.91864 | 2025-08-29 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a6a4dee-b03d-3a4e-8f61-3e8c5332ed1a | -24.16423 | -49.57202 | 2025-08-29 03:51:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 262243bf-b6f4-30f2-bd1f-d75d11824086 | -23.37459 | -51.97622 | 2025-08-29 03:51:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8168e81-d85e-38bc-a1f8-540176bc6180 | -20.37514 | -43.97231 | 2025-08-29 03:51:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 737aebeb-1ad0-3d73-be46-279d3689a829 | -28.73179 | -55.65988 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 6b2031c4-b2d1-3cf2-b4ca-d09e7cd7d957 | -28.73011 | -55.64107 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 567a43e2-dd15-3ce2-bd3b-18be006e31e9 | -28.73323 | -55.65436 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 0b8b729b-1a85-3dbb-a9c9-8682d5bf17a8 | -28.69906 | -55.58336 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 93b0fccc-1c4f-30ef-97fe-ff9535303ca7 | -28.69762 | -55.5888 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| a697f65b-dfef-3515-afbd-7548a465b72d | -28.72864 | -55.64666 | 2025-08-29 03:53:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4d47548d-f866-3921-ac6e-1a8fb7188e42 | -9.462 | -60.549 | 2025-08-29 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| f6eb4a37-79d0-393b-9bb3-f9b941bab811 | -12.4345 | -63.9173 | 2025-08-29 04:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b8138f00-2cd2-3081-8bf7-2db1d99b1975 | -3.4254 | -49.0517 | 2025-08-29 04:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c73c29fa-5e8e-33d0-91fe-98622740f08b | -8.1758 | -61.3755 | 2025-08-29 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1e049cd0-35bd-3f5a-bb13-56d2c2f47291 | -9.7322 | -64.9067 | 2025-08-29 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6025638f-421a-3d6e-a14b-0194dbfff460 | -9.1155 | -65.7699 | 2025-08-29 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 29941c95-0548-3ff4-aafe-e14bad18f523 | -6.5358 | -43.9237 | 2025-08-29 04:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6284ad8c-9afb-3509-a5b7-da91f8f50436 | -6.5546 | -43.9221 | 2025-08-29 04:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8e9d20e7-7f5a-3233-854c-35a19af571bd | -9.1154 | -65.7886 | 2025-08-29 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f5a56dd9-243e-3feb-bb91-76c4d2a9c83f | -9.9328 | -59.9247 | 2025-08-29 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fd67bdd8-2e07-3867-9321-2d8654180119 | -9.4432 | -60.5692 | 2025-08-29 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e64aa076-11dc-3389-8466-2d6ac8a7c0b1 | -9.4433 | -60.5499 | 2025-08-29 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 318374e8-20e1-346b-bc6c-fc1abac09858 | -9.4618 | -60.5682 | 2025-08-29 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 32dd7f35-3f17-30a9-adf8-e65d4f88fd2a | -9.0969 | -65.7705 | 2025-08-29 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e6b88bb1-1b32-3597-8539-99e37a5bcf9f | -5.6268 | -45.0025 | 2025-08-29 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d77327c0-0e2f-3cd3-ba84-5134c04d4ea0 | -3.4254 | -49.0517 | 2025-08-29 04:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4fcb4a53-b205-3fb1-83b7-bb40127e83ba | -9.773 | -64.2469 | 2025-08-29 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 96df1ebf-ae90-36a5-a4b5-2470bd9033c2 | -9.4618 | -60.5682 | 2025-08-29 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 6191f5e1-2689-32c7-a81a-024a02452b52 | -9.7728 | -64.2657 | 2025-08-29 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4031a607-c153-303f-a957-3db27529e6e5 | -9.1155 | -65.7699 | 2025-08-29 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 8d6ca82a-934e-32ab-ba5e-1889e002d276 | -9.7322 | -64.9067 | 2025-08-29 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| d5539fb1-7265-3317-9cce-cd1f7633b4b8 | -6.5546 | -43.9221 | 2025-08-29 04:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6aeaccae-7e4d-3432-8165-4774c2fcdf9a | -6.5358 | -43.9237 | 2025-08-29 04:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 03ac4b5b-139f-36e6-924d-3499561d1a81 | -9.4432 | -60.5692 | 2025-08-29 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 65d8d2e7-db28-34e5-a99a-bf119058c101 | -5.6268 | -45.0025 | 2025-08-29 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 50992efd-5ee0-397b-af89-17d1893e3530 | -9.1154 | -65.7886 | 2025-08-29 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1b5bf643-ccf7-3b9e-8773-8e728dd06fe9 | -9.4433 | -60.5499 | 2025-08-29 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b5d8c2a2-6f4a-3e3d-902d-a86e6fdf5d7b | -9.0969 | -65.7705 | 2025-08-29 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9a6c4774-5e6b-30ea-86df-d44331887dd7 | -9.462 | -60.549 | 2025-08-29 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| f876285c-a9d2-3042-96f5-bb5e3ebf301f | -12.4345 | -63.9173 | 2025-08-29 04:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c2d8a057-4286-3d62-9a6e-6b601eb2b0d4 | -8.1758 | -61.3755 | 2025-08-29 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| dca0db01-f03f-3adc-b300-baa7ff25ed96 | -9.4433 | -60.5499 | 2025-08-29 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b16ef269-125c-3fff-9841-f118b6ec7924 | -8.1758 | -61.3755 | 2025-08-29 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1e0e6ea6-f2d0-3e89-8436-2f3d59a3d835 | -9.7322 | -64.9067 | 2025-08-29 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 48da2710-3510-3c63-989a-c2c9374e937d | -12.4345 | -63.9173 | 2025-08-29 04:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9c077025-fd3f-378a-89a5-2b1160e5f170 | -9.9328 | -59.9247 | 2025-08-29 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4a212ea3-2ab2-3d43-aa91-aff06ac06e5d | -9.1155 | -65.7699 | 2025-08-29 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| a70982e7-fbe5-3a10-ae34-0e9e9b4a1601 | -9.4618 | -60.5682 | 2025-08-29 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 7cdffd0d-bbe5-327a-9b1c-cece42aa056a | -9.1154 | -65.7886 | 2025-08-29 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dd02e33a-2e6b-34b5-a6c1-e9d3b38cb2b4 | -9.4432 | -60.5692 | 2025-08-29 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 47840371-e814-3d8d-a2d2-4b229663dccf | -9.1156 | -65.7513 | 2025-08-29 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 073b8ac0-fe5d-31f3-9cb2-913701aca74f | -9.462 | -60.549 | 2025-08-29 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 4bc2038c-8e9d-36a0-a295-ad0a91d66101 | -3.4254 | -49.0517 | 2025-08-29 04:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ab49fe43-0807-30eb-a0ba-163de66739e8 | -6.5546 | -43.9221 | 2025-08-29 04:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8d917694-803b-32c6-8ccc-322f02c08e2c | -8.1758 | -61.3755 | 2025-08-29 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4f8f2e03-9586-3a7b-8b0f-0e249fd9f632 | -9.9328 | -59.9247 | 2025-08-29 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ec5adb7b-90aa-3cf2-a3ae-461c484a4cb0 | -10.9712 | -46.9042 | 2025-08-29 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5e90d458-27e2-3e6b-abc0-5ed6127cd602 | -9.4433 | -60.5499 | 2025-08-29 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| dcc07dab-6c43-3d75-959c-a74fa09baa37 | -3.4255 | -49.0303 | 2025-08-29 04:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| fb6b1ee4-9c3c-3369-83c4-17b646c07b26 | -3.4254 | -49.0517 | 2025-08-29 04:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7cba4c66-28f9-3559-b5e8-460840b56012 | -9.0969 | -65.7705 | 2025-08-29 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1d296ac1-e981-3912-b9a9-2acf5bf60949 | -9.7728 | -64.2657 | 2025-08-29 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 22a9ad56-f8cb-384d-9bb1-b3b7ce89acc9 | -9.7916 | -64.2461 | 2025-08-29 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| da5d27fe-d303-3f22-ba2e-509f7418869f | -9.1155 | -65.7699 | 2025-08-29 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 851192fc-b93d-3d97-b16a-8c08731130d2 | -5.6268 | -45.0025 | 2025-08-29 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 16242659-6593-3e01-82b5-bed739ed78a4 | -9.7322 | -64.9067 | 2025-08-29 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9f088a84-1297-31cd-aaa8-186f16125fae | -9.773 | -64.2469 | 2025-08-29 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.3 |
| c12179a3-052d-3210-a1bc-c8267f910a1f | -9.462 | -60.549 | 2025-08-29 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 21e03021-9938-32b6-8e73-dbd01edc0aeb | -9.4618 | -60.5682 | 2025-08-29 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 36fc4f9c-ddd1-39bf-a1f2-6d3faf0de5e1 | -9.1154 | -65.7886 | 2025-08-29 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 03fb569f-c50a-3791-ba92-fc035bf8a94d | -6.5358 | -43.9237 | 2025-08-29 04:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |


[Clique aqui para ver as próximas entradas](README38.md)
