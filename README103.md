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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13bbb4fc-dc39-3b5c-a6e6-69fe93a42b27 | -17.02346 | -57.49107 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f32ffb29-520e-3282-8fdd-4de4506be939 | -17.02297 | -57.49492 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6981782c-1ff9-3a15-9e8c-a6a52c25a6ba | -17.02278 | -57.4636 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 46c89244-567b-37d4-b4a6-80d771f4a19d | -17.02198 | -57.50258 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 8c04669c-a660-334d-84bd-a23f8454b343 | -17.02149 | -57.5064 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| def90970-823f-3e78-a6f0-4eb324993459 | -17.02051 | -57.51406 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 27a7e888-b8ec-3234-81e8-3d781d3d2e8c | -17.02002 | -57.51787 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e1fb9198-4344-3029-ba8d-b1e6ee33a00b | -17.01934 | -57.49051 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 55c44587-374d-32d4-bb0e-f1e371c0be4f | -17.01885 | -57.49433 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 68867ad9-7415-3a4b-809a-70b3b477c3de | -17.93953 | -57.21715 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c49761dc-8fe0-30db-b99c-26c0999fe670 | -17.01836 | -57.49817 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c20adc2d-612f-3a51-8d1c-0f594254b905 | -17.0164 | -57.51348 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2449ee37-39f4-34b4-9b68-84c1150a3871 | -17.01571 | -57.48609 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6370ff65-43d7-37ee-b65a-d2c105ffdd90 | -17.01522 | -57.48993 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5d301645-9d50-3fca-9087-f30df2729538 | -17.01229 | -57.51291 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fe527efe-4c05-355f-949c-922003acd343 | -17.01131 | -57.52053 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6e0d40be-5320-3b53-af40-5b31380c4bb7 | -16.97069 | -57.519 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 369852d6-c044-3bf0-9a3a-b9c63722bd16 | -16.97018 | -57.5228 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 9797a0a5-5e42-382d-82eb-4fbc92026880 | -16.96608 | -57.52223 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 6b26c460-29af-3669-8185-e191fd0617ed | -16.96197 | -57.52165 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3501e671-dcd3-3cdd-b112-eb70b4cb50fc | -16.94766 | -57.53512 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 20a8c2a5-a18d-3447-a436-020767a5b476 | -16.94717 | -57.53891 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f415fbd5-7cd4-354b-943b-5f6d9f3db2c3 | -16.94605 | -57.51556 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bca8dbe1-b966-3a72-9d8d-33c9d21c7a3f | -16.94145 | -57.51878 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fc122a66-e2ab-3190-acb3-90a95d4c5874 | -16.94095 | -57.52258 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5a0dfcb4-cc65-3912-a270-9510b7369c6c | -16.93897 | -57.53777 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 25ae79fc-d7ef-3cb4-8775-e8eb776b87d0 | -16.93685 | -57.52201 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 08806bba-351a-3b09-a81b-c80dc4475d46 | -16.93225 | -57.52523 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f896d200-693a-3e6b-bc91-29b292a17593 | -16.91565 | -57.49191 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b78c769c-2ba0-3715-8acc-67b40bf3c58e | -16.91516 | -57.49571 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da3492d2-c5e3-310c-9013-0f7b24ca3445 | -16.91105 | -57.49513 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41a0b7cf-4492-3aca-aaeb-68466087942c | -16.90694 | -57.49456 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 74eebfd1-944e-33a4-89a0-9d885ca53766 | -17.01689 | -57.50965 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7f63b5b4-8846-3210-9794-1b00defa51e2 | -17.01657 | -57.38 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 05157a00-1b21-377c-ba69-0c7c89595fcb | -17.01608 | -57.3839 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 12d0e7de-b885-3464-9a8a-ec52473fa554 | -17.01591 | -57.51729 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 93837959-02b3-3d59-8328-0869ba1a19f0 | -17.01375 | -57.50142 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1335bbd3-b018-3b62-a3bb-11125dcc451b | -17.93797 | -57.22948 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a0b55bc5-eecd-351c-8e58-aa91bf38ad85 | -17.01327 | -57.50525 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 14f395b0-d7ed-32a1-9dbe-aaad540dff5b | -17.01278 | -57.50907 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c2ec147b-3c57-3428-b1a6-c02ce5e49e0d | -17.0118 | -57.51672 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57a97cc4-cd86-30d7-9117-f33eb671b346 | -17.01023 | -57.36324 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 46278657-dcf6-3927-acfa-4a6371878fac | -17.00974 | -57.36715 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ffcb14a5-5b28-39b6-b337-e97c149e0640 | -17.00918 | -57.35561 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a02e9368-622f-34d0-b07f-ec029fb10ccc | -17.00876 | -57.37494 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 75e23281-1004-3009-b9f1-93b4520e4330 | -17.00866 | -57.50849 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ec6af5b8-b5cc-3fb3-8e4a-bfa29f4b488a | -17.00827 | -57.37884 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f759e59b-623c-3aa6-a77d-d27e68e60b1c | -17.00659 | -57.37508 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cd623650-de93-3e8a-95d8-dbb1e41a5087 | -17.00413 | -57.37826 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5ae6bea9-bdb3-38d3-8398-1ada4399cb7b | -17.00244 | -57.3745 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ac6180fe-7669-35a5-b311-d1d53e0ee2da | -17.00193 | -57.37839 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 97cc6bb4-d648-3fbe-949c-28f3f0ab9fef | -16.99981 | -57.33043 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ec4b08a-2382-3171-9e9f-f3fef03a3099 | -16.96658 | -57.51843 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| cb347f69-6e0f-32fa-ae78-73519d75bf91 | -16.96248 | -57.51785 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 9f2df32a-c2ca-3f41-bebe-2646e955a533 | -16.94555 | -57.51936 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d75a91e-2662-33d7-ad51-84b9af978e0b | -16.94357 | -57.53454 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8d7609c3-8845-3bdd-8f02-45c4b0789e5f | -16.94307 | -57.53834 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7608083e-f2d6-3be3-a625-c180352d4121 | -16.93996 | -57.53016 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5d4ca658-33ff-3909-98a3-df039194b505 | -16.93946 | -57.53397 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 07b53b89-08b6-3958-89be-e508e7dea096 | -16.93734 | -57.5182 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 865df56c-4a67-3291-b984-efb85db315f8 | -16.93373 | -57.51383 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e0ac6d0b-b377-3a76-bd71-18542821e52e | -16.93324 | -57.51763 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b9cf0108-c8e4-30f9-9abb-d1ce0c584338 | -16.93176 | -57.52903 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b443740d-4ae3-3d44-95c0-a00e21e82261 | -16.91056 | -57.49894 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8925b30a-633a-3e3c-95ae-03b4e72bede1 | -16.87011 | -57.27349 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| adf407c5-5060-3938-b4cc-7cc8539d4f5e | -16.85292 | -57.68987 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 44e0a2ac-6f57-3b92-8082-61046d9306e9 | -16.8527 | -57.69036 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9155ccd0-6b9f-3623-96c6-b9e1722128cc | -16.82199 | -57.41716 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 74d35693-612a-3741-a176-963e14889b7f | -17.20278 | -57.51916 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 29040da9-3fb9-3043-ba15-264478bf57f1 | -17.20161 | -57.51768 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 36408c52-8b77-34a1-8b40-98c4fed333ad | -17.20113 | -57.52154 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 47968343-35d3-3c96-a332-e5c98220bf08 | -17.19041 | -57.29113 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 91e5edde-567e-3574-9802-bf21b1a61de9 | -17.1899 | -57.29509 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b8eecf4b-24c5-3919-8b29-766dd2cc07ed | -17.18521 | -57.29847 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3a496090-2617-3cdc-b6fe-47f076c33656 | -17.09956 | -57.47343 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c4c24868-e148-3cc2-8ed8-26e7ee5553a8 | -17.07928 | -57.38478 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ec3613b4-f6d2-39d8-a887-2c65ef2d903d | -17.07513 | -57.38421 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fb5aadd5-3017-3f6c-b612-7c4ddf4cdba4 | -17.07077 | -57.48205 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f29dcbe6-829f-32b0-9f59-91eb208a6166 | -17.06715 | -57.47763 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c82db57f-c59c-3dd1-983b-0589c617b0be | -17.06614 | -57.48532 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8cf15441-a510-34eb-a26f-b423c901f6ff | -17.06582 | -57.39085 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55dc78b0-8cbc-36b6-a2d9-8a4c487573bd | -17.06252 | -57.4809 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d3f31fca-e5d0-3d42-823e-6b555450e315 | -17.06091 | -57.46109 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6608090f-bb69-3298-b762-6865807f646f | -17.05929 | -57.44124 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 95795376-b202-3406-928f-9ec0e12a55f8 | -17.05779 | -57.4528 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8a8e6e11-e1a9-38f8-a917-69146dcd6f7b | -17.05728 | -57.45667 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4799df84-3538-3c9e-9f87-d34850a752cb | -17.0449 | -57.45494 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1089465f-a7da-3cae-ae84-dc45603dd2a6 | -17.04176 | -57.44665 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 12043ebf-54fa-30e6-bdcc-40b41719fd35 | -17.04127 | -57.4505 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2d1a309a-06b3-34a6-8adf-f7cdb3558a93 | -17.04027 | -57.45821 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 3f6d9cad-af50-39ae-a1e8-6c2e70d73157 | -17.03878 | -57.46976 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d6d0b3d4-1499-3337-a0b0-fcdb7f93a66d | -17.03829 | -57.4736 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c79766c2-5d97-31e1-a0f5-4752abe57349 | -17.03779 | -57.47744 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7dec9bfc-d4ba-365c-a3f1-568b8ff343d5 | -17.03763 | -57.44606 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4a306e68-03ef-3e8c-a66b-b428d9ba81e6 | -17.03664 | -57.45378 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 099c65a8-43d2-3435-82fd-27ab1009e715 | -17.03565 | -57.46148 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a73bcd98-2fc1-38fa-b03f-9a41f99392a7 | -17.03285 | -57.51578 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 513f540b-b712-3365-9a61-be1799fe8029 | -17.03235 | -57.51959 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 05f0a97d-0e96-3acc-9fbc-bcbf59ff4edd | -17.03054 | -57.46861 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| acdac074-7ce7-322e-83f3-b6f64eb57895 | -17.03049 | -57.37005 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README104.md)
