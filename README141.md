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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b67d6486-1cf2-36fc-a9cc-0fa60c943a2f | -16.92432 | -55.83327 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 708276a0-8364-394c-bc65-3745960e9540 | -16.9235 | -55.84104 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d4c57e50-18fd-31c2-9c09-4506bdf93755 | -16.91949 | -55.82476 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d23e5f76-d0d5-31df-8924-b039c2ebf657 | -16.91908 | -55.82869 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 110dce77-b7d2-3fd4-882a-110823131f7e | -16.91729 | -55.82435 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0cee057e-0948-3dd1-b8bc-dd0bccd3f1fa | -16.91685 | -55.82826 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4c2565b2-eea7-3927-8b1f-aef7a210bce4 | -16.82343 | -55.9 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 620a7b45-104f-34e5-b37b-2a2f8a4e1020 | -16.81782 | -55.89931 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 518ab85d-b7c4-370b-9b5b-ca8c0c2667dd | -16.81261 | -55.89474 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8b4a3a36-1cfd-358a-9c84-10102bb38449 | -16.5125 | -57.73403 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8aa97ce0-c93b-3f3c-90f2-d1a234745ce8 | -16.51183 | -57.73978 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e9eddee4-f9c2-3931-9c72-478aeda3ac64 | -16.50687 | -57.73923 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e6e35bf2-3e3b-3c06-b269-86724a74101f | -16.42617 | -57.34161 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c9210f2-959e-34aa-a8b6-c72b358f6f63 | -16.42583 | -57.34464 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 48325991-6bd1-393a-a5a2-7319465787e0 | -16.42548 | -57.34768 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cc211262-6637-3200-a130-37eff50b9ed7 | -16.42249 | -57.34387 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b9c19848-ea1b-3307-aec4-ef83b8659ae5 | -16.42074 | -57.34401 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c68ecf1a-c356-3052-8102-281131f00f6a | -16.4204 | -57.34705 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 16f901e4-5f67-348a-9fba-3f64b8f4e7f3 | -16.41704 | -57.34629 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 71268381-c4a2-3a00-95cb-cb006d5d6a2a | -16.41232 | -57.34264 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9ef3a479-4295-31fc-9eba-03bff9829fa0 | -16.41196 | -57.34568 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c4f54fb9-9aed-3f5e-8ebe-7dca745bbd04 | -16.41057 | -57.34277 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7438a50f-e6b9-3a84-a4e6-3c650286178a | -16.41023 | -57.34581 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a29936a9-83a4-36c9-b67f-3d172824225a | -16.40724 | -57.34204 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2afca0c3-a284-3947-abe6-b187b94b6167 | -16.40687 | -57.34508 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8e38ea51-8559-37ad-adc3-bd9177fb9e4b | -16.40651 | -57.34813 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3f438deb-f5f6-39eb-8085-1c3c22d9074e | -16.40649 | -57.37922 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4d80a5d5-09b5-3e0f-98c7-f1f1edf4b5ac | -16.40307 | -57.37691 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8170aae2-f490-3864-b9c5-304406ae05d2 | -16.40143 | -57.3475 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 44cf35ec-3a0b-3395-8277-22424863a09b | -16.40107 | -57.35052 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| abb43e92-3b96-3be3-bb52-86258a9801e5 | -16.398 | -57.37628 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 348fdfe2-dbcc-393b-b2fa-4bc74906ff5e | -16.3902 | -57.35534 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a4b2cc8b-5567-31ed-ae39-5534e1565eb6 | -16.38984 | -57.35838 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7706636f-88c0-3b69-98af-5efb565387d1 | -16.38947 | -57.36142 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e3fdd43b-3927-37b0-9356-9b9567c1e64b | -16.3884 | -57.37048 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 82eeba97-ed5d-3839-abd8-3f265e7b84dd | -16.38787 | -57.37502 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f9aa1a37-9025-3417-8a1d-b2faf16e54e3 | -16.3844 | -57.3608 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d020084e-3f17-3b2e-91f9-2b14cc14f15c | -16.38333 | -57.36987 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c3c978e2-ba6c-3242-9e8b-3884bf724514 | -16.38136 | -57.38651 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 60ca8849-8157-37b2-b74d-0cac3edd08f8 | -16.37897 | -57.36323 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a729cafd-de5d-34dd-ad0d-6b3132899956 | -16.37861 | -57.36625 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| bea0cb89-e440-3836-a774-c607791dcad1 | -16.37825 | -57.36927 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 757f8b71-0755-3c1f-aa78-f729d7160f35 | -16.06525 | -57.53298 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8426ff58-5cce-3d39-b989-b5a48e69e700 | -16.06145 | -57.52653 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8eb867c4-fe69-338e-b4d4-4c3ad2d2ee3c | -16.06145 | -57.52185 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7de63856-abe5-301c-a626-4b9c2c3121ea | -16.06088 | -57.52684 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 953f3ace-d99e-38b8-aa4f-c7944dcce534 | -16.06081 | -57.53178 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b8af7a9-d9b9-3e1f-a7a1-89c6e38f9d99 | -16.52098 | -57.23812 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cc31a73c-899d-3cac-841c-07398efa14b0 | -16.52061 | -57.24122 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b8d2cba9-414d-3c58-9e49-97c9d4cef4c8 | -16.52024 | -57.24432 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e7148738-3b68-38da-853a-d3e672f34977 | -16.51988 | -57.24741 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 612cdfd3-f7c7-3f93-b141-e7d86b6dc4c7 | -16.51584 | -57.23759 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1bc89807-cfa9-3f7a-8249-5e4ed8da23cc | -16.51547 | -57.24071 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4f6eed3d-3004-3df7-abcf-37395dab2335 | -16.51511 | -57.24382 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a6c373c0-307d-39c2-8d66-98e99698612a | -16.51474 | -57.24692 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 30d36b9e-064d-3a6f-8970-e342d9fa5da2 | -16.51108 | -57.23388 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3b00e957-7ae9-3bfb-81fa-a47c8a799463 | -16.51071 | -57.23703 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 37f73076-3ed9-35b8-83f4-394e741cb9f0 | -16.51034 | -57.24017 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de8e3938-5472-3816-8d1a-896c4ca9f6bf | -16.50997 | -57.24328 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b6649ba6-5de8-3cf1-8554-aa4bf02c8a02 | -16.50961 | -57.24639 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4737bb2f-397f-37ad-b7ef-39e7bbbfdfad | -16.50639 | -57.27382 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ecb4ab41-59c5-39e2-9675-eb0fa67dc306 | -16.50521 | -57.23958 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 251b6eb5-b187-36c2-aca4-07241340a552 | -16.50484 | -57.24269 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c22ff803-18b2-3deb-afc9-bb773a3be022 | -16.50448 | -57.24578 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 02739bc0-6bc9-3775-a9ec-c18a6350c25f | -16.50413 | -57.24881 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 99d23ebb-d7d5-3bb4-b9b1-06e73f5f646c | -16.50378 | -57.25181 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| faf2c241-ae3f-3579-973a-0faceae33eb3 | -16.50307 | -57.25785 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d735cf74-e452-3850-b091-23ea116723c8 | -16.50127 | -57.27323 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7741ea1b-d0a1-337a-9369-8e32295ad22f | -16.49902 | -57.24809 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ee26d047-ca82-37e6-86ff-6e8204ac256e | -16.49867 | -57.2511 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 53417c06-7f00-3b42-9aed-325c54e7af45 | -16.49831 | -57.25414 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 08c08ea1-4285-304e-a01b-d8365051247c | -16.49796 | -57.25721 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b490a0d7-5281-3177-895b-b613048f55dd | -16.49759 | -57.26029 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c7bc0392-707e-3d46-ac95-7c01857dc9f7 | -16.49723 | -57.26338 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c1323f55-52d3-3bb9-a332-b386f00201cf | -16.49687 | -57.26648 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 391fd29a-ec7c-3457-a83f-c2ed52f32dac | -16.49391 | -57.24738 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04792c75-b1a8-3247-9cfd-9fa51f3c9408 | -16.49248 | -57.25969 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ef267694-9495-3973-a955-f0e216d27483 | -16.49211 | -57.2628 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d745a7e4-21a4-3cdd-877f-1a9b205a8969 | -16.49175 | -57.26591 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| afc802b5-8f5b-3771-9ab0-be8e7ce1e3ee | -16.48808 | -57.25284 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c500ba69-019a-3d71-8b53-e9506efd06e4 | -16.48736 | -57.25908 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4eda22a5-e543-3516-b315-a0e9afe8b6b1 | -16.48699 | -57.2622 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dbda6797-68ad-3d89-8994-6c4bc57c2f6c | -16.46407 | -57.28118 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f37a7801-cab6-3ebf-aaff-b3249076662e | -16.45931 | -57.27747 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e37b0dc6-d129-3484-8d42-188ea828a62c | -16.45 | -57.31361 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 283990e2-7865-3840-9bd0-0bc0fc7e534f | -16.44965 | -57.31668 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b68de9a8-4df9-314c-aee3-e9a346bf5b0c | -16.44526 | -57.30987 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| de26fe89-6465-3669-8998-0de27da5f5e2 | -16.44399 | -57.2755 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7d2ffa36-97bc-36fe-85b5-4c94090ec430 | -16.44365 | -57.27857 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dcb8f2ce-2e3b-346e-aabe-5222c3b29b79 | -16.4433 | -57.28162 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 93d6b780-0b2b-37d9-9a2b-7cbb5e92a40b | -16.44295 | -57.28466 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b037d06-831e-31b9-be96-9bf8e0189a1e | -16.43854 | -57.27792 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| da3f076c-2340-30f6-82fd-128b4133f150 | -16.43819 | -57.28097 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ce3c192f-b7d0-335a-8570-760e2799823b | -16.4375 | -57.28706 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f3c7e070-11e1-35e2-82c4-33e16407d112 | -16.43716 | -57.29013 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3ce728f8-a9ff-3981-b544-9877382c68c3 | -16.43378 | -57.27419 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0fce6dbf-b6db-3f30-9ad9-8e74027e2a5c | -16.43344 | -57.27726 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c3d618c5-f0a8-3639-afe7-fb34b79f72db | -16.43309 | -57.28032 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 24bdd563-96fa-3821-9d76-547409a1cd16 | -16.43274 | -57.28337 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 50b3835e-920c-3869-a9f1-8673af7a537b | -16.4324 | -57.28644 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README142.md)
