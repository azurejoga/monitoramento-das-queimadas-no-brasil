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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c737155-0469-3a7c-9c7e-cd5c0b3b629c | -12.83648 | -62.52154 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d71b917-968a-3e4b-8420-e573c33eedee | -12.83574 | -62.52528 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d134b18-3c6e-3616-830d-8eb12154e5ba | -12.83499 | -62.52902 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e2cf35ad-a4c4-322e-9d63-733d61214ecd | -12.83424 | -62.53276 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88b35cb6-8605-327a-ad1c-9d0fe4f702dc | -12.83096 | -62.52043 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6ca647d-1a35-37ea-966a-693fdce08352 | -12.83021 | -62.52417 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e431a624-81b8-3e8f-aeab-6932fe5dbbf1 | -12.82543 | -62.5233 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7560d8ec-c55e-3030-8f18-626ea53681f7 | -12.82471 | -62.52705 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcedf188-60d0-3b46-98b7-29b754c0f02b | -12.82469 | -62.52306 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0040691-3124-38d0-a217-7359ba74dfaf | -12.82394 | -62.5268 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9feb0db-6e27-3e56-956e-65e2e195444e | -12.82345 | -62.55793 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8b909a5-e90e-3d94-9955-8a7d73ad44f6 | -12.8227 | -62.56168 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9121f89e-bf33-3624-904d-e22675250bee | -12.8189 | -62.55715 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 789ca6f4-e51d-36e9-ad78-e44950967439 | -12.81818 | -62.5609 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 33caea06-ea18-3006-9348-5600013eed5b | -12.81792 | -62.55681 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ac1f616-0e50-3c42-aa47-4b44660e8c42 | -12.81717 | -62.56054 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c00f26d-6fcc-3d6c-958f-5ff01c75aed3 | -12.81293 | -62.52856 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82817682-7ba7-348a-b547-618944e77f90 | -12.81213 | -62.52833 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3eb6cae8-b911-33a3-b86c-9ea4e7181530 | -12.8074 | -62.52745 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7db677b-026e-3cf0-9c81-ebfd2a9c9d64 | -12.80661 | -62.52722 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2613c053-f526-38bc-84a4-c10375b138c8 | -10.37228 | -64.08837 | 2024-10-02 04:49:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57066789-8411-3ac2-8f8c-8a5923e10ed4 | -10.36597 | -64.08698 | 2024-10-02 04:49:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d0e2cd1-f478-3a3f-bf1a-c30d47fa2960 | -10.36486 | -64.09248 | 2024-10-02 04:49:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851e483c-35b7-39f8-94c3-97cbf1aca698 | -10.26226 | -63.33271 | 2024-10-02 04:49:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18bda959-3f52-3eef-9903-bcdcd8a2305a | -10.26134 | -63.33733 | 2024-10-02 04:49:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b793c23-4121-37ac-ad93-f346370f9bf8 | -10.26121 | -63.33483 | 2024-10-02 04:49:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53758a1c-b12c-38cd-9513-22c34575835d | -9.96459 | -62.99973 | 2024-10-02 04:49:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfec2b56-37c6-3e61-b7ed-23573615abeb | -9.9586 | -62.9986 | 2024-10-02 04:49:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a824d96-cea3-39d7-a30a-31e72ff01009 | -9.77771 | -63.14879 | 2024-10-02 04:49:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5f2edbe-7389-3ef4-b6b2-ce78fcab0344 | -9.5651 | -64.25727 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 330b81a3-9b9c-312a-bda8-e2d3a3be56a0 | -9.56442 | -64.2585 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76d30c65-3099-3d41-9af2-6a7b03539aea | -9.56404 | -64.26279 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8b15d1b-c00d-3e0a-8f56-19b6b5cb8956 | -9.56332 | -64.264 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e69e7de6-ec52-37ef-9f01-9d0073a46499 | -9.55754 | -64.26151 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23716dd5-9e50-3c83-b2aa-bd20264ef129 | -9.55682 | -64.26274 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2732f254-4a35-35db-9d8d-b2cdc68d6ec7 | -9.55104 | -64.26025 | 2024-10-02 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46adea5b-20d0-3238-a093-b8d7b6c6bf44 | -12.32012 | -63.71769 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55ecd289-cfc4-34d9-bfb2-73c2bbbc55c6 | -12.31413 | -63.71637 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e8bf0e2-8942-3d2f-8554-450af3ccc14b | -11.65656 | -64.01967 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c3be1fd2-3c92-3731-bd98-7b67ea251dba | -11.65499 | -64.01953 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2e15f1a5-84a6-366f-962d-4cd756f431d6 | -11.65101 | -64.01521 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3905cf02-f8a4-3399-9805-3046359de0de | -11.64945 | -64.01518 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a57a245-ef92-3131-8058-130864914cbe | -11.63028 | -64.02245 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6df5376-b90f-3330-a2af-da28665ff6d6 | -11.62929 | -64.02741 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 186f50b0-0b9c-3bb0-a1a7-9d94a36c03da | -11.6287 | -64.02212 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 15449b99-e295-3706-99ec-dd31ce7c3b14 | -11.62767 | -64.02711 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e3eaa248-3b73-3ae1-ba66-2d36aeb57996 | -11.62406 | -64.02135 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fc7454dd-7019-39c1-be26-75c3fe5efa52 | -11.61855 | -63.66887 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46c0d8b-36d4-3f6a-ad40-7b731f6d9422 | -11.61832 | -63.95363 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bb45564-9912-39f7-98cd-15b2400c68e4 | -11.61768 | -63.67312 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb459b5e-c358-3f72-bf6c-dd7726f8da0d | -11.61734 | -63.95856 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 629f4a9a-7629-3168-b2c2-898d9a8ddf6b | -23.81153 | -47.64118 | 2024-10-02 04:51:00 | AQUA_M-M | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| ca521bcf-313a-3b90-bf94-33dc3e0f5625 | -23.50707 | -47.22307 | 2024-10-02 04:51:00 | AQUA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 52da9223-9e46-313b-8c54-06967fa2f6d7 | -23.3509 | -47.00527 | 2024-10-02 04:51:00 | AQUA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 5fb41ad8-b3f1-37a9-b41c-6593d5b8452b | -23.34926 | -47.01224 | 2024-10-02 04:51:00 | AQUA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| ba692383-58e8-3e18-8d86-5bd13c44f86e | -23.34796 | -47.02171 | 2024-10-02 04:51:00 | AQUA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| b416598b-a164-3c37-b895-76a6cc52f409 | -23.1164 | -46.26138 | 2024-10-02 04:51:00 | AQUA_M-M | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| b58a4c43-45d8-3180-b1e6-a16a6e629b87 | -23.03592 | -46.88696 | 2024-10-02 04:51:00 | AQUA_M-M | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| e01d6523-b68b-37d9-8f9a-e3bfb6566a0b | -22.93435 | -43.72831 | 2024-10-02 04:51:00 | AQUA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 8133b230-18f6-318f-a06a-d82e06f093e6 | -22.92682 | -43.71618 | 2024-10-02 04:51:00 | AQUA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a70a771a-a6ef-3dc4-9cf0-264768f0225c | -22.92513 | -43.72659 | 2024-10-02 04:51:00 | AQUA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| a79ab9ce-87b5-3999-be1f-ba7126b8a174 | -22.77687 | -43.7938 | 2024-10-02 04:51:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 628a70b1-032f-3377-95d3-e5a5adf51f3e | -22.76901 | -44.22676 | 2024-10-02 04:51:00 | AQUA_M-M | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 30319f99-0012-30d4-83df-c1c2dd4c11f2 | -22.76766 | -43.79168 | 2024-10-02 04:51:00 | AQUA_M-M | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| c21299af-bd17-3b4a-ac31-40343677edd8 | -22.76728 | -44.23718 | 2024-10-02 04:51:00 | AQUA_M-M | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 699c6c89-99f9-30cb-91fb-a87eaf066096 | -22.766 | -43.80194 | 2024-10-02 04:51:00 | AQUA_M-M | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| fff00122-18ff-391d-a51a-473dec5e45ce | -22.71379 | -46.68227 | 2024-10-02 04:51:00 | AQUA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b9c12e3a-a355-3719-a2c0-72fef22f3706 | -22.66981 | -43.70312 | 2024-10-02 04:51:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| aca9578f-8326-39a6-b9db-6f7f5eccf8b6 | -22.66052 | -43.70171 | 2024-10-02 04:51:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5c5699b4-e68b-3771-a977-fbbe98f7d91c | -22.60829 | -43.96228 | 2024-10-02 04:51:00 | AQUA_M-M | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d6cdf080-eaec-36e8-b955-7560101f87a0 | -22.51155 | -43.83339 | 2024-10-02 04:51:00 | AQUA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 244582d9-1076-348b-adb0-85a3e7d7208d | -22.38905 | -49.29531 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.8 |
| 09c8779d-546c-3530-bcda-b7619367ec13 | -22.38431 | -43.523 | 2024-10-02 04:51:00 | AQUA_M-M | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 593a9f93-534d-3289-836a-33ed7b297436 | -22.38291 | -49.28685 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.1 |
| 80b80933-f692-32fb-a098-442333580cd4 | -22.38033 | -49.26911 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| a12afbff-fe3b-3ccc-abb8-cdbbda0775cd | -22.3784 | -49.31023 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| bea56bd3-a431-3c52-8e1a-927829f68d06 | -22.37747 | -43.51604 | 2024-10-02 04:51:00 | AQUA_M-M | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2267e547-232d-330e-b89c-1c6c7dfe8a2d | -22.37561 | -49.29263 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 213.8 |
| ca593112-f4d0-323e-9ff5-4f5def296272 | -22.37405 | -49.26055 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 71d629cc-45de-30bf-a831-94ffe9053003 | -22.37096 | -49.31581 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| bc7cb6de-b422-3401-a5e8-2c6d9a8c6088 | -22.3695 | -49.28404 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 216.9 |
| ac52cffb-496a-338c-865f-add5bf664198 | -22.36694 | -49.26633 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| c274021e-1b00-35f1-8b03-275a8dfe1bbe | -22.36498 | -49.30733 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| e8151b8c-b65d-30b0-ac7f-7afafa3adb04 | -22.36222 | -49.28973 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 156.1 |
| 8c2c59af-ea7f-3a26-9484-b7386414cefb | -22.35754 | -49.3129 | 2024-10-02 04:51:00 | AQUA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| ddf9c0c5-13a2-3c58-a666-6e069eb1e5b5 | -22.35712 | -44.21988 | 2024-10-02 04:51:00 | AQUA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fb81221d-9c2e-35bb-b646-c2f498fadc18 | -22.35612 | -49.28104 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 32885790-5d90-3ea6-98ea-c68d25323443 | -22.35158 | -49.30434 | 2024-10-02 04:51:00 | AQUA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 91cf99da-6d22-3792-a255-ea64ec614e81 | -22.3489 | -49.28646 | 2024-10-02 04:51:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| 6fac05f9-0c6f-3b2b-a8e6-372c63a548b6 | -22.34763 | -44.21806 | 2024-10-02 04:51:00 | AQUA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1a408535-9eba-3a6d-9598-421eb91f8c3e | -22.34583 | -44.2291 | 2024-10-02 04:51:00 | AQUA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4ebed5d9-d903-3b83-aa94-a8b71d18367c | -21.61264 | -42.8032 | 2024-10-02 04:51:00 | AQUA_M-M | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 5c1ed1d3-7700-3b5e-b4ea-1583008526cb | -21.28543 | -47.62434 | 2024-10-02 04:51:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a38b4aa4-3964-3b7b-a5d0-5ab566a712d7 | -21.28124 | -47.61708 | 2024-10-02 04:51:00 | AQUA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2ec50391-9a43-30f2-ac41-3de11b0d6785 | -20.80472 | -42.29757 | 2024-10-02 04:51:00 | AQUA_M-M | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d56c8027-eaef-3af9-8d48-60fcb289ffcb | -20.53209 | -46.25613 | 2024-10-02 04:51:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e0b17fa5-0d18-35c9-8677-b971ec1ad998 | -20.53098 | -46.26475 | 2024-10-02 04:51:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0e7655e6-1fde-335e-8b50-5911ae1002c7 | -20.52932 | -46.27136 | 2024-10-02 04:51:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b5435962-5a09-38b6-a399-d150fb604e10 | -20.51976 | -46.26304 | 2024-10-02 04:51:00 | AQUA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7a1f6ed3-6f50-326c-8ec6-cf98aa7adcda | -20.20497 | -44.74189 | 2024-10-02 04:51:00 | AQUA_M-M | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README117.md)
