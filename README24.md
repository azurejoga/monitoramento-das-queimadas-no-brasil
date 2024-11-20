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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3663267e-ecaf-3e07-989d-a67619976cfc | -0.91125 | -51.7805 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de19d84a-dba2-3adf-8261-fa8e62ae810b | -1.10232 | -51.74065 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be9b6479-ce61-3774-83ef-e69028340ae0 | -2.31866 | -48.85314 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99d6be4-f9d4-31a3-8f44-6c97f436c70b | -2.40186 | -47.02816 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 038e3e7c-74b0-30a1-998f-0043fdbc7938 | -1.87881 | -48.78955 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40340522-2668-3bc6-b7ed-b342f9011f02 | -2.31057 | -47.89719 | 2024-11-20 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bea7165a-6a89-33d5-91ab-758b61ed602c | -2.00015 | -47.68299 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9bffe00-a2ce-3d64-9996-bf13d14443bb | -3.62604 | -42.4022 | 2024-11-20 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2524d504-71c1-3545-b7a1-b74656146bc3 | -2.888 | -41.76245 | 2024-11-20 04:25:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 88e9040b-79e4-3b8d-b1e5-f982a8940f81 | -2.21904 | -48.41139 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9fb05b-666e-32f0-98a8-e2a6fd175d1e | -2.20837 | -47.20443 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e371a19e-7b54-38a1-babd-a877b1b726a3 | -1.65141 | -52.68805 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6acd61d-e1a4-3eba-aa63-ada93536f416 | -2.66178 | -46.60885 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adf7df6c-bb99-3dd0-b972-74369f031128 | -2.6416 | -46.218 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c70f2ca8-99b4-308e-a291-82441f8f7e74 | -2.26167 | -48.418 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d601990-79c5-3b7f-a21f-7a9b0f7c6f66 | -2.82529 | -46.67406 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cac6b85-3be8-3555-b0db-439e984d3d48 | -1.32533 | -52.39991 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 18c95ac7-2467-3fb5-a9a4-c3fe1ed1eea1 | -1.62429 | -52.58834 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7727aeee-aced-3eea-9233-fec67aafef83 | -2.89227 | -45.83459 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f265d376-8811-35ed-9bb5-414a1bfbbd54 | -2.68835 | -46.17926 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea5a34d1-4117-35cb-8728-97ddedfa93d5 | -2.54834 | -46.33469 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dae8dbf-3f25-3f33-a2cb-3960e2157c33 | -1.22033 | -51.793 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab44cd8c-c4f8-3455-80b3-96e0b0b6e9d0 | -1.77298 | -46.13839 | 2024-11-20 04:25:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 633eafda-226a-3f28-bd69-1546542a3d75 | -0.9387 | -51.72194 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab665372-db60-33c7-b216-ea04bbc68451 | -1.20234 | -51.76352 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e96fd6d-db0d-34f3-b536-a54e52a1575e | -2.24647 | -46.82876 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12a41d6a-9129-3e24-97b7-46f360b525a9 | -2.05149 | -47.73306 | 2024-11-20 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 768d924b-6269-35c0-a087-4c83d81cb17d | -2.68358 | -46.07975 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3274ae8-65c8-39ab-a9d0-537ecc0a6b90 | -2.77942 | -48.58044 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f606a2d9-9f9f-339c-91d0-73626a2d2ada | -2.35483 | -48.60446 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f41f354-955b-3057-98c9-44e7336ff2b5 | -2.5401 | -47.33349 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51e23422-7beb-3de3-a0f5-5f29288efb6d | -2.31596 | -46.86118 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bae97df3-1da0-3690-9115-78799b2bad65 | -2.62249 | -48.18015 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f950ffb-8623-38f0-ba8f-155775c4fd22 | -2.21973 | -46.479 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1820c29-b5da-3901-9667-b405c769b97c | -2.71191 | -47.97721 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfaf62e2-271d-3a4d-8448-28f5f5970aa1 | -1.09417 | -51.7349 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84be3ffe-495c-38b8-95b9-eaaaa061d65d | -2.65697 | -46.55441 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bfc52d76-bbf3-3742-9d39-fb508b10603c | -1.71036 | -52.49064 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 607bb5e3-6c8f-398f-bd06-aeaf42a559ea | -1.45312 | -52.66644 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 252f4d5c-dd4b-39de-8a76-213dccd9e165 | -2.0899 | -48.94623 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4502ad9-2dcb-3c91-b9d6-0d1fc2c8fea4 | -1.63053 | -52.40511 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6fd3b62-a1ca-34f0-bb5c-ef59f7affcb5 | -2.67479 | -46.80844 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3f67e54-c50b-3c43-aeee-7967da3796f0 | -3.00211 | -46.9572 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 241a22c8-48c8-3539-b43b-1ddb96dd058a | -2.71942 | -46.08879 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a4ca73e-6fd5-3204-856d-bb9a1ede8a69 | -2.50163 | -46.22117 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd9c9d13-31fc-3ff0-b1e9-c318914511f4 | -2.53801 | -46.20554 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5389025f-4307-37d3-8ebf-463addc09a52 | -2.32044 | -46.85455 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b307891c-6cf8-30fa-a3a8-d24f5f650f24 | -2.64937 | -46.23335 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ffed39f-2c2e-3ba5-b5a1-8ad62858a247 | -1.93674 | -52.99353 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef5fffa8-6db8-37ba-8a9c-0069657e36e4 | -2.13076 | -48.53018 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc375907-1b95-3908-a795-5dca9b6503e6 | -1.54849 | -52.26829 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f28e7bc-2509-3b96-9399-6fcf275c73e3 | -1.90743 | -53.33527 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ece560-740a-39b0-a6e6-cd7e0245e9e6 | -2.59882 | -48.30141 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b7f2e5a-5363-32ae-b5ca-94a1f923e55a | -2.00209 | -46.60632 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84a597f9-7ea6-3340-a7b2-7cc17e08433b | -2.54126 | -47.32619 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7ccc62e-b848-38f1-b5df-2a1f102048fb | -2.84528 | -46.67714 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6c1f7c-9322-3ae0-a853-c15d17eaf1aa | -3.08544 | -45.97008 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9316c527-a0f8-32fd-92b0-a1b3f1463805 | -2.6339 | -46.05094 | 2024-11-20 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5debd8bc-7afa-3b38-a55a-09eac1ee945b | -2.0344 | -48.08799 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| abcf112f-c359-3b08-9645-ada7cf699505 | -1.08172 | -46.77575 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e0ec86-16cf-370e-9695-ff62f33dc147 | -3.59408 | -43.62411 | 2024-11-20 04:25:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abc80362-2246-394b-9b12-05b2dfa2876d | -1.20024 | -51.77651 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c230db4b-a44d-3594-b40a-555ebcf06a14 | -1.23945 | -51.78711 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcce4835-a963-349a-8524-0abdde00c7c2 | -2.68858 | -46.24294 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0e83065-cfe0-38df-b5a5-80395c74b257 | -1.45047 | -47.11383 | 2024-11-20 04:25:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b72792a-71c7-3f83-b11c-b5ddf49a9481 | -1.33602 | -52.24426 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48cec1b-ce00-387b-83a2-7ecd3bebdec4 | -1.15868 | -46.86893 | 2024-11-20 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c62efa-e326-33e3-9fee-e18d38da67ca | -2.64269 | -46.21109 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31c248a4-9fb5-35d7-9a78-e97d505cd4ab | -1.90518 | -53.3365 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98976bd0-1208-3a60-9a08-ad8ce4ce51de | -1.46067 | -52.69183 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74f3186a-15bf-3e2d-b435-81a29f37d119 | -1.20083 | -53.67653 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c60d187b-8f37-3818-885d-6f013532524d | -1.64518 | -52.66687 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6049cb8-84c7-3f1e-bbd7-8661fa55af0e | -2.16489 | -48.34164 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46f1d2e1-3066-36bf-9b97-49cb734730e7 | -3.1501 | -45.90266 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7a434e-4c0e-30da-92eb-fe01268a6885 | -3.37567 | -44.42889 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1c0e47cf-a9ef-34d6-b36e-27d4c96cccff | 0.64115 | -50.57412 | 2024-11-20 04:25:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1168510-a673-3a51-bacb-17fd74539fd5 | -2.65931 | -46.23489 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387bcba8-33a9-3eab-9d6b-30e76ef10156 | -2.2691 | -47.86734 | 2024-11-20 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b8c5209-c288-3c12-91c5-03126ecde34e | -1.49557 | -49.68223 | 2024-11-20 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02d11294-cdfb-3e1e-8071-08c0e148b2c2 | -1.70731 | -46.2312 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d6b5065-a148-314e-9758-7cf1ee18d9a6 | -2.20442 | -47.20753 | 2024-11-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46fa4d67-3b1a-3845-8d5a-f8990df8ced5 | -2.11261 | -49.13531 | 2024-11-20 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d95a47-5fac-3b98-bb9b-d72acb74b0bd | -2.30399 | -48.49364 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| df696501-ceaf-3e06-b05e-15669832ac4b | -1.71298 | -46.67314 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9454815c-74b7-3f38-8608-d392eed8d459 | -1.21911 | -51.74391 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1307d60-7ae8-30ed-8704-8991d3c69f6e | -2.51646 | -48.36552 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cfbe2b6-abad-3606-a980-938cdb735f23 | -2.26229 | -48.41399 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09b55ba7-63fa-33a6-a4c8-63d6a90d39aa | -1.93593 | -52.99866 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d0ee94-21be-3bd3-a010-dbc03b73b832 | -0.9282 | -51.64487 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc65fa9d-c2e5-3ef7-adab-bb8a109222c0 | -1.7535 | -52.37136 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a23abe4-771a-34b4-bf1f-5f64140c3a35 | -2.64965 | -46.14503 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13e92e3b-071b-3cd6-81b4-51ac4145f954 | -2.6042 | -46.26176 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0695d7c6-107d-330a-b797-a574f3d6771c | -2.72818 | -49.34361 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bb63885-b1f3-3038-b129-41b10e1514ac | -2.31709 | -46.85404 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d21175-8781-32d0-890a-adbd61448804 | -1.22545 | -51.78938 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9593dfee-75f5-3708-83a4-0dd020acab5c | -1.14927 | -53.51982 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adcf16c3-296d-36a6-b78b-150377c574bd | -2.22306 | -46.47952 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab9707a-8b1c-3ab4-87dc-34800f831c8d | -2.36012 | -46.8643 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69dace3f-e405-366a-85d4-6d2cb277ae0a | -2.63428 | -46.5688 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90fac4be-0eba-3da6-8ae8-dcc53a77c7f2 | -2.68966 | -46.23603 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README25.md)
