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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa80121d-ad2a-3e17-9f7d-a313126d52e6 | -15.89257 | -46.01673 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eed23e6d-bf31-3b20-8319-f3b73fea0ff0 | -19.15998 | -47.81799 | 2025-05-21 04:17:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d286461-baeb-371f-a97d-236518523e24 | -13.66834 | -53.93767 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4020dab1-93fc-3209-88c4-611ae8ab08f0 | -14.68078 | -45.11446 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c578533b-8089-3832-b21e-c290793603de | -12.6874 | -58.13302 | 2025-05-21 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe15b065-f366-3547-8326-4f31d4e47a40 | -14.02067 | -55.13722 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daa1fd8c-b24d-306b-800f-dcebced0f4eb | -11.2976 | -53.98029 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cedbffc8-c458-3403-a78b-71f9de29dc9a | -14.01663 | -55.12849 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b666fac2-c0f9-3e48-aa1d-3ccf2c9bf125 | -17.59522 | -43.19865 | 2025-05-21 04:17:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5a65c4-faeb-32e0-bc89-eabcc7ff4d67 | -13.80213 | -52.89242 | 2025-05-21 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe8ca0e3-e4a6-31b1-a57b-d4cf4d249f88 | -11.29832 | -53.98219 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a180a4bb-d8dc-3e2e-a036-05451f908e58 | -22.90285 | -46.50249 | 2025-05-21 04:17:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f1b7a17c-6e0d-3e8d-8ac2-ab9418a7ddb5 | -11.08134 | -54.7796 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3336a6fc-56f2-3fca-bd35-afa8be9f2626 | -14.16501 | -45.47266 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a169c4a5-5867-3918-8b51-93e3fd62a980 | -19.27247 | -45.30398 | 2025-05-21 04:17:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cf6e7b3-6e5d-32a5-8f19-250e783c8750 | -14.16719 | -45.48032 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49a41280-7304-3b80-8f52-4fedb7c1ace3 | -12.40861 | -52.15416 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6b52600-f9d4-3fe9-9f7e-4c87b40b1d4f | -13.61152 | -55.4604 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4f53ecf8-efb4-3708-9b99-b94bc77f1a3a | -13.32584 | -45.39843 | 2025-05-21 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e1ca79a-e14f-33b6-9c56-74a28d1a6f56 | -12.40991 | -52.15133 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1fb7442b-eb71-37e3-b653-6175d87bdf4a | -11.40858 | -56.73505 | 2025-05-21 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11cd072d-8244-36eb-8f74-22ea992d4091 | -12.13091 | -54.66214 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffbd213d-f5e4-3659-bb62-34607ad9bdb0 | -14.16227 | -45.46856 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91c01cd2-1eac-30c8-a77a-40ad3ed3e633 | -11.66918 | -54.94035 | 2025-05-21 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a1d992-9504-3c59-825c-3bf350dfaaea | -12.33726 | -49.95573 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 753c6028-4782-3a7c-98a0-dcd975b14b18 | -15.92448 | -49.27344 | 2025-05-21 04:17:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 065cf9f4-3b9e-39bd-aecc-acf4a47ff9f9 | -13.58331 | -47.35772 | 2025-05-21 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9df8fd25-8872-329d-bb35-bb83955c5031 | -11.64766 | -48.10305 | 2025-05-21 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 380f67be-021c-310a-a1be-959d75e3d141 | -23.09931 | -46.21643 | 2025-05-21 04:17:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcec4b00-cbc5-3e66-9793-7182d5694b75 | -12.72606 | -54.97325 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1aee830-e7e6-3c5f-bab9-7371cda9bfc4 | -14.16993 | -45.48443 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4e20972-8fc1-3cc6-8da4-b28158bcec3c | -16.03049 | -43.68462 | 2025-05-21 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab304e7-8880-388f-b8d8-076433596122 | -12.29198 | -52.49222 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 85cad95e-6aa5-3251-ba73-e444a55a8193 | -11.08212 | -54.77555 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5d245fa6-5e14-3e34-afc0-3e1931d3b1bd | -20.95216 | -56.59938 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e329c77f-9770-37cd-a4f4-a4ec5f125987 | -14.69179 | -45.10901 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272b9336-9ae6-34d3-8807-9c26777da182 | -14.16388 | -45.47977 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48329c05-ac0d-32f0-82c4-58b29ef713cb | -11.65137 | -48.1037 | 2025-05-21 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b70f7179-5d0e-3866-80c5-2722d3a6eac5 | -12.48731 | -57.19123 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d2e7bb5-26f0-3549-b990-b99d39fb4196 | -17.11963 | -53.18449 | 2025-05-21 04:17:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d20b0e98-317f-34b3-9ab8-a9f6de700286 | -17.70507 | -47.49641 | 2025-05-21 04:17:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53227e54-70ea-3797-9213-c98e4d0c0161 | -11.08868 | -54.77251 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e899a001-ede6-3df2-a993-3fa5c422ec97 | -12.36673 | -49.97336 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 170b6486-ac25-3669-aef6-c1b764facfbc | -14.23539 | -41.57316 | 2025-05-21 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2b33504-97c4-3afb-b8dd-70204cc4d3fa | -12.30373 | -52.48309 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bdec4a61-3e1e-3781-bda6-e3a23ae78c52 | -16.14114 | -45.9521 | 2025-05-21 04:17:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcb8c582-2d61-3870-a5e2-fb8203fe631e | -15.89314 | -46.01313 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dc6f9f4-7702-3331-906d-8408e4281efe | -12.43043 | -43.72706 | 2025-05-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ac0f12c8-4976-369b-b614-232ec6235807 | -15.27116 | -51.47332 | 2025-05-21 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e001e428-7e44-31b7-93fb-b4ba7d25fb20 | -22.54147 | -48.81371 | 2025-05-21 04:17:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76266fc7-16eb-3116-9580-cd9f082c38d0 | -12.50097 | -57.22388 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51dc135-9cb5-3e6b-945a-911277fcd617 | -11.29691 | -53.984 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce2eab48-0731-391a-a919-3c3e2e2e3cad | -14.70212 | -48.66433 | 2025-05-21 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 496e1578-b0ae-3b2d-97f9-19472e12f0e4 | -12.28815 | -52.48582 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| feaaa65e-5bc0-3051-bdfb-d2e239ee178c | -13.61813 | -55.4573 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 41b898de-cc8f-385b-959a-dbe6c0c5c93c | -18.29888 | -51.85891 | 2025-05-21 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1fcab01-f01e-3abe-aa5b-65b38d49d5d7 | -12.29504 | -52.4758 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee9a74f8-513d-32c5-9be2-9763c3954774 | -17.69684 | -54.09101 | 2025-05-21 04:17:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f5781c1-ebe1-3e11-b2f0-7ad753fbdcfb | -13.51599 | -46.81479 | 2025-05-21 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d558f43e-69a7-3017-a5e5-af15f614a6ed | -14.04711 | -45.50751 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b7ed9a-067c-3570-8e44-123b93087371 | -17.69502 | -54.08884 | 2025-05-21 04:17:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b7119da-a601-3f39-9e33-e85da41c2340 | -19.46119 | -40.05737 | 2025-05-21 04:17:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6bbc178-a290-3c08-8a69-84c6f72cf186 | -13.66436 | -53.93027 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e7139a1-90df-319f-95e9-e7fa058fe4f1 | -11.66834 | -54.94455 | 2025-05-21 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33a2c82-946b-3cba-acb7-ee3c17845ee9 | -11.4088 | -56.73089 | 2025-05-21 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81e7159a-cf51-346f-801a-64784ef64657 | -13.6735 | -53.93892 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6220614-55c2-3571-9b35-c062c4a5cc84 | -13.8007 | -53.3001 | 2025-05-21 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff433942-7c54-3c88-9c63-c97dcbccb3d3 | -12.13017 | -54.66596 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6ce4511-18bb-3ab0-85be-7129871abdf6 | -22.78495 | -43.75612 | 2025-05-21 04:17:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d25c8c89-d350-372d-87ad-9bd3fbdc45f9 | -10.68464 | -57.59752 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc0aece4-09bf-37ac-a6a4-8ae363592347 | -11.07976 | -54.78771 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b8ce2eaa-40b6-3b01-99a3-5ff2713021bf | -12.36264 | -49.97258 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f20debdf-0a0a-3250-91de-c4ac38fb8093 | -14.16606 | -45.48744 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1271c1e0-7094-3789-9ef2-7f1d1af8fc61 | -12.29989 | -52.47671 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5f159af-cdc1-39f8-8684-f342656fbbd2 | -21.88975 | -53.31342 | 2025-05-21 04:17:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3620da14-8336-3bfe-81f6-fd02d5a812b5 | -12.03674 | -54.96553 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90fe00b7-3fae-3792-aba4-ac4f8b55f50f | -15.09625 | -52.83325 | 2025-05-21 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a658ac5-32c8-39b0-8990-0ec82e809558 | -17.10604 | -43.70678 | 2025-05-21 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5831531a-ef3a-3d24-8cd5-6113c9ca5db9 | -12.29786 | -52.48765 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a9e26d3e-4991-377b-9788-229eed7dd2a8 | -23.60182 | -46.35324 | 2025-05-21 04:17:00 | NOAA-21 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af46dae5-e49e-34b8-98ce-3edd4a2f932a | -17.61329 | -44.63728 | 2025-05-21 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef40d48-ac44-3b83-b923-8ae90b2138e9 | -13.32039 | -43.0088 | 2025-05-21 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 38979aad-19a0-3043-a68f-90f6f40232b3 | -13.32528 | -45.40198 | 2025-05-21 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37b1717d-ed19-3df3-83cb-ca5409fc608a | -14.15727 | -45.47868 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cd26fbf-94cb-3744-95aa-025981b5b1ed | -12.12114 | -54.66991 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88c9eb6c-15dc-3da2-8793-2526b4be903b | -16.04648 | -43.80973 | 2025-05-21 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d6a336f-90bf-3960-8eb3-07dc268565b6 | -11.07713 | -54.7705 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f1999d33-3a0e-33f3-b0a7-5c8de0871e9b | -10.68606 | -57.59227 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cfd7dac-5bc0-3ac9-840a-8d7516598e2f | -12.34137 | -49.95645 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ed5aaec-a7a0-3bc7-afdb-e6aca6b3afaf | -11.29904 | -53.9785 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4a15b4e-1509-3a07-b6bb-e60c2764e153 | -14.03936 | -45.51351 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fed9cbc7-e967-3f77-ae32-65d8559b82e6 | -15.05009 | -45.66502 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9894d10c-6147-3642-a175-97edb04092b4 | -14.02627 | -55.13829 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6345162d-2147-3692-8a26-dd004a4f11f0 | -10.6779 | -57.59721 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ecf5c2-e5cd-32b9-a925-93b35d777ea8 | -14.03871 | -50.5152 | 2025-05-21 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13ad7c4d-d6e2-3173-a113-178b84ed1c77 | -14.16231 | -50.50581 | 2025-05-21 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9c902db-6a01-3dc8-a397-7be5e99fbeb0 | -12.48643 | -57.1925 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08947425-141c-3b90-a762-2d4323fe7656 | -13.19782 | -47.26963 | 2025-05-21 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ef4e955-0e4b-3a1a-b074-98721b22df11 | -12.83844 | -47.39729 | 2025-05-21 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 593ee275-8d58-32c5-8c00-25b65d00055a | -12.13164 | -54.65834 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
