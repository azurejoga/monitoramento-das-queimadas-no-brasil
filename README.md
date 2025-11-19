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
| e044f9fb-9cce-35af-a4e3-d66206705e1c | -21.42306 | -47.68993 | 2025-11-19 00:28:00 | TERRA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1fd3380b-fae7-321f-9aac-8ca1570b6dbf | -21.23864 | -49.30444 | 2025-11-19 00:28:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 45518072-28de-36e5-98d0-2b6a06fb06ea | -21.42176 | -47.6803 | 2025-11-19 00:28:00 | TERRA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 98b112fc-b3f8-33b3-844d-a186a2a0ae7e | -18.91446 | -47.17757 | 2025-11-19 00:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 59a96406-c535-3584-b359-00d668b74374 | -11.62427 | -44.98671 | 2025-11-19 00:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d8070a6-f54e-3128-a6af-1bb081325e05 | -12.31119 | -47.90607 | 2025-11-19 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd077208-b07c-3ed0-bf4a-995aa066a083 | -8.93559 | -49.85461 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2b2184e1-d5e2-3d3a-92cc-6631f4c8d0f9 | -12.4581 | -54.43971 | 2025-11-19 00:32:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c524220c-0acf-3c8b-96d1-9d8d8a27f893 | -12.15925 | -43.97892 | 2025-11-19 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 22e3a068-2ae3-384a-99db-056495eccd5f | -12.76617 | -45.4316 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c00f84f2-dd82-3b30-a367-0628e6aa31cf | -11.5119 | -44.99748 | 2025-11-19 00:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1d554adf-dd6e-322a-a201-1bb1b03d96a2 | -12.3557 | -43.98131 | 2025-11-19 00:32:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| fde7d288-8843-3f5e-9367-18cf965ae46b | -11.01415 | -49.03401 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1acaae9e-4b6c-3510-8ebf-df3944b2783a | -9.38332 | -48.4403 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c2a9575c-ffaa-31ed-8e98-6de393759dff | -10.5456 | -44.11143 | 2025-11-19 00:32:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 67171ede-2255-3f50-9644-75e65dbdee71 | -9.37038 | -48.41376 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| cc109722-12d2-3376-bcb1-1668b31077fa | -12.88061 | -50.16026 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 959ed10e-f75b-3b78-a9a5-50662add6a87 | -12.14169 | -45.17543 | 2025-11-19 00:32:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c51f1eb2-65b0-3c04-87e1-b01fcb722ef5 | -11.61876 | -43.908 | 2025-11-19 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1870c552-f78b-3806-976c-a57c6dfe511c | -11.81211 | -44.62681 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 6d165a00-c0a3-3d53-88d4-2397661c0e36 | -10.06459 | -44.8661 | 2025-11-19 00:32:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d75be110-ebf4-395e-a641-127f4366220d | -12.31252 | -47.91537 | 2025-11-19 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 429cda88-1b46-3a9b-a7e6-8c0c031e8bf4 | -13.36059 | -44.78264 | 2025-11-19 00:32:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2be2d5f-6298-32f4-879a-0a22ca93658f | -10.88212 | -49.54082 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5af274d-2115-3ed5-abe1-15f6fb41fb5d | -10.09664 | -47.88504 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 0919e36d-a7a5-32c8-a218-7196da12c688 | -11.77937 | -44.63219 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8cb60ada-99fc-3fcd-aba2-ecd24f5ae636 | -9.39426 | -48.45171 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ea894f7d-959e-3e14-a2ce-7bd4d4011907 | -10.06425 | -47.9193 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df4d5e99-d68c-3aa4-aee2-b4610ded8ccd | -11.82302 | -44.62499 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ee3ce54f-ed7d-31c3-bbed-252e1a8f0297 | -10.77619 | -48.12629 | 2025-11-19 00:32:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe404b86-8aa9-36ac-896e-99c4d2ca8894 | -13.06921 | -49.51137 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 421dbacd-b9fc-3b20-820e-542df44dbf8c | -10.54814 | -44.12769 | 2025-11-19 00:32:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 73376578-7bef-330b-ab11-788208a90d6a | -10.77479 | -48.83349 | 2025-11-19 00:32:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05dfb180-6ef3-38a9-a652-c2155bbd9371 | -10.07201 | -47.90843 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4775e6f8-b680-345b-8e64-3a9316f86f3d | -12.60448 | -48.87415 | 2025-11-19 00:32:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5b4b3e3f-e7dc-3d2b-9cd3-81de43f2d125 | -10.35181 | -48.9075 | 2025-11-19 00:32:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 74e55687-21c4-3acb-b806-9bb2029f1a5e | -13.38435 | -44.37594 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 277c3768-d7d0-324b-b469-6a8f319be2dc | -11.67511 | -47.96826 | 2025-11-19 00:32:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5455fd61-8cb9-3e8d-878b-5e7c5f9961b2 | -11.93343 | -44.8139 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 02197e74-641b-3fce-bc71-4152acc64459 | -11.78161 | -44.64628 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e7cdf197-b684-331d-b5b3-cd7101ab9012 | -10.4066 | -49.75838 | 2025-11-19 00:32:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4cd8d59f-3a03-34ff-ad70-838ec6a9b078 | -10.88336 | -49.54979 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8ca24c6e-4e0d-3745-b0d9-912b26652a23 | -11.66611 | -47.96964 | 2025-11-19 00:32:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 48b8824c-3878-3cf2-9677-c061b02faac3 | -12.69642 | -45.37462 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9e2a86fe-fb7a-352a-97f0-54c703eaf356 | -10.88734 | -54.13479 | 2025-11-19 00:32:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f6d731ed-1429-3b3d-9286-c738999465e5 | -11.79898 | -44.61447 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 8ecc8a4a-aded-3292-9865-7b4c9fec2818 | -12.64945 | -45.53664 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d9aec2c7-007b-3c30-8d44-9f27ab625f7f | -13.90766 | -48.78059 | 2025-11-19 00:32:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d8436ce-5112-33da-bb19-7dc21ce0276b | -12.87935 | -50.15083 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dfb4c40e-c25f-31d6-bab3-ba6f38fd5f85 | -10.09802 | -47.89466 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8953ab0b-7789-38ab-b867-b1386f8d59bc | -13.07045 | -49.52051 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1454c5e3-89f1-3e42-8e98-6817f0a6b589 | -13.49018 | -44.53646 | 2025-11-19 00:32:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc78a3fe-b89b-3223-be8a-4d9638692410 | -12.64957 | -45.54301 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 3aaa2109-a65e-3c42-bf1c-2ebfb35f46e8 | -10.87328 | -49.5421 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c68cadb0-9c4f-3d2e-abd9-e17801e63bcb | -13.4363 | -48.23653 | 2025-11-19 00:32:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d91b279e-8b8b-3923-9e18-2aa42478e1ae | -15.54711 | -55.22429 | 2025-11-19 00:32:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 63c46885-cb4f-3fb4-b679-159b63bd1ca9 | -11.78806 | -44.61628 | 2025-11-19 00:32:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8b97a15c-ae20-32d8-8846-2e21f2d49f8d | -10.35055 | -48.89848 | 2025-11-19 00:32:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 904d1e8b-ed75-3187-823d-5d1a1c10b7ee | -9.98746 | -49.19586 | 2025-11-19 00:32:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce0a053d-d60b-347b-86cc-9318adb128c6 | -13.9719 | -44.22034 | 2025-11-19 00:32:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e557e1f8-c966-31d5-968e-0d69f536ff63 | -11.8099 | -44.61263 | 2025-11-19 00:32:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9d337ad9-f7a5-34e8-b985-99d3b625d8bf | -10.03422 | -49.20731 | 2025-11-19 00:32:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1ef74bb-efe3-39f1-8fd9-9a11b3329072 | -9.37169 | -48.42305 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f7715372-5dc6-3cec-bceb-c1d8f2763824 | -10.74035 | -44.91864 | 2025-11-19 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 53645707-9650-3af6-bca0-27469d49c3bf | -13.06896 | -42.14152 | 2025-11-19 00:32:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 35d3438a-311c-3d8f-a0a0-3c80daf547f6 | -9.38071 | -48.42173 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d60f03e9-e8a1-3bcf-802e-90f78954891e | -12.89594 | -50.20613 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34a7fe76-b6cd-3813-be55-481a061364a2 | -11.66744 | -47.97897 | 2025-11-19 00:32:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6e8a11b5-9d97-3c50-adce-361b43c27559 | -12.16168 | -43.99414 | 2025-11-19 00:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5c2be46b-79c3-3775-842d-d5438c867ba0 | -12.768 | -45.44363 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a84372de-4005-3abe-817a-ebd5f47c1617 | -12.13316 | -40.87545 | 2025-11-19 00:32:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| f93e78e5-838d-3ff7-90f9-20c73fb05d43 | -12.46013 | -54.45629 | 2025-11-19 00:32:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c9be138c-ecdb-3d1c-8ab8-59682b44ba41 | -12.89468 | -50.19669 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef0bdf2f-f459-3fb0-8c15-9034ee777012 | -13.36408 | -44.77499 | 2025-11-19 00:32:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 595e581e-71c2-38bc-8937-b29c23e961eb | -12.42881 | -47.89127 | 2025-11-19 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53704d03-63bd-36bf-bd68-86ec7322a600 | -12.64116 | -45.55024 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c2f5cd9b-e288-3b9d-8556-f7938819cb11 | -13.20882 | -48.32574 | 2025-11-19 00:32:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 71fd3f65-8d6a-3d46-9167-2260e85c1e63 | -10.75121 | -44.91676 | 2025-11-19 00:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e6dd50b1-4236-30f4-9298-c68732d6d7f7 | -10.69638 | -44.7809 | 2025-11-19 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 11315c68-6b91-345b-80a9-0906488ab115 | -10.07338 | -47.91795 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 43513962-e5b5-351f-85e2-5d7663bf43f2 | -9.16421 | -49.63992 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8807faf-0376-3e14-bd62-817b12f7c0e6 | -9.38201 | -48.43102 | 2025-11-19 00:32:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b5c72595-fecb-3511-89b4-eef9b08a2a64 | -12.64772 | -45.53108 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 782eda12-7206-3c18-b1da-b3a224581774 | -11.02784 | -43.89382 | 2025-11-19 00:32:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f8b058b6-0084-3b5e-858f-5474a7f593ae | -10.06287 | -47.90975 | 2025-11-19 00:32:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f68e3773-3beb-3175-8d4b-713df8bf8cd8 | -15.48489 | -43.15749 | 2025-11-19 00:32:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 53.9 |
| 0ed23269-728a-3efa-9e6a-4995fc99bb2f | -12.81553 | -49.34353 | 2025-11-19 00:32:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 215ccb62-47df-3b35-b276-d31c0e8801a4 | -11.79675 | -44.60028 | 2025-11-19 00:32:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 68e23ff4-4109-3a42-b399-8d3a627f046e | -12.42749 | -47.88195 | 2025-11-19 00:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 72f39a48-cc29-34fb-8828-681bff9de205 | -12.63938 | -45.53831 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 749ad371-86e8-334e-ad15-58f21012c3ca | -11.51879 | -44.89897 | 2025-11-19 00:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 097f6e2b-4ba2-3721-a409-6e8b7bc08e35 | -10.77485 | -48.11692 | 2025-11-19 00:32:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 87d99ed8-81d0-30f2-a9d8-73211ae4cff0 | -10.69542 | -44.78674 | 2025-11-19 00:32:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| b4e53ef4-b120-3980-bb1e-cba80af60839 | -11.86058 | -46.96453 | 2025-11-19 00:32:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87ab7851-219c-36c4-92b3-6114500009cb | -10.77606 | -48.84251 | 2025-11-19 00:32:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5da7158e-8cdb-3439-ab10-fe81bb99f6ef | -12.65123 | -45.54858 | 2025-11-19 00:32:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c3b2df33-7aaa-3e99-b6c6-233e809600a5 | -13.20755 | -48.31663 | 2025-11-19 00:32:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c08a2944-ba6b-3ae3-9915-7d181f0872cc | -14.59029 | -47.9918 | 2025-11-19 00:32:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fd15660-e312-39a4-930c-1838291282e9 | -11.0154 | -49.04299 | 2025-11-19 00:32:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e7e185a8-f581-30ed-acd7-47e9f7eb3be7 | -11.20597 | -49.41468 | 2025-11-19 00:32:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README2.md)
