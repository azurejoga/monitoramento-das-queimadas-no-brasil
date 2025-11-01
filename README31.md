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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d40540d9-9376-379a-b33b-e04d06d7d1dc | 1.26422 | -50.84327 | 2025-11-01 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a79e23a2-5b04-36a8-abec-5b1ebfe7ea2f | 2.12379 | -50.97987 | 2025-11-01 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7bc85072-606e-349a-9d8e-a8b131b97910 | 2.12253 | -50.97114 | 2025-11-01 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5b97425a-601e-3566-8efc-d130385a4349 | 1.73384 | -50.96087 | 2025-11-01 12:34:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3dfe4b2f-5319-33bc-98e5-31356e86ec3f | 1.25543 | -50.84449 | 2025-11-01 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f0a150c8-d8f4-3790-baf4-b40752e04a8f | 1.73259 | -50.95214 | 2025-11-01 12:34:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7cbaed59-2b14-3e5d-b5df-20952fad5c56 | 1.26296 | -50.83453 | 2025-11-01 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5637b63b-c281-3a08-9503-213a68216d6e | 0.50552 | -50.76614 | 2025-11-01 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 04536577-c689-3899-91a3-5d8d4b550eb6 | 2.61462 | -50.99631 | 2025-11-01 12:34:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8dcd5414-62d3-3f8b-b83d-d7ac0b60dba3 | -1.25683 | -53.86368 | 2025-11-01 12:36:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a895ad09-2852-3ff2-a119-2a586d89e83d | -3.64853 | -42.5556 | 2025-11-01 12:36:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 9953f966-d4dc-3689-9554-00872a4ff45d | -3.02182 | -49.44856 | 2025-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6496b1b6-e9e6-39b5-b181-c4fea487fdd4 | -3.63757 | -42.58443 | 2025-11-01 12:36:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 60af43a5-1cde-3638-9c9a-477c1851ec4e | -4.86361 | -46.65934 | 2025-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 6dd861c1-ad30-3cd0-98f6-cf25e54e1a74 | -3.41453 | -50.00563 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 389ea78a-0fc7-3d75-8ec0-7a306f582cb4 | -0.4318 | -51.76413 | 2025-11-01 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0d86651f-3b3e-38ec-b5e6-9548dc2eedcd | -1.83187 | -52.68753 | 2025-11-01 12:36:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f4e96a7-a535-3f16-a5e5-9e369f98738b | -5.00583 | -49.68364 | 2025-11-01 12:36:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 463c34c3-277d-3735-9738-2a6815a74fcb | -2.65048 | -48.51061 | 2025-11-01 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 88948aad-69f7-344e-aa6e-8d67e982d568 | -1.60819 | -49.87022 | 2025-11-01 12:36:00 | TERRA_M-T | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c845cabf-7701-3d4c-bb12-8fb555ab3586 | -3.72321 | -50.04658 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 358522a7-adcb-35bc-a9e1-e0cb96f5ef8e | -4.86123 | -46.67657 | 2025-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7c9494db-3c86-3c81-ab3b-6db3eacfe5bb | -3.02326 | -49.4382 | 2025-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ba4829c5-3eee-39ca-afcf-26f0f3391e31 | -2.80832 | -51.34766 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba736790-62a3-33bb-a029-f7cdafdf8f98 | -2.31245 | -48.58676 | 2025-11-01 12:36:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3e5dc884-d55b-315e-ae54-bedbdfe55890 | -1.01192 | -47.80147 | 2025-11-01 12:36:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 98712f43-e066-39b7-943f-270c0c6fd74d | -0.43306 | -51.75537 | 2025-11-01 12:36:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2ca1350c-49da-396e-8116-e836fe0001ed | -3.58292 | -42.35755 | 2025-11-01 12:36:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| bf586a51-f3b5-332e-8350-048b17de69db | -5.0031 | -49.6768 | 2025-11-01 12:36:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| b67f7861-a7b1-3c53-a77c-a5672ed3601f | -3.41584 | -42.20363 | 2025-11-01 12:36:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 7d83e3e7-7215-3e8d-8faa-294016d72e42 | -3.64224 | -42.54946 | 2025-11-01 12:36:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 7f042205-7bac-3259-aef9-fd673e5611df | -3.50435 | -49.95398 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9fb9d2ba-b4a2-3264-bc7f-07d0b4834d11 | -3.01229 | -49.44726 | 2025-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cc10bc06-8b8e-3274-b3c8-0b166bf922b5 | -3.64407 | -42.59072 | 2025-11-01 12:36:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 425d84c0-af31-3eab-b996-44b05cc26965 | -1.0137 | -47.7891 | 2025-11-01 12:36:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d8d1a4de-b37f-3ced-ac47-a66782b65df5 | -3.60417 | -50.62404 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4345b3ce-c935-3c4c-8b15-b6650d14652b | -3.23267 | -50.57653 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3ee57d20-8a2a-3f24-9738-b3ff7e0a1e2f | -3.31141 | -50.0154 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| efde70de-fff0-32ca-a97f-ea687e33eba9 | -2.31088 | -48.5981 | 2025-11-01 12:36:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d9514308-ba6e-3347-a420-784d9f0abe9e | -3.1474 | -49.41855 | 2025-11-01 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 39fe31af-f6f4-3ca1-b47b-1b0c412cdbf5 | -2.80706 | -51.35648 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb6d0958-5ca8-38ab-a35d-bb7c163c0bb9 | -3.96386 | -48.92273 | 2025-11-01 12:36:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 0df770bf-edab-3997-8af8-ecc0f24d52f4 | -3.57166 | -50.26684 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2a4c4649-0819-3460-8fa6-3c18f06f2e54 | -3.97868 | -43.07323 | 2025-11-01 12:36:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e73de7fa-e8c8-3db8-a516-97c96e0a6e26 | -2.97624 | -53.26123 | 2025-11-01 12:36:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 412207d5-23c8-3bde-9a1f-d251521dbe98 | -3.07229 | -51.24922 | 2025-11-01 12:36:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fc04821a-4512-3e83-b524-ffc2e93fc2c3 | -2.87659 | -51.38998 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bffbdbcb-8207-33bd-ba1a-3ba2e28062bd | -3.57824 | -42.35032 | 2025-11-01 12:36:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 0c5ef51a-ccc0-38a7-b42d-26502b25fea8 | -1.30454 | -49.34435 | 2025-11-01 12:36:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| adf09d53-5048-38e7-8578-131cb8a4fa6c | -3.23136 | -50.5858 | 2025-11-01 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3974a7ae-f971-3856-97ed-a9e928010057 | -3.96547 | -48.91124 | 2025-11-01 12:36:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0626a732-5c2d-3843-91e6-ec9647ceeddb | -3.32886 | -54.07632 | 2025-11-01 12:36:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 05146a0d-4108-3fe4-b79e-18c918c2985f | -5.00729 | -49.67292 | 2025-11-01 12:36:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ad3571ca-e4fc-3f8a-af79-27d14428170c | -4.86821 | -46.66642 | 2025-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |
| bd2ef4c9-81db-39e2-a8af-347957bb9068 | -3.29184 | -51.89954 | 2025-11-01 12:36:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6f09dbb2-6d91-3a69-bc26-0e355ed41cf6 | -3.4159 | -49.99585 | 2025-11-01 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 05d4a9ad-483d-3707-860c-4860f05be978 | -3.29309 | -51.8908 | 2025-11-01 12:36:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 65ac4a7e-81b9-361f-92e7-f3fe2954fc95 | -12.46896 | -58.5608 | 2025-11-01 12:38:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5040c5c6-90be-3153-8e36-86f1371be743 | -11.85001 | -47.67119 | 2025-11-01 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| b5044791-bdba-37ff-a5ff-2d636aad5ce6 | -11.32235 | -51.44363 | 2025-11-01 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1576b07a-ecb9-3687-b1c9-28e6a6ecfe0e | -9.71132 | -43.37188 | 2025-11-01 12:38:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 035efa84-3799-3b5d-b747-8174c7bdc0e2 | -9.70983 | -49.35678 | 2025-11-01 12:38:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5bb285e3-816a-33cf-8cfa-953e703ae265 | -10.60063 | -46.89233 | 2025-11-01 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2637be54-be3d-37f8-a215-649d3b01fe89 | -11.57164 | -47.05504 | 2025-11-01 12:38:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a5fd36ea-ff74-3b53-834d-0f8675d44659 | -11.31295 | -51.44234 | 2025-11-01 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 7d642864-0c5c-3cfe-8741-d637d4967a11 | -9.89807 | -44.84052 | 2025-11-01 12:38:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 270.1 |
| befc0f7c-56f4-3aef-a549-21e94e5476da | -13.68333 | -56.6497 | 2025-11-01 12:38:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f0bb0db-2c1c-39d8-ab31-6ae814e89cd0 | -10.53332 | -43.28163 | 2025-11-01 12:38:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 591e34b0-e9bb-3db7-bdba-533d190787e4 | -12.11906 | -55.99974 | 2025-11-01 12:38:00 | TERRA_M-T | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a695a780-3210-32c8-b827-2cb96bb5aec4 | -10.53141 | -43.27441 | 2025-11-01 12:38:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| e6428bca-74e8-3138-8aa8-542b4da255a9 | -11.3196 | -51.46406 | 2025-11-01 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| dd7bb713-80b6-3b6d-a5fb-0ea16b41c9c0 | -14.394 | -55.78744 | 2025-11-01 12:38:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c319062c-795e-334f-bb3b-7ccf77d7d77f | -14.19875 | -57.24957 | 2025-11-01 12:38:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 35ea4007-8aaf-3b3f-9ae9-1df3dd091be7 | -9.90159 | -44.81079 | 2025-11-01 12:38:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| edcc0a00-7fa0-340c-92ad-4c987b5bf617 | -10.63102 | -52.19024 | 2025-11-01 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4edbf534-6037-336c-8f53-cb2892a961f3 | -11.57396 | -47.04853 | 2025-11-01 12:38:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| f597ec44-2323-31d7-bdce-0adf894b7da7 | -10.63234 | -52.18087 | 2025-11-01 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fbd30fab-3fd5-3f9d-be09-b76d0ddee994 | -14.39543 | -55.77794 | 2025-11-01 12:38:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| eade1d6d-d6f4-3e6f-8cd6-859439c97e9b | -9.8946 | -44.86988 | 2025-11-01 12:38:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 3b1d2c96-26d7-3c96-84b3-066a766d4989 | -14.38498 | -55.78605 | 2025-11-01 12:38:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 799fe5ec-bd28-3095-b30e-e105bdf941a6 | -11.7859 | -54.25214 | 2025-11-01 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77e0ad3a-2394-36eb-8e89-9dd659d6e182 | -12.87443 | -56.53683 | 2025-11-01 12:38:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc94d051-7db4-33d2-8ee7-087227795aa6 | -11.57138 | -47.06962 | 2025-11-01 12:38:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6ff8343a-a2e1-3741-a5f4-f73c61a0cab9 | -10.42179 | -49.36489 | 2025-11-01 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 36716e0a-b8b4-3cfa-a129-a2b4ade11e41 | -14.38641 | -55.77654 | 2025-11-01 12:38:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a662634e-993c-38a7-a15d-3aa9e3b4a36f | -12.54757 | -57.04572 | 2025-11-01 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 65e11e9b-8ff5-3c4c-8a1f-37c296e818fb | -9.42959 | -54.7096 | 2025-11-01 12:38:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a85f9dd2-2cdd-3c12-b2c6-f2d30b576786 | -10.41146 | -44.33152 | 2025-11-01 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| ca4ab988-e26e-3a26-9b03-ce86e7e61fbf | -3.6495 | -45.0939 | 2025-11-01 12:40:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3bc40bdf-80b2-3add-ae10-caca586e3436 | -17.93695 | -52.69868 | 2025-11-01 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1e216617-21bf-3119-9b49-cbba8b9a4761 | -15.03149 | -56.45583 | 2025-11-01 12:40:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 03e46868-9c89-3bf0-8cfd-074003c3e0e0 | -15.59688 | -55.83314 | 2025-11-01 12:40:00 | TERRA_M-T | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6cd47cce-227c-35c8-b8ef-a7d5c57d586d | -17.94135 | -52.7052 | 2025-11-01 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2151bde8-b002-31cf-a925-31af2f71a621 | -16.56119 | -56.23833 | 2025-11-01 12:40:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1ec60d84-72ec-3f4d-9348-776f257eae91 | -17.95222 | -52.69565 | 2025-11-01 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d3dcf8b9-0868-368e-ae04-5bca21d982db | -17.94274 | -52.6944 | 2025-11-01 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0cf46806-2640-34b7-ab2e-8ce243d14c53 | -17.96308 | -52.68618 | 2025-11-01 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c8fc2aed-86f2-3355-944f-39f08c07a76c | -29.18947 | -54.86319 | 2025-11-01 12:44:00 | TERRA_M-T | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 5.3 |
| 6a720f93-aee8-3091-a593-dbde56b2deab | -29.22939 | -51.33809 | 2025-11-01 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 90f6bb58-c36c-3466-bb19-83e3b97f786a | -33.45285 | -53.01102 | 2025-11-01 12:44:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 11.2 |


[Clique aqui para ver as próximas entradas](README32.md)
