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
| 3bff37dc-90bf-3d01-8add-ce21d205c6ac | -8.5942 | -62.6505 | 2025-08-10 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3bd5fed2-5c61-3d42-a0cf-656d7449a438 | -6.9422 | -44.5562 | 2025-08-10 01:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c4736c7b-6deb-3116-a694-f6b2bb3284f0 | -9.3806 | -61.5315 | 2025-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 14056195-023a-3846-98d6-ac953cfcf511 | -16.393 | -42.5379 | 2025-08-10 01:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ae0cb2de-ff11-3c9e-ad40-c568461c92ac | -9.362 | -61.5324 | 2025-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 48466151-f968-3552-8926-5e7b4b952b04 | -8.5757 | -62.6512 | 2025-08-10 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1e1fcbef-8e53-3803-b756-394a4b653595 | -16.3731 | -42.5425 | 2025-08-10 01:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9c5e3595-3a49-3798-9e32-f149f277f40a | -9.3622 | -61.5133 | 2025-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1e72e6aa-c76a-3a10-a88d-089012263562 | -9.3808 | -61.5124 | 2025-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 3460aa79-433b-35fa-88a3-b6e00ed47a80 | -14.598 | -47.1584 | 2025-08-10 01:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0d452540-8459-3377-9df9-7c3471dfdc53 | -9.3619 | -61.5516 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 4f1ca6d7-670d-3765-acb8-6df0173d27cb | -8.9398 | -60.7673 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 72452d82-cb22-3565-a3b3-c5456d489819 | -14.4678 | -47.8338 | 2025-08-10 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2a1cd943-1002-3094-af88-1704793515f4 | -9.3808 | -61.5124 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e9c2d4b5-d2d4-3c59-a00e-6329a5616131 | -8.9399 | -60.7481 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| f896dcf9-f5d2-3f29-9b73-124219b2cd33 | -9.3806 | -61.5315 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 890db350-3dd6-322c-b391-bb391d4fc638 | -8.3102 | -44.9967 | 2025-08-10 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e4eb80ab-4a1c-364c-885a-2e527cdd6fd5 | -8.5604 | -54.6973 | 2025-08-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6c887e42-0c18-3ca7-bf65-b6673b12c2ee | -8.9401 | -60.7288 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 90e76d80-23c8-36fe-b429-f38aecdd0bb4 | -16.3731 | -42.5425 | 2025-08-10 01:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 45de6bbe-3909-3b15-9d07-20c8d0e889a7 | -14.2945 | -51.9635 | 2025-08-10 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 862fafb4-4f1f-39a6-a5f0-61a206cc7d60 | -8.9213 | -60.7489 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 46cae54d-070a-3d6f-9040-6ec0601dfde8 | -8.9215 | -60.7297 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 08a75dc3-ea9a-3a55-aca6-b4a1a0dd31ee | -9.362 | -61.5324 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| ae1612df-e4ba-359a-aa62-362237fabb79 | -9.3622 | -61.5133 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 96e87082-e0b4-3f6c-8405-a0e6da4acbe4 | -8.5605 | -54.6771 | 2025-08-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| db0c7250-9d2c-3a21-b763-41a49e4c72ef | -9.3805 | -61.5507 | 2025-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ca23a850-4f79-3653-a51e-ad1eac8e5af1 | -8.5926 | -62.6353 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da4ec3d8-1f44-3304-979e-e629a47d0ef9 | -8.7941 | -63.811001 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98a2c055-e1f9-3962-b632-9a6c7a976bee | -9.6776 | -62.879101 | 2025-08-10 01:13:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f29c622f-ed52-3dd1-8c5a-642ae12a2fff | -9.3702 | -61.519798 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d47e0a03-1d3a-3d42-9c8c-c8d2a0862049 | -11.3619 | -50.551701 | 2025-08-10 01:13:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e81ac9e-e74d-3619-a2e3-d2eeafda3eda | -8.9324 | -60.736099 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39b75abc-a6c1-34a2-a1d6-493d7364653a | -9.3718 | -61.5271 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4bcfb2c-e597-3579-9d45-f0eeaf392f02 | -8.9507 | -64.332603 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a72bc3b-175d-3c08-a325-3fb4c4c71b39 | -9.3685 | -61.512501 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8c79ee-93dc-3ca0-8327-60078529b32e | -8.9245 | -60.746101 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43c5e312-12db-3e92-bf14-f0b41071ac1e | -9.3735 | -61.534401 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf94dbdc-d6a8-3da9-a7b8-784fc4d2d9c3 | -8.5942 | -62.6423 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44752a8a-8de1-385b-bb3f-5ab546ca8839 | -14.2692 | -51.970001 | 2025-08-10 01:13:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 509ffe05-c14e-3f7a-ac9b-9826175d5c84 | -8.9288 | -60.720299 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c82801b-8a3d-3142-ad3e-c61cb8c4a4fc | -8.9306 | -60.728199 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d583aca-e4a2-355a-80cf-e58b9764e878 | -8.9342 | -60.7439 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3c7c2f2-f750-3eba-82f5-665827b32849 | -8.9263 | -60.754002 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8173479c-0626-3595-b73e-e5b89e7f0d31 | -9.5572 | -62.7094 | 2025-08-10 01:13:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3225d4c4-e714-3b35-bdfd-7d0d78ae20fe | -9.6791 | -62.886002 | 2025-08-10 01:13:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cfd4751f-9a94-30f4-ac23-ce85d6538ca7 | -8.5828 | -62.6376 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a39236b7-638f-3d90-a971-1800ecb35623 | -8.9191 | -60.7225 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1c0b6a1-52ef-38fa-865a-048d99849af2 | -9.1907 | -59.672001 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff137db0-c117-3b1c-a503-0022475d14a5 | -14.2849 | -51.990002 | 2025-08-10 01:13:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b47376c8-7ae6-3428-893e-0f48cf5271f4 | -9.8194 | -63.007099 | 2025-08-10 01:13:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39c6d1db-b5cb-3cf0-ba84-c3aa34780731 | -14.2788 | -51.9673 | 2025-08-10 01:13:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 919af0d4-0a5f-336e-bda9-6fcd9fef632e | -8.9209 | -60.7304 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc045be2-9133-3eff-8c80-8b9bae2ec52e | -8.9227 | -60.7383 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12d6c75c-008f-3254-936b-11d16a07b990 | -8.9361 | -60.751801 | 2025-08-10 01:13:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a94924f9-2e1e-3c45-924d-6fbb7588723a | -8.7956 | -63.818001 | 2025-08-10 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69fbd987-57d2-3c54-94d8-994cbb72c632 | -9.3806 | -61.5315 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 207.7 |
| bc8cc40d-2706-321e-81d4-c1f3e5a28e22 | -8.9213 | -60.7489 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 174c3336-c910-3364-9e90-b9bddc551064 | -8.9398 | -60.7673 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| aea07304-cbfa-3c0e-9269-fd5a460d881b | -8.3105 | -44.9738 | 2025-08-10 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 695b9f69-f879-39c3-9020-51ac5d3d8439 | -9.3808 | -61.5124 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c9051be6-6060-312c-8b19-89c00113bd23 | -8.9399 | -60.7481 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| fe780366-833e-344f-b2dc-f32989b3207e | -9.3622 | -61.5133 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 86a79eae-3025-36bd-8beb-eeb99e69a5a1 | -6.9422 | -44.5562 | 2025-08-10 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f13e6789-9310-3922-9377-641eb4e4cf58 | -8.5605 | -54.6771 | 2025-08-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3b5934a7-1b5e-363f-b797-be77cecd59e9 | -8.3102 | -44.9967 | 2025-08-10 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 2405c5c8-d0eb-3aa9-b080-391e4b21a8fd | -16.3731 | -42.5425 | 2025-08-10 01:20:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2c3c304f-2db0-3e2d-af2d-e1ae688cd658 | -8.9215 | -60.7297 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| d14ecc59-2937-3a79-9121-9dd0168a6da5 | -8.9401 | -60.7288 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1fbc6009-587c-3aed-bd0a-c090f5519d5f | -14.2945 | -51.9635 | 2025-08-10 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b911b841-622f-3d73-a90b-88b0ba99f762 | -9.362 | -61.5324 | 2025-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 8c170263-08dc-3aee-95cb-0c9b0b6d3f03 | -14.28502 | -51.98668 | 2025-08-10 01:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| b99c8829-51a2-3817-b65e-be1217ba13cf | -14.29945 | -51.98407 | 2025-08-10 01:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 79eef822-2ae7-3d1c-8960-95a66ca6c32f | -14.28033 | -51.95995 | 2025-08-10 01:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| a156d8e6-e8a9-3987-8c78-a03646320348 | -14.29477 | -51.95721 | 2025-08-10 01:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 61044a6f-a8ab-35d2-b13d-7b8cd0fe51eb | -9.19436 | -59.67243 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08b1013e-21a9-3c5e-b2fb-c9954b452658 | -8.9395 | -60.73608 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e73c0b29-4888-31b8-b355-2acb3f3b5185 | -8.92425 | -60.7566 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0caaa029-1d42-3c7f-82a7-609575c2b341 | -8.93313 | -60.75531 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 43075b1b-6c1a-3d2c-a393-d1ca9b187b8a | -9.8236 | -63.01654 | 2025-08-10 01:26:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b1827418-6e42-376b-a168-5b70b418f64a | -8.93187 | -60.74635 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d34a2da4-84e3-3cb6-a4a5-199de57a1dd4 | -9.18359 | -60.82842 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13ac77f5-6fab-3f55-8e65-e176c45cacad | -8.92936 | -60.72841 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 40fc3cbd-6156-396d-975a-b79e355b78a7 | -8.94075 | -60.74506 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| afd52a59-97a4-37f3-9dfa-d8f1c4f01898 | -9.37451 | -61.54102 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9c7c0fe5-4fb9-3a24-96eb-2d0d38b8899b | -9.37205 | -61.52315 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 220.1 |
| db0bbbb9-c8f7-3056-82cb-a675c4ff3509 | -9.20347 | -59.67105 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c5cab8fa-fda7-3710-be4a-f4248df4f730 | -9.25914 | -60.77501 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e985ddb-4455-3a18-b82d-e60e401b3492 | -9.19573 | -59.68192 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 66d1fdbe-dd1a-3624-855b-933c5dbad6d3 | -9.37328 | -61.53208 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| c9864e7e-f529-3e99-9b53-9b035d04de3e | -9.36442 | -61.53335 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ce59401-c25c-3c26-b262-ca00d2d59b25 | -9.03161 | -59.75756 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8ebed53a-0ef9-31ae-98b0-3934cb468165 | -9.55297 | -62.72118 | 2025-08-10 01:26:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c18ded56-4195-3213-8aae-b0895e8c0379 | -9.37574 | -61.54995 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 563f1a98-16da-3a0c-bfea-3ecdfa00a763 | -9.71026 | -61.30452 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98b9ee84-9ed3-3f14-a37f-fad86309c15a | -9.20484 | -59.68055 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9cdfb12-db7b-33d3-b729-8e75b584a9f7 | -9.67619 | -62.88371 | 2025-08-10 01:26:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e8a1ddee-9446-33ff-92da-78178b14becc | -9.67749 | -62.89343 | 2025-08-10 01:26:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| af310621-ec02-3bb5-b65f-78a1ee4c4c5f | -8.93062 | -60.73738 | 2025-08-10 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0d9f960f-027c-3b46-be72-31de4d628e22 | -8.9401 | -60.7288 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |


[Clique aqui para ver as próximas entradas](README5.md)
