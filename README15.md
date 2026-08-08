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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4796700-3242-3b7b-ba6f-a64a5a710fa7 | -4.36617 | -47.76844 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8c3b40a4-ebb6-33c4-a962-2fb7ed29702d | -3.8384 | -59.30053 | 2026-08-08 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9effa240-0320-3095-bc77-37316c35ddde | -4.16359 | -48.77246 | 2026-08-08 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5582549-7a4d-36e4-89e7-2394a7ca9357 | -4.69799 | -50.43864 | 2026-08-08 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68af7c4c-eb34-3f79-80f4-0c6804503e57 | -7.16661 | -44.06847 | 2026-08-08 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d972dc0d-25da-3c42-95ce-e2220afb976b | -3.06687 | -48.35954 | 2026-08-08 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70dfb0f9-3147-380e-b7d4-103b977cc184 | -5.52433 | -45.7723 | 2026-08-08 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e96029d8-90c7-3325-82e9-dd2f1c34df6e | -8.40124 | -48.48464 | 2026-08-08 04:44:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da94146e-fcbe-3add-9584-87ee80d011fc | -7.04083 | -56.51279 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712d420c-c7b1-3652-a83d-d2755fdcdf8d | -5.43615 | -44.38492 | 2026-08-08 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d635e124-735d-3233-a96c-b1140a19baf5 | -4.27258 | -48.18863 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1b33928d-a960-30ab-a482-3b5f4e2b5c90 | -1.58744 | -50.44109 | 2026-08-08 04:44:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba7be7d-f437-3afc-b674-5bfe804508a9 | -5.98025 | -52.14303 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c69495d5-d23e-3f00-95c9-c54a23e6c0aa | -6.64323 | -51.87147 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 410ae376-0035-3eb6-ba0e-cbb271a58bba | -4.64891 | -43.12717 | 2026-08-08 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0706879-9194-3c2f-93c5-a9a95b985fa5 | -6.92267 | -41.96069 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 125e4c7d-b773-319b-bc75-bc7005686d8a | -8.33305 | -46.39396 | 2026-08-08 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c75d09ac-3ff4-360e-827f-222406f433c9 | -2.69199 | -47.35706 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09c1513e-bcb9-37b2-8bd1-6b4e6a0e3820 | -4.00041 | -56.23413 | 2026-08-08 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e9c5803-4b65-368a-afe6-ba08120ba3f1 | -4.26148 | -48.19408 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3a86423c-adf5-3d8f-9d42-c312a79aca59 | -6.72261 | -58.93783 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f02b3b99-4314-34a5-9ad0-2dd3550d97e8 | -6.73069 | -58.58651 | 2026-08-08 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90fc58e9-0f95-3af3-8c57-8c8eca99299c | -2.83119 | -46.71957 | 2026-08-08 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ff929cf-83c8-3eec-af2b-e042af0377cd | -3.72866 | -49.26772 | 2026-08-08 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e00a9e4-96da-338b-9b2c-ffee78ed907f | -4.46039 | -47.91754 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1eff5e33-5b89-3400-8f9e-84c3dc59c44f | -3.73196 | -49.26824 | 2026-08-08 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e49437-d4ab-39f2-b42f-32914e3b52c0 | -2.69142 | -47.36065 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 975b09b1-e6d2-37c5-a566-de417089b45d | -6.4218 | -48.54031 | 2026-08-08 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 629cc860-58fd-339b-b724-4658617c4274 | -8.91471 | -44.24733 | 2026-08-08 04:44:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bff859ad-7a80-3b03-ac12-01244f8c2d20 | -4.45499 | -47.91684 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e06f120d-4b3e-302b-aeb6-d546d99eb893 | -6.65201 | -56.41552 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bad90ff-3233-3ce0-9783-e442ca20da6c | -3.0487 | -39.92952 | 2026-08-08 04:44:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0199502-faa5-37e9-a8c7-933cb2be43c5 | -6.70898 | -58.95259 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da1759a0-3d3b-3f70-9cad-61ec8c641e9e | -4.64706 | -43.12774 | 2026-08-08 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b3fdd6-ce5d-3b74-b4dd-402b19bc64f6 | -6.60508 | -56.36464 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e656910-09a4-3359-8094-9308a4e4482a | -8.21062 | -42.21141 | 2026-08-08 04:44:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 084e5a9a-5e03-3c50-a129-cc469acda745 | -6.64753 | -56.41453 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0960aa6-76ee-393c-8425-7cc72e47e92c | -4.46374 | -47.91806 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0973bb5-08c0-3ce4-9c01-f76c7047db81 | -5.2724 | -45.16827 | 2026-08-08 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1665ef85-a911-3bd6-897b-9c94a57dfefd | -6.88998 | -43.71553 | 2026-08-08 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7edbdb01-f65b-345a-98d3-3d2abe63313a | -6.64306 | -56.41355 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52b06f6f-5081-3cbe-9fe0-26fdf7a5782a | -8.28065 | -50.40833 | 2026-08-08 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35146676-163e-34d8-a040-24f65b942fff | -7.51279 | -47.56435 | 2026-08-08 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f8ef5d7-f995-3f2d-9df6-90ae770f5791 | -7.16184 | -44.07164 | 2026-08-08 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f5d3a5-536e-3bcb-b129-4df86419c32a | -5.52601 | -45.78602 | 2026-08-08 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5208756d-dfbc-3f3e-a0c0-d0cf2b9c5f83 | -5.87763 | -51.72356 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae2cf698-400f-370d-994e-c0ce397d3aec | -6.60584 | -56.36024 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c084def2-1a38-3216-9b5c-877efa0501c6 | -4.64458 | -43.12651 | 2026-08-08 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79dd0b5a-876a-36e3-b22f-561200c12f16 | -6.84656 | -58.97086 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a4a407c-2392-3c84-bfeb-a3c84de69183 | -6.30826 | -52.81273 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12e38b59-0a8c-3e0e-bc26-490d35069164 | -7.15818 | -44.06716 | 2026-08-08 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e347e45-9c8f-3721-8efe-eda6d618753d | -2.76934 | -49.46604 | 2026-08-08 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86fe7355-0f78-3370-86be-c84197f91468 | -6.83944 | -58.98008 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 464a82b1-4005-3c37-a1f3-0742edbd259e | -4.69742 | -50.44218 | 2026-08-08 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16460dd1-da2d-3b98-b681-57d90a08e898 | -3.85097 | -54.22084 | 2026-08-08 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d3ee397-fd4c-31f5-8808-bab92289d68f | -3.0259 | -54.52452 | 2026-08-08 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f157105a-c7a2-3c2b-8661-d9ad59983da3 | -8.2155 | -42.21204 | 2026-08-08 04:44:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 056e8a49-b26c-369b-8586-5a545a01fc91 | -2.37726 | -48.22997 | 2026-08-08 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4e9252f-d5c8-3ce1-b104-a64e930d61f0 | -3.83999 | -49.16544 | 2026-08-08 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61e1ba77-0694-39ce-b527-000f1672b424 | -2.87419 | -40.30085 | 2026-08-08 04:44:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af98f505-6cfc-3528-b775-d6699249360f | -3.2655 | -49.53051 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a3a4f1-41f8-3032-b1a8-655b40ba45cc | -4.45834 | -47.91735 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 20bdc9d6-e05a-3c20-808e-3da1e80e3268 | -6.72009 | -48.12061 | 2026-08-08 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baa053a1-1303-3a49-98eb-d8aead7b2fca | -6.42514 | -48.54084 | 2026-08-08 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 575bce47-9ade-3d99-a83c-545977ca9c8b | -3.95385 | -48.12075 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc5c0a8d-51d6-3536-93bc-24a1bc82af42 | -3.95663 | -48.12477 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90eed536-59c7-35b3-8e90-1ca64d5441d0 | -6.64953 | -56.41318 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9ce7ea4-e0e4-350b-8187-26dcb6d22ca9 | -7.84883 | -56.58781 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e19ba70-6855-3d99-8c10-3d4e147425c6 | -2.93986 | -54.15442 | 2026-08-08 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2ad6598-b159-3f7b-91db-f983ff022506 | -6.0251 | -51.33253 | 2026-08-08 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138ca889-b493-39bc-a8f7-9543fb9da68b | -5.88047 | -51.72794 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d904a82-6e55-39bc-9acc-5dc66fdcac25 | -6.85634 | -46.00301 | 2026-08-08 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabe5306-0c68-30df-99fd-cc08c2591629 | -3.83772 | -59.30454 | 2026-08-08 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b17ae83-bea0-30dc-a88e-fd3e220d1e36 | -5.52669 | -45.78163 | 2026-08-08 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a6cf627-9a87-32af-9e7e-1863dd4dedcf | -6.72403 | -48.11751 | 2026-08-08 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03210fd3-7814-3923-a056-380e1ce69c0a | -5.42555 | -43.43081 | 2026-08-08 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9d6800a-513d-308f-af9d-83db9b9b9c53 | -4.3656 | -47.77201 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d44631d-82dc-3cce-91c1-9230d457c6e2 | -7.77398 | -49.4877 | 2026-08-08 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3af81a70-1a8b-300b-accd-f3c986482359 | -6.60135 | -56.35943 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0e79a1b-36e9-3814-baa0-d2229b08566d | -8.32632 | -46.3883 | 2026-08-08 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 636d421b-bb8b-388c-aa0d-bd52fe9ccb27 | -6.72065 | -48.11697 | 2026-08-08 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0715a7ce-f82a-3fc0-a2de-a36a1a721373 | -2.0861 | -54.44371 | 2026-08-08 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d889398-a22e-3785-9dbe-ca8da905beb0 | -2.97813 | -51.68684 | 2026-08-08 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26866220-de73-368a-b92d-eddb3ba8d6be | -3.95718 | -48.12127 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 725d8c35-54ce-3d7e-b83e-1ccd1fee303e | -2.75165 | -49.47036 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a3ec974-eeae-3dde-8346-0b159ed1252a | -6.89333 | -59.89412 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4bdfe6-ad65-3207-b4ba-07ddbfaed8c0 | -5.44927 | -45.14518 | 2026-08-08 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1f06730-9cec-30c9-9cd6-65da57a086b5 | -7.84804 | -56.59229 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4c52dae-7d92-3e37-acb0-f303d5014cb7 | -6.70778 | -58.95932 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51131f0e-bad3-3e5c-9ee0-60b9b675d9ab | -3.19279 | -50.28915 | 2026-08-08 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b847f963-2a8a-37b4-9425-bb56ada079d4 | -8.33373 | -46.38943 | 2026-08-08 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a178e59-4541-327f-869b-9af73a40c6a8 | -5.42616 | -43.42673 | 2026-08-08 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5006123e-a275-3f70-8551-a8822f504d5e | -6.65032 | -56.40868 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41ec92b0-daba-38b7-99a1-c5324c66200f | -4.64272 | -43.1271 | 2026-08-08 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8279b0-cf9d-3dd1-a68c-a7cde0e1fd03 | -6.73125 | -58.58343 | 2026-08-08 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61bf1db-6e62-37c2-86c0-0e99b04e5925 | -2.75774 | -49.47488 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cc74be4-c3b8-3a08-84d0-0ef27873e522 | -6.97854 | -41.4935 | 2026-08-08 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2bf085e-23d6-3efb-bf5e-c5f71b5de289 | -6.98394 | -42.90693 | 2026-08-08 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b4a70d08-770a-3df2-8cd6-add260e3c3a8 | -6.33756 | -46.05096 | 2026-08-08 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fda389a9-394c-3d98-8d2d-96b48fcbf2f2 | -6.97363 | -41.49195 | 2026-08-08 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
