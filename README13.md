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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78adc9ef-d537-31e1-ba5f-7a394fc9eae0 | -12.9993 | -54.8423 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 957749cd-be20-31a8-8453-fed46c28fdc6 | -11.6104 | -52.197102 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9287c53f-f89e-33ee-abbf-e322f87c25e6 | -20.353001 | -48.6497 | 2025-09-06 01:05:00 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c6508507-e3e4-343f-93d0-1f8892c86c5b | -15.1754 | -52.402901 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb203d7-b0fe-3a6b-8842-891913ee681d | -9.9893 | -60.0224 | 2025-09-06 01:05:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e51cd3aa-e153-3271-8425-3f7f284f065f | -5.9448 | -53.805698 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce228ce9-9815-35ff-92c3-c6f9519b479a | -4.3738 | -48.063702 | 2025-09-06 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72df5ae8-0f7a-3d14-8345-4b6bf48e1109 | -6.2707 | -53.429901 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d47eda9-5f8d-380c-925b-0e8322e5d5d6 | -16.327 | -52.946999 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ffd700c-3c56-3abd-88a5-2b094873cc7e | -9.9811 | -51.629601 | 2025-09-06 01:05:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53a678b4-29e0-3636-9819-e70b203c2ee2 | -9.7004 | -49.4935 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a41a619f-ddd7-332d-a076-1dcaa1db7379 | -15.2164 | -52.356098 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e698e12-1646-360b-ba02-218cd7054789 | -10.4629 | -53.627998 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9477b4bb-2209-3865-aea7-e1e9524b0974 | -5.0026 | -56.0429 | 2025-09-06 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117e6b33-7398-394b-986f-e561497bd13b | -15.5395 | -49.8237 | 2025-09-06 01:05:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd35716b-fd22-3f01-a223-f99cf115df5c | -11.5875 | -52.187401 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d35333aa-fc0f-3d2c-800a-fc71e525937f | -12.9732 | -54.816898 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a57b76e1-8274-3e99-aff7-71c802824420 | -8.0514 | -52.386101 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a625207-11fc-399c-ba80-c4cdd7b00ad2 | -12.4938 | -53.8601 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbaac0b5-d433-36f8-9189-83fdff251ea5 | -24.144501 | -49.5313 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 781f15a2-fab2-3ad3-901f-50026a31db92 | -14.252 | -52.196499 | 2025-09-06 01:05:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a700f90c-ff55-3c97-a187-d762e91b4b55 | -9.7125 | -49.500702 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a63e569-8179-3d21-ac81-8e3aa886c9d9 | -15.7119 | -53.566101 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91735f44-cda0-3a9d-8591-ba5d3a8e762a | -11.1064 | -52.0271 | 2025-09-06 01:05:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36ad5d62-8385-3f89-b52b-4b401ae57bc7 | -7.788 | -52.142101 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0379dca4-85b0-37a7-a2dd-e3c4dce3cf6a | -15.066 | -48.119999 | 2025-09-06 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54b98c68-b5c0-30aa-a9ec-0c2fa2c18f4e | -13.001 | -54.803001 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b35c8a22-93ae-3057-814a-b1b573a3a14a | -8.5138 | -51.362499 | 2025-09-06 01:05:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573371ff-9180-3782-a52e-033f441754eb | -8.0497 | -52.378799 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8796e336-fc56-3e6b-9298-7f8fc27ddbfb | -9.9793 | -51.622002 | 2025-09-06 01:05:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f328b16d-0d87-34ce-93cc-98808173782f | -15.5778 | -52.911701 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34850ab6-79f2-3cc6-b158-9ad968c51bd2 | -12.9748 | -54.824299 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7db99c96-60a1-3f10-8a1c-7924cbe7be4e | -4.5001 | -42.880501 | 2025-09-06 01:05:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23a37b50-0d5e-3510-8757-276cea6e10be | -6.8364 | -52.842602 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79371db4-dc73-35a6-9004-9f4ea5e2eeb4 | -15.7069 | -53.590099 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a274a6d-a386-33a8-9f90-c91dc4317245 | -12.9928 | -54.812599 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7205cb-02d4-344c-a884-a9c75b43f8c7 | -14.2618 | -52.194199 | 2025-09-06 01:05:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f33e7a2-6bbc-32e9-826f-816b5f20e772 | -5.8641 | -52.1689 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2c220e-c436-30af-9a58-bfc31dd053b9 | -7.3266 | -48.5182 | 2025-09-06 01:05:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9056dec1-6b9e-3e74-ab39-27f4a558e552 | -6.2756 | -53.451 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1ac0ff6-b54d-34c1-98d4-edb5b8180667 | -10.0317 | -48.138901 | 2025-09-06 01:05:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3045ac04-4f69-3dc1-b8ee-a2e9587cd1e5 | -15.8506 | -52.2883 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2de17fa7-5187-390f-9b5c-902a7a47644f | -12.5119 | -53.848598 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aab5f889-8449-35ed-81d3-f09ee0b386c3 | -14.837 | -48.200001 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f07b729-ebb1-3d14-aa85-7aac63b0fa8e | -14.5717 | -48.0896 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 633ee9aa-9761-3a3b-a9ff-b403a3634026 | -8.3502 | -52.516701 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc76b1b6-3344-3cac-ab4a-d73ab1e01a92 | -11.5989 | -52.192299 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0032564-74cd-3b55-bb0d-3f76c8033058 | -12.0026 | -47.788502 | 2025-09-06 01:05:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0eca385-d17c-3d6f-aabe-db937e725ba2 | -7.0521 | -50.8573 | 2025-09-06 01:05:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c833a793-f1d2-3258-8568-6ea60b19a314 | -12.5052 | -53.864899 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38d71aea-6582-3d6a-a1ff-103734ce3f4e | -14.8346 | -48.190201 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50b7b4bb-b8d3-37f0-a2a6-c9a635f6e924 | -6.1874 | -53.247799 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a647ea3-74e0-34d8-8bd1-ec92790f6cb6 | -10.2112 | -49.726501 | 2025-09-06 01:05:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0abf293c-8be6-319e-9b12-d81337953fb0 | -7.3335 | -48.503899 | 2025-09-06 01:05:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8c9c986-0904-37c4-8f33-a4208430a5bd | -9.7028 | -49.503101 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19a0278c-48be-3d23-81cc-bcd2548427d0 | -12.9618 | -54.811699 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 871ac57a-14c8-3e15-b627-708b0482b4b5 | -5.6854 | -53.754601 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59cdd7ec-818c-3c7d-ab0c-45720abc3c6a | -11.6251 | -52.216202 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1779761c-9010-339d-9f58-f6f073f00973 | -11.4775 | -55.542702 | 2025-09-06 01:05:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 114ce1ee-8ec2-3e50-916c-dcf408e6e967 | -11.6087 | -52.189999 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95f74aa2-ff38-3a9a-aaba-be20c43162ba | -11.5373 | -47.331902 | 2025-09-06 01:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f63474d5-1292-37f8-9d4b-83a09b727151 | -15.7217 | -53.5639 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65390ca4-f17c-3086-b644-c5609b86d8af | -15.581 | -52.9259 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a66244c-43e6-3554-ae8f-30303f751b85 | -9.3868 | -54.747601 | 2025-09-06 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 431bab96-64ac-3e30-b516-15e963eb82c2 | -6.8084 | -52.810902 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afbff2c4-0a6c-3e3e-a8ec-8204c49f89f7 | -10.4661 | -53.6418 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68d01b16-d85d-3b65-bd7a-6bbb57cea187 | -14.5641 | -48.016701 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3326c07-90dc-35bb-9574-56348ba45d83 | -12.5185 | -53.832298 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b879719-f4cc-3b7a-910c-fe8856e5025b | -9.5583 | -53.5947 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5be0562-32ee-3f55-b906-803860fcee87 | -11.547 | -47.329399 | 2025-09-06 01:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f662db61-ff5c-3d7c-b378-da726bbfc45d | -12.515 | -53.862701 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 157a0804-9a64-3f8f-b389-69aa1dfa05af | -9.673 | -49.294498 | 2025-09-06 01:05:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8259a84b-9119-3802-8510-dd4291a5e5a9 | -10.4677 | -53.6488 | 2025-09-06 01:05:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1fd5fb-0236-34fc-ac10-e43acda23ef2 | -9.6837 | -51.111599 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 284b67ce-3df8-3f5f-8e09-92fea015e9e0 | -6.8378 | -52.8041 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548e787b-be02-3c56-9a8d-68b163282518 | -11.2095 | -55.026798 | 2025-09-06 01:05:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aafd942f-c30c-34a9-bb5e-5274715dad89 | -12.6884 | -44.991001 | 2025-09-06 01:05:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32466377-f254-3716-9956-9e78b16d9908 | -5.9546 | -53.803501 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c336dbd5-9e39-3c03-86eb-e96d61976959 | -15.6005 | -52.921299 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd43cf6-3893-3c2b-b017-1065e0b74de0 | -12.965 | -54.8265 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb14ed68-1242-3d58-8643-b872643318e1 | -15.7085 | -53.597401 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 310d3e37-1ba2-3fd6-8adc-5bb4039727ec | -12.4809 | -53.848202 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3c7d08-551e-3790-adde-21f2e522ac7a | -16.330099 | -52.9613 | 2025-09-06 01:05:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9913a3fa-d815-3e2f-a27d-213b06b95e48 | -12.5217 | -53.846401 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c773796-336a-37bd-af97-47eeb86370b7 | -14.9017 | -55.0909 | 2025-09-06 01:05:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86253dd8-803d-3df9-b4e3-468ec9cbda44 | -11.4694 | -55.552399 | 2025-09-06 01:05:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c644a1-6c3f-3884-97d8-a98b30259533 | -6.2658 | -53.453201 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c0b28a-f599-374e-810f-4ecea812885e | -12.9536 | -54.821301 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0176ae23-84ed-395d-bcf7-c1d1c8b51b03 | -9.6897 | -51.093399 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6978da99-cbb1-339b-90ba-493b1f5f8ecc | -8.3522 | -48.281101 | 2025-09-06 01:05:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 703077c6-a1ae-39c5-b887-befd3d63e1f9 | -15.1902 | -52.377102 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8496c606-03f2-3da7-b624-c2706b43799c | -22.83651 | -49.18945 | 2025-09-06 01:07:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a3e20664-fcd6-3f64-b470-f06d5c36c038 | -24.14042 | -49.5037 | 2025-09-06 01:07:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fe1ef902-7382-3009-815c-3156f5bdf055 | -19.84201 | -57.94529 | 2025-09-06 01:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6e39da17-bb80-30d0-9355-10eb4e41ac5a | -22.66215 | -46.82956 | 2025-09-06 01:07:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 8a7e4039-0dc6-37ea-8e2d-a4f27bb38341 | -18.14862 | -51.77544 | 2025-09-06 01:07:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b6275d1a-9d3f-30ea-8818-e1ad3419619c | -22.24805 | -48.74467 | 2025-09-06 01:07:00 | TERRA_M-M | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 204.5 |
| fdccbf41-b0b8-3a37-ae78-c0874aa43da9 | -19.89837 | -57.92603 | 2025-09-06 01:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| f636eebc-139d-30e4-9378-01442c44c099 | -20.53008 | -46.47731 | 2025-09-06 01:07:00 | TERRA_M-M | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0dfc0814-7515-3959-b48a-93ede5f7668f | -18.15067 | -51.78826 | 2025-09-06 01:07:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README14.md)
