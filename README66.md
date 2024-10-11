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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77c0e3aa-fb9c-3a66-9fc8-7b0d54446d8b | -12.85216 | -53.48402 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 687daa5d-0c89-3c4c-9123-bbdbc57c55c6 | -12.84936 | -53.47538 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 019aa0cd-ff8b-3ce2-948b-e49460311ea5 | -12.84656 | -53.46674 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6eb5d59c-690f-3537-bbc8-bc8d10c020b7 | -12.84518 | -53.47459 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 86f54888-df4c-3419-b138-86db82710d21 | -12.84449 | -53.47852 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 237.4 |
| 0e7156f1-0331-33cc-a7c6-fbad851cbccf | -12.84238 | -53.46596 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c51f5795-242f-3ad1-902d-6008cba3f376 | -12.84099 | -53.47381 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9c625ddb-c792-3315-a2b3-b02cc4b4aa69 | -12.83889 | -53.46128 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f597bfab-3193-3a13-b10b-e41acc0b1e88 | -12.8382 | -53.46519 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1311e6-fc8f-30a5-9b6d-ffede48ae908 | -12.83751 | -53.46911 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86f697ec-6f5f-3b3d-809f-bd2361d1ab3f | -12.83542 | -53.4809 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2971901f-f0e7-3f1c-8d97-19d4780fc1c7 | -12.83402 | -53.46441 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80263180-eb64-3fad-8b2d-a3738ed7c85a | -12.83123 | -53.48014 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2d055341-f3e9-3b8c-950f-cb992dcc8620 | -12.82914 | -53.46757 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dde9960-f588-3202-915b-ee3e7d5ce83f | -12.82844 | -53.4715 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 672b3b7b-fedb-3c4b-9ea3-c121d1a1c92a | -12.82775 | -53.47544 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f7514e-46a6-3993-bfbe-b950a69c88c1 | -12.82705 | -53.47936 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ce06886-6dff-3a56-9abd-44046490cca6 | -12.84445 | -53.45424 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2055533a-a15b-3b69-8fa7-6e615d584b7c | -12.84379 | -53.48245 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 237.4 |
| 3ecfe6a7-ab87-35bd-a11e-99420789187b | -12.84376 | -53.45814 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c0460ac-d4dd-34fb-a60b-a0799f3622f1 | -12.84311 | -53.51087 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24a1df1d-35af-3721-a975-2ae1998af739 | -12.84307 | -53.46204 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 15b584bb-f3fc-36e4-8047-191563f36028 | -12.84241 | -53.51485 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 527ef163-7dae-3e1b-b539-e8e71846c9b5 | -12.84169 | -53.46989 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6a00e5d1-4d23-322e-ad04-131df8c5062d | -12.84101 | -53.49821 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 26b830a6-7bcf-3d31-a884-a6b59723e5a9 | -12.83962 | -53.50611 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 584d2141-3da3-3096-acf8-a8100f914bd7 | -12.83958 | -53.45738 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c135c758-65b3-35b0-896c-2a7b1cf6b802 | -12.83891 | -53.48561 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 333.3 |
| d203ceed-dac0-3968-a707-fac39b17d271 | -12.83822 | -53.51406 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5332cb27-0787-3979-b861-a82d2618bf1f | -12.83822 | -53.48954 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 333.3 |
| bb269ef7-b57f-3e90-a066-00d6d998f742 | -12.83681 | -53.47303 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e18e289-0288-3f73-b377-3d829d6e907f | -12.83613 | -53.50137 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 709d0a5c-a828-3714-aa97-4435f959b798 | -12.83612 | -53.47697 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cdc01c91-0529-3ef2-8c14-0c266cbeae50 | -12.83543 | -53.50533 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1665a6c-2968-3433-bacf-fa816a3934ac | -12.83473 | -53.48483 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8a47f1a-cfa7-3044-beaf-078462349767 | -12.83471 | -53.4605 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b195b2e7-3aae-3ca9-b2d3-9d27c5ed63ac | -12.83332 | -53.46834 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa3ab16c-e917-32f5-8b45-a4cbb4f627c5 | -12.83263 | -53.47226 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1eec28dd-a8c8-3872-b9a2-1aaa87f2271f | -12.83193 | -53.4762 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2199532-ee57-3912-804a-7a7a91ac4a12 | -12.83054 | -53.48406 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b5bf7974-3b25-3edc-bca4-1bb0438af0bf | -12.82984 | -53.48799 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f645bfa-793c-3adf-93e2-14606e0e5fb5 | -12.82915 | -53.49191 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ea583f6-7893-3226-ac65-b7a5d88b0685 | -12.82845 | -53.49585 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 549372f6-2a21-3d0e-8526-dd34a0547196 | -12.82775 | -53.49981 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e2c43b4-e405-30ea-be1f-34bd4581675c | -12.82704 | -53.50377 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26d20797-f7d9-389e-8504-c3741a14887a | -12.82635 | -53.48328 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e99ee6-2e61-32d0-a475-05287fcf947f | -12.82634 | -53.50774 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df62507-90b2-3b16-bf84-dd9417ca73f3 | -12.82496 | -53.49115 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de77192a-77e9-31f2-a4c6-f98cf4c752e3 | -12.69443 | -54.12035 | 2024-10-11 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de4e5c6c-235d-325f-af75-8f5169c718c4 | -12.69005 | -54.11955 | 2024-10-11 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285c4023-114a-356a-ab27-4646582c3885 | -12.41498 | -53.158 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f334282f-2813-36cf-bd3a-5846e0520e09 | -9.16698 | -54.67033 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bf48506-4008-31b3-ad0f-c6a7c43f5bb3 | -8.88673 | -54.58836 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f749ac2-b49b-3884-b03a-63b5391c7154 | -8.70086 | -54.84051 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5397340-e273-39dc-b12a-aa72cad83548 | -9.02489 | -54.53241 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 917c1873-d586-3f21-abd6-0c94f1a0f0a5 | -9.02011 | -54.53141 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad46461d-c869-3ae6-af3d-562b41e4c8bf | -9.01336 | -54.51395 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74bdeedf-7c49-38a7-acdd-1d08c0e6a1fc | -8.89348 | -54.57853 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50996500-3402-3b0c-8aba-9f260a50c2d9 | -8.88866 | -54.57771 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3881761-d398-3493-bb8d-6363a8c423be | -8.88771 | -54.58294 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 929cb269-5da8-3a45-b200-22c5646820ae | -8.75955 | -54.74816 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19b410dc-abcc-32f9-b05e-23a7f890d50b | -8.70207 | -54.84165 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a3a281f-1dd7-3b15-9994-3f878e72541b | -9.49209 | -54.53566 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cf96acb-09e3-3548-8a3c-cfc4b2c55dfc | -10.46963 | -54.44272 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02d8df1e-e00d-3c1e-97ca-004f4a80e032 | -10.31024 | -53.70825 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91b27e7e-60fa-33ad-82f9-9efa06c4342d | -10.30752 | -53.70461 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172813b0-5a97-34fe-985c-742185c51b66 | -10.30674 | -53.70904 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6680f27-2944-30cb-a9b3-b0c9f6a23113 | -10.27112 | -54.26008 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ea6d3c-205f-371e-8b17-389ff1ddafc2 | -10.22213 | -54.27339 | 2024-10-11 04:25:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 920fb483-c708-35c7-88f4-a13e3383401d | -9.49684 | -54.53653 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec71817e-c516-304f-af9f-22c8f977454f | -11.61306 | -55.01854 | 2024-10-11 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05feb103-c70b-3da4-9ea6-3b8646e31444 | -11.6121 | -55.02365 | 2024-10-11 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4820a70d-b21b-32c5-8605-7fdf612d886a | -11.61152 | -55.02245 | 2024-10-11 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95a8b5c5-4e28-3aac-87dc-a9235b1a18dd | -10.23094 | -36.36166 | 2024-10-11 04:25:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a73bc63f-b7e5-35f5-9608-634bb87c9ad3 | -13.05 | -39.97185 | 2024-10-11 04:25:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1b79121-d7df-3cb9-9c9a-1a8ec55600d5 | -14.00626 | -41.01554 | 2024-10-11 04:25:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 546fc202-cf62-35fc-bc2d-49c7328502fd | -13.88513 | -41.66357 | 2024-10-11 04:25:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ee14d4c-f493-3585-9f84-a15b87653722 | -10.80094 | -42.45135 | 2024-10-11 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c550572-d9fe-3409-9113-9598e7a87aa9 | -10.18607 | -42.44086 | 2024-10-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11182b6a-1bd4-3434-ac67-77f4ae5065a7 | -10.19393 | -42.442 | 2024-10-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81b6e248-5c86-3da2-bbc2-d7ccd63929d2 | -10.17752 | -42.44475 | 2024-10-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c3df433-d5e2-32a4-b540-bf9e398fa49b | -10.17681 | -42.44979 | 2024-10-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6fbf31b6-cb9b-3d41-8205-9c3996d18537 | -12.11924 | -43.17563 | 2024-10-11 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2488318f-48bc-3fe8-8757-a70e3a4318ab | -12.11776 | -43.17316 | 2024-10-11 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3acf4e0a-3e2c-3bb9-b3f2-bcb4c5d01808 | -12.11702 | -43.17831 | 2024-10-11 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6235b706-b9ab-3c6e-a347-6349194ebaf7 | -12.11539 | -43.17508 | 2024-10-11 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b0c21cf0-5895-3713-a155-3d1f23a32b46 | -12.11391 | -43.1726 | 2024-10-11 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7dea2304-36e9-3ad3-ba80-49b4c6d5227a | -11.21521 | -41.60608 | 2024-10-11 04:25:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 699a92a7-fa7b-3d06-b251-e4be496041f8 | -11.08471 | -42.30508 | 2024-10-11 04:25:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa1a0f85-2453-3d01-89a7-e4a6158b333a | -11.0133 | -42.87127 | 2024-10-11 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2d17840-7f69-3664-b223-74062f5aa5b5 | -12.48338 | -42.17255 | 2024-10-11 04:25:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 28a23f66-1baf-3de9-b32e-9e262190a766 | -12.47925 | -42.172 | 2024-10-11 04:25:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1786bb89-d8dc-3ace-ae71-a5b0a2d09c39 | -13.02177 | -42.66441 | 2024-10-11 04:25:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2ce0a87-3106-3608-9467-05015117b33d | -13.07547 | -43.37314 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bee1ff2-464c-3e2f-84db-07782e66a926 | -12.42992 | -41.79851 | 2024-10-11 04:25:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 300c2d19-d704-3884-9165-95155f0061c9 | -13.21646 | -43.04656 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 782832b1-43de-3d6c-aa45-efb1aeb81825 | -13.21558 | -43.04821 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf51dc20-15a1-3ab8-89db-0cd8cc19bbd4 | -14.72698 | -42.29615 | 2024-10-11 04:25:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cb1b6d85-3795-35cd-9138-261660ab42c1 | -15.12177 | -43.63143 | 2024-10-11 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91f0b5b2-7b05-3b1c-ad00-7516b7f24827 | -15.11787 | -43.63086 | 2024-10-11 04:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README67.md)
