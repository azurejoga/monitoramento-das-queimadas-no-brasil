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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34db6c1f-efb7-37e6-bb92-0c7934f65cdb | -10.11765 | -68.07532 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14a4f188-de12-3022-8d47-554447c933ce | -10.84235 | -69.4882 | 2026-10-05 17:37:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c757fa62-1dd4-397a-b7b4-06eae6464991 | -10.21978 | -68.40376 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae79dfcc-1f55-3ef8-a4ff-711299abd9e9 | 2.06796 | -59.88175 | 2026-10-05 17:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 558c06d8-0cfd-3841-8bf3-9624302e3e93 | -8.57182 | -66.99837 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd8065e5-3456-3afb-bb17-2d4d3a1175f4 | -2.29867 | -57.08632 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 156d91e7-dd27-3366-a546-a286c19fffa9 | -7.22941 | -55.20762 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7e375570-bae5-3c87-af45-8c96cafb8960 | 2.10094 | -50.73787 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dc87f1da-baa8-337a-b1f5-2d451d5d0ffc | 0.31034 | -60.43686 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c98c323-a966-3898-8fd8-6ccba459e4d9 | -9.01272 | -67.74986 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0a79e35c-e2a6-335e-8bb4-d0b77202f277 | -8.88332 | -66.81837 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f78cb541-01a3-37db-85b0-e93f2fe51445 | -9.137 | -65.91026 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| aeb46745-2670-3071-be48-bcd89ba2c08f | 2.40235 | -50.89835 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daf56ed6-2cfd-3379-9a39-4816160a989c | -9.26689 | -67.62398 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab1e80f7-b5e8-39ab-a70e-5c054988ce91 | -2.27565 | -57.01361 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a33ba8d0-afff-3519-8bc0-ae774dd53fd4 | -9.04754 | -66.10738 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| df4bcf77-32ab-3655-a0c3-4adbd5f35c9d | -9.01672 | -65.69056 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4036bad5-8e07-3469-bc3f-35e2a744f5fd | -1.95997 | -55.38689 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 750ea033-2200-3010-8aef-accc1a790e69 | -8.90395 | -69.38847 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd79aff4-3f37-36d7-ac85-95fe82c2ad31 | 1.57526 | -55.99174 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 88e16dcc-7617-3b05-8557-b6948ad27f7e | -8.86252 | -66.7795 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d4681dfe-c84c-3dae-88c7-0addf1f0e7df | -1.61606 | -55.10844 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0561b70c-01e0-3db2-98ed-2c1ad5cc6db8 | -9.13389 | -67.92511 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0cd6dbb3-bc8b-3bac-aa52-fe8361821473 | 3.35218 | -51.33866 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 620fdb82-6ac5-3bda-bfd9-3cb816e1953f | -0.37277 | -52.06077 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4148ca8a-4afc-3a64-bb09-2bf7b4d31651 | -10.06782 | -68.58688 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 110954ef-43ee-3137-97c1-3ab65b8db73d | -2.37728 | -56.12147 | 2026-10-05 17:37:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| af7e0b9f-84a5-3186-bac6-004b8e539416 | -8.87071 | -66.83002 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3d95cd72-6315-32cc-b3ee-73a5fcd976c7 | -9.47287 | -65.68154 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6bfbe4f7-8dab-34ce-bd3d-ef61606e1f7d | -7.23258 | -55.18742 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5572d850-9372-37df-b22d-b718b4860f54 | -9.07977 | -71.94945 | 2026-10-05 17:37:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1e166d2d-0eb2-398a-a3f0-0bc148e32a9b | -2.92484 | -58.06554 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd595301-453d-35cf-aceb-ada9ac896cc1 | -10.49376 | -69.43217 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a9b3dcb-9e1a-3194-bd7a-adb2cb4f2d3d | -8.94612 | -70.7438 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 209d7d46-c4e5-371e-9299-615cd78c52f3 | -8.72032 | -68.9008 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 18d8f5cf-bcf4-31f9-8439-2e161cfde910 | -8.97318 | -65.4412 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| df2c23cc-5072-3746-9753-9ce57f295699 | -9.82009 | -65.01582 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 042dea12-c610-3435-b322-2e36a43eb11f | -1.63251 | -55.12754 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d72621de-f7cc-3ee7-9adb-edb4cc39fa91 | -1.62379 | -55.1288 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d28ca17e-828a-3d66-aae1-86758de64e3a | -10.81361 | -69.54073 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e589c57f-7a96-3847-9363-337772bebe4f | -7.2269 | -55.19216 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e7faa53e-b5a4-3a4b-ab34-e0ab1ca64049 | -9.80623 | -64.98734 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.7 |
| a29e233a-0080-3410-bdd7-f66d303b143f | -8.86316 | -66.78437 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8dacbd22-5b05-38af-99c6-a4e27deed787 | -1.48881 | -55.66759 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25450a1f-0ed9-3eee-84d5-944e26f503d6 | 1.85291 | -55.79305 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 69f39ed6-f500-327c-b00a-376925d0b244 | -1.47813 | -54.51334 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 775f04d0-9313-32eb-98c0-964057f67967 | -1.55832 | -55.1725 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7e1b433f-67fd-3cac-9b8a-6fa68f0af2a0 | -9.80348 | -64.98693 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ab04aaf4-5b83-31bf-bf52-109ee2342ab0 | -8.6401 | -66.51098 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8914492a-7cd1-3076-9414-108261896ba3 | 0.43855 | -60.53291 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ba6a6aa8-9fb0-32b1-8e6d-696672321bf0 | -9.48673 | -67.1567 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2105c26a-c2b2-3275-a2c3-858eb51463d0 | -2.53655 | -66.04575 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 67c12851-e769-3c1e-906b-01587dc8c5d7 | -10.35509 | -68.41706 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f01817d0-87c2-3e01-b872-acfb1993acda | -10.34847 | -67.98762 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| deb2649a-d3af-37e7-b897-cf4968e7b5c1 | -1.62043 | -55.10777 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2cb1f5a3-c1d4-3e88-bfb0-536a80f4358a | -10.09972 | -68.26088 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff883cc7-1be5-367f-91d3-babf617b5b01 | -6.36701 | -55.13256 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1aa78654-64ef-3c60-b190-4e0716d0de3b | 1.48029 | -55.66978 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a52143ed-c52e-3abe-9567-a8b349210576 | -9.1759 | -68.27287 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d03a3cc9-c7b1-36a6-99b3-6fb5971761e6 | 2.29131 | -55.89837 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ca43b64e-9154-3dbc-af5f-e0028ed1845b | -9.46941 | -65.67868 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ece276c-b574-3f83-b8e3-be8c6b3dcc53 | -9.16292 | -68.24025 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fa008443-7ba0-3d83-bdef-2560450d12f8 | -10.40083 | -67.82836 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00080a1e-d7c1-3182-aa23-1e45094bac53 | 1.84656 | -55.80513 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ece3c3b6-de67-3802-ad11-18f0cf0ee709 | 3.08419 | -60.591 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 034db4a5-1b93-3700-9447-176bbc3678cd | -2.94695 | -58.56064 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5a4d9460-3544-3e9d-91cf-db82a43ebf73 | -10.44391 | -67.89867 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 25056cbe-bbc9-3e2b-b7c8-6662c5cc4ba9 | -7.22685 | -55.17768 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2ce6a8f1-6617-3ed3-8675-f202baf0edfb | -2.55089 | -65.86877 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 80cea07e-9a5b-30d1-a6a1-2d188530f800 | -8.97958 | -71.40602 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 906ad715-5a4a-34c4-820a-e6702a23df3d | -9.33919 | -68.79113 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a4fafdb0-473b-3c8b-a45c-951b3d76f4e3 | 3.50282 | -60.34758 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1681e36a-1307-312c-81bb-b1aa1be67ab1 | -7.4439 | -55.68036 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d73e80f3-8cb7-3f6c-a5fb-c56466e519a6 | -9.35857 | -67.43457 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b77d0240-4dcb-3f85-89a9-93b6b3b865d9 | 4.05129 | -59.99056 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b6ed26db-1fa4-396a-b037-a0df02a7f03e | -9.35614 | -68.7958 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fa46f4fa-8af5-35a1-9778-c9711800981a | -8.52166 | -54.61426 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f320d39-efff-3bfb-a885-6dcc0b224b63 | -1.25051 | -55.72048 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c55e530-fac9-360b-a091-c97b851194a4 | -2.43918 | -58.01601 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5141149a-ac00-345c-b1e3-b5c311ac8e6d | -3.81685 | -69.44302 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf1dbae0-926d-389e-9b67-15ef27107397 | 0.44471 | -60.53745 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b81b87a6-15f4-322b-b5a7-855ec407bbec | -9.34176 | -68.79398 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 73161e52-b945-38ec-99f7-22c734087d26 | -10.11991 | -68.07769 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a553cb86-79d8-3d77-8f7f-4addfc3f254e | -3.49028 | -68.98969 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 33667bf2-8775-39c0-addd-dedda50134a3 | -8.7414 | -66.5728 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f192cadc-d098-366f-aae3-0ef2d121fde5 | -9.36333 | -65.92549 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffdef4bd-8d0d-396d-bfb8-b916016cba86 | -8.85137 | -66.79298 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 8e007266-db0b-3781-98ec-706751e51592 | -9.26403 | -68.3697 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 48e75024-e1b5-38e9-a879-3ff21904d316 | -7.12552 | -55.72624 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 284947c6-fed0-3d64-8104-e589e6ff8c0a | 1.05269 | -60.55267 | 2026-10-05 17:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 81f72c87-9dc7-31d7-9722-b3bfb1734fbc | 3.50225 | -60.35135 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1aca2439-55c3-37ff-80d2-4694f0d51baa | -8.57651 | -66.99771 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff519de7-5734-32c9-936e-880153b0303c | -2.63732 | -57.72592 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7887fd4e-1797-3743-b212-ed2c333f928a | -3.17497 | -60.0602 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7da2862f-3808-3609-a662-f238f5128f60 | -7.22604 | -55.18684 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 538f06b1-ff2d-33c3-8fa3-da1f8f2d7743 | 1.83081 | -55.55063 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b55e2c4b-5011-362e-bcfd-9b5ba856a126 | -7.22771 | -55.1828 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bb839ae6-3168-382d-ba45-53deacbc8478 | -10.56444 | -68.34262 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e97020bc-09cc-3088-a360-838cf6cf03a6 | -7.3816 | -47.43522 | 2026-10-05 17:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4bedc328-7924-3e43-b7e7-d770d3453d83 | 3.52309 | -51.50103 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README156.md)
