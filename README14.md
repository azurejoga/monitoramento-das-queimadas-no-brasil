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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b4ff3a-3208-39d1-ae3f-ab44b742f757 | -6.49978 | -43.10877 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d61fd91b-ae4d-35ff-932c-c3a2ca7667f2 | -11.43632 | -47.32521 | 2025-08-21 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5954f89-a167-3132-a617-6d034139038f | -13.02761 | -45.15938 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 2f771a3c-3041-3fd8-a61c-c9b5b435d1e9 | -12.08204 | -47.91332 | 2025-08-21 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e501e47-a994-313f-8af8-c1bb7562f736 | -13.03151 | -45.1882 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a0d9dd01-67e0-3861-9331-d34191d0fb19 | -12.99 | -45.21311 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97941bd6-0c19-38c6-ba47-8a67b05d773b | -13.65314 | -45.71644 | 2025-08-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46baf9e5-a5cc-39e3-8b06-4f38efeb5059 | -12.9324 | -46.20081 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30e68105-ce58-318a-b539-4791bbc9235a | -9.66065 | -48.38029 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5886de36-70c9-3b4e-9374-283f6f8fa7f3 | -8.14862 | -47.34223 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 617f0031-3c34-3d9d-b99b-ac425ec5b4ea | -11.91433 | -44.87725 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92e24667-5b23-3840-9d4e-3c8260f5e5d3 | -11.3005 | -44.93101 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f82d5f2c-a11b-332e-bd68-cecd1e22e944 | -12.63921 | -46.87094 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e314dd92-c214-3fe9-afe6-5c28d4db09aa | -13.01455 | -45.18028 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a7e099f3-8c89-316a-903e-e8dcab13105e | -12.89088 | -46.07827 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482fad10-89be-3696-bcfe-93aced42aeda | -13.64617 | -43.80489 | 2025-08-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e8d640b-23d5-39c8-871a-a768b9c35850 | -7.70665 | -44.01873 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f78e1cd0-0edc-3daa-b7e5-c7d52cb80bf3 | -12.21062 | -45.43306 | 2025-08-21 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d85b9dd4-d52e-3592-b0cc-6bdf692828aa | -10.72019 | -48.23745 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d8f4399-675d-353b-9b46-66a1ce15207a | -6.49204 | -42.9688 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad87a8b7-dd7d-319e-a422-6f234b324009 | -13.03677 | -45.1846 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2ca9b7f5-e650-344e-949a-2c97ded7a2f2 | -11.57314 | -47.00659 | 2025-08-21 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e15cfad9-d32f-3505-9c28-34f599089b87 | -13.03957 | -45.19447 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d7148bb-e1d0-3b89-89d0-da99448dba59 | -9.55478 | -48.11536 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29efe04e-c9ee-39bc-a7db-753f4e1f200e | -7.57381 | -44.39941 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6c774b7-65ab-377a-980b-bb9b5d1888a0 | -6.29175 | -43.69122 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65614837-73bc-33ed-9ff2-644cc1e4ff8e | -7.86671 | -46.73085 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e1c1ac4-2c15-3d0d-8efe-712bc92d71ee | -6.10233 | -45.41162 | 2025-08-21 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 388811d4-4e88-3254-b86d-6cf2cd42eb32 | -13.04565 | -46.82769 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a82eb8c-5547-3987-8adc-434b7bd7298f | -11.09326 | -44.81336 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f33ef5f5-5817-39aa-bc23-216da01d4224 | -12.93985 | -46.18747 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 831b2af9-6d1b-38e0-95bb-c093ef58beec | -13.02095 | -45.19552 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0790d402-26ad-378d-a04e-eea84d2cb570 | -13.03204 | -45.16025 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 896bc03c-218a-3c64-83f0-9d14f2253ed5 | -8.21642 | -44.42569 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83dffac2-23ab-3da9-9be3-9fbeeb90da20 | -6.29096 | -43.69579 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be4144c4-5c5f-3e4a-b23c-d74f3c386ab9 | -6.95003 | -43.86551 | 2025-08-21 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18b6003-4a93-34d7-b7cf-4b30698d97a1 | -9.53881 | -47.93931 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f884f72-ce75-32b5-93d9-3b280e9b1a08 | -6.42961 | -45.48535 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67e31a7f-ba5d-35ef-a092-170b59bc6dc2 | -11.81618 | -44.25814 | 2025-08-21 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 630b4568-ddca-3507-9031-ac164275463f | -11.0908 | -44.81208 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 92231667-7d7c-3717-8764-b84e9c12eee5 | -7.62241 | -45.26933 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64d70cbe-68cb-3217-89e8-721f356695f5 | -7.2768 | -43.68103 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de83c843-0078-3f9f-acdd-19d77923a152 | -12.98373 | -45.20789 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c3f4ece9-732b-37d2-9629-a62b93f2ad78 | -13.03926 | -45.17102 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d21e4df3-e6aa-33ee-b1f9-5c24710c3910 | -13.01177 | -45.17042 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ba15e9b-3367-3443-a387-42007ec0ed75 | -7.01689 | -44.61266 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 5490708b-ff13-307f-949b-02b4acb42974 | -7.38952 | -45.98394 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4906448-56a5-3002-a0d5-4dd53f5d0b41 | -7.57012 | -44.40144 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d0bb83e-6660-3228-84f5-fcc1040f469b | -6.28752 | -43.87758 | 2025-08-21 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2cf503b-3fdb-3cdb-85fb-9246fc385689 | -13.02652 | -45.21535 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9468bf55-1e9d-3ea8-81f5-84ece5fd1023 | -6.49808 | -43.10309 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 893addba-8b21-3557-8085-f9703c009428 | -7.95374 | -42.64849 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c068298-1437-33de-b44b-e233ee56e9f3 | -10.39414 | -42.57969 | 2025-08-21 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aef83d03-d546-30bf-b045-4bd5857336fb | -6.12919 | -44.71482 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 358e4a53-f4f1-3a2e-88fd-a7f3ef78a42f | -6.53236 | -45.46721 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71287c4-f39f-3c10-a688-44c35cc0820f | -13.33226 | -40.34391 | 2025-08-21 03:49:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8adc54d6-58ba-3fcf-b98f-a3616f6f40c5 | -12.95853 | -46.2195 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18da61d8-bda9-3063-b065-1523d562b1ea | -7.01912 | -44.63095 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 900fb9b5-9d75-3f84-8e26-bb48f59ac21b | -13.03921 | -46.80764 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97984675-60e5-3e7e-8b57-e9b18a25ba8e | -8.09453 | -42.3592 | 2025-08-21 03:49:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0bb26d13-4111-3ea0-b4e0-9c72ac57cbf1 | -13.15469 | -46.90646 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de80dc1f-9a00-37c5-93bc-563c880f455c | -7.95909 | -42.64178 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2af6e015-9999-3c4b-bbc1-97708d1ff139 | -7.3838 | -45.98611 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db85a0aa-5b24-327a-bc33-16266c2c14b1 | -7.12839 | -44.65474 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb7b9d42-5390-3d08-91ed-5e049beb7b6b | -12.98738 | -45.21328 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| acc77695-ec55-30ba-a1a3-dbc7cb9a820d | -11.43757 | -47.31861 | 2025-08-21 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0534ce8e-306a-33fa-b127-d4deae0385a9 | -13.02456 | -45.20089 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c11df782-aedb-34a1-97b8-28c812d8ac7b | -12.95654 | -46.23013 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e965cc2b-f1c3-31e9-a32e-c4a127e054ca | -7.14982 | -44.18372 | 2025-08-21 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a031dc49-225f-305a-9afd-8edceac48cac | -7.72647 | -46.61768 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 648a20d2-e560-3308-9574-3d5ef6f08f2b | -13.02735 | -45.2108 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 83dd8814-dc19-36fc-9115-eb790c390290 | -11.81968 | -50.65022 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e233b3ba-a11a-3d97-abea-2abcec6a97d2 | -6.34248 | -43.42569 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53c8ac11-8315-3f53-9b25-30d8a4a69c1b | -7.23649 | -44.71209 | 2025-08-21 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a40281e3-bcf1-3dc8-9c96-427ff19400e0 | -7.09676 | -43.51326 | 2025-08-21 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11fda0f2-d1b8-3606-aba1-5deb23029ba2 | -7.49181 | -44.94582 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f4349ea-d199-3923-859e-d9458f8c0b8b | -7.26582 | -39.67148 | 2025-08-21 03:49:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebff6aab-0dac-32df-967a-6192cf4304f5 | -8.07162 | -43.68587 | 2025-08-21 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9166e743-2518-3180-b66a-a9d5ee4adb49 | -7.01706 | -44.61481 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 83b16b64-401c-399d-98cb-483568dc3b1b | -12.95754 | -46.22478 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb307791-dc06-3c42-ad1a-7b1a0c964ece | -5.87311 | -48.11588 | 2025-08-21 03:49:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa1da2b2-ecfc-3bf5-beb2-f1c0068bfed5 | -5.87926 | -48.11668 | 2025-08-21 03:49:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b41831ff-f036-3d01-b183-b1c4d2380ea6 | -12.94451 | -46.18894 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ec20971-e1f3-395c-a11a-da605be5452c | -7.28052 | -49.39827 | 2025-08-21 03:49:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 54cc634c-7aed-3ec3-9ed3-9d07602dfe52 | -9.63971 | -40.60357 | 2025-08-21 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5c3f5eb6-2f74-34ea-8a76-97f2d5edc1a2 | -7.30324 | -43.68038 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 12817df8-58d6-3c82-acda-8bee6f5ac504 | -6.36302 | -43.25494 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87f3b825-82d5-3cd7-89c2-219a2e809435 | -12.0858 | -40.31688 | 2025-08-21 03:49:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 89d60e2b-b0c3-32df-84de-18d21807604e | -9.91474 | -49.24891 | 2025-08-21 03:49:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a391a329-9010-3b57-9423-6dc3e024eec4 | -11.28668 | -46.2822 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb5f3afb-b875-3b2c-bc5f-7f1288a82d72 | -13.65325 | -45.71416 | 2025-08-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 700b39c2-7dea-394e-8212-2ad035b28cb9 | -9.29797 | -48.42777 | 2025-08-21 03:49:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d39678d-54cd-3e28-b888-ec1908d3bf5a | -7.14926 | -44.64753 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9a97ae0-3e41-3bc1-9f56-00f20f4d011c | -7.49157 | -44.94187 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d1bf487-dc5f-36ee-8287-34027536b271 | -13.03513 | -45.19356 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 11d9eac5-5474-368f-8de1-4d4583d2aea0 | -8.064 | -43.00126 | 2025-08-21 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 800304a7-3323-3491-a6df-9560b29c39b0 | -11.29958 | -44.92798 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60b2d794-d6d6-360f-bbce-31882d4ae20b | -7.70513 | -44.02755 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55ddd312-8bd2-312e-97a6-02f100a93f19 | -12.98657 | -45.21785 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0c3a6f22-fed9-3207-8c9f-897f975fb624 | -7.6633 | -45.25004 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README15.md)
