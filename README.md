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
| 4820ff4c-ce0e-3b39-a615-1d2e3b1acc15 | -3.2239 | -48.6094 | 2025-12-04 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7b007ad2-7ed1-3941-81e3-92a592c6d234 | -6.4335 | -44.7822 | 2025-12-04 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 72ab1816-0fce-36b2-ac9c-6bc041f5ff70 | -2.8934 | -53.0001 | 2025-12-04 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 029fb69b-53f9-3ecf-b88b-265cd7145a16 | -4.1232 | -50.085 | 2025-12-04 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1783397d-8ca0-3401-b67d-6f57cbf6d5d0 | -9.9731 | -36.0634 | 2025-12-04 00:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 166.1 |
| b4d7936d-719c-3d5d-83bd-3b947f27c464 | -4.5016 | -45.7711 | 2025-12-04 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1c779c94-7208-3cd4-9745-e19a39f24301 | -3.3876 | -49.2448 | 2025-12-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 14204b8a-45f8-3399-abfa-9b8fa9390bbf | -2.9044 | -45.3494 | 2025-12-04 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b1a6c825-7634-3618-95b4-fd6dbe6a0035 | -3.2238 | -48.6308 | 2025-12-04 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 8d9a856a-b60b-35e4-813d-3060919751db | -4.1231 | -50.1061 | 2025-12-04 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a649f5d8-ac1b-3d08-acd9-77e5a59e461a | -2.5367 | -49.4618 | 2025-12-04 00:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 70df66f3-5a6a-364e-a7c5-06887d7363d5 | -2.8933 | -53.0204 | 2025-12-04 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 80364b4f-e058-3afd-8487-9d44dabbb383 | -2.5367 | -49.4618 | 2025-12-04 00:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9c2215ef-9e95-3c88-924c-8c7a0f0bea5f | -2.8934 | -53.0001 | 2025-12-04 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 55fe54c7-6da2-324f-9288-7002c068df53 | -3.2238 | -48.6308 | 2025-12-04 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 30aee8e7-24e1-39ad-bc4b-8eac7eea251e | -3.3876 | -49.2448 | 2025-12-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ed4da5cf-f1c3-3c82-88c2-2b6c4d794d00 | -6.4335 | -44.7822 | 2025-12-04 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d0a76e69-be7a-369b-a204-ba8951b18996 | -2.8933 | -53.0204 | 2025-12-04 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 43a88d63-33d2-3041-990d-dd1b010e4a79 | -3.2239 | -48.6094 | 2025-12-04 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 19f959bc-3eb3-3a74-b567-0018d9bf2463 | -4.1232 | -50.085 | 2025-12-04 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5b2259be-4d30-3d5c-b9e2-e6acd4bd02a0 | -2.3463 | -45.5917 | 2025-12-04 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9ffb3752-2b7f-3f2a-a87c-00ac4d134a36 | -2.5516 | -45.3162 | 2025-12-04 00:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 992eb708-56c8-391b-a69d-bad2d4d8466c | -4.1231 | -50.1061 | 2025-12-04 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 296e621b-0fd1-30e1-827c-1721e74044a4 | -4.5016 | -45.7711 | 2025-12-04 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9cac10ca-3e07-3efd-8129-2c618acd82f8 | -2.3462 | -45.6141 | 2025-12-04 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 86787ad7-a660-32ed-a463-5628f7c80d22 | -3.2238 | -48.6308 | 2025-12-04 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1cb83c43-850d-31ae-9e3f-bbfbf3f6a35d | -2.8934 | -53.0001 | 2025-12-04 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| b87fe9cc-0469-3dfa-9f0e-c96e8b02abb7 | -4.1232 | -50.085 | 2025-12-04 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5a7307b0-215c-39c4-b183-a6828c0ea87b | -2.4776 | -45.2285 | 2025-12-04 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cee9a699-7647-39d7-8ccc-e8bf9d521bc8 | -4.5016 | -45.7711 | 2025-12-04 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9d83828b-cadb-3dbe-b8d8-461a9df24553 | -2.3462 | -45.6141 | 2025-12-04 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| daa7805a-4632-3988-aa33-f578cb81d802 | -3.2239 | -48.6094 | 2025-12-04 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a065ca76-99c6-3da1-b8e1-51984038958b | -2.3463 | -45.5917 | 2025-12-04 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 01a48733-36d8-32e5-b6b5-18b220fd89dd | -2.5367 | -49.4618 | 2025-12-04 00:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d2a283d5-6db7-30e2-b337-bb0f1b7f6c49 | -2.8933 | -53.0204 | 2025-12-04 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c9a28733-1419-3800-b544-01f3e4edbf2e | -20.92342 | -56.38061 | 2025-12-04 00:28:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 36.0 |
| a8d3e85c-8a9f-3802-9a98-4a8bf03f7d0f | -22.96694 | -49.95406 | 2025-12-04 00:28:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 09366fb3-5566-3442-a795-47ab93f443fb | -22.96479 | -49.94862 | 2025-12-04 00:28:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| 87665a89-d6d0-3b64-bee9-a7d18761c58b | -19.70399 | -49.19958 | 2025-12-04 00:28:00 | TERRA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b1182f6d-b243-32b3-9db5-5739a59bf5cc | -22.96626 | -49.96066 | 2025-12-04 00:28:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 5e50eb64-5c85-3b66-b06e-c70f3a577341 | -20.91136 | -56.38836 | 2025-12-04 00:28:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f31b49bd-3ce5-38ec-9fd6-00b849f469ff | -4.5016 | -45.7711 | 2025-12-04 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 131.2 |
| af5acf97-207c-3123-81b4-4ad4aaa8bb37 | -2.4776 | -45.2285 | 2025-12-04 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 325b7f62-7ed0-32d8-a460-c1b4f22c2b73 | -2.8933 | -53.0204 | 2025-12-04 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1d8b7fce-dcc8-3668-9a18-d74514216fba | -3.2239 | -48.6094 | 2025-12-04 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f2bcc4a0-ae14-3f38-bb75-7d04a160a75c | -2.8934 | -53.0001 | 2025-12-04 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| b7802b27-7ec9-311d-9474-6e486a89609f | -1.423 | -53.0071 | 2025-12-04 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7379adfe-9d9c-3a20-ad7c-d21346915519 | -2.3462 | -45.6141 | 2025-12-04 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 69c73ea3-fb9a-357b-b4c7-9107ffa1f117 | -2.4962 | -45.2279 | 2025-12-04 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| acab9445-f7c2-374a-a7c7-ac7de85194ba | -2.4775 | -45.251 | 2025-12-04 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 889dbfba-da64-32d3-a20d-17dddc22e588 | -3.2238 | -48.6308 | 2025-12-04 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| dc1efd2b-8473-39a9-af02-bf9bc723e19e | -2.3463 | -45.5917 | 2025-12-04 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4bf9db7c-aca9-348d-a0a8-71bd79368cd0 | -8.99236 | -48.08904 | 2025-12-04 00:32:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e0357602-e383-3ed1-8172-29f261e8fae7 | -5.98455 | -44.58944 | 2025-12-04 00:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1641444c-9fa9-3828-9fff-5531e3a217ad | -5.34815 | -42.11283 | 2025-12-04 00:32:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| b3cdcd1b-081e-3137-9179-2c15be815010 | -8.15747 | -43.17959 | 2025-12-04 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 6fc5798a-a1f5-3fed-8807-22c77dfa054b | -9.43108 | -40.32578 | 2025-12-04 00:32:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 6bd89c5f-a964-3cce-b60e-0c1eb971d818 | -6.4261 | -44.79731 | 2025-12-04 00:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5cfaa63d-9bf0-3227-9857-40211eebfca6 | -8.98315 | -48.0904 | 2025-12-04 00:32:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e0234f2c-433d-33a3-8850-14e99449b617 | -8.99374 | -48.09878 | 2025-12-04 00:32:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce26ed10-57d7-3cee-bd10-ee7a9a9e8eef | -5.3311 | -43.5689 | 2025-12-04 00:32:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9e55c172-c51a-3984-8b5f-5382fc87a20b | -5.44387 | -46.90598 | 2025-12-04 00:32:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4e6b67b-c4f9-3a42-af0e-fa0cc105938c | -6.43805 | -44.7952 | 2025-12-04 00:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5922ff89-8458-334d-bae4-6ad5a7cc1d09 | -8.98454 | -48.10012 | 2025-12-04 00:32:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d79cb780-92c1-3635-8bc7-a48d053ed2e9 | -5.56754 | -45.41673 | 2025-12-04 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f3783e8a-6bc7-3ebf-b35d-1e9ad3a24dc0 | -8.17072 | -43.17744 | 2025-12-04 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| ebd28d91-f4ab-308f-85cf-975bf454bc1d | -5.02302 | -41.01704 | 2025-12-04 00:32:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 40.1 |
| 4b6d563a-8489-3650-80cc-b4deda5d8923 | -5.46459 | -46.90314 | 2025-12-04 00:32:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ecb1d30a-f9a3-35e2-8d4a-7e3d542e5ede | -8.16656 | -43.17162 | 2025-12-04 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 76fac985-2abc-36b4-8f00-29d8c25b8655 | -3.1124 | -54.17955 | 2025-12-04 00:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86f2e9c9-625a-359b-aaf5-079c0b228886 | -2.64132 | -48.54095 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91da03cf-78cb-3084-809f-96f4d061a0ec | 0.83371 | -50.22101 | 2025-12-04 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| adb3f273-c61f-33bb-b61f-2438204dff1b | -2.21576 | -46.2267 | 2025-12-04 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 96a2e243-3d15-3079-a4c6-0191de8c29a9 | -4.00673 | -46.5513 | 2025-12-04 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7a04e208-9c69-38ce-8669-10051e1d1a82 | -1.16079 | -48.86592 | 2025-12-04 00:34:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 33af1b8d-8c28-385c-b38b-5fa57261aa8a | -2.4198 | -45.79991 | 2025-12-04 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8edb5b0f-aa02-3b7a-a69e-96655a658feb | -3.54703 | -50.52619 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d468e5a6-5b44-3733-91df-5cc75734fd2d | -4.74201 | -44.43572 | 2025-12-04 00:34:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 450c1318-7539-3d55-8b27-6beb77106382 | -2.7908 | -47.43993 | 2025-12-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e24453d3-8952-32cf-a141-820a3460291a | -3.93673 | -50.40435 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0f21c99-516c-3613-93af-5ff51f07b99b | 1.96919 | -55.7271 | 2025-12-04 00:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8f1915b-9711-38b3-a2da-307e994394a8 | -2.6071 | -49.2624 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 57e1f356-6531-33d5-ab15-8dba2d729bec | -3.76616 | -50.17725 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 525fcfdc-638d-3476-a935-e81c2f3f0ef5 | -4.59133 | -46.05153 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bca6d68c-b70f-3576-9f83-6b6a3a0bdafb | -3.22247 | -46.85939 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0cc3e7a2-81a6-3d8d-96f7-d4b2319210a3 | -3.93077 | -43.11701 | 2025-12-04 00:34:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 13524493-85a3-38e9-97bd-aa4ce12af79f | -2.63789 | -47.31476 | 2025-12-04 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f9513a8e-a262-378c-b7fa-a4ebb37fc0de | -2.38351 | -49.38559 | 2025-12-04 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6439639e-f3da-3f39-9406-f4443ff61dc8 | -4.39949 | -45.38372 | 2025-12-04 00:34:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cc9e22e0-cc2c-3d41-8355-6d3cc9a8fc9f | -4.3959 | -43.13872 | 2025-12-04 00:34:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 934d1f09-be35-384b-80c4-89e36e26a184 | -4.17129 | -50.29874 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5fa21677-c1b9-3250-9875-ddbd6302c6db | -2.89455 | -53.01001 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 137a4158-2a6b-3a37-a21f-33b400f18168 | -3.04278 | -48.42657 | 2025-12-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| ffa48fc9-86c5-384a-846c-ca11e36342bd | -2.89584 | -53.01958 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 361314c1-f773-3433-9bd2-9f8166f54233 | -4.34506 | -45.7916 | 2025-12-04 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ee82f131-faa8-377a-be43-57cc43c932b1 | -3.76882 | -50.79746 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d2b3d12-d8be-3f3e-90ed-f19bb02b4423 | -3.22545 | -48.62371 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 192544c3-cc71-3c6b-806d-425d0f8382c4 | -4.77593 | -46.13171 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| bea0f0ed-1503-331c-ad25-56803d672644 | -0.41135 | -51.62811 | 2025-12-04 00:34:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ed8acc2f-5e1d-3933-8afe-2b2c91fa53a1 | -2.89325 | -53.00047 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |


[Clique aqui para ver as próximas entradas](README2.md)
