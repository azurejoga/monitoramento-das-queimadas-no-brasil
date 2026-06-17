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
| d9ebc5b5-e3c0-3361-9b46-0ab744b0bf27 | -12.8548 | -44.3625 | 2026-06-17 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 6ce4d2b4-9b9d-33ac-934a-9fbb2844fa34 | -4.3588 | -47.7636 | 2026-06-17 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 1d20e562-c59b-3822-9542-77adecd5ec07 | -12.0756 | -54.6131 | 2026-06-17 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 55e03dbe-999e-35e1-9e2b-72a2875d47b4 | -12.0758 | -54.5926 | 2026-06-17 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 90512af1-95d2-3911-b997-ea2bdf64ae61 | -9.3237 | -45.4559 | 2026-06-17 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a1f40607-ef7c-3e75-9c02-0a346c5f322c | -5.7943 | -45.0813 | 2026-06-17 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 562137ce-d4a3-354c-843c-fee0eaf80231 | -9.3234 | -45.4787 | 2026-06-17 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0554d1a1-3c40-3d73-8971-f3bcb5f8a9b9 | -12.0945 | -54.6113 | 2026-06-17 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 05fe4c77-b1bf-39c1-b941-7d40c8a216fc | -5.813 | -45.0799 | 2026-06-17 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 04893a1d-b7a0-3737-b9d9-b1d32cea3a44 | -10.5637 | -46.2135 | 2026-06-17 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e5739865-abfa-3bd1-8023-ede871639f9b | -12.84002 | -44.37399 | 2026-06-17 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 85d9c87b-b9cc-3d02-8579-d57b1e4c2b5b | -13.57381 | -48.2021 | 2026-06-17 00:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 785ddec1-7607-324e-9604-a08f015e6c57 | -12.44451 | -44.75121 | 2026-06-17 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e277c86-dfe7-3047-9283-74069979f6dd | -12.84967 | -44.37249 | 2026-06-17 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 07d7023d-1bf9-3ada-b875-7fe32b6f41cf | -13.28062 | -46.06699 | 2026-06-17 00:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 563c567e-0b7a-3a1f-8b77-2136c9a8c55c | -16.44508 | -46.36163 | 2026-06-17 00:05:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 543d1b86-ac52-3142-9d82-da0c44e40318 | -18.98449 | -52.46066 | 2026-06-17 00:05:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1ee2b51f-ddce-350a-88d5-7d1568c2a144 | -15.43725 | -41.37027 | 2026-06-17 00:05:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| f76ba4b9-1a39-3b13-837d-11d8d2a72fc6 | -13.27169 | -46.06838 | 2026-06-17 00:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 416b412a-b3e7-3ab0-9eee-93ad60b5cc5a | -12.84805 | -44.36162 | 2026-06-17 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8e363363-9efd-390c-88cb-d636f700a63f | -12.75574 | -44.49342 | 2026-06-17 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 887edcd0-8827-3331-aab5-abe398b62738 | -13.9473 | -46.02698 | 2026-06-17 00:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da5ea6c1-bb28-3b95-8297-fa1717d1da89 | -13.9486 | -46.0362 | 2026-06-17 00:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 269056f8-1642-372d-8f1b-01c21551f7a5 | -13.47896 | -49.92126 | 2026-06-17 00:05:00 | TERRA_M-M | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a7d22b60-568c-33d6-98f3-febebb59e171 | -12.26785 | -43.50562 | 2026-06-17 00:05:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| faf3ce48-88f6-38d4-8e08-f520fa5b8863 | -13.57506 | -48.21152 | 2026-06-17 00:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8df27c5c-8826-3f1e-87de-ecdf4c23c7f5 | -12.84165 | -44.38485 | 2026-06-17 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 71e5d98d-3221-3cdd-ba8e-a4db9485fb28 | -16.1689 | -51.95449 | 2026-06-17 00:05:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 82a92bb4-7b88-37ec-bea4-d1bc40ab4eb9 | -13.47064 | -49.93373 | 2026-06-17 00:05:00 | TERRA_M-M | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd8d836c-c396-3d41-a50c-8d0223e27a7b | -10.25466 | -47.35844 | 2026-06-17 00:05:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5aacd795-cad3-33a7-afd8-a61e36622a85 | -9.35248 | -45.47172 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c31a72e9-f279-351c-915b-9d9c31cc4b28 | -12.18675 | -52.77928 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4028.6 |
| 72a7edb1-dc11-3b51-acff-4f1f3fda1608 | -8.95132 | -46.99307 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f487b1f6-e4f8-3716-87ae-2ff0f78f1a8f | -12.19629 | -52.81796 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 48bbd065-4fa0-3754-8904-4ea518326d55 | -8.96918 | -46.99049 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| baae4e86-ccd4-33b6-8dcf-d55a4e4821e8 | -9.35099 | -45.46134 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a435e9ef-2832-3e81-80ae-168e85c41a04 | -11.59055 | -55.34395 | 2026-06-17 00:05:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 3e2fe112-746b-349e-aa79-240ad9a7a20b | -12.22227 | -52.77473 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 948.2 |
| 0bdbe45e-3db5-3df3-b6d1-a0bcf7e876ec | -9.30589 | -48.97282 | 2026-06-17 00:05:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f741ca51-e71b-340b-bbb9-15982c58195d | -10.54839 | -46.23281 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f963d754-5981-3228-8c7f-98821dbbcbdb | -10.98028 | -46.4856 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 87cd9346-e77c-3add-aad6-eb72e5c472a5 | -11.39684 | -47.82267 | 2026-06-17 00:05:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d8b5c5d6-0559-374e-a8ca-5ab9e7f5871e | -12.18441 | -52.81945 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| d8b19afe-f8c9-37e3-afbe-9f80e062ca37 | -10.97899 | -46.47639 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 012ea2db-bf0b-362e-85d1-ddf14939052e | -9.69516 | -47.03929 | 2026-06-17 00:05:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fbad5899-273b-379e-913f-e5fc0ba3179c | -10.53026 | -48.15421 | 2026-06-17 00:05:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| acebdefd-f5fe-3f69-9896-8b123988a903 | -10.77524 | -54.10246 | 2026-06-17 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d847c752-e914-3d39-a4af-47155fa5433b | -12.47461 | -55.12916 | 2026-06-17 00:05:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7b320f61-63bd-3b63-99ad-1b5102dfce07 | -12.20453 | -52.8285 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7484859b-2790-3e28-8860-507f64678e4f | -10.54972 | -46.24218 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dcae6fab-1873-3fb2-995b-c0d82e126bb3 | -10.6399 | -51.80945 | 2026-06-17 00:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c6e7f8f3-b591-3a4c-8ef9-7f0c4ba9b871 | -12.17299 | -52.7641 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 713.6 |
| 19cc4e24-ec3b-379f-861a-516900ef1572 | -12.23614 | -52.79012 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 402.9 |
| a6957348-a227-3248-a481-9c0768c22a17 | -12.15499 | -48.46266 | 2026-06-17 00:05:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23d6f09c-1add-31ed-a342-64f6d3aff6eb | -9.62511 | -49.01655 | 2026-06-17 00:05:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0858642a-06ae-3822-a4b8-48c4bcfbb646 | -11.88832 | -43.83579 | 2026-06-17 00:05:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29150cb0-827e-3ec4-9ddb-d59c0e9ff401 | -9.32407 | -45.47606 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9c9aa725-2172-301b-a38a-3943ec1bebf1 | -12.19664 | -52.76105 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 225.1 |
| eb5248b3-4cdc-3c52-b741-85c4290d3a81 | -10.15121 | -56.62979 | 2026-06-17 00:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| b278c44c-6878-322f-bd56-b862104c7bc3 | -10.42741 | -49.44519 | 2026-06-17 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fa76c828-c3ea-330c-b200-e1f6da6d2062 | -8.97175 | -47.0087 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5d511066-9bd3-3610-bd68-488d4a0bad26 | -8.93964 | -46.98246 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8416858a-7b6e-37eb-b03e-76bfa8e4e2a7 | -10.95459 | -46.43296 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f3849e5-a511-36ab-b2d6-38d351ebe3b9 | -12.17048 | -52.80408 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 299.8 |
| 5a319052-2178-3af2-8672-2a0e3677b6e3 | -10.56514 | -46.22067 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ee4bcd83-46f5-34d2-ab8e-bef3882d5b57 | -12.15862 | -52.80557 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9c538488-294b-3d47-b109-634fa712e469 | -12.20056 | -52.79459 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 515.8 |
| 992927ad-029b-3ab0-bb9d-834124276c1f | -12.18482 | -52.76261 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 933.2 |
| 53d7b21a-c661-3911-b0f1-a5f145aca8ff | -11.38677 | -47.81496 | 2026-06-17 00:05:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52a48110-b3a8-33f0-8dc8-e4241f9a304e | -9.3757 | -50.53716 | 2026-06-17 00:05:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 45bf2c67-0f75-3155-9609-82c82c88e7f6 | -10.56647 | -46.23011 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 30ecb901-37e4-38a7-88b9-7adaebbefad1 | -9.3131 | -45.46716 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| d74bbc66-fece-3dc8-9a5e-ca10b3af3947 | -10.56779 | -46.23945 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b90ab59-c1f3-3ab7-bfb0-78689ff8d930 | -9.8833 | -52.44415 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d9c302bb-c0ab-3f05-8bcd-3d73bfb9871a | -10.63079 | -49.03785 | 2026-06-17 00:05:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d4db4b6c-337f-3d72-be52-56a80289bdf2 | -9.34301 | -45.47317 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 518babd2-9463-39f1-9781-e760cb4e30cd | -10.5561 | -46.22205 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9bc4a974-0e2c-340e-81fa-47c88ab0ced7 | -12.19067 | -52.81307 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 259.7 |
| d089c6d5-b401-3dab-ae56-b895b1e91190 | -12.17685 | -52.79765 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 690.9 |
| 7c5c1b3c-5d84-3717-a7da-5c7eba7534af | -10.95589 | -46.44218 | 2026-06-17 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 936b4dd3-2fb6-3b31-a707-3d332041e9c2 | -12.1782 | -52.769 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2912.5 |
| b65c142b-3efb-3ded-979d-a9f1bb0edebe | -12.1986 | -52.7778 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2860.6 |
| 5bb59208-e8ab-3696-bfae-f34773c7c051 | -8.96533 | -46.96318 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a3ad59dc-ed37-314d-8e5b-d4982dc9eb1c | -12.18649 | -52.83639 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 259a4d3a-e59d-358f-920a-d494946d9d28 | -8.94091 | -46.99158 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2587770-c1b3-3340-a459-90b3d992a3de | -12.2263 | -52.80856 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| a8219b12-b55a-3aaf-98aa-ccd5274fba63 | -8.96661 | -46.97229 | 2026-06-17 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f66a6391-57b6-3faf-92de-e4ae30cb8d12 | -12.1921 | -52.7842 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4029.8 |
| 7e4c8b31-df84-3c49-90a1-15b3917f5af0 | -12.19419 | -52.80104 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 8e9ee620-76d3-3144-bcae-d01d6f9f0113 | -10.82174 | -44.30844 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 821e8ba6-00f5-3c39-baba-2af35225446f | -10.60015 | -44.33257 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c7506286-c872-3d2b-9b48-a3c575080bd7 | -10.14754 | -56.59816 | 2026-06-17 00:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 138c0320-5c9d-3db7-96e5-2835a351f2c5 | -9.31461 | -45.47751 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1f7480dc-1320-3308-81c0-1a8d72acc17b | -8.93494 | -48.00285 | 2026-06-17 00:05:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 491f4235-413a-30b7-930f-37b198276d20 | -10.63822 | -51.79601 | 2026-06-17 00:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2f4489f8-175f-360b-8ef5-4c66a77fdefa | -12.18871 | -52.7961 | 2026-06-17 00:05:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 820.2 |
| f6f9f5cc-641c-3b18-9694-dd0d659197aa | -9.88151 | -52.42965 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 334d024a-f606-3d57-80b3-16686246ffd8 | -12.08298 | -54.59491 | 2026-06-17 00:05:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8b06b6ed-022b-363f-9d16-3b8d11e87688 | -11.59284 | -55.33814 | 2026-06-17 00:05:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 1662c7e1-5596-3614-a3d2-e031658bafc3 | -9.33354 | -45.47461 | 2026-06-17 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |


[Clique aqui para ver as próximas entradas](README2.md)
