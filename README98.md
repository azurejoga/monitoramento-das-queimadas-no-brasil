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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebac6c10-7a12-3521-9135-2d90506cce71 | -8.45544 | -66.9745 | 2024-10-13 05:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53aa6477-4d34-345d-b435-00c898916ca0 | -9.87613 | -67.29076 | 2024-10-13 05:27:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be1a84b-19a4-30cb-a024-dfb15b69d7e4 | -9.83829 | -66.50328 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b47e365-db08-3b84-9587-d48d4191abdc | -9.76113 | -66.08872 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97e86e36-8f13-33c6-bd09-29f16a8bca0b | -9.59258 | -66.7191 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efe5c4b4-5f0f-39bb-aaaa-5234210fe7ef | -9.57037 | -66.64516 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc5547f-85af-33ae-ba5a-2839151105b7 | -9.45747 | -67.14923 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c10bb5ea-0253-30c4-9e04-6103c760134d | -9.45446 | -67.14372 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e10176d2-c076-3994-a9eb-12a1bcb0898c | -9.45362 | -67.14857 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f430f89-7d34-3f6b-afb2-a414d36efc6f | -9.44593 | -67.14726 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24780ff3-f458-3295-bf94-c070bf825056 | -9.64295 | -68.17989 | 2024-10-13 05:27:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81898894-af39-38a1-bff5-2e10e67ffc1d | -8.68944 | -49.93462 | 2024-10-13 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7d724ed-9898-3288-8d0b-3cbbd8c79511 | -8.69015 | -49.92872 | 2024-10-13 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d0c002-4d4d-313c-9993-f7bbf35adf52 | -10.52411 | -49.96218 | 2024-10-13 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15f36d9d-1252-3070-b370-c44b999ac9c5 | -10.51729 | -49.96135 | 2024-10-13 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f18b4c3-c9d2-39ef-a8ad-20e4a16ed01d | -10.52318 | -49.95872 | 2024-10-13 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c060a91-e4de-374c-b1c9-15723406699f | -10.51636 | -49.95793 | 2024-10-13 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6292866d-6374-321c-bc7e-f0280c47acdd | -10.51561 | -49.96411 | 2024-10-13 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4d0d264-3b3e-3a07-8853-762807c0f375 | -6.39464 | -52.71253 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f5ac3b7-8b0f-315e-ae91-9f5b6e2e768b | -6.39416 | -52.71598 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd8af21f-2a00-3c33-a253-0263f4af24e2 | -6.3892 | -52.71185 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b40985d-0aad-3d7e-9560-535b5dd5dd16 | -6.2479 | -51.72384 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8b1b15a-dfe7-3bc7-81fa-12aea282af6d | -6.24211 | -51.72306 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e75abb2-8beb-3397-89da-316be430f388 | -9.72434 | -52.81736 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b46f50f-0609-33a6-8dcd-4aacabacc3de | -9.72384 | -52.82117 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88cd7983-7c07-32ec-8abe-2342c9fccaa0 | -9.7217 | -52.81611 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f122319-5420-32d9-a762-f64461ca6d18 | -9.72122 | -52.81995 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d309b5d-cc42-3ccf-a8d6-b107e45f5a8e | -9.71363 | -52.85518 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 17b6257a-40b3-3c99-a55f-f6cf4782cd9c | -9.71237 | -52.82106 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac26463d-e971-38d6-b4a9-394ffe005e99 | -9.71173 | -52.85031 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89e6c2bd-5e4b-3162-823d-78e9f83bfeca | -9.7113 | -52.8538 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7b00652-b8ce-3b31-aa8d-733230d4c8e5 | -9.709 | -52.8468 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2e2a4b5-3f10-3d93-93c8-3c76ddd0b188 | -9.70854 | -52.85033 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 447a849f-6aea-38bc-9c39-1e37ba3f31ca | -9.70632 | -52.8234 | 2024-10-13 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 453a5c8a-c41d-333d-b071-76d7ea408d8f | -9.57763 | -52.1745 | 2024-10-13 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 694b82e0-9370-3ee9-8117-65eeb2839cee | -8.63468 | -53.65213 | 2024-10-13 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e0d1961-3d57-336c-bfc3-7bb7f52d08f8 | -8.63424 | -53.65534 | 2024-10-13 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed052a53-7cac-30b5-a2be-86ef279715b1 | -4.3213 | -55.61266 | 2024-10-13 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2744bac-2b8e-3752-b82a-abdc821f6df1 | -9.33948 | -57.60556 | 2024-10-13 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 228967ec-8b6a-3da2-8ee3-d5caaa2b4021 | -9.33897 | -57.60915 | 2024-10-13 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c5f516-6b66-3253-99dd-41ba081b9d62 | -10.53258 | -57.97311 | 2024-10-13 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d726cd96-4335-3115-b0e6-a14ad662253b | -9.92793 | -58.11027 | 2024-10-13 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02c65002-1d36-304b-be49-7d720d2f4e2e | -5.72589 | -57.53956 | 2024-10-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f63cc7c0-5ad7-35c4-ac96-7dd66a98cf32 | -5.72201 | -57.53901 | 2024-10-13 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| df106104-f4d3-3a39-a12e-7d2a706bafc2 | -10.05338 | -59.00773 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2189c87-eea2-347b-9e6d-4bd9e1674947 | -10.04243 | -59.4599 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07306a4e-082e-3150-a04f-8310112ac214 | -10.03876 | -59.45939 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba283e8b-e115-34b0-b04b-69d787c51fff | -11.19991 | -58.87609 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 871b7fc4-f61a-3d4c-bc82-59eb78ebb92c | -11.19605 | -58.87564 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 373ec6ff-e77f-3966-a2de-ca9d33484e93 | -11.19222 | -58.875 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a609f53e-b3e4-3790-972b-298dbba59b07 | -11.03984 | -58.97512 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06c251a4-fd81-32b1-a10e-7df787e2ab74 | -11.03922 | -58.97242 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c6ddee4-99ad-3d43-a2a7-bfd37fcb39e2 | -11.03857 | -58.97715 | 2024-10-13 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 044c268a-235d-3294-a209-1d183e585d38 | -7.39998 | -59.71867 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f476c71e-088e-329c-afe3-b0450e553782 | -7.39706 | -59.71419 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9ba65e5-266c-30dd-a842-2de4a5b3cee6 | -7.39236 | -59.72156 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 216d6a20-e9fb-374c-b8ba-c171472b7d01 | -7.38885 | -59.72102 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 888cb837-16ad-3406-96d3-9dac373a01ac | -9.39839 | -60.32168 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4b14211-1594-3581-9656-1954348929ba | -9.3949 | -60.32115 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9510cad-7a06-3847-83e7-33ccfddf9f7b | -9.2098 | -59.76759 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b69b279-e5f7-3ecb-9b24-eff25a651209 | -9.20919 | -59.7717 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 040d4b77-8384-37db-9b07-7de5bd5178ad | -8.80292 | -60.1446 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c9caa8-8f7e-3e6e-bcc5-1f94387f7bb5 | -8.80233 | -60.14848 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9931eeff-2053-3671-be82-96410cc42e84 | -8.80175 | -60.15229 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008ee55d-9794-3811-9288-ebf29a568b4e | -8.79767 | -60.15567 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf2d7989-f489-3f93-a768-309c063c9c7e | -8.79708 | -60.15952 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a654798-ba95-3924-910f-e6f4616ad6fc | -8.79358 | -60.15903 | 2024-10-13 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cc7eb4a-07f9-3b5c-9d23-049f8dde5aa8 | -9.34614 | -60.59771 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b822ee32-f2f4-3f0d-afff-aa2eb2735641 | -10.45607 | -60.10881 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd5ab67-db0e-3eb7-bf39-011f23ebb3a7 | -10.45251 | -60.10826 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5cfcc67-06d7-38e8-8903-98d8cec43fc3 | -9.89483 | -60.29235 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa4ea4c5-c4cd-36df-9969-100bb8afd3f8 | -9.86024 | -60.73946 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d38986ce-a460-3c35-abee-25f61d38f773 | -9.85935 | -60.116 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cc8d918-b619-3249-9c72-4f25dc031ca0 | -9.85875 | -60.12003 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b27b6474-85cf-30cd-8af3-eb57dd295bed | -9.85815 | -60.12407 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05074612-cd90-3670-9f78-ceac5f692630 | -9.85754 | -60.1281 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c53d897-cc60-396e-8d12-5741342c9a7f | -9.85119 | -60.31457 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e050e61-f43a-3ef4-a0fb-439ec7d3de79 | -9.8506 | -60.31849 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc636127-8efc-3365-aa1a-ca0d07c619e2 | -9.84769 | -60.31402 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a4b9ff0-8fc6-38ff-8d76-cf0c6dbe14db | -9.843 | -60.32137 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6f765df-bdeb-38cf-a28c-09ba4b15b296 | -9.8424 | -60.32531 | 2024-10-13 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94669135-39ac-3dbe-987e-ddbe1e9008a6 | -9.39096 | -61.04159 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8abd34-8b1f-3e31-8228-ad688dce439b | -9.3904 | -61.04528 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf48d93-1066-352c-b338-31c1480c1718 | -9.38588 | -61.05214 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9b2dcf-cd3a-3824-a74b-55d8b8754716 | -10.43752 | -60.99519 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fadaa432-1672-3875-b8e6-7f2988948397 | -10.40448 | -61.23928 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19470670-3f68-3427-be92-e252aada0540 | -10.40108 | -61.23872 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c095729-df5a-3a74-aa21-7345b1279183 | -10.38342 | -61.19039 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9490978-0fe6-35a0-8076-d2ea413948f6 | -10.38285 | -61.19411 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a13eb33-4ea3-374f-894e-e46c4db7531a | -10.38228 | -61.19785 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33ba67c0-b4c7-305f-94d9-683fd7e03b93 | -10.38001 | -61.18987 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27f268d4-a112-3b48-b100-39322c1aa2bf | -10.37944 | -61.19359 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fe1c468-75c4-39b6-a095-61d83ba0dd6a | -10.37887 | -61.19733 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8694bb16-26b8-32d5-85ac-f4411217bbc9 | -10.37717 | -61.18561 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88360b28-9833-345e-b65e-d13f83182545 | -10.3766 | -61.18934 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5831bad9-db38-3a20-9b91-a591f3a86357 | -10.37603 | -61.19307 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45420abd-d14d-3d1f-b34a-78681edc6bb5 | -10.37546 | -61.19681 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 221ca759-c78b-3d64-979c-1217f50a22b9 | -10.37376 | -61.18509 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b5413c-5e52-345e-828c-e4e5c1689928 | -10.37093 | -61.22651 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50503b00-14d1-39bf-807f-698e759f0629 | -10.37037 | -61.23021 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README99.md)
