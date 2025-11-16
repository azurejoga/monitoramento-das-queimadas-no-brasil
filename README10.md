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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13e353e6-01c8-3be4-9c96-328cb9253c53 | -2.5238 | -47.8332 | 2025-11-16 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9f4f12c5-bd95-372f-858e-9fc7b1ad2ddc | -4.7027 | -46.3176 | 2025-11-16 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 94e09100-a8d1-3373-8a4a-c66f23b84182 | -4.7209 | -46.3832 | 2025-11-16 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 02a059eb-770d-3145-88cc-215f75ea2851 | -4.4433 | -43.4027 | 2025-11-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| a3394ed5-77f3-39ac-80f3-2371717d65f6 | -4.8432 | -47.5428 | 2025-11-16 00:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 16b5cc37-a4fd-390f-af30-db192c5f602d | -12.0191 | -49.2877 | 2025-11-16 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a6f132a0-e68c-304d-bf79-4168b5c19e16 | -4.4246 | -43.4038 | 2025-11-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| bbd46d79-e13a-332e-b01a-11c0e4b15560 | -12.0004 | -49.2683 | 2025-11-16 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 4cf709da-3869-351c-9931-0dfe60362763 | -4.6841 | -46.3186 | 2025-11-16 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 541641c0-6aa8-374e-b2be-e4c4f48fa43d | -11.4136 | -43.32 | 2025-11-16 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e25b7c77-aab6-3109-976a-e7c27de9b0e4 | -12.0195 | -49.2659 | 2025-11-16 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0786d178-2dbe-3d9e-980d-d16553930cab | -12.0 | -49.2901 | 2025-11-16 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| cb67c732-fa80-3594-9ff9-e7d54e545dca | -2.5238 | -47.8332 | 2025-11-16 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 141a8e0c-d36e-3a92-8564-56e8dc25b0d1 | -3.6038 | -43.285 | 2025-11-16 00:40:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 06fc8ba1-86ee-3877-84a7-e49160039453 | -12.6864 | -47.1642 | 2025-11-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2a740be6-6498-3be8-b933-a61ad29bcd72 | -4.6841 | -46.3186 | 2025-11-16 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 63a07e88-7970-3378-97c6-1a3520129f5b | -12.6672 | -47.167 | 2025-11-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8adf9c26-abd8-3475-a851-19a23d7d01e9 | -4.7395 | -46.3821 | 2025-11-16 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| dcdf44cc-f823-37ca-8ecf-a70911450b2b | -3.1473 | -45.0699 | 2025-11-16 00:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b3245cca-e553-39c3-b97e-d3e4ad023f16 | -8.0513 | -43.1001 | 2025-11-16 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 28d64324-0eab-330f-8e3a-13e438eac924 | -2.5238 | -47.8115 | 2025-11-16 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 245.4 |
| 0cee6828-9454-3e15-be4b-bd4c4243fcf8 | -12.0195 | -49.2659 | 2025-11-16 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ab11f0c6-16cb-3e53-88f5-1625b01d3c25 | -4.7027 | -46.3176 | 2025-11-16 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 53ec91f5-2c77-31de-a4b5-1cb3fdcb9355 | -6.7013 | -40.7962 | 2025-11-16 00:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| a33c9bd8-7a24-3002-8275-c81244d5ae7f | -3.2757 | -45.4477 | 2025-11-16 00:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 676c0189-9d07-3c7a-aa42-98c256eeb80f | -16.5637 | -47.6042 | 2025-11-16 00:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 35f1377a-e938-33a4-b6a3-0172bf2f52ec | -2.5053 | -47.812 | 2025-11-16 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b5cd1117-fc39-33cc-b667-1f44f2a1b3c8 | -12.0191 | -49.2877 | 2025-11-16 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 307c5905-9335-391a-a032-c90fb83b018f | -3.2554 | -45.7846 | 2025-11-16 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5634810a-f48e-38b6-b3bb-1cc580d07fdd | -12.2047 | -49.6121 | 2025-11-16 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| b13349b9-708c-3cef-8674-f1d8ca7ec793 | -8.0703 | -43.0981 | 2025-11-16 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 209.4 |
| 4cadb7d6-5304-3c40-8fde-ea73ca2b97b5 | -12.6553 | -46.7633 | 2025-11-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b6d09231-dcd1-33f7-b00a-5874d5e51908 | -12.6557 | -46.7407 | 2025-11-16 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| e68d9fc5-c2b1-3657-a2c1-968c1935beae | -1.9886 | -47.3465 | 2025-11-16 00:40:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 074bc791-f7db-3a3a-b0a9-407178a34b1a | -14.6094 | -46.6103 | 2025-11-16 00:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| cd6dd2c2-ec4f-315a-b43f-c8235593a5a0 | -12.0004 | -49.2683 | 2025-11-16 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| c1d9a64a-d06d-342b-bdc9-30abf4068a7c | -12.0 | -49.2901 | 2025-11-16 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c3a6fcb3-dc52-3b8e-b855-e1400fe693f7 | -3.1472 | -45.0924 | 2025-11-16 00:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cd32b73a-980c-3386-9762-6ca959b27897 | -8.0706 | -43.0745 | 2025-11-16 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| d7629df4-0851-37e8-acba-4a9548f182bd | -2.8925 | -53.2842 | 2025-11-16 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5f62dcd6-c52e-3f64-9dc4-743f659b3dbe | -4.7027 | -46.3176 | 2025-11-16 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ceab03db-2a66-389d-986d-c8fc3eb61d99 | -2.8925 | -53.2842 | 2025-11-16 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f6c57ed9-5346-3ffe-b113-d6a5cd2ec27f | -3.8288 | -49.8012 | 2025-11-16 00:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| dc2348c0-c231-3ab6-b8ff-ffeb383d61b2 | -4.7395 | -46.3821 | 2025-11-16 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 12d69089-32ff-387d-89a7-61380b75d9d2 | -12.6864 | -47.1642 | 2025-11-16 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f83a4589-6e85-3122-bc60-825750516ac4 | -8.0513 | -43.1001 | 2025-11-16 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 3b190750-f745-3028-a279-dac6c666e0e8 | -3.1473 | -45.0699 | 2025-11-16 00:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3a74674a-ae9c-3dac-9469-373e870f6f1c | -2.5238 | -47.8115 | 2025-11-16 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 2cae5a53-acb6-3dbe-8cfa-ce9e8d168174 | -3.3276 | -50.2825 | 2025-11-16 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 62ed8e47-384b-36e5-b9a3-c098015b1e5b | -6.7013 | -40.7962 | 2025-11-16 00:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 99b4c81e-81de-312d-87d4-73534a1b6951 | -12.0195 | -49.2659 | 2025-11-16 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 604c6034-c4b7-344b-990b-fad2c981a9a8 | -12.2047 | -49.6121 | 2025-11-16 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6d472c15-65cc-3896-8e9a-f17dcf1bb62b | -12.0191 | -49.2877 | 2025-11-16 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ab6ac9f7-70dc-36f6-b71c-c562af2bce21 | -12.0004 | -49.2683 | 2025-11-16 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 68bd9536-a5a7-3be0-a0e0-5ab6d136d16f | -3.6038 | -43.285 | 2025-11-16 00:50:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 994b3cda-8268-3570-9927-906f44ddf730 | -16.5637 | -47.6042 | 2025-11-16 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d4102fe7-dda1-39e1-b635-957c8d04fdec | -8.0703 | -43.0981 | 2025-11-16 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 187.2 |
| df7083a9-2c82-3ca3-9f40-d7a4737cb5f9 | -2.5238 | -47.8332 | 2025-11-16 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 62048e55-d033-32f1-ad29-248ac3c15e8d | -2.5053 | -47.812 | 2025-11-16 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| dbbfe59b-2690-3a5d-8932-bf532973299d | -1.9886 | -47.3465 | 2025-11-16 00:50:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 730f6962-3551-3e81-a406-431f464b22d3 | -12.0 | -49.2901 | 2025-11-16 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 2cb7f10d-82b4-39ad-a4da-abf590fd6b74 | -12.6557 | -46.7407 | 2025-11-16 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6bb82124-d566-3362-b43b-eb752494d2bb | -12.6672 | -47.167 | 2025-11-16 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0edea1d7-e050-3a92-85a1-3263ab096f77 | -4.6841 | -46.3186 | 2025-11-16 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c97f1b8-ca54-3fa5-9bb3-2912482402c9 | -8.1092 | -46.0363 | 2025-11-16 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d45521c7-ff15-387f-ac15-e572c9e78c06 | -3.3294 | -45.8487 | 2025-11-16 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8f0a77d7-ca4d-3222-b94e-6a897eb98f5c | -3.2554 | -45.7846 | 2025-11-16 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| aa2c6062-1365-3c05-b5b9-3b22c08676b5 | -7.252 | -48.018799 | 2025-11-16 00:52:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 063468f1-5209-3d47-a043-c163971be97c | 4.0247 | -59.659199 | 2025-11-16 00:52:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a2a4b0ca-2e4c-384f-9de9-53bf66046766 | -2.7936 | -52.965401 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc96e60a-b487-3b6f-b4e9-e51be410b7b3 | -3.823 | -49.812401 | 2025-11-16 00:52:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4380950e-13f9-3b5f-8696-d5a152db3cb3 | -3.3186 | -50.261902 | 2025-11-16 00:52:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b46d08-0b1c-3506-aca0-9a5dd3d57caa | -5.1196 | -55.9566 | 2025-11-16 00:52:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11f1982-52e3-36a0-80f0-b8ecc971a9e5 | -3.8271 | -49.787201 | 2025-11-16 00:52:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b794ab4-051a-3b77-98af-2ae136b08f8c | -2.7902 | -52.951 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90c67495-e069-3072-9ebf-66305c04ac16 | -2.5758 | -51.823101 | 2025-11-16 00:52:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73d75094-0e71-3f3e-9474-55157ace2dfe | -3.3238 | -50.283501 | 2025-11-16 00:52:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 724c0c7b-3a69-3e20-9118-4a982addb47d | -1.1838 | -53.716 | 2025-11-16 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f93ded6-ab57-3c27-9f4d-7fb089482ad6 | -16.5473 | -47.581402 | 2025-11-16 00:52:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 907a8b8b-960d-3215-8501-c148666789d1 | -2.5085 | -47.792 | 2025-11-16 00:52:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b97ee8-2f43-30bc-9e06-64be1c5dd5a8 | -7.7058 | -47.276402 | 2025-11-16 00:52:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce362c7e-bd0c-3fec-a649-6d285ed51c1b | -2.8786 | -53.283501 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84967403-0436-3c53-b50e-eef363050de6 | -2.5069 | -47.827202 | 2025-11-16 00:52:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01aedce-9c24-3db3-87fb-564005f467a3 | -3.8175 | -49.789501 | 2025-11-16 00:52:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afdd67c8-a0de-3687-b65f-a3f405fb25f5 | -2.8851 | -53.2677 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f594668-4c6f-31db-af45-f8f6ed472c4f | -2.4989 | -47.7943 | 2025-11-16 00:52:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e6e0d8-ad5d-362a-be91-9e0510422c61 | -5.1216 | -55.965199 | 2025-11-16 00:52:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8016ead-2ed8-377a-90cf-33440af3ff6c | -16.562201 | -47.598301 | 2025-11-16 00:52:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2508d4b1-6117-3e6c-9c0d-042cf30e28de | -16.5569 | -47.578602 | 2025-11-16 00:52:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63c87664-0ba3-32be-8c12-20a48c18d99d | -2.5165 | -47.824902 | 2025-11-16 00:52:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a56062d1-0121-306b-b7a1-22d5b1a085c8 | -7.2616 | -48.0163 | 2025-11-16 00:52:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2bc433d-0e3e-35e9-908a-cbad3009a72c | -2.8754 | -53.269901 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18731abb-fcb3-331e-960d-92f15554b937 | -3.8327 | -49.810101 | 2025-11-16 00:52:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39922acc-c38d-3c9a-b969-6415ce255a05 | -9.7029 | -48.8899 | 2025-11-16 00:52:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afcb40f3-d556-3a45-8689-41bb859b3a21 | -16.552601 | -47.601101 | 2025-11-16 00:52:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0c7864-86b4-372b-8891-8147ec6277c5 | -2.8883 | -53.2813 | 2025-11-16 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e48a074-c0a2-3414-bf6f-b4c00c4a1b28 | -14.649 | -46.5807 | 2025-11-16 01:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d69a84e6-a6d2-3988-8d5c-bc67cd82f7df | -1.9886 | -47.3465 | 2025-11-16 01:00:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 31b4afe8-af79-3b85-a04a-ea314295b34b | -8.0703 | -43.0981 | 2025-11-16 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| f9e05cb1-eb8b-3595-9533-1ded7ed1f5fc | -12.0004 | -49.2683 | 2025-11-16 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |


[Clique aqui para ver as próximas entradas](README11.md)
