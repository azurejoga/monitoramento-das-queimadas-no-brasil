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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cb40ca2-cb31-3a67-96dc-f3b061d3ffb6 | -8.1179 | -45.3125 | 2025-09-06 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| fb6b4065-3e61-3ca5-bdc1-6e0fb3a7f453 | -6.139 | -44.2331 | 2025-09-06 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b52adfce-9402-311a-9919-d43d8b676039 | -7.6881 | -50.2991 | 2025-09-06 13:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9f2ad16d-497f-3ae8-87e3-7db494fd5c35 | -6.1944 | -53.2585 | 2025-09-06 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| fcfe8816-e3a8-36ec-bd2a-1f2c7f12f82a | -15.0635 | -50.1089 | 2025-09-06 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3369cbed-dfff-3179-96f5-2291dc13a7c2 | -6.1945 | -53.2381 | 2025-09-06 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b45c6f74-6565-3c90-bc23-e6e8b9e43da8 | -6.2038 | -43.3475 | 2025-09-06 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ea2dd106-804b-38f7-bd00-707f6477ced5 | -6.2036 | -43.3709 | 2025-09-06 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1ee8e0d9-f578-314b-a072-7c45df7537e9 | -11.0245 | -45.9502 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.1 |
| 93f5b7cb-4a20-3ae9-8456-a36cd039c41e | -8.4323 | -47.3191 | 2025-09-06 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 98cf21f6-aa69-3274-8aee-35ffe15171af | -11.3567 | -50.3161 | 2025-09-06 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| c96ec367-6f1f-3971-82e8-2c07fb1c7e60 | -12.8636 | -47.9877 | 2025-09-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 162b61ea-17ec-34e5-a05d-dae5a569aa4e | -11.2298 | -46.2176 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 361.8 |
| a0052e99-2cf5-3850-a91b-7881e2dabf43 | -11.6532 | -47.1512 | 2025-09-06 13:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ba8c375d-d21a-333d-ac39-29be94ced480 | -10.3327 | -46.4225 | 2025-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 47decff0-6330-366c-bbe5-1f94db02b494 | -9.6843 | -51.0819 | 2025-09-06 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 04dbce72-8c79-310c-9fc0-65541c209620 | -11.0249 | -45.9274 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0166b4ea-69c8-3c89-86fc-befe07b0d95f | -11.2302 | -46.1949 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 617.1 |
| 05e55f2c-972a-3769-beb5-db30baaf210a | -6.2296 | -42.641 | 2025-09-06 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| fdc7712a-c15b-3e2b-a246-d8c8ee35e593 | -14.1061 | -51.7113 | 2025-09-06 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| a877cafc-0b8f-3c5a-9c81-26c15b9744cf | -11.0055 | -45.9527 | 2025-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 694f88fc-f1c9-3810-88cd-12d8e9187ebe | -15.0639 | -50.087 | 2025-09-06 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6197d713-f358-355c-a388-47c8faeef9ff | -10.314 | -46.4022 | 2025-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 7a5b96a6-a81b-346b-8873-e37f16809df8 | -9.6841 | -51.103 | 2025-09-06 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| bc6bcf12-cba9-3d6c-ac22-9f4e4277c2ed | -10.5937 | -44.331 | 2025-09-06 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8e71d2c9-49d5-3c1a-9560-fff8abbb74fd | -7.0129 | -44.9613 | 2025-09-06 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f7c8d376-b185-3e4f-9677-03780bc66afc | -5.7183 | -45.2226 | 2025-09-06 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 426ade3b-e103-328c-9acb-7678edb0ab4c | -7.8593 | -44.9053 | 2025-09-06 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1e59fed1-bc1c-34a3-a072-cdd915bcdd0b | -10.6128 | -44.3284 | 2025-09-06 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| b6f01837-c9bb-30cc-aafc-bef7e14fb247 | -5.7298 | -43.9189 | 2025-09-06 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 339.5 |
| 07f4b720-eb7e-3917-9f7b-9b7e5db5677f | -15.7186 | -53.5743 | 2025-09-06 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f82ea584-ba2e-396e-8c26-0788647b38d7 | -6.2203 | -43.5791 | 2025-09-06 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 30aaccb2-53a2-3665-9789-dd049703de56 | -9.0954 | -46.9871 | 2025-09-06 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| de360bc3-8451-34c6-9dbf-623745ed705b | -11.3567 | -50.3161 | 2025-09-06 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 12175034-a324-39d3-ae17-c1db168be893 | -8.099 | -45.3144 | 2025-09-06 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3ace432a-442b-31f0-b2a1-d3d08a468e88 | -15.3064 | -52.7208 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 701a3155-6db4-3b9d-ac10-4ec2666856eb | -10.3137 | -46.4248 | 2025-09-06 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| f405d764-992b-385f-9a0c-070a6fb6ecb3 | -9.0948 | -47.0316 | 2025-09-06 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 73a5144b-15d4-3b6a-a1f1-2c21a2c4d6cc | -9.7031 | -51.0802 | 2025-09-06 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| d2d37f3f-d125-37fa-8090-d74e14f6c051 | -9.6841 | -51.103 | 2025-09-06 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 260.8 |
| e1f79281-0dde-3f9b-bd88-79a72c9e1d58 | -9.7029 | -51.1013 | 2025-09-06 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| f2677b8c-6666-3d3e-a595-1c02558f9d63 | -6.1944 | -53.2585 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 65b8389c-ada6-311b-a7a6-99a07a43306f | -5.6996 | -45.2239 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 89b6e14f-9bff-39df-b07f-38be145df2c1 | -6.2296 | -42.641 | 2025-09-06 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 4cac594e-8d84-36d0-a736-9d8bf9d7a6dc | -6.7419 | -51.975 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ccabe19f-23bb-3c70-b3cf-c6ae18222e6d | -12.8028 | -48.1739 | 2025-09-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bcd5d3bd-f759-33e7-8f41-d3d5c4e4abab | -15.7182 | -53.5954 | 2025-09-06 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1c9c2e97-8ff4-3a04-b4b6-b94d2a276fde | -6.1945 | -53.2381 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9dd550d9-3d2e-3af5-93ab-f026552f0420 | -12.8825 | -48.0073 | 2025-09-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1c37a71e-4799-3ae7-a0fd-c6b156810ebe | -9.6843 | -51.0819 | 2025-09-06 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 1d3542ee-f1aa-34d4-a442-a2380691d1ca | -6.3058 | -44.4265 | 2025-09-06 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 606fe159-dd6d-3c29-b6a8-ff1962ffe044 | -8.1179 | -45.3125 | 2025-09-06 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 218f0fce-5839-34ad-bb6c-6c134cec2db3 | -12.8636 | -47.9877 | 2025-09-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bb6cf2b1-df8e-313a-b907-c6bfa8116866 | -8.3427 | -46.9515 | 2025-09-06 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7de82e8e-5c6b-3f15-9572-e58b42e864a3 | -11.0245 | -45.9502 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.4 |
| e25ea48c-f592-3c57-ad71-db7666a77a57 | -11.6532 | -47.1512 | 2025-09-06 13:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 67bb7553-8bcd-3216-8630-39a49f6a3077 | -6.5138 | -42.4266 | 2025-09-06 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 562c51a3-28b0-3d4d-a154-5835a92e4b7f | -11.2302 | -46.1949 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 594.4 |
| 4b844a92-0453-3748-9747-04bed318dcca | -7.6881 | -50.2991 | 2025-09-06 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7b50a6bd-b0d0-310b-9fdb-1584f3cc5bac | -6.2127 | -42.4532 | 2025-09-06 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| f0c7b241-5ec9-3a45-af3a-a6d8f966c4d0 | -15.3258 | -52.7182 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 223db468-0902-3240-af4e-dfb4ff13c516 | -10.5937 | -44.331 | 2025-09-06 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 30e85e8d-dd58-351c-9c80-489787e0b292 | -7.0129 | -44.9613 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 359.9 |
| 9282dcc0-3d26-38d6-9876-393ec272c1c6 | -5.7181 | -45.2453 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eab335d0-76c7-3b5c-9ce9-c4a7195efde5 | -5.9254 | -52.0012 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e716cd68-c8e3-304e-a188-91cf7147efb9 | -5.8877 | -45.0972 | 2025-09-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7f5c5e44-4d37-3018-9ac3-149dd814f225 | -7.0132 | -44.9385 | 2025-09-06 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8b10c139-094d-36a2-a031-0965f82571a7 | -9.0951 | -47.0093 | 2025-09-06 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| a8ce846f-24ea-38c0-97b9-ed7101d8cd4d | -11.357 | -50.2946 | 2025-09-06 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ceaa83cd-0ee4-344c-a373-4caf737b5bb0 | -6.4021 | -46.0944 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 07dadbc1-97c9-3762-a0ec-a11f09e11d57 | -5.7183 | -45.2226 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 0886cc9a-c67a-36bf-81bb-655a8398ba52 | -6.139 | -44.2331 | 2025-09-06 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| dcb38937-a681-3938-b3f6-7091ee54d412 | -6.0948 | -44.9455 | 2025-09-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 38cb5c7b-9f3b-3efe-8a9d-a9078a0b4d16 | -10.314 | -46.4022 | 2025-09-06 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| db48a098-32e9-3a5e-893d-31511d0c73c8 | -6.2418 | -43.2976 | 2025-09-06 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d4883904-36a0-3b3b-8629-b42537cc31b8 | -10.3324 | -46.445 | 2025-09-06 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| fc924346-0e1e-3c01-874e-7d9ac4ad424c | -13.8006 | -52.7454 | 2025-09-06 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4c6116a8-94d9-3a91-86a5-b0737534d95d | -15.3067 | -52.6995 | 2025-09-06 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| d36be73f-cb70-3fc5-aa17-6dfca1a6dc1f | -6.2036 | -43.3709 | 2025-09-06 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 4baf159e-34e4-3e58-9d1c-fee34bcdbe8b | -11.2306 | -46.1722 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5618c6c6-d755-3835-9988-e22ee07ed7b3 | -5.73 | -43.8958 | 2025-09-06 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2607a9ea-fe78-334e-b9a7-165fa609a248 | -11.2651 | -46.3938 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 5e07fb94-eef2-399b-828b-0c4a9917b666 | -6.2421 | -43.2743 | 2025-09-06 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 084e30d6-1044-34ee-8ec6-6c2a66407495 | -11.2111 | -46.1975 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 02ca1bb2-aa13-3886-a737-da853d0d7c55 | -11.2298 | -46.2176 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 375.1 |
| 171197a9-f9d9-3dd4-b3d7-d5d98604d75d | -11.0055 | -45.9527 | 2025-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.0 |
| d4fc4ff6-88a8-33df-8017-5364e5220728 | -5.8877 | -45.0972 | 2025-09-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3dca4875-f86e-3792-953f-7c6ba0fa8170 | -6.2205 | -43.5558 | 2025-09-06 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fcfa932d-f24b-3b37-ac6c-f5ee32f8bf2a | -8.3427 | -46.9515 | 2025-09-06 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 7fcccba9-c488-320d-88aa-22f66043ba81 | -6.2203 | -43.5791 | 2025-09-06 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 42302d59-2566-33a4-be84-332f6eb8ee09 | -6.3058 | -44.4265 | 2025-09-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| dd3dcb7f-a76e-3153-bad8-220f16a1a537 | -6.139 | -44.2331 | 2025-09-06 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 8b9766ab-771f-3dd0-aa89-a1e03e467766 | -9.0951 | -47.0093 | 2025-09-06 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| c832f22d-d2ce-301a-9061-93817030c6c5 | -11.758 | -47.739 | 2025-09-06 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1120f713-1501-368e-a982-18084872b851 | -11.8153 | -51.436 | 2025-09-06 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 3d4772b0-eb5e-35e7-bd38-0fe9219b67ca | -8.5374 | -51.3278 | 2025-09-06 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 6e12ff78-d85c-32a3-bccf-a5619d361af2 | -15.7381 | -53.5717 | 2025-09-06 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d47aa682-e574-357c-9b18-62b1ae27fbe3 | -15.7186 | -53.5743 | 2025-09-06 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| fbadf84e-2866-3862-bf4f-274962835ff6 | -12.8636 | -47.9877 | 2025-09-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 354490d8-ecb7-3b7f-ba3e-a465c80cdb3f | -15.7182 | -53.5954 | 2025-09-06 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |


[Clique aqui para ver as próximas entradas](README94.md)
