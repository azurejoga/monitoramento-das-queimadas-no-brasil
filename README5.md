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
| 67b218e4-6fb0-3905-bbb0-ed47c2d41a1c | -5.06789 | -40.81637 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a19c2226-a4ba-3829-bd05-b9dd0575990e | -3.86803 | -40.6479 | 2025-11-28 03:19:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3336bcea-4208-335a-b95e-2befe58a5d9a | -5.36234 | -35.39101 | 2025-11-28 03:19:00 | NPP-375D | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a5c3f4f-69b5-3c83-92ac-225892f4e539 | -5.87916 | -35.38208 | 2025-11-28 03:19:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7a7a040-28b4-34c4-b33a-7e55576c0c3f | -4.94858 | -41.19207 | 2025-11-28 03:19:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a788f2f-4b22-366c-bb18-17658c08a374 | -5.06036 | -40.82081 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03d96d26-8bd5-37e6-ad5b-6e15bbc65228 | -3.08925 | -40.65403 | 2025-11-28 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 09660af4-601b-3fc7-8716-3503867213a4 | -6.79784 | -35.18471 | 2025-11-28 03:19:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 8383ef0b-8b6d-3577-bb68-74fcea7d24b1 | -6.79826 | -35.18329 | 2025-11-28 03:19:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 0d7c43e3-bea8-3c3e-8e54-144bf065dada | -5.06181 | -40.82086 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e62c986f-6da6-3081-aee8-2b390570364d | -3.0847 | -40.65841 | 2025-11-28 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b173e49d-b3b5-36a5-8b16-cdb2dfcae183 | -5.06832 | -40.82204 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7e01e6b3-f956-36bc-a217-b29f79d4c8d9 | -4.94749 | -41.19822 | 2025-11-28 03:19:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b15b36da-19b3-3fcd-965b-7b76a9d89b7a | -5.36184 | -35.39362 | 2025-11-28 03:19:00 | NPP-375D | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13f1040a-72f5-380a-9541-eb2362e649cb | -5.06738 | -40.82743 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a129a1ab-70bd-34b1-8346-c7aa53a0ec95 | -3.08826 | -40.65968 | 2025-11-28 03:19:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b34514e2-2687-3b46-acda-57dcfd9315d4 | -5.06687 | -40.82198 | 2025-11-28 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| eab93180-9920-3f13-ad29-e7b52491e350 | -5.36335 | -35.38441 | 2025-11-28 03:19:00 | NPP-375D | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3cc82c81-1e86-3485-8316-a913024c6e26 | -5.36313 | -35.38642 | 2025-11-28 03:19:00 | NPP-375D | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 68fd7c9b-4329-3edf-8d16-817564618c40 | -3.86246 | -40.64106 | 2025-11-28 03:19:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbd225f6-3499-3e66-903c-4bf07a8c239e | -4.9408 | -41.19709 | 2025-11-28 03:19:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 748556a3-503b-36d8-b950-75f321a1ae0f | -3.751 | -46.9388 | 2025-11-28 03:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| dbcc0429-620b-3b81-9430-1c06a36cd15b | -2.6181 | -47.3521 | 2025-11-28 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| a7eca7e9-9ff8-3e32-a9af-54a6c710dfa4 | -3.7694 | -46.96 | 2025-11-28 03:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 835c6e86-bfd8-3710-b2ca-ba3b3f76c70b | -9.3809 | -40.375 | 2025-11-28 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 45805977-040d-3e0a-8aa4-bf40c76d9ff0 | -3.8431 | -47.0666 | 2025-11-28 03:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 44848855-3ae0-3609-9b74-5bad901ff162 | -3.7508 | -46.9608 | 2025-11-28 03:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 146.2 |
| c2a6f0c3-ef57-3d45-9ff5-bad69823b829 | -9.4 | -40.3722 | 2025-11-28 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.9 |
| be586705-45b7-3567-b4bb-ae8964d31c8c | -9.3843 | -40.37496 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6ed6fe5f-d127-3938-8326-9e706909d49e | -9.3902 | -40.3761 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 0ebb9eca-40d8-376c-954a-ceeb1f0c17ad | -10.13945 | -36.13903 | 2025-11-28 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f0976cf-47e5-3ac0-801d-dd895a92e0b4 | -9.39183 | -40.36744 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 582f185c-55ed-30ca-8ab7-ee888e5ddd10 | -9.38858 | -40.38472 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 4a6799b4-1a49-35d8-af4b-e550688d41e2 | -9.39376 | -40.37424 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f25cdeea-2610-3751-961a-1b55a273ffc4 | -7.37178 | -34.91773 | 2025-11-28 03:21:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3fcca2dc-fb3e-3bb2-a5cc-beb2cdec1083 | -9.38675 | -40.36197 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b90bae16-7e52-3a43-82cb-8428d03a282a | -10.14385 | -36.1399 | 2025-11-28 03:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d8531e7-b6fb-3253-b5bc-abfddca97cb6 | -9.38511 | -40.37064 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b911ccb4-49e1-37a4-96ce-ce66f190da86 | -6.7887 | -38.34472 | 2025-11-28 03:21:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f5d3d3f-72a2-3384-a08e-d484f40e700e | -6.72099 | -40.81671 | 2025-11-28 03:21:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 284fdbe3-40dc-3fab-a20e-9b21aeddc833 | -7.37322 | -34.9193 | 2025-11-28 03:21:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6696bc8f-a231-379b-8f03-97ba8a7b2ac5 | -9.38003 | -40.36517 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b0f43162-518d-3a83-8419-dc3cfa9bfe53 | -6.72 | -40.82209 | 2025-11-28 03:21:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 36601e6e-0ea5-3776-b854-64465478778d | -7.37606 | -34.91832 | 2025-11-28 03:21:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d3a8e60-07ea-3d99-8982-3665e5dd8a74 | -6.78968 | -38.34409 | 2025-11-28 03:21:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10ac241b-85d2-34a2-8411-e79e30264dc8 | -7.70176 | -34.91681 | 2025-11-28 03:21:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fa2c92b0-881f-329c-ae8e-74c1158e34ed | -6.91948 | -38.62954 | 2025-11-28 03:21:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 13.5 |
| fd47bccf-74b1-3f3a-9828-1c7fcef28cba | -9.39102 | -40.37178 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 584f97b0-4833-3287-b991-7b2ea2a580cb | -6.72635 | -40.82322 | 2025-11-28 03:21:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0859ce56-e2ba-3348-a63a-ad238fab4ae6 | -6.92012 | -38.62594 | 2025-11-28 03:21:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d4a0f021-e54c-3cb4-a6cc-7a7c93f6a6ff | -7.45933 | -34.81524 | 2025-11-28 03:21:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| f57789a1-818a-3a0c-a9d0-dab7c9ac96aa | -6.78931 | -38.34125 | 2025-11-28 03:21:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4bb2210a-5b37-331f-98a2-232b8106deaf | -9.39292 | -40.37856 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7f4e41e3-1607-3c23-89b0-38318f90e1fc | -9.38939 | -40.38042 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 7eff9575-5e5f-3df7-ac68-d40726819ede | -9.38085 | -40.36083 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6e2df1f8-6a1f-3d18-a8f3-1aa7fb8a53b0 | -6.72534 | -40.82876 | 2025-11-28 03:21:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8c532f02-a5ee-37d0-b3ee-e2b640754b09 | -9.38593 | -40.36631 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ea0e3c42-44d4-32b7-8c82-9139afa7f5ce | -9.38348 | -40.37928 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 5c9f4103-b40c-3a20-8ff7-fd5d544cc857 | -9.38267 | -40.38359 | 2025-11-28 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 533321cd-bea8-3d1e-9bdf-c88e03c4feb0 | -6.79031 | -38.34063 | 2025-11-28 03:21:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4568d5a4-6cfb-334e-94fa-c22a19aaa8c7 | -7.2337 | -39.2099 | 2025-11-28 03:21:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 5b6fe50b-588f-3831-bf12-2ba82e07514a | -6.72734 | -40.81783 | 2025-11-28 03:21:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a047f3a-d69e-3b4d-9dad-ed2eb7a42951 | -20.4629 | -47.47853 | 2025-11-28 03:25:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b021a88-478f-36da-a82c-58b3112ae0bb | -9.3809 | -40.375 | 2025-11-28 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 84fa8bac-6c1f-3caf-a552-1e0afd67eb9f | -9.4 | -40.3722 | 2025-11-28 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 76d13dcd-d399-3863-b8cd-d09b48a69bbe | -3.7694 | -46.96 | 2025-11-28 03:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| de4dfa05-8a5f-3882-a65a-f48deb72b4f0 | -2.6181 | -47.3521 | 2025-11-28 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3bba393c-89e1-35b3-918b-c8ac2c439f62 | -3.7508 | -46.9608 | 2025-11-28 03:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3d63367d-f554-37d1-93a2-29717a247e45 | -3.751 | -46.9388 | 2025-11-28 03:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1e062a6b-973c-3b4d-bdb6-5576def0fd30 | -2.6181 | -47.3521 | 2025-11-28 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| d652b6df-bbde-3555-9386-a46895c7257f | -9.3809 | -40.375 | 2025-11-28 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 48bb498c-8644-3a17-b014-74c38487cf02 | -3.7508 | -46.9608 | 2025-11-28 03:40:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6d0e31db-8c48-3a7a-a565-54297a6518ec | -9.4 | -40.3722 | 2025-11-28 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| b04bd6f9-dbd9-3971-999e-1edd9a51f566 | -19.9973 | -49.9861 | 2025-11-28 03:40:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| d491c54d-771f-3a69-a654-44f7135d01e8 | -3.7694 | -46.96 | 2025-11-28 03:40:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5f022a90-1320-3311-8d3b-d9715042ed81 | -5.59877 | -35.63661 | 2025-11-28 03:42:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 247408ee-c1df-3828-9361-2b1ef101c882 | -6.91643 | -38.62234 | 2025-11-28 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 084e8a66-40b4-3f55-a99e-2f9e2b796df4 | -3.86562 | -40.64238 | 2025-11-28 03:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 36d16a7b-6c78-3534-9878-7fe9bd2b56fd | -3.859 | -47.03632 | 2025-11-28 03:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d826ba16-acd0-3f45-85d0-24d770c49fdc | -2.61827 | -47.35709 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 998c6ad3-924b-3f13-aee0-dfc61c0724c2 | -5.06205 | -40.81973 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 5b853727-8531-3c13-a605-ebd378264ffb | -6.91937 | -38.62713 | 2025-11-28 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 268fa73f-7c07-3e24-a26f-f80f592fcb52 | -3.46652 | -43.93958 | 2025-11-28 03:42:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b02f709-cb20-3349-b2d1-b6088b23c8ef | -4.94342 | -41.19518 | 2025-11-28 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a3834c6-a662-3e58-913e-b486ee2dd295 | -2.71583 | -45.22097 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 740dc6b0-6254-3222-a6d2-786459040453 | -4.95871 | -41.1843 | 2025-11-28 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e944e35-a6df-3075-9e49-8181c14953cd | -3.75887 | -46.95867 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 99ca20c5-043f-31f3-9869-d2bc28ffba28 | -6.72019 | -40.81889 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 012eba86-0c3d-3102-acb2-5a0c02c25c95 | -6.96547 | -38.53478 | 2025-11-28 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5ab4625-af04-3deb-a731-4687432f3e7f | -2.41823 | -45.74725 | 2025-11-28 03:42:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f33cae4-4245-33de-a261-c0a6da6cc691 | -6.72085 | -40.81505 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5596fe82-60a1-36f8-80a1-fb8a2653e458 | -5.06204 | -40.82537 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5a5dc05-bec2-3421-9bc0-fe3dddc5f4ab | -4.16645 | -43.75521 | 2025-11-28 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65b82e03-392f-34fe-b22f-5b7691b53853 | -5.66135 | -39.48609 | 2025-11-28 03:42:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31d02d2f-3b38-31d5-b04d-4992ab94fcee | -6.78732 | -38.3424 | 2025-11-28 03:42:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b359ea1-881e-33ea-8e06-c75045552591 | -2.61937 | -47.35059 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68b924fa-9650-377c-8f2f-8a9e5410a051 | -3.63902 | -44.87932 | 2025-11-28 03:42:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9685aa7-f69e-30cc-80d7-b28bc305c18f | -1.83969 | -45.52179 | 2025-11-28 03:42:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e3de3d0-1164-3a60-8af4-8717f57118d0 | -2.74135 | -47.13834 | 2025-11-28 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1db669d-eb87-37eb-aa22-04e7f13b2644 | -3.29204 | -42.42804 | 2025-11-28 03:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
