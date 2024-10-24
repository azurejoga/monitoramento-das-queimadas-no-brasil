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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae5d991d-d878-3d81-9916-fce0a24b71c0 | -4.76545 | -46.40248 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ad83f24f-17aa-3a37-8607-4d950920192a | -4.76449 | -46.40919 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| eedaa8fc-2318-35fd-bf3b-1daab9f9ebdd | -4.76353 | -46.41597 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2575dbed-dc1f-3b71-952d-290e465b4a11 | -4.7617 | -46.40307 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 369b3239-ca7d-3063-87d8-4ba77e651d89 | -4.76078 | -46.40983 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08764bd8-2065-3cf3-9d26-04e511481c47 | -4.75738 | -46.40802 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 162d51c6-3520-3c7a-8723-d4fff9ae1c66 | -4.75226 | -46.64685 | 2024-10-24 05:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34e640b8-2f77-39dd-a7f2-83168db2d5a4 | -4.749 | -46.61945 | 2024-10-24 05:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6cc093f-1a5a-36f7-ad17-002e9d825ec8 | -4.74801 | -46.62639 | 2024-10-24 05:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 739fc2a8-007f-3119-8971-d1f23da1189e | -4.27853 | -46.75549 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59f13d7a-4b7c-3787-9dc7-fc7ad52f6e39 | -4.27763 | -46.76173 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2c46e0-53ed-3198-86c0-a4142caf6a67 | -3.94599 | -46.43156 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2157d5df-739f-3af7-9dce-f32261531f3c | -3.94496 | -46.43856 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e6a4cfdd-23d7-35eb-9e28-61030e9388bc | -3.94401 | -46.42933 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 543c48a0-c55d-32da-b724-c87d5157a8ba | -3.94304 | -46.43626 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 62f5bd19-25c0-3492-a78d-1f93e999db5f | -3.9389 | -46.43077 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8c8e0730-f259-3c91-b87d-4dccf96472f9 | -3.93791 | -46.43755 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 60ba797d-3a77-3e21-a2aa-d96704e19d77 | -3.93695 | -46.42836 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6704bc01-1d51-3ae1-84ef-29fd5de745e2 | -3.93599 | -46.43521 | 2024-10-24 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc6e949c-d03f-39c7-abb9-87af19484d17 | -5.69615 | -47.34995 | 2024-10-24 05:21:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 048af027-958d-34dd-9377-f2b75da9fc61 | -5.64867 | -46.97587 | 2024-10-24 05:21:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aa853a26-3dff-358b-8c3b-19e3dd46a9f5 | -5.64714 | -46.97582 | 2024-10-24 05:21:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 826a1081-0df4-3237-91d8-112c7b7df531 | -5.64168 | -46.97491 | 2024-10-24 05:21:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bffc0f13-0cc5-3037-bc4b-86e6f84e8bd7 | -5.44726 | -47.68322 | 2024-10-24 05:21:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58069777-acab-3bbe-b20f-409d6d312a2f | -5.44393 | -47.68015 | 2024-10-24 05:21:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 55504ea2-0042-3050-ab1d-c9c771df4c9b | -5.44309 | -47.68614 | 2024-10-24 05:21:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 577e5f0d-b600-3bab-9919-dc83c086cf79 | -5.44063 | -47.6819 | 2024-10-24 05:21:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ca0ecbeb-9c41-3759-9722-fa49b0863a01 | -5.43983 | -47.68785 | 2024-10-24 05:21:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c598ac7-df0c-3909-862a-d37768d8b252 | -5.30597 | -47.00473 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a28e19ee-033f-3eb4-b514-1dbd671cf5a0 | -5.30579 | -47.00947 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 599ae2d0-ba9f-3b18-b86c-ddca6eff0525 | -5.3051 | -47.01123 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af83e0c2-7c7b-3274-8899-fb21e83af97f | -5.29983 | -47.00149 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3796197c-ef79-3fb9-9a0e-72f8e8f0e22a | -5.2991 | -47.00316 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7ef34be-0e70-3faf-b899-743ef0deea1b | -5.29892 | -47.00797 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c2ec795-500c-3bf8-94d1-0d6e3c3642de | -5.29823 | -47.00971 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6763e1cb-5eb4-3192-af35-793a65463b16 | -5.29802 | -47.01444 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41595723-0d9c-3931-83ad-818c05174816 | -5.29738 | -47.01612 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2842b21e-26fb-30e2-8537-f5227c06f0e7 | -5.29204 | -47.0066 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4602e6dc-e625-3456-8e99-a795e258a8e2 | -5.29112 | -47.01318 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53edf7ce-45f9-3184-aafe-2b226a4f58d0 | -1.87421 | -47.81401 | 2024-10-24 05:21:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f037013-8c40-3486-b648-30eb4a27799b | -3.10944 | -48.60037 | 2024-10-24 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70df8daa-4ef4-3ec4-8084-1cde7284b047 | -3.10876 | -48.605 | 2024-10-24 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee830b6-bdbd-36e7-bcb7-e7f4443fa16c | -3.09994 | -48.66549 | 2024-10-24 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d3cacfc-4fc0-374c-aa0b-793f39e0109d | -3.09926 | -48.67012 | 2024-10-24 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fc37efe-aef8-34b6-8b9c-98f94cfa473f | -3.45685 | -47.67347 | 2024-10-24 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb41c9fb-0528-3a2c-b0c4-07be1bf372a5 | -3.45619 | -47.67456 | 2024-10-24 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45d318d0-6521-3cb0-8e87-e86b98a9b6cf | -2.77521 | -48.70102 | 2024-10-24 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd997bb3-699b-3640-b6b4-25eb15009696 | -4.87822 | -48.21389 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 435037ae-49e8-3ef8-a1a8-49158e3eec08 | -4.87178 | -48.21301 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21447cb8-6353-3fea-af91-ed27e22f5a71 | -4.25171 | -49.18887 | 2024-10-24 05:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a714ce-7886-3e00-a4f2-5c032ced7da5 | -4.25108 | -49.19317 | 2024-10-24 05:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87dab3ae-e952-35c3-9214-cbd47951e815 | -4.24912 | -48.3409 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1fd43cef-b5a1-3559-bb48-edc5504c957f | -4.24843 | -48.34573 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 06331257-8c9a-3932-8c14-58a1c5366bc4 | -4.24216 | -48.34448 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1302f3c2-0489-3131-80be-fe4a9716b740 | -4.24148 | -48.34917 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 63b4d70e-df3f-31d9-8ad7-4ca920fb8452 | -4.2079 | -48.03297 | 2024-10-24 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dba7653-5edf-3a58-b4e4-d87b2421a2cd | -4.20714 | -48.03846 | 2024-10-24 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a080b0ef-54b7-3eac-b5c4-19e91460c1a9 | -4.18097 | -48.59356 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ed748c-595c-34c8-bd43-62a6cc5d3240 | -4.18029 | -48.5983 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50bc7ed9-a6a5-3fde-af8d-7c3fe9a6b3bc | -4.17477 | -48.59249 | 2024-10-24 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509bf16a-be84-3938-8635-1574d2205f32 | -3.82794 | -48.87427 | 2024-10-24 05:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 879cad74-ecd0-30b6-ad97-bafbb829f94e | -3.82728 | -48.87883 | 2024-10-24 05:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1c5c99b-7489-384c-8fe5-2664050e1fa0 | -5.49082 | -49.50885 | 2024-10-24 05:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe484a97-18f5-3625-b69e-a91a5a77aa39 | -5.49019 | -49.51325 | 2024-10-24 05:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 235052ee-8d55-30fd-8062-c83cce28a93c | -3.25715 | -50.17027 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 512b036f-6725-3a0d-b59b-d3152019123b | -3.25162 | -50.16942 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b93f35b-e1d5-3394-a17a-b13d53b95eb9 | -3.2494 | -50.18421 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 935859cb-7f0f-35a1-a2d0-54de12f608ec | -3.24441 | -50.17974 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e16aeaf-a811-380f-9922-c58b714a7457 | -3.24386 | -50.18338 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7d0d01-5d9b-304d-aac9-529d13ba0765 | -3.22391 | -50.16537 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6293ea85-bb31-3499-9fbf-555d46b85166 | -3.22336 | -50.16907 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c048d6e6-703b-3e62-a33c-12df32e4953d | -3.21782 | -50.16826 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84333064-d68a-3d66-b78f-c39f46d8cbfe | -3.21727 | -50.17195 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3c48236-cd6e-370c-be87-104e7d25366f | -3.21674 | -50.17556 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 785f27cb-ba7c-3dd1-aada-2c6bd425a63e | -3.16273 | -50.46588 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16b871df-d981-38b6-adf0-cdd31c93b53c | -3.15781 | -50.46161 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 737708d5-b5f8-3a58-8fac-87e28e351cd3 | -3.1573 | -50.46508 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1694ef62-363d-37be-bcab-f2add481cd28 | -3.15679 | -50.46856 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ea8b3d9-ef72-3765-b389-666d2123fc82 | -3.15238 | -50.4608 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd7bb4e4-686b-37cf-94f8-f44e6aad3565 | -3.15187 | -50.46429 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 98e8130f-6ad3-30f0-852a-52185bd0b409 | -3.15136 | -50.46775 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f98e7cd0-6610-3e7e-891c-a19dfa2420da | -3.14746 | -50.45651 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2df6cf9b-2271-392c-bbc0-fa651fa79e12 | -3.14695 | -50.46 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dcadf581-23e4-3e69-af7b-cb9ce67f10fc | -3.07233 | -50.50106 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4660bf3a-91b3-341a-b35d-03efbcbd761b | -3.07182 | -50.5045 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de12165-c209-38d6-a762-b3e149db6d08 | -3.0713 | -50.50795 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3baad22e-585c-3cb1-a78f-eaad74191350 | -3.06693 | -50.50026 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| faa53baf-8c41-342f-8a6c-ed1b850c7ead | -3.5097 | -50.47975 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 017203fc-f0aa-3763-89b8-2c306716a9da | -3.50917 | -50.48337 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e89e4db-af04-3fc1-b91e-59bde5c3b078 | -3.50504 | -50.28262 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 334dbe00-75cd-3ce4-9be9-5ed288b611d7 | -3.50451 | -50.2863 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7f5b14d-8b69-398c-948a-c59a38c27f24 | -3.48145 | -50.48267 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259ca0ad-7964-3ce0-99cd-496b067355b3 | -3.48092 | -50.48627 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170f28a5-4aea-3134-8b72-0c3f3506c237 | -3.46741 | -50.08201 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed1795df-7d78-39a4-bf18-48863f2115a2 | -3.46684 | -50.0858 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79268933-98f9-39d7-83db-c281e356d6fd | -3.46628 | -50.08959 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 629390a1-6612-3a26-9e9e-64b3496d76ca | -3.43771 | -50.3573 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 579d1bca-08e6-36e1-86b4-a1ce677bac17 | -3.43719 | -50.36076 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79e24c2e-1de4-30d4-a396-352e514d3755 | -3.43223 | -50.35647 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3ae88a-739f-3a02-a6ae-871cd809897c | -3.43169 | -50.3601 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README94.md)
