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
| 3f4dfb3b-412c-3a18-822f-5bc05ce84529 | -32.667 | -52.4673 | 2026-02-12 00:00:00 | GOES-19 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 355.0 |
| 392166f5-fbfc-309a-94e5-ebed5141a7ea | -32.6429 | -52.4748 | 2026-02-12 00:00:00 | GOES-19 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 160.3 |
| 1b705b64-0c63-385b-9f41-cb773ef5b41f | -32.642 | -52.4999 | 2026-02-12 00:00:00 | GOES-19 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 117.2 |
| eae909b5-04b7-32a3-976f-10daca81b0df | -32.6911 | -52.4598 | 2026-02-12 00:00:00 | GOES-19 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 56.9 |
| 496d9b74-e50e-3706-8644-b6f8272e9f25 | -32.668 | -52.4422 | 2026-02-12 00:00:00 | GOES-19 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 57.2 |
| 7e0aee41-3ce5-3055-9f49-ce9368a84b7b | -32.6661 | -52.4924 | 2026-02-12 00:00:00 | GOES-19 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 237.0 |
| c0b5aae6-681e-342a-a454-d6981f405931 | 1.3403 | -60.0461 | 2026-02-12 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 25c2d66f-df66-3ccf-9e48-a70d5920ba84 | -32.65618 | -52.46406 | 2026-02-12 00:22:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 204.1 |
| 0e6c0d14-70fc-361c-9363-f2eb8e54ac48 | -32.66005 | -52.49319 | 2026-02-12 00:22:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 185.9 |
| 6895e5e9-c9c4-363b-9b23-e210692bdee0 | -32.42052 | -52.41192 | 2026-02-12 00:22:00 | TERRA_M-M | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 20.5 |
| cbb1a0ae-4430-346e-b1be-fcf76fb7cea7 | -32.65809 | -52.46915 | 2026-02-12 00:22:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 288.1 |
| c8da3a56-1667-310a-9042-8d5206c64a13 | -32.65797 | -52.48809 | 2026-02-12 00:22:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 323.3 |
| 2e214caa-a9cc-3955-a6f1-4057ad73f71b | -18.97437 | -52.91984 | 2026-02-12 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7b7816fb-2ab5-388a-9d14-42cbd1f313f4 | -18.97609 | -52.9347 | 2026-02-12 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ee0d8a9d-370b-335f-873e-036ce93500a7 | -25.04667 | -49.24223 | 2026-02-12 00:24:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| a719c1f1-41f5-3192-b748-e52bee0586aa | -24.67152 | -51.16963 | 2026-02-12 00:24:00 | TERRA_M-M | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 20b2b743-6cf2-3e3f-a399-2150a90992ff | -3.53142 | -48.88478 | 2026-02-12 00:28:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5379de3f-b5b3-37f3-bf10-dff3f1074277 | 1.3586 | -60.027 | 2026-02-12 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 918ea2c6-b688-3a84-bf60-2021e34e48c3 | 1.3586 | -60.046 | 2026-02-12 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 66a83eb7-0d10-334b-8128-f1ecb748532b | 1.3403 | -60.0461 | 2026-02-12 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c107bc7e-1351-3235-9f9d-c43006b22b24 | 4.2617 | -60.5903 | 2026-02-12 00:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a3adfdfe-b324-3ea1-a58a-4f3d96d9af5e | 1.34519 | -60.04353 | 2026-02-12 00:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.8 |
| bc38c3a9-caa8-3b29-adca-143a81be2024 | 1.34088 | -60.0363 | 2026-02-12 00:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b3968e69-4e56-3d1c-a4c8-cd60f099c786 | 1.34876 | -60.0191 | 2026-02-12 00:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 7f5af340-1fbd-3d07-a67a-5ca4269694e5 | 4.24976 | -60.61365 | 2026-02-12 00:32:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 331e7d8e-c1ae-3750-9110-a21bd1b096bf | 4.25343 | -60.58887 | 2026-02-12 00:32:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| dcd9417a-bb90-32f4-85f1-ea24ebbf9417 | 4.25809 | -60.59506 | 2026-02-12 00:32:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f8ba2fe8-bca4-3939-b411-1032a0d8907e | 4.2617 | -60.5903 | 2026-02-12 00:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0c4cc1c8-b6cb-31e8-ab5b-7eb76f1a7cc0 | 1.3586 | -60.046 | 2026-02-12 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1e911d3c-6df2-31ab-a7de-d7ca87449952 | -25.196 | -52.7255 | 2026-02-12 00:50:00 | GOES-19 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 6700bc4e-2a32-3cc0-b4a2-16dd4860f546 | 4.2617 | -60.5903 | 2026-02-12 00:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 920ee4e0-83df-3519-9c6b-31fc2b9cab03 | -25.1967 | -52.7026 | 2026-02-12 01:00:00 | GOES-19 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| 0a2bf1ff-3bf5-3979-97d0-cf3a67ef62da | 4.2617 | -60.5903 | 2026-02-12 01:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1779ff04-79ec-341a-9c5c-92a5a4f7318a | -25.196 | -52.7255 | 2026-02-12 01:00:00 | GOES-19 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| 2081e582-196a-39a7-8739-cd2f31e94e3a | 4.2617 | -60.5903 | 2026-02-12 01:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 71a55852-ce4a-3749-b7ec-a17bc969bda4 | -25.196 | -52.7255 | 2026-02-12 01:10:00 | GOES-19 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| d2f42fea-0c8c-38cb-9ce7-be7026fda3ee | -10.11972 | -42.16982 | 2026-02-12 03:19:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9e1c8623-83e3-39f7-99b3-e3e5793a1283 | -12.12278 | -38.6546 | 2026-02-12 03:19:00 | NOAA-20 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73096af8-de46-396d-88df-59c6dee7ccd0 | -9.39508 | -40.60611 | 2026-02-12 03:19:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b60d295-ee99-32f2-9fd3-bbbd2c1d5585 | -12.12288 | -38.65281 | 2026-02-12 03:19:00 | NOAA-20 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5ed1ddfa-a173-3dbb-9d74-2eee04b26593 | -9.39589 | -40.60175 | 2026-02-12 03:19:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf17b9a5-850b-31a9-ad7e-454469c75386 | -15.61695 | -39.82823 | 2026-02-12 03:21:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 01328ed8-91c9-370c-8537-e683f0f37c6a | -15.62198 | -39.82933 | 2026-02-12 03:21:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 530f14e0-64f6-3755-ac87-be537618b75f | -15.62258 | -39.82633 | 2026-02-12 03:21:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ae9c25df-46fb-37ac-8917-1eb9e7c11ca5 | -6.34981 | -46.18846 | 2026-02-12 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c3e7fd-4e34-32db-8201-7d6649ad5199 | -5.88261 | -39.59784 | 2026-02-12 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d66b84f4-55e8-30fd-9b6e-c9dc1d7b7aca | -6.34845 | -46.19108 | 2026-02-12 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88e64f58-61c1-3f04-a179-1d92c00bc9c5 | -5.50783 | -39.3859 | 2026-02-12 04:08:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c32a12d4-cc32-3cc0-a3fc-3ace70c14be5 | -10.12294 | -42.166 | 2026-02-12 04:10:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6f1f1fc4-e6db-31d0-978e-90ef5010a17c | -14.48244 | -40.1648 | 2026-02-12 04:10:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9af7e347-f44c-3aba-b8fb-e06512baf83f | -12.12497 | -38.65465 | 2026-02-12 04:10:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4231108-5ad0-3484-a520-54c26b7977e9 | -9.32375 | -41.08841 | 2026-02-12 04:10:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f376be0-b634-3348-bc8b-164061e4018d | -15.1756 | -40.53634 | 2026-02-12 04:10:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3580b0dd-719c-3dfd-80de-8d1b2c6cfd4d | -9.24098 | -40.51131 | 2026-02-12 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87341e43-ce78-3571-84f0-1c0412f164f3 | -14.48114 | -40.16604 | 2026-02-12 04:10:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bce7de95-b4cd-3d63-bc86-cc6331d7a3b6 | -9.24042 | -40.51501 | 2026-02-12 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f9a22f1-f49d-3905-a15d-e4831c4d97f5 | -12.12564 | -38.64979 | 2026-02-12 04:10:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cc59067-e969-3629-9c84-2cb90a6eac21 | -10.11909 | -42.16896 | 2026-02-12 04:10:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fc3fda1-c36a-30f2-9124-a954511e6b9e | -10.11964 | -42.16548 | 2026-02-12 04:10:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c3c1732e-9537-3c2a-ae88-41c223f6a643 | -15.62255 | -39.82603 | 2026-02-12 04:10:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e65bba4c-d2ed-35bc-b0d8-8dc42c632302 | -12.67753 | -39.42668 | 2026-02-12 04:10:00 | NOAA-21 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 92ed10c1-37b6-34dc-928d-2dc2077954f4 | -9.39823 | -40.60292 | 2026-02-12 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38c50002-b2cf-3c67-86e6-671890b1d5ca | -9.15933 | -45.01501 | 2026-02-12 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd6fe471-419b-3a5a-9c23-8fe3970eb921 | -11.81778 | -40.90755 | 2026-02-12 04:10:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee5f990c-9184-339a-91c1-839bd375b732 | -9.15871 | -45.01517 | 2026-02-12 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98261f00-719d-34f4-83f5-61f28ad6acd3 | -9.67819 | -47.89541 | 2026-02-12 04:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8355c60-f14a-3f43-89f1-e89df948e48c | -9.29636 | -40.42119 | 2026-02-12 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cc111e0-c950-3839-87b7-e5b3ed139c92 | -16.59313 | -42.67549 | 2026-02-12 04:12:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08499e7f-db69-3ed4-8f65-5fb5350b400f | -17.31383 | -44.92941 | 2026-02-12 04:12:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae92688f-5eaf-355c-934b-7b782c9a571f | -18.61629 | -39.7825 | 2026-02-12 04:12:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 58236f71-71b8-3c79-8353-cf0ec7e03ba0 | -28.62133 | -50.43363 | 2026-02-12 04:14:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2d148f81-dedc-3cc7-90f0-d657a18b47a9 | -25.18587 | -50.70273 | 2026-02-12 04:14:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6b8b0faa-3d67-307e-a892-1cc268b83382 | -20.55841 | -54.65759 | 2026-02-12 04:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ff076c5-ae96-3005-ae25-ab73af80cc62 | -28.62489 | -50.43445 | 2026-02-12 04:14:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3fc786eb-6fb4-35f6-8f46-3f9ef534768a | -27.10079 | -50.52971 | 2026-02-12 04:14:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 756586f1-a0cb-3139-bdcf-3a5ff0c75d28 | -21.17493 | -56.50541 | 2026-02-12 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cde61964-03d0-3d41-8bec-bad3e8f3f50c | -22.69461 | -53.94832 | 2026-02-12 04:14:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 165123ac-c440-3cda-8df7-144ca6f1200a | -25.04839 | -49.24437 | 2026-02-12 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08f59d58-8aa5-36f0-bfc5-46d82f5cc11d | -25.04919 | -49.23989 | 2026-02-12 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| efec7029-f270-3530-905d-3c4905eb2638 | -20.5592 | -54.65718 | 2026-02-12 04:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddf5bc50-f2f9-3346-9a84-9eb538d4f92e | -21.1759 | -56.50117 | 2026-02-12 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 913e74e2-51d6-36de-a1fe-88dfbb657e0c | -20.55918 | -54.65409 | 2026-02-12 04:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f92eb13-234c-34b4-bc34-7626a0b0ff57 | -25.18478 | -50.7045 | 2026-02-12 04:14:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c527998-5b6e-3b02-8f40-d393c1d74c9f | -25.05272 | -49.2407 | 2026-02-12 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 00129c07-d36d-350c-b726-449f12c02029 | -29.21133 | -50.84362 | 2026-02-12 04:16:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f150bae7-2b4c-392b-80d7-d997cf973b11 | -28.85257 | -50.58036 | 2026-02-12 04:16:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3abab61-0c31-3682-b21b-eebf35bd1cc8 | -31.06403 | -52.5941 | 2026-02-12 04:16:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 46ec7bd0-f2d8-3697-a5e2-40f1c532d8f1 | -29.68505 | -51.08335 | 2026-02-12 04:16:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 8ed48e83-0cf4-3c91-ab13-94d6274610d5 | -30.10171 | -51.8883 | 2026-02-12 04:16:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| 61fbb93d-8351-3a8c-9513-57d273cc3604 | -30.2958 | -50.92437 | 2026-02-12 04:16:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 2d0738d5-7a98-38a1-b207-f87a38ab510b | -29.1115 | -51.47457 | 2026-02-12 04:16:00 | NOAA-21 | PINTO BANDEIRA | RIO GRANDE DO SUL | Brasil | 4314548 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e914cc3-9ed7-36e9-aea1-6b2636cb7366 | -30.62459 | -52.32981 | 2026-02-12 04:16:00 | NOAA-21 | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| f2307f9a-a680-3c14-8c87-bc0a7cf8169c | -6.34672 | -46.19061 | 2026-02-12 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa241cc3-c50a-3f4a-8a9f-65cd0df1d220 | -6.35014 | -46.19112 | 2026-02-12 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 343de51d-2864-3e51-a9cf-e69f1ffdb7fc | -7.92657 | -42.88735 | 2026-02-12 04:38:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 227c6a23-c5b4-39d1-84ab-bb440ba911c3 | -6.35071 | -46.18743 | 2026-02-12 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70d88922-cc09-3102-a5b9-2b1efba7001a | -9.67589 | -47.89467 | 2026-02-12 04:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92560ec6-0674-3335-8ea3-48e29c1f1de9 | -10.12028 | -42.16619 | 2026-02-12 04:40:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 385ab8f7-339f-31a2-854b-d0c557ec6385 | -9.15884 | -45.01789 | 2026-02-12 04:40:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ac76918-0d2b-3a75-927d-003c0f6457f6 | -9.23457 | -53.20597 | 2026-02-12 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README2.md)
