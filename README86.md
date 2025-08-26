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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa54de62-3279-3f28-bfff-3ade06c13aee | -8.57003 | -63.92409 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aae06067-ab03-3f4d-ad1a-6faf7a272f8f | -9.2727 | -56.91327 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cd59816-946c-3e68-8a9a-9f435472c86a | -9.15735 | -59.54176 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3817edc8-1b68-3bf8-ae97-0dd780ca0fa3 | -9.10525 | -61.42661 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 591239b5-f440-30ef-bc2f-50e523b87d9a | -8.97933 | -65.41216 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae4ae6ac-5e50-342d-af86-104721c44cae | -9.18535 | -59.51722 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1126ac45-6208-37f6-b6a1-7489161f447d | -8.5801 | -62.60413 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6561babe-dd9a-3fff-a5b3-9cded02034c3 | -9.15637 | -59.54878 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dddb27f0-d303-36f7-b97b-aaae9b4c65ed | -9.18282 | -59.50603 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 816c415e-7dbe-327a-b7e3-984236d05253 | -9.02798 | -65.72632 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e15d1136-5d0a-3e5d-9452-13f4614f63ca | -14.29764 | -60.36609 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c803eb2e-5517-3590-9d37-c51b63565d7c | -9.64523 | -59.64148 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90dcd90b-fec5-3e39-a2c3-35cd8a85ab96 | -9.15658 | -59.45868 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66d666d0-56dd-3ab0-a17e-e12233a10049 | -9.18228 | -59.48066 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc2f42e5-f427-3149-b626-3dc104a3881d | -9.17786 | -59.5413 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28d5381b-3353-3625-8ed6-2660eb3d2d30 | -8.66779 | -63.86444 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f55073a-8a1b-38fb-a5de-7cd1ad894d1d | -11.31303 | -55.10991 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feba0367-b84c-3153-b300-74e659e073d0 | -11.55576 | -52.1223 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a17ac01c-26da-30f9-8296-1c90d91c9bb6 | -10.40975 | -64.40569 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b6e46d2-53c0-3b93-bd3e-5f5a4b17193b | -9.25398 | -59.7688 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899869bb-23e8-3e43-89a0-6858bb152a8c | -9.80781 | -64.25254 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96d1c9a6-c672-39e7-b485-99df99e05f3b | -12.07361 | -63.14566 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 966f0462-7cd0-3938-9ca6-b712f5d3939d | -8.9871 | -63.6454 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0aee56f-8a5a-35ee-8ffb-bb382e71f74d | -9.0917 | -65.72922 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 213e46f0-1c97-3ec1-9428-bb4055ca50d2 | -9.23859 | -60.81913 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71efea4b-22c9-37bc-8a31-1ff9ee05fe22 | -9.19135 | -59.50367 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c26998ac-a465-34df-8635-02f610d22743 | -9.25527 | -65.62403 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 051134fc-6ea8-35ed-a993-2d4802005cf5 | -8.55124 | -62.63362 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30854563-57fd-33c3-93af-e0bc846e9af6 | -8.35227 | -62.93133 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3efba7f3-480b-3bc8-b57c-a03c34ac16a7 | -11.57271 | -52.11722 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6b7eb64a-36b5-3db1-a800-83248d8eb52e | -11.29841 | -53.9614 | 2025-08-26 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0666bc2-8087-3886-a04d-af3822daf4e4 | -12.33711 | -64.22855 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 222d2cf6-1c03-3760-84c6-48a228eab5ae | -9.01524 | -65.69852 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b329e552-2e32-32d1-9805-952b619b60e3 | -10.54133 | -63.0125 | 2025-08-26 05:38:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69485e5e-8bae-3db8-b467-aebbaf2f1aaf | -9.08138 | -62.67568 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5bb77c2-ca9f-31ce-8725-78ed46e5f92f | -11.53489 | -52.12568 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 36a45f51-0013-347a-ac3d-47a669663368 | -10.90593 | -68.43609 | 2025-08-26 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d2da43-1675-38ce-b9f9-52b497de5096 | -9.07775 | -65.7159 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 44cc4fbd-2861-36d9-96ad-a3bcce84dec5 | -9.17885 | -59.53426 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7699229-0528-31df-8d11-23e66969ac19 | -9.18546 | -60.79299 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b7eeea-616e-3edd-889f-2e03ca91d95e | -9.58189 | -55.37131 | 2025-08-26 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a370077c-881a-38f6-8f49-85a0d345f804 | -9.00156 | -65.40121 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb974977-23ff-32d8-8c50-ac483aee49cb | -8.84972 | -62.44623 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6a6cce08-266f-3e78-9443-89703f994d96 | -9.17721 | -59.45813 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e023251d-6657-3fd2-adc5-2f7cfcd2f925 | -9.19086 | -59.5072 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6be97b2e-cedc-3702-98f3-080e78a4d192 | -8.85427 | -62.43924 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3e6662c-589a-3d99-b298-936f4253f3fe | -9.25616 | -59.63786 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f78f7a17-445a-3a12-ba58-046d51a9ba4b | -11.56252 | -52.12296 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3dd3180-7773-32f0-ae3b-0029703f4f49 | -9.03411 | -65.73098 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0430157b-7310-3b7f-8e30-5ba2b6001092 | -9.16831 | -59.52185 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c28403b7-2b2a-3b4e-ba8e-9f0ea5862279 | -14.63434 | -59.5559 | 2025-08-26 05:38:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77acce7c-609f-32e9-9c01-542c7375faec | -8.3489 | -62.93081 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41161dd8-e32c-3a55-af7f-811423ed3dca | -11.57062 | -52.1118 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0031d6d-cd1e-3847-951a-0f0f10bfb7f8 | -8.57842 | -62.63781 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e1227bb-99b8-3451-84cc-5afb345dc76e | -10.74606 | -60.72066 | 2025-08-26 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9edc4b-6b2a-3d01-a933-ece8ca1e01b5 | -8.97877 | -65.4157 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf3b8dbd-9713-3c0e-a5a5-857aac887586 | -8.98045 | -65.40508 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcdacc41-6b22-38be-8d73-1253d4bc605f | -9.27894 | -56.90339 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f6a1ac-5ebb-3eec-b0e8-523f13baafd6 | -11.69602 | -60.17056 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16fd041-d66e-3667-97d2-edee1d4340d2 | -9.18853 | -60.79805 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9f858b5-1074-3663-a379-42f02360cc69 | -8.05625 | -63.8605 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d5f40e7-f155-3f0d-85bf-8b63782158f4 | -8.97098 | -65.42171 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91f87c11-d404-3ccd-aaf3-b03f03ad4e71 | -8.84231 | -62.44893 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85a270da-5074-3003-83b6-f964325f18c4 | -9.01711 | -65.38921 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c37964-577e-34d6-b272-0a77784cd3bc | -10.41854 | -64.39275 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8862dc0-50df-3b0e-a574-96aeeed03148 | -8.85658 | -62.44728 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7cc2ca47-1678-3a00-b1d8-c060604f0f5c | -9.20241 | -59.51248 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f6b696-ec19-393e-ba64-b6d3c970a244 | -8.97375 | -65.42578 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2689f2bc-c957-3a45-bdb9-9c073f3c6317 | -9.62726 | -61.46438 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95cc975b-6a15-3d81-b4bc-a75c25af4153 | -9.1893 | -59.45995 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e7f75d-85a2-37a4-9ff5-d0504b595fc1 | -8.34836 | -62.93441 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28092add-27b9-36be-b92c-bea142bb2a0f | -9.81563 | -64.28955 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02ed4662-51ee-3814-bf9f-05ab74127f6f | -8.87259 | -62.45741 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0d22f2b-c689-399e-8d1c-cf523eefb5c2 | -8.89258 | -62.46433 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c314ca1e-a7ae-386d-9b0e-38191d033a8c | -10.01514 | -62.38874 | 2025-08-26 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b70a073-7e7f-3e04-86ef-68287953bf46 | -11.30144 | -55.11203 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 924acf77-eefd-3847-841c-c9bc40e25ba0 | -10.39045 | -57.69707 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41460eda-5081-30e1-a8e3-b052ca5642b5 | -10.65446 | -65.319 | 2025-08-26 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abe71e16-8ce4-3d72-934d-70199b3259c7 | -9.1868 | -59.47771 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 846661e3-72d4-3c1c-bf9b-6f4238e2172c | -9.17435 | -59.53718 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8c1f7ba8-8feb-3ea7-957f-571b7091f764 | -8.9971 | -65.40775 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c337d838-bba2-3393-843b-cd6e6f425866 | -9.01266 | -65.39573 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6432e114-9dae-3e5e-9d11-63dd73d7feba | -9.1861 | -60.78849 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6a4563a-bad2-31d1-a7c2-bb1c6a8eddf5 | -8.88459 | -62.47077 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be93a1af-2ee7-3e53-a4db-97788a6d4c31 | -8.55632 | -62.6231 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68153707-bd44-35a4-bb8f-7b64fe59a0ca | -9.49811 | -60.5515 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b97483e-810c-325b-bee8-9f4770751736 | -9.01075 | -65.70514 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c673e497-8827-3a8f-8038-c0919b26c548 | -8.98374 | -65.42738 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09b0ab22-057a-3c41-bdfb-6706ca0c918b | -9.09285 | -65.72204 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16a87d78-e6e8-36de-9c30-5575e4d83238 | -9.17633 | -59.52308 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7898dca-0034-318b-bcd8-07dccca93133 | -11.60195 | -63.49099 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 301be5a7-5631-399a-9f9f-d3f2814edd26 | -9.18332 | -59.50248 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bf04235-487a-3f7f-9571-6ba2bbdee4fa | -8.62926 | -67.24744 | 2025-08-26 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eabe7dc-b655-32ea-b2ee-b4fa057463dd | -9.10635 | -62.67194 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e8aee06-4312-30ca-9418-9bdb2737d620 | -9.27549 | -59.78783 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63710aff-08c0-3b05-a716-8036f9d3e38f | -9.01211 | -65.39927 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da1ddbd-cc0c-3a9d-8315-1f95be8c9ac3 | -14.11875 | -53.9845 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8a6f9b8-42ca-3bb6-b62d-bf230b5e40ac | -8.64112 | -62.62045 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76024e77-9d41-3555-ac78-7819f33beb82 | -9.82713 | -64.25916 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67aa5559-3cf0-3cf7-9171-947cf53e39ae | -9.02741 | -65.7299 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README87.md)
