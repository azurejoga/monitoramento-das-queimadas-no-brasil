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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27ed588e-71ae-33f7-a112-a30819cc6911 | -8.95789 | -60.52021 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bddf48c0-0f6c-3a82-99fe-9c036ed0c5a1 | -6.83372 | -59.10164 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe411e7d-d0a5-36a0-a5d9-9a298bb2bbcc | -6.83221 | -58.97874 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 819363f7-097c-3353-97eb-9e70826ae083 | -10.07396 | -60.49673 | 2026-08-17 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbbf07ef-e41c-32ae-875c-c8835d93a6a2 | -6.78475 | -59.45635 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c6fb5a8-2106-3ea3-9b65-34fc658846bf | -6.85156 | -58.97193 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d612c02-382e-3a3d-9687-769bf6b37ce7 | -7.45744 | -59.9973 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 535abf05-6b14-3819-ac9f-a71c8cde1d75 | -8.97743 | -60.52002 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5969746d-28a2-329c-9dd0-b81f35efadac | -8.98264 | -60.5248 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28b1b8a8-e759-3e3b-950c-87a7490fccea | -8.9636 | -60.52106 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a551000-2810-3c4c-be5d-b7cf707091ec | -8.95482 | -60.54371 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aad8243-8f1b-3195-8f7b-f518559edc9f | -8.98216 | -60.5287 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2442fe6b-e2f7-3fbb-a0a9-dda47c1ac570 | -8.95841 | -60.51624 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 620e433b-bdbf-3ad8-8b38-3ae4ae2e52e8 | -6.11163 | -57.73721 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 17138c2b-ee04-3cb8-a5b8-ab98b34f3b19 | -8.96503 | -60.52625 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2b9b169-f5b2-37ee-863e-9d1acc66e73f | -6.10585 | -57.73049 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa44562d-ba78-3ea0-95d9-593ed60f5876 | -6.64787 | -58.95384 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 523da8aa-c369-3c18-b049-6e9840387af7 | -9.47515 | -60.50678 | 2026-08-17 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27cd4359-9cef-34ff-aea5-1621776ce6cc | -10.92012 | -62.76964 | 2026-08-17 06:01:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a79ad32e-cca9-36d1-885d-5cb76ac2d54d | -6.61488 | -58.96782 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d27ebd9f-a5c6-34c0-b477-b13cac3fba06 | -6.8716 | -56.42237 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c89330ee-f54e-3bec-afda-4c0cc5df44c7 | -8.98313 | -60.52089 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf7e5221-2634-3d5a-8561-dcf2fdece349 | -7.55524 | -61.175 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1941f59-c1e6-3bc6-b52c-e3552df3dd9d | -8.9543 | -60.54768 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01359b2f-a27e-3a3d-834e-9ede4d7afe32 | -8.97596 | -60.53181 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b69e25a-cbbd-3566-b9a1-711c7df40ec7 | -8.97346 | -60.53447 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c6312ae-9b03-300a-bc87-43fb268af918 | -8.9067 | -60.55694 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afdab448-3b61-3a7e-a4a6-48209fcb424c | -8.97123 | -60.52312 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b0380d-ba34-35fc-b221-60f2eb21fec2 | -6.12488 | -57.73167 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47016475-ef21-341f-8bb5-a9a3bd2cb09b | -10.92056 | -62.76625 | 2026-08-17 06:01:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0be474d-40a0-3e0e-9d0e-b20949b92467 | -8.90472 | -60.57248 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d92c663-add9-3b6a-bcc4-4ea7c51f4a8d | -8.98335 | -60.50361 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92189029-ba23-38db-900d-da937670f104 | -10.91515 | -62.76831 | 2026-08-17 06:01:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b472dd9-1aa4-32a0-9e58-b46d436e7217 | -7.38106 | -59.9927 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cb6cc34-948d-3b72-85ec-f48dba6c9f8c | -6.89714 | -59.00705 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f5b4ac1-a408-36ab-85d2-b30daffde478 | -6.83954 | -58.97035 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67ac50c0-ce90-3d71-9469-8293a0ad9fa0 | -6.77759 | -59.46442 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9478a8bd-8f63-360f-b311-2fdd129ebce8 | -6.63093 | -59.08265 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f1cd6bd-7c90-386e-9489-27c4742aa349 | -8.91956 | -68.9053 | 2026-08-17 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe34422-3b25-3ff1-a57d-cafdf5d3ef84 | -6.96432 | -59.29942 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29906671-a6ca-3182-8688-b3235275be4b | -10.04733 | -62.45382 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a36fce10-679b-3b03-93ef-687effc8fa41 | -8.97763 | -60.50284 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf86242d-b89c-3adb-ac2a-b9b7acb1c25e | -6.98652 | -59.03957 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6e020c8-33d2-327e-ae98-13494bb0fe7b | -6.98224 | -59.02478 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d005a24-0738-356b-8ba5-8fa6286fefff | -6.6467 | -58.9628 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1966ad8f-a217-3589-81c5-5d315365545a | -7.88889 | -61.80056 | 2026-08-17 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6560277-be4e-3ef6-a40f-9987b080e4d8 | -6.77472 | -59.46917 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c92c83d-1b4b-3a77-9243-03e332d76331 | -6.85028 | -58.98126 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27a2b382-6502-321b-a566-cbd2179e350e | -6.62158 | -58.9642 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62b36ae6-692d-3504-80ae-d46369f76ae0 | -6.62606 | -59.06329 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4feec2f4-6879-359d-a8e7-05fb9a6afa23 | -7.58998 | -61.22665 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ce97598-6594-38ee-8741-f2d16dceac85 | -9.33371 | -62.33427 | 2026-08-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b541748-b9c4-3ac0-9b72-bdb18fedf22a | -8.95675 | -60.59311 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29b81994-9aab-362b-af66-15962ddb2cb9 | -8.9603 | -60.51746 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ce8a1a-f677-3179-be50-0e41c0cc78d2 | -10.04694 | -62.45687 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd9e363-8a4f-3047-aba0-0938eae2bf56 | -6.54577 | -58.50338 | 2026-08-17 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bebb7ee-b960-394b-a770-2d75e4a7d399 | -6.10813 | -57.71353 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b857e48-4e89-3d3d-8c9a-fec6403be874 | -6.77586 | -59.46046 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bbbd289-a68e-3fac-afe9-6a7456304fcc | -8.95397 | -60.56877 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5761c537-473b-3882-86f5-000166af63d4 | -8.96879 | -60.5258 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e65d2b30-c8d6-32e8-999a-307aa7915c54 | -6.97492 | -59.03307 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c27ada3f-0d00-3932-8295-ca2af4f29f30 | -7.33799 | -59.60085 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e9bf6b5-941f-311f-ba41-af44d5cf8d3a | -9.18006 | -59.67366 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1b04425-1269-3e1d-9688-1f0e669540a7 | -8.09353 | -61.35493 | 2026-08-17 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9bfad7e-9569-3238-84d5-3bee08cf9692 | -6.60086 | -58.97523 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3aa3dac-7952-3775-8abc-a03040357481 | -6.63329 | -58.9659 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09185158-24ac-366a-b4f8-28c1cbe76347 | -6.62104 | -58.96429 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a5e8c804-86db-3078-8c0b-650af33a243f | -6.1147 | -57.71437 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be8f2350-eb63-3a60-bfbb-858e03aadc73 | -7.5557 | -61.1716 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ca4b383-dbbf-3bd6-bfe3-6ba4ef80ade9 | -7.40723 | -60.01737 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1495e479-ffae-3bd8-a916-45f2649a3d52 | -9.34794 | -66.60979 | 2026-08-17 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18f6006-dd75-38d6-a053-516c8b8bfaf2 | -9.40735 | -68.76012 | 2026-08-17 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b73fc53b-b956-34e6-b99c-90bec2a1a6e4 | -7.88904 | -63.7598 | 2026-08-17 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05db3b94-ad04-34fd-beda-d71d4bd015d1 | -9.33331 | -62.33731 | 2026-08-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb7c0324-4094-3310-b29e-d703e1e06d16 | -6.77819 | -59.46003 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0a39258-ae7b-3bdc-b89c-7a0aeb56e1a8 | -8.97842 | -60.51205 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4923146-0e9f-3b4d-bca8-ffc5959f53f7 | -6.78065 | -59.47005 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 814e18c9-2271-3b46-9055-51f43f720dfc | -6.98041 | -59.03865 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b59589f-24a0-37e2-b22f-dc4712326141 | -7.40776 | -60.01346 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8ac6fb-f74d-362a-9391-07ebef7d9397 | -6.83867 | -58.9748 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eaca93a1-e5fd-3c35-83f2-966023a3cef2 | -6.6278 | -58.96051 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5fa63012-aa3b-3606-a7fe-be77072e4000 | -6.62485 | -59.08182 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cb4e1a7-9bfe-3260-b6d7-e570f19f576e | -6.84964 | -58.98594 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eef8ad94-773b-3754-84e8-4bc47085e89b | -6.77663 | -59.77163 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f018281-6af6-3762-9d6d-7e074d71c38c | -9.52423 | -70.50942 | 2026-08-17 06:01:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec3fa49-050a-3f83-9714-98ea10c9440f | -7.45674 | -59.99993 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9a1eb6c2-fa73-3e5e-b797-7d7993956cdd | -6.83192 | -58.97849 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02766536-d007-3287-941a-facdb6424d22 | -8.90102 | -60.5561 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc1262c2-134b-3dca-ba1b-a4de05c597ef | -6.65281 | -58.96373 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 029481f9-d346-39e7-b4b0-cdb70cf29a59 | -9.17587 | -59.66936 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e11f9a8f-b54d-367d-87f1-ff5509d06296 | -7.55479 | -61.17838 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f18b9e51-bead-3265-a12d-a9d0cf0b252b | -7.65633 | -69.99345 | 2026-08-17 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb540a4-6831-3d97-b5da-8484ef6c67d9 | -8.95932 | -60.52541 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee8bec1b-5225-3752-a963-0c759abd69bd | -8.98072 | -60.52351 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd7d6314-a445-3ad1-8aae-4cf1f974ea07 | -7.43063 | -60.02251 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b85739d1-ad45-3cf0-bd78-831acf78f566 | -7.59042 | -61.22328 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ed8c7d8-e3f6-366a-a5c8-2133431f4c65 | -6.61368 | -58.97258 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 830c9424-0714-399a-9209-3652ebf8e0e1 | -6.11977 | -57.72636 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 219fac38-74c6-3dad-8b19-1d1e977065cb | -6.10436 | -57.74165 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e5940410-db33-33ed-a288-1258eda37008 | -7.88737 | -63.75823 | 2026-08-17 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README64.md)
