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
| 50bf537c-7d68-3ca2-b822-48ce02fbdb81 | -8.9416 | -60.4982 | 2026-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 42e6a5a7-20b8-3eba-a736-ef09923bdc75 | -11.4681 | -44.5558 | 2026-08-11 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2ad872e2-79ae-38bc-b72c-19bde845e061 | -10.4237 | -46.6809 | 2026-08-11 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 445d9599-73a1-330a-a4a2-455f7f0c6951 | -14.4539 | -45.6948 | 2026-08-11 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 61940cff-7ebe-3d27-966a-942a4ea004ca | -12.4703 | -45.3308 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 305.5 |
| 1f8b4989-0d1f-36b5-a939-20c543b6fe99 | -8.9415 | -60.5174 | 2026-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d685a394-bfc2-38b0-801f-fae3bf57c711 | -12.4905 | -45.2816 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 080c12ee-74fa-3388-90da-2d6937b9d220 | -4.4507 | -47.9112 | 2026-08-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 152bfddb-48e5-36e2-88f8-99098690e298 | -14.4734 | -45.6914 | 2026-08-11 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| fa2e6bb0-acc0-3b72-beb1-d1e372ebe57c | -12.4511 | -45.3338 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 0aec0784-d40e-39f3-b276-7fd0794ad139 | -8.9601 | -60.5165 | 2026-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bb9369af-7a7f-338f-81e5-03ba27ec1180 | -12.4699 | -45.3539 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3ce83cd5-1ae2-3730-949c-8fcc2d3ea765 | -18.0619 | -51.3063 | 2026-08-11 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| e8d9cf5b-0a64-3815-a616-bde0398779b5 | -10.424 | -46.6584 | 2026-08-11 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 34a0a0bf-a9a2-3625-90a8-ca1604f2b8d7 | -14.4544 | -45.6716 | 2026-08-11 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a1084579-532d-396b-b0e6-9b04fd339650 | -4.4507 | -47.9112 | 2026-08-11 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| edb76396-cb02-3f3f-a847-b1000de0eeb1 | -18.0419 | -51.3097 | 2026-08-11 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a4371096-bf04-35e2-9dfe-75327cc0ae42 | -11.4681 | -44.5558 | 2026-08-11 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| dbafed52-cd93-37d0-b5ef-d8e2f5b9256d | -4.2634 | -48.2016 | 2026-08-11 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| cbc866eb-6967-387c-8b43-35cbbe48d55d | -18.0619 | -51.3063 | 2026-08-11 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 72f6da9c-eace-38b2-990e-bac405887c71 | -4.2821 | -48.1791 | 2026-08-11 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 1b967a8d-5894-37d5-9359-2053ff782d2f | -14.4734 | -45.6914 | 2026-08-11 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b66ccdd6-fddc-3557-9e9a-2b9ea5e55552 | -11.4677 | -44.5791 | 2026-08-11 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 242ea404-7f82-3a89-ad15-3c7f7cb385d3 | -2.9623 | -49.2587 | 2026-08-11 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d1316e3d-97dd-30af-95e9-c2f075a97c5d | -21.4622 | -48.6122 | 2026-08-11 00:50:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 30ad8b86-d932-33ca-b946-483377f796bf | -8.9039 | -60.5769 | 2026-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 26ef68f4-df1a-324b-a471-677c1204b924 | -4.2635 | -48.1799 | 2026-08-11 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 4f70d04f-2fca-3496-bbbd-77da300067ca | -14.4539 | -45.6948 | 2026-08-11 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 55954f67-1154-33c6-9f43-e83de2a1250d | -2.9623 | -49.2587 | 2026-08-11 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 40567215-0594-3aad-a347-846846544ba6 | -21.4622 | -48.6122 | 2026-08-11 01:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0c4993c2-85fd-3c31-867e-bf433f3ab11a | -8.9039 | -60.5769 | 2026-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8335bd87-8343-3d13-b87b-72090530deb6 | -14.4734 | -45.6914 | 2026-08-11 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 53fc4771-83a1-350a-ada0-49d4a6c64fad | -8.9041 | -60.5577 | 2026-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c50fc4f8-62e5-3058-b408-8d1e6a5762d8 | -4.2635 | -48.1799 | 2026-08-11 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 08669b4a-84e9-3b86-accd-12709e096552 | -11.4677 | -44.5791 | 2026-08-11 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f25d1e7e-1e8c-3c10-aac1-8d293ed767a1 | -14.4544 | -45.6716 | 2026-08-11 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c9a836fc-3fdf-3877-993e-5004507f3b66 | -18.0338 | -44.4178 | 2026-08-11 01:00:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 93bdafc8-3794-3fdd-b469-26cc9e8c6482 | -8.9038 | -60.5962 | 2026-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7fd4b3e9-e9ea-3a20-a136-5a6d90a7f694 | -11.4681 | -44.5558 | 2026-08-11 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 68eb5825-87f8-32ac-9a39-ec60b4eb5ae1 | -14.4539 | -45.6948 | 2026-08-11 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5e5e048c-c321-36d6-92c0-9a69609a1f1c | -18.0619 | -51.3063 | 2026-08-11 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 434ef444-fa8a-3710-ba3f-67cb68c58178 | -18.0137 | -44.4225 | 2026-08-11 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1b610b5a-4ec4-3d04-9a2a-18267e3a5769 | -13.8803 | -53.7823 | 2026-08-11 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 89e78880-e704-3e56-85b5-612ef031b222 | -18.0619 | -51.3063 | 2026-08-11 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 396d846f-9b7b-3fd4-b3ec-87ec4f42ff0a | -8.9038 | -60.5962 | 2026-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1bc6906f-7c88-31bf-8067-d72119f562d5 | -11.4681 | -44.5558 | 2026-08-11 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c6c806b4-fd7d-323e-a9e0-2a50a8fa071b | -18.0338 | -44.4178 | 2026-08-11 01:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5a00efea-4bd5-3da5-a9f1-709539235726 | -8.8854 | -60.5778 | 2026-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 02547559-ae88-364d-b9b3-9e53d78a152c | -11.4677 | -44.5791 | 2026-08-11 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8cde5028-de3d-30f8-9247-7283adc51fa7 | -14.4544 | -45.6716 | 2026-08-11 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b842e30f-7b3a-3bad-ba66-d5baf72b2662 | -13.8611 | -53.7845 | 2026-08-11 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9ba6f1a9-0f0a-3811-8228-d48fa60aab11 | -14.4539 | -45.6948 | 2026-08-11 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 0596adc5-45e7-3a39-ac69-1ef0bf4cef19 | -8.9041 | -60.5577 | 2026-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| c59fc6c2-d90c-373d-b25b-33ab342743bd | -18.0137 | -44.4225 | 2026-08-11 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d421792c-68da-3b2e-b397-32ca2905bb9d | -8.9039 | -60.5769 | 2026-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 43866012-6688-3fa8-860d-792c41b84c34 | -14.4734 | -45.6914 | 2026-08-11 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4f1f7dc5-d67f-3bf5-9ef6-4ab19399f560 | -9.3906 | -47.4878 | 2026-08-11 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| ee130c6c-2e24-3579-8723-a2e7a186c90c | -13.8608 | -53.8053 | 2026-08-11 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| a09ea525-6806-3463-a652-d60fb7304adc | -12.47 | -45.38 | 2026-08-11 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39729980-c077-3c95-9d85-04febcee6560 | -12.44 | -45.37 | 2026-08-11 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5e4c770-ff9a-329a-8a2a-221ed6d8b900 | -12.47 | -45.33 | 2026-08-11 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b630c77a-3df9-38e7-8181-c50cfb71ce5f | -12.47 | -45.28 | 2026-08-11 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29afec21-30ee-3318-bb17-169213e4e823 | -12.44 | -45.32 | 2026-08-11 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c33ad80-a28e-3797-b316-d6efb9d27e29 | -4.2635 | -48.1799 | 2026-08-11 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7df77fdf-b7b8-3fb2-915e-5f49c1662443 | -12.4896 | -45.3278 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 97b068a0-3c99-3f55-b540-cb5d1a18b071 | -4.2821 | -48.1791 | 2026-08-11 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| db0abec6-995e-32ca-8b2e-d5598ab8c5be | -21.9258 | -48.9666 | 2026-08-11 01:20:00 | GOES-19 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 80fc4cd3-e4a3-34f9-80d2-4e65ad999fdd | -12.4511 | -45.3338 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5be1ba60-3478-3b51-87c6-7621e606ac11 | -14.4734 | -45.6914 | 2026-08-11 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 908872bd-1650-34c0-a67a-f9816ab3fd09 | -12.4703 | -45.3308 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 649.2 |
| 15d65536-c6af-3ba3-ae74-cd63bbd44db6 | -8.8854 | -60.5778 | 2026-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 29ba71c5-6913-3fa1-9740-5275d6928dbe | -8.9039 | -60.5769 | 2026-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| df214d3b-2fdf-3878-acc8-379db215b721 | -8.8852 | -60.5971 | 2026-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f9c04966-47ac-391f-8781-d6c85621d15e | -12.4905 | -45.2816 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 650120b0-cd61-31f8-a530-9a34b8b9760f | -18.4117 | -55.5584 | 2026-08-11 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| a4759fc3-5698-3c93-aa69-179b07f57444 | -12.4699 | -45.3539 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| e175b18e-2bad-3a51-8f7c-151ac626b53c | -18.4121 | -55.5373 | 2026-08-11 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| c67e6ea0-071e-3fdf-81a4-67663836a664 | -14.4539 | -45.6948 | 2026-08-11 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3fd50605-6b66-3897-8bd0-202bc492d051 | -14.4544 | -45.6716 | 2026-08-11 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7093e3b0-0283-3802-a482-975ed0468d68 | -4.2634 | -48.2016 | 2026-08-11 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6a59898c-efd0-35b3-a86f-f99dfc801b3c | -12.4708 | -45.3077 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 0168f7ab-9a6b-357d-8b3d-dfcce6d89dde | -12.49 | -45.3047 | 2026-08-11 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 54cd384f-e40a-36f4-81e7-ddf93d52abe6 | -8.8855 | -60.5586 | 2026-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7cd41b61-38e2-3e05-ba36-9c6472ebf02e | -18.3918 | -55.5612 | 2026-08-11 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 33ec44d2-2be5-3eef-8940-3bfe1a08e6bb | -14.4544 | -45.6716 | 2026-08-11 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fb20de29-1684-3c48-9cf9-fb52732ace26 | -14.4539 | -45.6948 | 2026-08-11 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9c6832ec-6344-32b8-8026-c3d16eae2844 | -11.0298 | -45.6308 | 2026-08-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c6c73b9e-4ab0-3924-918e-32069b583b96 | -13.8803 | -53.7823 | 2026-08-11 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| aa1c04d6-1d40-385a-9ac6-2d7b1786d0f9 | -2.9623 | -49.2587 | 2026-08-11 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f535a24a-a360-3540-b2e7-9a4d9d5d79df | -13.8611 | -53.7845 | 2026-08-11 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5afbda9e-a559-3f62-b1df-040a8a7695d0 | -14.4734 | -45.6914 | 2026-08-11 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7e0706f7-2f79-33c2-8a5a-743ec848cbc8 | -8.9041 | -60.5577 | 2026-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e5799062-55e5-37a1-b986-c8fcb7367ec1 | -8.9039 | -60.5769 | 2026-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 07ec74c6-fd4b-3056-b693-1e9697f026df | -4.2634 | -48.2016 | 2026-08-11 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 25a082e4-4691-3f1c-b461-50e67ccd91d5 | -4.2635 | -48.1799 | 2026-08-11 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| fcfb5826-77d4-30ad-9fcf-a027e98aebdf | -9.3906 | -47.4878 | 2026-08-11 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 21089c37-2f8c-315d-a34e-9312fb65824a | -11.0294 | -45.6536 | 2026-08-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4894afb1-2169-39e3-a928-9f310604dbe1 | -8.8854 | -60.5778 | 2026-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b191d3f6-e38a-3c42-bbc3-5cb388d71268 | -13.88 | -53.8031 | 2026-08-11 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d012d14b-1457-36a1-bfba-f1d12645d9fc | -13.8608 | -53.8053 | 2026-08-11 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |


[Clique aqui para ver as próximas entradas](README3.md)
