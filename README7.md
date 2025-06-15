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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4855fec5-81d7-351f-aed8-10d38411bc32 | -17.59643 | -43.19672 | 2025-06-15 03:55:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 102ba567-3a0c-39f6-8e4f-0e4c60d94339 | -19.45461 | -45.30691 | 2025-06-15 03:55:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b5fd1c-7fcf-32e3-83dc-7e9902af8687 | -12.76263 | -44.40601 | 2025-06-15 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02d6f382-8443-377d-8132-ca940b259f3e | -14.82967 | -48.42743 | 2025-06-15 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e11a3765-6690-340c-ad65-c65e9366fb85 | -12.08929 | -49.49177 | 2025-06-15 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81109f7b-8037-3e7a-ac1f-347b28163caf | -12.60433 | -47.07367 | 2025-06-15 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6ff731a-d9e4-3d8e-8a3a-acf07845214d | -13.22955 | -49.83682 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cdf2dec-bb4a-32cf-8950-dcc318ba8fbd | -14.37828 | -47.82366 | 2025-06-15 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70fa3d0d-dd8d-3a7e-b87a-a9722c64ba8e | -19.85025 | -43.84578 | 2025-06-15 03:55:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b8b52b83-83e4-3e35-8d2e-91e1ddc49490 | -15.4111 | -47.87742 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d9fda92-9af8-30cb-a1a2-b295d79c6c7d | -15.40749 | -47.87107 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b55de095-f543-32c6-9df6-3717c4116723 | -15.39875 | -47.89141 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68deb627-7db3-3759-a8ac-87b6dea8d7e0 | -18.38976 | -44.33664 | 2025-06-15 03:55:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10401cf9-ee37-3a87-9ac5-31d25ae10db4 | -15.6403 | -49.37675 | 2025-06-15 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 933f94b8-0286-3f32-aa89-3b3e96042b4e | -15.40547 | -47.88162 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 98c8712b-eb50-37a2-b3c9-dc9a7292370c | -17.34822 | -50.38086 | 2025-06-15 03:55:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dce1f81-738b-3b72-8471-e2525dcb64c4 | -12.97775 | -48.64391 | 2025-06-15 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9997b3c8-fe5e-3696-9226-52c84ac91b58 | -18.7486 | -40.077 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e70833af-c796-3822-99cc-918fc859b479 | -13.92409 | -54.61556 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1edf3ddd-875c-32ff-8b4b-95e6dde281fe | -15.32983 | -47.35819 | 2025-06-15 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24a72553-cbfd-35f9-b491-acbddaf505b0 | -11.77483 | -47.39068 | 2025-06-15 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8cb25dae-e5f7-3ea1-afe4-b64a5d3c084e | -13.28039 | -39.86115 | 2025-06-15 03:55:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b186e1f0-871f-32b1-afdf-bf798d4715c3 | -11.89416 | -47.46667 | 2025-06-15 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6def0ea6-663d-3205-9739-cbe0ed3aac2d | -12.69009 | -52.3987 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0a776b9e-f976-3675-b18c-8cd1bde71fa5 | -15.41008 | -47.88275 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43816a15-3767-3b35-8fb1-3d2c49241150 | -14.37923 | -47.81863 | 2025-06-15 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 263f4dcd-b3c8-3ebd-9ac5-7e58e0524dc3 | -15.40649 | -47.87627 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 36d95839-fe0c-3cc6-8793-cd0e59f625ae | -17.21903 | -40.85891 | 2025-06-15 03:55:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1da1e126-58f2-3822-b68c-8b2fd5f53949 | -15.39716 | -47.87456 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc6f08a8-be8f-3b33-afd7-e4b8dd6fc570 | -17.78067 | -42.80862 | 2025-06-15 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2eacabb-0a77-3755-a170-7681243c1a14 | -16.34989 | -43.69445 | 2025-06-15 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3656c735-d7de-3ad6-8f64-201e3a983317 | -14.83339 | -48.43425 | 2025-06-15 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 555612c5-3174-34f9-9dfa-d27b9003fe76 | -16.28403 | -52.93856 | 2025-06-15 03:55:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f3d90f4-eb1e-31e8-ac26-34e924496969 | -13.22406 | -49.83567 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2a78859-ca3e-3b53-a7cd-05b78740bd52 | -15.40574 | -47.85506 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa7d693f-c182-3853-a947-d240e9a1d862 | -16.28519 | -52.93316 | 2025-06-15 03:55:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4de4208a-5af2-3bb6-a86a-20300cb09716 | -15.40848 | -47.86592 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7f629a2-bce9-37e5-a6fd-d3b2b8e8d6ce | -17.23747 | -43.62405 | 2025-06-15 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96bfa82d-ea09-3eef-bb69-aca465129878 | -15.56011 | -42.62543 | 2025-06-15 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| efcc5040-f27c-3bd2-b283-2c4caa340f43 | -19.71632 | -40.35276 | 2025-06-15 03:55:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39b980bd-8600-3879-b0e1-2f64e8e03f7f | -17.77727 | -42.808 | 2025-06-15 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd3520a5-555e-371b-b946-073775b18976 | -14.83819 | -48.4356 | 2025-06-15 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 90f2783f-e58a-39e7-90ee-40800871fe75 | -20.34706 | -40.36031 | 2025-06-15 03:55:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e0b8adc-460d-388a-aa90-fbcc9165afc2 | -10.51064 | -53.58432 | 2025-06-15 03:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 38be5783-ae82-34c2-843d-dd5d27fa6ef0 | -15.57028 | -47.8561 | 2025-06-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13dc65e9-a00f-320c-8080-b1e724f8665d | -13.91792 | -54.60065 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 639f14fd-a15f-3fd3-947f-f54d33d3d803 | -19.43792 | -44.34155 | 2025-06-15 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908c4242-5d3a-3eb9-98ae-4340d1f3a65a | -18.39274 | -44.19116 | 2025-06-15 03:55:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94d9860d-3c61-3bf9-9fe0-3e39c4ede2cd | -13.22925 | -49.83596 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4d6413b-edc9-3cca-b6df-0fe66d92dd48 | -13.90193 | -54.60492 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4a0b859-e191-3263-a903-84f63f399d23 | -11.89037 | -47.46019 | 2025-06-15 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78ff57f9-4cb3-333c-9abf-c510b44ac87b | -15.40483 | -47.85979 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 560889af-9076-35c7-872c-db2ef626e4bb | -18.74917 | -40.07328 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 393e37d1-788d-3075-b31f-570052f4fad8 | -15.40114 | -47.85395 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2eb84799-d4cc-3c1f-8a72-630ddef760a9 | -17.75232 | -42.89487 | 2025-06-15 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b16575de-55cb-3151-83ca-86bb7f7657f9 | -17.09341 | -43.80547 | 2025-06-15 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0783715c-5275-36eb-8263-cd5491ca8f32 | -10.50346 | -53.58282 | 2025-06-15 03:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| be66f9cc-70d6-3548-90e9-b131875a18c9 | -13.92357 | -54.60906 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 88e36738-8c08-3e54-989a-856753721711 | -15.40943 | -47.86098 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 947cc19b-0648-3f57-bbd0-ee3d9b8e27d0 | -18.52925 | -40.2042 | 2025-06-15 03:55:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6762531b-a228-3b7d-b8ce-c43368bb1a6d | -14.82743 | -48.42753 | 2025-06-15 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a094a55c-3895-32fe-8ae1-61240346ebea | -20.31125 | -45.58686 | 2025-06-15 03:57:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f443448-a97b-31ec-b816-068e4427d3c6 | -21.26119 | -50.29791 | 2025-06-15 03:57:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7cdee5f7-28f9-38f4-aa36-72ae6a58b02f | -21.6704 | -45.53885 | 2025-06-15 03:57:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62c82ac1-b657-37ca-b3d1-bb77582f9e42 | -21.62612 | -43.46477 | 2025-06-15 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ae117a0-1ed0-3842-b4c8-f9d524e535b4 | -22.78555 | -43.75787 | 2025-06-15 03:57:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 602c0d04-1f34-3d0c-9c0c-5e594835d263 | -21.18058 | -43.98151 | 2025-06-15 03:57:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 98141b3c-0c96-3999-a1e4-826de9d08214 | -22.67678 | -42.85321 | 2025-06-15 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06cb37b4-bd1d-34b6-af48-0fea7ee4cde9 | -23.40431 | -46.55733 | 2025-06-15 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9640bde8-e2c1-3bc8-b845-f3a848ae86f4 | -19.83924 | -48.37509 | 2025-06-15 03:57:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b4a4adc-e190-3d93-91ab-ac6e53013a41 | -21.62547 | -43.46862 | 2025-06-15 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 026cbcb9-ddf1-39ac-b7bd-cda2cc27dd0f | -22.90172 | -43.75563 | 2025-06-15 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 386bf504-003c-350a-b919-87cb8f9e1501 | -20.25909 | -46.31563 | 2025-06-15 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d557d4d0-67fc-3923-afcb-b1452afff1ad | -20.8928 | -43.07487 | 2025-06-15 03:57:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 290f10af-9820-3913-9680-8974e8e43c36 | -22.40296 | -44.29377 | 2025-06-15 03:57:00 | NOAA-20 | PORTO REAL | RIO DE JANEIRO | Brasil | 3304110 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 575a52f6-e1d6-30a1-b42d-149063f6c401 | -20.76532 | -46.76734 | 2025-06-15 03:57:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbd4b3d6-8f84-3191-86e9-d2c618e274e2 | -9.4158 | -48.4504 | 2025-06-15 04:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b68dc4ce-91db-3ffb-b88f-93f5af9d62e4 | -13.9059 | -54.6291 | 2025-06-15 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e82e6ab1-5542-3d72-adf0-24cf5abafdc7 | -13.9254 | -54.6063 | 2025-06-15 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 851b7d17-7126-3955-8ab8-8b24e230d846 | -13.9251 | -54.627 | 2025-06-15 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 63d6f4b6-acc7-310d-909a-4f7df47ab4b0 | -13.9062 | -54.6084 | 2025-06-15 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 211.5 |
| e5f90900-40af-3df2-8d5f-d3a94185b1a1 | -13.9059 | -54.6291 | 2025-06-15 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 0245713f-8a47-35f3-8543-024f1d01557b | -13.9254 | -54.6063 | 2025-06-15 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 161.3 |
| d99da09a-c625-3e20-9238-e9d51c913ec7 | -13.9251 | -54.627 | 2025-06-15 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 91220e83-af95-359d-9ef9-5274c68ea4f0 | -11.0113 | -55.0764 | 2025-06-15 04:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| eaa2ca9c-dd81-3ce8-a6c9-7666d85ab062 | -13.9062 | -54.6084 | 2025-06-15 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 180.2 |
| a651cf58-cebc-391d-b819-e7e7a3f9731e | -13.9254 | -54.6063 | 2025-06-15 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 44cd2594-8367-3d53-b96f-6200b6bbf8c6 | -13.9062 | -54.6084 | 2025-06-15 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 648a492b-840f-350b-bb97-43c77dff8462 | -13.9065 | -54.5878 | 2025-06-15 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 775fd343-8000-3b9a-b7c8-a95fca4b1888 | -13.9059 | -54.6291 | 2025-06-15 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| fbbaf3af-626c-31a2-a350-9e0db3e73787 | -13.9251 | -54.627 | 2025-06-15 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| a5c7f8bd-c3a5-3b17-915a-ab9c9e3acfed | -13.9254 | -54.6063 | 2025-06-15 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 65c362fd-d73c-375e-bcb1-1a977e3afc5c | -13.9062 | -54.6084 | 2025-06-15 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 941da386-b855-34e5-8d4e-ba7168654031 | -13.9251 | -54.627 | 2025-06-15 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 86ef7119-ad4c-3695-a5af-22799a40a733 | -13.9059 | -54.6291 | 2025-06-15 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 459feda8-0c80-34ff-b6e2-5cb0fe933fd4 | -13.9059 | -54.6291 | 2025-06-15 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ae60798a-1dd0-34dd-8631-25b98c50972b | -13.9254 | -54.6063 | 2025-06-15 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 172.3 |
| e1736515-4d27-3378-ab47-9049b457c9a0 | -13.9062 | -54.6084 | 2025-06-15 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 4b39cc4b-8cb4-3f67-8ebf-e4ac973bdba3 | -13.9251 | -54.627 | 2025-06-15 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 35f84e3d-692b-35de-a106-2c8401fedfd7 | -5.62257 | -44.00037 | 2025-06-15 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README8.md)
