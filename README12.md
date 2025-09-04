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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f782bf5-3978-3699-87aa-3ac90373c098 | -6.7782 | -44.0876 | 2025-09-04 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 02af29ef-26c8-3810-bf15-f094a050da80 | -5.908 | -57.7311 | 2025-09-04 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a0a3e6aa-6980-35fa-bf46-8dc83c261d55 | -20.0979 | -50.0105 | 2025-09-04 02:10:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| d40963d2-7758-33ba-801d-72b5f1cb6d53 | -6.7503 | -58.7462 | 2025-09-04 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 69f769db-9c35-352d-8cc2-e4cae2e7c370 | -11.6599 | -54.5297 | 2025-09-04 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 23a9ac27-a857-3822-8d13-fff98943781d | -12.8816 | -56.9505 | 2025-09-04 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4ba60e8d-0ab2-32d7-bd35-61bff35bfcb1 | -8.0799 | -45.339 | 2025-09-04 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 68cdbb46-fe84-39f5-b078-a74eb48fe62a | -11.0572 | -45.123 | 2025-09-04 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 962e025f-19f6-3f1c-a61b-40b6c305fd85 | -6.7319 | -58.7276 | 2025-09-04 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4e50cce5-319d-3f5c-8e6b-b912b2546ce7 | -4.9951 | -56.256 | 2025-09-04 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8b988791-27ed-398e-a3a9-47d484341ec5 | -12.9006 | -56.9488 | 2025-09-04 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 93e07946-98c0-352c-ab9c-2d915bb905e0 | -6.7833 | -63.1286 | 2025-09-04 02:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 827baebd-93f9-334e-9fb2-d7930352fb30 | -6.7318 | -58.7469 | 2025-09-04 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 06b6280a-5f77-3d4d-83f5-dda20490a005 | -6.7504 | -58.7268 | 2025-09-04 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 42be3ed6-5605-394d-b662-17d09eb6e28d | -5.6079 | -45.0265 | 2025-09-04 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3b29a148-1e28-3b7b-862f-b12dcbbd043b | -12.9189 | -57.0074 | 2025-09-04 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1263a993-177f-3b08-9d5a-5798b9348442 | -13.1079 | -57.1109 | 2025-09-04 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0f473186-e7bb-3de3-906a-5aabd97d9fd3 | -11.0377 | -45.1487 | 2025-09-04 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 39ebd4d2-c00f-39f0-aa63-df89199ebb08 | -6.797 | -44.0859 | 2025-09-04 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2fd6c6a6-5bf2-35f0-aaae-39a9f11649e1 | -6.7465 | -63.1297 | 2025-09-04 02:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 528e97b7-73f4-3213-a46a-85fa8d590adf | -12.9009 | -56.9287 | 2025-09-04 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8672fc84-ea97-3fe8-9bf0-2009e1207af3 | -12.8816 | -56.9505 | 2025-09-04 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2639386e-89e8-3d1e-868b-3bd762852a0d | -6.7782 | -44.0876 | 2025-09-04 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| fb9eeca9-0177-31ab-9e69-d6b81c2429f7 | -6.797 | -44.0859 | 2025-09-04 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3db25dfe-3fb5-3e2f-b7c6-6347699e8c7f | -12.9189 | -57.0074 | 2025-09-04 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 938cdabb-42bb-3009-8615-55df412df4c5 | -11.0377 | -45.1487 | 2025-09-04 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| e188f14c-bb0c-3335-a2ca-317f20f1530f | -12.9006 | -56.9488 | 2025-09-04 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| a04abdec-9bff-377a-b3a3-6fa4df61bbe4 | -6.7833 | -63.1286 | 2025-09-04 02:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fe1e3d7d-363c-3b47-ad92-e36d6da94488 | -14.5606 | -48.043 | 2025-09-04 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c574bc90-3248-3d2c-816f-58b59f06d942 | -14.5412 | -48.0461 | 2025-09-04 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d0c063ee-0eb1-300f-8fb6-ea86bfa69caf | -11.5779 | -52.115 | 2025-09-04 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 71aa4439-3ddb-3af7-93c8-e17a0825f8d8 | -11.6838 | -57.3319 | 2025-09-04 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 548b2a32-37be-37e3-85cc-0decedc2ddbf | -5.6079 | -45.0265 | 2025-09-04 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f9c23ead-f096-34b6-999e-aef957bd4fd3 | -6.7504 | -58.7268 | 2025-09-04 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 3c547c13-f01e-39aa-ace7-470528139049 | -11.6836 | -57.3518 | 2025-09-04 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 76a1a723-1ad8-3d6f-b539-4c5550795c85 | -10.4472 | -50.3713 | 2025-09-04 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 14b81092-9b1c-35a7-bbfd-91797dd73eba | -6.7318 | -58.7469 | 2025-09-04 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a80fd5b9-9cd4-35c8-9733-d774eb7cd48b | -6.7505 | -58.7074 | 2025-09-04 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0c5d70d9-2f06-37ec-a6a1-fa88f54de93a | -12.9197 | -56.9471 | 2025-09-04 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1852b2ad-2fc1-35d9-b90e-6b22560a711f | -4.9951 | -56.256 | 2025-09-04 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| cc823e6b-fa36-34f4-8f3f-9e85fb40e481 | -5.908 | -57.7311 | 2025-09-04 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b6cecf27-0f6e-375d-a948-d53f18a79609 | -6.6796 | -48.4049 | 2025-09-04 02:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 369b1c08-7431-35d0-8f99-b672823263ef | -11.0572 | -45.123 | 2025-09-04 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2b9352dd-eba8-32d9-8616-f9b2cb1441be | -6.7649 | -63.1292 | 2025-09-04 02:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 74f79407-dddc-32ec-a74f-0dbf78957f5e | -11.0381 | -45.1256 | 2025-09-04 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 3519cb58-0ea0-39dd-9378-2f1e4a3520d1 | -8.0572 | -44.1264 | 2025-09-04 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ce2e0f8d-3038-3373-bff0-44cfdbc9932a | -10.4283 | -50.3732 | 2025-09-04 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dc336e75-7fb5-3ca3-b2cc-e7f0d10ae35d | -6.839 | -59.3608 | 2025-09-04 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 11394791-d9b6-374d-866f-758f3705f08a | -11.0568 | -45.146 | 2025-09-04 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 06b47e19-2f3d-3ea1-a387-eeea9ec8be5c | -6.7319 | -58.7276 | 2025-09-04 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| e877992b-1dfe-3e40-8e98-ff9802de4664 | -6.7503 | -58.7462 | 2025-09-04 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 67b6228b-0a13-3f55-9c29-3685a1f87e2b | -11.6647 | -57.3533 | 2025-09-04 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 26cd7456-2ad8-3489-8910-5ed35bc61775 | -10.4475 | -50.3499 | 2025-09-04 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7245e300-cbb8-3756-ab19-3135b082556c | -14.5407 | -48.0686 | 2025-09-04 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a1c72a59-3003-380b-b683-d49161bcf9cc | -10.5746 | -55.4161 | 2025-09-04 02:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3fe9bd0e-aac2-3273-8756-d4b9a4407ac8 | -11.0381 | -45.1256 | 2025-09-04 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 70f1c65e-c67f-3898-a5a7-97c6ebc84e01 | -4.9951 | -56.256 | 2025-09-04 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ba98ac05-866f-3775-8101-58da929bd375 | -8.0572 | -44.1264 | 2025-09-04 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e8619812-f9bd-3592-abf5-2d605583bb1a | -11.0568 | -45.146 | 2025-09-04 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| fc7e2031-27d6-30cc-b66b-e3bfd54d911a | -11.0572 | -45.123 | 2025-09-04 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ffba6ace-bbde-36ad-afbb-a8e00f4d1396 | -6.7318 | -58.7469 | 2025-09-04 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 32033429-827a-3f35-b613-96d03006ba20 | -11.6599 | -54.5297 | 2025-09-04 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 43f35317-ffd4-3af9-959e-96682f0c45d0 | -6.7833 | -63.1286 | 2025-09-04 02:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6343a49e-f438-3f0c-aa6f-5f5891de5efc | -2.9619 | -49.365 | 2025-09-04 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 6dd7a28d-3608-35cb-bf75-19e19d47701a | -11.0377 | -45.1487 | 2025-09-04 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 3a305581-aa29-3f8a-8681-721da8976920 | -5.6079 | -45.0265 | 2025-09-04 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7bfe6b20-e4bf-3cc6-914b-9a89bcdb968b | -11.5779 | -52.115 | 2025-09-04 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b54c0df9-f680-369f-8745-38ce22a8d2ad | -6.7649 | -63.1292 | 2025-09-04 02:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 579ae2a6-308a-38a1-ac4e-de07ddb57a34 | -6.7503 | -58.7462 | 2025-09-04 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ddcca62e-bc93-33a4-8430-b0f9132419f5 | -6.7782 | -44.0876 | 2025-09-04 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b94c6169-8cf5-3b2c-aecb-8e58bf1d0524 | -14.5407 | -48.0686 | 2025-09-04 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 042a5c9d-d1da-3134-a05c-2210e30b1a04 | -6.839 | -59.3608 | 2025-09-04 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a6324cba-784e-356b-ae7d-573ece52ab60 | -10.5746 | -55.4161 | 2025-09-04 02:30:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fa93804c-e070-3110-8239-0bafe5785485 | -11.6647 | -57.3533 | 2025-09-04 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ed398725-cf80-3288-a4cf-7dad4e5352da | -12.9006 | -56.9488 | 2025-09-04 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0a659cec-06be-3034-82df-a73efac00966 | -5.908 | -57.7311 | 2025-09-04 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c90be5b0-d17e-38be-ac5d-fce0fd1934ef | -11.6836 | -57.3518 | 2025-09-04 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c9504393-30c4-369b-a828-abe4b4d85f30 | -11.6838 | -57.3319 | 2025-09-04 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7b5598d3-d633-35a8-b5bd-7b71783e8a9c | -12.9197 | -56.9471 | 2025-09-04 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a8debb4d-814b-3329-8358-287b5fc838b3 | -10.4475 | -50.3499 | 2025-09-04 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 67d92060-2842-3181-8dad-601dd26d4fde | -14.5412 | -48.0461 | 2025-09-04 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5a305274-db4e-38c6-afbd-297620fa23eb | -12.8816 | -56.9505 | 2025-09-04 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2101e022-ea5f-3fe4-8e72-9ad8abde92f1 | -11.6649 | -57.3334 | 2025-09-04 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c4c8ffc1-bed0-3cda-a536-76a4f125bf11 | -12.9009 | -56.9287 | 2025-09-04 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6a03c670-9041-3730-a586-8675055f889d | -6.7504 | -58.7268 | 2025-09-04 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 8bfcb43c-67d0-3efc-825f-ed624c5d4803 | -10.4472 | -50.3713 | 2025-09-04 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 86f7c168-2cd2-36cb-b98b-c91f9a19707a | -6.7319 | -58.7276 | 2025-09-04 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| d0213247-052f-309a-874a-5d5ea0cdff6b | -6.6796 | -48.4049 | 2025-09-04 02:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2678f9a4-ccfb-36e9-930d-417cbf644fa1 | -10.4283 | -50.3732 | 2025-09-04 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 95c490e1-0028-38ab-9b48-56b378133a33 | -11.0377 | -45.1487 | 2025-09-04 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| d6ca30a4-1d77-32dd-b357-9746a2782a7e | -6.7833 | -63.1286 | 2025-09-04 02:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 24f420d8-4403-3ed6-9cf6-89cbe1b0152d | -6.7782 | -44.0876 | 2025-09-04 02:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 422dc26a-a169-33e8-be65-03c3641b98d5 | -11.0381 | -45.1256 | 2025-09-04 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1b5ca6e1-5712-3890-b749-9711dae6d4ec | -6.797 | -44.0859 | 2025-09-04 02:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1feaa509-7ae5-309a-9b82-4d8d09166f67 | -8.0572 | -44.1264 | 2025-09-04 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2396f421-5d6f-3441-8eec-0cc035c321b1 | -9.5347 | -40.3033 | 2025-09-04 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.2 |
| b063757a-41d2-329e-9c8c-78b5027d3c78 | -12.8816 | -56.9505 | 2025-09-04 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 6f0649b0-4987-37ea-b4a1-b8e01b5b5210 | -11.6649 | -57.3334 | 2025-09-04 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 668cf32e-252e-333c-ae37-723a74aa9b79 | -6.7505 | -58.7074 | 2025-09-04 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 8841ce1a-4c6c-3162-9d57-ca928bdf21e9 | -6.839 | -59.3608 | 2025-09-04 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |


[Clique aqui para ver as próximas entradas](README13.md)
