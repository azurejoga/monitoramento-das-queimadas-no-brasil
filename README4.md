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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41666d4f-aa67-38a6-a3e1-f762ddf87e1b | -15.02531 | -48.16363 | 2025-08-26 00:28:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 297f0789-ba2d-3332-8aef-42c587ad6eed | -13.58774 | -48.19352 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8746c996-2b34-321c-8d83-1f19ba9f8301 | -11.30273 | -55.11798 | 2025-08-26 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 97416846-38a8-3c06-b1e9-f4278946499c | -13.16442 | -45.30058 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ed45079f-a983-3aa7-a183-988ccaf25fec | -15.10778 | -48.73943 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ea51d555-46ba-332b-8b38-b12c8ff2b3b9 | -11.62202 | -46.39109 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6f4568f5-77b7-3174-b777-b03f2402f2ba | -11.62452 | -46.40903 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c87b179a-2fc5-3bdb-b903-ef5f302e50b9 | -11.62327 | -46.40006 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a61b216d-58e8-39aa-b0c9-9c5fe8b1cd73 | -11.90864 | -47.59949 | 2025-08-26 00:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a875c43d-aa36-3e77-b41e-dd92542fc326 | -11.9199 | -46.74115 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4d290a87-6b00-3430-85ae-b8129801c4a2 | -10.86139 | -47.34315 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3c419236-dd83-3ef7-a90c-6dadef76401d | -12.08004 | -46.63223 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bc5c6221-f769-3665-9b26-49f15b9e41f6 | -12.41271 | -46.50407 | 2025-08-26 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5f81904-2944-304f-97ef-22c2a66fcb93 | -14.36201 | -51.90298 | 2025-08-26 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e25fa556-5bc4-3350-bc7c-ff78626ddd16 | -12.67931 | -47.86074 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c74aadc0-def8-35a0-87fe-55f611b047aa | -13.44268 | -51.14677 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e427e3fd-04a5-300c-aa32-33bd511df5e6 | -10.74778 | -47.05436 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 256.5 |
| c5b75589-ae80-331d-bc68-c95f6c3f8ad8 | -13.16176 | -45.28203 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 547fb62f-5f63-34a4-a617-292fcbe48333 | -13.41813 | -46.92317 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e3fbf9df-0a4d-3ebf-b212-b78040e9c55c | -11.63386 | -44.85558 | 2025-08-26 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f5e8d810-3c31-38c3-ae1b-b389edcbe005 | -15.06119 | -48.70668 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5011ab9e-795e-3105-9d06-d31114200b89 | -11.55958 | -52.13765 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| fe432e2d-39af-3408-bb86-b2dbb68123f6 | -14.25761 | -48.03584 | 2025-08-26 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b76db809-e85c-37f4-a6d5-84a3cd77d67d | -11.56055 | -52.10998 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5cf23790-296b-3115-a7e9-add2ad051aeb | -11.63673 | -44.87515 | 2025-08-26 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| faae7cb9-cd17-30f8-a219-7a7dfa896f14 | -13.61288 | -48.16959 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d8d20a7-64d7-3cc2-a28e-8f87c6908175 | -11.15211 | -44.77871 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 207833d7-2db3-3307-a4c2-6a44ced06692 | -11.62688 | -46.21931 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 234729d7-90c6-3904-b865-be68751739c4 | -12.48211 | -47.21885 | 2025-08-26 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69100466-c565-3f55-a6ab-0a73ccc0cc2f | -10.52306 | -46.76211 | 2025-08-26 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b9cc432b-d560-34a6-9096-abd6ef4e0d19 | -13.59832 | -48.20219 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 832f3e76-a7e1-31cb-81bf-a9cc09e9388c | -10.75148 | -47.08123 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 98ac9856-7f73-3588-9f44-87f91c90edc0 | -11.15845 | -44.7573 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 894426f9-6ad0-32bb-b8db-567909f71b96 | -11.55761 | -52.12084 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9c796f8e-022c-3845-832e-23d229339d63 | -11.25721 | -44.98357 | 2025-08-26 00:28:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3827a754-695d-368e-8ad2-5aff04967155 | -11.0891 | -44.7844 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c2e5aba-91b8-322d-8a1d-1181888d8671 | -13.81959 | -45.89365 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b795cd10-3f45-3f0a-90d1-db8fcc0b5a07 | -9.80773 | -43.9481 | 2025-08-26 00:28:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b72f1a32-8995-396e-b235-0b67a303c8d7 | -12.6598 | -47.85051 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ba1f985-203b-3d36-898c-3374541da695 | -15.10504 | -48.71756 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cddb37bc-7ebc-3c6a-9787-6a795ea77142 | -12.7103 | -47.88538 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e9daa598-eb7d-30bb-85d9-2fead362878a | -14.11312 | -53.99527 | 2025-08-26 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 501528db-3574-3ab9-9b09-a863d3b0fa33 | -13.17204 | -45.28996 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2b8fbc94-d4af-3a0a-97d0-ec87771b3d82 | -12.70122 | -47.88668 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fcfbb7f-f95e-3da4-b428-0cac6b844e5d | -13.45513 | -51.15427 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| aa90b7b6-694d-300e-b67e-c1cd56e6b1a9 | -11.16773 | -44.75589 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab4b9c64-e27a-30bf-8e5c-17a4a3d17aaa | -10.87025 | -47.34188 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7a1ad9c-8ca0-316f-a96d-41d85d33cfa8 | -12.37368 | -46.56154 | 2025-08-26 00:28:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 02d939e8-8ede-3dce-a2f4-97ba4a42be2f | -15.58392 | -43.80213 | 2025-08-26 00:28:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f9652feb-6528-3899-9466-cac4bc064e50 | -10.78304 | -46.38641 | 2025-08-26 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a03714b-d5a1-3633-bbdc-c2f4b9270d18 | -14.78685 | -49.18953 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 49950b6a-8354-3d57-87cb-1374c94320b8 | -12.66108 | -47.86 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 9f138a1e-4ae0-356e-a0b7-256d98b4b9bf | -11.2979 | -43.2947 | 2025-08-26 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e90b5269-ff8e-334f-8063-4043c7b55e6e | -13.51776 | -46.91185 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6492a307-3407-32d2-9e6e-0a9ae3403ac1 | -13.17337 | -45.29924 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| edd48537-3347-3e99-9c17-8e524da8d022 | -13.58905 | -48.20353 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e26b597b-f349-34f9-acd9-bf9e4b8cab3e | -12.48336 | -47.22799 | 2025-08-26 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de66beb8-7a36-363d-a57e-b56949913c19 | -9.1747 | -40.61819 | 2025-08-26 00:28:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 617446e7-2438-3026-b4d1-f69515857350 | -13.4558 | -51.16045 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 079d1e29-c1b1-364f-b27c-2acf29c54107 | -11.63211 | -46.39877 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f48fd118-28f5-34e1-a0af-267658c4ea46 | -13.52538 | -46.9013 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7cc94744-a193-3910-8165-fec26ba034c5 | -11.56265 | -52.12671 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| a2de9389-860c-39a2-b21d-4260bc511ed2 | -11.61712 | -46.22666 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b75d8374-3498-3bfd-86d6-bb543faa67f0 | -13.44582 | -46.99354 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c7fa5d5f-c1eb-3e16-9ff0-60d7fd341c4f | -11.30196 | -55.11249 | 2025-08-26 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 22a1b14a-87c5-38a0-931d-f307315d9bdd | -10.68067 | -47.17081 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df9b1b64-2d1a-3eca-98d7-e698ca09fc39 | -10.75908 | -47.071 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 683b3fd0-c0ca-3982-8c9f-01f3fc8bdc29 | -11.62077 | -46.38213 | 2025-08-26 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 703d16d3-30e5-3d2b-aeac-a1e0b998938d | -13.43328 | -51.1633 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f6930ac9-5170-33d2-9a97-544d16366514 | -11.14771 | -44.74878 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 02c42b62-edde-3ea1-b5d9-3d5a0d8b6ec6 | -13.61156 | -48.15964 | 2025-08-26 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 020c0dae-7c1d-3e9c-9660-13a78811a687 | -11.53904 | -52.12959 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 233.4 |
| 9eb51622-3c93-34a1-b5fb-00136c082aa6 | -11.537 | -52.11305 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c7029baf-bb66-31dc-85a3-c5927c792e4d | -15.11607 | -48.64899 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7362d4ff-8117-3358-9b5f-cd767d771700 | -13.4849 | -46.86998 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7441e2c3-aa04-3701-bcfd-b2578c33a2b1 | -13.16309 | -45.29131 | 2025-08-26 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d814dfc6-5077-3815-b7d5-1dba316fbfdd | -10.74018 | -47.0646 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| f1e57f01-1e4f-3bb3-867f-73b80eb6d120 | -11.54112 | -52.14645 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e6f0e7e7-131e-39e1-83d6-d59ebb99ca0a | -15.63785 | -52.7338 | 2025-08-26 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 03c3b09e-834d-3778-b159-4519cf90e3ec | -11.55292 | -52.14489 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 202.1 |
| 7ead78d8-89de-380d-9bc7-7e88c0e0ee05 | -13.43144 | -51.1482 | 2025-08-26 00:28:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3c43dc01-e439-35a3-8582-09ac47921517 | -12.73542 | -48.14583 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3e3bd4ed-920b-3ed3-890e-a064f3af57d8 | -13.41564 | -46.90488 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f3b9b8d-b7cc-3beb-98dd-74eda8285b93 | -12.74738 | -48.09502 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a53ae3c9-db8b-3e67-8c0e-09b1b5561912 | -11.54877 | -52.11148 | 2025-08-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4c0288a7-5f98-310e-ae9c-c3a034f52386 | -14.64009 | -49.08065 | 2025-08-26 00:28:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bf50df35-ade9-3966-a179-88ca1434d32c | -15.73615 | -48.16954 | 2025-08-26 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8214fbf3-1cad-3491-80f6-16b1a3a7afaa | -11.43848 | -47.32507 | 2025-08-26 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 377f0064-8aa1-3af6-8590-6e5aa1f0b6f2 | -12.78135 | -48.13999 | 2025-08-26 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f8e2a356-178f-388e-9de2-30c3c68c312a | -11.16138 | -44.77726 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 0d73b44c-9fac-3729-b21d-234798aced17 | -13.42827 | -46.93108 | 2025-08-26 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 938ea73b-c3cd-3e28-955a-b2cba2eee10f | -15.95397 | -46.89488 | 2025-08-26 00:28:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 24f8298e-73ef-3936-bb9b-9c5aa2b5ba71 | -15.07886 | -48.6655 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b5adf46b-207f-3949-a48c-83858f731303 | -10.76792 | -47.06971 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| efe81a63-5b7f-3c55-93b9-62577804ca40 | -14.7854 | -49.17777 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| fc20dc30-3af1-3872-b134-09af3f519059 | -10.75045 | -47.00841 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a4a31de-870d-34ab-873a-e04de6100daf | -10.74141 | -47.07355 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c990ff7b-4e61-39f0-8e72-fda54e38d9b6 | -11.15065 | -44.76875 | 2025-08-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 84e0e4b9-76c0-33f1-91c8-2f623b13eb96 | -15.10641 | -48.72844 | 2025-08-26 00:28:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 53319b94-28b4-3961-acc3-413f6d669d5b | -10.75785 | -47.06205 | 2025-08-26 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |


[Clique aqui para ver as próximas entradas](README5.md)
