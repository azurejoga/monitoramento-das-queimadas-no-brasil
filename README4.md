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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 205aff5f-06c8-3217-b10e-00f6621e2695 | -21.25778 | -50.29832 | 2025-01-11 04:04:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3dcdf191-8052-3372-b222-d9632aa36334 | -20.87777 | -49.87313 | 2025-01-11 04:04:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 454ccefe-707a-3c39-b978-f02b76435469 | -22.47287 | -48.36818 | 2025-01-11 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6a1a446-da43-3369-a473-cf21d2bb6f19 | -23.45748 | -47.43332 | 2025-01-11 04:04:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 372aa7e5-805b-33bf-9dfc-77f72b6e9036 | -19.66139 | -54.41501 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b3ebde7-2dc8-3332-ab4d-77df7769770f | -22.01186 | -49.1166 | 2025-01-11 04:04:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 815e62f4-edb1-3efa-9b24-446c3b1d0e42 | -23.33718 | -46.77403 | 2025-01-11 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0cfbfd53-25af-3f72-8b32-5188b2ee1447 | -19.69342 | -58.03315 | 2025-01-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4236d007-10c3-3e76-9c1c-c6d1818e73c5 | -22.73962 | -42.96042 | 2025-01-11 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 76461aba-d342-3719-887b-3d33b1a48782 | -20.37559 | -45.6036 | 2025-01-11 04:04:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d317cd8-a166-3aba-b8d9-62c56a66a68a | -20.40616 | -49.84171 | 2025-01-11 04:04:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa44ebe5-54ab-37fe-b8dd-55ed385936dc | -30.83166 | -55.3996 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 927af313-aa99-3858-bac4-6797893df3fc | -30.82899 | -55.39212 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3a9cec4e-2831-3796-a5ef-d7e38225cdf6 | -30.82344 | -55.39007 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b56f62ff-aa3b-33ab-8650-3d798d416399 | -30.83231 | -55.40009 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| cd2d420d-cdbf-34dc-a717-c04a429b215f | -30.38341 | -56.1645 | 2025-01-11 04:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| af57a9db-d9fe-3862-a783-bd8fcbe991df | -30.82829 | -55.39163 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 79468db3-109b-377e-8d47-0a32d7ea8dce | -30.37495 | -56.1539 | 2025-01-11 04:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| c0830678-feba-3f9e-98c8-4990a5b95a2a | -30.82413 | -55.39059 | 2025-01-11 04:06:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| f9809634-57b1-3759-99b1-8f9c68389073 | -29.5464 | -54.33503 | 2025-01-11 04:06:00 | NOAA-20 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 510482dd-9858-36de-b0a6-20ba229e5db3 | -30.38253 | -56.16821 | 2025-01-11 04:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 4643d6df-4157-31f8-b346-10b69687bad9 | -30.38004 | -56.15561 | 2025-01-11 04:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 4bed019b-7d03-3a0f-b760-878041d13b22 | -30.38427 | -56.16093 | 2025-01-11 04:06:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 5d4ef6da-9172-3a12-9ac4-64d71c2dfcf5 | -1.71155 | -54.49923 | 2025-01-11 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c48023c-243a-39db-b813-cce2b4d4a2a1 | 3.31551 | -60.0001 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c899e8e2-8a0b-35ae-9590-602d649c35fb | 3.3775 | -60.26255 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c2da36fe-3493-359e-bc35-54ca96aa923d | 3.37704 | -60.26649 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c2c6b04-6eab-33ff-9b72-08185bd546c0 | -2.91844 | -40.42527 | 2025-01-11 04:50:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4e8b3784-3f14-3ed9-8ec7-12e158d008bc | -1.53529 | -53.51344 | 2025-01-11 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2f6b89-e4b3-3880-a1be-47c3f91afc8b | 3.92418 | -59.76247 | 2025-01-11 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d19a61-627d-3080-8a73-a49e9bc168b9 | 3.31447 | -59.99318 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c53488b-56de-330f-9791-dbe9b352ccbd | 3.37598 | -60.25908 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27eea560-f220-3818-b7d6-a4f68c679b5f | -2.91771 | -40.43007 | 2025-01-11 04:50:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3b23cb1a-da42-379d-b872-502f6b16177d | -3.86439 | -40.45724 | 2025-01-11 04:50:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d710335-96ee-3d25-9167-83ce091947f4 | -1.67394 | -54.34641 | 2025-01-11 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b019279c-14f1-37b1-bb5c-bf636a1ead96 | 3.92367 | -59.75901 | 2025-01-11 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d167535-f3b0-3111-a0d2-af0af0edf624 | -1.88107 | -48.71303 | 2025-01-11 04:50:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 141015f8-fefc-3a86-bfb7-c31e40f22f10 | -2.65926 | -48.79043 | 2025-01-11 04:50:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5dc7701-d77e-3a9f-b394-8036e3be36b5 | 3.31499 | -59.99664 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8219eff4-32aa-30fd-9f51-b2d477ebe9ed | 3.37694 | -60.25885 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ce0b3c2-7bce-3ef4-b9f2-acf230cf98f3 | 3.37652 | -60.26279 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b403a0e3-205b-393e-97e5-9d190c831aab | 3.31002 | -60.00081 | 2025-01-11 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38665e35-446f-3b7a-b18f-5f4f06b35bdf | -2.81483 | -52.61796 | 2025-01-11 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 800b4c81-5407-3b75-84e6-07296ac4f438 | -2.84094 | -54.07538 | 2025-01-11 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f187f3cf-ce71-32bb-8072-173b95d236ff | -3.15542 | -53.75456 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffaaadc5-47ca-3742-9c4a-243fa2654bf9 | -9.12815 | -43.11109 | 2025-01-11 04:53:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bfd15e35-7d07-3932-981a-d6fcd21ea9b1 | -3.86927 | -54.23318 | 2025-01-11 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87e50a36-261c-3245-8cee-0ea74898b66a | -3.85808 | -54.08243 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5d38053-c2da-3df5-bf93-770e4cceacdc | -3.86987 | -54.22942 | 2025-01-11 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34945da1-22fb-3645-934e-d752ca861206 | -3.72098 | -53.7532 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed898ad4-575c-3a10-9840-69b60c72ad61 | -3.88317 | -54.21227 | 2025-01-11 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a90d6f3-2cc5-341f-a65c-93fad93297bc | -3.46374 | -53.95684 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 657b3488-6fd3-3722-b38d-aad8d2c96f91 | -3.73797 | -53.73358 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 820f95e0-7eac-3dd3-a5a1-dd63701ffe2e | -3.46316 | -53.96052 | 2025-01-11 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9632be72-865e-370b-b20c-eca42d844acf | -2.60275 | -54.18299 | 2025-01-11 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fb4105-a129-3fa6-b5e1-5c8c493a9e70 | -2.86052 | -52.56469 | 2025-01-11 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f2c1ee4-cc58-3ebb-b544-9446287dcb53 | -2.79768 | -54.16982 | 2025-01-11 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d34145e-f65a-37e8-81f7-7e045ed27cfe | -6.81443 | -48.84287 | 2025-01-11 04:53:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14179325-7104-31ea-965b-0f3ed2dd1904 | -2.84153 | -54.07161 | 2025-01-11 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ba7fccb-93ab-3a77-9ab3-1d0c18670f96 | -2.67033 | -54.26399 | 2025-01-11 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ea2c7f-66c0-3675-a504-48c10d33208d | -3.87271 | -54.23372 | 2025-01-11 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e373bf12-137f-39ea-918f-e48acb052e75 | -20.76468 | -46.76971 | 2025-01-11 04:55:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fca3a68b-51cc-3286-9b7d-5f5aea3cdb12 | -19.49172 | -55.33137 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 674f9ce7-793b-31c2-81e5-be8ed72412d1 | -17.59068 | -46.56433 | 2025-01-11 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90944ed0-1dd0-3bcf-808b-5115340bfadc | -21.56262 | -54.19835 | 2025-01-11 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3661d7eb-903e-3598-b14a-b83e2a394d19 | -19.15957 | -54.83632 | 2025-01-11 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a9f0386-fe2c-3fe9-9721-2ec6f2c21053 | -10.71261 | -59.23258 | 2025-01-11 04:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a81889ab-1937-3e9a-9952-3211a2937060 | -16.21365 | -59.08171 | 2025-01-11 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b7fd9bce-7d8c-31cf-8d7a-729bd1eb63ab | -19.70069 | -58.01823 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b7bfe926-5c5c-3902-9ca2-f261277ebe13 | -19.49116 | -55.33502 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1cf4e3c-8c6e-3013-9536-65a2a1f828ba | -22.19649 | -56.26525 | 2025-01-11 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e550296-35c6-353a-8c34-cc04e93dcae0 | -22.01114 | -49.11896 | 2025-01-11 04:55:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0ed520c-f71f-3818-b28f-499bef10c643 | -23.68777 | -51.69252 | 2025-01-11 04:55:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3653edeb-e731-3bb0-8014-078c27f9ec6b | -19.70824 | -58.01554 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f4c057d3-48a9-3686-9fbb-2b7a6d5ff2a9 | -20.87796 | -49.87206 | 2025-01-11 04:55:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 92ed710d-f2e8-33b3-b127-ee701942f5f7 | -21.29048 | -48.9937 | 2025-01-11 04:55:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d39c23cb-25f9-34f2-aa07-c4d753f09adf | -22.01276 | -49.11488 | 2025-01-11 04:55:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e005bb14-2cd9-3ad4-acd2-3b0d9f5ba7d7 | -22.01222 | -49.1199 | 2025-01-11 04:55:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6596b957-3091-3964-8ed3-d6403e546e7f | -16.21301 | -59.0833 | 2025-01-11 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 97daa6ee-2a91-35db-afa5-4cf61e94cd42 | -22.01627 | -49.11448 | 2025-01-11 04:55:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90b0fb15-fade-3f8c-9ffc-2f4b3dc1b687 | -21.56547 | -54.20288 | 2025-01-11 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2bf5f3f2-d959-3fc6-8e70-6fa986f2930a | -19.69179 | -58.02888 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0e5e141d-a742-3915-986e-4172b2b83789 | -19.69726 | -58.01759 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ede56b1d-01e5-3691-a1ce-1a1cea8b9076 | -19.69455 | -58.03351 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 70eb9585-7a4c-3e49-b655-78a31837645e | -21.26182 | -50.29658 | 2025-01-11 04:55:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e48c299-c034-3c75-af14-d0fb715c8e70 | -19.49228 | -55.32772 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 59dff54f-1d51-3841-9757-887f4193e65b | -19.80769 | -53.82201 | 2025-01-11 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88b7db74-074a-31cc-8306-435b0d299d84 | -21.17616 | -49.22292 | 2025-01-11 04:55:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 95d499c9-3135-34d2-850b-9424a520aee0 | -22.01569 | -49.1195 | 2025-01-11 04:55:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42b12cee-207e-3e6d-8d52-0e8b8aec41b0 | -19.49059 | -55.33867 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e8284a0f-cd2e-3c8c-af8a-2dd9602d0204 | -19.69658 | -58.02158 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 2dcdfe5b-731e-3f69-9b67-2d587fc9d4c2 | -19.34423 | -54.16705 | 2025-01-11 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd951900-5c57-3f52-a148-7c3d085c923a | -19.30489 | -48.38929 | 2025-01-11 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 970afc4d-cc3c-3ff5-9e6d-b44fe354d744 | -19.48784 | -55.33445 | 2025-01-11 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dd22884d-4cc2-325f-abdb-399ee1c6fa83 | -19.70075 | -58.03877 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8b2fbd83-757f-3ed8-a8ff-711eab6cec35 | -22.53853 | -48.81405 | 2025-01-11 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f20fbc64-4e61-37a9-a199-8f5c00fddb1d | -19.66874 | -54.40923 | 2025-01-11 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cedf63ec-5972-3407-b930-2678e46d7cc0 | -19.16233 | -54.84055 | 2025-01-11 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7130c417-626d-3262-8656-ee9ea9942bf4 | -19.70757 | -58.01953 | 2025-01-11 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ae8f38be-ceb2-304d-b13a-4188d5b047ca | -17.59035 | -46.56741 | 2025-01-11 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
