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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7172a2d7-db43-3a5e-8244-145030ec235b | -12.1673 | -45.1003 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f833ac9c-72a6-30d5-b7cd-bd580e5cf24c | -13.2644 | -47.1007 | 2025-10-18 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 2f74ec61-7fcf-3ddb-9816-799c28a5ea4f | -13.2001 | -46.4312 | 2025-10-18 13:00:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b8cc1593-1679-3960-8869-d80fb268bd05 | -11.4931 | -44.2259 | 2025-10-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 343.5 |
| 02fe6f37-3ea2-3e98-ae4d-15e53e317146 | -11.3603 | -45.2646 | 2025-10-18 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 38cd7cd4-af98-3119-bbba-7ad37589bab5 | -13.2451 | -47.1036 | 2025-10-18 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 602c0148-dabd-3cac-b509-c509529f0c71 | -11.9521 | -45.3401 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 87cfd4c5-4718-33e4-aa5c-53d61376d9c4 | -11.4944 | -44.1556 | 2025-10-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 6aab6d49-064f-3692-9c8c-1bd10f86a851 | -14.0287 | -44.6757 | 2025-10-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 24200209-8b85-3b23-8406-443f2fc26776 | -11.3792 | -44.1727 | 2025-10-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| cf8f9869-e8a9-3584-8629-73d2d51798a6 | -10.8293 | -43.9248 | 2025-10-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 55657eff-8a0c-393c-9f2a-e4925db5bae3 | -12.187 | -45.0742 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c88ba258-2ca7-3419-984f-06c108fbb14b | -11.4939 | -44.179 | 2025-10-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 3a56d087-7b73-3a25-b64c-d87d33c9eb46 | -11.4935 | -44.2024 | 2025-10-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 1f3be0fd-adc9-358f-838a-ac11e23cc296 | -11.9516 | -45.3632 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| a3e3dce0-69a7-3665-87c4-11b304784486 | -14.0905 | -43.6235 | 2025-10-18 13:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 616cc6ed-522c-33e9-b6d3-3c3b928659ae | -11.9713 | -45.3373 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 378.9 |
| 72e32015-80ef-3a77-9ce8-c3b5f588496e | -12.1678 | -45.0771 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e1af4c5d-c36d-3757-9524-eccea94f2547 | -11.4927 | -44.2493 | 2025-10-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 3a59988f-4381-373a-ba09-e5c69a7ef337 | -12.487 | -45.4664 | 2025-10-18 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 130c49db-a675-3d74-a15a-30460a5c1ab6 | -14.09 | -43.6475 | 2025-10-18 13:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f0db9d30-424e-3c82-803d-13f409981fd1 | -12.4678 | -45.4694 | 2025-10-18 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| af6eb1b9-8f80-364c-b244-9c963db1979c | -11.3792 | -44.1727 | 2025-10-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 1be0fb0c-4810-3f83-9415-4d0956717584 | -11.9713 | -45.3373 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 773.7 |
| 30b407b9-65bc-3506-87ac-bbf6e4ddfa5d | -11.9709 | -45.3603 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 772.8 |
| f250e615-0baf-39ce-96f3-a1fb9a879f9f | -11.8544 | -45.4464 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4d9cee6a-c553-3243-9904-741313a0dfdc | -11.4931 | -44.2259 | 2025-10-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 36dc79d6-b9d6-3608-a486-560ea851a774 | -12.1485 | -45.08 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8f42abba-4ca9-3bc9-bc4b-9f2f1a1a75db | 1.7664 | -55.9608 | 2025-10-18 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 66fe3191-a2f4-319b-808c-d8443aa1a717 | -11.449 | -43.4803 | 2025-10-18 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5f41f417-7a70-38af-8bfe-cb2779c42af6 | 1.7665 | -55.9411 | 2025-10-18 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1c98507d-1fad-3bc8-a572-89ff1a277654 | 1.7481 | -55.961 | 2025-10-18 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d77a96ab-2eca-3c55-8cd6-c8690db1df4f | -10.8293 | -43.9248 | 2025-10-18 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2597ddf9-3f05-3e2a-8f61-ce9608e8c134 | -12.1678 | -45.0771 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ed32ebbe-019d-36d4-bfbd-33a673b26c4b | -13.2451 | -47.1036 | 2025-10-18 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a39b30d6-3168-336a-913a-b03d78781df5 | -11.204 | -47.8318 | 2025-10-18 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 980b7a59-7966-38d3-a8d4-6caf311b058f | -14.0905 | -43.6235 | 2025-10-18 13:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 81b5eee8-1bc9-375d-80d2-df9f8bf90180 | -12.1673 | -45.1003 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| d534d172-fae5-3f88-82c7-8709c951a27b | -11.9516 | -45.3632 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 0d3fa0fc-90df-3141-b1c2-aab74dd09a16 | -12.7196 | -50.8622 | 2025-10-18 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bc925d64-3f1e-3f1d-a0ee-f7f8abfb5920 | -11.4939 | -44.179 | 2025-10-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| d3ec5ce8-230e-3b01-9aa6-b64e59ea88e0 | -10.6221 | -47.371 | 2025-10-18 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| fbbc0e27-00c0-3636-a041-9fae56ba9b68 | -13.2644 | -47.1007 | 2025-10-18 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a7fd0502-6eb1-316a-817f-9d770b442050 | -11.4927 | -44.2493 | 2025-10-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 9d0ad298-d2ef-3fe0-9c0d-974c1d56f2c8 | -11.9521 | -45.3401 | 2025-10-18 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 2e3c7840-f143-33be-85fe-d0ab8787d305 | 1.8402 | -55.6837 | 2025-10-18 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 26c423d7-4316-3f41-bcdc-c0d8f135aaf9 | -14.0092 | -44.6792 | 2025-10-18 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6f698fc7-7f65-3a14-8ee5-6dffb73cf3e4 | -12.5059 | -45.4866 | 2025-10-18 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| edb8dcec-d521-377f-b086-bd806dd85f5d | -13.2001 | -46.4312 | 2025-10-18 13:10:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 88ee3d06-149f-3d2b-bd43-cec86747506c | -11.4735 | -44.2522 | 2025-10-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c37f376e-aff7-3cb8-aa5b-39dbef38ca9a | -12.1678 | -45.0771 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 944a3f03-bdb0-32ad-8e05-8f941953d7cb | -14.0905 | -43.6235 | 2025-10-18 13:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| b2701944-300b-3001-9ee4-cc4f677de7aa | -11.204 | -47.8318 | 2025-10-18 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 23465e5d-6d75-37fc-99a9-370f7aaaab35 | -3.3089 | -42.5969 | 2025-10-18 13:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 896922f6-f50a-3d99-b5aa-02eb71b74018 | -13.2451 | -47.1036 | 2025-10-18 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 033bd103-98e2-3098-8246-0f8b0d67c3e1 | -13.011 | -47.2738 | 2025-10-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8656e14a-8fc9-3027-9aec-7969f8d158da | -10.4941 | -43.4315 | 2025-10-18 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 58c19948-c9f8-32e9-8187-fd448ad70d07 | -10.8293 | -43.9248 | 2025-10-18 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6c99f651-02a9-3cf0-89a6-924aeec05701 | -10.475 | -43.4342 | 2025-10-18 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2e6ac938-9ee5-3541-b1c0-468d8af5b961 | -12.487 | -45.4664 | 2025-10-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 4d38875d-6ddb-3844-acb2-b46d5b8c9b3a | -12.4678 | -45.4694 | 2025-10-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 98fe0665-02d3-3d89-b760-1b276d69641c | -11.449 | -43.4803 | 2025-10-18 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| fc16bdeb-c0b0-3433-94c6-a9b0ba7e8c64 | -11.496 | -44.0617 | 2025-10-18 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 89603be0-8be1-3730-a51f-4a59b281900c | -11.9713 | -45.3373 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| db0641bf-2406-3a03-849d-f033b396ec4e | -13.2005 | -46.4084 | 2025-10-18 13:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2cc1f5e2-2db8-3a3d-9323-e4fdc4aff154 | -12.1485 | -45.08 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1c85c653-2294-3500-b17e-6abbdc0daec2 | 1.7664 | -55.9608 | 2025-10-18 13:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ac90defe-4cb1-33ad-aabe-bf94f643defb | -13.6368 | -43.9446 | 2025-10-18 13:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4e14f00d-47d3-3ca8-84ef-829f2d37a45a | -3.0632 | -43.2161 | 2025-10-18 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a2c67704-05a3-36d0-88cf-f0606e62274b | -10.5335 | -43.3552 | 2025-10-18 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bf4d4f2b-5ba4-3251-9322-62ac69b5b524 | -14.09 | -43.6475 | 2025-10-18 13:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 33b0d609-1f83-39b8-9009-037c1e6d7eae | -13.8573 | -43.6193 | 2025-10-18 13:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 29e8f5e8-1980-34ee-9b0a-e59207b47c4f | -10.4937 | -43.4552 | 2025-10-18 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c91d9ab0-e051-3d8a-882e-5b4231dec722 | -12.5059 | -45.4866 | 2025-10-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bd708158-f4f5-3b2f-b3f1-73133f3de563 | -16.0324 | -43.4953 | 2025-10-18 13:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 244.0 |
| e6bb2694-a347-362c-b904-c48d98585d78 | -11.5152 | -44.0588 | 2025-10-18 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 8fa7beef-3c4f-39ac-b22b-d147379e5952 | -13.2644 | -47.1007 | 2025-10-18 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 13182003-5eff-3ceb-a697-a297f8d6b46c | -12.9524 | -47.3274 | 2025-10-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7fd6eb22-97cf-3442-bd04-fd0026e9537a | -11.8544 | -45.4464 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 22afbc89-75c3-3d55-86ef-c7365c90c3aa | -13.9438 | -42.35 | 2025-10-18 13:20:00 | GOES-19 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 154.4 |
| fbabacc2-7c63-39e0-8104-5bbf78708b51 | -13.2001 | -46.4312 | 2025-10-18 13:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f68dfc0a-edcf-3f50-b34b-4dd777e70fc8 | -12.1673 | -45.1003 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 34914211-7da5-3552-9e67-7f59e34498ce | -10.4945 | -43.4079 | 2025-10-18 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 0fb1ed86-e021-3fb9-9941-2d68f0927b11 | -13.0303 | -47.2709 | 2025-10-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f157c046-25dd-383b-9414-225b3756637a | -10.5331 | -43.3788 | 2025-10-18 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c3ed7705-2bc3-3b8d-9aa6-8e1ccba87439 | -12.9519 | -47.3499 | 2025-10-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 17affc13-9408-3301-b683-2bff0c2a5330 | -12.9716 | -47.3245 | 2025-10-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 16a9a765-e6be-3fb2-82fb-86efca34d262 | -11.9709 | -45.3603 | 2025-10-18 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 701eccd1-9c02-35e6-a0d7-34444e347791 | -12.1682 | -45.0539 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f5bcd602-4345-385b-ba49-90586dc08fd9 | -10.7044 | -44.548 | 2025-10-18 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 257a537c-2c44-3e32-ab33-72979ed139c3 | -11.6109 | -44.0678 | 2025-10-18 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 481.9 |
| e2c88542-540c-376d-85af-dd4830ae0299 | -13.2001 | -46.4312 | 2025-10-18 13:30:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3ce1562b-8e2b-38f5-93d3-61fd1dc064e8 | -14.0905 | -43.6235 | 2025-10-18 13:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 7e2868e7-7925-3127-91ee-10f8291183ec | -11.5152 | -44.0588 | 2025-10-18 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c732d84d-e6cc-3e21-9231-9e7c83ed6c60 | -12.1481 | -45.1032 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b95b3247-f680-3746-a470-b835ea5eb0ff | -12.9524 | -47.3274 | 2025-10-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ae7039c3-a310-3af3-9c01-59fc88729852 | -12.7254 | -50.4969 | 2025-10-18 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f769b21b-8782-342b-87fe-223256ca371c | -13.011 | -47.2738 | 2025-10-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0ed34667-ee11-34b7-893e-5161fbd292e8 | -13.2451 | -47.1036 | 2025-10-18 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ca1ceaf6-06a2-3e6d-b2ca-5d3c385fbc2a | -12.7063 | -50.4993 | 2025-10-18 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |


[Clique aqui para ver as próximas entradas](README92.md)
