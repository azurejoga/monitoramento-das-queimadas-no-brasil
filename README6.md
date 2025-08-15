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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27eb15bf-2835-39b4-9e5d-9aa498b3a4e3 | -14.2444 | -44.5897 | 2025-08-15 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8d9d914c-2f89-3bb6-b563-ad2eadece79e | -6.0808 | -59.9274 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6f40be97-cd6e-3cec-9d17-2a1aa17f8503 | -7.3116 | -60.628 | 2025-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7ff15d2d-ed3d-3cfc-b9f7-02da12e7d1c0 | -6.0807 | -59.9465 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 305.3 |
| f6d61fdf-11f6-3a71-a7ec-e15e1c8b466d | -5.762 | -46.6741 | 2025-08-15 01:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 608c8760-dae6-3d4f-867a-2c967b727f16 | -8.3099 | -45.0196 | 2025-08-15 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9ce54423-7b86-3264-a380-687567589a43 | -8.6041 | -45.6029 | 2025-08-15 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7d0710ae-3772-3372-ab28-266e7e0a686d | -15.6546 | -49.7536 | 2025-08-15 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1c4076c2-c782-3172-9fdf-ff82c1071d81 | -15.6541 | -49.7757 | 2025-08-15 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 130.5 |
| df7def9e-c21b-32c0-ab44-43bf641fc0b7 | -11.3655 | -55.431 | 2025-08-15 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 4d974a2c-90c2-33d1-a4dd-92e18ee5edec | -9.4992 | -60.547 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2db4575f-7784-3b4d-b6f0-fa4cd7324c3c | -9.4995 | -60.5085 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| bef49620-918b-3648-a891-e2c11db0164b | -8.6038 | -45.6256 | 2025-08-15 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 184.2 |
| de01d9e0-529b-3afd-ace7-539493c9748b | -10.87 | -62.0115 | 2025-08-15 01:10:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| fd4e956a-591e-3d98-ae2f-6372b54f71d2 | -9.4994 | -60.5278 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 749edd3e-80e6-34bf-8b0d-016baf7ea518 | -11.3466 | -55.4326 | 2025-08-15 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 6eedbc25-1fe0-35e4-9acb-fc8451c02fba | -7.3116 | -60.628 | 2025-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ce80496e-4a97-3997-ad47-80e2efe01f26 | -15.6741 | -49.7505 | 2025-08-15 01:10:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6dd5cd5b-2628-3b43-ac46-e8a1bd15cea3 | -9.5179 | -60.5461 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5b4803df-8e4e-33e8-88d2-fdf7a7c585ce | -9.3875 | -60.5528 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2e647596-afbf-30e2-b057-5517cfc58589 | -8.6227 | -45.6236 | 2025-08-15 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 26b6f519-7048-3355-9318-50fcf713d710 | -15.6737 | -49.7726 | 2025-08-15 01:10:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 867a58b7-9ca5-3b0c-8c96-36eadb136e2d | -5.455 | -60.12 | 2025-08-15 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 3e66f377-4c5e-386e-b19d-6a23488fc35a | -11.3657 | -55.4107 | 2025-08-15 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a7fd4fc3-bf27-3531-805b-c081354bfc91 | -14.2449 | -44.5661 | 2025-08-15 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 052a3b20-f5fe-3f2d-ae73-7e480f5ac0eb | -7.0982 | -59.215 | 2025-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 24e44c5f-7d62-35b9-bcf5-4b0264f91f5e | -7.9517 | -61.7464 | 2025-08-15 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6b1f8e85-b285-30af-8973-9f357058b448 | -7.5292 | -61.3254 | 2025-08-15 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| e3b6e35b-f2b0-3ad2-a129-b4f94a9c2a23 | -11.3468 | -55.4124 | 2025-08-15 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 569fd86c-66fd-33c8-b411-9481eca682c9 | -7.0797 | -59.2157 | 2025-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 0174ca9e-1f33-3202-887c-09a07032b742 | -9.518 | -60.5268 | 2025-08-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| faa87c0f-90c5-32a9-820f-d388d550da40 | -14.2444 | -44.5897 | 2025-08-15 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 455db058-b8ef-31ba-bb85-a1acd0e3e4f6 | -6.9303 | -59.5305 | 2025-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 065b57ca-0d62-37c0-82a1-3eae49fd3bbe | -5.455 | -60.1391 | 2025-08-15 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| a4a991ff-329d-36c2-8c2a-a0d5eba6d256 | -7.5291 | -61.3444 | 2025-08-15 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 03c7710d-22a4-312d-8c50-ff2cef268463 | -6.084 | -59.9557 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6488e0c6-7d9b-3087-8412-bc8b0e13948c | -6.9233 | -59.529499 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42e40f46-dbef-3288-9989-5e677b369b47 | -10.1188 | -57.7645 | 2025-08-15 01:10:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 660b8f2a-f610-3e4a-8306-4a7d5457efdf | -9.5493 | -63.574501 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5211eb2e-05da-300e-9b35-632b1505a4d1 | -7.9395 | -61.7589 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48033435-140c-3d55-84dd-6268819e972e | -13.1143 | -57.162899 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5738f2c8-c318-3361-959c-58201d02ac27 | -7.8199 | -61.322601 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af470a81-f2af-3785-88af-9f18e99289f6 | -10.8684 | -62.002899 | 2025-08-15 01:10:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ebb1a018-0336-33ed-aa47-c99638b1415f | -7.5893 | -63.457802 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf6e2ed-c04c-3606-9119-f5147e322df7 | -5.4614 | -60.116001 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1819e73e-607f-3da5-86dd-f5516a5a2b7b | -7.802 | -61.334202 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85d0f7b2-27a5-3c54-80af-2a4d31fd01b3 | -9.508 | -60.543098 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49d68910-8e19-3d2f-afbd-04aaa6201e99 | -6.9516 | -60.007999 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5b6c9d4-d2f6-3bfb-a06d-7550d8362216 | -6.6293 | -59.996101 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ccd2564-c581-3216-af9c-2567b5436386 | -6.1114 | -59.940601 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5806745-91fd-3ce6-b728-065fd5fd4e5d | -7.9594 | -63.455799 | 2025-08-15 01:10:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea01a891-81c3-3474-a583-7c7ab54e5aee | -8.6038 | -62.651798 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2d4133db-8fb6-3b5f-8f39-132cf72d9d93 | -7.4647 | -60.400299 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8176dcb3-aaed-3af5-b5f4-06eb44c1babb | -6.1016 | -59.942799 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20725a4f-c3a8-3ff1-828e-175864858a6f | -7.5373 | -61.348999 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f973e916-2d87-3ac8-badf-cf8a3d6cf655 | -8.5642 | -63.911499 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 52ccbf37-6a83-3e59-a1ef-76a346a04f91 | -15.652 | -49.753799 | 2025-08-15 01:10:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d48413a-1cdb-3fb1-ba75-33cffd07a5d6 | -6.8862 | -59.1483 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 700a3028-c009-33ce-993a-e1688c4da7f5 | -8.9513 | -62.225498 | 2025-08-15 01:10:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81fab948-cf4f-3e20-a189-57678f8e3d94 | -9.1518 | -59.667599 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 232361dc-a71e-39a8-9493-49ed70e811ee | -7.3931 | -60.000099 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cbb9db8-bb96-359a-a093-d056e6456795 | -8.1105 | -61.195499 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87caced7-9514-3235-b118-9ce20b874f4f | -8.1072 | -61.181099 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f4b13d8-9710-3347-9674-eabf1409042d | -7.8183 | -61.315399 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e468375e-891a-37e6-9c2d-990c5ec8e950 | -5.4438 | -60.128799 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d83b592e-a8b3-35a3-9138-dde3571ccd36 | -7.5324 | -61.327301 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6b60165-36a7-3200-baae-c7d553577cd4 | -6.896 | -59.146 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97685dc6-7632-3452-95d9-d320f37328af | -6.1056 | -59.915401 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38b741d1-686c-32d5-8a0c-1c81cefc4eb7 | -6.0802 | -59.9389 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdde00d3-6f76-3d37-97f7-12d9dd5862b7 | -6.4915 | -62.9221 | 2025-08-15 01:10:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f67a9be-ff82-33f7-8427-83421cafacd1 | -7.8134 | -61.339199 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b187b60-b81e-39fe-960e-9af63bdb6472 | -9.0218 | -61.2141 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e990d46b-2930-3c8f-a17e-5c8b8122b10e | -7.0831 | -59.196999 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6a15640-1038-3676-889e-354244097229 | -6.8804 | -59.833599 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd6fb4dd-4657-359f-a95e-5b2d787105a6 | -13.1338 | -57.158001 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e911f114-0c27-3a6b-a0c9-d38ffb1899d5 | -9.9141 | -60.425499 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0d5cdc-ee1c-3314-970c-f2d9b0d60f74 | -9.4995 | -60.505901 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61b1a5b1-a482-3198-a6a7-1afefd63867c | -6.9331 | -59.527302 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1fbbadc-9df0-3a4b-925e-c4b1b261e217 | -9.1872 | -59.6423 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4161561-ed48-385f-81aa-cb4a3e33d699 | -8.5709 | -63.895 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb94ee99-40fd-3ec7-a343-7f3a508271ec | -9.2067 | -59.637699 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 082beb30-bdeb-3be9-aca4-ba3fd22f93d0 | -6.1134 | -59.9048 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd4acb13-817f-3300-a054-9f7397d39d5e | -9.5477 | -63.567402 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c6795633-8b83-368b-9ec2-8c129ad7c9eb | -10.1164 | -57.754601 | 2025-08-15 01:10:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c25e22f5-4b12-30e2-b85b-6881501a51db | -6.6751 | -59.0825 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c75e737a-a2c6-3958-a98e-b1df49ed681c | -8.1089 | -61.188301 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3447b04-c541-3d7e-b258-22232ef87369 | -6.9134 | -59.1325 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7137ee8-d538-3a70-b103-cc2bfd5a71fc | -7.597 | -63.4925 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4eabe6d8-5dbb-3818-ad8b-b791029348ad | -7.4145 | -60.0037 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1feeffed-643a-364e-bad3-9f8f2f928f07 | -7.4378 | -60.015301 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a70cdb5c-f208-3a74-a0d6-ae41db4e4745 | -9.1555 | -59.417301 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab6ffefd-46c6-3af8-b3a6-65eacf331ac2 | -9.1732 | -59.671101 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa986c1e-89b2-3035-85ca-5c9ae7e52f21 | -7.132 | -60.119701 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8d0ab14-0e35-39c9-8bb2-151ba6c039f0 | -16.3022 | -52.898701 | 2025-08-15 01:10:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9859a1-15fd-374c-8775-f00116b5e302 | -9.511 | -60.511101 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e576daf9-d4b0-3ed2-9844-61b17ab3addd | -9.1676 | -59.6469 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0bb2d39-5c2b-3c2d-9d26-3455a5c55d18 | -7.4397 | -60.0233 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7abd4e3d-c437-3340-ad93-6e2ec5647aca | -6.0782 | -59.930599 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09c5ed36-85f7-3979-adc6-e514d307d6ab | -7.2979 | -60.616901 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 734bf1ad-5f7d-3d23-ab57-6573def1e135 | -7.5619 | -61.411499 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
