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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 256a1961-a702-3557-b7c6-f902527f604e | -21.62621 | -43.46754 | 2025-04-15 03:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b504a6db-c7f5-312c-b134-5cf61ce29b04 | -21.95761 | -44.88249 | 2025-04-15 03:51:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e328dbb-1e46-354a-b198-98c248bd989b | -20.23044 | -46.55908 | 2025-04-15 03:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ae059ce6-23c0-3b95-8b16-5fe91b0b8820 | -19.45299 | -45.30634 | 2025-04-15 03:51:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d580b24e-e2fe-3a44-96f0-b4344da40af3 | -19.51215 | -44.27687 | 2025-04-15 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 530d7569-386b-311e-882d-ea1742ed53c2 | 2.3965 | -61.2859 | 2025-04-15 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5421acf9-4a75-35e4-a78d-348a50070688 | -9.61782 | -37.0326 | 2025-04-15 04:14:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec5934f9-cb79-3ada-b13c-ae2d34bf9962 | -6.35993 | -43.65363 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 659934c2-c336-368e-ba2c-f3d76f9dee85 | -7.44707 | -45.51393 | 2025-04-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a77cd45a-1e84-359e-b10f-301dfa46e1e5 | -7.45054 | -45.51449 | 2025-04-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35893442-90bc-37d1-8035-4bd193dc770c | -8.11222 | -43.12241 | 2025-04-15 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 611d34a3-e0b9-38a6-bc39-25eeaa51be52 | -9.61327 | -37.03202 | 2025-04-15 04:14:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 891081f3-583a-3703-8897-bc512a7b1ae0 | -6.3577 | -43.64616 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a812c6aa-c4b5-39b5-877d-d706a31bdda0 | -6.36381 | -43.65068 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4f901a5-1b6f-30c3-9d8b-1e911eb44b11 | -9.84203 | -37.19374 | 2025-04-15 04:14:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10091e3c-1ba1-363d-9b09-28b3b7cda98f | -6.36103 | -43.64668 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc238b43-1d1a-3d92-9c05-f6f25244e6f1 | -9.23275 | -36.88641 | 2025-04-15 04:14:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51a55b6f-74b3-3201-b85b-3cc499245af7 | -8.93928 | -44.22096 | 2025-04-15 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b66d8e8-eb3f-3bfc-94b2-4a79a1204377 | -8.94205 | -44.225 | 2025-04-15 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fccc563-e8ff-38fd-a175-d0d495874fa0 | -5.56598 | -44.53239 | 2025-04-15 04:14:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2b03832-cc2a-3656-a494-6fa9466291e8 | -9.61264 | -37.03666 | 2025-04-15 04:14:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4fdc58f-f252-3e6a-8bd7-af3635d9b927 | -6.34993 | -43.65205 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68181795-b7c6-3826-8351-304df8c29fb7 | -5.56938 | -44.53294 | 2025-04-15 04:14:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aca3bb69-436b-39cd-af89-89482ff3daa1 | -6.3627 | -43.65764 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bcb53f2d-dfc9-32fc-a279-c41bf1463d06 | -9.60809 | -37.03605 | 2025-04-15 04:14:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed148a30-b224-3776-a225-6d2894786305 | -3.39471 | -41.64167 | 2025-04-15 04:14:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca178eb2-cb2c-3d90-bb0c-8b9f74dde2cc | -6.69892 | -44.35158 | 2025-04-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ed18b0-c507-3f58-8f4c-e9dfd209406a | -7.07195 | -44.37884 | 2025-04-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b66edcf1-7ed1-31ff-9192-c25948108641 | -6.35715 | -43.64963 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9a96d92-473a-3ff0-82b8-43d944716e1f | -9.84653 | -37.19443 | 2025-04-15 04:14:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f843d894-0b51-3b53-adb5-39388ab39635 | -6.35326 | -43.65258 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8aad8834-7e79-31b9-ad9a-41bc3e5a6813 | -6.36769 | -43.64772 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5b7cef8-566f-3570-a337-10d2c93d938e | -6.36326 | -43.65416 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e8f72db-0cf4-3bb1-aff8-3208bc5b8a07 | -6.35271 | -43.65605 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| da7c4254-354c-3d8b-b314-a7bf8c1210d4 | -8.93816 | -44.22798 | 2025-04-15 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1bced90-d3c0-37b7-ab4d-889940bae10d | -8.93872 | -44.22447 | 2025-04-15 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f88a0da-4e9d-3e12-8875-5f51e412e0ba | -6.36825 | -43.64424 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d6c269-b26f-3d19-9d66-9d64496c7124 | -5.56539 | -44.53604 | 2025-04-15 04:14:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b705e932-bd75-35a9-9214-88f1a7816dbb | -6.3566 | -43.6531 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6a6fb865-ecf3-3280-8b9a-9ebbdfff8277 | -6.34938 | -43.65553 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a59bf62c-c43f-3fcf-9994-b793f086c4f1 | -6.36048 | -43.65015 | 2025-04-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b48109e6-f431-3767-a7c2-4994dc3fd1c3 | -8.94149 | -44.22851 | 2025-04-15 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e10236c1-6d0e-35c1-9099-7138a6d415da | -9.22821 | -36.88565 | 2025-04-15 04:14:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6cce782a-42d5-3e6d-9feb-0cec59cfc02a | -6.66376 | -47.59345 | 2025-04-15 04:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1d45c59-3b6a-3f78-9f2f-ba1d4049d77f | -7.44644 | -45.51777 | 2025-04-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a60a5a01-7a8d-373a-a539-0ee727390ada | -21.61944 | -48.90559 | 2025-04-15 04:17:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04cf6649-f55e-3388-8636-6efb5ad42785 | -19.9417 | -47.61136 | 2025-04-15 04:17:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca4bdcb-69fa-3ea6-8ffc-3f57cf74f186 | -19.96486 | -47.66167 | 2025-04-15 04:17:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82f8f05d-71f0-346c-98ed-334805dd8131 | -20.25743 | -45.80979 | 2025-04-15 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98eb078e-7c99-351d-81ed-1b75d787d3e6 | -20.25034 | -46.55696 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bd8cf7b-79f2-314a-b74d-efe9ed6c2cab | -22.53912 | -48.81163 | 2025-04-15 04:17:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe40f5d0-a30b-3d2e-9077-3343860e1758 | -12.23262 | -40.97985 | 2025-04-15 04:17:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22aa50ba-3191-34af-a7e2-ac50f4928350 | -21.13084 | -47.80174 | 2025-04-15 04:17:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e99c8815-0b3e-3daf-a768-96ffe704658c | -19.9377 | -47.61452 | 2025-04-15 04:17:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6568814d-f83f-32e7-964c-6b61f08eafb8 | -20.23069 | -46.55766 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f870eacb-1982-3138-b0a3-1f605a59e38c | -21.95562 | -44.88017 | 2025-04-15 04:17:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8f88c726-7597-3e5a-a7d5-d573cc53fdd4 | -20.41765 | -43.55459 | 2025-04-15 04:17:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 628afa15-6471-36ad-b900-390de08269c6 | -20.23343 | -46.56194 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d2a934c-4589-3bdd-8816-2593a21f897e | -22.78697 | -43.75538 | 2025-04-15 04:17:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 365f3714-de1d-3adc-9a25-a4956e86aa39 | -22.46132 | -47.79026 | 2025-04-15 04:17:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f809aa9f-e038-3f44-aca8-7d11a72deda7 | -13.95562 | -47.38446 | 2025-04-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5daa0124-b59f-32b0-bb26-fb2d032184c3 | -21.3504 | -48.59492 | 2025-04-15 04:17:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dc171942-5ce6-3de5-ab0d-b9c8b5616ecf | -12.82014 | -39.4494 | 2025-04-15 04:17:00 | NPP-375D | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d44ceea-9abc-35d0-a3da-9f711c80f658 | -20.25919 | -45.80938 | 2025-04-15 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c849b8d-c943-3a26-843a-3de8fa1405cc | -12.23291 | -40.98208 | 2025-04-15 04:17:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26c2415e-93d9-33c6-8453-4395411d1f09 | -20.23284 | -46.56562 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50bcd4eb-5720-3596-8aef-8389e12ac133 | -19.93832 | -47.61074 | 2025-04-15 04:17:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98622ddb-3d0f-3db6-8e88-7dbc777ee564 | -20.22952 | -46.56503 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 210191aa-edf2-32f1-90be-61b41c72ebdb | -21.99123 | -51.02798 | 2025-04-15 04:17:00 | NPP-375D | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5b078ed-1845-38a6-96a8-bbe42dfd4060 | -20.24848 | -46.55326 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12fc9216-cbbe-33ed-a5d6-003d11f2b4bd | -22.3863 | -48.38947 | 2025-04-15 04:17:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 69edfefd-02cd-3c80-be2c-810d8a3ccd3d | -21.12989 | -47.80224 | 2025-04-15 04:17:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e18879a9-19d7-3563-91f3-04fb170b2e14 | -20.2301 | -46.56134 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d23cd10-a5c5-3f65-9c38-ff1ea260c5de | -20.22619 | -46.56443 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34f7982d-9d6d-3044-8faf-ecf94109422a | -20.24789 | -46.55694 | 2025-04-15 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58125397-2778-3691-a722-0008c072cb75 | -11.7902 | -40.93218 | 2025-04-15 04:17:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25afb8e0-724e-34aa-af1b-7238a66a6efa | -21.19529 | -44.93933 | 2025-04-15 04:17:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb9edf33-e39f-3c60-8ece-6e8470959191 | -19.45249 | -45.30699 | 2025-04-15 04:19:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be9983ab-755f-3b55-a2ae-0210661fab90 | -18.8087 | -48.52325 | 2025-04-15 04:19:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9d9b6eb-5a50-3551-b33d-ae4750858413 | -30.15081 | -52.02451 | 2025-04-15 04:19:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| d3a28631-2653-37c2-a666-a749f32c6342 | -23.98401 | -48.917 | 2025-04-15 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d769623-2d9d-32c2-8205-25526f4e4a78 | -19.70905 | -44.76848 | 2025-04-15 04:19:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b10dbe02-951f-3301-ba20-a48a43917b4d | -20.3479 | -40.36174 | 2025-04-15 04:19:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8c3fb81-114b-3a49-a732-c9777192c038 | -18.8122 | -48.5239 | 2025-04-15 04:19:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4073a2f3-d58d-3376-ae2f-e0a1faa2efc5 | -23.11147 | -49.89605 | 2025-04-15 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 37078875-b16d-30a8-b232-1437ebdec767 | -19.51397 | -44.27712 | 2025-04-15 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abfc8723-f6eb-3802-81d3-24bb3c604505 | -19.31583 | -44.83265 | 2025-04-15 04:19:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3629b1bf-e5b8-38ee-8926-4adb72beaa03 | -18.14703 | -47.80171 | 2025-04-15 04:19:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d726f35c-0861-3ed7-8c67-f9c8e9af5c0a | -19.21842 | -43.22689 | 2025-04-15 04:19:00 | NPP-375D | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 15891778-2d88-3d04-a66b-2a72a6f97b1a | -20.081 | -41.56848 | 2025-04-15 04:19:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a0c9d0f5-1636-30fd-bbdd-5fc38853f03c | -19.70567 | -44.7679 | 2025-04-15 04:19:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0633e291-aa41-393e-9bce-ee7dd9033a0a | -19.417 | -44.34057 | 2025-04-15 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6460935-c370-31fd-b0dd-b4ca4a9d38c4 | -23.63082 | -46.42538 | 2025-04-15 04:19:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbfb4ce8-f45d-365c-bf1b-8916185c60bc | -17.86838 | -44.5682 | 2025-04-15 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8b7b630-14fb-3ccf-9c4b-098577ec50cd | -19.80475 | -43.99845 | 2025-04-15 04:19:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 380453ed-ba81-3cf9-ac2e-f449efd02dee | -19.45583 | -45.30756 | 2025-04-15 04:19:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00e88fb8-77b7-3098-b10a-21b5f2541675 | 2.3965 | -61.2859 | 2025-04-15 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| e7bd1379-9c08-3af9-9cad-c3ab65f18822 | 2.3964 | -61.3048 | 2025-04-15 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 976425f6-a15c-3496-a875-17e420a0ea2f | 2.3964 | -61.3048 | 2025-04-15 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0636d7c0-8118-3326-8bcd-41650e03df38 | 2.3965 | -61.2859 | 2025-04-15 04:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 98.8 |


[Clique aqui para ver as próximas entradas](README4.md)
