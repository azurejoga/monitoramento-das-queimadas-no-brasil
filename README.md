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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4615a29f-7dcb-3cc1-be91-f7a36332fcb1 | -9.0415 | -65.7349 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b0ef861c-b874-33da-a504-f5a35449cc8e | -6.2275 | -60.018 | 2025-08-26 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1e74ba92-8365-3d7d-be5b-5673d320f774 | -8.2193 | -49.5544 | 2025-08-26 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c5c91ca3-4fe1-3e6c-a7a1-ea48db27173e | -9.1724 | -59.4436 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| b31e082e-05ec-387b-b0d9-ff864d3124f8 | -8.352 | -62.9436 | 2025-08-26 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ce62a9d6-a5f6-3334-a563-4fca555abc53 | -11.54 | -52.119 | 2025-08-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 258.4 |
| c87cab0e-a904-36fc-a196-8ec9559bdec3 | -7.3541 | -59.6669 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 31a41c0f-48ad-3a0f-8723-f4a914ab19a3 | -9.2677 | -56.91 | 2025-08-26 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2b1ee85a-b893-3e26-adc3-c946b4c60e19 | -6.9128 | -59.3578 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 1c73bb51-8c86-3a49-8730-1a284a59dc48 | -4.9606 | -55.8028 | 2025-08-26 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8f50a862-7eef-3b7d-baba-53abdaa18de1 | -8.3209 | -50.5667 | 2025-08-26 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 668ee5db-763c-3f50-989d-993c67122474 | -9.1722 | -59.4629 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 613fd49e-a4e3-3f9f-b5ec-56f9d78ea1c1 | -9.2362 | -60.9064 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 76e98b08-7a50-3f5b-956a-d164186fc362 | -8.9874 | -65.4192 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e58463e0-dc31-3c82-a58c-9c2a827785f9 | -11.5592 | -52.096 | 2025-08-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 02d99e84-fa23-37e8-a9b3-bd6708bce013 | -6.246 | -59.9982 | 2025-08-26 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7310e5a6-7f81-3dfa-8489-4a02558a2850 | -7.367 | -64.348 | 2025-08-26 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 84972df1-351a-376d-b4f6-462a1d022684 | -22.8987 | -49.0569 | 2025-08-26 00:00:00 | GOES-19 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 81958b4d-6c35-30d2-abf3-9f6e0b2d8157 | -16.24 | -58.7185 | 2025-08-26 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 9d349bd0-1a1b-3772-9984-139547b8f110 | -4.9605 | -55.8226 | 2025-08-26 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 15bec86b-e8cf-3cd4-a43a-3d6d91955a6d | -8.9689 | -65.4198 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| cc73163d-61e9-32ab-b3cf-e44a33de728c | -10.4241 | -64.3903 | 2025-08-26 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 974733d4-d7b1-390e-afdd-4b9d18f2607e | -11.5587 | -52.138 | 2025-08-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 7026f827-ea9c-3f33-bd25-18913cb44cf9 | -9.0231 | -65.7169 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a1407b1e-95c1-3581-bea5-bf25288638ac | -9.1909 | -59.4619 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6d67a365-4be3-35ce-b62c-e69e1235d873 | -10.7597 | -47.0648 | 2025-08-26 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| da6c2b67-2ffc-3075-a53a-b12ae5c5fbca | -7.3854 | -64.3475 | 2025-08-26 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 325.4 |
| 6d8db79f-3c45-36fe-826b-15dc0102a604 | -22.9197 | -49.0517 | 2025-08-26 00:00:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7ce46109-5cfb-3cb1-8f0d-7150a90841e4 | -9.191 | -59.4425 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 63b271b9-b0c8-3bfd-bb96-532d86cf90da | -7.4737 | -61.3466 | 2025-08-26 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 44b76a3b-6cbe-3540-9c2b-972786dbf5f3 | -6.9127 | -59.3771 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4bb71eba-3667-34dd-a70a-3f7595a742ec | -6.8228 | -58.9753 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6538f7d5-3edf-305f-9798-403a12425f64 | -11.5397 | -52.14 | 2025-08-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| a31fa8a4-878e-30d4-9545-55605984a4fc | -10.5174 | -46.7591 | 2025-08-26 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8ea50e29-5d11-3525-9d67-b34fb0191f60 | -8.3394 | -50.5863 | 2025-08-26 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c65b61d2-55b4-3f3f-8d76-9c2ad8973431 | -7.4736 | -61.3656 | 2025-08-26 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0a4b34ae-ebda-3660-8191-494db2b225a5 | -10.76 | -47.0424 | 2025-08-26 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e7d72e35-5a70-371e-8ef9-c11f13adcd43 | -7.3854 | -64.3662 | 2025-08-26 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 180.1 |
| c242cb3b-1f18-3e2f-b169-d4a012a5f1aa | -9.236 | -60.9256 | 2025-08-26 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 53a3b6b2-a15f-33a3-8689-3edd962a4210 | -8.9873 | -65.4379 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 406f8091-6f14-3141-b234-64320dc3fbba | -6.2459 | -60.0174 | 2025-08-26 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 8008d1db-536d-306f-b7c9-31758aa45726 | -6.7144 | -58.5732 | 2025-08-26 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 79c05ca9-60ca-3722-818a-31b79e703a9e | -6.7819 | -59.6711 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d4d8f27d-7510-3c56-a6b9-a6049643e440 | -7.3669 | -64.3667 | 2025-08-26 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6de66244-86f5-388e-a100-af51a12c5f99 | -10.741 | -47.0448 | 2025-08-26 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5f4e4da7-c3f3-37a5-99dc-397b975ceb18 | -8.9688 | -65.4385 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| a3847ba9-c420-33a0-9558-83d2b20d83b2 | -10.7406 | -47.0671 | 2025-08-26 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| ead3d14d-c12c-3f18-917d-9d6f97a23094 | -7.4224 | -60.6236 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| f137c8aa-35af-36e0-8e73-2abd7b69788e | -6.8229 | -58.956 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| bf48db62-b374-3625-9d7a-bc5154e83938 | -6.7635 | -59.6718 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 3af18593-687e-32e9-a852-3663be2174f2 | -9.0416 | -65.7163 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8fd41ecf-4c0c-3f42-b083-79ab3ff2c1b4 | -7.4039 | -64.3469 | 2025-08-26 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| de9b712e-b1fe-34e0-870c-902c0db391be | -9.023 | -65.7355 | 2025-08-26 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7a9f3a7e-2150-3583-857c-514f54452cfc | -7.4225 | -60.6044 | 2025-08-26 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7d79b989-4e87-39fd-b465-131996d4a503 | -11.559 | -52.117 | 2025-08-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 232.1 |
| ecb4b54c-7fc9-31e6-a8a6-69f2599d8dcb | -8.3396 | -50.5652 | 2025-08-26 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| f77aaa72-a6cc-386a-929c-c24e47b5b7b3 | -5.5281 | -60.2133 | 2025-08-26 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 21ee7c43-a66b-3867-9a6f-3d8e1d5fe073 | -6.7145 | -58.5539 | 2025-08-26 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 67755c3d-f1de-3170-ac38-5a0609b2e2a5 | -6.6961 | -58.5546 | 2025-08-26 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 96e12694-f9ce-3cfd-8de7-5279d2568ac0 | -14.7903 | -49.1847 | 2025-08-26 00:00:00 | GOES-19 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 16832372-8fbd-3034-9223-c02bc0ccdafd | -22.8994 | -49.0334 | 2025-08-26 00:00:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4c1d7aff-e4c2-321e-8ecf-32ad19afc818 | -11.6277 | -46.3899 | 2025-08-26 00:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4b7ee0fb-208d-3472-8dc8-255e29ff84b7 | -6.6961 | -58.5546 | 2025-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| add93ecf-3a2b-318b-be26-576c9ae3d683 | -7.3541 | -59.6669 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c584971c-a200-34e6-8c38-26057503bbce | -9.1722 | -59.4629 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| e230849f-9b7d-3098-924b-501871404019 | -6.7635 | -59.6718 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 246cbb11-fd28-3388-a2e9-6a86f82da03b | -10.7597 | -47.0648 | 2025-08-26 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| bb6c4f27-f326-3b06-b472-3ddb0bd42d6e | -6.8044 | -58.9568 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 971e5287-75c0-3a81-81d2-1f6ce7b8bdb1 | -7.3854 | -64.3475 | 2025-08-26 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 298.6 |
| f009bd71-7961-3fbe-b4e6-ecddd5758924 | -6.2458 | -60.0365 | 2025-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c22bb5a0-e702-3435-aa7f-95c30ade2b78 | -8.9688 | -65.4385 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9aba3373-df99-354a-9405-c079f1ef3261 | -7.367 | -64.348 | 2025-08-26 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 1a707360-a650-330d-9418-46a8cbe49f5a | -11.6277 | -46.3899 | 2025-08-26 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 877ee911-8f85-3c12-9a1e-d5a4176257ad | -13.1644 | -45.2897 | 2025-08-26 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| df67a801-9052-37b2-a2c0-1d774e918bab | -8.3209 | -50.5667 | 2025-08-26 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 636896f2-3369-3272-8b03-97f6c449bfb3 | -9.0415 | -65.7349 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| eb1670e7-162c-32c9-9be8-b430941ca281 | -11.3126 | -55.1112 | 2025-08-26 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e9c14b18-e7ad-3e31-9a37-3630be008f2d | -11.5587 | -52.138 | 2025-08-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 8a978a48-388f-38a1-b0bf-c0db913c61a1 | -9.0231 | -65.7169 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dbe00f71-2963-37f3-b7d6-d145ba2fa6a3 | -11.5592 | -52.096 | 2025-08-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8aa940e7-4095-3d83-8c69-71fa0bfe4f75 | -11.5397 | -52.14 | 2025-08-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 250.4 |
| 9cae7cd1-d472-3a63-b7eb-e3e93175cab3 | -6.7819 | -59.6711 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| d1acf826-f6aa-3afd-8052-bf28a6634a7c | -9.2677 | -56.91 | 2025-08-26 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 360ba628-9440-3e37-aaa8-f4bf7c803736 | -9.1724 | -59.4436 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 444eafe6-ad4e-3418-a1e9-dc5fa3a01199 | -9.236 | -60.9256 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 30e82ae5-8fec-3111-b81d-e5105831da87 | -6.7145 | -58.5539 | 2025-08-26 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 860fe9f4-dc9a-349d-b83a-2b208a3315f3 | -7.3854 | -64.3662 | 2025-08-26 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 231a0379-58d4-3c48-958e-3cb0d6e3f29c | -6.8229 | -58.956 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.1 |
| c1ae959f-fc3f-3e5c-abdb-b763e71cd437 | -7.4224 | -60.6236 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 18a17701-7fd7-3252-8b07-e46efd2a02d2 | -8.9689 | -65.4198 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e8a7d4fe-d1ca-3f06-94ab-9652c6daf5d0 | -9.181 | -60.8131 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a0302aaf-b8c2-3cfc-badf-0451b96ae486 | -8.3396 | -50.5652 | 2025-08-26 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 4f6b1ee0-e015-3588-b561-ef171d7ee590 | -10.741 | -47.0448 | 2025-08-26 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| be6b483d-3bed-3967-b559-8834bfff25f5 | -6.9128 | -59.3578 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 93d7e827-1fe6-3372-b450-ba135e332df7 | -6.8413 | -58.9552 | 2025-08-26 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| b06d2506-6ba3-3876-912e-4dde97f67f52 | -9.023 | -65.7355 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 02949e86-aaf7-3ce7-948b-b1536f68c7f7 | -10.7406 | -47.0671 | 2025-08-26 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f31f17f7-fa8d-3363-9d31-e72c00ead286 | -6.2276 | -59.9989 | 2025-08-26 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a70e49fc-f8d7-3706-9f14-5628da21cf4e | -9.1909 | -59.4619 | 2025-08-26 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| aefdf63b-b172-33a7-9c4a-2e1a67f8c3a6 | -8.9873 | -65.4379 | 2025-08-26 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |


[Clique aqui para ver as próximas entradas](README2.md)
