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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a905a53-d928-3a99-ab63-a6e1a54c96a7 | -20.18381 | -46.92203 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e77537-06ff-33a7-b92f-fcca8bbfa51f | -18.22572 | -54.59452 | 2026-04-26 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fcb151b-6362-3547-8819-e324e15d5763 | -20.18329 | -46.92618 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69c21efa-1474-3c53-8a11-f3b7d013117a | -18.50748 | -55.50673 | 2026-04-26 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ebbf50c2-0682-3ed7-814f-4773c080fe18 | -18.29263 | -54.12778 | 2026-04-26 04:44:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46f56c3b-b84c-31e2-ac9a-be680055fc44 | -21.12137 | -42.20477 | 2026-04-26 04:44:00 | NOAA-21 | EUGENÓPOLIS | MINAS GERAIS | Brasil | 3124906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5a0e426-787b-35f9-a88f-231a7decd9f0 | -18.17172 | -51.11052 | 2026-04-26 04:44:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c343546f-b92c-3984-8932-081a10e163bf | -19.49168 | -54.21246 | 2026-04-26 04:44:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a21d3111-eff9-3d10-83a7-d428b9970668 | -23.09794 | -50.38432 | 2026-04-26 04:44:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e944874-1328-3c25-9996-14d01cccaa2f | -18.28856 | -54.13108 | 2026-04-26 04:44:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c1a3b1b-6a2d-3de9-9838-0d918f1d093d | -20.18067 | -46.91352 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2927c6ec-cbcf-362e-a5fe-72749532a20a | -20.71909 | -55.17662 | 2026-04-26 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dac475f2-170f-351e-bcd4-a362d2d5928e | -20.18015 | -46.91778 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fd5eee0-4d93-3c92-bcce-9648bff066a2 | -23.80149 | -54.49928 | 2026-04-26 04:44:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ccdb623c-4752-3f69-8603-76d4a0a3a556 | -22.56986 | -54.92373 | 2026-04-26 04:44:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 834ac634-6459-3ea3-aa3d-9cf16424998d | -18.50824 | -55.50234 | 2026-04-26 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 66a7b225-5f9a-3247-ad4c-7531cf3e077a | -18.75365 | -40.27217 | 2026-04-26 04:44:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b1a189bd-adfb-3dad-ac3a-9ffd5254677e | -20.18645 | -46.93439 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca644f31-82c5-389c-9608-579fbca19926 | -22.57325 | -54.92437 | 2026-04-26 04:44:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a6f1dc4d-00a3-3743-ada8-d515c19564eb | -20.18798 | -46.9221 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd450c8-4ffc-3131-b71e-83d2779b9157 | -19.09561 | -56.05849 | 2026-04-26 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4a93d0ea-3b7f-3deb-83de-0f04f992cd01 | -20.71979 | -55.1725 | 2026-04-26 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c7d88f6-5179-34f3-8e16-28fd8752fcac | -21.49496 | -51.76962 | 2026-04-26 04:44:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e33acd7a-9d2f-3919-bb63-69b983216704 | -18.50843 | -55.50605 | 2026-04-26 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f3d2fe37-ddc6-35dd-9082-c4fe4e514286 | -19.49508 | -54.2131 | 2026-04-26 04:44:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad2afa98-9b2b-3cc7-a6f3-2d9120dedc4f | -20.17299 | -46.87395 | 2026-04-26 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabb53bb-fe64-3771-8c16-039b429779a5 | -18.22641 | -54.59777 | 2026-04-26 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3334d328-8592-3e80-b07c-31ae453a3de3 | -21.50165 | -51.77076 | 2026-04-26 04:44:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a13258fb-2e8b-3a20-8df2-3390a8d5fbcd | -19.95132 | -54.38645 | 2026-04-26 04:44:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aad6f27-6aad-3e72-be3e-7b4e7e3e3426 | -20.46275 | -45.5694 | 2026-04-26 04:44:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85eabf1b-f188-3b98-96a0-39cc3014970c | -18.75414 | -40.26681 | 2026-04-26 04:44:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5a780a3-e11c-3a25-a55e-0840ea5cab3b | -21.49831 | -51.77019 | 2026-04-26 04:44:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2d688acc-16c3-3082-ad81-7953256fc586 | -18.29198 | -54.13169 | 2026-04-26 04:44:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d0584c8-56aa-3161-892c-5c2dbb8a0048 | -18.22505 | -54.59858 | 2026-04-26 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45bf5545-06a6-34eb-a769-ca8ab440e4f0 | -23.79911 | -54.49963 | 2026-04-26 04:44:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0e7ffc0a-9f0a-3062-a4dd-f42664c62834 | -20.40963 | -54.61057 | 2026-04-26 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b64fc9d-dad5-3cf5-a86e-6255f8665bf6 | -18.50921 | -55.50167 | 2026-04-26 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f8f3b321-464f-3242-8043-8bb8f277ebb6 | -20.18432 | -46.91789 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3e608c-c556-3f5c-8b3d-546bd9c87259 | -20.19418 | -46.87237 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3f666f8-efc0-3c28-af97-30f845b301a0 | -20.16395 | -46.84479 | 2026-04-26 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cb7ba6c-1f3f-316a-a471-a471995901a9 | -18.31222 | -54.64277 | 2026-04-26 04:44:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee819686-0189-3824-aae3-66e25272df81 | -21.50108 | -51.77455 | 2026-04-26 04:44:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4440a9a8-3b23-3e93-9e82-339ffffa2d1e | -20.17248 | -46.87806 | 2026-04-26 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f260274-9937-36bf-b590-b6c02795de06 | -20.19001 | -46.87212 | 2026-04-26 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21f79491-750b-3630-9678-fadfa45c1371 | -20.17598 | -46.91758 | 2026-04-26 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4878515e-d0a5-32fc-9b0f-fb8d1e234534 | -11.07729 | -45.27168 | 2026-04-26 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1fbd8f4-0662-31f5-be0b-56378dfa840d | -11.84628 | -55.0171 | 2026-04-26 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3dc664e-7d20-396a-ae3c-ffe565d2094c | -11.55913 | -48.26339 | 2026-04-26 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4bcbc54-fc94-3566-97af-b1ad8f19563a | -11.0809 | -45.27029 | 2026-04-26 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31fdd902-43bc-3523-a65e-9e98abfba04e | -11.29609 | -54.02053 | 2026-04-26 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8a98195-b18f-3bb6-a58a-6b05cfc23436 | -13.49568 | -46.25506 | 2026-04-26 05:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af0e30d9-6c15-36b7-86bc-4eb8a3a01f82 | -14.20221 | -57.42962 | 2026-04-26 05:14:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9d0b61c-890a-3973-b601-4dd6f21fe32c | -11.07463 | -45.26919 | 2026-04-26 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aafe3ea9-6be7-30ed-b960-9496b4b76291 | -12.28533 | -57.39569 | 2026-04-26 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fb412d-02e3-3b79-ae9b-fd69cd073e95 | -11.07791 | -45.26668 | 2026-04-26 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21de1156-6b00-341a-be43-661904664a1c | -12.28977 | -57.38918 | 2026-04-26 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289d1585-9745-3601-adf9-718b0f878de5 | -15.23261 | -54.60657 | 2026-04-26 05:14:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d1c856d-1cd0-3edd-ad4d-0867293e2e2a | -14.20277 | -57.42606 | 2026-04-26 05:14:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09e5b151-aa82-39c0-a1ee-ce3c49055793 | -11.55391 | -48.26271 | 2026-04-26 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5435e2ad-d36e-3d5b-8c39-ddd45581ac07 | -12.28589 | -57.39216 | 2026-04-26 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67a21e59-0778-3e01-bbb4-f994b592f983 | -21.50126 | -51.77134 | 2026-04-26 05:16:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ab5deb60-be7d-3e46-a1b6-6574cd030fa6 | -18.50606 | -55.50683 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8b5143c-f412-396e-bb5c-aa2cb3048484 | -20.7201 | -55.17402 | 2026-04-26 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 018f9f1f-4a3b-3a03-ac0f-a5ffd5f9f4e1 | -16.59345 | -58.24009 | 2026-04-26 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 86ac0315-b7f0-3f29-8e73-800faedb87d6 | -19.09734 | -56.05983 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b7ede9a9-3bc8-3059-8c2d-e09fe763be0a | -18.50968 | -55.50739 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a74cf326-c00d-33cb-b4c4-b8ade4ee976d | -20.18075 | -46.91446 | 2026-04-26 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41722ab-5c32-355c-9094-7840944342c2 | -18.50623 | -55.50935 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0387899f-6754-3cb4-b763-413789e80c3a | -18.3096 | -54.64243 | 2026-04-26 05:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0bd4c26-83db-3df7-8c1c-c69eeca8c1cb | -18.51046 | -55.50556 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53cfd22d-8524-3ed1-910c-0fa1150ae183 | -18.22718 | -54.5958 | 2026-04-26 05:16:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c060fe1a-15a0-3021-992a-89ec3ec5e4f5 | -18.50683 | -55.50499 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 605b275d-93ae-3d0f-873f-4502610b4727 | -18.51031 | -55.50303 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aefbb34d-8014-375b-978f-a95f732e1022 | -18.28899 | -54.13233 | 2026-04-26 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b33e7f8-fd36-3ae6-9b2c-69c1ad6ff536 | -18.31232 | -54.64475 | 2026-04-26 05:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 247faedc-7513-3cf3-9eac-7e11238b13d7 | -20.1867 | -46.91936 | 2026-04-26 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3178b561-61f3-34c2-985e-96fa481bcd71 | -18.29288 | -54.13292 | 2026-04-26 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 450958ca-a373-3e39-b7f3-248302e67aa7 | -20.18614 | -46.92575 | 2026-04-26 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a41024-16a8-34b2-9a2d-5b2db934d6d5 | -21.49653 | -51.77074 | 2026-04-26 05:16:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6ff825a8-9491-329e-9cdc-d067f5f014a6 | -23.79981 | -54.50028 | 2026-04-26 05:16:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8d181c51-1991-39d2-8df6-235bc447cae2 | -19.94844 | -54.38551 | 2026-04-26 05:16:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47a118cc-44b7-35e7-9b6a-172ce20261f3 | -19.09674 | -56.06403 | 2026-04-26 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c14b5c77-f357-34a6-9911-34f8e9c2356c | -9.72107 | -60.20173 | 2026-04-26 05:31:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90037df0-998a-3ced-9e60-65be030aa729 | -18.50763 | -55.50283 | 2026-04-26 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fa19db16-c262-3b58-bef6-5e6708bb12ad | -14.20115 | -57.42708 | 2026-04-26 05:33:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5e00f6f-6837-30db-9566-e34d1dd922bd | -15.23542 | -54.60923 | 2026-04-26 05:33:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20a4940b-7e0f-3185-9eeb-e7bcd08ef2ed | -18.28969 | -54.13308 | 2026-04-26 05:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaee5504-bd85-39e8-879f-76a4b4cbd406 | -18.50724 | -55.50628 | 2026-04-26 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e67b94cd-b373-3b32-8b22-ba8c77d25215 | -15.23582 | -54.60568 | 2026-04-26 05:33:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 948a8a9e-23e2-3916-a91e-ca881440c04f | -18.29012 | -54.12885 | 2026-04-26 05:33:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b463ff5d-3a42-3380-9630-ade34a574552 | -14.20559 | -57.42751 | 2026-04-26 05:33:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43af678b-68b9-3f51-9f5f-3caed8f98fbb | -18.50686 | -55.50972 | 2026-04-26 05:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 082660fc-bf55-35ea-b391-322676c189c4 | -21.49497 | -51.77066 | 2026-04-26 05:36:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cdbd55b4-7f5b-398a-aa98-f66e65f48a2e | -21.49498 | -51.77007 | 2026-04-26 05:36:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7f3a48cb-769e-38e9-94fc-b9d11f8fd244 | -19.0946 | -56.06064 | 2026-04-26 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b59b5da8-5838-3c98-bdd8-22422a2cc38d | -19.09424 | -56.06388 | 2026-04-26 05:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fdbfc77f-38e9-35f7-840c-4077b6dac250 | -21.50187 | -51.77118 | 2026-04-26 05:36:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 918f92b0-117d-3a5e-a92e-60232566e90b | -21.50188 | -51.77061 | 2026-04-26 05:36:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0466ee47-c352-35d5-b0bf-2ad5dfab4329 | -22.13499 | -53.7607 | 2026-04-26 06:37:00 | AQUA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 43415641-2b17-3ef6-a4b1-91d5fd1ec363 | -21.49672 | -51.76864 | 2026-04-26 06:37:00 | AQUA_M-M | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |


[Clique aqui para ver as próximas entradas](README3.md)
