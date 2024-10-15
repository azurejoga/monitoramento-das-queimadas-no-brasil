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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 114b467f-bb60-30af-83ab-01092cf99888 | -3.9505 | -46.448799 | 2024-10-15 00:18:18 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bee13e5e-8454-3dae-8491-2646823e08a5 | -3.9358 | -46.4291 | 2024-10-15 00:18:18 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6128bd-6c4a-37c9-9744-8e7b01c6cbc6 | -3.9382 | -46.439999 | 2024-10-15 00:18:18 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6018f035-5a07-3f11-bf2a-fcb3138f5de9 | -2.3363 | -47.249802 | 2024-10-15 00:18:18 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5caee3a5-7699-361a-90e0-3e3b4c81c7c8 | -2.5039 | -48.536701 | 2024-10-15 00:18:20 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed7ab7e-024d-3cb4-a813-030203e26db6 | -2.5071 | -48.550999 | 2024-10-15 00:18:20 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf65882-1350-30ae-b49f-ad9f762832ab | -2.4941 | -48.538799 | 2024-10-15 00:18:20 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab930d16-4282-3687-af86-853d03b1b194 | -2.4974 | -48.553101 | 2024-10-15 00:18:20 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f3b340-123b-3d46-9148-637055b6101f | -4.001 | -47.502399 | 2024-10-15 00:18:21 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7857049-eb0e-3b32-99b0-a6d0e9ea6e00 | -3.8455 | -46.8965 | 2024-10-15 00:18:21 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6b91ec2-45c9-3d2a-852e-72f5397bd9be | -3.8481 | -46.9081 | 2024-10-15 00:18:21 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69622b33-66ea-34eb-bcb1-2cef0c758f33 | -2.6157 | -49.260601 | 2024-10-15 00:18:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d5bd29-9323-306d-8205-b2b79d7a677f | -2.6382 | -49.4972 | 2024-10-15 00:18:21 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 940e9a98-22b3-3dd8-9d7b-442b4d715fee | -2.642 | -49.514 | 2024-10-15 00:18:21 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9509a9-16f9-301d-b4fc-ac0d97636db0 | -2.0272 | -46.9263 | 2024-10-15 00:18:22 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6553b905-81ce-3b93-a72d-b2384de8a52f | -2.488 | -49.056099 | 2024-10-15 00:18:22 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff70c8a4-70d7-3c46-b77a-0cbd2e3043cb | -3.9106 | -48.337898 | 2024-10-15 00:18:25 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9df314-8b6f-359d-875c-efd38b06a4a0 | -3.9138 | -48.352501 | 2024-10-15 00:18:25 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 259fc1f5-7b14-3a90-93b4-e761711139ed | -3.9008 | -48.34 | 2024-10-15 00:18:25 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e349b91b-8a78-3f5b-b3f1-08782b43037e | -3.9041 | -48.354599 | 2024-10-15 00:18:25 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e17dc16-cc8d-301a-afb5-7b8dca611c87 | -1.678 | -46.4291 | 2024-10-15 00:18:25 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527dcca0-56db-32ca-8890-af7b3af4e6c7 | -2.4314 | -50.209702 | 2024-10-15 00:18:27 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e373ef8-0364-3fe8-9a98-5b3fb764a68b | -2.4356 | -50.228401 | 2024-10-15 00:18:27 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb7e39d5-8944-3435-b112-ce7af36e2534 | -2.4217 | -50.2118 | 2024-10-15 00:18:27 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6fd75d-0aaf-3bf9-9b97-08e34e325500 | -2.4259 | -50.230499 | 2024-10-15 00:18:27 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7ca70f-dbc5-3bf2-8f5e-7ed747d003d7 | -1.8653 | -47.7952 | 2024-10-15 00:18:27 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a531d40-1cf7-3a54-ae4f-217d07a775b2 | -1.8681 | -47.807701 | 2024-10-15 00:18:27 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d33ee7-e8e8-30a9-ab0f-b8d3c3e2ff6a | -1.864 | -47.8349 | 2024-10-15 00:18:28 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54084c98-241b-3978-b65a-6aeda4be2b74 | -1.8514 | -47.824501 | 2024-10-15 00:18:28 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6f9d9e-134c-361e-91e6-0c29f727fcae | -1.8542 | -47.837002 | 2024-10-15 00:18:28 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c286b7b-1fab-3f7c-ae74-6bb403587c27 | -3.0344 | -53.2229 | 2024-10-15 00:18:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7c5880-4767-38d9-8867-61c1f2b92b76 | -3.0413 | -53.254002 | 2024-10-15 00:18:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afab2fbc-a412-3b01-bcfe-2f7cba89146c | -1.6288 | -47.025501 | 2024-10-15 00:18:28 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd359d2-ec68-3605-a441-7a6ee1283e55 | -3.0247 | -53.224899 | 2024-10-15 00:18:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ded0ffd-6c6c-3fb0-85f6-071abf6ce522 | -3.7243 | -48.970402 | 2024-10-15 00:18:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 752fd8d2-869b-38e1-91a4-0bee1a8306aa | -3.7279 | -48.986401 | 2024-10-15 00:18:30 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c11fe38-d74a-37e2-8f79-a71620c5938b | -3.7146 | -48.9725 | 2024-10-15 00:18:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80cb602d-3caa-31d7-8ee3-bceb7576c541 | -3.7182 | -48.988499 | 2024-10-15 00:18:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c199dd9-bbb3-3095-8f2a-a344d17f54b4 | -3.7217 | -49.004601 | 2024-10-15 00:18:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6ee05b3-fd18-31b7-b83d-b682e49f577a | -3.7084 | -48.990601 | 2024-10-15 00:18:31 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7867d9-3e2b-34a9-bcc9-58735a0cd118 | -1.4633 | -47.154999 | 2024-10-15 00:18:32 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7f10a3-08cc-3ffc-9b94-87dc0eb83e05 | -1.4658 | -47.1661 | 2024-10-15 00:18:32 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6424fd-a921-3a63-a162-2a3580e3c402 | -2.3939 | -44.8293 | 2024-10-15 00:18:37 | METOP-C | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24b086cf-64a5-31ef-b6c5-c2d3bae87937 | -3.4332 | -49.724701 | 2024-10-15 00:18:38 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb29f33-2f86-363c-8799-a65789a65ca1 | -2.5689 | -47.053902 | 2024-10-15 00:18:42 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f9f7b7-dac2-3e47-b5fb-204887877548 | -2.4429 | -46.904598 | 2024-10-15 00:18:44 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3bc84e1-73a2-3625-b7cc-9e0501b4aa49 | -3.4785 | -51.532799 | 2024-10-15 00:18:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10244432-3075-380f-b3d6-850838434ba9 | -3.4635 | -51.510899 | 2024-10-15 00:18:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 664a3c20-b387-3b1f-bf65-92f80d5d2730 | -3.4688 | -51.534901 | 2024-10-15 00:18:44 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51cd792d-d4c0-3c58-a0b3-beb320b8d29c | -11.58027 | -48.4278 | 2024-10-15 00:20:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 81e01d15-1ee1-322f-8e2f-f8dbeff14d56 | -11.57726 | -48.43499 | 2024-10-15 00:20:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 89f405c3-bba4-30e8-a1c2-187ba7c1e819 | -10.62478 | -47.7226 | 2024-10-15 00:20:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e17c536b-3c87-304b-b48d-a2a527e8a354 | -10.61746 | -47.71663 | 2024-10-15 00:20:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 265bf49d-492f-3ff6-8fdc-9c91d8a9db97 | -10.16972 | -46.2918 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a2e1cab1-5baf-3771-965f-1d1aa10b404c | -10.16679 | -46.26617 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 9df02f05-2c98-3f53-aa40-1b523e462b62 | -10.16607 | -46.29758 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c3271a73-126c-388d-9f0d-f40e83043f85 | -10.16296 | -46.27201 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f1dadf7a-0142-35c0-b0ad-a4d3ff327092 | -10.15843 | -46.31943 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 15acd52f-2be0-3c33-a1bf-f838e9dbc6ec | -10.15498 | -46.3252 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| bce53c35-148c-3c3d-a53e-bc5f7adff2a5 | -10.06449 | -47.72355 | 2024-10-15 00:20:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 675de68d-98ed-30a4-8f2a-c941eca9448d | -10.15191 | -46.29975 | 2024-10-15 00:20:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| fd0aeabb-c891-3083-9707-46adfe969a50 | -10.05682 | -47.71796 | 2024-10-15 00:20:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 9801c5fd-de11-3be3-b06d-e0d06941a880 | -10.01254 | -47.28712 | 2024-10-15 00:20:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 7f322cc7-9aca-32fa-8cfd-49c13991354c | -9.72327 | -43.864 | 2024-10-15 00:20:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 369cccc7-d371-3cee-a85a-5889fa0b747d | -8.86814 | -40.86793 | 2024-10-15 00:20:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 80a5fcbe-3f57-3119-9edd-a6abfa37b71b | -8.7231 | -44.01213 | 2024-10-15 00:20:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8c06f6d6-613c-39c0-bd82-d9f2b7542f7e | -8.42337 | -39.9611 | 2024-10-15 00:20:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 83f09d18-6d6a-3764-b33e-6fedc6cbda5e | -8.32242 | -42.7732 | 2024-10-15 00:20:00 | TERRA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 17de4625-2803-3e88-bf8c-9fa76240c4c9 | -8.24937 | -44.85061 | 2024-10-15 00:20:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 83422a96-29d6-3f5c-ba6b-063c688df2a5 | -8.13362 | -42.34845 | 2024-10-15 00:20:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e885e7c5-8043-3961-a330-93cf56a3caff | -8.01274 | -44.81968 | 2024-10-15 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9e969754-1cde-3473-b148-4479da770913 | -7.8866 | -44.54403 | 2024-10-15 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a76463a1-bd53-3348-85be-83d592146140 | -7.78181 | -43.90105 | 2024-10-15 00:20:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f26bed74-a491-3c99-82fc-dcbab4b26b12 | -7.72634 | -43.20918 | 2024-10-15 00:20:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 14073f42-e574-329f-aedc-557a1d7e17f0 | -7.72463 | -43.19608 | 2024-10-15 00:20:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 49fde997-19ab-3f7a-a87a-4558e80bc4c1 | -7.69194 | -43.23404 | 2024-10-15 00:20:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 14b81a04-9bdc-3a7f-b2d0-b6608e17661c | -7.52305 | -40.51442 | 2024-10-15 00:20:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f2db53b9-c102-3e26-a489-d9f9e1251004 | -7.38031 | -43.64724 | 2024-10-15 00:20:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d971fd19-a88b-3ac4-bb89-d47be148e28d | -7.29102 | -42.22641 | 2024-10-15 00:20:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b39c4668-6ef9-3334-aa82-28a5c271b93e | -7.21089 | -42.16387 | 2024-10-15 00:20:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6b0eb827-5709-3280-a0ae-f9567192833f | -7.17331 | -42.65341 | 2024-10-15 00:20:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9eea3eb2-c169-3e13-9d7c-ca46d0381c68 | -7.08232 | -43.03814 | 2024-10-15 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bb529eeb-855e-3117-93c2-7041eca2c7bc | -6.92866 | -38.94088 | 2024-10-15 00:20:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b11fbcdd-11cd-3388-ad2e-c87de87ca549 | -6.70582 | -43.04952 | 2024-10-15 00:20:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d494a2bc-2c4d-3367-8ab5-8b5b53d7f14f | -6.54596 | -43.67028 | 2024-10-15 00:20:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7d836b70-1021-365c-9d1d-2439e405e77f | -6.4843 | -43.87709 | 2024-10-15 00:20:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d39fd774-6899-3f8e-9608-4a4b7a0cb349 | -6.48285 | -43.88352 | 2024-10-15 00:20:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e06ce9e9-50a2-3726-baa2-cf726a470795 | -6.39896 | -39.91353 | 2024-10-15 00:20:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 57046cca-6c84-35b7-9d95-943f90797b45 | -6.39351 | -41.62487 | 2024-10-15 00:20:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c5222d39-4b55-3f13-9129-5b236a732ac6 | -6.19222 | -43.41208 | 2024-10-15 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1d0da9db-e62f-3b28-aa55-3c9052381b9e | -6.15109 | -35.22412 | 2024-10-15 00:20:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 98934749-1e56-36fd-8e0a-dd1c02b876a9 | -6.14908 | -35.21066 | 2024-10-15 00:20:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e2b9a904-e93b-38fe-964e-439bcc50552e | -6.06851 | -42.41032 | 2024-10-15 00:20:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c41e8b6f-c7dd-3fb6-b2b6-eed156bebc43 | -6.05569 | -42.38936 | 2024-10-15 00:20:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b92b5a3a-2d2e-353b-8d78-f9d9a1a0e82a | -6.0542 | -42.37827 | 2024-10-15 00:20:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 893ee976-ee8b-3cad-b00b-359a06e29c0e | -5.53301 | -41.45579 | 2024-10-15 00:20:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9dcb4c41-4396-3666-a839-d62f82c449d2 | -5.47558 | -42.78582 | 2024-10-15 00:20:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| f8023aaa-baf9-3841-a73a-a63855ba99e1 | -15.58534 | -43.21238 | 2024-10-15 00:20:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 76f92d02-93d7-39fe-bf39-c728e001c917 | -14.09385 | -46.20676 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 4a1a37fd-38b4-3409-9bb0-8b2a383c4f67 | -14.09279 | -46.20025 | 2024-10-15 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 195.6 |


[Clique aqui para ver as próximas entradas](README8.md)
