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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1089043e-9f74-3fde-8271-1b403f121b83 | -9.46298 | -57.84133 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 571197fa-b136-3a12-9c29-9bc01ad90aef | -9.10242 | -50.02091 | 2025-06-22 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d64eae8f-dd9d-3ec0-8226-98976aef2b6f | -13.78773 | -54.29524 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c984f3a-17cf-3289-bc6c-3674f9295e50 | -11.88099 | -54.66894 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29f784a9-a418-383a-ad19-60d420e7112c | -9.4748 | -57.83218 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 391221ce-6c12-3d6a-9c84-3bd54c046c1e | -12.47727 | -54.42146 | 2025-06-22 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 110eefef-bcb2-3022-a9c3-8459436e5762 | -9.86293 | -60.29131 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a9866ebf-9158-3cba-858b-0b717ae5b4ad | -11.86939 | -54.67516 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff470e6a-e7bc-3f49-ad2a-7fa058b8cab4 | -11.0985 | -46.67772 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c499547-4756-3a39-92ea-31a26ca41c2d | -11.39035 | -54.76683 | 2025-06-22 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c6dca5a-8d45-373a-8808-5451f4cfc2d6 | -10.93283 | -57.12769 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0efcb1ce-17f7-32f8-9a04-2455483b80ca | -13.45775 | -56.70525 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44012294-754c-38ad-8e02-5db1b718601a | -9.87275 | -61.39843 | 2025-06-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6c5753-f4f0-338b-854e-a4716a4ab29d | -9.9193 | -59.91279 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 97624796-5a8a-3bc0-bf02-1f1e640277d1 | -10.92621 | -57.12661 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0abc95ba-133c-3b66-9dec-7409e77bb547 | -10.93063 | -57.12015 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17a76429-ac46-3e79-bbc3-bbea4c426601 | -10.93007 | -57.12365 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c6e0812-b67c-3357-9d13-a4d0c8a84c1b | -12.02481 | -57.0966 | 2025-06-22 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec68361-213b-375b-9871-2f6e10b56c0d | -11.14384 | -53.9393 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d212654-2bca-39f7-bad7-038923353f5f | -9.14909 | -47.15225 | 2025-06-22 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26fe5287-7298-3fe9-9ca2-709f76098233 | -12.52365 | -57.22813 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bd276ac-1c58-3630-ac44-3fde79aa35c1 | -11.62627 | -58.29028 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50bb4658-39d3-3bcf-97e0-f37dc9dc8436 | -13.14353 | -56.80397 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cefd90f-5812-34d9-8eae-578d724b1d69 | -11.61226 | -58.29168 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 363db15d-42a0-387f-b2ef-1719730d3be3 | -11.7918 | -57.23842 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f06de113-731b-39de-b94b-7cd9d813945a | -11.7885 | -57.23788 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56fd9b70-c0ca-3d86-86b1-f427fe577c0d | -9.63407 | -62.19814 | 2025-06-22 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee298ca5-86a5-37ad-99d7-23c55a148df8 | -9.47977 | -57.33186 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac930658-299b-37a6-97cb-1383fdbaebfd | -10.52627 | -53.62104 | 2025-06-22 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9228cb0b-3c26-32aa-ad09-bd8db1823f99 | -10.45681 | -47.02455 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4ec8d1b-0632-3f31-8433-77c9f2fa4e84 | -9.67604 | -56.09206 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61f1793-88a6-3f65-a745-c2d6cc66ebc0 | -10.23074 | -54.29394 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e293b9-8278-3cbe-a315-09df392c96df | -15.07913 | -48.94385 | 2025-06-22 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c011cc37-14b5-3c33-9730-4414bb3e3eb4 | -10.06357 | -49.66481 | 2025-06-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a41cad-005c-3f3d-8e32-681a99ca672f | -13.27398 | -46.83752 | 2025-06-22 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed71c67f-6d0e-3e35-8e93-e25d071bc985 | -18.42233 | -54.86831 | 2025-06-22 05:06:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8d5fe38-cd4a-3b7a-8175-0486be18da1a | -19.99197 | -47.86602 | 2025-06-22 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee42bbf0-47e2-32a2-9559-3e30f19109c6 | -19.98608 | -47.86547 | 2025-06-22 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e18a068-1ce0-356f-acb0-bfc9c5728363 | -15.93119 | -57.67418 | 2025-06-22 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ee21b5f-8ce3-3298-9ddb-5b3f152f9fde | -16.28854 | -58.59436 | 2025-06-22 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b0d1ac8c-3187-3372-8aff-0e37346018d6 | -8.11013 | -43.14478 | 2025-06-22 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 18bd79d1-ff01-3405-86d2-0291d373d894 | -8.01821 | -47.65152 | 2025-06-22 05:29:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 06d1b04a-42e3-3dd1-b0ce-3b41128f4c86 | -3.60977 | -47.53876 | 2025-06-22 05:29:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0fe53c70-cc98-3837-97d3-7d165cff644c | -8.03167 | -47.63871 | 2025-06-22 05:29:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6525e063-331a-394c-ae79-954d753acd32 | -7.09996 | -43.71537 | 2025-06-22 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 256f77f1-e0ff-3ca2-b690-4741eb3f8560 | -8.07146 | -43.10289 | 2025-06-22 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 2fb631fb-8197-3ea7-8808-c6beb3222c4d | -8.10133 | -43.14346 | 2025-06-22 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| de9cc47f-c5be-35f0-aa20-3b2c8347976f | -10.98545 | -45.08262 | 2025-06-22 05:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 60aca769-ea85-355c-a832-1176777273ed | -10.65023 | -44.4953 | 2025-06-22 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 440f9aec-a068-3751-9ac7-a3b36db8697e | -10.98397 | -45.09207 | 2025-06-22 05:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 10a503a2-6537-3777-b460-55ff614c9eec | 2.75015 | -60.36585 | 2025-06-22 05:53:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5169ced3-1024-30b4-a1a5-ca151c8b2383 | 2.74874 | -60.36813 | 2025-06-22 05:53:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 677c4332-c410-329b-82ae-3783c6674fe1 | 2.75083 | -60.37001 | 2025-06-22 05:53:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8bd6130-e756-31de-bce0-0338362af041 | -9.02973 | -61.22562 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ebb10f3-5e08-3d81-b61f-429b59d34a1f | -9.01919 | -61.22979 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea641c61-1706-3b88-9462-aed2786845cf | -9.46451 | -57.84164 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dabb9b34-675d-3b4f-bf31-4b1449d1a2ec | -9.45718 | -56.06479 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28466df0-08bf-399b-b847-b43403ef078c | -9.46521 | -56.06401 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2aa555a8-cd31-38d6-a472-a6ca8e301f63 | -8.12508 | -61.41466 | 2025-06-22 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 720f5096-1918-3ca5-b1e1-bb68aff68f9b | -11.78868 | -57.24415 | 2025-06-22 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e14bf14c-09e7-3cc2-9f6e-95fc8348f42c | -11.61949 | -58.28625 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26d4f829-e592-345b-abb3-a1d2ded1c2c1 | -9.92062 | -59.91138 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb4148cf-d176-3b65-95a9-978dd6af5718 | -11.61956 | -58.29036 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 00903172-d13b-30a2-8887-cf3b6166f4e3 | -9.92019 | -59.91488 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 51cdd7c5-5c0b-3f05-bb52-a39119bac2ee | -12.13711 | -58.18114 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63d31cf2-49b2-3888-a987-4cb6b7f9f84b | -12.13088 | -58.18018 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f128848-9d8a-3c83-8fdf-b945bf4b5243 | -9.02827 | -61.23674 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18ddbd90-cff9-31bc-8346-ff152247456f | -9.47127 | -57.83767 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 00abd91c-e07d-306e-8bbf-5572cb10f833 | -9.2588 | -57.52657 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe4b451-00ad-3319-aa72-8819c95b747f | -9.45795 | -56.05854 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 723d76c0-1141-3130-8039-65456287da5a | -11.61341 | -58.28944 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1851ce4-fcc8-34d0-a6e3-c39de2a991c9 | -9.03391 | -61.23188 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 535cec95-9f19-3b96-9ce1-43e2832df80d | -9.47069 | -57.84242 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aaaf17b0-15a5-365e-9873-045141f3860e | -11.62572 | -58.29124 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 74098abe-137d-33a8-a9f2-f1c81ef209c8 | -12.13029 | -58.18526 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a10955ad-deda-3141-9ff5-2523e0a48e99 | -9.86366 | -60.29059 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2fc6fe5-fca7-3720-ab01-db83d1bbe770 | -9.39729 | -63.26333 | 2025-06-22 05:55:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d97b87a5-fcc2-325b-8a9b-d8ab6e977be3 | -9.46403 | -56.06584 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f7dcc981-e8e5-3c63-a5a5-19bdda27e403 | -9.47011 | -57.84713 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 38b5e49c-ea86-3ff8-ba42-7d4e4e4b504a | -9.45835 | -56.06297 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8385f8d8-97d4-3e1b-b9ae-c116a539d91e | -12.13511 | -58.18277 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c34c3d29-47af-3d12-a89b-eb881505d461 | -9.45909 | -56.05666 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e37e2131-3cf2-319d-b0d1-d78dc99a3fd3 | -12.5205 | -57.24215 | 2025-06-22 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5e80b9-b1f5-3da4-afdb-445175e9ffd8 | -12.57978 | -56.96946 | 2025-06-22 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 831ca8cc-5827-38ab-ac65-efe467fa06d0 | -9.46509 | -57.83688 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9194ca2-b4f1-34ad-8ba9-14c247b8f562 | -9.25194 | -57.53057 | 2025-06-22 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e075a17-47b6-3dbd-9c9d-8f253d43a933 | -9.8757 | -61.39848 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd7ff62-64cd-3737-88c1-284d09cb1298 | -9.91924 | -59.90873 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebc333f4-d55e-394c-9c37-104068adf0fd | -9.02409 | -61.23051 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f04f9b2d-1d38-3b96-b74c-623ee73b14cd | -9.46596 | -56.05762 | 2025-06-22 05:55:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5b8872ee-3c10-3d05-8689-469ac6714018 | -9.17217 | -61.40845 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 80b22854-3878-3c13-ae9b-58c7376010d7 | -8.12529 | -61.41667 | 2025-06-22 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96a7ca2d-254e-31fd-bcbe-a1fda8ea2a34 | -11.62565 | -58.28716 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59940649-bb94-3055-be99-91145ea45543 | -11.61899 | -58.29512 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cda3dfa8-804c-3b99-8498-5bc4638519f8 | -9.63465 | -62.20141 | 2025-06-22 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d47ae12-e900-3281-8f75-8036f4cf2578 | -9.92422 | -59.91295 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37ebdd60-fc01-38ab-aab1-4b11a296fc1b | -8.66089 | -63.84369 | 2025-06-22 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe3fc69-0656-3aa9-82e2-faedee409b1a | -9.029 | -61.23122 | 2025-06-22 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 491c2862-36bb-38fb-b69e-b88779b70767 | -11.61895 | -58.29103 | 2025-06-22 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 991e90f2-7b9e-3f90-8237-3fabd7335d9c | -9.91879 | -59.9122 | 2025-06-22 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README15.md)
