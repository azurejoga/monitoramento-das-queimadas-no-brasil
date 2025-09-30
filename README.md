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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed56cf66-ebdd-3d00-aed4-894bc49cf591 | -11.7524 | -44.7228 | 2025-09-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| c224582f-0ed1-30ff-a24b-404341783b68 | -4.7271 | -42.9417 | 2025-09-30 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 56da20c6-0c9c-37a5-af53-eb7c117f52f5 | -14.6942 | -48.1557 | 2025-09-30 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f7375ee9-035f-3380-9658-b8600fdf465f | -5.8341 | -42.7681 | 2025-09-30 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 3b94af7b-fb29-3ea9-b535-20366edc8c06 | -13.2341 | -61.1715 | 2025-09-30 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d21d396d-7f36-3ee6-ad38-1781f4beedb2 | -5.214 | -45.2341 | 2025-09-30 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0892e62e-e278-3717-83aa-acb9d65aa31f | -8.672 | -47.7144 | 2025-09-30 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 94db4c5e-e90e-3624-9749-fce079b175cc | -10.2041 | -44.8915 | 2025-09-30 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 15a2f2fd-a6a3-39ce-8a00-f539c2144419 | -13.2339 | -61.191 | 2025-09-30 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1a517da0-93c8-32e5-b35b-2f13c7a93606 | -14.7171 | -45.2291 | 2025-09-30 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1d1cf001-cc83-3891-83ef-f7be02e75c25 | -9.4192 | -54.7172 | 2025-09-30 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6e69bf13-61e8-331d-ba99-450606d91f3d | -1.2928 | -54.1784 | 2025-09-30 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d26da164-083c-3056-b4f5-a15853def95d | -9.4005 | -54.7186 | 2025-09-30 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d532bbe3-6f48-3601-a202-90150466aff3 | -5.2326 | -45.2328 | 2025-09-30 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 46704b98-a0a4-326e-ad24-09df04fe64c0 | -11.7327 | -44.7489 | 2025-09-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b62f5006-ea5d-3149-a135-29fad0779bc2 | -5.2141 | -45.2114 | 2025-09-30 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e73ac1a0-e361-36e5-b5e5-778affab4d06 | -17.4681 | -46.2027 | 2025-09-30 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ba72a10d-fdc8-3e0c-9ed4-757f4f83b118 | -8.1425 | -46.3917 | 2025-09-30 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b0cb43d1-ac2e-3a57-8614-47c5745cf743 | -21.0572 | -45.6638 | 2025-09-30 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0c397dc2-11b4-3f4c-ab41-b067967a10a3 | -7.0481 | -45.1856 | 2025-09-30 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f8eed6fc-54ff-39d8-853a-ad59be156ce3 | -11.2138 | -47.2086 | 2025-09-30 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bb60f01e-8407-3956-b78f-d394af39511f | -5.8153 | -42.7696 | 2025-09-30 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| deb8aa62-77fe-31eb-8679-3a0245e1f869 | -14.5522 | -48.4684 | 2025-09-30 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0cb91a32-b1ca-3aee-976b-13c985cca49a | -11.7712 | -44.7432 | 2025-09-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 5d1eeba8-776f-3043-a0cb-566000fae0bd | -5.8339 | -42.7916 | 2025-09-30 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 0a75a5d6-f433-3e46-a834-2b2a6230ddca | -13.6285 | -42.5324 | 2025-09-30 00:00:00 | GOES-19 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 58.5 |
| b611f314-6806-35f2-b46e-7cae410b916c | -10.2045 | -44.8684 | 2025-09-30 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ddae4dd4-e285-309a-93ba-a964b76a503d | -11.7716 | -44.7199 | 2025-09-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f67d6a8a-0bc9-3058-a4e8-6bd754e624db | -11.2329 | -47.2061 | 2025-09-30 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d9c3552d-7350-31e1-9728-22d36175241c | -3.1013 | -47.0082 | 2025-09-30 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3b59e8cd-018d-3d5d-9311-e1acebdb9317 | -11.1548 | -54.1054 | 2025-09-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| d190592d-f98d-305e-aaac-93065e586db3 | -8.2471 | -45.5263 | 2025-09-30 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5944ab7c-4da1-39dc-864a-693382346248 | -13.2151 | -61.1728 | 2025-09-30 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0c0d74cd-ad51-39f4-8b0d-f8a4610eff5d | -5.5241 | -43.8878 | 2025-09-30 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e8a53589-9b0e-39a1-9eeb-d255e6f0b470 | -18.6041 | -42.7372 | 2025-09-30 00:00:00 | GOES-19 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 81d3872d-1a64-370d-94b6-0ada606d3907 | -10.1855 | -44.8709 | 2025-09-30 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 7a064d0d-d3d2-3ef4-9b90-0d01e0afa65f | -11.7519 | -44.7461 | 2025-09-30 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 23cb17cd-f4bb-323c-8012-7776fe741e46 | -4.4013 | -44.0755 | 2025-09-30 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 78ec7bc9-7d9f-3ef3-8629-50027b377f01 | -19.6027 | -45.8861 | 2025-09-30 00:00:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 3948c11d-866c-35aa-9fde-de67e5e14418 | -11.1546 | -54.126 | 2025-09-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 227.2 |
| b2c71345-e23c-353b-9fce-75817bdbbb2f | -0.1012 | -51.2738 | 2025-09-30 00:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4baa2298-95c5-30c8-a8bd-d67b81937237 | -10.1851 | -44.8939 | 2025-09-30 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 333.6 |
| c422f0dd-fb7b-3468-932a-3877285c790c | -7.0669 | -45.184 | 2025-09-30 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| afca194b-016d-37e0-b262-d818cac6c0f1 | -5.5243 | -43.8647 | 2025-09-30 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3fc9ad95-b1bd-3dde-9bc4-01468375aaac | -11.1735 | -54.1242 | 2025-09-30 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5812d5ca-be98-36e8-93bd-6f151e577246 | -5.8151 | -42.7931 | 2025-09-30 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 2d5fe515-30b1-3efb-a235-4d704e5dd366 | -21.0564 | -45.6881 | 2025-09-30 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8f642ff7-d99b-3c70-8d92-d7a3230d52f2 | -14.7137 | -48.1525 | 2025-09-30 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1e5af1bd-c78b-3ab6-a7ec-d0fdd2f97e3e | -13.2149 | -61.1923 | 2025-09-30 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8bec6db1-4f3d-318d-b9d0-161a69da8dfc | -17.4687 | -46.1792 | 2025-09-30 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fe6d24d7-08b7-3de0-89f9-dc937eab83c3 | -19.6027 | -45.8861 | 2025-09-30 00:10:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1deb61e3-c82c-31ac-b918-1c0fad062acf | -4.354 | -45.5773 | 2025-09-30 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1e665e12-7e68-3bda-9bc7-ea1dfdb4e8f4 | -5.5241 | -43.8878 | 2025-09-30 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 649a03c0-6611-3795-96bd-c7babadf66be | -10.6317 | -53.7011 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| fc2d5e01-e205-3562-a56f-3c777f8ddcc0 | -1.2928 | -54.1784 | 2025-09-30 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 32a8b0d6-088a-3cb4-9f25-157878c52d2c | -18.6041 | -42.7372 | 2025-09-30 00:10:00 | GOES-19 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| 9b199700-71d0-3c65-9be9-a8f1558358d7 | -10.1851 | -44.8939 | 2025-09-30 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 298.6 |
| 74ae2db6-3ba6-33be-857b-3f51d3a51f0c | -11.1546 | -54.126 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 199.7 |
| c2063744-ebda-3c5c-a6fd-bc079be7d2f2 | -7.0481 | -45.1856 | 2025-09-30 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0b0abf8e-a2fb-3305-bc86-a31716177474 | -5.214 | -45.2341 | 2025-09-30 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2415aed4-b129-3503-93b3-b7f950938762 | -8.2471 | -45.5263 | 2025-09-30 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| af239946-7aaa-3a10-842c-dd0a120a2deb | -5.8339 | -42.7916 | 2025-09-30 00:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 67a321e4-7c34-3c94-94be-d3063fe18e02 | -14.5137 | -48.4522 | 2025-09-30 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d1ddea0d-81ab-3b2a-83e1-17b20809da99 | -11.1357 | -54.1277 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 96bf4ebd-039b-3a82-9979-31a284c8f2ee | -17.6343 | -40.2135 | 2025-09-30 00:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.1 |
| 52584ad5-d597-323c-9b88-b5611225ccac | -5.8151 | -42.7931 | 2025-09-30 00:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 652dbabe-4bc4-3605-940c-8dff2c7c0aa2 | -4.7271 | -42.9417 | 2025-09-30 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| beadcfe2-5eca-332d-88b7-8d9f57f4b793 | -11.7712 | -44.7432 | 2025-09-30 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ac6cebb6-993e-3bf8-aa6a-38a24d403f4a | -11.1735 | -54.1242 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 02a643bd-269a-3e39-8228-b64a98a388c5 | -10.1855 | -44.8709 | 2025-09-30 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 1c4b16e6-e694-3148-8c71-d56138b67e84 | -13.0144 | -44.1006 | 2025-09-30 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dbe43a9b-b8c3-3fd7-a491-0e25ce0a282d | -8.672 | -47.7144 | 2025-09-30 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 74d0a368-46ea-3978-8c7f-7389a1988f1f | -11.7524 | -44.7228 | 2025-09-30 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| a7b83175-dc7e-36cf-b816-8280e64de625 | -11.1737 | -54.1037 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fe3b0844-db8c-32a3-a3f0-3d1e55a79c8f | -11.2138 | -47.2086 | 2025-09-30 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| fdeb9f1c-907d-3816-beb2-0065c54da208 | -9.4192 | -54.7172 | 2025-09-30 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f630a631-8ad4-343f-95a7-0eb2de738d84 | -11.2135 | -47.2309 | 2025-09-30 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a44c8f29-16ba-3735-8d2f-4afc40b5b732 | -11.1548 | -54.1054 | 2025-09-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 4adc6d75-75e7-3d1f-9d4e-5a315023922a | -13.222 | -47.3097 | 2025-09-30 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e77fa67b-0085-3e2e-830a-876ce76aded3 | -10.2045 | -44.8684 | 2025-09-30 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 72eddd44-561d-3b9b-82d8-dff737572cb4 | -13.0139 | -44.1243 | 2025-09-30 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 732b083e-8df6-3e63-bacb-a474d374e20a | -5.5243 | -43.8647 | 2025-09-30 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1a03d8a4-6106-3952-adbd-0e48f768082c | -10.2041 | -44.8915 | 2025-09-30 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 42c74140-c25e-3b49-9e3e-6cb25b20c03a | -14.7137 | -48.1525 | 2025-09-30 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 64a8c7e1-bfcf-3a71-b581-2a514147f821 | -13.2339 | -61.191 | 2025-09-30 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a355a7cc-8814-3d5a-811d-5f0d485b66fd | -8.2659 | -45.5244 | 2025-09-30 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| ad303468-d9ef-341c-9640-869995d188e3 | -11.7519 | -44.7461 | 2025-09-30 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| f1b43709-1235-390d-9d47-911ced6726db | -3.1013 | -47.0082 | 2025-09-30 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 774e617b-15e2-33e7-9b2e-6bc740420e4f | -8.2474 | -45.5037 | 2025-09-30 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 60bfa8b0-98a2-3f15-b8ac-65287529b134 | -14.5522 | -48.4684 | 2025-09-30 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| df5dd9fe-918d-369f-bdd3-84ed9d2c4a82 | -10.1851 | -44.8939 | 2025-09-30 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 301.8 |
| 8992bbd8-d6d2-3a62-a362-293141e8e1a5 | -11.8868 | -48.0323 | 2025-09-30 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 1a09e5bf-3672-3e99-bbf7-2278888bd3ff | -4.3538 | -45.5997 | 2025-09-30 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a464a495-18c8-317f-9a30-927e19be6af2 | -11.2138 | -47.2086 | 2025-09-30 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 85e9674a-cb28-334f-bbf0-7aeed149dd5c | -4.4013 | -44.0755 | 2025-09-30 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a2d951fc-b56d-38b7-932c-71eef4c6b973 | -5.214 | -45.2341 | 2025-09-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 28c5ba94-b839-3afc-9971-8ed2face9d1c | -4.3826 | -44.0766 | 2025-09-30 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| b47af874-9c7e-3298-bf0d-3b02a6eaa6d2 | -11.2135 | -47.2309 | 2025-09-30 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 95843613-b2e8-3742-8742-ba4bb183ed44 | -7.0481 | -45.1856 | 2025-09-30 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 76816d70-62c6-3c73-97f5-6dc10329744e | -10.2041 | -44.8915 | 2025-09-30 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 248.1 |


[Clique aqui para ver as próximas entradas](README2.md)
