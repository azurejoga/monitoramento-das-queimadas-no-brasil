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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5734c483-4e7d-3dac-9656-ee5098737b27 | -12.4608 | -57.2079 | 2025-05-18 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 2bffa799-3170-3c06-9d49-d4e0b75f52f1 | -12.442 | -57.1895 | 2025-05-18 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5576cd1b-86b7-3058-9e4d-f852729ec346 | -12.4608 | -57.2079 | 2025-05-18 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 218.1 |
| 8b5ab53c-39db-389c-8aa7-2adb00711de0 | -12.442 | -57.1895 | 2025-05-18 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 160f4562-3084-379b-8cb4-a5c982bf9956 | -12.461 | -57.1879 | 2025-05-18 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 296.7 |
| 5b3995e6-2f4a-34ad-94b7-976f9c6dee45 | -12.4608 | -57.2079 | 2025-05-18 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 173.3 |
| fd4d3a02-d624-3a85-93ec-b5aa3ab9f397 | -11.4461 | -44.7215 | 2025-05-18 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 7d3837ef-ffc8-3748-9434-ac2c07a3be3b | -12.442 | -57.1895 | 2025-05-18 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c08111bc-daec-3725-b481-5785447b9cc4 | -12.461 | -57.1879 | 2025-05-18 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 343.7 |
| ba359693-6ea9-3b4c-a179-62cd7e93607f | -12.4608 | -57.2079 | 2025-05-18 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 2b1032b2-7fe1-3b0f-8429-7c6b047bb619 | -20.7425 | -54.409 | 2025-05-18 12:40:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a0630928-7d6c-3ab0-8dea-155079e071c2 | -11.4461 | -44.7215 | 2025-05-18 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f91fb978-5bd2-3b6d-b362-986e60d809f4 | -12.461 | -57.1879 | 2025-05-18 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 324.8 |
| cc96d048-28ea-32c8-9fb0-4d060c9e575f | -12.4608 | -57.2079 | 2025-05-18 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| b61653be-9f8f-3698-8e13-80f73bccbd41 | -11.4461 | -44.7215 | 2025-05-18 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| de03fe95-ed75-3484-8e12-0ff4d40defde | -12.461 | -57.1879 | 2025-05-18 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 336.7 |
| f0308850-0eb8-374d-8158-c7865fe67c2a | -20.7222 | -54.4124 | 2025-05-18 13:00:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 545d880f-f496-34ec-809a-9145193ce0c6 | -12.4608 | -57.2079 | 2025-05-18 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| f3a53d4c-0a18-3f2e-8d82-bcf26bec96d5 | -12.461 | -57.1879 | 2025-05-18 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 302.9 |
| 798fb801-8aca-3d1d-a5b6-315eefe8d0b2 | -11.4461 | -44.7215 | 2025-05-18 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a866c896-0557-3bca-9a53-042cdec7658e | -12.4608 | -57.2079 | 2025-05-18 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 23d06e26-abd4-3d09-af3e-056de62084fe | -12.461 | -57.1879 | 2025-05-18 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 268.5 |
| ab662632-fcaa-32a6-be25-cc09775ab1ae | -11.4461 | -44.7215 | 2025-05-18 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2e5275ca-0ae4-3ff5-8389-ebb11c8ddb1d | -12.461 | -57.1879 | 2025-05-18 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 247.5 |
| da418fcf-a9ed-3d51-a8ea-fa6da72d17b8 | -11.4273 | -44.7011 | 2025-05-18 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 2ba55ea3-e8de-31d8-94af-6103deda57ff | -20.7222 | -54.4124 | 2025-05-18 13:20:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0786a0f1-641a-3854-9884-b746a19ff1ba | -11.4461 | -44.7215 | 2025-05-18 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c83ade29-b4d0-3dcd-80a6-3ee5e0fb979e | -12.4608 | -57.2079 | 2025-05-18 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 637da7c7-1a60-36fc-8c46-ed5123723690 | -20.7222 | -54.4124 | 2025-05-18 13:30:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1899bd44-4b5f-3c40-975e-e15163583674 | -12.4608 | -57.2079 | 2025-05-18 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 52d72633-a9e0-3c1f-9c5c-fb1252027c41 | -11.4273 | -44.7011 | 2025-05-18 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 937ed1bd-6c93-38d5-ad29-4a474f874a93 | -11.4461 | -44.7215 | 2025-05-18 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8a5f67ee-6f2c-3250-be38-394a7cf41cc1 | -12.461 | -57.1879 | 2025-05-18 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 5a6e7381-d0e6-358b-8885-524d618a8e5f | -11.4465 | -44.6983 | 2025-05-18 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 598ddf10-9f03-3647-9811-5a9bf2b9ef68 | -12.4608 | -57.2079 | 2025-05-18 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 6e201f6d-4e51-35e3-8081-ef93e15a85ed | -11.4269 | -44.7243 | 2025-05-18 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4ea5a446-13ef-3144-83e6-467b4fc49b07 | -11.4273 | -44.7011 | 2025-05-18 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 642cdf54-b3e2-3830-9e38-7d8d1a7e5779 | -12.461 | -57.1879 | 2025-05-18 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 0fe0655f-b28c-3e5e-b66c-66c094608687 | -11.4461 | -44.7215 | 2025-05-18 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8078d88a-dd27-3b93-a6f7-80c13c0761f3 | -11.4269 | -44.7243 | 2025-05-18 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 49990a71-dc4c-3ba5-824f-2078057c4446 | -12.461 | -57.1879 | 2025-05-18 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 192.9 |
| b2bdb76d-fb5c-3434-9dd2-61b04e2db12d | -10.4831 | -46.5165 | 2025-05-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 3efb64fb-c759-310b-a96c-58c6b628f328 | -12.4608 | -57.2079 | 2025-05-18 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 7d91037f-4e55-3404-b325-609e68229f66 | -11.4465 | -44.6983 | 2025-05-18 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 91167dbb-be73-3b64-bc9b-621a542c841e | -11.4273 | -44.7011 | 2025-05-18 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 3ee6ff11-51f2-3e2b-840b-7afff045a06e | -11.4273 | -44.7011 | 2025-05-18 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 5316c608-308b-3d18-b525-26d6333f9a16 | -11.4465 | -44.6983 | 2025-05-18 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d209e414-6830-3c1d-a54b-11c1b43e3a04 | -12.4608 | -57.2079 | 2025-05-18 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| cea3805c-7adb-37aa-b208-a1cf0cee7107 | -11.4269 | -44.7243 | 2025-05-18 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 98e66c1d-76ac-3b10-af08-a2a5c969e4ab | -12.461 | -57.1879 | 2025-05-18 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| d16de507-60fd-3181-ab05-4111337da04e | -11.4461 | -44.7215 | 2025-05-18 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c9bfbbb2-3a7d-386c-9bd5-32ea1727594e | -12.4608 | -57.2079 | 2025-05-18 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| d0976cd9-1898-322c-9f6d-d55d951d3ff9 | -11.4273 | -44.7011 | 2025-05-18 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 225190fa-5a16-3129-9e0a-0ed927e196c6 | -11.4269 | -44.7243 | 2025-05-18 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 686e1a3b-db7e-3689-a8f5-e45aa57484bd | -12.461 | -57.1879 | 2025-05-18 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 3b5d37c6-ff61-3292-9da7-481f177cd976 | -11.4465 | -44.6983 | 2025-05-18 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8ecbcff1-138c-35bd-8eac-fb72bb15a567 | -11.4269 | -44.7243 | 2025-05-18 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 520611a1-34e4-30cd-8360-ce86a8d643bb | -12.461 | -57.1879 | 2025-05-18 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 0710a0a1-c3df-32e1-99c7-ac118871feb0 | -12.4608 | -57.2079 | 2025-05-18 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b87e5282-9d72-37f5-b2e1-4a1a7deec637 | -11.4273 | -44.7011 | 2025-05-18 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 76370f5f-0807-33b8-a607-5d9e16ae78ea | -11.4269 | -44.7243 | 2025-05-18 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7f6e85aa-0c25-33b6-b379-5f42f1b7f172 | -12.4608 | -57.2079 | 2025-05-18 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 25160c9c-e887-30a2-aaac-abe8a00527ee | -11.4273 | -44.7011 | 2025-05-18 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0c63954f-87a1-3aa6-903f-953fe0c16388 | -12.461 | -57.1879 | 2025-05-18 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 4c8db648-c8db-3dec-8d10-815c92575331 | -12.4608 | -57.2079 | 2025-05-18 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8bd8c7f5-51f0-33ae-92a0-76ae74dafd55 | -11.4269 | -44.7243 | 2025-05-18 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 83840d0a-bd07-3f52-8c63-fa3481ffa4ab | -12.461 | -57.1879 | 2025-05-18 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 6f12b6cc-0cc7-3d8c-af22-e169be3953f9 | -11.4273 | -44.7011 | 2025-05-18 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |


