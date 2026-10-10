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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f71a203-28c4-377c-8ef3-088f225c81cb | -12.02541 | -43.48918 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0dd3b15-d088-3483-ae0f-ba4f6cdd7927 | -12.36375 | -46.60384 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e01e4a2a-b2a2-31a8-82b1-3a6045b860a6 | -11.75827 | -46.79293 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5df851ef-e3b9-3a38-b1e5-07dde92a670b | -12.37806 | -46.57501 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1151deb8-dd66-3913-b444-c32db75966ef | -11.84187 | -46.80836 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b63ad859-27f4-3867-be1b-93e699034dd1 | -11.36578 | -54.03022 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 817da145-a42e-3630-8733-73886edd0573 | -11.76321 | -45.45504 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7da7a570-91b6-347a-ae54-faaa8bb8fd17 | -13.11034 | -46.35424 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1c90374-dc5c-3c88-b9cd-2d66b5d96957 | -13.15526 | -54.37023 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a38c1bf-98a4-3b3b-85af-2ef92b95b497 | -14.0311 | -48.76046 | 2026-10-10 05:06:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a98b3ff2-d896-3def-99e0-11512caf691a | -12.93213 | -47.44222 | 2026-10-10 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e79ad865-5c30-3721-b498-dd81665ef422 | -10.18501 | -52.56264 | 2026-10-10 05:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28553609-661a-3b8c-bc5b-3d64410dc000 | -10.27872 | -43.94703 | 2026-10-10 05:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1be3ea8-03bb-3bcc-ba68-89f26c0120e0 | -13.17217 | -54.37293 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 113139f6-85af-357c-be36-46a1f4c9b25b | -13.15187 | -54.3697 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51e78970-5241-3730-8c20-18a61684bef5 | -10.60659 | -60.47922 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 893f5253-0b1f-3dc0-affc-a1ad7a8b0ced | -6.99173 | -59.10382 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a7ff6b-3eb9-32db-b426-a2d51c225ed5 | -13.36421 | -43.89381 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa11b541-ed30-3a36-b105-c27023e6fcd4 | -13.63383 | -44.42496 | 2026-10-10 05:06:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ac49afe-c844-3490-b025-bf33137cbf70 | -7.95174 | -54.76191 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ee90cc-dd7f-3d19-b24d-f49bc51aea20 | -11.01924 | -49.11157 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f073d10-a88b-3216-8908-7ccf57629ad4 | -8.53452 | -66.98029 | 2026-10-10 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff36b49e-7c94-32ab-82aa-395c448af2cb | -9.76055 | -53.87848 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8f89c7-c919-35d4-b55f-18b1f527d05c | -9.51734 | -54.67706 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe686a3c-6ed0-3142-bfd2-d688900b6d0c | -11.48551 | -54.61795 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c57451f-9e87-34cf-b4da-4fb0a68c928c | -10.61529 | -60.47705 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe51446e-07e0-3279-9351-5886f0d40515 | -13.1036 | -46.36408 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2787f918-1b36-3ac2-b842-e1aafba62746 | -12.07404 | -47.3829 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 918ef242-39ca-3dc1-816e-481a3b2a6fbe | -14.45887 | -43.94171 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c91ff0ee-932f-3e3a-93d1-130a79fee07c | -11.59802 | -43.75107 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc3539ca-5bc3-3b3a-9e07-4f55779ce802 | -7.45438 | -63.64683 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be5a3ce-e4a2-3941-a021-61af6430ffdb | -7.91841 | -54.71358 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a0d7103-b580-30b8-b02c-04dced0f9b9f | -11.6684 | -46.78263 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ac2ba4-dc60-3af2-bd0f-be2c1e3b01fc | -11.9801 | -57.61369 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8ad1a19-929d-3413-baa4-b3ee7884abe9 | -11.90778 | -55.90662 | 2026-10-10 05:06:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d1384ad-bbdf-3d6f-b8ac-2b46a0266c37 | -12.24329 | -54.38594 | 2026-10-10 05:06:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f54bc3e-deb7-3935-b14f-a04c741407c7 | -11.08227 | -44.1038 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8aac507-e091-3def-8dd3-1153db1c12fa | -7.56531 | -61.5448 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e99d948d-205d-357e-a6e4-e5916e859d17 | -14.53097 | -48.04475 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c0b79e-e47b-388e-a92c-59b83cccc89d | -6.48979 | -62.85346 | 2026-10-10 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f72c6d2-46ca-3d06-b29a-e244fe2b150c | -10.6222 | -54.75615 | 2026-10-10 05:06:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d9fd3b1-68c6-3342-aab6-cbe32b2e06f6 | -6.49032 | -62.8505 | 2026-10-10 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd27923-2adb-3946-aabb-eca963fff859 | -7.92337 | -54.72504 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25495d56-c629-3535-839f-332ea3d2de50 | -9.29822 | -47.38601 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5556992-87df-37c6-9098-f10ba09f903b | -6.97405 | -59.30828 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcbde80c-c803-3886-93c4-be48f6cdb17f | -7.75566 | -54.94766 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c176a2d-90eb-320c-a883-4d6cc51d067b | -11.31968 | -51.10898 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 556cbf1d-37c8-30f3-be3d-0a1aa164b30a | -8.19237 | -54.7224 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dd026e2-7258-338b-bc75-6033b61d5d35 | -7.56609 | -61.54237 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 105a1e05-04fb-3148-bd19-f629a4ce9a2c | -15.02512 | -46.26316 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dfccf1e-27a6-3cba-9529-4804370b868d | -8.75927 | -49.60804 | 2026-10-10 05:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9187cc2b-29ca-39f8-83c9-26147fdc9753 | -8.24308 | -54.72337 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46fd02ca-f5fd-3d81-bdbe-84266a570e17 | -8.5848 | -53.0988 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8f6142-d265-39a5-92dc-d605c4075a07 | -13.37575 | -43.90623 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6dc26fa-f792-31b4-9ad0-be7c9965894f | -10.89424 | -44.83362 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c61b83c7-3052-369d-8b0d-d0207bb2f2f3 | -10.90012 | -44.83401 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c187a075-23cf-3cfc-9842-e47328610351 | -13.14141 | -46.33637 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48df1bce-0bef-3f17-ab16-1d3d779be48d | -9.45317 | -56.91071 | 2026-10-10 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4573d53-14ca-3ab4-8816-4a67a2dc1865 | -13.77512 | -48.13485 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3d32378-8c03-3206-854f-e72d0fa11425 | -11.96203 | -43.47219 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7856518-ddfb-3c7f-bbb6-81027cc81ef7 | -14.71642 | -48.22934 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0af5142b-df41-3902-a14a-3fd85f17fd49 | -8.48814 | -54.61268 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f01dd44-244a-32f6-859c-4067ae3ed52a | -7.90739 | -54.71893 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85ee4d1-03cb-38ae-b46e-d482ff25bfc0 | -13.50429 | -48.6131 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0df5690-bee9-3e4f-9bd3-9a3884249c37 | -13.14678 | -54.35757 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 088e4dbe-ceed-37db-af74-aa99481306d6 | -10.60935 | -60.48711 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fefbe35c-7aa4-3873-b655-3402a7f2946f | -7.92007 | -54.72451 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb09c4d-cc61-3e48-982f-7675029d7b02 | -13.16879 | -54.37239 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8e36de-0b11-3b7d-b6e8-748e13c7492a | -8.49916 | -54.60731 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 167850f1-9905-337b-8427-e3ceae4a438a | -9.21489 | -45.65351 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6563f44-e90e-342b-82d2-69704399d110 | -9.51181 | -54.66903 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52d99221-1ad6-306b-8ba4-95f69cea67c9 | -11.00088 | -47.96281 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a5adadc-9510-3414-80c5-eb9c1a3144dd | -12.36335 | -46.60713 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef8e494b-9576-367a-86ce-bf02ad8db7a2 | -12.49442 | -51.29681 | 2026-10-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b263f84-7097-382f-81f4-6d74064d49bb | -11.07041 | -54.5153 | 2026-10-10 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36eca53e-092a-332f-a115-7428dd4fcf21 | -12.41045 | -54.36386 | 2026-10-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45ac4ed-3fc4-352e-9dfc-9e83a5f9278c | -9.87256 | -50.51962 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5ddbc51-d313-3dc5-9744-8186dc3d333d | -11.45836 | -43.37925 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e070308-3de1-3767-80c5-25ec4960c4b4 | -10.25709 | -49.69407 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fabc0d9-5f24-3acf-8185-cfcf30243699 | -11.98319 | -43.45827 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2027f4e-a03a-342a-9088-f26fad35dfa8 | -12.17538 | -54.27842 | 2026-10-10 05:06:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13b058b4-0eb3-30ae-9289-c498218f79c0 | -7.9085 | -54.73333 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1768d595-a6a8-3806-918b-5f897832a89f | -11.02967 | -44.02516 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b5cf6d9-712f-3fd5-80d4-21be44a00756 | -6.99564 | -59.10447 | 2026-10-10 05:06:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3774e10-ebc3-3782-b3ad-788953a1261c | -11.76407 | -43.53034 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c832a55-a477-3ac5-9a3d-d0081aa69a62 | -11.08088 | -44.1154 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cfe7ecb-0c50-324e-a96c-3f1c48f5bf77 | -10.87389 | -57.08574 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05640473-887a-3ccf-865f-c10a579e9841 | -11.36971 | -54.02709 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aec7857-5ab4-3ddb-996e-e34913f00753 | -11.98941 | -43.4548 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4ada37a-0ca2-340c-a7d9-6d20fed019f4 | -7.8902 | -63.77625 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec0e9628-46bc-3c23-af6a-ed3550aaba96 | -10.86266 | -49.1428 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15fcb748-2171-35e3-9a9e-beee810d8f14 | -7.95229 | -54.75844 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd913e28-3b89-3f12-8a94-d1f620e3aabc | -7.75619 | -54.79495 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32767efd-6cfa-34e7-a54e-950185543288 | -7.75343 | -54.79095 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 064721e1-c73a-3772-b919-dad7d0dbb4a7 | -11.20156 | -44.87575 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65fcdaeb-f916-3bf3-a277-f0aafb93c218 | -12.29643 | -63.36762 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5595a2d-138c-3770-8742-bd0ac6d5c0bb | -8.17362 | -54.7123 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfd357a5-acd0-3c8e-bb1e-06be08ff6af0 | -11.78857 | -46.72228 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8befbc80-aa12-3394-8343-2f65b01d47a1 | -13.3636 | -43.89928 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c794ef-c620-3f5b-8f73-20734825be43 | -12.2974 | -63.3624 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README130.md)
