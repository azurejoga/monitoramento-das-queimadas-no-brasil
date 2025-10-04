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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7d33c57-270c-39e1-9977-e089dc401bd2 | -9.6293 | -54.3158 | 2025-10-04 14:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2db71396-0f46-3e88-b61b-145a966e5107 | -7.7489 | -46.3168 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 1db77210-ee8a-34b7-a984-ff2d955a4183 | -14.5941 | -52.4976 | 2025-10-04 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 26e04d8e-c97e-304d-865c-bf735ac1a568 | -5.8741 | -42.5052 | 2025-10-04 14:10:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 5cd1b3ae-e7c9-3f03-8c69-33c75d8488ba | -10.2017 | -50.3749 | 2025-10-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| de316fac-dfa7-3cd0-becc-0f6d7268bde3 | -10.297 | -50.3013 | 2025-10-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ef05931f-8e33-3054-9949-f66c7ef98461 | -13.4925 | -47.2685 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b306068d-0a56-32d0-b85f-2f62e7ed9bf7 | -6.287 | -44.428 | 2025-10-04 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b6eb126e-1f89-3570-a038-995b029927f6 | -11.8442 | -44.9408 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 319.3 |
| 26923a48-10e6-3d90-b550-87701f0925e9 | -14.5945 | -52.4763 | 2025-10-04 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| fad2fadc-c6e3-35a4-a3e7-149376625677 | -7.8593 | -48.2037 | 2025-10-04 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 54ce0096-44cc-3da0-a90a-f435c5b7d0b1 | -13.2938 | -47.5905 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f37b1344-36d8-3ba5-83ae-1c5411c41341 | -9.1901 | -49.9604 | 2025-10-04 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d5978a67-76b9-3162-ae73-a4b423eb1422 | -8.1891 | -44.1357 | 2025-10-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| b7146cdf-803c-3084-be36-3a044529208e | -12.3162 | -45.3545 | 2025-10-04 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6280be06-2c57-3145-8742-63db302ff8bd | -8.2314 | -46.8289 | 2025-10-04 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| aff8b870-b8e7-3e37-8b71-1d300c67c43d | -9.5914 | -45.2652 | 2025-10-04 14:10:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 850cc59f-fe41-314b-8d44-cdf889e16ca8 | -8.6322 | -54.9949 | 2025-10-04 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 7b553bca-aee6-3381-95d3-3a5376b5fbe2 | -11.8818 | -44.9815 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| aae7cdb8-c78b-37c2-9ef6-1845fb17bb4c | -8.1702 | -44.1377 | 2025-10-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 85432ea0-3097-3ddf-bd87-4f3a38ce0c35 | -15.5408 | -46.8344 | 2025-10-04 14:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 83730dd0-4194-3c87-b2b4-4d467911a89e | -7.793 | -44.1535 | 2025-10-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7b149201-12f0-33b0-99db-41a58fdc3aa7 | -13.4732 | -47.2714 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 426c218e-f30f-34fb-b00d-fd08e51e1be0 | -5.6843 | -42.7328 | 2025-10-04 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| ab1c2ed2-dcd2-3087-b1e0-f5b1de59eb9b | -8.7589 | -49.9139 | 2025-10-04 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| bec2ab53-4c38-3b7d-aa4d-2cae5e20b190 | -12.4167 | -44.1057 | 2025-10-04 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a4d28d92-6c41-3539-8bf0-88cc9adfce5f | -9.3196 | -45.7515 | 2025-10-04 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 60d4698b-8db5-359b-a32d-ff56ce41fff0 | -12.8761 | -47.2937 | 2025-10-04 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 229.2 |
| b87e20f9-806e-3093-9f68-bc3e7367b400 | -11.4678 | -43.5011 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 8db6e1b1-dac6-3183-a829-529a04dcec3b | -12.0891 | -45.1814 | 2025-10-04 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 35d450c1-0181-3f08-801d-27afe6f6b0a3 | -16.097 | -51.0611 | 2025-10-04 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 29afec99-6b36-3fbf-a9c8-b934c49976cb | -14.3899 | -45.9601 | 2025-10-04 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 4c5cad52-44dd-32a8-b723-b41a7e4b6d25 | -9.3193 | -45.7741 | 2025-10-04 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 69515a7a-0d04-34d9-aca6-3ba47a3b1ca1 | -13.3225 | -48.1216 | 2025-10-04 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| ea4b3992-f1a4-33bd-8651-4ebdfaddf553 | -11.8635 | -44.938 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 253.7 |
| ceda100c-b3d0-3a81-95dd-118e96f0441b | -12.436 | -44.1026 | 2025-10-04 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 616997b2-11ca-3320-852b-c012ad3b46cb | -7.6458 | -45.4716 | 2025-10-04 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 03bfc677-9a34-3066-aea3-6b08ceb72d92 | -11.5492 | -47.6773 | 2025-10-04 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 86dcecf0-9bae-3995-a737-056b12f6c5b8 | -8.9948 | -47.4845 | 2025-10-04 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8cc4ac66-3ebb-3fbf-b6cc-4995344103f5 | -12.3853 | -50.2595 | 2025-10-04 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 233.8 |
| b73d0612-281f-376f-8f51-9db7928a222b | -13.0968 | -47.8429 | 2025-10-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| cb2c6e2e-f41e-3b18-88d7-8c2a320d364e | -11.449 | -43.4803 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| fe5dbdf5-a1d7-396b-af4c-2403804dfb4a | -7.878 | -48.2021 | 2025-10-04 14:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 2977aa5e-0159-3590-bfba-c88c1dfd6f87 | -14.672 | -48.2933 | 2025-10-04 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| bdfdd808-6663-318f-9b26-b823eaad7bb2 | -15.5402 | -46.8574 | 2025-10-04 14:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 78f3c601-1bf6-3f3f-9f4e-493523534d52 | -14.3904 | -45.9369 | 2025-10-04 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 5efd9007-c311-3499-8cc9-d23b3b2cf08a | -5.6655 | -42.7342 | 2025-10-04 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| fc2798cd-4030-3e80-bb2e-a6fb41f7aa4c | -16.3627 | -51.4752 | 2025-10-04 14:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 7922fa87-a192-3c65-b45d-cba246ebf6b7 | -15.7297 | -46.2707 | 2025-10-04 14:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| aa3eaa25-5bb3-325e-8471-c0ff6efb43b7 | -7.0558 | -42.7782 | 2025-10-04 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| a4b6a4cb-a281-3a80-86f6-54f3ffcb995b | -13.7476 | -48.0583 | 2025-10-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e2485aaf-41a2-31bd-a9cf-3febd62ba863 | -12.4171 | -44.0821 | 2025-10-04 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 333.6 |
| 9d65b5c5-9886-3b5d-8d64-dd42a9082cc7 | -7.7491 | -46.2944 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 141a764f-363e-3e92-a51a-686e174883e4 | -9.1713 | -49.9622 | 2025-10-04 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 8dd2dc74-a2b2-3f75-8866-02dffda0e089 | -11.4298 | -43.4833 | 2025-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 567e9ffb-93e9-3f1d-9cb8-8dcfeb050e7b | -11.3268 | -53.9459 | 2025-10-04 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e1cbc0bf-fe3f-3834-a6f9-124a9f88a44d | -13.7279 | -48.0836 | 2025-10-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3c2b4fa0-30c9-32e1-ae05-817df0727367 | -7.5317 | -37.9919 | 2025-10-04 14:10:00 | GOES-19 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 4038397a-7545-3e3f-8bad-fbaff13a7516 | -7.4416 | -46.9666 | 2025-10-04 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d0d65e2b-ceec-3b09-936c-79da21290a8e | -8.8529 | -46.7897 | 2025-10-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 35788adf-0035-3377-b28c-b6952d0b4541 | -6.0618 | -42.5133 | 2025-10-04 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 756a2125-e7bf-3cf2-a423-27e15fb4fed3 | -6.3673 | -43.8916 | 2025-10-04 14:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c020fb13-b287-3d98-8798-eb1292f4a2be | -14.9347 | -46.8736 | 2025-10-04 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fd426ced-2e6c-3f09-9001-97d01999e02b | -9.6641 | -48.2064 | 2025-10-04 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| befa8e1f-e145-3478-a9b1-bde700258ff5 | -12.4171 | -44.0821 | 2025-10-04 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f1170cb1-c0e3-35cd-b9b8-62564dbbd6c8 | -11.5256 | -46.7871 | 2025-10-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| edffdc4c-2138-3c2d-aaf7-313d00118798 | -14.3171 | -52.9131 | 2025-10-04 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| fc4f95b2-ffc1-33a5-a359-cacbb81e0a7e | -11.505 | -43.5663 | 2025-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 6f656ee3-c764-3984-bf14-bc9abf775c51 | -14.9881 | -49.9892 | 2025-10-04 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 81431e35-7e45-3a86-ba2f-a6175ef3d487 | -6.1994 | -45.7736 | 2025-10-04 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2150f5d9-64e8-3a5b-ac42-0fe5ad0facef | -7.0369 | -42.78 | 2025-10-04 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 282.8 |
| 06b9e4a2-be75-331c-b6cc-d99e96cd23a7 | -11.8818 | -44.9815 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 8533c08a-d5b5-33f2-bd87-006f1f372835 | -15.5408 | -46.8344 | 2025-10-04 14:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 46edb624-c409-3d61-bdd2-72e8df91300f | -9.9624 | -45.8124 | 2025-10-04 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a1be98ce-1bbb-3b5a-8d49-e623104b7ed3 | -13.3225 | -48.1216 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| c684f070-5c0b-3150-a93e-5ebce529ea13 | -16.097 | -51.0611 | 2025-10-04 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 4ba834a4-e92e-3e75-89c2-94cdb0bbc49f | -6.2596 | -45.341 | 2025-10-04 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 72fd339b-5c42-37eb-ad2b-611fd6e321f1 | -8.8534 | -46.7451 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| fcaad999-8af1-3939-b76b-baec8669f540 | -14.5941 | -52.4976 | 2025-10-04 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 4eedfa06-ba14-3589-a0a9-5eff63e65317 | -5.3228 | -43.3454 | 2025-10-04 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| dce24ed5-54f3-35fa-bb3e-629c8c3ea226 | -12.0891 | -45.1814 | 2025-10-04 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 0799d348-0312-3c54-b8c6-3acbe6dd2ea4 | -6.0616 | -42.537 | 2025-10-04 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 211.4 |
| f895b971-bafa-3e53-832d-2e3a7fdb271c | -8.7777 | -49.9123 | 2025-10-04 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| d62c3a60-adc8-3121-894b-95476deed2cc | -5.9584 | -43.5072 | 2025-10-04 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 61d6ee8b-06ac-3c20-bebd-083086f76325 | -15.3185 | -46.278 | 2025-10-04 14:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 26eaecbf-4a60-3a53-bcb9-67aa35df96eb | -12.5733 | -48.1393 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 5b5d4c64-7f83-3366-913c-89a2aaee63d8 | -13.7476 | -48.0583 | 2025-10-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9eb0d42a-8588-341d-bea9-b8d5f1639be1 | -12.6512 | -46.9894 | 2025-10-04 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4939c1b7-a5e8-317c-aaec-6f28b001f9f3 | -8.8531 | -46.7674 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 86bf138c-a2e5-3541-baa6-d720d064161d | 1.7667 | -55.8228 | 2025-10-04 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 5cb457d1-e9ae-3cd0-a597-5a57a8f543eb | -7.0558 | -42.7782 | 2025-10-04 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 190.9 |
| a91db0c0-c441-3e93-b9ce-01b762e3b2dd | -15.1357 | -45.7104 | 2025-10-04 14:20:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| e02dbe90-8514-393d-9d66-6fd2ceb389fe | -10.127 | -50.3184 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ba2e3acb-5e60-33b9-af6c-236672ed5231 | -11.8814 | -45.0047 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c8b3919d-17a5-3e19-b260-c7e35ebe04a6 | -15.9838 | -50.8614 | 2025-10-04 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| b2bb0ab5-e8ae-3efa-8d1b-950d035674cf | -6.2325 | -44.2487 | 2025-10-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a3cae7da-3080-3ff2-a64c-ac8dd813ad00 | -7.4416 | -46.9666 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 36ad202c-3f0d-33d4-bb06-5d6f00521271 | -9.648 | -54.3143 | 2025-10-04 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1f449bf4-fa4d-378a-b387-5d341a613122 | -9.3196 | -45.7515 | 2025-10-04 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| e11a6c6d-bf5f-3b38-9e50-208154fbe0c0 | -14.8461 | -54.7903 | 2025-10-04 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |


[Clique aqui para ver as próximas entradas](README155.md)
