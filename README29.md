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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3284a4fc-145c-3094-86bd-7d3eefbc3794 | -11.2658 | -46.3485 | 2026-10-10 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4f9d6685-d652-3a99-a10e-25a95c8cb238 | -11.2467 | -46.3511 | 2026-10-10 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| bfb1a80e-280d-3811-a424-8187bd3a2a41 | -6.4566 | -55.5008 | 2026-10-10 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f6481dee-b64e-38ea-9a61-5dafc6ab2dfc | -4.4025 | -49.7774 | 2026-10-10 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c59a873b-bebf-3181-aa9c-43d1c78c904b | -11.2662 | -46.3259 | 2026-10-10 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a6741e67-f184-3055-b43e-2c64b29ac708 | -7.535 | -45.3006 | 2026-10-10 04:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c23e07e1-3d5b-3bf5-870e-15e44234a203 | -7.5347 | -45.3233 | 2026-10-10 04:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5bb74b76-c0d5-3bbe-95d3-a49e0eea4fdd | -3.9912 | -59.356 | 2026-10-10 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bab98bef-1d55-3656-bed1-35e85b429b25 | 1.00258 | -51.0965 | 2026-10-10 04:06:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ffc94fb9-2c07-3da2-a8ed-c6b4b4eb984e | 0.47488 | -50.79437 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 53f56b9e-9ea1-3f9f-85bb-f9631bb3b867 | 0.28456 | -51.4145 | 2026-10-10 04:06:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ae6aa17-ebcf-386c-af9c-82e48335e947 | 0.94211 | -50.19677 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87c8c102-563a-3f77-b1ef-6ff4fdd0d48d | -0.983 | -52.44599 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54fc3180-f3b7-39da-9c0a-22946449a9bb | -0.98214 | -52.45122 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd4dc72c-90aa-30a4-adf7-084fd0779bf4 | 0.47421 | -50.79015 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5257eff1-5400-3b0d-a077-cbae4f748494 | -0.87838 | -48.71927 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7cd63708-0792-3df2-aee8-77c6aae308a6 | 0.29603 | -51.40787 | 2026-10-10 04:06:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86d5ce6a-64f1-341b-88e8-887d979efdb8 | 1.53777 | -50.89823 | 2026-10-10 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a5e9288-22ff-35cc-83da-01d03a9bd83d | 0.94271 | -50.20073 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa867941-57f8-351c-9450-8d8cc6cf50df | -1.79705 | -47.84706 | 2026-10-10 04:06:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94698927-c4fa-37df-a613-31b190165189 | -0.88431 | -48.71423 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b3795cf5-0a95-36c8-8e33-727b40c599e6 | 0.47948 | -50.793 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a98ece90-82bd-32bb-bd4a-d929c6002d98 | -0.98054 | -52.44918 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4f6dbf2f-c444-31a2-b4c6-d97104c1fb20 | -0.88477 | -48.71133 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| def0fd00-4f3a-3637-92bc-d0527927be07 | -0.97661 | -52.44498 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecb1ef3e-95e0-36d6-b144-ef34dfc98da9 | -0.97488 | -52.45545 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63628a5e-7789-3e86-8a81-6eb099a47bda | 0.48077 | -50.79348 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 31f965f5-625a-337f-b8a2-3ca4548fbc52 | 1.5431 | -50.89286 | 2026-10-10 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89edd9a5-dff4-3584-8e12-e10425369fee | 1.54448 | -50.90177 | 2026-10-10 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb01d872-bc9e-3ed4-b8b5-e945c26aa74b | 1.54379 | -50.89733 | 2026-10-10 04:06:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feac1526-7bee-3e2a-a719-f65ce3426af4 | -1.74192 | -47.16372 | 2026-10-10 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6124f36b-1fc9-3aa7-82c1-353906a058a6 | -0.98136 | -52.44395 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55e1c253-a88c-378c-bd7d-6b6ef4f16661 | -0.87884 | -48.71636 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8a3c131-e7e6-377a-b6e2-e325213014c0 | -1.79629 | -47.85189 | 2026-10-10 04:06:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d8a8bb2-3cc2-3ba2-8fc4-af42baa904ae | 0.47359 | -50.79391 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ce4b8da2-7edc-3d2d-8f6a-8ce932036aaf | 0.47884 | -50.78877 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e547ae4c-ddf7-36e5-ab5f-cd83d9dba436 | 0.29065 | -51.41348 | 2026-10-10 04:06:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82efe5a3-ba66-30c8-b6de-180583090d5e | -0.97402 | -52.46066 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71be9dff-4937-3a88-ad56-4751f10063ee | -1.02475 | -52.43099 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 851f39e2-c87a-3cb6-8eb4-c71072e1db69 | -0.87428 | -48.71267 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e806a3-ec9b-33cd-ae98-a501b3389993 | 0.28993 | -51.40886 | 2026-10-10 04:06:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7759068-0099-3f8e-b51b-6735bb16beed | -0.91663 | -52.43888 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50a930ec-e99c-321f-8ba8-ef84b1748a42 | -2.87004 | -40.01295 | 2026-10-10 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1b558c5-f8d3-3b40-b104-688ed1ac83de | 0.48009 | -50.78926 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cdfda8e-5efc-3f46-930a-ac555292decc | -2.86672 | -40.01244 | 2026-10-10 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa50c3f6-91b4-3933-91d5-782f36ca0335 | -0.8793 | -48.71345 | 2026-10-10 04:06:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 934fd65f-3989-32cf-a7f3-6f73d87c34b0 | 0.48598 | -50.78836 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a046771-f756-3982-b71c-facba519310f | -1.02559 | -52.42577 | 2026-10-10 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06f1249c-fa6c-3f50-b725-4209191cc38f | 0.48472 | -50.78786 | 2026-10-10 04:06:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 083c3f4e-1c70-33d5-b8d3-d2e16223adf1 | -3.36293 | -50.47838 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d859fb1-fa16-3ab5-98bf-366411a38ad5 | -5.61826 | -44.84847 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06383a05-2e28-399b-b7a9-6f970dcb1904 | -6.37327 | -55.17286 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c964c33-9fab-32b7-a2e2-94153406fca8 | -3.39118 | -44.48626 | 2026-10-10 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37650113-dab5-35b9-9041-bfae185125e1 | -3.47177 | -50.08977 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 70891b14-3413-3228-9743-89900a68360d | -5.04625 | -49.3534 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ede1133e-ceee-3966-b6e2-02ec3642843c | -9.27305 | -45.62457 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d9ae647-a94f-32ae-8739-b879dde5619e | -3.20091 | -53.85447 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a3dc823-dd8c-306f-973d-4d430528e394 | -6.99229 | -47.70397 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 769dfa37-c434-3a86-86c6-2dc21db8a1ca | -4.13816 | -50.82323 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c42d8918-fd3f-3511-bf99-6b34d4b83c7d | -3.12443 | -54.17124 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d2c8f8dd-52ae-3c60-8d31-bd65ac56ebce | -5.08737 | -46.20795 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03b165fe-7a91-3693-8767-306e2727fdf2 | -8.97983 | -45.89767 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd4a9678-b8e7-3f24-bd21-23673bf92b55 | -4.93039 | -45.78541 | 2026-10-10 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16ae202-a2ed-3ca1-b544-7e5a23ff17c7 | -9.9378 | -44.79236 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a8847ab-7bd7-3ecf-b7c6-86d2f2a5958d | -6.77667 | -48.66463 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b4191eb7-3958-3245-8bf6-d1fe5977ed36 | -3.46807 | -50.07937 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7faef7d4-31b9-3631-bfc8-bdebec6d7ace | -9.90537 | -44.77973 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad13f4f7-30c3-3dc4-bc2f-f92781508831 | -7.91747 | -54.73466 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5668944f-b0ae-3ed3-8014-83b552e02346 | -5.23751 | -45.37453 | 2026-10-10 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d44b147b-8117-32c6-af52-da90814518f6 | -1.62823 | -54.43531 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71283447-84e6-3616-9c17-0d03d8d92ace | -7.1228 | -42.5451 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5e5022ef-6495-371a-afee-a0bdb156a3e3 | -5.87589 | -50.09693 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9e2da0c-3001-3647-bf2b-e0315ad454c3 | -3.18394 | -50.59641 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed28f847-9162-30b2-941b-77ba50c356fd | -7.11837 | -42.53011 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 384552e3-6965-35b5-80ea-cc05d5c8555b | -10.28006 | -43.94614 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c9294b4-8bff-3a36-91ad-901ce29863e2 | -8.95906 | -47.38062 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff1e0bf8-939f-354b-8cfe-898a04047715 | -8.9286 | -45.13931 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6871dfa6-10c1-3617-a3bb-6ada5cbda150 | -3.5021 | -49.93851 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 366d9181-b6e6-3d7a-b3b8-b43b1cd8e6b8 | -8.63373 | -50.22335 | 2026-10-10 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8e3cbbe-bd83-39f9-a300-f2dfe44718a0 | -6.13403 | -53.09972 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d4590cd-aeb2-3871-bb9f-6ed122ab44e9 | -2.85525 | -48.72114 | 2026-10-10 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf2d974-d5b3-3db6-ae66-962ed92cba38 | -3.341 | -50.41064 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 818e7dbc-e5bc-3803-8b05-d3431c65e6dc | -6.47018 | -55.07076 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7cd1273c-ae33-37e5-bd4b-ea1b01de7a61 | -4.10663 | -54.01405 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c787c04e-33b8-3be2-81b2-44b9db6ab036 | -8.98832 | -45.88905 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fbc1aa12-7bf7-37f1-82ce-3e2e107ae225 | -4.07954 | -44.91943 | 2026-10-10 04:08:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9721c62a-3538-3f18-9787-6062af1dfbef | -5.599 | -47.28035 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f029d9b8-a9a2-39df-98e6-79919a3ef391 | -8.9496 | -47.379 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9938dbb-3da3-3713-a8a8-7c943542f982 | -5.7187 | -53.48985 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ff45fc7-f1f9-36f3-9572-556a1e81bdbd | -5.11261 | -46.22761 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab03570-6734-36bd-8166-8d385242a492 | -3.03987 | -50.34493 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 607b0dad-f8f7-3793-9477-b3ab12b1b036 | -9.30058 | -47.38979 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42bde4d2-2208-3c72-a071-c0d7942194b2 | -6.81915 | -39.54749 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5fa507c-f8f1-321c-9ff2-f07d6e0c74ce | -7.90546 | -54.72608 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52ebf048-0f3d-33a1-b533-a9ebe295245b | -3.25376 | -50.42096 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8495ffc3-e45e-37aa-a1ab-d137e3b38e93 | -3.4676 | -50.59713 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1f27b11-4276-34d0-afc4-2a58d131be83 | -6.0902 | -44.26576 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94808337-484a-3e24-b673-bbd12dfd553f | -2.82636 | -51.28422 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16aac3bc-45c2-313c-928d-87779b8a2def | -3.57695 | -54.70826 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a6b52b8-2191-35ce-832e-32ba09258455 | -3.22426 | -54.29096 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README30.md)
