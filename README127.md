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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31798c4d-c4c7-3207-9143-7d53880311c9 | -10.4655 | -50.412 | 2025-10-07 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b6d8fed4-f5b9-33cd-b0b6-aa0528a9a0a9 | -8.8717 | -46.7878 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3af62a22-a322-3041-82cb-035588ca27d9 | -10.9106 | -47.1353 | 2025-10-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| cd342098-8104-3500-9dbe-211e9a4bc228 | -19.5789 | -44.6198 | 2025-10-07 14:10:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 50cc84bf-e743-396e-92ee-73191d8f8da6 | -8.6519 | -46.2964 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2ef34079-9a94-339c-921a-3e91c6538528 | -12.9101 | -54.7558 | 2025-10-07 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d11a071a-0243-3be4-99a5-9b4c01679faa | -15.6202 | -52.5501 | 2025-10-07 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6e51bd5d-7165-3e63-bb1b-9715ebfdbd7f | -11.9963 | -47.1944 | 2025-10-07 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 56121987-0e80-3e3e-a0c5-baea9ff30764 | -7.4666 | -43.0909 | 2025-10-07 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| c821ef43-026d-3698-b720-ff8437fc24b3 | -12.9106 | -54.7147 | 2025-10-07 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 52b52202-6141-37e6-9765-6b4c99f88ef9 | -8.1327 | -44.1185 | 2025-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 74a796c0-0dbb-342b-88df-82cc2bea0ef2 | -14.8884 | -47.2226 | 2025-10-07 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 8dd086e9-9ec9-30c4-915d-058836a24e08 | -7.6932 | -46.2548 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3d3cfbab-dc32-3f74-95dd-e2c5abcd0cf8 | -8.6521 | -46.274 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ad7807df-442e-329c-b5f4-2a3bc680547c | -10.2212 | -50.3303 | 2025-10-07 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4b13df03-573e-326d-b18b-0efbc377d4c8 | -16.0016 | -50.9456 | 2025-10-07 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e2e3ee4d-d3f9-3e4e-bbb0-df3398266e5b | -10.3532 | -50.3382 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 08bd0393-246c-3b1f-afac-314f40e0d303 | -9.921 | -50.2109 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| aa331a4d-d0cb-3979-a6fc-390feebd95e8 | -8.613 | -44.9189 | 2025-10-07 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0e72779f-b69e-3ee9-850e-35289f3ad049 | -3.9134 | -41.5687 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| ff201e46-aaf9-36a7-bcf1-15bedfd5ade3 | -3.8943 | -41.6177 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| edfa4137-b16d-3921-87f1-bfc0237d8be6 | -10.3721 | -50.3363 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 7b7f3e16-083b-3f0b-ac37-8b48021c9239 | -10.8921 | -51.0269 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a74316e9-d3da-350a-ba26-9ec4c7398ab4 | -8.4821 | -46.3136 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6a2d68a2-8c4c-326a-8290-41fbfdf828c0 | -10.0865 | -50.5354 | 2025-10-07 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fb35d2a7-99ba-3c32-9a5e-dc6084ce5f72 | -12.7637 | -50.4921 | 2025-10-07 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 29522e62-2500-383e-9834-f62bf59b4bba | -13.8863 | -42.3126 | 2025-10-07 14:20:00 | GOES-19 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 4092416d-673e-31f7-afe8-3c33fde20296 | -3.4366 | -43.1532 | 2025-10-07 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7e803e84-4128-31ee-ac42-0850b0510c3c | -3.8948 | -41.5458 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| cf5cfcf5-549a-3143-b957-9c03fa928234 | -11.8038 | -45.0624 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ad5f3896-6be7-3259-b929-b2251b934cc7 | -12.2022 | -44.2573 | 2025-10-07 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 06443cb1-416d-3010-9d77-0d837ea96c69 | -8.5395 | -46.2406 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d4e4f79a-3e88-3eb3-9504-1dad35da5c85 | -15.6202 | -52.5501 | 2025-10-07 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b1545869-977b-3b84-8681-e721bb7269ee | -11.0262 | -50.9067 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 18e6db61-3391-3937-9844-5f2183f6142c | -9.6807 | -45.6417 | 2025-10-07 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| fc92c147-9eb0-3e56-bc7f-acbb74c55b6c | -11.0451 | -50.9047 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| c66dbb44-d15a-3244-8b42-b47e70fc5e21 | -8.1699 | -44.1608 | 2025-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| d5dbbdc7-cd3d-3894-9e3c-171bedc8232e | -10.3343 | -50.3402 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2b0092b1-fee3-31d4-8bec-7902c848c90d | -4.0382 | -42.5129 | 2025-10-07 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| ddb7ba47-7ef0-3686-bae5-06964268584a | -10.3057 | -46.9635 | 2025-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| eb093e61-74bc-350a-8c8c-275f3ffdb2f1 | -12.9101 | -54.7558 | 2025-10-07 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 0de3b546-63fd-31f2-9a3e-823edcf8261d | -16.0012 | -50.9674 | 2025-10-07 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 431e87e3-377d-3299-977f-b411bff29b9b | -11.0265 | -50.8854 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 181edb0b-0ec4-3096-befb-06c0aaf38d28 | -15.6007 | -52.5529 | 2025-10-07 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 8b32cad5-7ccf-3177-bf08-4988086f1fae | -12.6159 | -44.7519 | 2025-10-07 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 3a6f5b01-b550-32b0-b9b9-a66845059a9a | -8.2077 | -44.1568 | 2025-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 4cd7ad4c-0a36-308f-b53a-ca25ac3b7402 | -12.4919 | -54.7158 | 2025-10-07 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 03521b3c-c55d-3c1e-b906-a20c14060672 | -11.7409 | -45.371 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 65107858-a67e-3b63-9dbe-6d71e814450b | -15.6003 | -52.5742 | 2025-10-07 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 61ab34a8-ccb7-3d52-b454-fb317390bafb | -9.9024 | -50.1914 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b6d92711-e4d7-30fd-8d84-62587c185f6a | -8.8618 | -46.0949 | 2025-10-07 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 787cd53c-e51e-3ac7-bd90-e965d6507cd0 | -14.7088 | -48.399 | 2025-10-07 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f4500dad-993a-3f38-9f23-b4c21acec6f8 | -8.501 | -46.3117 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 09c8006d-2a8c-31a9-b5d7-2d8253cafa7a | -8.5602 | -44.6264 | 2025-10-07 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0fdf6a70-b78d-3732-a34d-55a2f1d7aa6e | -11.8422 | -45.0567 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4a90f6f2-259c-3f36-ac68-b10d5c076ef4 | -10.4054 | -45.3931 | 2025-10-07 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e5af7dd8-704b-304b-a69a-05b643c9e08b | -11.8033 | -45.0856 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 427442a8-e317-3727-b91a-f24dc8481eed | -8.1885 | -44.182 | 2025-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 1e15c3d4-1f8b-3135-9961-1a34375d5171 | -3.4179 | -43.154 | 2025-10-07 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| dcc65566-6cca-3e17-a44a-89c6ac4f822e | -8.8903 | -46.8081 | 2025-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 590048ff-899d-31a2-97e3-7d3b83cfabfc | -8.2159 | -49.875 | 2025-10-07 14:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7dc33570-ce0a-3533-8fdb-5a3f17de3dbf | -10.0679 | -50.5159 | 2025-10-07 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 28ae8b07-b77a-348a-94c9-cf079bd8734d | -8.2346 | -49.8734 | 2025-10-07 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| af173ff3-9fa7-370c-a2a2-a582bac3f30a | -3.8759 | -41.5708 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 4ee121f1-fe9c-3b73-9d25-1e1b1db1d7de | -12.0318 | -45.1669 | 2025-10-07 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d320beaa-73aa-3edc-ac17-4a59dc314f42 | -3.5761 | -41.6348 | 2025-10-07 14:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 85199787-5b42-3b33-b1f1-d98466514b02 | -10.3724 | -50.3149 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0aa83042-7054-3d75-825a-446c97e90bf8 | -11.7198 | -51.4677 | 2025-10-07 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 05c41516-d144-369f-a0ca-bea870167b3d | -10.9475 | -51.127 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 06399366-636b-3b9b-9c19-c6269c979820 | -11.7837 | -45.1115 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 68bff393-1dbf-336b-9e88-dc910f43b17e | -3.1306 | -40.9824 | 2025-10-07 14:20:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 13d628b1-3351-35e2-bf54-5355dbbb98e0 | -11.7389 | -51.4656 | 2025-10-07 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ac430299-8e0a-3912-8a11-38957a9b4f68 | -11.8442 | -44.9408 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b010f9e3-c5a2-3a59-a578-c5fadcb82cb3 | -8.0866 | -44.791 | 2025-10-07 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 65219716-5539-3489-9569-c9c9a074b085 | -10.0217 | -48.2994 | 2025-10-07 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4d4dc4d8-63bc-3bbb-a3dc-e4e5c39ce7b3 | -9.746 | -47.7365 | 2025-10-07 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d4310860-5fff-3258-93b6-d1819c439b22 | -10.1569 | -45.493 | 2025-10-07 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0bd1e1f3-45be-3db0-a02e-6ccffee67885 | -11.2433 | -50.2859 | 2025-10-07 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| da7c1b76-3058-336c-b54f-97a410c1a35c | -11.7201 | -51.4465 | 2025-10-07 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 8e330b1a-444b-3f51-84ef-e1f91831a7b2 | -12.9103 | -54.7352 | 2025-10-07 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 259.7 |
| c5bb422a-860d-3fe0-b7a0-19ef1ff77d04 | -9.9021 | -50.2128 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 139665d4-cbb5-394a-9fb0-61de203df2be | -3.8761 | -41.5468 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| a014d149-c5c1-3c94-bff0-356d31681707 | -10.8731 | -51.0289 | 2025-10-07 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 5ea0bac5-0ca1-3549-ab75-7fade8132b93 | -8.1055 | -44.7891 | 2025-10-07 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| f4e7ef07-765b-37ed-b10a-098520d937cb | -10.325 | -46.9388 | 2025-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 2a5aa487-d35f-3984-8864-7167ad4eac13 | -10.3665 | -47.9978 | 2025-10-07 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a49d9bbb-97f5-3946-888f-ab2e8eadfd20 | -3.8945 | -41.5938 | 2025-10-07 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 9215367e-874c-3606-ae8c-c71ae70a4760 | -8.1888 | -44.1588 | 2025-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 13c84eb4-9116-3f0c-9704-399ad7f97af4 | -9.4275 | -47.5501 | 2025-10-07 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6781335d-cb4d-3198-8423-fdd60b5e085f | -11.9963 | -47.1944 | 2025-10-07 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ca67b4d6-eba9-32d6-80fe-393e0a35f257 | -10.1573 | -45.4701 | 2025-10-07 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2d43d779-eca7-3021-918f-83244d9cb384 | -12.4916 | -54.7364 | 2025-10-07 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c6c55688-5477-3dc3-ab4d-b28155589638 | -11.8635 | -44.938 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| bff80fd3-02d0-3d34-bdb2-1abd4050a6d5 | -9.9207 | -50.2323 | 2025-10-07 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 53740286-35aa-33b3-90af-47a23606badf | -10.1383 | -45.4725 | 2025-10-07 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| fe1668e8-a39f-328e-a002-9daa9ffd9d69 | -12.9106 | -54.7147 | 2025-10-07 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 265e042a-b353-3b2e-9b89-20717043b034 | -9.6614 | -45.6667 | 2025-10-07 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f6475218-551a-3b8f-90d5-8d81b95a082e | -9.7463 | -47.7144 | 2025-10-07 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 06390716-a054-31b6-8274-e3cd2da5bfc7 | -14.8884 | -47.2226 | 2025-10-07 14:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 140.9 |
| de3d0591-8c71-3364-ac26-1f1093347f18 | -11.8447 | -44.9176 | 2025-10-07 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |


[Clique aqui para ver as próximas entradas](README128.md)
