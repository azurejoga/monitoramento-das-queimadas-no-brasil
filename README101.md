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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e48daff-e0b5-3442-b89a-4ab3b92cb887 | -7.7531 | -49.21508 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05957d1c-7019-3751-8959-36f8d827d520 | -7.74978 | -49.21456 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7fb1283-f93d-3e26-828e-6320946193e9 | -7.74924 | -49.21803 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee18c6fa-27e4-34f0-be2a-c391a63cd1bc | -7.74593 | -49.21751 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea4d2f7b-9f4b-307e-b1bf-2ff97095b9a0 | -7.74539 | -49.22099 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2566975-ce00-3682-8e1f-8949bbcf7047 | -7.74261 | -49.21699 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed3caa44-7059-310c-a856-b06675f617ad | -7.74207 | -49.22047 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa0e0dfa-7a3d-3649-bdb6-74d0b69be117 | -7.74152 | -49.22395 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095eee02-0234-3352-a58a-8c505c9041fc | -7.7393 | -49.21647 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3c9e85b-e048-3fbf-9b84-18af42271369 | -7.73876 | -49.21995 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7e030cf-43b0-3f63-91f0-22e95dd5a39f | -7.73599 | -49.21596 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29fc4936-3eea-30ec-ad99-099d54ade2ed | -7.73544 | -49.21943 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a471cfe1-e1ae-32da-9c3a-ffddba7d4c3e | -7.7349 | -49.22291 | 2024-10-05 04:38:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d23d56-f72f-38f8-9031-e9e1cc516a95 | -7.36884 | -49.6095 | 2024-10-05 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c28159ee-c88c-3008-8dc0-a0266680d426 | -7.36829 | -49.61296 | 2024-10-05 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 903c7006-4573-360d-8368-48bc78dc05e4 | -7.30819 | -49.25911 | 2024-10-05 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 147e248d-9681-34c5-990d-c4ca3b3e3b01 | -7.30488 | -49.25859 | 2024-10-05 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc44ad97-dfff-3dba-944c-3db9f64ba5a2 | -6.97959 | -49.42757 | 2024-10-05 04:38:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb8120f-1e13-3242-8092-b72168def114 | -6.80381 | -49.16209 | 2024-10-05 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e20fdc7-cc13-3dc2-94d3-6a73ef28312d | -6.77823 | -48.95529 | 2024-10-05 04:38:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd00c5bf-36e7-3661-898b-121fb3bb0195 | -8.17681 | -49.76207 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca11c1ad-6e17-306c-b5ec-6a1a1059be07 | -8.10995 | -49.51755 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 367c1d3a-4345-30fd-a63c-2d35e2770920 | -8.10665 | -49.51702 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1014118-1d7d-3ca6-b6ac-0dd1faf820c6 | -8.08023 | -49.53421 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89bf45cd-4310-3ae9-9074-aa7103ab7d51 | -7.92964 | -49.86521 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aed10506-8a6e-3251-917c-7ee64b4ce787 | -7.92909 | -49.86868 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ca7683a-4faa-3ccb-8a95-67cdaf9e9c8c | -7.92855 | -49.87214 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd248f35-07a7-3b34-b270-2e45bb7787ae | -7.9247 | -49.87508 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24d5fcfa-915f-3c49-a11b-ee6b3c37c401 | -7.92248 | -49.86763 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f253b2-045c-3257-b25c-d4baa0dd2daa | -7.92194 | -49.87109 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c4fbea2-9504-3889-a327-fc763f64c990 | -7.91917 | -49.8671 | 2024-10-05 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 712e5159-5fdc-39a9-9ed4-88517a3e95ec | -9.00734 | -49.81615 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcd51fbe-d660-3bec-9eec-777d68b0eb87 | -8.98365 | -49.81595 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5684f137-ffaa-3e7e-81b2-f75a366a12ab | -8.9831 | -49.81943 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffcb95c5-e4d9-34ee-ace0-89eada5bcf8c | -8.98034 | -49.81543 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6fe99bcc-770a-3a71-b76d-7639929ed1f5 | -8.97594 | -49.82186 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b35f6e82-32ed-3c71-bb17-f2996065a5d8 | -8.97318 | -49.81786 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8a7dde9-bfc5-34db-9d8b-1eecbcfe37bf | -8.96987 | -49.81733 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0022e2ef-7a87-3323-a757-b6c7d4fb34d0 | -8.94041 | -49.74493 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4de04639-c257-38df-8557-38281f1f01ff | -8.9149 | -49.66963 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f533e318-3152-3fd1-8a96-ac9d36af009c | -8.91436 | -49.67311 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70e888b4-f0c2-3626-aadb-7f17dce5e00e | -8.91381 | -49.67659 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 939369b8-9da4-3b3e-9989-1f873c025219 | -8.91327 | -49.68007 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5d7f395-6596-35eb-953f-b154d5405318 | -8.91105 | -49.67258 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af459515-777a-37cf-930f-d6f1eae2d722 | -8.91051 | -49.67606 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ecd82da-fe8e-35e1-8322-df9c4599a619 | -8.90665 | -49.67902 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cc6ca4f-744f-34b4-ae4a-4f4cd4cdc81d | -8.89061 | -49.65152 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6620b5c-5942-3635-b32f-bb7f87152712 | -8.88458 | -49.6684 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae0a7a38-d26e-3b3b-a5e1-b50eab015f18 | -8.883 | -49.70023 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545155f2-3100-359b-89bd-e81b878ed8ef | -8.87915 | -49.70319 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92bca8a5-53fb-30e5-ad55-28724f0fd96f | -8.87742 | -49.67083 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04851bee-8a68-31c1-beff-bc22711b2f04 | -8.85736 | -49.6673 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05bb5d7c-0b29-3950-944f-b96e49e245ca | -8.79834 | -49.95711 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54de8d72-e4b4-378a-98f0-17844ebb7e9c | -8.7978 | -49.96058 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0e3635a-1b87-3684-9197-b4996aa9fab1 | -8.79449 | -49.96005 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9b0f749-d926-357a-99d4-8c25026d2fc1 | -8.79064 | -49.96301 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5255b252-f568-3164-aa35-e06da39ad8bd | -8.79009 | -49.96648 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 724b2dd7-9024-3b7d-8fa9-5ab7f3e92951 | -8.78733 | -49.96248 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cee42fe-0181-368b-bd37-21fe31ab72bd | -8.78624 | -49.96943 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5615a8d7-753a-3c22-8627-0918f978dd22 | -8.78621 | -49.94806 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2d592c5-b186-3363-a3b0-50a48c7c15ea | -8.78402 | -49.96195 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7cbe3ce-a515-3cb5-8a53-5c4480d96021 | -8.78345 | -49.94406 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 209ca921-5fac-3fce-93f3-723452fa9182 | -8.78235 | -49.951 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80cb62f7-6ec0-3b01-965a-73201caf7415 | -8.78181 | -49.95448 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11513995-9e41-394d-861f-1190f9981731 | -9.58372 | -50.08281 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7666f2c-0f3d-363e-9c98-c6a11bc692d0 | -8.78071 | -49.96143 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ae796ee-49cd-32bd-b9af-1f9a4dc6ddf7 | -8.78017 | -49.9649 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5039aa0e-1274-3a5c-b80a-123fc5308b20 | -8.77962 | -49.96837 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d54d840-7081-3f5c-9e06-77082109df5a | -8.77738 | -49.93953 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b7baddb-0c41-34f7-95b9-ef0e28f45b07 | -8.77632 | -49.96785 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f3b4bf2-fa19-31eb-8cb9-a4093cf6d615 | -8.77465 | -49.9569 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dc93d92-6502-3435-a57a-521c056a00cd | -8.7741 | -49.96038 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 922f3632-c0c9-30e8-a492-7d1aa225b814 | -8.77353 | -49.94248 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857b8894-1882-38a4-9a46-5da53daa533c | -8.77243 | -49.94943 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 597e4fcb-313f-3b56-a5fa-521b8c59c251 | -8.77189 | -49.9529 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb8be607-a5de-36d6-890b-ff68df5c9009 | -8.76913 | -49.9489 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 210735a0-5408-30c6-89db-e275191330a6 | -8.76858 | -49.95238 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b8fc843-a4ce-3df2-b782-84d61e257c50 | -8.76582 | -49.94838 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be41d5e0-b31d-3bb9-a420-38e51c20925f | -8.76528 | -49.95185 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1ed51d4d-a5ca-3dd8-873f-15f53768769f | -8.65222 | -49.10927 | 2024-10-05 04:38:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38a4b37a-ba4a-3bdc-92fc-0c0799616472 | -8.64943 | -49.10524 | 2024-10-05 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de9c1298-445d-37b3-88a8-3367c51ffbf8 | -8.64889 | -49.10875 | 2024-10-05 04:38:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37cfb797-4025-3919-b17a-482809c7c858 | -8.64333 | -49.10068 | 2024-10-05 04:38:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95e478c4-9695-34a7-b840-6fcefc1e9067 | -8.64054 | -49.09665 | 2024-10-05 04:38:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77e2ea20-8b54-3a5d-8004-6d6eeff0ef7f | -8.63742 | -50.05253 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09dd18d9-3550-338e-8359-037084b12ca4 | -8.6138 | -49.09619 | 2024-10-05 04:38:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e106aa2-8102-3a21-8599-ed68a857f9f3 | -8.61233 | -49.47551 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 127ca033-c087-3d7d-8b82-4cc4fc68a41b | -8.54178 | -50.09808 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 517501b5-9304-3248-9693-851bd4d3466c | -8.54093 | -49.64957 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02af8b96-2c0a-3fdc-8bdd-8a28c727b2af | -8.53984 | -49.65652 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9550813-619c-3c83-aeab-04084bd5aa58 | -8.98696 | -49.81647 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5362b00-1f18-38ba-bc50-5755697f1752 | -8.98641 | -49.81996 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e29fee90-3c99-3147-a915-05d63cf98b58 | -8.98256 | -49.82291 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e932843-8309-3364-b39f-96008ab6074f | -8.9798 | -49.81891 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe0dc595-51cf-313a-b418-6a5d38f867de | -8.97925 | -49.82239 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ea43d01-f6a5-3972-a85c-984c798126a3 | -8.97703 | -49.81491 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 15e68135-487f-3d19-af9b-9460d92a289c | -8.97649 | -49.81838 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56be4b18-b48e-3a40-8686-aab232dbf2c1 | -8.96326 | -49.81628 | 2024-10-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc0e920e-01eb-3af0-beaa-34248181fa4c | -8.91767 | -49.67363 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c14089df-4fdc-3fa9-a53b-461716ca2615 | -8.9072 | -49.67554 | 2024-10-05 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README102.md)
