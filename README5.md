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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72520a86-8975-3019-9446-745850b9bca3 | -3.54552 | -43.67944 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b956db82-51ae-30c4-9a7d-ce65432dece2 | -3.01335 | -46.71159 | 2025-12-31 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85598713-ef41-32be-b8c2-17578b2a707a | -4.6312 | -47.94154 | 2025-12-31 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf626a2d-17d0-3231-a944-35f75349639d | -5.98192 | -35.48026 | 2025-12-31 04:14:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9885bf0-675d-3c1e-9caf-20332a868bef | -6.61539 | -43.73716 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9691e8a-ffda-344b-80ff-e4289908a87d | -2.89874 | -45.09877 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56401048-c320-37da-b22b-b3fce7136b4e | -4.9 | -38.92388 | 2025-12-31 04:14:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4d416cf-d0aa-303e-8058-80d959aece9c | -3.34667 | -42.14978 | 2025-12-31 04:14:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 165581d1-5bbb-30a7-bd80-373b419d4e1b | -2.34385 | -44.89098 | 2025-12-31 04:14:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea513913-8601-316f-a148-0f89747246c1 | -3.55904 | -41.9671 | 2025-12-31 04:14:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6fda3a3c-c2f1-3c02-99d7-95caca533c44 | -3.54218 | -43.67891 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d682bf1c-c27b-3182-acf9-0f080a8d6361 | -6.96236 | -46.21944 | 2025-12-31 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f936543d-e4e2-3741-ae43-a4ab6c038644 | -3.55221 | -43.68047 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 254b56ca-c676-3769-a72c-b87c0ed2d7e1 | -1.08018 | -47.99202 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6c56eb1-13e0-33e0-8fe7-c146d3f380f1 | -1.79327 | -45.89986 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97135021-e568-3105-843c-929f26488cc3 | -1.07954 | -47.99605 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 842b97e8-fb3e-37f7-a6e3-a73883c53937 | -2.90579 | -45.09986 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0439eec-3035-3fbd-836f-a551b0448c6a | -6.4266 | -35.13704 | 2025-12-31 04:14:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b159697c-8043-30ab-af6c-fa87419ae8be | -1.79185 | -45.89678 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8720a621-4d96-387f-b960-0be5e82b0d1b | -4.32072 | -43.78752 | 2025-12-31 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0b499d7-16a1-32c9-80d9-b1728a03c04f | -1.79399 | -45.89544 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8629f5c2-e100-3d7b-96fa-81c0b66a047f | -5.47426 | -44.70254 | 2025-12-31 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e710aa9-7028-3bf9-b580-ba0d5dfd6158 | -2.63461 | -47.29444 | 2025-12-31 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fc1266d-f238-34ad-b349-a04aaeb531c2 | -4.99194 | -47.93157 | 2025-12-31 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb7c30ae-2626-3871-b998-e91e8a027a55 | -5.79505 | -43.99559 | 2025-12-31 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e632e28-270a-366f-834d-be41033d7c84 | -5.88237 | -46.50318 | 2025-12-31 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7c07a78-f98e-3ffa-8a5b-2e0bf0efb04e | -3.55387 | -43.6699 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aef27b7e-6469-34d0-8679-f35cc5b90889 | -3.87484 | -40.451 | 2025-12-31 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a62d34b0-4704-34cc-91e4-932c43025ef2 | -5.57595 | -40.62755 | 2025-12-31 04:14:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ea4ee0f3-8bec-35fe-afea-d8d6a40a082a | -6.68768 | -39.47689 | 2025-12-31 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 38315604-9f5b-3399-ae12-8ef45cfa3284 | -6.47331 | -43.53678 | 2025-12-31 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87229cb0-f669-3cf0-859a-6e599c4066c2 | -5.05716 | -47.1842 | 2025-12-31 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89f4803c-717d-3b52-a540-494c8b4a703a | -1.07588 | -47.99137 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2dedabf4-99e8-321f-92ed-47f73c0aabdf | -5.62222 | -37.33618 | 2025-12-31 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 6530be1d-f7d3-374b-8331-7ab12b6dcadb | -3.89541 | -42.5569 | 2025-12-31 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93a5051b-99e0-3dc1-ac68-1b04d47d3e72 | -6.34094 | -43.75015 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 064679f6-0be5-3591-acec-033234f0320f | -1.79116 | -45.9012 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bee2f24-e9c3-374e-b1e1-e9741504b8ce | -4.97171 | -42.78632 | 2025-12-31 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d05482f-b6e5-38e8-ac77-108a90d95e75 | -3.44081 | -41.6784 | 2025-12-31 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b6d539c-ba99-30c0-a042-fc6667fe3138 | -3.53327 | -43.67029 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b72b7920-68c8-3a32-b007-982dfe21c7df | -2.94673 | -40.42004 | 2025-12-31 04:14:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9b78e94-ec6d-39b7-88e8-ebb6f9e58891 | -3.55442 | -43.66637 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b15667b-1dd1-3442-acad-654b89c988c8 | -5.98626 | -44.57158 | 2025-12-31 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57cfa796-6c1a-356c-9b97-7e3686287f7a | -3.55166 | -43.68399 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08228d7-2baa-3ff9-9153-d1ad68b74287 | -6.79399 | -46.75792 | 2025-12-31 04:14:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 716e82f0-21b8-3ec7-99ec-4d7704df7fcd | -3.5444 | -43.66481 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d49ca7e3-b66c-3aea-82fb-9ef1c372ec2e | -5.42967 | -44.86821 | 2025-12-31 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 655f7e9a-55b0-36fc-856c-c65145d04d97 | -3.87426 | -40.45478 | 2025-12-31 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57fb4818-bc46-3c0d-b5f2-28525db2e0c8 | -3.54876 | -38.8716 | 2025-12-31 04:14:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 35e6b7e3-e111-334d-8226-a8a8b146efb1 | -7.00191 | -46.2674 | 2025-12-31 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61079022-4df5-3200-8cb1-ecbac11c4569 | -4.07479 | -42.88771 | 2025-12-31 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc75fbbb-5eba-3a04-bd14-229823c6c06a | -7.77708 | -37.19793 | 2025-12-31 04:14:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9eb45a57-b775-3377-8a1c-4be7ea286332 | -3.53995 | -43.67133 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d3bd939-e9f7-3783-823e-94304269e236 | -3.54329 | -43.67185 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9402f8e5-99ca-33af-92ed-fe2fe99fa47d | -3.34336 | -42.14927 | 2025-12-31 04:14:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9f92178d-292f-3b7e-a0a7-7fdbc6d30e6d | -7.49936 | -37.41254 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 39865666-4b11-30a9-9456-4ad0add0522e | -6.49388 | -39.03769 | 2025-12-31 04:14:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 57db2939-b388-3293-9720-efa08a1de8c9 | -3.1554 | -48.139 | 2025-12-31 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee3ee73-af3f-3390-8525-ee72ce474e2a | -6.42165 | -35.13626 | 2025-12-31 04:14:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d1e97b4-2e9f-31f0-a59b-c645925ee498 | -6.86816 | -35.44388 | 2025-12-31 04:14:00 | NOAA-21 | GUARABIRA | PARAÍBA | Brasil | 2506301 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 24bf74ee-d67e-37a6-a002-c08bfb2a9cff | -6.0005 | -43.45122 | 2025-12-31 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53f9a434-2dd7-391a-94a6-f7999d869e19 | -3.69671 | -40.81242 | 2025-12-31 04:14:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b68adae-85fb-342a-b246-00286fd3ca98 | -6.3227 | -35.80064 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOSÉ DO CAMPESTRE | RIO GRANDE DO NORTE | Brasil | 2412302 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0cf05a92-914d-3937-818a-4e5d07180510 | -3.9357 | -42.12571 | 2025-12-31 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0aa1f956-66ac-3401-b289-7169610880ff | -6.49458 | -39.03292 | 2025-12-31 04:14:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5107d310-1859-3f54-825f-7e0e07b04770 | -3.53717 | -43.66728 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5105a0ef-0e92-3056-83a2-9c9a3c43bc0e | -5.67448 | -45.20499 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdaea45c-e7aa-3b3e-9a94-77e3f25a5e75 | -4.79445 | -40.78831 | 2025-12-31 04:14:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 7ebfdada-6812-3475-9dfe-036906a97ee4 | -6.29392 | -46.99968 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52f2ad4-3a1d-33b3-97d3-9f845c96a264 | -4.44288 | -40.63567 | 2025-12-31 04:14:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c9c2655-8630-3ca0-a105-448f38d93d55 | -4.5343 | -44.33499 | 2025-12-31 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae759302-53ce-38be-8001-102d60e4c80f | -4.56702 | -40.85428 | 2025-12-31 04:14:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| edeafb7c-15f9-3a7b-828f-b04e410dfca2 | -4.1126 | -38.7238 | 2025-12-31 04:14:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a26cf744-3ee7-3dce-9eb6-29b5a04348f7 | -6.18257 | -43.41612 | 2025-12-31 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57b69966-5d35-35b8-bd6f-b6d4f9e89c4f | -0.93292 | -46.89417 | 2025-12-31 04:14:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d844f38-035b-3aca-9e57-18ce45ea07f1 | -2.70417 | -45.59709 | 2025-12-31 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6efad009-cafc-3f85-93cf-20b6117b64a6 | -3.97475 | -46.60225 | 2025-12-31 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 728ccc92-f486-3b72-acdd-ea5c9288581f | -3.55958 | -41.96364 | 2025-12-31 04:14:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5b44ece-42ea-3c94-b612-32e04d646b5b | -6.6187 | -43.73768 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7c7dc6b-3c5c-31f5-abd2-b7c762d33934 | -3.52937 | -43.67331 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccc1c164-53ff-3ad8-98d8-09e3fcc1bc7b | -4.62657 | -47.94438 | 2025-12-31 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d3408cb-4a26-3d24-96ab-0244c2f9fa35 | -2.89806 | -45.09954 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77de3225-62df-39ec-9858-1e665a08cb0f | -4.45529 | -44.124 | 2025-12-31 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d09dc95-5dc9-3f5a-8324-223bd3daaa35 | -8.78709 | -39.76024 | 2025-12-31 04:14:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b0435a4-e428-3701-9460-b8bd3fdd1e17 | -4.07533 | -42.88427 | 2025-12-31 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d01104a-9f9d-3e8f-93da-a9022999d40b | -1.79557 | -45.89735 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ba8f44a-778c-38e7-84f8-2b87c0765ae4 | -5.07222 | -43.70535 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9effa47-e7c7-31f7-b5ef-bfdfce449f4d | -2.90226 | -45.09932 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4aa1bfe8-b688-34fb-8764-8aee0d488fb1 | -10.7697 | -37.14003 | 2025-12-31 04:16:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 16e78e68-c32b-30c8-9c8e-b153c35684ab | -11.15834 | -43.32192 | 2025-12-31 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 756bf539-ebee-3fb8-af80-cad2c23d7fef | -12.6622 | -46.76091 | 2025-12-31 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37881e14-518f-3270-9edf-5282d9a2809a | -14.72332 | -53.97131 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86fd3ed2-72df-37a3-bc93-3bf882f142f6 | -12.66437 | -46.76913 | 2025-12-31 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8883554-76e4-3e39-9cf9-3f85a3ee9c76 | -16.43266 | -42.20929 | 2025-12-31 04:16:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f44258c9-70f2-3d44-a976-1d7c305d4534 | -14.72003 | -53.97271 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d48e8fa-36b5-3c24-b5bf-9960570182a1 | -14.72269 | -53.97445 | 2025-12-31 04:16:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18b2eb19-6b49-3d8c-8e40-3fde5a61d87d | -11.1561 | -43.31426 | 2025-12-31 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42c63096-3020-3baa-9a01-088639b7fb79 | -11.15276 | -43.31373 | 2025-12-31 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d300ae9-71fe-3b21-ba64-dcaef62606e0 | -15.26555 | -41.88086 | 2025-12-31 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81be458f-740f-36aa-9c57-84208988fff7 | -16.43628 | -42.20987 | 2025-12-31 04:16:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
