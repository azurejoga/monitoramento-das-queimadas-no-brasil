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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ed3d5ca-b4c8-3c4f-8677-97f037df5dcf | -12.7145 | -47.7419 | 2025-09-22 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ba6250a4-1614-3714-a1fa-742d3f55f121 | -10.3759 | -46.0788 | 2025-09-22 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 890528cb-c43d-3137-8827-dd52d75e33fb | -11.9296 | -43.4288 | 2025-09-22 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| f7efc153-a381-3b8b-b569-b177d6273904 | -14.8479 | -45.4846 | 2025-09-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| a6b1de61-8f1e-3bda-901a-1fb5fc2c4385 | -10.0131 | -46.2358 | 2025-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 32556999-aa0a-31f9-af8f-3cfd247d6165 | -10.0128 | -46.2583 | 2025-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 404.1 |
| 85414bc0-c471-328d-a8bf-611bf6bbda52 | -4.8638 | -42.2252 | 2025-09-22 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 68bf7296-df62-3a14-b020-d7879c641c2a | -15.9397 | -59.3906 | 2025-09-22 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 92736278-ec6f-334d-b959-5993d4d51710 | -11.6247 | -52.8624 | 2025-09-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 0cd00f8e-2f84-32f5-aed6-919b69e349d4 | -16.3204 | -43.0438 | 2025-09-22 14:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 99.8 |
| d36d9b01-c22b-3105-aabb-e9b8142e6ff6 | -15.8404 | -59.5799 | 2025-09-22 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 810113bd-7a2c-39d4-bbfa-d18cd0f6f9fa | -14.4721 | -44.8532 | 2025-09-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 383.0 |
| f928505b-9920-3234-bcca-6efe06fc1578 | -9.9026 | -50.17 | 2025-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f8e6ef73-101b-3e14-b9bf-04d0465a7087 | -4.2492 | -41.7407 | 2025-09-22 14:40:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| c9df5adb-881b-397d-961b-f402576f4d05 | -14.8675 | -45.481 | 2025-09-22 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 04aad7f3-fd3b-3751-b54b-df125b3bd421 | -16.4707 | -55.1509 | 2025-09-22 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 272d516d-2968-3c82-ae60-3456d642f44e | -10.5802 | -50.3148 | 2025-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 112742e2-3ee0-348b-910e-602fe631fb3e | -16.3403 | -43.0394 | 2025-09-22 14:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4e175862-fca5-3ea0-8502-6587d13ed0f9 | -10.0321 | -46.2335 | 2025-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f2a7bc5e-4fc7-38dc-a111-204328b35fb7 | -11.4862 | -43.5456 | 2025-09-22 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 74a4b595-a9fb-385f-82b5-1c3bb5cb0484 | -11.6249 | -52.8416 | 2025-09-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 77f0405e-1f7b-3f4e-bd19-f89516ce25f3 | -12.6474 | -45.1183 | 2025-09-22 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 9268d408-8d7e-3679-b043-404c1ffe8fbb | -15.9591 | -59.3887 | 2025-09-22 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 6f80ab3f-b436-3e04-8dd6-6d847e023326 | -12.647 | -45.1415 | 2025-09-22 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9ba00737-2985-3a15-b62c-b381bf296593 | -6.1878 | -41.2097 | 2025-09-22 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| afb8ea24-4c3c-3140-a966-ff92d441f24f | -11.8626 | -64.9332 | 2025-09-22 14:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5fb06495-c61b-3b1d-9b99-3146d29f801c | -5.5771 | -42.1493 | 2025-09-22 14:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 38ddef26-66d2-321a-b6a3-e0a91f0c43e8 | -6.3413 | -56.1811 | 2025-09-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8d8c4c99-e2c1-3001-a8ed-1dab265384b4 | -11.4665 | -43.5722 | 2025-09-22 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |


