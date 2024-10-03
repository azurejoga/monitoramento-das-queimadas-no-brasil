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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 778f4c40-9f59-3b1a-9750-def396790f5d | -18.8797 | -41.24749 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eb8ffe20-3730-39e2-b057-bb695d82327f | -18.87764 | -43.62873 | 2024-10-03 03:38:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d1f1f1a0-4f22-3532-b2a2-998c6e7d88ba | -18.87224 | -43.63229 | 2024-10-03 03:38:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24e1134c-3173-38d6-aa11-90e8ccd07bf9 | -18.85286 | -41.80592 | 2024-10-03 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7293b03-8d9b-332a-890d-a4405da199ee | -18.85218 | -41.80957 | 2024-10-03 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c4a5b9d9-a692-31cd-8507-0503b0f6a72f | -18.8508 | -43.54932 | 2024-10-03 03:38:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0d3156ca-68bf-3c47-8b63-56bc2dddc3b8 | -18.84986 | -43.5541 | 2024-10-03 03:38:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 94545429-7d75-33c2-bf93-3f7405542dbb | -18.84416 | -42.92946 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6a01ae16-ad01-3c7d-89da-9d3433ba1a00 | -18.84329 | -42.93393 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 5fe407b4-b00a-3940-bafe-6a2fbafc0a85 | -18.84078 | -42.92363 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f6622b31-a08c-3a3d-9d5d-c4945330dc2e | -18.83985 | -42.92841 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34d22ee5-b2b0-35e8-9e52-bdda5f61e189 | -18.83896 | -42.93302 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3bebae2f-4bae-3d08-8b44-02a02fdc62b0 | -18.83645 | -42.92271 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 18b87b63-6795-32e0-9b5a-8d96d98b8764 | -18.83552 | -42.92748 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0ff3efa0-280f-3a00-99c5-f874a3f54234 | -18.83206 | -42.92212 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9889b3b6-e2a6-3ea1-b668-6e23edb479d2 | -18.83115 | -42.92678 | 2024-10-03 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6681fe54-d0f1-31ef-835b-7a6357ac8ca5 | -18.79089 | -48.00013 | 2024-10-03 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea59e0c5-2082-38e8-9192-5706256160e6 | -18.78489 | -47.99898 | 2024-10-03 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 13ea7939-73ac-303e-ae95-910e55f17b6d | -18.76452 | -43.38506 | 2024-10-03 03:38:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e9651522-bcd9-3c92-ad80-a5bf1aeff83f | -18.76362 | -43.38968 | 2024-10-03 03:38:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b2fec449-7ce0-365e-8631-5929456c105e | -18.62801 | -41.84213 | 2024-10-03 03:38:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 69b4712c-01c3-3d12-9594-1e9529af550e | -18.62395 | -41.84127 | 2024-10-03 03:38:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c63e94ce-328b-31b6-be7a-906d894f1329 | -18.61562 | -49.19585 | 2024-10-03 03:38:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ffb21f31-8f3d-3172-b7ba-577a344841df | -18.59947 | -43.92737 | 2024-10-03 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd85bf8-8ad6-396a-aebd-98add561928d | -18.59842 | -43.93254 | 2024-10-03 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa8ba01-8c51-3b6c-b987-92b3b65801d7 | -18.59736 | -43.93773 | 2024-10-03 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dc079c8-b700-3fe5-ba87-d5f9702687b0 | -18.59637 | -43.93012 | 2024-10-03 03:38:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f31a56b9-0aa7-343b-9d6f-6b07a446c7cf | -18.59557 | -43.39663 | 2024-10-03 03:38:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8122f77e-a144-39f6-bbf9-6998687be8bc | -18.59109 | -43.39564 | 2024-10-03 03:38:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 59486dbe-f365-3137-9a35-7d434509753c | -18.53996 | -42.24129 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 49e5bd5d-7f99-34d9-9ed1-e183ef4ae247 | -18.53919 | -42.24535 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ddcc0d30-2466-3ce4-8645-d7255595d364 | -18.53891 | -43.25785 | 2024-10-03 03:38:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72015700-6668-3da9-9e28-ecab280a2b4d | -18.53726 | -42.23272 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fa5f5f67-7bab-3ac5-b6db-18db8aff9ce9 | -18.53652 | -42.23659 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 82c026e1-9302-3729-81a0-cc2b246eb161 | -18.53575 | -42.24068 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b37456b5-5a5c-3fd0-a3f0-3d39813d8d2b | -18.53494 | -42.24492 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 77ccb2a8-6764-3aa0-8dac-0c953ff4b28d | -18.53412 | -42.24923 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 973275f8-485a-3576-a2e5-9b32c06286e8 | -18.53379 | -42.2282 | 2024-10-03 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 457dc0ff-5ba3-3e6f-97e4-125c2893fc88 | -18.53305 | -42.23209 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 36260ff5-08c7-34b4-ae52-66be1f6b98cd | -18.53145 | -42.24046 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 33352207-ca41-3ab2-92c7-c079fb3c7376 | -18.53062 | -42.24483 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2987afe2-8899-3b8f-b9f6-757d6e3b37cb | -18.52983 | -42.24899 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| b4269996-f41f-3fad-81f9-fcdc07007139 | -18.52885 | -42.23138 | 2024-10-03 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 059dabf3-4386-3ab4-8fe5-49c90209b3b8 | -18.52873 | -43.35654 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c3553818-485f-37cc-a44d-a5225c0c1059 | -18.52562 | -42.2483 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28bb9820-008b-3035-9d5f-0928d6079410 | -18.52466 | -42.23063 | 2024-10-03 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 56933918-f0a5-30ff-b8e4-028842e9bda7 | -18.5239 | -42.2346 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f66cc0fb-9892-3fc2-9824-cb7be1e1b346 | -18.51819 | -42.24179 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 86226be9-5d08-3f87-b7ae-cc9addc6e7a0 | -18.51735 | -42.24617 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a797116-2807-3885-af01-999cc4ee3628 | -18.51654 | -42.25042 | 2024-10-03 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46e2cbe4-ca61-3893-a187-449f59b01a16 | -18.50941 | -42.21975 | 2024-10-03 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 772341d5-3235-3bb1-81c3-8fd44a174c5e | -18.50907 | -42.21796 | 2024-10-03 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be57f2e0-2f54-3946-b592-ef69db097116 | -18.39352 | -44.01114 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9353a2c-711c-3ab2-85c8-83244909e50f | -18.38772 | -44.01569 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7ed5637-007d-3a87-82a4-1a76f095acd2 | -18.38466 | -44.03086 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fe3ee0b-42f6-3885-a5b2-7c4001f7a675 | -18.38366 | -44.02925 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f27212fb-e956-3192-a5bd-ae71a00c6f30 | -18.38263 | -44.03455 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e64d473b-5e3b-31ae-871d-c45f3ffaddf4 | -18.37988 | -44.03032 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18acf10b-ce27-3c68-9768-c3dd62c18574 | -18.37313 | -44.0332 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c7bf243-fd17-3d04-ac29-2371e98d65d5 | -18.34495 | -44.02734 | 2024-10-03 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f049b8d-e016-3d7e-bf87-f3380057c300 | -18.34371 | -43.04778 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d769a64b-19bc-32f8-b168-a9269333360e | -18.34021 | -43.04229 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0b48509d-1be1-3fa3-a518-f5cee302cd8f | -18.31585 | -43.23556 | 2024-10-03 03:38:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 81fdf148-06ac-363a-8582-5e925ae1b60d | -18.31395 | -43.23431 | 2024-10-03 03:38:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9c7ce8af-259c-34ab-8e5f-e1e93d4adf05 | -18.31312 | -43.23866 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d734aadd-4cd4-3c59-9942-db713c00cb62 | -18.31137 | -43.23473 | 2024-10-03 03:38:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e3cae71d-a55d-39b4-a1a7-f35c7442fea2 | -18.31048 | -43.23923 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| bf9bbe84-4d96-3c52-a1bb-65a8c620f45e | -18.30946 | -43.23357 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2ebfafd4-3a0d-319d-92e5-e606f697d0c2 | -18.3086 | -43.23807 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2fcf8ab3-5ff8-30fd-af8a-bab240628b57 | -18.29586 | -42.17269 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a25bd5ee-c290-3ba6-b55a-f460da120e6e | -18.29562 | -42.54172 | 2024-10-03 03:38:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a5bec98-4a55-3ccd-a6a1-edc180c83c9d | -18.29515 | -42.17639 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8cfc53da-399a-3121-aaa2-9f24d26a1d0c | -18.29509 | -42.17364 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 7b4b02e7-8b66-33b8-919d-a3e362bc37f6 | -18.2944 | -42.17736 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a8032ea6-5590-34a7-8573-85ca9cb30547 | -18.2918 | -42.1713 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d8c32e8e-c3f5-365c-a6fb-3f96088811a3 | -18.26502 | -43.03356 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a231b3c1-7e08-3179-87bd-b8d22699460f | -18.26416 | -43.03795 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 55a1dcc5-a57e-3e69-953c-9163ad81d1da | -18.25467 | -50.82516 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7bddc922-515b-3898-a08a-1cd88321e6f2 | -18.2496 | -50.81532 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53020c12-5fee-369a-ab01-16d65d72032d | -18.23675 | -41.82913 | 2024-10-03 03:38:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73247abb-815d-3991-ab41-daab466841e8 | -18.23605 | -41.83289 | 2024-10-03 03:38:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 36ba9e4e-e4c9-3032-bc95-3f7fba87a96a | -18.08476 | -42.64618 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| d4b0fe69-83e0-35b5-a5a4-0b0535cebbb6 | -18.08334 | -42.6062 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6043c31d-3e7a-34a2-930a-fb4d27e2c460 | -18.0805 | -42.64504 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 47f13ff3-6791-35da-860f-44bc424a246e | -18.07906 | -42.6052 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce86d9ed-7f79-36dd-936f-4bb71cf0277c | -18.07399 | -42.60834 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4ec1a0e0-89e6-326c-a33e-3e9679846d40 | -18.0716 | -42.62097 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dca9a073-773a-3902-81ce-0eb86e534411 | -18.07076 | -42.6254 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edef9871-f885-3eb5-bad4-38cbedb5da8a | -18.0697 | -42.6074 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bc16f813-cfea-3eed-bd6d-67ea3a8954dd | -18.06732 | -42.61991 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c859abc-435b-3026-9f2f-d6cca751f984 | -18.06651 | -42.6242 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 909b732b-bd07-3e46-8c0e-651d17100554 | -18.06536 | -42.60665 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 469753ab-80a6-3962-beff-8ccbefc2af93 | -18.06224 | -42.62308 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b8f13fb6-ff31-31a7-b05f-f608591db4f6 | -18.05799 | -42.62189 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a2eaf9c-37e3-3597-8b7c-8d805990515e | -18.05372 | -42.62075 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| beba0f6a-e9c2-32e7-bd52-f6f4e495f078 | -18.0529 | -42.62508 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2eb76da3-e549-35d1-9e93-b5e3103ed0f4 | -17.85752 | -42.88626 | 2024-10-03 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edaed80-d073-3451-872f-d346f6bcf7be | -17.85401 | -41.42554 | 2024-10-03 03:38:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1ab316af-18b6-373f-ac2f-55e1285ebfe2 | -17.85332 | -41.42928 | 2024-10-03 03:38:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eb8c8ef9-55c5-3ac3-a4ea-f3f446494343 | -17.85235 | -42.25512 | 2024-10-03 03:38:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
