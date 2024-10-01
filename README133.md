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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6adee0dd-e9b7-3038-9d2f-02ebaf653bde | -17.10586 | -56.23966 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a1dab697-23f4-3691-8279-4a104de2382c | -17.10529 | -56.24352 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9d849bbc-bb62-3986-aeae-27540119302a | -17.10414 | -56.2275 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a723714c-233b-3323-a252-1751a4dc69dc | -17.10312 | -56.40053 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6901ed9b-a573-3a3d-988e-75bc471e53f8 | -17.10187 | -56.24298 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5fbe90a0-3f40-3f80-b7e7-0bf24509dc7a | -17.08871 | -56.21316 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6f590920-b9e5-3f42-9291-c7924adef1d1 | -17.08815 | -56.21703 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9276d89c-dc67-35be-95dc-2236c9f373ab | -17.08641 | -56.20486 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 274a75d0-d2e4-3e54-ae4a-4d318ad0017c | -17.08529 | -56.21261 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 39fcafe0-5192-395a-a234-cd664a6c6898 | -17.08299 | -56.20432 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 444e0b68-a446-3b66-8791-417db6bee08a | -17.08243 | -56.20819 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0766b984-b297-3a47-9b77-dd6f6f4c2e6b | -17.07957 | -56.20377 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b7fb21b-8f45-316f-a23d-514e05028918 | -17.079 | -56.20764 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e9d813b7-8814-33d1-8ec3-878bfb260c37 | -17.0787 | -56.37704 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2c42026d-63f9-3d94-b98a-533d5e139e83 | -17.07814 | -56.38087 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1f06979d-edd8-3335-bfcc-1a2a328577b9 | -17.07474 | -56.38032 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cd091d49-af5d-3d96-b95a-a08dc301a7e4 | -17.06512 | -56.39834 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 72ea9b2f-7487-3811-92f3-88e5f9bf95a4 | -17.064 | -56.40598 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 832faa87-ef65-3bb8-aa00-e75363f86a93 | -17.06344 | -56.4098 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c010fa5b-9898-3dbd-85bc-4db621169c6f | -16.97674 | -56.21222 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a0b3249c-a949-3995-a59e-7431c86ba071 | -16.97332 | -56.21168 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 591beeae-cb94-36da-81ac-fb353e6262ae | -16.97102 | -56.20341 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e8ae73e-315b-3590-978d-8e4a0955da63 | -16.97046 | -56.20727 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fbd6ef8a-85df-388d-a17c-fb3bdc9c0870 | -16.9699 | -56.21113 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7bb372e-6470-3a78-9f7d-795518f9fc97 | -16.9676 | -56.20286 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d44addfa-eaa3-3850-8783-c3bfeaa1e08e | -16.9397 | -56.20261 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 73cbe777-e7d7-38f0-8227-7cf55ce4727d | -16.93913 | -56.20646 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1d2fa298-ab3b-33f1-bf31-4543f3c076ad | -16.93628 | -56.20206 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7a53ea6a-d616-38e1-ad34-c5cc7bfe937a | -16.93571 | -56.20592 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 64236826-731a-37ac-b1f7-f577f32b409d | -17.0891 | -56.11376 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 08424ab8-965e-38bc-b7ee-c3f5cca04de3 | -17.08566 | -56.11321 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b22b0e1c-1e0a-3a90-a898-008348e6ea01 | -17.0851 | -56.11711 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 69e4531d-10a4-314e-bd5a-936abe2e607b | -17.08454 | -56.12101 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 24d622d0-3e08-3ba3-88e3-6954eb5ecb0d | -17.08054 | -56.12436 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 590aa82f-dc4d-3172-a8eb-cd35a3f94761 | -17.07383 | -56.12446 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d83d6825-d888-3e07-b5b1-5c519654193d | -17.07367 | -56.12327 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7891498f-57fb-359b-8913-7114e8b3996b | -17.06525 | -56.11113 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 98d19c4b-f910-3e46-ad03-9842b70ea4ab | -17.0624 | -56.10669 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 425e651f-c2fb-3a78-9c34-fe1147127033 | -17.05896 | -56.10615 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 48fc8feb-010f-30c5-9947-5097e2bdb359 | -17.05838 | -56.11005 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ca2791c6-28f8-3de7-8f24-f1720d3c4b52 | -17.0498 | -56.09671 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dfe7cc41-6783-3efb-af3f-118aaecfacca | -17.04922 | -56.10061 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cf250f3c-0974-3c25-96d7-72577f7b846f | -17.02401 | -56.08063 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c5675416-0067-3672-914f-e81acf84cc56 | -17.02057 | -56.08009 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cd8ade0b-29e7-3913-99aa-bac5734beedf | -17.0177 | -56.07563 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8faf5750-376a-3656-b87d-32f7ecb6134f | -17.01713 | -56.07954 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 82c9aa08-319b-3c14-9e3c-862345c5c7fa | -17.01369 | -56.07899 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f6ad4770-922e-333a-a883-1c34af4cdba7 | -17.00795 | -56.07009 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f7f9a3fa-c216-3c99-94ae-5db856020802 | -16.97956 | -56.19289 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d47adbbe-642b-3fb5-89a9-6658948af3a6 | -16.97899 | -56.19677 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 751c8928-d6f0-31ee-b091-9d2f3b91f462 | -16.96474 | -56.19844 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dfe7f005-d9e5-3ff5-96a6-24693c878cc9 | -16.96294 | -56.16248 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cf56f1fc-537a-3c69-8939-5900f1763adb | -16.96244 | -56.19015 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1eafb67f-cafe-32c3-be5e-7361ce9ab6a2 | -16.94427 | -56.19543 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 371fdde5-11fc-3d57-9339-64a94cb75ee7 | -16.9437 | -56.19929 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f8b6158f-ad9f-376e-9301-c0dff8f58aa4 | -16.942 | -56.18715 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e4342093-7353-32ab-8204-b53d028457c2 | -16.94142 | -56.19102 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf7abdd7-735d-3569-87a4-589a6a7de1f8 | -16.94085 | -56.19489 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5d7fb569-8670-325a-a347-88700bc11b31 | -16.94028 | -56.19875 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e4181e02-268d-354c-94db-36e5603dfff2 | -16.93857 | -56.1866 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0807980a-5527-3346-a32a-cd4f8680e410 | -16.938 | -56.19047 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e8aa2c5b-e8b2-3f1c-816a-c0842bea86f3 | -16.93743 | -56.19434 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 73fc41ae-df04-358c-870a-b69b8a5b4d89 | -16.93686 | -56.1982 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 877c425a-f366-3687-8e82-26dcf4aac682 | -17.18283 | -56.21519 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 6214fcb3-877c-30dd-af94-e6d128dd5e55 | -17.18236 | -56.26664 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e574096e-57c0-3091-b733-c9cb03943e5e | -17.18109 | -56.203 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d87b1b3-7a74-3c47-b248-f3f170b18015 | -17.17996 | -56.21076 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e4a8ab92-8004-3914-9a26-1acaff11a2bc | -17.1794 | -56.21465 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7770420c-190d-318d-8a93-0cfdae7151d0 | -17.17894 | -56.2661 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e736222-1ae3-3a99-ab4b-3f5f2b80f710 | -17.17889 | -56.24232 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b0606d93-d8d3-3c19-a19b-6ce9044a2c7e | -17.17884 | -56.21852 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3134d1f7-1ee5-315e-a860-9515c5405f30 | -17.1771 | -56.20633 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7b2fbaaf-6aaf-3698-baf5-108d7d859a47 | -17.17664 | -56.25782 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2e75bdba-4f72-3923-bb9a-f5224a0b2798 | -17.17653 | -56.21022 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ea619fce-f7a0-3f18-8780-c6dbd2da1199 | -17.17608 | -56.26168 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 17cca10a-cc8b-386c-99ad-bc06b32aa5dd | -17.17597 | -56.2141 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2d32751a-6b6d-3073-b03a-dcee34c3fd9f | -17.17541 | -56.21798 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| cb7b7941-6f22-3d84-b734-330eee2ddc94 | -17.17485 | -56.22185 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8750e83d-39f6-3947-9c0b-484bc2c43cfa | -17.17367 | -56.20578 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f1d1f3dc-b7b4-36e2-9b3f-5b2418095494 | -17.17254 | -56.21355 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3ed147d9-3f92-3f9b-ac8e-eeb71b596c42 | -17.17199 | -56.21743 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3334d1de-c249-3211-a70c-2bc0ee0ee3cc | -17.17142 | -56.2213 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2a2e99b6-52df-3a40-9c51-2253a252ddbd | -17.17036 | -56.20633 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| baea8860-6e9f-3df3-b5ce-846fc3d3c684 | -17.16978 | -56.21021 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 52b01611-e756-326a-bde3-273f1b428425 | -17.16968 | -56.20912 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d4c0f404-c6ab-3899-b730-65c62888ead7 | -17.16921 | -56.21409 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fbb0c8d6-ef7c-30df-a363-9325a8f36c5b | -17.16912 | -56.21301 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3d05aa8d-a435-39df-9114-af770a8041fb | -17.16863 | -56.21796 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 32054690-3eae-3612-a51b-3cd5fbd97bd5 | -17.16856 | -56.21688 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2447886a-78d8-3c5b-8f7c-83f12fc12a42 | -17.168 | -56.22075 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3f9e681e-4ddf-3da0-af1d-38e53c7aae64 | -17.16751 | -56.2019 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1f772077-a202-36a1-8f24-2b33a783ff2e | -17.16578 | -56.21354 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e098839f-0b7c-32a4-a727-2fdbf99ccae3 | -17.16521 | -56.21741 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6d204b4d-e5a3-30d3-a546-54fe01fae690 | -17.1635 | -56.20524 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 013c18cd-a65c-37b5-bd62-da44914c7942 | -17.16293 | -56.20912 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| dcaab675-d5d0-3972-b7ff-d0be61c516e8 | -17.16236 | -56.21299 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 913168e3-c2c9-3211-99ec-bf5f3eee44c1 | -17.15893 | -56.21245 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6135a290-130d-3558-9be1-f56458e5f95f | -17.15778 | -56.22018 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4fba64eb-9495-385c-9837-753e07cd7735 | -17.15721 | -56.22406 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2c563dca-5f17-340a-aef2-9ba51d1ba69b | -17.15608 | -56.20802 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |


[Clique aqui para ver as próximas entradas](README134.md)
