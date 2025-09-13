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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb42cd4d-6f73-3f66-b4bd-f3101352430d | -22.24786 | -48.56871 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 25c66386-3427-323c-b89e-7e883d090afc | -23.14241 | -49.65842 | 2025-09-13 00:48:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| ed8a4457-f00d-3b95-9ff7-a91a50cec777 | -22.22493 | -48.59879 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 25c9abd0-7c9b-374a-ab19-70ec2e0d4b97 | -25.16429 | -49.69884 | 2025-09-13 00:48:00 | TERRA_M-M | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 84c0a20e-4503-3b6a-9bac-fa7ed05849d5 | -21.06666 | -46.1422 | 2025-09-13 00:48:00 | TERRA_M-M | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 1cf51fdc-406d-308d-b6e3-e12a340b2c58 | -22.24934 | -48.57869 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| f641aee1-676c-3327-8f11-9a2164a22a00 | -21.24163 | -47.76683 | 2025-09-13 00:48:00 | TERRA_M-M | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6dd229db-2312-3968-a6db-9406e62f119f | -22.23126 | -48.58164 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 6ddbf022-7f85-369d-9e8b-ccb2aecf5504 | -23.44374 | -51.42802 | 2025-09-13 00:48:00 | TERRA_M-M | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 06f038c1-ed1b-3f7c-b4d7-238eca40d3ff | -23.29972 | -47.33916 | 2025-09-13 00:48:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ccda4499-0004-3303-967e-4ef147ecb905 | -23.61189 | -51.37962 | 2025-09-13 00:48:00 | TERRA_M-M | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 122ca62e-2797-3835-9f0e-e4f2fbe705c1 | -22.17705 | -49.61297 | 2025-09-13 00:48:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7fc76da8-bbc6-3347-9a10-4659eb3a7ca9 | -22.23423 | -48.6016 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| 221509e5-d77f-33a6-b13c-d61157f18c09 | -21.58867 | -48.41729 | 2025-09-13 00:48:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5562fa06-17f3-3e42-959b-c92d1151442a | -22.24179 | -48.59015 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 5e5557ab-caf8-3a93-aed0-f3f44b29322c | -23.14107 | -49.64885 | 2025-09-13 00:48:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 7b97dc2d-d383-3ba8-b0ff-622aa6a8ef3b | -16.0257 | -47.9294 | 2025-09-13 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 943b4e44-7f83-3150-b125-d1c4f924b97f | -16.1001 | -49.9457 | 2025-09-13 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 86143c8b-7fc2-34f6-b5ee-8792a7afdf22 | -10.7664 | -50.5299 | 2025-09-13 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 242.9 |
| c89e0c9f-d8f7-325e-89d2-1829eeb5a5dc | -20.6162 | -50.3771 | 2025-09-13 00:50:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 706f3c0d-d057-3823-ac48-24e3bc8f353e | -14.4394 | -47.3206 | 2025-09-13 00:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a9337be7-ec82-3c8c-8aa4-862ba69c49fa | -9.5006 | -55.9588 | 2025-09-13 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 2c769da3-ce58-3ae2-b633-28ad4ecf990f | -16.0252 | -47.952 | 2025-09-13 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 32ef4548-c52d-346e-9043-a26272e2ea0f | -20.5952 | -50.404 | 2025-09-13 00:50:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 66d52bbf-eccf-375c-a8cd-78f20a8e50ef | -12.9292 | -54.7538 | 2025-09-13 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 07bcd628-efb8-37cb-be08-b4fbdf8ddbc0 | -9.247 | -59.4201 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 20c83f23-a593-38b5-9c09-6027b7376ee1 | -3.2283 | -47.6154 | 2025-09-13 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a66a5156-52cb-3d90-bca5-fc0f18267e11 | -16.5106 | -55.1042 | 2025-09-13 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 2ab58fad-0160-3ce3-a392-4c2025a63865 | 0.6904 | -50.6481 | 2025-09-13 00:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f0db02f5-f51e-3c53-b92a-9e7a2941a0fc | -10.7661 | -50.5513 | 2025-09-13 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 0a874dc9-b222-303d-9676-2379e0208a80 | -15.2229 | -56.6782 | 2025-09-13 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 07ab61b8-b4b9-33df-b910-91c93583cc36 | -10.7474 | -50.5319 | 2025-09-13 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 58abafef-e3fb-32b7-8b26-03203ebd187a | -9.2503 | -51.2472 | 2025-09-13 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 5d3790f0-6a01-3dd9-9095-60dfe7736c9b | -3.2321 | -46.7836 | 2025-09-13 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a40e04dc-a6fc-3b35-b6f6-db65b5ccf92e | -10.9092 | -47.2247 | 2025-09-13 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 920a9b7f-e787-3b72-b93c-2c26a1194bf0 | -9.5193 | -55.9575 | 2025-09-13 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c53c4312-eebd-320e-8c31-511d1c4644af | -12.9294 | -54.7333 | 2025-09-13 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 71fdfffb-1fe5-3d2b-837c-83a0c594fb09 | -11.7196 | -46.6031 | 2025-09-13 00:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8c1b5881-49f0-36e5-8da0-713d5fdbbe0b | -9.5004 | -55.9788 | 2025-09-13 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 12c3c904-fad9-3f44-b609-20eff1fdb5a6 | -3.2305 | -47.135 | 2025-09-13 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fcaeccf2-420c-31de-a158-b8acfb49b2ce | -3.2282 | -47.6371 | 2025-09-13 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 34cb9e5d-7097-3f8e-b703-19dd9fadbad4 | -16.0997 | -49.9677 | 2025-09-13 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 686c0901-55e2-3bef-9b02-18d71e96f0a5 | -9.2656 | -59.4191 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 248.6 |
| 41c51127-8bd8-388b-8f2e-6502f641fdf3 | -9.2843 | -59.418 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 597c2710-a6b3-3997-a582-4888db83f0b9 | -11.7424 | -44.2117 | 2025-09-13 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 560fa242-4fc0-34cf-92d9-5840847f16b1 | -9.2658 | -59.3997 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 207.2 |
| ade774ae-f7b8-3947-814f-79286a72ffd6 | -17.3622 | -42.7029 | 2025-09-13 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 48ce9f87-8161-3818-a14f-0f2347aed303 | -16.2546 | -50.0524 | 2025-09-13 00:50:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 829b514c-e86a-303c-b065-e55d45bffe20 | -15.2036 | -56.6803 | 2025-09-13 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4073ffc4-884e-3224-8c0a-32157a709c42 | -16.4906 | -55.1276 | 2025-09-13 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 149.9 |
| 3e767a46-0a86-36a8-a1a8-87ede9857288 | -11.7388 | -46.6005 | 2025-09-13 00:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f56e9cac-80a4-3600-9ce9-38a46d94f56e | -16.5666 | -49.2247 | 2025-09-13 00:50:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5c831c07-fbda-3969-8c43-acacc663e935 | -9.5324 | -54.6277 | 2025-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 57f9842f-918c-3afe-9e64-6cb23257f088 | -9.2472 | -59.4007 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| ac7219c3-e955-3aed-94f7-80406e4c882d | -16.5102 | -55.125 | 2025-09-13 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 4eb6ac89-9b18-36c8-b2c5-90267d86ae3a | -12.0056 | -47.7728 | 2025-09-13 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b959826a-e65b-309d-9b3f-b3c3514491be | -16.491 | -55.1067 | 2025-09-13 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 25bc857d-798e-34dd-b8c1-eddac205893e | -9.5137 | -54.6292 | 2025-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 73e032d5-4180-3368-b0a4-857c0d956ff7 | -10.6389 | -46.2718 | 2025-09-13 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6dce87c4-bf07-3011-aa28-da776161b10b | -9.2844 | -59.3986 | 2025-09-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 4243e837-36bf-3590-98e2-9c4f44fe00dc | -20.6156 | -50.3998 | 2025-09-13 00:50:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.8 |
| 872f1eeb-dfe9-320c-af45-0e81f70d0713 | -11.0747 | -51.5153 | 2025-09-13 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 609133b5-cb99-3bd0-a313-b40475e95a5f | -16.08 | -49.9709 | 2025-09-13 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0a6cbc36-229d-3ba4-8ebf-1a0d76856d07 | -16.2541 | -50.0745 | 2025-09-13 00:50:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| aa08f2de-a038-3698-85a0-76d6c9709d04 | -9.4993 | -46.4299 | 2025-09-13 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 20591034-bb12-3a59-b04b-3fb5ae6314f3 | -12.006 | -47.7505 | 2025-09-13 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| db13db13-1f63-3bf8-9b6e-9f69f3874a29 | -9.4819 | -55.9601 | 2025-09-13 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| eb1dfde2-1587-35ee-9694-db0eae2073c9 | -10.6579 | -46.2694 | 2025-09-13 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 5e5962cd-caaf-3a7a-b78c-4b0ec64e6613 | -12.12506 | -44.84604 | 2025-09-13 00:50:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a0d5481a-b1ae-3e17-be59-7798e95b3004 | -11.11246 | -51.47507 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| efed1f86-0962-3932-9d23-46d77a65bf91 | -15.68723 | -50.57906 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d460a7cf-de06-3c14-8212-f4872eae3dfa | -15.1713 | -52.50196 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 60183b3d-58fa-3ab4-9842-7c18f8d636a3 | -11.78349 | -47.40524 | 2025-09-13 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 3fc01e37-76a4-3269-9e32-438870a7bc57 | -20.61138 | -50.40358 | 2025-09-13 00:50:00 | TERRA_M-M | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| a0eac2f3-29d2-3111-8ca8-99fef239b48c | -15.87261 | -49.94205 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1c9043db-a051-35e9-bc2c-995f7f1ce1db | -17.29156 | -47.23631 | 2025-09-13 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b858da5c-bee0-3410-b288-39845f0bdd80 | -12.96278 | -54.73968 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| aad7fc49-9e48-321a-a685-16569c554090 | -15.70793 | -50.58897 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9c267fb0-c448-374e-90c7-e54b117710db | -16.79169 | -51.35648 | 2025-09-13 00:50:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 84a86582-1c70-3058-8be7-92938df98ccc | -20.02084 | -47.6331 | 2025-09-13 00:50:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d7ca9585-523b-35c2-9a68-3146c8f627c2 | -16.39593 | -49.06207 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bfbd13e4-5810-33a1-b6d9-c481613ab859 | -16.56246 | -49.23827 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b0688683-a134-3978-a37f-648ae20e4dbf | -15.58453 | -54.75065 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5adbde08-2fe5-3949-b8e8-f08148603361 | -16.26009 | -50.07159 | 2025-09-13 00:50:00 | TERRA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 8e4b2fc9-d889-37d6-a2cb-61bc4f935597 | -10.53684 | -49.86376 | 2025-09-13 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 25989d05-4b18-382e-bfd2-aaaecec8637d | -15.4727 | -47.33879 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| dd94f72d-cc8d-3da2-aca3-560554b0b78e | -15.17299 | -52.31322 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5076d09c-8e80-35f9-acde-58e3b10e743c | -16.0974 | -49.96634 | 2025-09-13 00:50:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 729e3959-1343-3a5d-abde-03d2e1d2c775 | -15.11622 | -52.50691 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0e81507-53e0-35fb-830a-e7c07c780a8c | -11.16736 | -51.40426 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3e8f9a33-4438-339d-87d9-395be975e07f | -11.1521 | -51.42534 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d0c25ccd-5395-325a-8810-a5427f33f16a | -20.28657 | -46.59047 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| df356974-4716-35ff-9b28-219491efd687 | -20.65147 | -48.68898 | 2025-09-13 00:50:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 43b8deed-3e05-3ecd-abed-2a668a2292f6 | -11.4296 | -43.53535 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 8ccb225b-8635-3061-97f5-10da46e24c20 | -16.51298 | -55.18013 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 23.9 |
| db609b3e-dc46-3544-9e29-809f1c3f11fd | -17.28126 | -47.23821 | 2025-09-13 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7a82871b-427f-3d26-a93e-906f469351fa | -12.56301 | -45.67766 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| b76270d7-7d6a-382e-94c4-0306ad26436d | -11.06151 | -51.50142 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 01b7ecbd-86bf-324c-9790-b1e5845bff28 | -12.65943 | -44.24775 | 2025-09-13 00:50:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| a2d3c12a-071a-39d6-88c1-fa5733f6e46d | -17.41941 | -49.2278 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |


[Clique aqui para ver as próximas entradas](README6.md)
