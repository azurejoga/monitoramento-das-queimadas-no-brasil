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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c08d32c6-e3ff-3f4c-a506-2307a663ebf7 | -4.9951 | -56.256 | 2025-09-04 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 968384b1-a377-39c8-8027-f547bcb4f170 | -6.7503 | -58.7462 | 2025-09-04 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| caf27b20-16a1-3c96-a749-7090da7b060c | -6.7504 | -58.7268 | 2025-09-04 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 24a3ae0b-d7ec-3a2d-8bf3-ac827213b268 | -5.0135 | -56.2553 | 2025-09-04 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ddfa0924-869f-3b57-8b5e-cefd0d8cbef8 | -3.43003 | -59.57387 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c646bff1-e570-3301-b888-6a6662ac467e | -3.43075 | -59.56898 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b58c9d30-afce-373b-8af5-2de2aa69cf0e | -3.43698 | -59.57001 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa81daf5-3cae-332d-ba4a-f31055bc220f | -3.43516 | -59.56926 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 870d4af5-1f47-3ac0-a6c7-bfee3fcc3a13 | -3.43447 | -59.57415 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f32bcf95-47d8-31c4-a78a-bbe3a8e2a432 | -3.43627 | -59.57483 | 2025-09-04 06:05:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa5786c5-5d1e-328c-88e3-5b37fc30f1de | -8.88155 | -69.34403 | 2025-09-04 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 958baa90-c461-34c1-8fe5-1b9057573729 | -6.78393 | -63.13867 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01fe4711-44ce-3282-a703-6bbbfd268c74 | -6.74175 | -58.72258 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e192ac96-0526-3a62-90c6-5f8586258b17 | -6.77963 | -63.13162 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 350954fe-0c67-3482-8b69-2d8c9f523e22 | -6.74577 | -58.73889 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| deb0c4fc-a423-31c7-8a18-d1de83a835b7 | -9.37644 | -71.10838 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2bbfb8-8163-350a-86e0-789c4a87791d | -6.77465 | -63.1397 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3f58c95-1985-3a06-b5a8-a6fb7c7d2e21 | -6.77507 | -63.13655 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e865e75-1a07-32ae-974f-b31ba55d93c1 | -6.75386 | -58.73725 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 70b495cb-762d-328c-9a20-8aa81c1093d5 | -6.77874 | -63.13794 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51f01410-502d-369c-9f8b-f7f24281e460 | -6.83998 | -59.15445 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb58d6f5-50a0-3c65-834f-445fa6243a3e | -8.34832 | -70.25912 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d785167-3e0c-3362-a714-11f3e9a3833b | -8.77261 | -71.05984 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a676b40-a16c-31bb-a7f6-ca08a9b74ba3 | -6.75841 | -63.1319 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e85c28b-9baf-32ce-9733-0260d219057a | -10.25042 | -61.77401 | 2025-09-04 06:08:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f370374a-da36-3f46-b2cb-93c80e7b5945 | -8.58188 | -70.63769 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9abb623-9ef4-37da-b73e-f2461da20a38 | -6.74063 | -58.72506 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 134d38bb-51d2-3636-b13d-a749181e7a2e | -6.8395 | -59.36425 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55dbc90d-11a0-3ce2-a2a6-aa1d59ab6205 | -6.73884 | -58.73845 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f7258fdc-4b51-313d-a3aa-fe7273265903 | -6.66653 | -60.0304 | 2025-09-04 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faa2671d-8aa6-3f23-9a25-1544415c0878 | -6.75885 | -63.12876 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 050f3a26-b0d3-3a93-911e-8ee39f9adece | -6.74664 | -58.73239 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4705397d-f637-3032-8c62-bac2bb06e4ae | -6.78504 | -63.14119 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9cce466-8950-378a-b945-36e5f0289224 | -6.78069 | -63.13415 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da123c08-2411-3a60-9e93-09c902bad78a | -6.87513 | -58.93783 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a90b4659-8afd-3bb9-a4d9-2464673e76ac | -6.74092 | -58.7291 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8a07d4ea-93a9-3dc1-ad0f-8f00174289d4 | -6.75438 | -58.72688 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66084c72-82c4-3dbf-a990-d17b018a492b | -6.7478 | -58.72999 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af756569-6ff4-3f67-89ab-8fa72356ab7f | -6.883 | -59.08747 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36a74f8b-c989-348d-808f-d2cbd5294e66 | -6.7475 | -58.72595 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9d65627e-e82a-324c-8a2c-440a266a9ffb | -6.74005 | -58.7359 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 464eb24a-bac1-3e5f-b79c-4e047aca4b3b | -6.75266 | -58.7396 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a26a3cdc-e734-3cc9-bbe4-1dd7e94fc2dc | -6.67287 | -60.03133 | 2025-09-04 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863bd705-712e-3f0d-9448-7cc72f8cfdcc | -6.78912 | -63.13938 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f4568b-3b36-3516-9f77-ad60c5d44474 | -6.83744 | -59.36554 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 69f14055-dee0-3cd5-890b-d5a2d5e258d2 | -6.78026 | -63.13731 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22c80125-9d86-349f-8f51-a69d12a7548e | -7.9954 | -71.0061 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 069b4350-45d6-33d3-b001-504659a01f54 | -6.76924 | -63.13017 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c5468f7-e431-3ede-88f5-462f027beb92 | -6.75467 | -58.73091 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8afaa2ea-d029-3a95-9e2f-f71b598fe709 | -6.83289 | -59.36328 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6eb766e9-3ea5-303a-8dba-80bab95a042b | -10.24989 | -61.77819 | 2025-09-04 06:08:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8bc16ba9-57c6-33c6-b01c-f28121e5ee34 | -6.77399 | -63.13404 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b61978b0-6b21-3b6a-9a59-2fc348980c4f | -8.37273 | -70.84395 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ddf4016-ad46-3931-8f49-cf196217bb66 | -6.7636 | -63.13261 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49b372da-b235-3a30-b5f1-d9945000fc8c | -6.73975 | -58.73168 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e3a0032f-8c32-32ad-bf8d-0902b9eccec1 | -9.08425 | -71.59492 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 826a049e-392a-3952-bc72-fd297c939c8a | -9.08371 | -71.59843 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6630ab61-8444-3f01-9665-336aa50732a0 | -6.7688 | -63.13332 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f8427c48-cde5-3d2e-bea6-0d104992d98a | -8.37077 | -70.25043 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13e044db-68fc-3de4-8a45-bdf8840b1d34 | -6.84747 | -59.1494 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19687606-64a8-3acf-9a9d-a2acf41a3fcc | -7.01865 | -59.65941 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e89b463-36f8-3ff7-a41b-56f242b0b151 | -7.99139 | -71.18678 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 435d1ee2-147d-34cf-82ea-845bb9aba152 | -7.88263 | -72.99216 | 2025-09-04 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ade9c89b-af8e-3dea-889d-0c55da86e5f2 | -6.78546 | -63.13805 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2766f2a-1514-3c30-9cae-3d565be41a5e | -8.60958 | -70.68314 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b6b5a09-0130-3f11-91af-b958d0472c74 | -6.77829 | -63.14108 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2118325f-1920-3b3a-bc8c-a94466c9e223 | -6.75352 | -58.73325 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 755ff761-6335-30ac-adbf-644d92cf6138 | -9.1771 | -71.63159 | 2025-09-04 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1ad0acf-12ba-30cb-9ab4-afb22baad96a | -8.54732 | -67.12273 | 2025-09-04 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98ee0de-2ff1-3bb3-b965-e8780e1ece88 | -6.78438 | -63.13552 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 436b7f28-98e7-33c3-b062-fcf8879eac98 | -8.03132 | -71.25766 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e5d07c-1ed7-3ea4-8823-e3870b3f82d4 | -7.99444 | -71.18696 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8529199-c180-326f-bbed-ca739edd54f1 | -6.74697 | -58.73642 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 675fed76-6141-3cba-944f-88a3ad0fad66 | -6.74862 | -58.72352 | 2025-09-04 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8e07cd07-8537-3976-9419-2944ecb3f25f | -8.54629 | -67.12995 | 2025-09-04 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f3bf99-4021-3ef7-9d7e-6eca2740a51e | -7.01797 | -59.66485 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e6aa53c-8b6f-35a8-8927-d6987cb94c75 | -8.22957 | -72.79972 | 2025-09-04 06:08:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfd2f312-8ae3-3e6b-97e7-b1d0ee9fb731 | -8.37218 | -70.84756 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90ec6cb-6010-3868-9b1a-b9eb0d78263c | -6.77918 | -63.13479 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0bda25c-85d7-307b-8dec-431dc2ac735c | -6.76405 | -63.12946 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d477cee3-576b-3ff6-9e5d-b0bdfe6385bc | -7.99595 | -71.00253 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eefda4a2-c53e-31e7-ab73-1370079bab0b | -8.88513 | -69.34458 | 2025-09-04 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 329036ec-80f6-3d90-856d-97f98357a10e | -7.02516 | -59.66046 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54d23adb-5a26-36e1-88e3-f220e889d4c4 | -9.37252 | -71.11147 | 2025-09-04 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eadc261d-2448-39e2-b2c5-7f77a7a6b229 | -8.5435 | -70.84398 | 2025-09-04 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 916c558e-fe1d-363a-8799-450d9b1bc29f | -6.84668 | -59.15538 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4c138b5-aa0f-3022-8b02-87f5ea0e8b48 | -8.5468 | -67.12634 | 2025-09-04 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 028b8052-ef7b-3487-85f4-78947fce99f8 | -6.77549 | -63.13339 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 090c5bd8-be37-3234-ba0b-e5caf08b585f | -6.78868 | -63.14249 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18feadea-5e7e-357d-b715-7ea701e0f7b9 | -6.77592 | -63.13024 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e2877db-856d-3877-b22b-741f2ce7c24f | -6.78111 | -63.13099 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b0a0682-bfa2-337b-ac1c-794db40e9225 | -6.83213 | -59.36897 | 2025-09-04 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 14bfa5ae-19aa-3fab-a27e-a48b889929f1 | -6.78349 | -63.14179 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9ceed9a-ea22-38fc-996f-754dc4099d01 | -6.77444 | -63.13089 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ecac8e45-f50e-3516-9169-66131a6a1df6 | -6.77984 | -63.14046 | 2025-09-04 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba428a0a-e2ac-3e3b-9e8b-f45efdd149af | -8.0228 | -45.39 | 2025-09-04 06:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| d0f06c8d-d02c-33c9-8150-d564ac017810 | -4.9951 | -56.256 | 2025-09-04 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ef9082a1-d8e9-3e0c-91bf-b6028f0cd2d8 | -6.7503 | -58.7462 | 2025-09-04 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 28beb4de-8830-38c5-b17f-8f8d667e6910 | -10.4984 | -46.7614 | 2025-09-04 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e938c746-80e8-3a65-b4a8-fc8df49a0c7c | -8.0417 | -45.3882 | 2025-09-04 06:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |


[Clique aqui para ver as próximas entradas](README95.md)
