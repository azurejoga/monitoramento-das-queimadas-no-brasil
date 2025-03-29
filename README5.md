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
| e0d640a0-94f8-37ee-8f46-40fe71fb7b89 | -9.25806 | -60.31688 | 2025-03-29 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56e2274a-44f8-360d-b782-b977109d9c31 | -9.26338 | -60.31256 | 2025-03-29 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bda0996-4c07-3a2f-92ce-65e02bde7dae | -9.26273 | -60.31754 | 2025-03-29 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec173d4d-3e20-306e-aba8-b0c66b59a533 | -20.57883 | -56.03978 | 2025-03-29 05:53:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a28c2768-fdc5-37fd-b685-1d0546b0b00c | -20.57278 | -56.03555 | 2025-03-29 06:03:00 | AQUA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8e7a3cac-cde8-3635-8d3b-953c985af3ce | -20.58166 | -56.03708 | 2025-03-29 06:03:00 | AQUA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 17b437d9-96bb-39cc-993e-3b19757a297c | 2.30691 | -61.60962 | 2025-03-29 06:10:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3926904-6718-3d1a-9bbb-9a46684d1db8 | 2.18231 | -61.81328 | 2025-03-29 06:10:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb18472-dcf3-36b2-a570-82f580fb8b19 | 2.18174 | -61.80978 | 2025-03-29 06:10:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6eb0327f-efbb-3794-bd88-3e7afb54021f | -7.81144 | -45.55068 | 2025-03-29 12:29:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 66ba26bf-a576-3a91-ad9f-543fbc8e35be | -8.54181 | -39.56718 | 2025-03-29 12:29:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 17.2 |
| e96572cc-03fb-3f33-b61c-de02cb24620b | -11.33343 | -41.67533 | 2025-03-29 12:29:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c3e44af8-225c-30df-b436-888df96ce924 | -13.1694 | -53.65277 | 2025-03-29 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 17a49a95-593c-35b0-83a5-e6dcfad144ea | -10.6058 | -43.26309 | 2025-03-29 12:29:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e6bc72cf-f3ea-3059-8b86-5c78e1b0b8ce | -13.15877 | -53.9485 | 2025-03-29 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 5d28c51f-9250-3cb8-8b76-f69b9ad94260 | -7.93037 | -45.36169 | 2025-03-29 12:29:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 630030b3-1be4-363a-8f08-8572694dc563 | -13.1107 | -53.04302 | 2025-03-29 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e11a6f09-3260-3278-a830-bb0bae31b4b3 | -15.15046 | -47.44037 | 2025-03-29 12:29:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 34d0deee-fabf-3fad-93bb-7deda645b8e5 | -7.31424 | -45.86727 | 2025-03-29 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b63a586-1f8a-3afa-b123-5ceab58da530 | -13.30513 | -54.48458 | 2025-03-29 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1a306a48-c56b-310c-af91-aa0734f5c5da | -10.60868 | -43.25753 | 2025-03-29 12:29:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5b6ae5fe-316a-3ce6-a4b2-6ff7d8afab52 | -17.40551 | -50.70979 | 2025-03-29 12:32:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a960752-b3a7-3a25-9ee3-07e3d40eefbd | -18.47569 | -50.83653 | 2025-03-29 12:32:00 | TERRA_M-T | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a45e91b-1560-38cc-bbc7-001bfac117f3 | -17.68279 | -47.84961 | 2025-03-29 12:32:00 | TERRA_M-T | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a1fab491-03ec-3ef8-b654-7f6d666db05e | -18.39577 | -44.18681 | 2025-03-29 12:32:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2429f663-b7f3-3004-8c16-7ce8877cfe84 | -17.95331 | -50.09688 | 2025-03-29 12:32:00 | TERRA_M-T | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7c18110e-c33d-3cd5-9908-0ec65d4c900a | -17.68148 | -47.8589 | 2025-03-29 12:32:00 | TERRA_M-T | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0b463b23-13a3-39ab-a342-dd781f5e32f6 | -17.23316 | -44.8785 | 2025-03-29 12:32:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15b651c8-f572-30a8-accf-ccb2ddc8e2b1 | -20.52234 | -44.64622 | 2025-03-29 12:32:00 | TERRA_M-T | CARMÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3114501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 879cac50-2f6e-33c4-92ab-e5f16ddf37eb | -17.23162 | -44.89077 | 2025-03-29 12:32:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3b10a84b-bc7f-3eda-9681-6f47097b8e00 | -18.4011 | -44.1853 | 2025-03-29 13:50:00 | GOES-16 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| af7f8df6-13ba-343d-bfd0-ebdf7dcb8f92 | -18.4011 | -44.1853 | 2025-03-29 14:30:00 | GOES-16 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 129.0 |


