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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cacb2c80-16c0-331f-b9a0-ef4a76238b05 | -8.78307 | -45.84443 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdfd4025-973e-3b36-8746-9d2dcdc25272 | -6.74075 | -55.09434 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03363057-c635-3ef8-829c-d603eae6884d | -14.63699 | -45.65117 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d752589-f0cc-3a98-9147-fada63f81e51 | -8.30551 | -44.76163 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a8a198d-eed6-32fd-9575-9ffa387b8c9f | -8.14938 | -49.55186 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bd403d6-ed57-3a22-9bd5-ddc62350a211 | -11.30075 | -51.35551 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b6e282f-b223-3e42-b38e-c27495ed80c2 | -13.85255 | -48.58849 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee86ee4a-6857-3911-b0a4-5370ab193df9 | -8.32971 | -50.72858 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 606ac4fc-5ef8-3679-a60c-6042c8961288 | -11.11287 | -48.31274 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1213c49c-5274-3604-b07f-dc927dc7728d | -5.73851 | -53.46621 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4aaf2e06-8c60-34b2-acf6-1cb3ee5f1485 | -11.29631 | -44.04408 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 075cca7b-b314-3712-b07d-71450c382090 | -10.50393 | -44.87295 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6eff38b-1eba-3d85-a565-bb8361c1f6a6 | -6.36007 | -58.28104 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a87d52e-0d28-3d91-9c0a-b4a3575145cf | -9.54939 | -47.93594 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724fc62a-d7ee-361a-bc62-349e7fbf4449 | -14.6299 | -45.62506 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b6c3814d-ee7e-35e5-aa9e-7b7013c5ac5a | -7.19159 | -47.46039 | 2026-09-23 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc3d5dfb-3ade-3dba-b1c4-293d9a3f7647 | -11.46834 | -47.74023 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f62f12a-2149-3ce8-8eeb-e14d68128cb0 | -8.33202 | -50.83051 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9421ddb0-0a87-35d6-8dcb-e96fc1c37620 | -14.7068 | -45.59096 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1c9824b4-bafc-3f42-9cc9-95f5536f21dc | -12.05318 | -50.35048 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 675c212f-4bd1-3132-9571-f4448f4e66c9 | -7.37295 | -44.80971 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f3ddec9-b159-31a3-b09c-dcccad1841a7 | -8.08489 | -44.34556 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18eaeef3-84c6-3b3d-959d-efbbd2583028 | -7.16343 | -45.81018 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fda55e3c-7cf8-3161-a785-0c25b72618fa | -7.32767 | -55.60133 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df51ac35-21db-307a-878c-2c1e38aa31ee | -12.80538 | -50.91509 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14e62036-458c-357c-8880-0ef32fd63463 | -8.25282 | -50.86189 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb613c2f-6af0-38cd-a4e3-d1e0c32102f2 | -12.41135 | -46.98639 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aadc298b-34a2-3e86-a554-47f408d1c9fe | -11.30371 | -51.36065 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 687b99e6-b587-3f43-b707-75450530d611 | -11.74855 | -50.05485 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2d8095f-5ebf-3702-9f87-7aba4c6ed2b0 | -7.4177 | -49.8589 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b15f61f5-ac18-35f6-96cb-8bfed0a7c2fb | -9.0521 | -45.77642 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a9e9fc1-c748-3f6b-a579-08e76789b9e0 | -7.42989 | -49.85205 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 615918b8-20f7-3441-b171-5e6a23182e30 | -8.49317 | -57.60887 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4bfdc007-3b16-3996-922b-0ba1d59ace79 | -14.64511 | -45.59389 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad902d62-cfe2-3d2d-b3db-daba66587be1 | -7.97864 | -44.09234 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f94cd319-9403-3957-87da-b6404f471573 | -14.62622 | -45.64628 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1bf42ed7-d2a9-3ac5-8717-cc69b8ff3c24 | -8.48658 | -57.61198 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6204dc2-636c-30d0-b705-d65ab6ec95c9 | -6.67067 | -55.05623 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2253d66-3719-3d89-8039-ec6d25e9f950 | -13.9228 | -47.835 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fbe04c28-635d-3cb6-9e0c-6ad3a02b69b2 | -6.67617 | -55.07353 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbf1a7f3-5c4d-31e4-a1f6-4ce988099b75 | -12.04515 | -50.34984 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e9aeecff-bc4f-328b-9233-cbb54409246c | -6.84068 | -55.30481 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4812e1a-efbe-374d-bb12-49ce7c6c4b95 | -9.86755 | -48.39487 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e52ac1df-250e-388a-a313-7f9d920d4f57 | -9.93753 | -48.47216 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be0cbd7c-35f3-3e43-aff7-d48a89fcd42d | -9.70993 | -37.27568 | 2026-09-23 04:27:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70252aa5-a7de-3a5c-9ee3-ce663b1b273e | -14.62736 | -45.66302 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0db2a229-ae94-3f44-a4ef-5d0f743a2fab | -12.50646 | -46.96464 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117661a5-4c18-3458-8f41-b89c65aa3d3d | -12.41685 | -46.97266 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d2fe390-b4a3-3093-810d-4bf13a235f1f | -14.62033 | -45.66195 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f5e1dd2-0146-320b-afca-896cdab01985 | -9.58591 | -48.43376 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 429251ff-f5b2-345c-8f20-14c0038c5c3a | -6.56766 | -55.40684 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e5a97ca-5da3-3206-8492-a88f59be41fe | -7.65138 | -45.44373 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0232e1e4-3016-3eeb-9f63-86e085f0ee4e | -14.63348 | -45.65063 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15976955-79d4-373d-adf2-e7af273c62d0 | -13.45601 | -46.26761 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe31d439-bc72-3979-8826-cdcf8901d584 | -12.77669 | -50.86767 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b55f49e-ea21-3502-bb08-95e92eacff4c | -12.6679 | -45.04107 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66660e35-ea03-3ef8-96a4-6539227e90d7 | -14.63868 | -45.61385 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aae02d6-8843-38da-aac7-c8615ef2bfee | -6.67216 | -55.06656 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ea126d7f-f566-30cf-976f-294ed263854b | -7.13107 | -48.42715 | 2026-09-23 04:27:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| cddabbfd-db7a-3993-b601-3bb91fa43d8a | -14.60104 | -45.62163 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e8aefc7-22f3-34ca-af2f-79f8d589569e | -10.24452 | -45.50215 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34783a74-7e3b-3bd9-82d0-dd196b4b4bd9 | -11.27803 | -44.04337 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2b6f7a-ce78-3d0d-8e4a-d4c831c90818 | -14.2973 | -43.18872 | 2026-09-23 04:27:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 96480f4e-f43d-3117-a116-ebaa5e14c825 | -9.66064 | -46.72456 | 2026-09-23 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 032bd6f5-aa52-3a91-9cda-fe622a253a38 | -6.93449 | -46.56296 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2ec2c9-f9a6-3b8f-90e3-99607bc1dce6 | -11.68923 | -43.45033 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76829d89-33da-321b-9b51-5aafc9e2e91a | -6.10259 | -57.67745 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c1fd19e3-9dd8-34eb-adc1-07b33c76cb99 | -13.30093 | -47.89695 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60e487d0-66b9-3a9f-a1e5-4e5389393169 | -11.66542 | -43.48079 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 725c43db-706c-3145-997a-74ba6186a6b9 | -8.44527 | -55.01757 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74b7880a-3938-388d-a3c2-1ef707b8ff01 | -14.38078 | -47.2423 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76082b23-c9da-3e7e-b285-e3030be02eb1 | -11.53412 | -45.35649 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 7d5f0ad0-e637-31a0-a273-b6b17a3d3c08 | -8.46252 | -48.69166 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.4 |
| bb0d1983-b8a9-3da8-96f5-939b8bc96a3a | -6.46209 | -49.87437 | 2026-09-23 04:27:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae9edbf4-7678-3103-b35d-b4c8e0c6b8fb | -8.39984 | -46.52154 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69424810-dc48-3507-bd1e-f6d523ade4e4 | -7.53502 | -45.40413 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68996a4b-b93c-30d3-abfb-2f68282684e1 | -6.61864 | -59.93094 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a2a1b62b-898b-328a-a539-c6fbbf17a027 | -11.35818 | -43.38548 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d975748-c8c2-3464-a1a9-c0836561a447 | -14.60864 | -45.64361 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f911124e-1be2-3946-bf25-288843ecfe8b | -8.08838 | -44.34608 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81af7a49-b84b-3094-bb6f-8a80eb940bef | -11.13494 | -42.78484 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| adaca42c-fe79-32b4-a16d-6264f40da9e7 | -10.31599 | -50.50653 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5085fd74-e5d1-33d0-a4d6-a7f332da7374 | -10.51091 | -44.87402 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114e8bfa-59ab-3523-921d-7755c46729d8 | -9.73655 | -48.15071 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2a8593-db60-3d0c-8c2d-bdd9838bc228 | -12.81538 | -50.92107 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f76c2315-627a-3084-81b8-551693344454 | -8.35643 | -45.63274 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a65cc601-77b8-365a-a213-b4996dc5efb6 | -8.77778 | -45.63107 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b51f6161-5e4d-3971-a7dc-bc054fd71a97 | -6.52806 | -55.35727 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9678d3b7-ec4b-3832-8045-17a809fc3704 | -8.37419 | -45.6062 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e9f32f7-6fe0-38c0-a83e-934b0947f468 | -6.34207 | -49.87423 | 2026-09-23 04:27:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 476c9c2d-1c13-321c-8f6f-17dc068d8692 | -9.83878 | -46.38601 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82502447-5fe8-31a8-9624-4c90916255b6 | -6.78764 | -48.6865 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b5789a6-6ab2-3af9-affc-342ec7eb1514 | -14.62854 | -45.65492 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fa4043b-7690-3d09-af88-77f019b74f8a | -6.6142 | -59.91641 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 77f5a4e1-ae27-338a-b492-06e76b49dc73 | -13.86657 | -48.56586 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7803e9c8-ff9f-3128-ae15-6ffcd94f26cf | -12.72699 | -50.88031 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00939a4e-511f-37e5-ad35-53b0ffdf1b72 | -13.92171 | -47.84208 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3449f5ee-7b7d-3375-bd3a-f58d116a0923 | -10.00451 | -45.18652 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f869d7d6-eeda-33ce-83fc-9682bc41be75 | -12.03259 | -47.81029 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24464bc8-0da3-3e3c-af3e-c48288215b1f | -12.07171 | -50.05573 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README65.md)
