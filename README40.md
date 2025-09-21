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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23f4b7c1-5a44-3e7e-b6b9-870b4400839a | -10.2854 | -46.08049 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4638d914-0ecc-30c8-b64a-337a1d85b2a2 | -7.9323 | -44.09879 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ec7dbb8-bcea-3371-8755-5f331da27e17 | -14.43544 | -47.57893 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e2883ca-7ad3-3dda-bc9e-20865cdaef30 | -10.29025 | -46.08427 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8263a8b-9037-3518-ba1e-dc1de0ffb349 | -11.20464 | -42.19753 | 2025-09-21 04:57:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d5e8b660-4086-39bd-9e5f-fe1294b6f600 | -12.41599 | -45.12407 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2da419a-2a54-315b-888e-7ed50db6acee | -9.47905 | -57.93225 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4e41bd1-3f62-325e-a474-f27a00d9f56f | -9.48901 | -57.91687 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a728cc98-df1a-3acd-938f-7601fc331b5a | -14.47463 | -46.51264 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7486094e-ee90-3dbb-b196-1c90f0622c32 | -9.4246 | -44.71218 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8ad4038-3d97-3266-bcc2-ba6813ad6c1b | -11.40408 | -57.43793 | 2025-09-21 04:57:00 | NOAA-20 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c5ca8fe-9d35-319d-a5b4-30ed5228adc1 | -12.69933 | -46.84098 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55d10e49-2b8b-340c-90e5-80a4ff9f48d8 | -9.625 | -47.21207 | 2025-09-21 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92d3199b-4306-3e26-967c-4daed906ac8c | -12.71299 | -46.8419 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7dd30f-e5a4-376e-b178-5d3811ebc8d2 | -14.25584 | -44.38536 | 2025-09-21 04:57:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97129ac6-2d87-3542-afa8-6fb7b7ab89b3 | -15.82326 | -59.51097 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 25a0d0cb-816b-37c0-a703-a9a73c6e396d | -18.46465 | -47.24579 | 2025-09-21 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ff54e3-eff4-35cf-98d4-3bfa31731761 | -20.24734 | -44.36314 | 2025-09-21 04:59:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 68b62827-58d9-3369-9632-36f1b90fecf4 | -19.84919 | -57.29824 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8d79f473-cb72-3beb-995a-c2bf38e42b77 | -15.95058 | -59.42658 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c2fed54-219d-3f96-b49f-cb9560be3836 | -15.94054 | -59.43047 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 239d7586-ca72-3f5b-9240-1fb39d607d86 | -19.83809 | -57.30381 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 58daeb0b-8702-3575-86d3-3e895ce465c1 | -15.81886 | -59.51488 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6e3ad7c4-9314-397f-9230-ccb7d2f94b79 | -15.96997 | -59.42098 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aba0cde8-fc61-3150-a0ae-3cff0767eba5 | -15.95488 | -59.423 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 10a3fd93-801c-36e9-af0b-d1ef737c540f | -15.83047 | -59.51211 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aeaf20ca-8fd4-36b6-b8c0-9dba651029aa | -19.83651 | -57.29224 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f32b9f5a-3f22-36dd-b8e5-168b3e62a04b | -15.89629 | -59.40929 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d88c099-9220-3788-9ad1-bb0323cad248 | -15.94981 | -59.45217 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| def8c8fd-0146-3eb5-98f9-1fead53e8c0d | -15.94832 | -59.46067 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc358db3-fee2-37a2-afd9-772e7451720a | -15.93766 | -59.4257 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd9c52e3-8d65-3413-8cd6-3a4624f1a329 | -15.95699 | -59.43208 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d43211be-013e-3afc-b944-579483cca4e1 | -15.96713 | -59.41611 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2953a118-182e-342e-812b-529b1b3d5657 | -15.89415 | -59.40031 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 099a451c-f639-32d1-bd30-20efbfcd2e90 | -19.84861 | -57.3019 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1ef5a9e8-fd54-3333-9801-2b8e7585343c | -18.74701 | -53.32705 | 2025-09-21 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3404ac6d-d98c-3a73-a79e-f212f56fa89e | -15.82687 | -59.51148 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8be57bc-7043-3c48-8a39-88ac63dca718 | -19.28775 | -57.58442 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d2829326-6f33-3973-a997-54e0ed4391bf | -15.93129 | -59.44153 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2d94458-58e3-3c01-95e2-74f2381557eb | -18.74331 | -53.32653 | 2025-09-21 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72a39e88-d508-36f0-830a-df27df8fefce | -15.8181 | -59.51923 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6f9df083-06ce-36cb-835b-23774f803ff2 | -19.07588 | -49.00063 | 2025-09-21 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a985a1bb-7108-3c5d-9942-f4fd30b62fda | -19.73361 | -49.65947 | 2025-09-21 04:59:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9d80879-2ea6-3341-9dd2-017a72941bce | -15.90978 | -59.45959 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ec16880-2325-31d7-b641-90e2804e80f7 | -15.94193 | -59.42226 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c38bb4d-0b31-30dc-973f-f84612e2df2b | -15.96637 | -59.4205 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4522b2ae-3f69-3af6-a880-22c437c9752b | -15.97503 | -59.41299 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| edb409eb-66d2-327e-a798-ce5f44ac5af0 | -18.77042 | -53.34882 | 2025-09-21 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52bdcfcb-fa82-31bf-bd75-e3e58919c552 | -20.41864 | -54.68234 | 2025-09-21 04:59:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88cf764a-6fa1-333a-ad45-583f2a579728 | -19.73204 | -49.65779 | 2025-09-21 04:59:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1c5914b-7c83-30c4-9485-fb7ad6eba15d | -15.94985 | -59.43077 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e4a4b38-ac3a-324a-b394-503ff67728b0 | -15.89488 | -59.39608 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4b576e1-ba07-319f-a2bf-8038e45cdf19 | -15.9692 | -59.42538 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce73d89f-c8b7-305c-91a2-accdc3360d15 | -15.90259 | -59.45847 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a8ff6ff-1288-3a78-b054-c6403bcb8399 | -17.98972 | -44.04654 | 2025-09-21 04:59:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e875f57-36ba-32f0-897d-813f14e32746 | -16.1268 | -57.72651 | 2025-09-21 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb44b561-85a6-3f9c-bf91-5955bd297a4d | -15.94551 | -59.45566 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebee2ab9-3170-34ec-9724-b519a2db04e9 | -15.90541 | -59.46359 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b9c395-b919-322b-86e1-ca46c68a6788 | -19.83261 | -57.29532 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f9c16be2-8e60-3df4-926b-9aa0269f56ca | -15.95415 | -59.42724 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99866370-e817-3b28-ab0f-2da7582b6812 | -15.96562 | -59.42482 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce6799ba-5fb5-31a7-aca1-5e794e915d08 | -15.97715 | -59.42202 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4627f8d6-1378-30ec-9974-90ae094fdb22 | -15.94907 | -59.45638 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f28db2e-463f-3183-83a4-0ca0b431b5be | -15.9743 | -59.41719 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06b5d5f4-227d-336e-85c4-d584bffa621f | -15.81964 | -59.51045 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d0ccaac2-c6d9-3f2a-83fd-fb4f17b045f9 | -15.97072 | -59.41661 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55caa74b-29a2-3c17-926e-86bad7748652 | -15.94123 | -59.42638 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d6d6db4-a242-3a7f-80a5-31eae33c4e19 | -15.94473 | -59.46012 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 321d66a8-c216-3e2f-b4d9-138ae0b8a0ab | -15.95269 | -59.43562 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 713c4f8d-86c8-3949-aa09-db55f3aaeed0 | -15.92626 | -59.42782 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d76ffa8f-f997-3744-8bea-45400d68509f | -15.94417 | -59.42107 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10244f40-2b03-3604-85cb-790fda27fdbe | -18.739 | -53.33055 | 2025-09-21 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2258953c-13f1-3dac-b644-2b86fe2a3b9d | -15.89558 | -59.392 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d821aa53-a17c-3907-af3e-8f73266d2a1d | -20.4157 | -54.67758 | 2025-09-21 04:59:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6609daf-53b2-3793-97d6-1f48a85623f6 | -19.83982 | -57.29282 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7088d49-3411-3fda-a017-5ac87dc64e0d | -15.94345 | -59.42523 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574766fc-e0fc-33bd-b10c-cd20b1b5d856 | -15.90619 | -59.459 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86303758-06fb-3c01-ad01-1fb474c510ab | -15.88841 | -59.41227 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a481ee1a-d714-3319-bac7-5df1900235ff | -19.83204 | -57.29898 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3f6e1593-2d19-3368-90ac-f37fe0861a3c | -15.96415 | -59.43327 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67c73248-f16f-3b15-8e8a-765f596f83d2 | -15.9341 | -59.42505 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46f4fed2-4522-34d2-89ec-3ae03a75d13a | -15.94625 | -59.45141 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 608b17e0-ed41-3751-b0db-9f2adcc9d035 | -15.88913 | -59.40809 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034f870a-6136-3942-8e34-6b760a86216a | -19.8453 | -57.30131 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 356c5e4a-8b7e-37a2-86fd-797d080e01a7 | -19.83535 | -57.29956 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 60b1943e-5d00-3dc7-b75b-6387403a8214 | -20.41922 | -54.67816 | 2025-09-21 04:59:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 828cf6f3-fa03-3c20-82c2-b54b3e27f8b8 | -18.20246 | -56.4979 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c598d994-8264-305b-aeaa-990a27a0449f | -15.96488 | -59.42907 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b47188d6-0654-3767-8d12-c8dc591bfdb6 | -15.82247 | -59.51548 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2cf4e0dd-a1e0-3b2d-872a-f9775d67bdcb | -19.83478 | -57.30322 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c15de95d-a970-3f94-9afe-e7982c34f5c3 | -15.93199 | -59.4374 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb9f0749-ec54-37c6-843b-aa33b9554197 | -15.92484 | -59.43613 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f09414d-a61d-3503-8fc6-42067a01dab6 | -19.84587 | -57.29765 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cdcce6f1-304d-32f6-8e92-ac2fe884ec4b | -15.96057 | -59.43267 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b25dfed5-b0d2-35f5-95aa-fa61c5b61633 | -15.97147 | -59.4123 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e1469968-90f8-34a0-b6cf-dd018461b66f | -15.94551 | -59.4229 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| effa1549-6f52-321e-ae5a-aada3f155ce7 | -15.92414 | -59.44026 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 532ed292-5155-360c-b9bb-a0ccd2ff3807 | -15.82608 | -59.51603 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69eb002f-352b-33de-b0f4-5bb5be9f46be | -19.83593 | -57.2959 | 2025-09-21 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0f1228bf-f8b3-3ab6-9901-dad8b776975e | -15.9334 | -59.42915 | 2025-09-21 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README41.md)
