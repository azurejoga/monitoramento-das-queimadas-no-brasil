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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e8945aa-21d9-3e57-b10a-7ca2235b9ea7 | -2.79895 | -49.58229 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab1a0260-e240-3813-a52a-6457a28e30e4 | -2.82498 | -49.49669 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d8c082b-2b96-3959-9ba5-3af178a026ad | -1.50719 | -54.9657 | 2026-09-01 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b2f249-8939-3b63-aa46-a3f04e0fe1c4 | 2.24148 | -50.7475 | 2026-09-01 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9a9722d-6de6-3dc2-846f-2065d520a74f | -3.86818 | -44.04967 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd10752a-7c5b-365a-b48f-44dd68a7bb75 | -1.78027 | -53.50042 | 2026-09-01 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7409183-141c-3220-8e98-300e7745c662 | -1.03431 | -47.55427 | 2026-09-01 05:14:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 863c1507-55b2-3683-9978-7bf6c08e97d6 | -3.85995 | -44.06276 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d05e9d-76d3-3fc1-bdd7-6eeb0305f68c | -3.85171 | -44.07601 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf71a230-f8bd-38df-bf0d-52ef180903da | -1.2773 | -60.33177 | 2026-09-01 05:14:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b8f7c24-e8a4-3822-9af0-3085e35ebb40 | -1.47149 | -54.23256 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc598c9e-4d8b-363c-9233-5466bd2820d5 | -3.86329 | -44.08274 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04eb7db-07d9-31e1-8cda-7c273646a8a9 | -1.47094 | -54.23603 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac3a7689-e514-3432-8249-f03469984752 | -3.85378 | -44.06197 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c55c315-5805-3b0d-8616-79725de2940d | -1.58744 | -50.43984 | 2026-09-01 05:14:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ade7ed56-ac04-3c13-aa9f-f6fd991bff08 | -3.16018 | -48.07376 | 2026-09-01 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c532320-3c3e-3ff7-8a8f-10db8db6ae78 | 0.19254 | -60.49733 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6779d04b-2589-3480-89a6-6faa7b2ff59a | -1.44433 | -54.23191 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb29c726-4a83-33c4-9e3d-1df2c9eba619 | -1.44542 | -54.22498 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aff66daf-f184-3df7-85f7-e9d585d0b43f | -1.46536 | -54.20676 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29c78a48-6b4e-3104-87fc-8283dc0a7bb0 | 0.97661 | -59.38326 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6831755b-bd6b-3a3f-a0e9-f9d0a670041e | -3.85926 | -44.06748 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c39146cc-bc38-35e7-beda-c72c3eefd6b9 | -3.86273 | -44.04391 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49b9d534-87d2-3a1e-b05b-5872c4c54a81 | -1.46428 | -54.235 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ecf1c0e-b8c1-37aa-9a55-b17f4a8e3a66 | 0.007 | -60.60161 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c63f9fe-ed21-30ba-84c0-28a8a4649bfc | -3.87156 | -44.06935 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a74e0c7-d079-3b88-bab3-b9c6c7d17c16 | -3.85311 | -44.0665 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15854f88-431a-3ef2-bac6-4a5eec6a83ad | -2.79536 | -49.57788 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfeecfcc-6252-3a1d-8344-8ad635aa0c20 | -1.7769 | -53.4999 | 2026-09-01 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4acde43-466d-3513-86d0-4441e08a47a3 | -1.01962 | -53.7237 | 2026-09-01 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe97bb6-ac6c-35d3-b827-cf1c3b838440 | -1.96463 | -48.37814 | 2026-09-01 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a024dc9d-e91d-3f18-85aa-6004167ea8ac | -3.85656 | -44.04308 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d5f15b9-bfaf-3270-954d-5231e16efa36 | 0.97829 | -59.39414 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c97342a1-d0f0-3ee3-8af0-caae00ffafc1 | -2.26302 | -47.86987 | 2026-09-01 05:14:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34c0a27a-6e19-3145-a71a-3e4524a52e2c | -3.85785 | -44.07702 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afd71613-7a9b-3d01-bcb3-b96ab616ad36 | 0.19745 | -51.52331 | 2026-09-01 05:14:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bac714d-79a3-3670-93d3-fada4c7d1539 | -7.35161 | -55.19811 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e35857-e061-370c-8dc5-942457eeebd9 | -7.62761 | -55.28817 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8b5ae92-7e2e-323c-9810-cbeaf1b19e2a | -8.69607 | -62.93876 | 2026-09-01 05:16:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d994edb-3c79-3c0a-9c64-5ea371aa938d | -7.33871 | -60.57463 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a348762-9314-30e3-8b50-2d06913e139e | -6.17896 | -57.73231 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 8d7ef94c-31a1-361a-bc30-1a380a99d70f | -5.24582 | -55.88927 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dffbc118-462b-34bf-81db-20f9616da513 | -7.05657 | -55.67556 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 999f465f-5f6f-380a-8f59-c228248b111a | -7.52448 | -47.33232 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 271e8318-b066-3e3c-8639-2e4804707967 | -9.39466 | -60.57822 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab0776c-f556-3854-96d9-dcdea52c196e | -6.59565 | -58.5899 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0c5927c-9bfc-31ed-93b2-08e1810e314f | -3.832 | -55.56602 | 2026-09-01 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8369d85-e02f-396a-b656-d45166d839e1 | -6.18179 | -57.73657 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 549b7203-bbfd-3760-917a-5002847b4272 | -8.78771 | -62.48394 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f7013704-d270-3fbd-ab10-e0666738d05b | -6.42955 | -53.56696 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0721d751-8961-3082-8bba-1f86c4479ca8 | -4.15388 | -60.697 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fca69fb4-813e-3990-8ad8-2d87eeb7fa3c | -9.2053 | -59.55111 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd1ff268-b7be-3f3b-a6f7-b8c5bb3208d4 | -6.24673 | -55.4266 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff6b10b-ad5f-309b-96db-dbe4fa0c005e | -7.26108 | -61.10999 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31e27b67-9370-3963-af1d-3ad504fa7fd0 | -6.57151 | -55.61669 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82dbb9ef-dd51-3df9-b382-d2ba1c2ecf09 | -7.5345 | -61.38635 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fd2a71b-653d-3584-ab35-0246e6cc222f | -10.0297 | -44.69322 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3012beae-bf53-3936-b472-d43d2117f9a8 | -8.81215 | -62.50346 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c7dd832-eae3-3f81-9e49-fa0cb712e7b1 | -8.93553 | -62.36881 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19bb3a58-0c89-3aa1-8dda-f2d4f3c44138 | -9.43835 | -45.63139 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe1d6ac-4abf-3987-baae-b281f3aa7962 | -6.24459 | -55.48323 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 547bea63-8376-34a9-a686-6e2865d048d8 | -3.59933 | -54.55152 | 2026-09-01 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28d33238-9a69-334b-b44d-ba9531b3f958 | -5.35132 | -56.66924 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 396f0a3f-f3df-3bc2-91dd-64af26c64b58 | -8.84697 | -47.08664 | 2026-09-01 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e29954f1-7319-3a38-8fe1-4f657d08154e | -7.50222 | -55.33376 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74365c09-48ba-3f1b-a578-5610d4b3707f | -9.42494 | -56.9761 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a53de0f-c5ba-328f-b244-3d8ec1a7d1aa | -9.15697 | -59.54429 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43c3efdd-cd92-3070-9d7e-7d8f2170a07f | -6.13259 | -57.84376 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a543e564-2927-3d45-8497-2c8f89c55684 | -7.57983 | -60.47495 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1571e31e-0367-3b6e-b280-bf5cfeef7713 | -7.42189 | -47.99605 | 2026-09-01 05:16:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6d884ad-9601-3e01-9d83-994223c906f4 | -6.90933 | -59.48056 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fac6a864-9804-3a25-a690-51daaa4e63e3 | -8.93188 | -63.28357 | 2026-09-01 05:16:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e713964-9933-3acd-9c24-f50cbae2cddc | -3.12883 | -61.17953 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d56f5cb1-a384-33bd-ac71-58620e65c101 | -6.2122 | -42.52068 | 2026-09-01 05:16:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71b11a23-1933-3f68-aa5c-7f20c5f35c39 | -6.72662 | -50.46426 | 2026-09-01 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93002d06-5dc4-38cf-863d-50c933214613 | -3.11202 | -61.22765 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37af00fe-5917-33cb-b9eb-71fc4064a948 | -6.95573 | -55.64901 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 550a4d11-b99c-3bb4-b6f6-b16e61ec98ee | -6.15987 | -52.639 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4d98941-a92d-35fd-93ba-9ae8660075a8 | -8.48955 | -54.59046 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec06851-3584-3e3b-a713-e112f4262837 | -9.2246 | -59.79174 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29ae922e-a679-307b-992a-aeabda016cdb | -8.94905 | -62.36707 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d343fa55-39c3-3997-bbdb-9f0a3a62a78d | -6.92316 | -55.72583 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25ef7fb-7eca-3dc1-b3b7-946081935a17 | -6.52423 | -55.22722 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aac00a5-a75d-3b6d-9e51-8beb68c3ab52 | -7.28784 | -49.82945 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffbe23cd-e436-3aa6-b5e6-89da63adedec | -6.21136 | -55.47798 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37978446-aa97-369a-8eab-ae39eeaf8876 | -8.79342 | -62.50861 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd47551a-a87a-339b-9e6f-7774b0009657 | -6.90493 | -59.48432 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111c58da-ffd0-3305-93ee-a6d469090904 | -3.63726 | -60.55704 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f5ac8e6-f7f3-3b93-9ecf-8fe064ab9ffc | -8.6155 | -54.79052 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31c53f0-ba1a-3c4b-a725-bff7acb0f102 | -6.0218 | -57.66922 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65fe317c-32b5-3a00-8a0e-5d4b2f265cee | -3.61505 | -59.07045 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18172310-17c1-362d-abe8-37179a4333f7 | -11.21073 | -46.07659 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2c033d4-08a3-3eed-8551-5ade57feca49 | -6.15392 | -57.77794 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bb86dea-e0ee-30f3-be25-70b4528f5637 | -7.48492 | -55.31305 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dfde351-9a31-3e9e-93b6-193183ce478b | -3.65942 | -58.91258 | 2026-09-01 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4adfe691-693b-3d75-b4f6-df2b9a96990e | -8.59168 | -54.71913 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612cc007-1e56-3335-8fb6-8241ef16c455 | -7.58064 | -60.4701 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f9fadcb4-e8f5-3dc8-beb6-16f76efc3e63 | -9.16094 | -60.2899 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03af1947-2ae5-31ab-aea0-c02807667cd6 | -7.18833 | -60.67995 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 433b92cb-e984-3a44-8229-c96838673265 | -4.94424 | -47.6556 | 2026-09-01 05:16:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README53.md)
