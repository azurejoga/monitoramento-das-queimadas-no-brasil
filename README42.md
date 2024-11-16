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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d260d3-a123-3856-a9d8-1f6dcb8f7651 | -2.40198 | -50.32207 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c324f663-22ab-3081-aded-634994047157 | -2.56808 | -54.42696 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ddb1712-49e7-3b8b-87f5-645992143da3 | -1.13444 | -54.10287 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4186baac-44db-33ca-84fb-ecceb9e93fdf | -1.15642 | -53.50879 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9529f400-be90-3caf-865a-68bec9fed94b | -1.57882 | -50.44204 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51b58d7e-a7c3-3e31-908b-93aa3fcf5fad | -2.08472 | -48.95391 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb369d5c-2d85-3146-b6e5-e6117c437c54 | -3.33775 | -45.15646 | 2024-11-16 04:48:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6586dde9-3d49-35bd-84d7-cbceaf5cddd3 | -2.37419 | -50.41248 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58e8f196-15c1-3691-9299-e24418a669c2 | 0.66417 | -51.76237 | 2024-11-16 04:48:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5d2d477-65d2-3e7d-881a-892ddf4191e9 | -2.46406 | -53.92796 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 520fd19e-62fd-30b5-8cd9-c1f5b5fd5b87 | -2.59653 | -48.32689 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d17e6523-0661-3943-bf45-90721dcd886e | -2.18149 | -46.39246 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83b1ac4d-24c6-3e7b-b0e9-114562392a04 | -2.20432 | -53.71101 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 472735f8-d22a-3203-8648-7bbd23310302 | -1.86325 | -54.28149 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1bb2f4e3-420c-3cd9-91db-9e9bd7e5d06f | -2.21894 | -47.21148 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4fba9cc-8909-30b0-9445-3173f2f2f108 | -3.01701 | -47.97758 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf5dcb5b-61fe-3da6-a781-ba6f30499a28 | -2.81415 | -46.66331 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9366e695-3f56-3bf8-90c9-4c397cf58f30 | -2.93337 | -48.32573 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b836dd-d16c-370d-8ebe-b7641fd58852 | -2.71111 | -46.07013 | 2024-11-16 04:48:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42ede3f9-a947-3690-935f-b243aaacb23a | -2.5745 | -54.43204 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a4fb788-f289-3db3-96ee-650b04ea6397 | -3.73993 | -45.65111 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6d3c616-0021-33b1-9ced-98c0216d8b87 | -2.63422 | -46.55953 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b003b909-28ea-3cbb-8e56-7881d1795d26 | -2.59708 | -54.04145 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 100150c1-0468-3c52-bed1-1c4b45468157 | 0.89093 | -50.95537 | 2024-11-16 04:48:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f834b001-dcc1-3fe1-baaa-06941bf7018c | 1.20871 | -49.90949 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d88bb784-c601-34e6-9b81-73c6a9704651 | -2.4766 | -46.3643 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd737bb3-b7a5-37d1-94b4-365e0aa9b2ee | -2.62797 | -46.19173 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adc7114b-c3ea-3f73-995b-829c7d96ee99 | -2.38059 | -48.53839 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afbeec97-bfb9-3eaa-8a14-f0c80138c3b0 | -3.94694 | -46.70916 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2d3676-ccd7-388e-aa45-d1091ed04ee9 | -2.13977 | -46.55563 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8c0b53d-df74-332d-92de-49ddd25fb269 | -2.15393 | -50.51944 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 488f9c04-00f5-3eab-81ac-5e7d86587b20 | -2.62713 | -47.91665 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2eb03b3a-5e4c-3032-ab60-5f05c34f769b | -2.20716 | -53.71526 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5f6e01b-468a-33e9-8e89-b5beb9c7cf5f | -2.17555 | -50.46864 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ff05676-08bf-3abb-98fc-b00225a87fb9 | -2.18689 | -48.38751 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 307c90cc-e2d2-320b-ba96-1ccc86aeed40 | -3.98219 | -43.72167 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08eb84fd-5e34-3e73-ac21-40cbd62eebed | -3.73854 | -45.66101 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f01498f3-9730-3245-b308-383db5ce48a2 | -2.62495 | -46.18345 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1804fea1-cace-31ce-bb54-de8c76aa4249 | -2.66506 | -46.84652 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a207347a-ca8e-33b3-a9ba-cefd9dc14e2f | -2.14575 | -48.53444 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64ddd754-6b98-3125-b93a-0e7aeb139602 | -1.12472 | -48.35659 | 2024-11-16 04:48:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711d88e3-bcbb-3656-a488-d63d330c6840 | -2.82227 | -46.66454 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad498f22-2e23-30ea-8d73-13d0401bf986 | -2.66082 | -46.2004 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a62259c1-960f-3189-83a1-93e552004de9 | -2.66687 | -49.1195 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca022635-f607-38bc-a102-da4d6aa50aa5 | 0.84977 | -50.13305 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21a79f0d-bb9e-3da2-8b04-44989b0ae238 | -2.35314 | -49.11005 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c591d84e-0e86-304b-b81e-76cb89d63055 | -1.7177 | -54.85665 | 2024-11-16 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7c11069-5445-3a8a-af82-4ca3cb5b9327 | -3.03855 | -47.96235 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5896f870-7b99-350f-82ca-56edd950105b | -2.73031 | -50.87416 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16a5aeba-5070-308f-8890-a4bdf208d795 | -0.23917 | -48.57714 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdb2affd-48d3-3062-9b37-9dc6ed177207 | -3.95163 | -46.70592 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a62f1977-65e4-3f37-9c10-7ce89f00d472 | -2.66453 | -46.84998 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 315720a1-7bc8-3d03-bb59-33f63e91b112 | -1.655 | -50.49627 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f5ee553-5f44-3747-8112-78eea197e942 | -2.94723 | -48.02387 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08b0b58a-1368-35fb-8706-b6685cdce3ad | -3.73348 | -45.66464 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0740262a-5848-305b-b924-6a0451e3f992 | -2.66559 | -46.19722 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95e81d01-84a1-3ec6-ae32-ad74cef1980c | -2.45959 | -53.97775 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ee7a0a-0e9d-3e88-b660-8d7bc1bca5d2 | -2.15193 | -53.71177 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0335908a-1f3d-3c50-9408-639f283fbaa6 | -2.28863 | -48.18867 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd73f9c5-2cea-3ef8-b027-0944d4e9909c | -2.38716 | -51.22207 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1433048a-cc3c-3a64-9938-7d99a803ed2d | 0.24675 | -50.96514 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d1c9e6-823a-3862-a833-5640de6e9a60 | -3.12326 | -45.74545 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78b5ff8d-30bd-3a21-b10b-e7ce03685f8c | -2.2923 | -48.18921 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f16dbc6d-db58-35ab-94e1-ef3627b2737b | -3.94227 | -46.71228 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c33e276-dece-322a-a6ef-d62c95f5a935 | -0.64304 | -51.72652 | 2024-11-16 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a7dce39-674d-3a00-a521-0b42553bdffd | 0.1762 | -50.60318 | 2024-11-16 04:48:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6b93e47-498d-3826-b1b2-a3096332476a | -2.17784 | -48.75205 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f730d984-d5b1-3934-82e0-48d2040d4670 | -2.36195 | -48.89331 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c98d6a4d-15af-3847-bf10-bc8c0ebabb50 | -3.50218 | -47.21493 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 482e83b4-67ca-36eb-900c-d70eb91cdade | -0.65306 | -49.39661 | 2024-11-16 04:48:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ac59d6-07e5-3c60-994c-53767239d7a7 | -2.18701 | -50.32897 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e9375e6-973d-36ce-b314-2a7780503b6d | -1.21182 | -53.55992 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0e3c75-2d30-35ee-a63e-2a9b69fbcaa4 | -2.79145 | -46.64888 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f77b0780-ce65-3c0d-9fe3-d66fe0d1d484 | -2.66316 | -46.18523 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bb2514a-0603-352d-b576-c67162494ffd | -3.99926 | -46.50142 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4e5c2f9-ce1b-32cb-bdfb-b9829340cee7 | -2.62865 | -54.27806 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17055317-7a15-3d39-8e6b-c923096b00fb | -1.22985 | -53.70939 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1808ca94-91dc-3103-a293-47fd9299a547 | -2.61241 | -46.18155 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdeae934-55cf-3d83-bd93-a2aac085ca88 | 0.79552 | -50.73861 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4bc5317-d999-3375-bf4e-fa9132f7607e | -2.02394 | -53.94754 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9227fec2-2d71-3a2a-9eed-b6ceb8eb854c | -2.65246 | -46.19925 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a5ba297-cf1a-3712-8741-88978d786b2f | -3.73987 | -45.65236 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b505d54-fcd0-39f0-850c-b2692df0e94e | -2.7848 | -45.9556 | 2024-11-16 04:48:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0060553-834a-3ffa-a192-75e770f7a476 | 0.81787 | -51.13881 | 2024-11-16 04:48:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273ae87b-d7cd-345c-ae18-6ba6b4c3f099 | -2.35129 | -49.12175 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d01b2507-1544-31de-a5ca-a2da218951b7 | -2.22087 | -46.86494 | 2024-11-16 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f13dd663-3dde-370b-8a68-efda3c39c023 | -2.92907 | -48.06675 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca6071d4-de72-38f5-b88f-dc8bceb222f7 | -2.08548 | -50.48037 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6afefa-b8e7-3408-8be1-f04df2b520fa | -2.31805 | -48.91921 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24ab4dab-a9d4-3820-b71c-4836b15f2cd0 | -2.13801 | -50.8179 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14629ba4-3863-342d-96df-267bd6608b37 | -2.66617 | -46.19343 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddbcda41-2d12-32c1-a823-a10382892045 | -3.50143 | -47.22001 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d39a23ac-04b4-34eb-aa34-d82eebe20d56 | -2.08181 | -48.94942 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bcc03bd-c8e4-331d-adfc-d6634432a9a3 | 0.82117 | -51.13829 | 2024-11-16 04:48:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336efade-43a6-3902-aae3-140dbb8247f1 | -2.97238 | -47.99376 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd9f730-2e83-3673-a03a-16017e1511ad | -2.13306 | -48.78223 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d615aa39-3983-3681-aaa9-3602dc823059 | -3.78482 | -43.9125 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48285dc4-7de7-3857-9ba7-834a3e9d5fde | -3.12263 | -45.7496 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea8f4163-6d0c-3c72-b484-dbb270ccc751 | -2.5563 | -54.0396 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63ca1d35-b7d6-3343-a922-cf7fc32d0852 | -3.90332 | -47.16421 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README43.md)
