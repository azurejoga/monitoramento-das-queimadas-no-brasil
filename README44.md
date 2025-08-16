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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72567f46-7715-3023-93bc-b77dff1536ed | -9.00098 | -60.52411 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76343172-076d-3250-bf7c-4fd24728d93d | -9.21259 | -59.65636 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46e9226f-aa80-3748-a1f0-addd22ff17dd | -9.49832 | -60.56188 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be7205b5-a821-30e7-94d4-2eb6c06c3319 | -14.94326 | -54.75471 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcb01d4f-db9e-377f-88fd-add6b72d9eab | -12.56246 | -46.97158 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce02b97b-07ba-3039-9ef8-76ca5c2556cb | -13.11076 | -57.13083 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb246f4-6d06-30e8-a23e-cf7e56e9745c | -10.93006 | -56.84806 | 2025-08-16 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c3e5cfe-18eb-3847-8fae-a9be72e2d232 | -12.54043 | -46.95219 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4702225a-51f5-34a0-87c2-9dd3ab961b1a | -12.60404 | -46.96504 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06d7a6a3-0965-3558-b764-fb96ee8f3125 | -13.44176 | -56.67291 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2a617b5-d9de-3331-a059-2cdb0069a9c0 | -12.46799 | -46.98486 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48d96e0d-b058-3103-8d19-8c68395ae4ee | -11.35771 | -55.41096 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bd3b4a1-fccc-3a28-b229-92f8afee893c | -10.86567 | -48.47992 | 2025-08-16 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1224720c-094b-3380-ad2b-5d6cf8640817 | -12.55666 | -46.96275 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2d2630a9-fa9f-3469-bd14-3b17b68aa3ef | -14.5993 | -47.94085 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00483abe-3c6b-320e-9a2a-33aeb301529f | -14.60619 | -47.94118 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0ad0697-27d9-36da-8b44-326289a39547 | -14.95582 | -54.72991 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e9a14f3-b128-3f7e-a925-c363914c4a70 | -12.29783 | -50.01432 | 2025-08-16 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3898074-18cf-3658-af73-45989c4ae59f | -10.17978 | -49.51165 | 2025-08-16 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02c13096-af35-316b-b14f-1bcf86e73c56 | -12.60805 | -46.93781 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a637ac93-a282-3bb9-8f34-43d61403b71d | -11.34543 | -55.40424 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 791a8aa2-00b9-3b03-87e7-26ebe4724714 | -13.42899 | -43.679 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5fa6d345-1a28-3a1a-aa8c-59278b79a21f | -12.59992 | -46.92032 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a68b0f58-9244-3a4e-9207-2718de3ca34d | -12.99897 | -56.87703 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a7d2960-8553-388d-9802-ca209c531239 | -13.1228 | -57.17154 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01519175-8e2c-3f94-b5d1-37a1c2cd84d0 | -9.50557 | -60.5581 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a56a5d4e-7037-3396-9c8d-57dcfdb29079 | -12.59645 | -46.94399 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 424cc08b-37d1-3d36-a241-b34917e0ccf7 | -12.54332 | -46.95668 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 52b07576-fda4-3059-951e-9d144caf1332 | -14.98639 | -56.0261 | 2025-08-16 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a95fe5df-12b0-39c1-a99d-cb0b820da320 | -12.83614 | -46.03411 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5df9768a-3287-3910-9c19-6c66fc0b076b | -13.60433 | -46.91401 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82bd1efe-ebc9-3a85-a0f0-4909d0b3fd00 | -11.31122 | -55.21181 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 688e1120-43b9-3bc5-b1d5-4bc575830e11 | -17.21522 | -49.59615 | 2025-08-16 04:34:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7bae504-7628-3276-9c4a-01ab5e7695ee | -8.99363 | -60.52826 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4bb1d932-9510-3f4c-a011-0d0f6a2c7efe | -12.82231 | -46.02463 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27fc226d-ee6b-3e22-be22-62ffe74bf022 | -16.37737 | -50.93238 | 2025-08-16 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0d91d46-75d6-3d62-88bd-aa90b4cb0af6 | -12.82462 | -46.01025 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6be52aa2-4121-38f3-8df0-0439be65faf6 | -12.59295 | -46.94352 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8151eaa-eff1-319c-8e1b-3d2148fff1be | -10.35608 | -50.80778 | 2025-08-16 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9324620a-b815-3539-beee-db4275c6fb14 | -10.45769 | -48.80918 | 2025-08-16 04:34:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0ed7997-74af-3651-8265-6faad47bd570 | -8.97041 | -61.71313 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 73bbc936-7cbb-3f62-91f8-5efda17ca5c0 | -13.1155 | -57.13169 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9d2b9f1-7f03-36e5-8d98-bce935a977ac | -12.53231 | -46.95887 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89078eb1-8b4a-3d61-af03-9c5d404d8328 | -14.58677 | -47.93121 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89b33add-82ac-315c-a3c5-7320e9325458 | -12.59816 | -46.93234 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d1f60764-a324-342b-9777-41722ee5f53a | -11.72374 | -47.56344 | 2025-08-16 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9b594e53-5cca-3b6e-8222-431d080c46d4 | -13.09226 | -52.14482 | 2025-08-16 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5f3ca0b-7451-307f-b2b9-90067ba55d9e | -9.20925 | -59.64168 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8ec6e62-2620-3208-8385-4a66ff53160e | -12.53695 | -46.95158 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2231dc13-00c8-323d-98ce-80ae6f7f9215 | -9.20073 | -59.65365 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4059fab5-5c09-31e8-9e2b-c123fb0ac940 | -13.13906 | -57.16646 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd9fd9cc-b1fa-38ee-ad6f-1f7d3516b176 | -12.83249 | -46.03359 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71b12b42-0764-3b87-b26a-52b95d6c3b8e | -12.03927 | -63.33865 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac6df07-487d-3945-ba59-7c2366f120e7 | -8.96178 | -61.68562 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fa044b1f-7940-3691-b167-55f28d0820f7 | -13.0074 | -56.87076 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a031d52-9d72-3ea7-9321-ac9c4e16fc67 | -8.98329 | -60.54786 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 936eb1f9-d35a-3526-898e-e3e808d866ea | -18.04375 | -47.72482 | 2025-08-16 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 065085a3-f285-3b6c-9738-f9e852bb68ef | -9.16818 | -59.64856 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aed0ab81-4a2f-3fb4-8387-5f5b77c0705b | -13.1295 | -57.1619 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ca1636-f4d3-3729-8fb8-dfd4bae9dcda | -15.69191 | -48.18784 | 2025-08-16 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d457f779-23c9-365b-925b-d52c85f50443 | -8.98863 | -60.55418 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff875e36-9207-3132-bd2e-43426d0bbbd7 | -9.49908 | -60.52478 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5356d9fa-d27b-3d04-a7aa-a3abd0756f6b | -13.10858 | -57.1687 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76c2a677-d33a-3095-a099-7be77054abb2 | -10.96544 | -49.57035 | 2025-08-16 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5688c5d-24df-3a88-aee2-352c20dffa25 | -9.18533 | -59.68891 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e4afd1b-e0a0-36da-a1e1-199fe7310b4a | -11.55245 | -47.26434 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9fcbb61-a253-33c0-8f42-fb71161c0fd2 | -14.21259 | -44.77923 | 2025-08-16 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31034002-e538-3777-8172-b59770b5104d | -9.21077 | -59.65233 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55e86b42-567e-39fd-b28d-898031128aee | -12.60462 | -46.96112 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 609e9b6e-aaa8-3f37-8302-c87f1fc07c05 | -8.10748 | -61.19798 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba1c331d-8b6d-363a-9b17-e9d3f899fd5c | -9.39038 | -60.54813 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eed1b3c2-2229-3f19-b2e8-9b41d883add1 | -17.28119 | -44.87522 | 2025-08-16 04:34:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90f8a0bb-bbb1-3f29-b0ce-56d004d6cb25 | -16.68411 | -49.40942 | 2025-08-16 04:34:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3be64b2-f291-365f-9d4d-415d519b507c | -12.53637 | -46.9555 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff3f8481-af4e-3f98-a05f-ce1b9cc1e275 | -12.45802 | -46.99181 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c6c402a-67c4-3e2b-9605-64357091eb14 | -11.34388 | -55.41282 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be02b7d9-e50b-345e-bf88-452ae080cba2 | -17.5098 | -44.885 | 2025-08-16 04:34:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4466fc47-6311-3b49-8ccc-e557d70181ff | -9.19985 | -59.6582 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36e77b6c-603a-307a-ba46-5c47ebfa02f8 | -13.1088 | -46.84503 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e38141b8-81a3-3236-aab4-950090ce9e42 | -13.14481 | -57.16216 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e3c06d-7b47-3a85-a1a6-a3061d75be5a | -16.37795 | -50.92878 | 2025-08-16 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71648ae0-859d-304e-b403-f3a295e01e7b | -12.79777 | -45.96289 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ca7b2e-9167-3ee8-9e73-1229ed4dbdbb | -11.359 | -55.42893 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f833d8-32e5-3a3a-afa5-0769f5193ebc | -12.47324 | -48.00122 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92b0c58c-bb74-3da4-87ba-428a3a114c17 | -9.18448 | -59.69341 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e67eba30-bd7f-3ce5-b3a5-166b6539cba4 | -9.17151 | -59.63099 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7177d8f6-fddf-3dcd-99d3-e309248a02da | -12.82532 | -46.0295 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c65a6888-4b75-3454-94af-dc681e9a8fc4 | -8.99796 | -60.53981 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24fd3631-03be-38c0-94cb-a27f573d2428 | -13.42475 | -43.67841 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6c1947d3-5253-3d27-932f-cf024f2d7016 | -8.11528 | -61.19337 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd686c2e-a455-397b-9632-1c4afa0f7ce5 | -12.82217 | -46.02764 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0899b201-469e-3b2f-8f31-1291cf2fd6f3 | -12.43043 | -44.69909 | 2025-08-16 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5080358b-86bc-39cc-ae5a-56ad8650ba7f | -12.29896 | -50.00722 | 2025-08-16 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79f328c8-f70e-38f9-b8d1-4bc76a6b7fe8 | -13.67323 | -45.89237 | 2025-08-16 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da666757-a06e-3a35-9572-80991fac36a6 | -12.60171 | -46.95666 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 49d391da-3ef2-36bb-b97a-29e054cc2c2d | -10.86125 | -48.48644 | 2025-08-16 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d678bba7-d576-3c64-b509-02577100259f | -11.00135 | -48.28439 | 2025-08-16 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1edeac9d-a48e-3cee-bc75-1e68ec39cfb3 | -12.61386 | -45.22545 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dc9f14d-590c-3361-a6ae-d3d3a02438d8 | -8.99854 | -60.50277 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8676259-2a6d-3622-b07d-219ec80efbc0 | -12.61852 | -46.93934 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README45.md)
