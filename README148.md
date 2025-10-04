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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5f0ada-76bb-3a6d-9b07-6da2c26a4fb6 | -8.8529 | -46.7897 | 2025-10-04 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 1299fcb4-7a6b-39fc-9803-34cc8691c609 | -14.2131 | -46.0596 | 2025-10-04 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 272.4 |
| 01a255af-8030-3de3-9ed0-7b903b0ec405 | -10.5835 | -48.7178 | 2025-10-04 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3e0a5ad4-d513-314d-85ab-45f135f714d9 | -12.7194 | -48.5611 | 2025-10-04 13:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| e5eda6ef-460f-385f-94d1-dc274742a1ae | -15.958 | -43.318 | 2025-10-04 13:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 6260d9bf-4bf1-3383-a0ab-1f3d5530d91c | -7.8595 | -48.1819 | 2025-10-04 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e70a1a98-68f8-3301-ae4a-24099653f170 | -14.3894 | -45.9832 | 2025-10-04 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b816590f-7d7e-383b-b20a-31d2dd113026 | -13.3233 | -48.077 | 2025-10-04 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| da630a29-d477-3edf-9d71-d3786e317e6c | -9.3196 | -45.7515 | 2025-10-04 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 07990487-6663-323e-94d8-8789862159d7 | -9.9582 | -50.2499 | 2025-10-04 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 44f3cef3-0aa1-3771-b7eb-0df7e941e9de | -13.7473 | -51.3097 | 2025-10-04 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 31887671-316c-3178-8b19-1cc5819f113c | -7.0604 | -45.7946 | 2025-10-04 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 50d1d5ed-9510-38b0-82d4-9da742600557 | -9.9584 | -50.2286 | 2025-10-04 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 928a8a56-5861-382e-91f5-6268817c31df | -14.5941 | -52.4976 | 2025-10-04 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 30951999-93bf-3e82-acc9-ab01c9ed8256 | -11.9335 | -46.3926 | 2025-10-04 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ff908860-e155-385e-9a42-6aba57ad9e44 | -12.6516 | -46.9669 | 2025-10-04 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ade571d1-3115-3b4b-b8fe-6f5dd7618671 | -15.5408 | -46.8344 | 2025-10-04 13:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 148.0 |
| cdc8f9bd-d100-3f42-beeb-63d0b26ad546 | -13.114 | -47.9518 | 2025-10-04 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 929095bc-2d18-303e-82c9-860a4b9a76bc | -7.0555 | -42.8018 | 2025-10-04 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| bcb59d22-82b5-3ad8-babd-0d8dfaf89e89 | -13.1144 | -47.9295 | 2025-10-04 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 726be0b5-de5e-300e-814d-1631654c29a2 | -9.3379 | -45.7947 | 2025-10-04 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 06cfd3f4-7d15-3f76-bebd-94d9f239de91 | -12.9471 | -50.9838 | 2025-10-04 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 5042aa01-4a93-3669-9207-ffd40003e946 | -11.9143 | -46.3953 | 2025-10-04 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2cd72e38-5fc5-33eb-a871-0ec1c7c60ad1 | -11.9011 | -44.9786 | 2025-10-04 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ea23a613-ba6b-3d19-94db-f8395d3b95fe | -12.3853 | -50.2595 | 2025-10-04 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 12bc19be-ee4f-3731-b8c7-2fbbba54cfc0 | -7.7941 | -42.5369 | 2025-10-04 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 134.4 |
| 360cd370-33b1-3c90-99fb-b6ec32af36d7 | -10.5835 | -48.7178 | 2025-10-04 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7ca45525-7c6c-399c-b217-6ccb9447c165 | -7.8595 | -48.1819 | 2025-10-04 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 30fa345c-e44c-3343-924c-17e09d8d556e | -15.5413 | -46.8114 | 2025-10-04 13:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e3a54978-3032-3cd5-933f-23014ba69073 | -14.7527 | -48.1462 | 2025-10-04 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 502d8e1a-31b3-3f69-b5b2-05fe51a57800 | -7.5316 | -42.3985 | 2025-10-04 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 212.1 |
| 1da741d5-4d2b-3ed1-b2b0-cb6ba3f7c983 | -7.813 | -42.5349 | 2025-10-04 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| a4c6126e-0539-3b6b-b4ed-f42117dc1307 | -7.8593 | -48.2037 | 2025-10-04 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 503ad322-50c9-3671-9ab7-1927a1064329 | -9.9584 | -50.2286 | 2025-10-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ed7aac02-94aa-363f-9bce-e080ce2121a6 | -8.5458 | -47.264 | 2025-10-04 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dcd8b0b6-2011-311f-b042-3ebdbaf8be03 | -11.792 | -46.8409 | 2025-10-04 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5d2c071c-1fa5-3499-a143-1d69851182f1 | -10.6024 | -48.7157 | 2025-10-04 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d2e1ae0c-4de7-30bf-8f28-e844e6e12201 | -7.7687 | -46.2255 | 2025-10-04 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 136bd1db-0ff6-3cdb-ba8a-41956ad7f9d8 | -10.2973 | -50.2799 | 2025-10-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fb2f4e5f-b1e6-3b43-9abe-91dcbab63ef8 | -12.8401 | -50.504 | 2025-10-04 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 15344cae-51c1-3c03-92d9-326be0c4f6c4 | -7.0372 | -42.7563 | 2025-10-04 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 62c41ce1-18c0-3abd-9090-4aa3a4c99a0b | -9.9393 | -50.2518 | 2025-10-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 8aac0f64-256a-3c8b-a946-db0ab9bdc8d5 | -15.5211 | -46.838 | 2025-10-04 13:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f9545842-157e-3f60-a64e-7d111d6d85cf | -14.6521 | -48.3188 | 2025-10-04 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| be907c2b-26ce-307b-a8ee-5baedaa92539 | -7.0558 | -42.7782 | 2025-10-04 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| e7da5dd6-ac43-3372-a62b-9afa88e0bcf9 | -7.7938 | -42.5607 | 2025-10-04 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 280106bb-6059-3b30-ab66-f8e9a0e402ca | -8.9948 | -47.4845 | 2025-10-04 13:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3c1d564b-2112-3a8f-99c0-0a9724566160 | -13.3131 | -47.5876 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 761296c0-7ab1-3b22-abf9-a7b42e10c924 | -13.3127 | -47.61 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 144.2 |
| c36214ca-4852-32cd-8425-992a5939546c | -12.4171 | -44.0821 | 2025-10-04 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 145566a1-cb1d-302a-bc62-d2f2e9cbafa7 | -7.5502 | -42.4203 | 2025-10-04 13:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |
| 057aad2d-68b3-3541-be0e-603367a28dae | -13.3426 | -48.0742 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7cf8dcb8-ea67-335a-b087-f03344178ef5 | -7.5504 | -42.3965 | 2025-10-04 13:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 350.5 |
| b39b05ad-d83f-3f5f-a354-90af2ff14821 | -11.4486 | -43.504 | 2025-10-04 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| f834935d-6fd6-3197-ad3f-04a275179479 | -14.3899 | -45.9601 | 2025-10-04 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 218.8 |
| d8ac2227-fa6f-37db-9f16-ca2185f95bf3 | -7.0604 | -45.7946 | 2025-10-04 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 806f3a9d-0b8b-3746-b9cd-8180d4f2f89a | -7.878 | -48.2021 | 2025-10-04 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 955eecfd-56b6-3537-9e94-57415ff0096a | -12.3162 | -45.3545 | 2025-10-04 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| ce07df04-d334-3840-ad95-74cf20c5968a | -12.3158 | -45.3776 | 2025-10-04 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e8be71c3-fbcd-3aff-8377-1c3ab12a7098 | -9.3379 | -45.7947 | 2025-10-04 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7db5128b-0ba1-3664-814c-314d7d4a1031 | -14.672 | -48.2933 | 2025-10-04 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7114e2bc-1cb3-3809-b8ee-319ecda116f7 | -14.2321 | -46.0794 | 2025-10-04 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7ba4fb39-e36d-3a3f-877f-0c5e8d1d56a6 | -12.9279 | -50.9862 | 2025-10-04 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8c4b519d-732c-3180-93db-c84bbddea405 | -13.2421 | -47.2617 | 2025-10-04 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e06e2736-9d99-3537-bdca-886d5a73f526 | -7.7684 | -46.2479 | 2025-10-04 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4239349b-c87f-35ed-875c-41df76243dd6 | -8.8529 | -46.7897 | 2025-10-04 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c5836c35-b60c-3bfb-9c38-5a428fdac298 | -13.7473 | -51.3097 | 2025-10-04 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 034a71bf-8b50-3dad-9287-f88f5a2eecf7 | -7.7566 | -42.5172 | 2025-10-04 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| ba7382d8-cfad-3f5d-add9-7481d0765b37 | -9.1716 | -49.9408 | 2025-10-04 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 94ce5973-d70a-34da-b8ad-49358a20d8d1 | -7.7935 | -42.5845 | 2025-10-04 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 87921132-69aa-3ef6-bf7b-487b80167407 | -6.8774 | -47.2334 | 2025-10-04 13:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a1912235-e162-30a2-a875-21723c3638f4 | -7.0369 | -42.78 | 2025-10-04 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 202.1 |
| c174d1c3-8071-3b68-b312-f6a7291198bb | -9.9396 | -50.2304 | 2025-10-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7de30a74-31b6-3a06-aba0-4b412beb53e2 | -12.4364 | -44.079 | 2025-10-04 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 02376ea0-a3f2-3e67-869f-7dab48a7919e | -10.5838 | -48.696 | 2025-10-04 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ed3b222c-a965-3b8f-85f6-4ab62d70c8b3 | -13.3233 | -48.077 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b7a2fb74-588f-33b3-9dab-64a259224f54 | -7.5317 | -37.9919 | 2025-10-04 13:20:00 | GOES-19 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 100.0 |
| ec678518-50fc-33fe-a865-e64f358aeb7b | -14.6716 | -48.3157 | 2025-10-04 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1c664674-153a-3be5-b4c6-1b85ef2d7d73 | -13.0959 | -47.8876 | 2025-10-04 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3a7a1fdd-5b6f-3313-af17-f41a98a013f8 | -11.7962 | -48.9231 | 2025-10-04 13:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2af03286-7cd5-32b0-aac8-19bcda92f1e6 | -13.2934 | -47.6129 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 143.6 |
| d1590cb3-e74b-3682-ba0a-e8e413dd5fc5 | -8.8523 | -46.8343 | 2025-10-04 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9c6b4d0f-e060-3142-a844-8d5c7ffe31c9 | -13.116 | -47.8401 | 2025-10-04 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a579b338-1ef1-3d91-988d-30fe4e6f3dc9 | -11.5492 | -47.6773 | 2025-10-04 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 57cd41e9-36d6-3e7f-8188-5c1183dfb739 | -11.5683 | -47.6749 | 2025-10-04 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 5a6a13b0-6381-3f1b-b60e-9d0b41d252f0 | -13.2938 | -47.5905 | 2025-10-04 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 142.8 |
| eb59e750-6168-3634-a19d-b6b3846133a9 | -15.5408 | -46.8344 | 2025-10-04 13:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 3701116b-1ceb-3e8b-acb0-86254f93050f | -12.3853 | -50.2595 | 2025-10-04 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 2064dee5-de05-329a-8c76-8a990aca1d2a | -15.958 | -43.318 | 2025-10-04 13:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d681b443-5fb4-33d7-8269-60821e1376da | -13.2426 | -47.2391 | 2025-10-04 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6f0b0a7c-a0fb-3d3b-a395-d571953a9080 | -12.6512 | -46.9894 | 2025-10-04 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d73ca052-4528-3d9e-be31-d2bdf62d6d87 | -14.5941 | -52.4976 | 2025-10-04 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 20476130-9d3f-3aaf-9799-8cdce51a21a6 | -12.9471 | -50.9838 | 2025-10-04 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 53bb6ceb-dbf6-380d-bfce-39041b23bdc1 | -12.8761 | -47.2937 | 2025-10-04 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| c80d62ea-4c46-3ce4-9c4f-fad99a717079 | -9.9582 | -50.2499 | 2025-10-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 207327ee-e921-3e98-8981-f8c5f8022163 | -14.3904 | -45.9369 | 2025-10-04 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a592194d-5833-370c-8126-6248ae1d3931 | -14.2126 | -46.0827 | 2025-10-04 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 131.3 |
| f5912323-05e5-39f4-9ae6-c159f529a47f | -12.7194 | -48.5611 | 2025-10-04 13:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4bd6012c-9672-31aa-9cf1-5a71851d68ac | -8.8526 | -46.812 | 2025-10-04 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 9023e76c-d95c-3ac1-8ca0-16777170715f | -9.3382 | -45.772 | 2025-10-04 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |


[Clique aqui para ver as próximas entradas](README149.md)
