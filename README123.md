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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96d35d96-a47b-38af-9b79-a33fee81e9bd | -18.1782 | -53.3024 | 2025-09-30 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 3f26cbae-5f32-3def-ad2a-2fbcafb5855c | -12.3867 | -50.1731 | 2025-09-30 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 591.8 |
| 2a0b3d1e-3fee-3320-9566-aa9d3695a029 | -7.6275 | -45.428 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8719df2e-572f-3e96-a15b-82673d3c5ea3 | -13.3808 | -48.0908 | 2025-09-30 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 2f7a6cd4-7162-370a-9c50-53bf80d13ac5 | -13.2226 | -43.3768 | 2025-09-30 14:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 198.2 |
| 09e67ae5-f0eb-3e0c-b8c4-7531d523a342 | -15.9268 | -46.2334 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 351.1 |
| 7a1929dc-0c50-3b57-a24e-ebe9d8f5c878 | -12.4055 | -50.1924 | 2025-09-30 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 269.1 |
| d79a3b47-4d5f-3521-9aeb-4126a566c8f1 | -10.841 | -47.9644 | 2025-09-30 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 72fb03d8-c46a-30ea-9439-1d228bc60967 | -9.0682 | -47.6313 | 2025-09-30 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 41388339-d1f1-3b9f-b9f8-410bec5c1e0f | -15.1688 | -52.8241 | 2025-09-30 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 601f4341-471e-3e47-bfce-9ed52fd98b16 | -9.1434 | -47.6457 | 2025-09-30 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4480689b-233f-34b8-92c1-ad9a6397d9b2 | -5.8612 | -43.8858 | 2025-09-30 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 662c94be-0139-3298-8a0f-4a3268678ca2 | -15.484 | -45.8773 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 06a66340-50d5-38b7-8877-825c9513b184 | -6.2572 | -43.6458 | 2025-09-30 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1c378725-cf30-327d-a9c2-207c4d44ebef | -7.9194 | -44.6016 | 2025-09-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6f34c4f7-44b3-3cf3-a357-c59e6d0bd888 | -5.2869 | -43.1613 | 2025-09-30 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 97788b50-ff4c-37dc-975c-8d38624317da | -7.115 | -47.785 | 2025-09-30 14:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f791f469-17a7-3082-bc86-43bc488e8abe | -5.826 | -45.7334 | 2025-09-30 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c5298d46-f627-31d7-8665-1f7e63e360b1 | -11.2138 | -47.2086 | 2025-09-30 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3913dceb-193a-3cce-9939-1fec36a53bdc | -5.7225 | -42.659 | 2025-09-30 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 5f22890b-0a0a-3668-839b-07561ab34bde | -5.7681 | -43.8235 | 2025-09-30 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c9548068-9969-354a-bcad-03fd5d933795 | -7.8509 | -47.2623 | 2025-09-30 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2b82cddc-55be-3a36-8c4d-f760fa1dd1ba | -15.2809 | -48.0138 | 2025-09-30 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| d03a5784-a96f-393f-84e1-1b0d6ba30656 | -9.1248 | -47.6256 | 2025-09-30 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 339568b3-79dc-35d3-8d58-0dbcd816cab3 | -5.9192 | -43.6961 | 2025-09-30 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 57eec53b-5dab-316f-8e2d-b6ae63259834 | -5.9004 | -43.6976 | 2025-09-30 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 3280a0c5-d1f2-37a4-a010-02534872d01c | -15.011 | -46.9515 | 2025-09-30 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 02a84224-8320-33ca-9aa0-5c09228d52c2 | -3.8269 | -40.4598 | 2025-09-30 14:30:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 169.9 |
| 3509cb9a-f931-314b-ad99-d91af022729d | -12.7018 | -45.2947 | 2025-09-30 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 9ba1bae0-531e-37dd-840a-bd76eced88a5 | -11.1948 | -47.211 | 2025-09-30 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4d07ae60-4bf5-33b4-9af1-51ad6e0008da | -10.1234 | -47.783 | 2025-09-30 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a07bff88-458b-3d35-a0ad-e9a17047f144 | -6.5163 | -54.8784 | 2025-09-30 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 248f15e1-be2b-395b-b1fa-7e6bda9a30ad | -15.149 | -52.8479 | 2025-09-30 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 6a542146-a63c-3fd8-81b3-9ec2fdae9cfc | -12.4246 | -50.19 | 2025-09-30 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 868b0085-55de-3fa6-bb58-47296e3f6b77 | -6.2759 | -43.6442 | 2025-09-30 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4e8c498f-c204-354c-abca-94d3d055510c | -12.9524 | -48.3963 | 2025-09-30 14:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| a270c398-e6ea-3ef7-860e-131ba2d355dc | -9.4206 | -54.5753 | 2025-09-30 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| c7231af2-836b-3195-b053-91174bca9ee3 | -8.672 | -47.7144 | 2025-09-30 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 76c2efb8-e00e-37d8-a123-22d5754409aa | -13.8264 | -47.9794 | 2025-09-30 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 8191a1e7-ff9a-3cdb-9e87-a6437c2358e7 | -14.7171 | -45.2291 | 2025-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 8c70580a-a196-30ad-99cd-e6c56f877187 | -13.4182 | -48.152 | 2025-09-30 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| cf01f0cf-d797-3654-ab5e-a0ac7cf6aa1f | -6.5227 | -45.2297 | 2025-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0118c046-9061-3031-ae98-cbb84ab756f8 | -14.5141 | -48.4299 | 2025-09-30 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a407a020-72ba-3eb2-9212-2b175a9210c9 | -12.3862 | -44.6953 | 2025-09-30 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| e10f359f-e2cc-3608-a13e-a4a999cf1eb5 | -5.4752 | -43.054 | 2025-09-30 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 258.1 |
| 036aafb5-50a6-33a6-9300-222238f2419a | -11.071 | -47.8262 | 2025-09-30 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e3248a5a-f09f-3e2f-98fc-fe8d769d8d1b | -10.0717 | -50.2173 | 2025-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f99b3d01-f2fc-3a49-bafa-d5897d5c8731 | -14.5853 | -45.0197 | 2025-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 79e87159-aec7-343e-a963-9580340b16ce | -9.0425 | -46.7032 | 2025-09-30 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 432fce23-eb05-3e92-882c-3b8f56e52749 | -13.1624 | -47.4084 | 2025-09-30 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| fb2c2005-23fe-3d15-aff4-721585ecc64c | -3.8885 | -42.5211 | 2025-09-30 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 184.6 |
| 70d379e2-88ac-3cc4-a9c5-9be9f2a71768 | -9.4557 | -45.4862 | 2025-09-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2a842e43-50a6-30fc-a4a1-5ce609768175 | -3.1763 | -42.978 | 2025-09-30 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9367f085-9c90-333a-b042-6b5dd120e3b4 | -9.8845 | -45.9576 | 2025-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 330.8 |
| 50fc8c4e-1175-34f3-9f5d-bbd3879a78ea | -12.4058 | -50.1708 | 2025-09-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 2dbdb331-da03-34ba-acf2-869c62866409 | -7.115 | -47.785 | 2025-09-30 14:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 638113fa-3337-35ac-9ffe-3490e0d2c05a | -12.2153 | -47.8112 | 2025-09-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2ca55159-693a-3d22-a65f-02fc46480e28 | -7.0478 | -45.2083 | 2025-09-30 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f5d6f763-2239-3e82-a096-8a745bb68663 | -15.1688 | -52.8241 | 2025-09-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 6016b75a-ef42-3be5-afc9-e00dbf9ab69d | -11.2138 | -47.2086 | 2025-09-30 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 26ba0b01-a6fe-360f-b238-1118356cd980 | -7.835 | -46.9986 | 2025-09-30 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| b31bb2f4-c80b-3f0f-956d-9f9737594833 | -11.8868 | -48.0323 | 2025-09-30 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 1f024a1d-847a-3ad9-9544-f226e161016a | -15.9268 | -46.2334 | 2025-09-30 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 201.7 |
| d7615c7e-ea9f-301e-8fe2-5b05fb57bb80 | -7.5146 | -45.4385 | 2025-09-30 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 44eca30d-4dbb-3bef-a4a7-c939fcd1e447 | -15.2809 | -48.0138 | 2025-09-30 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1d761c31-30fa-399c-8e29-e199726662a3 | -10.0528 | -50.2192 | 2025-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 61f74181-2a1b-3a78-abc9-5326c7272f43 | -5.843 | -45.934 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 92f4662f-c21c-3f3a-a94f-5344e0a67a3d | -9.0494 | -47.6332 | 2025-09-30 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| cc669a90-e8d0-3bd6-8655-44debbf304c0 | -3.8885 | -42.5211 | 2025-09-30 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| 47e77185-943f-3885-9ad9-207e849b264b | -15.011 | -46.9515 | 2025-09-30 14:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f60bb4b0-77ad-35de-8ea5-51aa25c60999 | -4.0146 | -43.2641 | 2025-09-30 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5dda5457-bf7a-3c95-93c9-8bf3eaf9f481 | -14.7171 | -45.2291 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| ef62b95f-5e20-3d7e-a125-90b66f5e6237 | -8.8737 | -46.6315 | 2025-09-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 27a60657-6d17-375f-84b4-3c38a98539bf | -17.4049 | -47.1431 | 2025-09-30 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d00f73e0-2c64-3700-ab20-ddc81619e620 | -5.4565 | -43.0554 | 2025-09-30 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 2ae5a9e9-c92e-3d20-ac49-8eb35a137295 | -17.9016 | -57.577 | 2025-09-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| d5d23815-7e8e-3c28-b909-a4d974706deb | -7.8538 | -46.9969 | 2025-09-30 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 38cd8285-c5bb-3a18-8148-d0aae3e8e8e6 | -10.7673 | -45.3687 | 2025-09-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cd16b8f5-ce1f-3c57-bb4b-1b6c91511566 | -14.7361 | -45.2489 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 308.3 |
| f575aeeb-3301-3f06-8a93-ae8f6642bce0 | -11.1548 | -54.1054 | 2025-09-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| fe43b822-70d1-3744-b114-a3945f2a5042 | -10.8242 | -45.3841 | 2025-09-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| f8d4dee1-c1f2-3477-aaa9-538c70b4c7dc | -14.6049 | -45.0161 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 92f835ca-6785-3e67-b0d3-814f703ab407 | -7.819 | -46.7561 | 2025-09-30 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| cfab9a59-28c4-3435-8a23-9009eeb46800 | -6.5227 | -45.2297 | 2025-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| f0a1d84d-f7d1-3b63-b239-8a580d8cda18 | -8.5407 | -44.6745 | 2025-09-30 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 8a464694-faf3-3273-835b-8b9fef54cada | -7.938 | -44.6226 | 2025-09-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1413ecb5-59fd-320f-a595-a602d49caa96 | -8.8357 | -46.6578 | 2025-09-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0c274265-eeb6-3a51-8c9f-b6b2c5390174 | -12.8425 | -47.0289 | 2025-09-30 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4911f75c-77de-3425-ac1c-208399e9e8a9 | -5.8445 | -45.7545 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| be28817e-f9ab-351f-b7b0-bdec34f998cb | -5.7599 | -42.6797 | 2025-09-30 14:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| da5ab5a0-60cb-32d4-b0ec-eaebef559113 | -8.8226 | -46.2115 | 2025-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 91427196-9d3f-3eac-8a9e-241142247eba | -5.2869 | -43.1613 | 2025-09-30 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b177fbb3-8568-3869-a62c-6da8e92f36fc | -6.5163 | -54.8784 | 2025-09-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 43545a29-b338-3998-861c-6fc575c7da6c | -8.8229 | -46.189 | 2025-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 399.3 |
| 6409d9c6-857e-3b4b-bb23-1445fe56259b | -5.9004 | -43.6976 | 2025-09-30 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 1a70b0d9-68c6-39c1-b945-d11bdfb0dbac | -11.7537 | -46.8461 | 2025-09-30 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 553698b5-3302-31ef-a915-3e961f339f94 | -7.8696 | -47.2606 | 2025-09-30 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 7aa22059-5565-310e-8e93-920128360e63 | -15.9273 | -46.2101 | 2025-09-30 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 1645355a-d96f-3cf4-b051-1d6220803fe6 | -8.2662 | -45.5018 | 2025-09-30 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 2954f68d-60ba-362e-a1ac-065b5cca8ea8 | -5.6803 | -45.2931 | 2025-09-30 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |


[Clique aqui para ver as próximas entradas](README124.md)
