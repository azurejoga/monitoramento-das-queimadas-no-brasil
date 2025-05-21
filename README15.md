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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab21d5c5-5e7b-3c30-8340-01260b01b00c | -20.95362 | -56.60835 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b4917fad-d32b-3137-810b-f952766c0dea | -20.62018 | -55.03964 | 2025-05-21 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a366e04-3a1b-338f-9fc2-b122a74bb7fe | -19.9726 | -47.18876 | 2025-05-21 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2fc0e9f-788a-3c10-a199-043d11db8496 | -21.88946 | -53.31164 | 2025-05-21 04:44:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d3ead14-824c-390a-a69b-421302fa280c | -15.27814 | -60.2095 | 2025-05-21 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6b25995-0766-3026-b18c-a6339a48f90e | -20.95076 | -56.60307 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e045b143-3c36-3023-8565-4b335bdd9432 | -20.22033 | -50.7578 | 2025-05-21 04:44:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 51023dc4-f9be-3ded-b76b-a85e6e313093 | -23.40369 | -46.55724 | 2025-05-21 04:44:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16b7934e-8964-3b28-a7d5-bdda78acb670 | -19.05973 | -53.4455 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd00c767-3203-3284-a2ac-ca8d87d90ed7 | -19.06091 | -53.44499 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb6dd41e-c692-33a5-81da-a0b6834c287c | -17.11792 | -53.18674 | 2025-05-21 04:44:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b781b4d-43a5-3807-a86d-3d8abab3ade4 | -21.45928 | -47.37399 | 2025-05-21 04:44:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 11d933f1-c401-3bd2-a918-bf2d7f77bfbd | -21.67488 | -57.65785 | 2025-05-21 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 056bfd05-6bf6-3200-bb20-9195c3ad7e68 | -20.9528 | -56.61292 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 902e8110-3dba-39d3-9dac-0cd3eaed49c7 | -20.31074 | -45.58346 | 2025-05-21 04:44:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1eac546-c72f-3531-a03a-704c6c534e09 | -19.80938 | -54.41127 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e48fd05-b4e3-393e-a58a-a8d647445e69 | -20.9573 | -56.60909 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8311d92c-c0e0-365b-8e98-602631082fc2 | -19.73739 | -54.51182 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a67622c2-63cc-3f40-8a9f-dc4858dc7902 | -21.45563 | -47.36937 | 2025-05-21 04:44:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abfe50e9-72f0-3342-8b92-e8c549c1f56c | -17.99882 | -52.31458 | 2025-05-21 04:44:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d1d5c367-3231-3ba4-a5a5-dfb2e9d704f1 | -19.11149 | -52.69641 | 2025-05-21 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 807c109d-7719-3a42-8545-ce9c1c4618a5 | -23.09955 | -46.21556 | 2025-05-21 04:44:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 039f7efe-4301-3264-8852-f151b3cf7a9a | -23.44527 | -54.17611 | 2025-05-21 04:46:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6317b67-ea81-3d45-a910-44171f975a23 | -25.191 | -49.32802 | 2025-05-21 04:46:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8e1619d3-72ab-30c8-bbac-09d40a025001 | -11.0712 | -54.7868 | 2025-05-21 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 280db13c-af2a-3d89-bbee-e8ab0e5a2869 | -12.2946 | -52.4785 | 2025-05-21 04:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| c3044e59-88d6-3923-93b9-8b3dcab608a1 | 0.69266 | -51.46022 | 2025-05-21 04:59:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8ef1607-42b5-33c7-9476-9381c137a2c5 | -12.2946 | -52.4785 | 2025-05-21 05:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 54fdbe91-55ee-3088-a85e-cc28e450e59b | -11.0712 | -54.7868 | 2025-05-21 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c2aa3671-8993-374b-8b13-096be11ac106 | -6.62381 | -48.02494 | 2025-05-21 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9c9f57b-4f23-3231-abcd-21edc06dd5dc | -7.59857 | -46.64641 | 2025-05-21 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fae2f90-80ad-3c38-8494-328a0b540f3a | -5.43859 | -46.28761 | 2025-05-21 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ff940b0-7017-3d7c-87b4-44d521d0008a | -6.63238 | -55.01223 | 2025-05-21 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 456fd817-b2c2-3c3f-9fdc-bde90354cc94 | -7.9546 | -49.76469 | 2025-05-21 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 569a79e4-13a5-3ed4-b8b0-92aa9ec9e8ad | -7.87338 | -45.98906 | 2025-05-21 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ea29055-f61c-3964-bce4-67ca14f14fca | -2.95352 | -60.015 | 2025-05-21 05:01:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1440c72f-95b4-397a-aa78-b94a54449764 | -6.55632 | -54.97887 | 2025-05-21 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22afdfa2-907d-306e-ad8b-be9b28d4dd8d | -7.30957 | -55.30799 | 2025-05-21 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d30c0c8-b2a7-39cd-801c-daae51cf44ea | -7.40795 | -49.66343 | 2025-05-21 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b55789e-872c-3c52-b890-ada0efd5fe63 | -6.62455 | -48.01973 | 2025-05-21 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68c21563-fbac-3935-9eef-6b925bc61922 | -7.95021 | -49.76399 | 2025-05-21 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907c9da0-05db-3ad0-a86e-0e4327b71136 | -6.62941 | -48.02048 | 2025-05-21 05:01:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fdc002a-5b00-3f8a-bded-4d973a96d03d | -11.07586 | -54.77813 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 0d70f941-46f9-3ff4-862a-a410ef737eaf | -13.71203 | -57.47879 | 2025-05-21 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee681516-0236-3ad9-b194-f377f6fba6a5 | -11.78755 | -44.28038 | 2025-05-21 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94ac2b0a-be26-304d-b9e3-caefd03dd25b | -10.5013 | -58.86475 | 2025-05-21 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3b06e0e-8dcd-3426-9611-78e9a9b7c1db | -11.83257 | -60.9257 | 2025-05-21 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 816b7d5c-68cb-3e63-997e-e203c660aac9 | -12.12855 | -54.65647 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc84239-811a-3db6-9b1f-2b12d9f42230 | -12.33694 | -49.96641 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 162956e7-a519-35fa-8dbd-c4aab35e58c5 | -10.65238 | -59.28835 | 2025-05-21 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e64276-37cb-39a1-9adb-f30a669b903d | -11.13673 | -55.5294 | 2025-05-21 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe70e4e-5135-322c-aff8-560c5956c6ad | -12.92345 | -56.83562 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3f63b39-3ce7-35a3-8839-b439b167bc16 | -9.35514 | -57.53671 | 2025-05-21 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b67b8c-566f-30f1-a001-02da56bc42a5 | -10.05552 | -46.58166 | 2025-05-21 05:04:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16513509-354c-36c6-a8e1-0cf714ac0ce0 | -11.35469 | -55.13091 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4cbf13b-eaa9-322f-bbe1-6233c298df0d | -12.4907 | -57.19219 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7900d505-2703-33d7-bcfa-af1198190a02 | -9.41452 | -58.32452 | 2025-05-21 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d3e635-1dfc-3f16-b270-6aeb7742e4f5 | -11.67041 | -54.94006 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16339f5e-714d-3402-ad71-2dd10b0aed50 | -15.27042 | -51.46841 | 2025-05-21 05:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 413db9de-274f-3f79-bc36-49f63fa6680a | -12.29487 | -52.49076 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e03f4e55-b4eb-3a1d-ad14-d2aa1396a5d1 | -11.8824 | -56.41493 | 2025-05-21 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 161166e1-e00f-3b4a-b58b-4b42b16e6374 | -13.7159 | -57.47579 | 2025-05-21 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2376aa1f-5390-3c1c-a953-3fc31ceddf01 | -11.08331 | -54.7754 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff6fb966-4568-3fb0-b902-d0fafda5476e | -11.29319 | -53.98232 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dc6020d-8013-3d24-b8cb-d1400cefd423 | -9.60312 | -57.91729 | 2025-05-21 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b923441b-f337-394a-823d-e28a3e460bfe | -10.34525 | -51.69664 | 2025-05-21 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28a93029-0364-32cf-98b4-f01708ed46b8 | -10.06115 | -46.58241 | 2025-05-21 05:04:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aa03bd0-d36b-39b4-977c-aa6233a6ea81 | -9.41914 | -58.31763 | 2025-05-21 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e65b2b5-a6e3-3e57-88e0-6c99b089f89f | -9.41854 | -58.32136 | 2025-05-21 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77bed9b6-5013-3da6-9685-6f8a7be10cc3 | -12.29293 | -52.47736 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b35d24d5-b4bd-3296-b329-9f51b681d03f | -13.61454 | -55.45581 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fea4fc0d-627e-3183-a95a-5911e94d4547 | -15.09569 | -52.83448 | 2025-05-21 05:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95d061bb-4d01-39d9-a1cb-a61652485546 | -13.19623 | -47.26958 | 2025-05-21 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 713e01c0-b3d2-3d85-aaa0-3551b301aa9d | -11.89516 | -49.19394 | 2025-05-21 05:04:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c0c3c7-51ea-339f-99ad-5b05192f696c | -12.50613 | -57.22363 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fdef532-4194-3f6c-89d9-47c96148f9e3 | -12.48951 | -54.91671 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dad9de8-e16d-3d4b-a46b-28dda342d60e | -10.68428 | -57.59235 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1297a4e-4d6a-33d1-8010-8ee23acbc038 | -13.66603 | -53.93876 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fe752eaa-8900-3d3b-bb1d-7de19aed92d6 | -14.01558 | -55.1316 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48ccb834-bae3-32e9-a9be-022e214de126 | -12.29616 | -52.483 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 34e89fda-3dbd-3fe3-8abe-264fa6ae1a6f | -11.07528 | -54.78193 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 23552383-7cbd-3de5-9f5c-6f83fa80c826 | -14.03798 | -50.51875 | 2025-05-21 05:04:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8de85278-b18e-3a5b-900c-44b54204674d | -12.29951 | -52.48629 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a4843bc7-0d02-377c-8072-80532700a05f | -14.01591 | -53.01979 | 2025-05-21 05:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b4f94d1-2c1a-3ad8-8bbc-1bba2365611b | -13.61398 | -55.45959 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2e441c8-17a9-35b1-86cd-b28eb57ea71a | -12.29224 | -52.48243 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3da6266e-1607-3859-af07-80419bf455fb | -12.29096 | -52.49019 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 829c19e0-b298-3870-b463-a4e0051558bf | -12.4747 | -57.18596 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35eb72db-c5e3-3859-b8c2-169e4ed9eeaf | -10.6962 | -59.11016 | 2025-05-21 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2b60af2-ebc3-3dfa-a65c-e25d3a084f27 | -10.30096 | -57.14291 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8b9d6c-280a-3412-a5a2-e0f93e07a67b | -10.36051 | -47.96959 | 2025-05-21 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7714ae7-9325-3fec-813d-55c0854c925c | -12.50006 | -57.21902 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35fe00f9-60fb-3211-913b-5737cb2f137a | -12.29705 | -52.47561 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc1cb211-d67a-305f-b7aa-c9b6f99c2932 | -14.05786 | -53.37982 | 2025-05-21 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b452ff1-7493-300c-92d0-247468901606 | -12.4882 | -54.9157 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 419c2c3d-bfb0-3527-9312-2a70e32df7b0 | -12.33355 | -49.95618 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17368ee8-d8be-34d0-ac94-f605c254b46d | -15.26987 | -51.47272 | 2025-05-21 05:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e35cb8-a2fa-315e-ae44-0dde94e57796 | -14.02891 | -55.13773 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f50fdf8-89bf-30fe-bc30-20dd94f69fca | -12.47801 | -57.18651 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f14a8e8d-8a7f-3dc1-8560-4bb379ea7216 | -12.29546 | -52.48806 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |


[Clique aqui para ver as próximas entradas](README16.md)
