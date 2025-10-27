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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96e46974-cc31-35a5-aa25-9a8ef46753fa | -5.60764 | -47.09504 | 2025-10-27 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 40b55c37-5c23-34b0-901c-52b597a82c53 | -8.52785 | -47.20866 | 2025-10-27 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 23b1fd9f-6528-30c3-8013-fcfef78c4276 | -9.47444 | -40.38704 | 2025-10-27 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e3df309e-74b1-37a0-9c8a-c6e99389e268 | -6.88059 | -43.5742 | 2025-10-27 00:13:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d81224b0-e7d9-3ff0-876c-317a882f6a14 | -7.84332 | -46.47619 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4f51c23a-dbca-3cd3-af38-eebfb23a1b65 | -5.65942 | -41.11104 | 2025-10-27 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e7a7aac3-a4d1-3315-9877-e8692fbcb40e | -8.21113 | -43.79842 | 2025-10-27 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| c522dce1-22bb-35ac-890a-98529b5fa5f8 | -7.0689 | -46.75078 | 2025-10-27 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cdaff280-1856-30b9-9f2c-4f3a6cf964f2 | -6.64174 | -44.63441 | 2025-10-27 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 006b21d3-b842-3557-94cc-33fa57ad931f | -7.77023 | -45.40221 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 77a93fcf-4399-30d6-9b23-e7ad44f3d838 | -5.4852 | -43.09329 | 2025-10-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f9503b2-5a70-3ffb-b35c-da7f6f6ed988 | -4.47207 | -43.41331 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 1fba5cfd-bb8c-3efb-8f63-87834ecad65a | -10.55865 | -45.05101 | 2025-10-27 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9dc0b73c-c21e-3925-a4b9-f15f687c244e | -8.88531 | -47.99949 | 2025-10-27 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| fa2ca662-8213-3219-9bd6-6187b3c3506f | -6.08743 | -42.15209 | 2025-10-27 00:13:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 90909651-f06a-3be3-9318-6aa01a2a4380 | -6.16977 | -44.21785 | 2025-10-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7f041ad-fa47-38c5-b41f-ef72d0e67eca | -9.13049 | -45.85603 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8d70357f-4f41-313e-a2b8-423cc5564bd6 | -4.85835 | -46.73587 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b66b4ee6-f41f-3f0f-914d-11a0ff4ff386 | -5.61874 | -42.66984 | 2025-10-27 00:13:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| aee79698-fb19-3b9d-8519-4c8cab1d97bb | -5.27944 | -47.12906 | 2025-10-27 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e36d5d99-528e-3798-884a-4841b15b5bc7 | -5.76589 | -45.56383 | 2025-10-27 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 400360e8-288e-37c5-933e-9eebf39dd152 | -6.25711 | -41.84196 | 2025-10-27 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 2c445c1e-4b93-30e6-beb5-756723d7c38f | -5.54996 | -43.94232 | 2025-10-27 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23a1630a-158f-39cf-9323-b8d843949a8e | -5.14113 | -41.19661 | 2025-10-27 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 46caf15b-0b03-38ca-9378-1c8a9660bacf | -7.33784 | -42.44738 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ce7a0e59-b95c-3240-aa0b-9c7c88bbbf2c | -7.24614 | -46.96178 | 2025-10-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1329ffdf-f349-36cd-be1e-7b942b665e66 | -4.95246 | -44.88198 | 2025-10-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d786bded-c34d-3c58-bc68-36ce578ac3aa | -7.84065 | -46.45669 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ab8d7a5f-2a11-3e11-8703-119790ec1038 | -6.15489 | -43.13303 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1d098c4b-2545-3ff9-82de-31a6d1b69084 | -7.84871 | -46.45919 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02fcf9e8-3c1e-3bde-9824-15055296d759 | -8.51934 | -44.54496 | 2025-10-27 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1bedac4f-611b-3be9-91d8-2eee068aea86 | -7.80519 | -45.38222 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 516ce1f3-62e2-3727-b268-daff176d72a3 | -7.06094 | -46.76188 | 2025-10-27 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 45fe6d15-2495-3146-89bc-1d87bcb77f87 | -9.99414 | -47.18039 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b8ac103a-bf14-36f4-9bbf-4c2b0174383c | -5.57279 | -46.43668 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2c66df5b-86a3-3a7f-a75d-250c304bf1e8 | -9.58314 | -45.19058 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6a8c2843-3826-3c60-9e3b-2283a4f84f17 | -10.17105 | -49.3116 | 2025-10-27 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d9ae2e7f-701d-31dd-beb1-231575746eff | -8.9659 | -47.19593 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9c3ea5cb-58cc-3cb9-a15a-6a3ea413478d | -9.2669 | -45.77683 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f88e3707-685c-3c5f-9f72-af985d857f38 | -7.85974 | -45.38375 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 27f40074-618b-3947-b067-283006630e38 | -5.64098 | -47.62477 | 2025-10-27 00:13:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4ad18aba-385d-3baa-8db6-6070b3f289f7 | -10.21907 | -52.67246 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| ce3bb581-48ca-3469-86df-0593e04eac6d | -4.26327 | -40.69441 | 2025-10-27 00:13:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a7f2a593-c717-3a6d-a862-3c35af635697 | -7.43068 | -41.88268 | 2025-10-27 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| c30494c4-a66c-3937-8519-2a51ec0c1537 | -8.31781 | -46.17812 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a6ffa36e-436a-3f8d-b365-9328b4ed05bd | -9.261 | -45.59684 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ebf6f63-7881-39ef-8926-853ebb47f07e | -4.45354 | -43.41602 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e7a22f5f-72d0-36c0-b882-7b42b387078f | -6.6432 | -44.57997 | 2025-10-27 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63fe14dd-51eb-36b7-9318-b960e1716d3b | -6.87381 | -45.17497 | 2025-10-27 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 58d2ec2a-a71a-3d3d-b267-29fe794bc9d8 | -7.44043 | -41.88125 | 2025-10-27 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f4d500a6-24ee-30e8-9b7c-c294b465a31f | -7.77787 | -45.39192 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e40c2fd-757a-3cc9-8c81-5761a98324cb | -7.94239 | -44.84184 | 2025-10-27 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4281fc93-4d92-373e-a64c-211c5f9e7258 | -4.23533 | -42.22697 | 2025-10-27 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 17342b4f-a92d-3e63-99ab-2c6f6817eb7b | -7.5914 | -43.5819 | 2025-10-27 00:13:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b42e783c-b88b-3b7a-a3de-63cb0daa87d9 | -6.78036 | -41.00002 | 2025-10-27 00:13:00 | TERRA_M-M | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| c03c44d2-0586-3297-a87c-e89910ab4212 | -7.83669 | -46.42767 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff493466-dc43-398f-b6f9-2e4c5faeaf26 | -7.07021 | -46.76059 | 2025-10-27 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4d233ad5-6793-398c-b239-2142b8bb35d1 | -5.43243 | -46.42141 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc909eea-bc1f-3e0e-81ee-51c4d6bd7f0a | -5.03746 | -41.1917 | 2025-10-27 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8255fb16-9fed-30ed-b865-21e5d72d5254 | -10.85689 | -47.93858 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2da882e1-adc1-39ae-8b59-8f4865c83371 | -8.5287 | -45.56086 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66606bdf-6d97-3344-87d6-8e1c3c79ed7a | -7.82879 | -46.43845 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| a828eda5-72f1-372e-b544-4b2307e969f2 | -7.53687 | -46.25441 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a5a5b1c-3223-32fd-bce4-22e5d1d00dc3 | -7.00155 | -47.00818 | 2025-10-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d6629eb-8602-3155-9bc2-c5740c54311e | -8.69735 | -44.43484 | 2025-10-27 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8d800fc1-372e-3ad9-aa00-59223e5bb5cb | -5.33726 | -44.725 | 2025-10-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddcf0487-0438-3811-bec2-f77535148cb0 | -6.38468 | -45.77059 | 2025-10-27 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90f91106-14bb-33a7-8f8d-c110fd4d9707 | -7.78427 | -45.37263 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 35f40a7e-e41d-3f3c-8c14-3279cff1610b | -9.1214 | -45.85718 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f7914b76-fb1e-3b93-815d-968e1f537f77 | -10.77359 | -43.86753 | 2025-10-27 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe186e9e-8ebe-3ccf-8934-258e3cb8ce5c | -6.01484 | -48.20939 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ccc2a4ce-339f-3374-949c-56f4551a6b81 | -6.88961 | -43.57289 | 2025-10-27 00:13:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| f1acfb7c-30de-3280-87b6-b932898c9c7e | -5.56029 | -46.34476 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c339bb07-09bd-31d2-9b62-761e65974b38 | -8.21238 | -43.80742 | 2025-10-27 00:13:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 48e55eaf-ee0a-3d0c-be5e-dce2dea189c4 | -8.02922 | -46.76973 | 2025-10-27 00:13:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9044e0b5-88ad-3727-8d96-42ce7435c169 | -5.65982 | -48.45748 | 2025-10-27 00:13:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c0eda7e-c3d8-309f-9645-260b6db9010f | -5.64698 | -41.09982 | 2025-10-27 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5fc556e8-b6af-3a9f-ac1a-2b82dc0ca6a6 | -5.59971 | -47.10621 | 2025-10-27 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f64f1d42-9fc9-3ca4-ab4d-63fd1e80f131 | -8.96449 | -47.1851 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 04705e34-1990-3bc0-9ab4-2f111f615bd8 | -9.4645 | -47.73888 | 2025-10-27 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| f388df2d-ec8d-321d-8f44-4551605a4a1c | -6.85176 | -46.29611 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 643ed07d-29ee-3fd1-a4f9-6c37c67efb38 | -8.02787 | -46.75964 | 2025-10-27 00:13:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dd6b456d-6561-31e3-8c8f-5ffd3446c4f4 | -6.88903 | -45.15473 | 2025-10-27 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f57f9e83-fc80-3530-ba3f-e927f6755cd8 | -7.84464 | -46.4859 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c1025332-9d01-333c-8468-a2a83362bc02 | -5.57153 | -46.42744 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 01aee776-eb7c-3e3a-ac98-a90d2faa34ed | -7.86854 | -45.71469 | 2025-10-27 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f5be899e-0812-36a4-8515-895d9f509614 | -4.84929 | -46.73723 | 2025-10-27 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec05b153-a245-3b9a-be73-6dc7329a1f68 | -8.30999 | -46.18907 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d452cb6-11ce-3698-94eb-2ee840cec2ee | -6.25549 | -41.83065 | 2025-10-27 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9ea7f029-1423-310c-b99c-423200478dcb | -9.82644 | -46.92553 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1126fa6b-5533-3f5e-a797-32f4c370e10d | -4.7329 | -41.48412 | 2025-10-27 00:13:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2f5306cf-5d03-30f4-86cc-ca235687d667 | -6.58106 | -48.77267 | 2025-10-27 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 91968f5a-4f8c-3fa1-b851-51e4258f6e42 | -10.20796 | -44.70304 | 2025-10-27 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 90899534-d02d-34b8-81ef-dd2c573fa3bc | -10.75515 | -44.20418 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4ea73dff-5932-343f-92c9-0a5ec5e7ca7c | -7.91853 | -45.67983 | 2025-10-27 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f945b61b-381d-3c87-9004-41e113ee9abe | -7.60669 | -45.68589 | 2025-10-27 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 525cc692-4b1a-36c8-9637-306ea6716ace | -5.76466 | -45.55496 | 2025-10-27 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d8bf0577-59be-38e6-888c-2ed9ab8e4095 | -5.65754 | -41.09824 | 2025-10-27 00:13:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0e361f25-6b30-367c-98b7-23d3053b8ccc | -5.83094 | -43.44935 | 2025-10-27 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2709fe88-4181-3bd0-86a0-06c872230056 | -9.48182 | -40.39322 | 2025-10-27 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |


[Clique aqui para ver as próximas entradas](README5.md)
