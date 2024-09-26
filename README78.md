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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f3a6ce-e474-349e-ae8e-13b99a59a439 | -12.82603 | -51.21368 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c441cfc-5b6f-382e-8b47-2ecc70ef21f1 | -12.82494 | -51.21951 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a5626a7-3ab1-3f60-8211-6124612f4b51 | -12.82384 | -51.22534 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5edd9b80-8a33-33c3-af02-edbe2aeac24e | -12.82275 | -51.23118 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3766955a-34b9-3271-b9db-86f997980d6a | -12.82193 | -51.23555 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e31c3de2-df59-3036-bd23-740d11f086e5 | -12.82141 | -51.26586 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86ecb0d0-2c0a-3749-83c7-88fce1cd9e14 | -12.82106 | -51.21268 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1f109c3-6222-3da8-95fe-f97f238d3a0c | -12.82086 | -51.2688 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c79d6d-2a05-3bd6-8868-149d4697e242 | -12.82083 | -51.2414 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3ec5c3e-ff05-3bea-8508-7e9ab99f66d7 | -12.82031 | -51.27173 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52402bcd-d022-36f4-83ce-bacae2f53d6d | -12.82028 | -51.24432 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4831fc9a-3534-387a-9d3d-eb47b675829a | -12.81997 | -51.21849 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8e0e51d-e054-3759-b7a8-0cf5ef0ec203 | -12.81976 | -51.27467 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22aa5eab-4d0e-3148-b77b-3ee147381f55 | -12.81973 | -51.24725 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3352e465-7930-3ae3-b08b-2a0ba670db71 | -12.8192 | -51.27761 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 377232f6-bc71-328f-8946-015484439b22 | -12.812 | -51.28837 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 256a1475-ee20-37ef-b949-e86129a93786 | -12.81145 | -51.29132 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00891ddc-bab0-3df1-9af5-730d7d73d6bd | -12.81089 | -51.29426 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d22d2397-3881-3d31-8189-d2b99209a061 | -12.81034 | -51.29721 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfeab7d-9d4c-3cbb-80d3-f5164f4a9959 | -12.80978 | -51.30017 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1f88215-078d-344c-8fb7-1e9bf1a3e8ce | -12.80478 | -51.29915 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2640e8cc-642e-3e22-a660-c97bc25a937d | -12.80423 | -51.30211 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b26596cb-239f-3b09-b617-fccafff5539d | -12.80367 | -51.30507 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dc754fc-a258-3133-a2ec-d6d9de6d87ca | -12.78923 | -51.29906 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0e21875-0e9d-3cc1-974b-92256cb03626 | -12.78867 | -51.30201 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8ac4a49-e38b-3b2d-9993-f9bf15465824 | -12.74149 | -51.27718 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 362261f9-49b7-3c5e-9730-c072e06fb53d | -12.74092 | -51.28012 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b739a137-3de5-32d4-b3b3-d7a582f0ca14 | -12.74035 | -51.28307 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a55f4db6-199e-3c65-8ee7-659457c075cd | -12.73978 | -51.28601 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3dcd0fc-c92a-3b66-b01b-c2e133e80fe6 | -12.73921 | -51.28896 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7abda38-ce18-3ed2-9866-12339ba97308 | -16.11311 | -51.9982 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 78e92203-4f30-3c59-be7d-b746b7c77b6f | -16.11195 | -52.00403 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 00e8f291-fad4-3fec-a3cb-be893a6c7ab1 | -16.11052 | -51.98537 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3de13c84-8a60-33ad-83fc-490ffe3bea32 | -16.10936 | -51.99123 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e70da080-6335-382d-802b-f90504552b4c | -16.10817 | -51.99724 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| af9ba551-2ba1-37d6-96ab-d4fce4f384ba | -16.10699 | -52.00317 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 10972021-a709-38bf-8b78-96c8c493f388 | -16.1058 | -52.00919 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f4c8b423-4466-39e3-a936-7620d58b51ce | -16.1032 | -51.9964 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e8510ca2-ee41-3814-ae89-52c347e65a8b | -16.10201 | -52.00242 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4e3f1f1a-2357-36ad-a5bc-a892a861e00c | -16.10082 | -52.00838 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0bb9def9-5551-3882-9df3-a4f55a38cc0a | -16.09967 | -52.0142 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 44a4f039-1afa-33f3-b593-fc40010b1588 | -16.09821 | -51.99569 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| eb633d69-cf39-3f3c-8b97-d677a963a71a | -16.09701 | -52.00174 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 391b8732-38a1-3aa1-a8d6-09fdcea5ee6b | -16.09325 | -51.99487 | 2024-09-26 04:08:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6b71b048-868a-39b1-8c3b-ad9919bead91 | -17.56766 | -52.95787 | 2024-09-26 04:08:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e68811f-0aa0-3b74-bbae-399731f92790 | -17.09773 | -52.14988 | 2024-09-26 04:08:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a880b54-ed6b-31bb-be9c-f2a8e3f2303f | -10.78046 | -53.57262 | 2024-09-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 425971f7-1e1a-381e-9c92-8822ac911816 | -12.84517 | -54.03775 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a190117b-2819-3e2e-96c3-20d5670b553b | -12.84426 | -54.04235 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e15c215c-31c0-3690-859f-c73a9bb40d14 | -12.84165 | -54.03681 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d610ff02-4348-3d67-b0bb-2528bdf7ebf7 | -12.83924 | -54.03645 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417ee799-14ec-310c-905a-1162780f12c3 | -12.83664 | -54.03102 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883d4029-9157-37e9-8ccd-af449c7668a1 | -12.8342 | -54.03062 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a522742-a20e-3eb2-b1f7-928b1f08316d | -12.83071 | -54.02972 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c98c3684-0b4c-375b-8580-db577ee17132 | -12.82826 | -54.02932 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aca44751-8e32-3368-8a8c-6a79ee47aef5 | -12.82569 | -54.02399 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36b50ed6-d311-33a5-852f-2cac7cb84cee | -12.82477 | -54.02845 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1f2815e-e8c0-3a61-9c05-8c8bf2193347 | -12.82233 | -54.02802 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8a0450d-70ab-3962-9b27-4a939579484a | -12.82143 | -54.03251 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5de8621-69a5-369c-8118-4dee28f93215 | -12.81729 | -54.02224 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93f2d9da-e53a-3218-9ac1-bf651273e85d | -12.81369 | -54.04023 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d339a058-7b5a-366c-b6af-501fee7de757 | -12.80684 | -54.04348 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 525c9cd7-a882-30ee-bf43-41646ad6a6bd | -12.80593 | -54.04799 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f690ecce-2658-312d-9ba2-49a00f950355 | -12.80503 | -54.05251 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf7914f3-c54b-33d3-a28d-51dc9b2d538e | -12.80412 | -54.05704 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87dd1574-00e9-35c9-bb8e-21a529810083 | -12.80361 | -54.02869 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f67eda4-924e-3528-8bc5-73ada222052f | -12.8027 | -54.03322 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adf1ef7e-f673-313f-a8b4-e5fcc34bb1a8 | -12.80178 | -54.03776 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04e63866-b9b7-3b2f-90fe-d6965efda71c | -12.80087 | -54.04228 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f23a6d45-7bbe-3587-bb63-b1a02c0e35d8 | -12.80049 | -54.07516 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51e6eac0-33ef-3973-9c3d-3def14f56c9b | -12.79997 | -54.0468 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59d1e84c-1908-3956-81c7-e570df6a6196 | -12.79906 | -54.0513 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8227dfbe-959f-3206-9735-be9dfc70044b | -12.79816 | -54.0558 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb62e1a5-4ada-3634-b0cb-ee029b31ab4c | -12.79766 | -54.02741 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1365b3a4-15a7-35e6-a30c-7fd8939cb1b5 | -12.79675 | -54.03195 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c830d3b-0c74-31b5-b24a-76863f0c47cb | -12.79583 | -54.03654 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a2e9590-0cc4-36b8-b924-46b4ac858a35 | -12.79491 | -54.0411 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9684ac82-8cf1-33b4-94e7-d295172ef373 | -12.79399 | -54.04565 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d4be8bf-c892-3bcc-b07e-3dc39cd2181d | -12.79309 | -54.05015 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92567f10-da68-36c4-9344-b8b199def1e4 | -12.78896 | -54.03983 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df50c3e7-a252-31fe-8eb0-005a3c45d2de | -12.78802 | -54.04448 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16e35b1a-af3e-3cbe-a9c4-128e9c60b950 | -12.7871 | -54.04904 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f577689c-73f9-3b2d-886a-57a2efe2961e | -12.75552 | -54.05163 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1962052e-f68f-3772-9712-3fcdd6e329db | -12.75458 | -54.05627 | 2024-09-26 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e615c588-888d-3702-a2d3-acdfeeebbcf3 | -12.53646 | -53.50146 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f16b5d3-939b-349f-8ba4-d87a4579cb11 | -12.53561 | -53.50564 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2e9836d-1026-32af-9325-90a6e5d2c8e5 | -12.53152 | -53.49605 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aea3ef5b-f21f-314f-a5a9-01a41f43a8f7 | -12.53081 | -53.50219 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df0248ef-6e9f-3161-a921-98030e48d86b | -12.53067 | -53.50024 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ccd0827-842a-3c04-94e8-3a0a14cd8bed | -12.52901 | -53.50848 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fd905b3-bc9b-3130-a623-bc0c1b8828e2 | -12.59787 | -53.16587 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 260cfe1a-5e6e-3f8a-a7e4-9d94afa6a7db | -12.59706 | -53.16989 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c18d286-b342-3241-a96e-216c8d7e61ef | -12.59627 | -53.17384 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8656fd4-808b-3f27-bc1b-f00ac42ef354 | -12.59573 | -53.16678 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df1c087d-a766-3216-8cab-b8c35ad0a0e2 | -12.59495 | -53.1708 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cb69fe7-6f6c-3d82-933f-97651a011687 | -12.53681 | -53.16674 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de8dbd3e-1c19-35be-96d4-de83a604f5a7 | -12.53603 | -53.17074 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a65063-7402-30a4-8228-0dc1532e83cb | -12.53524 | -53.17471 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a550e7-4f25-379f-9197-618867366f02 | -12.53478 | -53.50977 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36fcdc02-71ef-3dc1-b13e-ae83d88d5bf0 | -12.53163 | -53.498 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README79.md)
