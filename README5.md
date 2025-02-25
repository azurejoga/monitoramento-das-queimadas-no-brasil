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
| 98c48876-3cf9-30d9-85c0-fa4d7d93b7e2 | 2.7432 | -61.2624 | 2025-02-25 05:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c140401e-36f9-3da5-9f78-dbfc8c305f26 | 2.7249 | -61.2627 | 2025-02-25 05:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a511c5f5-e91c-3c8d-96c4-09a9fb2953e2 | 2.7249 | -61.2816 | 2025-02-25 05:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| bb8245b2-e946-3136-ab4e-e745aff59845 | 2.7431 | -61.2813 | 2025-02-25 05:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a4378769-35a5-31d2-9ab2-b3815b7588b7 | 2.7249 | -61.2816 | 2025-02-25 05:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.9 |
| a9614ec5-a8cc-32a0-9ed9-b272cc238eeb | 2.7249 | -61.2816 | 2025-02-25 05:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 67fd84fd-8135-329c-8d42-e9507669195b | 2.10751 | -61.82633 | 2025-02-25 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8df6f5cb-de52-354f-9461-57b28be0b80a | 2.73887 | -61.27088 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c318db9-b362-3e46-9210-7d6c29bb0518 | 2.7329 | -61.28076 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b583f24a-812a-37c4-901b-077a5029c516 | 2.72854 | -61.27702 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cc0ee22-31bd-3ed4-b9a8-ddbb7fe1cb32 | 3.03322 | -60.20942 | 2025-02-25 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b416bd83-7a2c-3930-a1e7-294c1a955e35 | 4.32956 | -60.59525 | 2025-02-25 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6982269-a786-33e1-84ba-6ad6d1ebb5d2 | 2.73657 | -61.28016 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d810dda-c636-31ca-b45b-a95018d236d1 | 2.7352 | -61.27147 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1d20312a-be43-3696-b963-dfba13d23d69 | 3.81442 | -59.62875 | 2025-02-25 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35e2066d-8117-3f36-b6b9-43a27ce4912a | 2.73956 | -61.27522 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4debba09-cac0-3d7b-bc7f-aefab8c591c5 | 4.52178 | -60.99212 | 2025-02-25 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74df6377-6083-3ba1-afef-746e69e74ca7 | 3.03244 | -60.20447 | 2025-02-25 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea70f7b1-4c2b-35f6-8c62-2dab43f33021 | 3.01605 | -60.20203 | 2025-02-25 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f413fb83-76f3-3880-a48e-150f39d3913e | 2.73221 | -61.27642 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d5ecb847-7b39-34f8-8394-655604565c56 | 2.73589 | -61.27581 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4582d551-f531-34ac-b38e-cfb35476cf0c | 3.02385 | -60.20077 | 2025-02-25 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34fa12a1-5835-37b4-bf66-46b281876b1b | 2.98613 | -60.86903 | 2025-02-25 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7750ba2b-abf1-351f-a2ed-a2f48599e62e | 2.73152 | -61.27207 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fc6353b9-b754-33b3-95c1-815d7ba2ca45 | 3.81787 | -59.62461 | 2025-02-25 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5e3eb88-145a-3924-bc4c-a4e2abc0856e | 2.74025 | -61.27956 | 2025-02-25 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b249825-43f2-33cb-860e-b54797d109e9 | 1.33229 | -60.72374 | 2025-02-25 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3414ef7-4af4-3f0a-99f2-680ca8fc3696 | 2.73573 | -61.27419 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2aac855-cf9e-3cbe-af61-820df653757a | 2.73507 | -61.27035 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8914828-3d8e-34c7-a26b-cd5a9a99166c | 2.73639 | -61.27802 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfa113e0-b276-3368-9ae3-a1379e288709 | 2.73008 | -61.2752 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81122a5e-5a8b-3a92-97c4-eaad97637749 | 2.7343 | -61.27696 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33c3dd23-48a3-32d1-9718-d087e2c4a9e5 | 2.73304 | -61.26926 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a980be8f-54b4-3897-8823-93964da49df8 | 2.73074 | -61.27905 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ce974af-6023-3eb2-8a37-53856cdd353a | 2.73367 | -61.27312 | 2025-02-25 06:12:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbc5f352-d8e7-3574-9018-516d3036954b | -7.54289 | -43.86625 | 2025-02-25 12:38:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dc84b4cb-e076-3536-a192-3df31f4ce221 | -10.87129 | -44.78463 | 2025-02-25 12:40:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 20433437-84bf-31fe-a470-b3b1a393c3ed | -10.87696 | -44.79184 | 2025-02-25 12:40:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e0fa6897-e898-395a-b6f0-abb5a083562e | -12.80153 | -44.84484 | 2025-02-25 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9523d06c-584f-33c9-8ee7-96e8d79b8301 | -12.84218 | -47.85576 | 2025-02-25 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f680fae-e984-3582-877e-fd05a13cdc45 | -10.87862 | -44.77878 | 2025-02-25 12:40:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 71b1db0f-be30-3946-ae9c-233d431cd570 | -18.86032 | -41.94673 | 2025-02-25 12:40:00 | TERRA_M-T | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| d94c6c95-8018-342d-afb9-f88b8d21ee53 | -12.18278 | -44.05331 | 2025-02-25 12:40:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 755a70fe-46ed-30c3-b087-a35d149a2e0d | -10.10976 | -42.21342 | 2025-02-25 12:40:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| e2374955-adb3-33df-a088-34e608dc0564 | -15.05276 | -45.16237 | 2025-02-25 12:40:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c97a7b31-aa47-3e28-8cf5-4b474b6124b6 | -22.83624 | -46.32689 | 2025-02-25 12:42:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 532b7968-2a92-3f56-929c-96c59d9789c2 | -22.92538 | -46.63765 | 2025-02-25 12:42:00 | TERRA_M-T | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| fe61af5a-43b2-3bd8-ab5e-424161e54817 | -23.35884 | -47.51488 | 2025-02-25 12:42:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 4e52dca5-6509-348e-a69f-33de27abad55 | -22.8511 | -50.62824 | 2025-02-25 12:42:00 | TERRA_M-T | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 0bf182e3-81c1-33bf-8f89-6c024734cb9e | -22.83921 | -49.29372 | 2025-02-25 12:42:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0c054f94-e7c8-34c1-8545-2aa78ea51479 | -23.08657 | -49.77784 | 2025-02-25 12:42:00 | TERRA_M-T | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b1ef0b3d-f1aa-3fd2-8bf0-9f30cac23570 | -22.71235 | -46.89203 | 2025-02-25 12:42:00 | TERRA_M-T | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 2ad1da26-76a3-3fea-b3b8-6caab119cb0c | -23.40751 | -46.82625 | 2025-02-25 12:42:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 65d1d2c7-9ed4-3272-9c45-4ccb788fed35 | -20.46074 | -45.44217 | 2025-02-25 12:42:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 31f278f5-0593-3447-8f6f-027100381bd8 | -22.8485 | -49.29508 | 2025-02-25 12:42:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e39b3d8-5552-34f1-a963-91877d025d18 | -26.22325 | -51.59676 | 2025-02-25 12:42:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 953a475c-dff3-3312-9da4-4cc2b8d74902 | -28.26316 | -50.87163 | 2025-02-25 12:44:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 2a0a6e74-2f0b-3c84-8f3b-2690bd5619f7 | -29.65525 | -51.86809 | 2025-02-25 12:44:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| daca6802-c29a-3f57-b2d7-8ecdf2142f9b | -12.5585 | -44.7378 | 2025-02-25 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 7fb27215-2bd1-3166-8c59-9ee22c98b3fa | -12.5585 | -44.7378 | 2025-02-25 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| da438116-8d8b-3e54-af6c-0afced6daed7 | -26.0283 | -49.4848 | 2025-02-25 14:00:00 | GOES-16 | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| 3e729c71-b15b-3f7d-895f-e33c4c3e5526 | -12.5585 | -44.7378 | 2025-02-25 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 16242056-0a92-3cab-9b63-970b3d27c72e | 3.0194 | -60.1968 | 2025-02-25 14:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9db41c37-e349-3ab1-a3e1-393cdaba3f34 | -12.5585 | -44.7378 | 2025-02-25 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 9eddb183-1839-32ff-a68d-7241dfff40c3 | 3.0194 | -60.1968 | 2025-02-25 14:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 89.9 |


