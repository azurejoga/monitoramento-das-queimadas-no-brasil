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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41192dcc-32e7-3d38-a255-36c55de0b156 | -20.57968 | -56.03762 | 2025-04-03 04:44:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e53355fc-17a2-351f-88f7-0af040f8c185 | -21.48391 | -57.08442 | 2025-04-03 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c29bb99-9848-3b31-af34-10d90b9a4287 | -21.13074 | -48.67539 | 2025-04-03 04:44:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c775f625-ac67-3089-a392-a315cbc9a489 | -21.23042 | -56.25399 | 2025-04-03 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c53f35a-90c2-3918-9206-1d75e1caa503 | -21.35271 | -57.638 | 2025-04-03 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 70cc5725-f8f6-37bb-b909-d3ed092f843c | -21.35682 | -57.63491 | 2025-04-03 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 06723fb3-d22a-3335-8afc-77b55e7d3826 | -21.3566 | -57.63884 | 2025-04-03 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 72719f8a-fd4c-3e74-b012-db1d4b36b32c | -25.19226 | -49.32732 | 2025-04-03 04:44:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b5828a35-c76f-3e94-a20a-cc321e67f937 | -21.13038 | -47.80125 | 2025-04-03 04:44:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50180126-c9a4-3a2b-9824-2f77a8689914 | -20.5554 | -55.33804 | 2025-04-03 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d7b4728-4fe7-30ef-bf95-e8df5776b566 | 1.15176 | -60.54986 | 2025-04-03 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1af9c01-8cc3-30e9-b8d4-198b2b618149 | 0.82917 | -59.94687 | 2025-04-03 04:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecee8e63-f2e2-3e7e-8b23-87567c9b65f5 | -3.73022 | -53.78565 | 2025-04-03 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318eecf4-32d6-3d0a-b6b0-68cdb4cb737b | -3.7302 | -53.76387 | 2025-04-03 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68fdab55-5ef3-3096-a66c-f9f1d5fe0384 | 0.76858 | -60.10985 | 2025-04-03 04:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 344af2fe-8caf-3539-b18e-2edb1c295212 | 0.76793 | -60.10566 | 2025-04-03 04:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08f21fb7-47df-3274-8808-027277f510d7 | -7.29818 | -55.31522 | 2025-04-03 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67934f7f-ecef-3ed8-bce0-647fa01a8c24 | -12.55805 | -45.34232 | 2025-04-03 05:01:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19a50a03-c90a-3627-9ed8-29df7ab9dac5 | -12.55665 | -45.33876 | 2025-04-03 05:01:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 713e4d89-ca63-33e0-969f-881f7cdc20a6 | -12.55863 | -45.33736 | 2025-04-03 05:01:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9b5196a-0aa3-38ad-bfa4-10d68e5530f6 | -13.03774 | -45.09289 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f073e39-eab3-37e7-a3e1-50421deda8a9 | -14.1061 | -47.68557 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d548b304-110f-358f-a97e-0ece8acc4f8b | -16.02717 | -58.45931 | 2025-04-03 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 34b0fe7a-c420-3a14-b2dc-8340832c959e | -14.10103 | -47.69242 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26efaff1-160a-3306-a40a-a9e0f7fcc4ff | -13.03832 | -45.08763 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67d924aa-4ce9-3e01-a42d-d31f4b1c64b6 | -14.1069 | -47.6895 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f10461c-a7a5-3881-a470-349ad623214a | -13.03138 | -45.09213 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a56fa7c0-438a-3a75-9162-c99abfdd0586 | -13.03534 | -45.09392 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b23fd28b-e976-3d38-8932-fa4fdb0d369b | -18.13838 | -52.35737 | 2025-04-03 05:04:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 194012df-e896-301b-b9a6-8a9418762b57 | -15.80356 | -43.56726 | 2025-04-03 05:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7f1e164-21ff-3061-860f-29aa01747bec | -12.27239 | -63.79782 | 2025-04-03 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1736ecfb-64ae-3d45-a990-b9cf894cfaeb | -13.03594 | -45.08869 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9d24358-e0fe-3852-a6ba-f851f8fb5284 | -18.13415 | -52.35683 | 2025-04-03 05:04:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 970532da-f8d1-3aa2-8e3a-f89f8a6d9294 | -15.80647 | -43.57209 | 2025-04-03 05:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 178dc199-51e2-3738-b487-4af32960d2b8 | -14.1073 | -47.68602 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c9206f-c3d9-3dc1-b24c-281a292b949f | -14.1065 | -47.693 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31722d03-0d61-375a-b738-d3cd63916b82 | -14.10483 | -47.69602 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 179ecc41-0c8e-3d7c-8ad8-53d49aa0d9ee | -14.10568 | -47.68903 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a7deb0a-4f16-397b-af0d-1e58f452a596 | -14.10526 | -47.69252 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e0ba840-e5a9-31af-98cf-0ca42eef8956 | -18.13834 | -52.35872 | 2025-04-03 05:04:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 297f451f-ab93-3523-8573-629d204424aa | -16.03049 | -58.45988 | 2025-04-03 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bd28b1db-a121-3556-ba4c-9f746e89af93 | -12.27689 | -63.79868 | 2025-04-03 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9568e9f3-b215-3f8b-9804-95e6711455bf | -13.03473 | -45.09912 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c4f442f-90d3-31a9-bad7-dad55259dee8 | -13.03717 | -45.09811 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cde9cb8e-b066-38d2-bacc-1a0aecc35c77 | -15.80713 | -43.56481 | 2025-04-03 05:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07aa4371-b131-3e39-97e8-3f190d006ce1 | -12.56287 | -45.33954 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 803f5510-ba53-3712-8ad5-ebe010bfa50b | -14.87101 | -51.98396 | 2025-04-03 05:04:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaa55a18-ff0f-3997-99ce-1e8fe954db88 | -13.03081 | -45.09735 | 2025-04-03 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79d15a59-598e-3326-9d6f-2ccec864c50a | -15.60226 | -57.34479 | 2025-04-03 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64cd333b-b305-3bbb-8ef0-3e13574ff0b0 | -14.10143 | -47.68892 | 2025-04-03 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d060f34-f991-3151-9e3c-48015bbbbf63 | -15.80286 | -43.57452 | 2025-04-03 05:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e252809-b5a0-38f9-8f26-969ec8bc77ae | -20.55525 | -55.33529 | 2025-04-03 05:06:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6006bef-8a2d-3871-98fb-de5774080eac | -21.48718 | -57.08561 | 2025-04-03 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e8f0fac-77d3-3e60-8a6c-74f036c80a67 | -23.98044 | -48.91745 | 2025-04-03 05:06:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f404dd-e18b-34b6-85e9-fd8fe4f2a953 | -19.42505 | -54.78476 | 2025-04-03 05:06:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 430cb065-099f-38f4-8c6c-eaff5057894d | -21.23297 | -56.25321 | 2025-04-03 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a54dc0-5dae-34b3-aa49-36d998babc7f | -21.35422 | -57.63514 | 2025-04-03 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cf48fca0-6357-3500-a4df-7ffca85bdd91 | -21.12658 | -48.67558 | 2025-04-03 05:06:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fcddb9a3-71e2-37f2-b012-e0f81d79ff4a | -20.58177 | -56.03874 | 2025-04-03 05:06:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d729e88-9f13-3466-9f97-07a52c43a71f | -21.22943 | -56.25267 | 2025-04-03 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52521957-78ee-3c1a-959d-042dcdc5d966 | -21.4841 | -57.0858 | 2025-04-03 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f6106fa-d777-3c44-b04b-d12983b82a27 | -21.13218 | -48.67618 | 2025-04-03 05:06:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc7ffd0e-dd43-3bab-b9da-caa058c8e41e | -21.48469 | -57.08181 | 2025-04-03 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05517763-2313-33a0-b781-a59229445ca5 | -19.42724 | -54.78308 | 2025-04-03 05:06:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a9df184-98e2-3ef3-bdfb-ee4bc183b141 | 0.76492 | -60.10698 | 2025-04-03 05:53:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2f3e037-aaeb-3895-a72d-2c5b4467c12a | 0.76563 | -60.11151 | 2025-04-03 05:53:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c482febe-f178-35a1-b045-9e0a9b1caaa6 | 0.76945 | -60.10623 | 2025-04-03 05:53:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 516b10b8-56a9-3599-9ea5-4929595a51dd | -6.23753 | -48.05158 | 2025-04-03 05:59:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 79305ab2-fc7f-3932-b1c6-0d4d844e1a41 | -6.22722 | -48.05033 | 2025-04-03 05:59:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e78c5c4a-8d75-3755-a0d9-40b1f30f5eaf | -13.0335 | -45.0794 | 2025-04-03 11:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5f4b5a10-2d77-34e8-8b09-0a11bc587df1 | -13.0335 | -45.0794 | 2025-04-03 11:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f43f8df5-0bc6-3f27-ba09-207790d31621 | -13.0528 | -45.0762 | 2025-04-03 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9836031f-1c5b-32b4-ba97-902fbe4da8e2 | -13.033 | -45.1027 | 2025-04-03 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9ac50c3d-06cb-3941-ba81-ceff5e1cdb77 | -13.0335 | -45.0794 | 2025-04-03 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9866b154-9a4b-323b-bc4a-7653ab0a038c | -13.033 | -45.1027 | 2025-04-03 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 86421ca1-3207-3bbf-8fe3-27355083ecff | -13.0335 | -45.0794 | 2025-04-03 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 388479c0-3b9e-376e-87db-1c89392fbe1f | -13.033 | -45.1027 | 2025-04-03 12:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 18ef80c0-c060-3011-934c-2abd99c9fbd8 | -13.0335 | -45.0794 | 2025-04-03 12:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 84043484-0372-345f-adba-4fe1c00835e3 | -5.9709 | -44.6439 | 2025-04-03 12:29:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9d2f132a-0e1c-3876-82ff-8dbac0c2255b | -5.80456 | -46.19671 | 2025-04-03 12:29:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d39315a6-9716-3148-9126-1b3d972b76d1 | -10.35402 | -38.47383 | 2025-04-03 12:29:00 | TERRA_M-T | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| dd6e7d51-e5d0-3af1-8a67-af4eb25f0bbc | -7.71525 | -43.00412 | 2025-04-03 12:29:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3a950260-70fa-3a40-add9-5aea8f7096b4 | -6.23628 | -48.05005 | 2025-04-03 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 23e40f96-5958-37dc-8f51-432e8e72b62c | -6.23486 | -48.05956 | 2025-04-03 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1dd14a0f-d977-3b31-a405-b35a84506172 | -9.24351 | -40.93221 | 2025-04-03 12:29:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 7a8a0d1b-e74e-3474-b907-0897cbc3476f | -13.0335 | -45.0794 | 2025-04-03 12:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 6b68e8b1-58d6-3beb-ad3c-225098451e98 | -13.033 | -45.1027 | 2025-04-03 12:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 3d428ed9-0ab8-37d6-b935-61d59d166d57 | -16.86452 | -47.3371 | 2025-04-03 12:32:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28a5d28a-41ab-3c54-b426-fdbb46257ccc | -15.49051 | -44.38766 | 2025-04-03 12:32:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 9967c720-5b74-3c7a-a80a-973b2acd89ef | -16.29943 | -45.1017 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 74b11fcf-6858-3a9d-804e-4c37dfba3a21 | -13.04412 | -45.09636 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| fcafd39c-b2cb-327d-91a0-b3ada1728a7d | -16.38619 | -43.50056 | 2025-04-03 12:32:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ae48950-32f2-32e7-a815-650ac2e7dc58 | -14.67487 | -45.82798 | 2025-04-03 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 7e51ff4d-072b-32fa-b095-2534f8b074f7 | -14.10785 | -47.67192 | 2025-04-03 12:32:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb6d53f3-ff17-3759-a391-f6236cf7ce5e | -16.77614 | -41.13498 | 2025-04-03 12:32:00 | TERRA_M-T | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| ddd36c67-34af-3b0b-b82d-6da4466a0771 | -13.03445 | -45.09507 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 5a0ca0ab-7f74-3d12-8216-2085aaf44568 | -13.03301 | -45.10599 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2c77baad-310e-3ef9-b094-b0dc314d03d8 | -14.77372 | -43.95247 | 2025-04-03 12:32:00 | TERRA_M-T | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 90ab5aed-bdd6-3538-a189-4df12862901b | -11.28019 | -44.53239 | 2025-04-03 12:32:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 71bed30f-166a-3f01-ab4e-ea9d87b97a01 | -14.67624 | -45.81758 | 2025-04-03 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |


[Clique aqui para ver as próximas entradas](README5.md)
