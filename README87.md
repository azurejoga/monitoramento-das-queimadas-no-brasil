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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6fce463-1e96-3d5f-ba6c-e02a61973b37 | -1.55004 | -52.27609 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29518a2e-46f8-31f4-a487-06a66c61fe31 | -1.21681 | -53.38484 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dae5040f-d8f3-3661-9888-c4e8e49de874 | -1.04333 | -51.73552 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 386ad024-a3ad-3c60-90b2-459b8c64ffef | 1.45312 | -55.89229 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779f6724-1d55-39cb-8f5d-560a201e612c | -1.09205 | -53.3829 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18b700a3-475a-39b8-b896-bf138a267a6c | 0.03711 | -51.10791 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bb39cdbd-4377-3415-a2d1-ed4fea44bdf1 | -1.14503 | -53.70187 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75c62e84-f13c-3825-a5ef-ca005cc54033 | -1.62922 | -52.36921 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61e2783b-c909-3c17-bb6a-ebd4714c948f | -1.06964 | -53.63486 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c0959eb-6ab9-38a7-9751-0536caf3e43a | -1.07294 | -53.63818 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e36b06cf-0295-30cc-94e6-8d137292d5b0 | 1.28488 | -55.92032 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e8c1a30-6e2c-3ef6-9728-8621737f3d27 | -0.29294 | -55.87203 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 371cb316-a3d7-3eeb-aa7d-2f37b4901bb2 | -1.62003 | -52.46045 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8720f7d5-f342-3ad6-b9bf-ef65dfccb5ca | 1.45376 | -55.8963 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7394b2c9-369e-3834-805e-7cd834d0f652 | 1.21228 | -55.95966 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce43181-10b2-3759-b9ed-2e131b40f157 | 1.4589 | -55.92828 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8900d707-cc1e-3fca-bc6a-ad7e2cbd1e96 | 0.34091 | -49.7149 | 2024-11-29 05:20:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c86895f6-9f9a-38b7-b14e-53f8bcb56b43 | -1.09459 | -53.36676 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57aa56c5-66c9-3686-b5c2-e7b83cd55f21 | -1.07385 | -52.33198 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c9a943-bbe0-3d12-861c-9ee86a0611dd | 1.4586 | -55.90373 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1396f31c-fd46-3529-a277-df99cad61f40 | 1.21814 | -55.95052 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c300427-c9cb-3096-b3a8-76a997922088 | -1.40705 | -51.58108 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d5283f8-1de0-3ed9-aa02-7bf23183e9ad | 1.25446 | -55.91272 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 803320ab-fe4a-3a69-a2f6-6b410f8b2411 | -1.2458 | -53.35422 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98939ca6-9613-3236-aa78-76d24491d399 | 1.21061 | -55.97226 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d35f6152-bebe-396c-a947-f0af7e2dc639 | 1.45441 | -55.90029 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 978e2167-5607-33ce-a597-e2148dd11b77 | 0.94403 | -50.73301 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b05782bb-b603-3422-a598-e4b00caf0454 | -1.3876 | -53.64041 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11489b69-72d4-3ce1-90dc-a52d9572fe32 | 1.26914 | -56.00464 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56d0149e-292c-3ed4-ae6a-187ed46d0770 | -1.33086 | -51.92352 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0394a6f7-ec55-3e78-80e5-990881988960 | -0.25157 | -53.76272 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1a797bc-b9d4-3bf4-be31-7c547f68011e | -2.33557 | -46.86576 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9345d7e3-25a3-3eb6-b66d-0185c6f81982 | -2.33951 | -46.87292 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 149269e6-0feb-3b17-8ddc-acf1ec4db4ce | -1.08964 | -53.37022 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ba5e50-4c79-3712-83b9-fceb9c835127 | 0.73521 | -50.86893 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccf3704c-d701-366f-9b28-1c6e4eb7eedf | -1.07354 | -53.63423 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94b6fa9-49ba-3d7a-8b11-e028ebb2dd65 | 1.26451 | -55.90701 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5278eec-8c7c-3a4c-897f-ea0bb874f2e2 | -1.08618 | -53.63631 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24336265-f3f1-37ef-bb3a-f298d5124fee | -1.30676 | -51.73336 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0da20a2d-979c-3719-8d27-0665d91c9ebc | -1.36738 | -52.12946 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31fe7d18-6c0c-3f63-88f9-2d7852021d65 | -0.26886 | -51.62918 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 586ca23e-d3f6-3b49-89df-e638724fe689 | -1.6092 | -52.29512 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1428ae8b-1a8e-392e-b0e1-6bb6a0d8e817 | -1.20768 | -51.74207 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ffca8cfa-3b6e-3bae-98a6-4c9de4a238d0 | 1.2321 | -55.93264 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae5bd495-5af3-3c18-96f8-c95316d10aaf | -1.19611 | -53.87516 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 27e9bd2a-f3f0-31bb-859d-b974888bd693 | -1.36891 | -52.11956 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39f2e658-9303-39f0-8772-909e63a6480c | -1.19669 | -53.87138 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dfd8a350-50c4-3b5c-8f9c-f7ed1f103ab9 | -0.95944 | -51.65192 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdb5e9ba-91c2-3643-9871-212e044f8f77 | -1.55556 | -52.01815 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2d34b9d-03f9-3c5d-8b94-e54d7f697b70 | -1.09008 | -53.39538 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c8e18bf-8de8-382e-89a3-429f18734965 | 0.98558 | -50.26908 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5edd8f5f-bbf9-37f7-b256-fcf38e6b9b50 | -1.16253 | -53.67281 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 353f95e7-3a28-381e-93a9-dae9b2f197cf | -1.25515 | -54.54384 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb1f3ff8-77c7-393f-87ea-b7e180e224e5 | 1.97762 | -60.91645 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8a8037b-83b8-3e05-bf2c-f0f51c781c2e | -1.39322 | -53.6323 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96ab928d-29dc-3eaf-9aff-ab3e8699e497 | -1.53254 | -52.69186 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd86c5e0-9d3e-3b1a-9b59-8d38cc5ad8b0 | -1.36834 | -51.96574 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2c82e5f-2e69-3b17-a5fa-a1bf27ebd4db | -0.88937 | -51.72099 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8367fb08-84ad-3838-bb8a-216fc14c7dce | -1.34855 | -51.96782 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0dd6a00-0747-3b82-a662-b01af058e4bb | -1.52905 | -51.61774 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c8658c-f99e-3993-b0fe-705f0b02c5e9 | 1.85095 | -55.79993 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa12c6e1-8131-3fef-b54a-c7545eef57c6 | -1.16156 | -53.56889 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c8c930e-0558-3daa-91ad-b6e4509e0395 | 1.21165 | -55.95565 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b14510e6-a3f3-3cf3-a499-442c2e75f7be | 0.99023 | -50.26521 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51d842a-d1de-3d8e-9cf3-f91c5e4e5a14 | -0.95859 | -51.65719 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5bb3ade-c7d8-31d6-bb7d-bdac1027d616 | 1.28552 | -55.92433 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8b0fbce-6997-397d-89e2-e2a8341283b1 | -1.08346 | -53.38163 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5bd2b97-72d1-39c6-a25b-50fc7482a6bb | -1.09438 | -53.396 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5642f0b-e60a-3dcd-92f7-efa4bff5e576 | -1.60291 | -52.29102 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3f67f769-1ab6-39fd-aaaf-ece2c735c100 | -3.04839 | -54.41606 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ebaed22-2cdd-3756-8f95-5ab7cc221b63 | -3.20702 | -53.84397 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e742da84-3dcc-34ee-a315-ef47027f1958 | -3.7116 | -51.79417 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f089938-f801-3cf2-a3b1-e4ee60b32080 | -12.41137 | -63.7141 | 2024-11-29 05:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c4d14b0-f86d-3feb-ac00-7c8509937b48 | -1.29947 | -55.74646 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee451b3-80ae-3db7-912e-566ea18f7b4b | -1.69312 | -52.47649 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c87f89-9e45-3c10-b411-41544757de22 | -2.9822 | -53.27883 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4f419c52-6c21-38cc-9f9a-d6ae0ddda84f | -4.43505 | -46.57999 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42bb5bcd-a9c6-3e2d-9fae-748c648639c6 | -2.77445 | -54.03322 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09f8a489-8ef6-3f28-b9e1-e686b63faa29 | -3.35662 | -53.74106 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fa6475a-be5c-37bb-b42a-4458534cd760 | -1.63163 | -52.71833 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8971cbe2-3a68-3795-8ee3-f6ccbbcdbdbb | -3.96155 | -48.0915 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad054599-4eb5-34e2-9ed1-21c7de538339 | -3.47073 | -50.52986 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c394eba1-e9bc-34a1-b34c-4116d2a6d536 | -2.00487 | -51.16919 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ae513ec-6182-392f-96fb-ebea3f0e4a24 | -4.17048 | -48.63058 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e319926-3524-38b0-ba36-98a8080dab50 | -2.01148 | -51.19433 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95193a65-0494-3565-8f1a-5e9e1281c9cd | -1.36439 | -55.17932 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae07011b-1161-398a-99f2-a3f563ab534e | -3.3587 | -52.67114 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70164daa-f223-30cf-9498-501ba2341be4 | -4.07731 | -50.03227 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3493b153-ae0c-3a34-910f-8be68b5e78c2 | -1.94285 | -52.96592 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1941ed8-fc0b-3850-a2a4-3296f688dbfc | -1.65747 | -52.73473 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0640848-ab0c-340a-98d5-ec56af68fda2 | -8.28247 | -48.03045 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c5b912f-66f5-3553-8b7a-4c58630278ae | -4.1881 | -50.68369 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35bd646a-d393-39fe-9735-68f9a693dab1 | -12.41199 | -63.71033 | 2024-11-29 05:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2b7c852-184b-3f4f-beba-991d155b4038 | -2.57339 | -51.83492 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c190bbfb-a467-3c13-a9cd-822eab43a16a | -2.98908 | -53.29372 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 291c4cfa-3677-3b37-94a1-4e7566a8149a | -1.79244 | -52.73899 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4754604f-7075-378b-a54e-5b454fc94225 | -12.25885 | -60.71746 | 2024-11-29 05:22:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8e903c-d6c5-3cc9-aa6e-a036499d010d | -3.07071 | -54.40809 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95b97c4a-7801-33fe-80f7-2459728d1290 | -1.70476 | -52.45217 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| cd6769b7-aa87-3f7f-a6bf-a2fcaeb11dd4 | -4.19481 | -50.68781 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README88.md)
