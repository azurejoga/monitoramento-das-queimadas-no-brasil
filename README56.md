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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e1c6654-1160-38d8-8eac-ee62cf823657 | -17.64644 | -53.15168 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18a17d7d-101d-39a0-8e10-6af24ea67aa6 | -17.64292 | -53.15097 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb63d6cd-3cf5-3ae1-9e9e-7a38db9d106e | -17.64221 | -53.15511 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eac78318-a97f-3a39-908e-bc970856e97e | -17.64149 | -53.15924 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de3818fd-3b26-37b4-944f-8342755a6e5c | -17.64078 | -53.16338 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| defba0b5-23a0-3b3d-8e4f-ff66e98a0727 | -17.63726 | -53.16272 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14856b9f-f517-30bc-b544-855918f9dc25 | -17.09303 | -52.14986 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aeec1cd-4b17-3e03-ac30-32bf4bcff809 | -17.09237 | -52.1538 | 2024-09-30 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a4cb0cc-ba6c-30bd-aef2-bbe172229b63 | -17.11635 | -53.2789 | 2024-09-30 04:34:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc1e1ca1-d322-381a-b187-254ef90cb511 | -18.65476 | -52.47149 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de258fab-a1e3-37ec-831e-6be1930c0090 | -18.65411 | -52.47538 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba62f6ee-79d7-359a-b070-959ccb6f10e3 | -18.65346 | -52.47928 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82416e9a-dd65-3ac0-9d73-a5cb02d241a2 | -18.65071 | -52.47473 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4deb412d-3f7b-3466-bc69-58983c53be44 | -18.6486 | -52.46634 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e00a3634-3240-38a6-9de3-b5974c2b4940 | -18.64795 | -52.47021 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c6985f5-1680-3189-97bf-0e327046a1df | -18.64326 | -52.47731 | 2024-09-30 04:34:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fea91942-448b-3eef-983c-bf054864342d | -20.47643 | -53.67517 | 2024-09-30 04:34:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 651f8e0d-79f7-3599-ba48-6ea6a6268dea | -20.81174 | -53.11753 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a33d888f-9515-3307-a027-a2c401cc8e20 | -20.81107 | -53.12149 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ce7abb-e0a0-301b-b1e2-fedb1f56e99a | -20.80765 | -53.12083 | 2024-09-30 04:34:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dbc2f83-e078-3357-8949-a595470cce62 | -21.38024 | -53.82456 | 2024-09-30 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 225f540a-61b6-3e36-9f4e-e13ca85ce4e8 | -16.4423 | -53.93753 | 2024-09-30 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b43a2c6d-a671-3bf8-8a2d-8cdf9ecd4ca8 | -16.44147 | -53.94222 | 2024-09-30 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da112f32-4f15-35f4-aeb2-d5485eecaa43 | -16.43941 | -53.93213 | 2024-09-30 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a748642-600a-38cc-bf79-20a30f8b3a2f | -16.43569 | -53.93147 | 2024-09-30 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1949985-e9d9-3052-a6b6-8f412ce7802a | -16.43197 | -53.93081 | 2024-09-30 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2278955-80d8-3371-b8df-59879ba1e97e | -16.0866 | -53.52345 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 178c7d13-d30f-3b40-b5c4-d0b279c824de | -16.08582 | -53.52795 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c14787a-ee5b-339e-8f81-6859da34cec3 | -16.08218 | -53.52717 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e9a77a5-dacb-3fb8-878e-180be5364aaf | -16.08139 | -53.53172 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1917819c-c324-3f45-8402-dcdfec316146 | -16.0798 | -53.54091 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4a8eefc-b37b-3e13-b226-68301fa1ae3a | -16.07774 | -53.53103 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4008a036-9ca1-3d97-a367-ff106588de83 | -16.07693 | -53.53566 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 754087d1-d26a-3597-82d5-ad3b90db968e | -16.07485 | -53.52593 | 2024-09-30 04:34:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 943519c0-848c-3818-a3e0-22898367c97a | -18.84738 | -54.50883 | 2024-09-30 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a59b8d19-8bea-38a6-99e8-5c2164769c76 | -18.84654 | -54.51354 | 2024-09-30 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b336d610-4a38-32f2-b6a5-4de4f2a955ab | -18.84571 | -54.5182 | 2024-09-30 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f614927-e325-3830-8606-63eba4f08fb4 | -18.84454 | -54.5033 | 2024-09-30 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7937a375-f4f4-34f8-9178-37b909e5dae5 | -20.76313 | -54.83547 | 2024-09-30 04:34:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c10aa63-549e-3e26-b2d7-9f40e7fc9a94 | -20.76031 | -54.83004 | 2024-09-30 04:34:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1f1255b-9575-39a6-acac-ac6bb25507c8 | -20.75948 | -54.83466 | 2024-09-30 04:34:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9506a098-2b7e-309d-83d6-ccadcc1b8780 | -20.47598 | -54.71799 | 2024-09-30 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60999de4-4058-37b5-a5e1-4d3de9259728 | -20.3366 | -54.84554 | 2024-09-30 04:34:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 01747881-12a2-347c-9b2e-c7459d6ac593 | -19.9909 | -55.48747 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddb8a824-98e3-3121-9e8a-dc4e2de726a4 | -19.98706 | -55.48668 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9f1527b-d3ed-3422-8b1f-14f2f91e7c69 | -19.98321 | -55.48599 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff5fcb10-6380-32a8-a372-fbbac91a68e6 | -19.98231 | -55.49092 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cb4db52-b9bf-3e82-87d9-79e09aedd33e | -19.97845 | -55.49025 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9046638-dd76-3571-b5b5-7c1e417ac157 | -19.9775 | -55.49539 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 876bf54b-aeaa-37e9-9e83-961419837973 | -19.97458 | -55.48961 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce3b5a4b-ed81-343d-bb48-5cbdb7a76c6a | -19.97359 | -55.495 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfd17df7-65d1-3ec8-8c9f-2195de87616c | -19.97257 | -55.50055 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 791e248f-179c-39fc-abc3-81206e78816c | -19.97159 | -55.50592 | 2024-09-30 04:34:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a4754f9-ebfb-3ab9-9dc2-69f7fea7e4f7 | -21.67252 | -54.8391 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea401e6-65be-3bdf-bebf-77dd288f1409 | -21.67172 | -54.84362 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5fcb4f7-a98b-3672-9b0f-b3b0acbb7a34 | -21.66246 | -54.83231 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c51e9b27-fe5b-3c26-81f0-dd034fbab4e6 | -21.66166 | -54.83683 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5c1c7607-0826-3fb9-9109-6edb26eba981 | -21.65884 | -54.83155 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fcf2969-e18b-3e52-8931-46378ba1dffc | -21.65845 | -54.855 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 160af2e0-665f-3125-9e4c-d7192ada7663 | -21.65483 | -54.85425 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb5bd551-f92f-38fc-8ef4-c80005e1bdf2 | -21.65402 | -54.85879 | 2024-09-30 04:34:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aac2e3ec-daa4-3e54-9c94-547cfb9f3e24 | -16.65273 | -55.21877 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d4523e7-264b-321c-963b-20237cafffcd | -16.65143 | -55.22596 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1e4f65fa-9ff0-3596-aa00-e57949a24f9c | -16.65077 | -55.22955 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9082f910-1dd6-3bee-a93c-385a9610d1da | -16.64941 | -55.21438 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e1c86ab5-8145-3c92-aaee-f945e822d677 | -16.64875 | -55.21797 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cc7a5b5b-369f-3ba3-a80c-fdb35269377d | -16.64679 | -55.22874 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7e3a407e-17cf-3955-903a-275ce866cc12 | -16.64613 | -55.23236 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd8c691c-10c6-36e0-8d52-6878bf458036 | -16.64477 | -55.21718 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f1068284-1333-3e4f-9ba4-961ad960809f | -16.64078 | -55.2164 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2fa94b57-a132-3274-a57b-2df149f8ff3c | -16.6368 | -55.21562 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0e4efd1d-4821-3dc5-9dc0-593c4bdac334 | -16.63215 | -55.21842 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4e73a840-3c46-327a-9743-0438519f58c0 | -16.59796 | -55.96707 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 74e5e0de-f796-3330-9ee2-8f7ae78d2f5f | -16.59721 | -55.97107 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 64f7c525-8fa8-3b40-9248-c85fd25d6018 | -16.59602 | -55.9543 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 434bbccf-88fe-30a2-8c55-1b51d55a7b0b | -16.59571 | -55.97906 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 059a542e-dadb-3fcf-b78f-79a4829e0d48 | -16.59496 | -55.98307 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 621dd32a-e3bb-3200-8154-b801c9478ecc | -16.59453 | -55.96224 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d339b2e5-1e5d-38a7-b068-bd6f1a96a34c | -16.59378 | -55.96624 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a6ab58ab-c5f8-39ff-b1ad-2b5c49ffd9a1 | -16.59303 | -55.97023 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 506acad2-0631-3ab4-8625-0a59e62a0dd9 | -16.59184 | -55.95346 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ced867fa-37b7-3651-9d7f-fdc7311f003b | -16.59152 | -55.97822 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 323c6baf-c677-320c-a3fc-f8810ab88cae | -16.59077 | -55.98222 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d756e94-2f55-3fde-9549-bdaac11770e6 | -16.59002 | -55.98623 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3941be64-4a6f-32f9-b1f0-927e0f24b24d | -15.90404 | -55.39752 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 377c2dca-c669-359a-9e12-af93bc8e34d5 | -15.89932 | -55.4003 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21bf2d12-3c44-3249-88ab-5b7000eb7baa | -15.50107 | -55.75068 | 2024-09-30 04:34:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d3a86aa-9a40-3764-80d9-c4c2f1d78bff | -16.71041 | -55.54461 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5cf03902-ce6b-3cc4-b4cf-731958704672 | -16.70705 | -55.54001 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 32e76fed-db65-3046-be15-8cd8ba0a513a | -16.70636 | -55.54379 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3253c437-8112-33cf-9cbb-ab58dc20ca21 | -16.60556 | -55.97276 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1d2777e7-8851-3a01-af4c-0ae6bb9ad32f | -16.60482 | -55.97674 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22dcb3ac-03e8-3dbc-a436-11af77b4a04b | -16.60407 | -55.98073 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 103d1a24-2560-389f-8582-22cf84b25a58 | -16.60288 | -55.96393 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8e7c58af-9b71-3c17-a54c-51824d7f9c52 | -16.60213 | -55.96793 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f28578e0-7255-3fa1-9bae-4c38a852bd3b | -16.60138 | -55.97192 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c0c8f7bf-a675-3349-a6d6-ebb4bcfe04ad | -16.60064 | -55.97589 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c86bbcca-b8b7-3247-9d9f-8b1f721ea0ea | -16.59989 | -55.97989 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 951171bc-b4b9-3f4b-8a9f-119bf4ed2cc2 | -16.5987 | -55.96308 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f22bee6d-0c4f-38cd-ac2d-1b42122300af | -17.162 | -56.26119 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
