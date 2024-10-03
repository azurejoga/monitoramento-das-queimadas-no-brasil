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
| 3646d29d-a4d3-3e9a-b1ed-fea6b659c71a | -8.45106 | -55.45643 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad80a73a-bb5a-3de7-a9c0-d1b2ac74c18a | -8.44755 | -55.45584 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79605610-8ad1-348c-910f-1893ecbbcac2 | -8.44499 | -55.47158 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8b5d2fc-062b-3fee-8eae-d0d596e55539 | -8.44149 | -55.47099 | 2024-10-03 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ab9e3dc-dce7-33c4-abf8-b77b6956414c | -9.92266 | -56.1009 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a14df36-ab24-3dff-afba-a3b8fd3cafd9 | -9.71378 | -55.59307 | 2024-10-03 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a80f0b-e9b6-3194-95e9-0c293f570d58 | -10.62747 | -55.87914 | 2024-10-03 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d7bffc-38ba-3091-9010-2d8c194a68d9 | -10.62682 | -55.88306 | 2024-10-03 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a842ab01-a672-3493-9384-b06998e7f1c2 | -10.62332 | -55.8825 | 2024-10-03 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5798d78f-6c44-3854-a3e2-ab251f2799b0 | -10.61917 | -55.88588 | 2024-10-03 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8f6c6b6d-e816-3f0b-8d06-0602fbc994a3 | -11.92383 | -56.95329 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a4c53a-fe9e-3f16-ab07-2aec985cf90a | -11.92362 | -56.95043 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b94f194-dacd-38af-9e38-fc3b51d71cb7 | -11.92311 | -56.9575 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81b3ebe-74d9-3ced-b0c8-0e1913e2a860 | -11.92293 | -56.95464 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b63c61-ae7c-3bb4-ad7f-24d7c9185082 | -11.92239 | -56.96171 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24cb5f0d-3793-382f-9f42-4f525573f452 | -11.92223 | -56.95885 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdcbedd0-0521-31ad-8d95-cf0a3f61ede0 | -11.92022 | -56.95265 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c56c6c7a-0209-3719-893f-b973b91c3973 | -11.9195 | -56.95686 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0972993f-7e31-38f4-8b1f-1a39d94cc2a3 | -11.91932 | -56.95399 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f41dbc2-b0bc-34fc-b7a5-63a0737fdc03 | -11.91862 | -56.9582 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b88140-d6a9-3403-9eef-88d9e728b58d | -11.91589 | -56.9562 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e7fc26a-4833-3176-b0a4-a36059b6cb68 | -11.91501 | -56.95755 | 2024-10-03 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b4430db-3e0e-3634-b111-e2ef73e43472 | -12.61461 | -56.48143 | 2024-10-03 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b99fa65c-575f-3b92-a216-f403f5b89968 | -12.61395 | -56.48542 | 2024-10-03 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ece90287-b8cd-333b-8c7c-0af6a3b74775 | -12.61044 | -56.4848 | 2024-10-03 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4e99333-5432-3273-9acd-da3bf6b64aff | -10.1665 | -57.26834 | 2024-10-03 04:51:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 422c69f1-6456-32bc-89db-b3a7f002026e | -10.16572 | -57.2729 | 2024-10-03 04:51:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 33be8dfc-36b3-3515-a979-a55d8f5a67ae | -11.99013 | -57.19706 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a4c9aa9-a899-3d4e-8b27-fe3254ede1dd | -11.98801 | -57.19347 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8da6ee4c-5d7c-39a0-b78f-b2fdff276793 | -11.98729 | -57.19782 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 240631e8-1c36-3997-8117-7e060c6329c9 | -11.98722 | -57.1921 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af922a95-0d91-316d-ac80-76b1930618bc | -11.98648 | -57.19643 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af842b94-d26e-3360-8b89-d52ae1671d4f | -11.98435 | -57.19286 | 2024-10-03 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 413e4e5b-e873-316b-9952-3a5e173fe70e | -17.32642 | -42.5046 | 2024-10-03 04:53:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0827fe9-dbc1-35ed-99c9-f9357ee21bee | -19.43933 | -41.36597 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79b5d938-3d4c-3865-b006-cf8df7e713c6 | -19.43841 | -41.37747 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fda92b84-fc04-3e4b-a93e-3c90d59fa6bc | -19.42565 | -41.35782 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a60fbf24-cef0-30d8-a1a7-9b15ae9aecbc | -18.90134 | -41.20699 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2e173c82-0bd4-3f24-972d-f2dc69a5c783 | -18.90067 | -41.21473 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 70073f88-228a-354d-b410-7a8ed33de8ba | -18.89756 | -41.20816 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 1067a6b4-be28-30fd-a927-2d132c1bcd88 | -18.89422 | -41.20621 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c561a9f3-3b86-323c-b477-a98bad8cc408 | -18.89348 | -41.21471 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2a2cd12b-97c7-3bf3-98d6-46c7c6d93e9c | -18.89041 | -41.2076 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 6ab22c1e-5603-3b1a-a8ec-168aa65e04f0 | -19.26661 | -43.77892 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a035d3d0-1fa9-3be0-b6fe-ab5bce611045 | -18.88976 | -41.21586 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 62415f9e-916a-34d6-befa-0088fb49590e | -18.88918 | -41.22303 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 79c9e8c6-76a7-32d2-bf52-a324c2be3306 | -18.88627 | -41.21496 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 575bf511-83f4-32f8-b1df-7ccc7025c840 | -18.88565 | -41.22221 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c49317bc-c345-3041-80a7-feb187bca3e9 | -18.88243 | -41.21766 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 39b30acc-fe2e-3e81-90d9-cfea2f30587b | -18.88195 | -41.22368 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| da59a8da-5be2-3a57-ae0c-80a9e64cde9f | -18.88049 | -41.24205 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2be11d61-98eb-3d06-be04-486b2564dfa8 | -18.87986 | -41.24995 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 94ba161a-dc33-3991-a24c-16576b302ca3 | -18.87886 | -41.21753 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 636a82e5-50a9-3712-9fb5-bbf71d748ecc | -18.87838 | -41.22315 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| d366076f-b3d6-3095-8391-01bfe4b912aa | -18.87622 | -41.24848 | 2024-10-03 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 55f9e3cf-aab4-31c1-a34d-ab32a9135e50 | -20.81436 | -41.627 | 2024-10-03 04:53:00 | NPP-375D | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0121deab-e2e6-3a21-b371-e6f5fc2a0a13 | -20.69255 | -41.98157 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 194bb88b-afaf-3d7d-a20c-6d629602cb17 | -20.69208 | -41.98073 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 321c39f1-8553-30a5-8868-117807d0882e | -20.68595 | -41.97662 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f11228c2-5d7c-3b64-af27-fe6db6f1b60d | -20.68556 | -41.98149 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 67ac4f46-0ac1-3725-bd1b-9e48d25b9e56 | -20.68545 | -41.97576 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 90a0945d-99f3-3317-96a6-ac3ad14d8775 | -20.68508 | -41.98075 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 90483a19-3243-3269-8053-ed738381f6c4 | -20.68473 | -41.98539 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a7a71003-866b-3a41-914e-1bccfafe31f5 | -20.67027 | -41.99762 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3e1a1ed4-f55d-3e99-9e17-2c210cca359b | -20.66986 | -42.00273 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 730c4163-76c1-309d-86f9-4a070f7a44ce | -20.66953 | -42.00185 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d81d5fa5-ebc2-3c28-bd74-313ee2bceda9 | -20.6695 | -42.0072 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 3f49fbdc-c779-3193-8c5d-cc24a20d613c | -20.66919 | -42.00639 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9eb95efd-b2cd-32b7-af06-fc0fd4879f92 | -20.66286 | -42.00278 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0366b278-af2d-3813-9a98-d36b45e147f6 | -20.66253 | -42.00198 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1176aa14-0e8d-3578-a0e1-8cd298772436 | -20.66252 | -42.0071 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e554ddf-99bf-349f-b4dc-96f877f515ad | -20.66222 | -42.00618 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d88536a9-53cd-3048-81e1-4888c48db0cf | -20.65638 | -41.99639 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0a4e29bb-9c0c-3b63-a38a-829402be8fc1 | -20.65603 | -42.00078 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 20238fc4-3b1d-3aea-b248-1860ed4d363d | -20.65603 | -41.99533 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b97e0fe0-0f34-3e38-8605-360767940586 | -20.65569 | -41.99988 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e782f58d-bf24-3866-bcb2-568c3cd7389e | -20.64957 | -41.99405 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ac10c776-7667-32df-9d36-e15da9238e7d | -20.64921 | -41.99294 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ca0c6488-1be4-3fa0-b621-824311d95112 | -20.6492 | -41.99879 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3cbf975c-2fd8-3146-8872-dde53789a8c2 | -20.64886 | -41.99765 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 77ff8f42-9109-3a24-9824-9f88b8a659f5 | -20.64881 | -42.00374 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b4392114-53dc-32cf-a1e0-1b572c30bc77 | -20.6485 | -42.00257 | 2024-10-03 04:53:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f9087abd-9b4b-3da0-a980-a2902cf0c49c | -22.08139 | -42.09402 | 2024-10-03 04:53:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1ee6ec47-e8b1-30b3-bb4a-32859a00cfb0 | -22.07462 | -42.09035 | 2024-10-03 04:53:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c89e4dc7-3cd9-3239-81f2-979883834337 | -22.07424 | -42.09555 | 2024-10-03 04:53:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e3d86776-62cb-30f7-83db-8f6b338e1061 | -21.30881 | -41.40742 | 2024-10-03 04:53:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 05a23cb5-4e5e-393c-928c-766724769bdd | -17.32697 | -42.49876 | 2024-10-03 04:53:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cb2a5d4-fe7d-3b2a-a7b9-7bae0dfeaee1 | -17.85476 | -42.25494 | 2024-10-03 04:53:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fe3c1d56-c9fb-3b90-9101-3e7652a788df | -17.85163 | -42.25066 | 2024-10-03 04:53:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd73ca78-9e89-303d-b42e-aea4d3b7bc41 | -17.8511 | -42.25662 | 2024-10-03 04:53:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 55edec59-fae7-39a2-993e-e0fb78db4cf3 | -19.30905 | -42.60224 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 1997e873-a663-3718-954e-422eaf507443 | -19.30865 | -42.60696 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| deb3484d-0cef-3e91-ba8b-0ab4de6b3aef | -19.30828 | -42.61127 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 6f19c4b4-433a-36b2-a564-c6b80804906c | -19.30347 | -42.58942 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9c6b5e18-561f-30c0-8661-a81f67f7a2ea | -19.30249 | -42.60095 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 9a805197-20da-3a2d-8132-d1f4017d1bc2 | -19.30209 | -42.60556 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a9574ef5-88c1-35b8-b21f-bba3c5c113b8 | -19.29981 | -42.58813 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| ce9c33a5-a72e-38b1-90ce-35ccec03c5f3 | -19.29918 | -42.59503 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 3fd5b875-27ca-3799-8fd9-df4ca29f8c8b | -19.29706 | -42.58613 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| d8daceb6-a06e-3d7b-820e-71607f199ede | -19.2964 | -42.59396 | 2024-10-03 04:53:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |


[Clique aqui para ver as próximas entradas](README142.md)
