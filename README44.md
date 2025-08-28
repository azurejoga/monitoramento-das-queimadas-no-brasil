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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4b1a332-cb3a-3341-918d-759620edfb7b | -8.433 | -41.4559 | 2025-08-28 04:10:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 5cf2ecab-d0e7-3668-9b72-d65120db459b | -8.2893 | -45.1586 | 2025-08-28 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 7a34b781-c02d-318f-afc7-99e924a752fb | -10.4738 | -57.9366 | 2025-08-28 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 00fe75da-9989-325c-8067-419abed9128d | -9.1155 | -65.7699 | 2025-08-28 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 33d1fd48-ffc4-3d5f-b668-1427d38d47da | -10.5378 | -46.6669 | 2025-08-28 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e4d64aa5-d67b-3011-a1ea-32a8c1236be5 | -8.452 | -41.4536 | 2025-08-28 04:10:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| dddae4d7-3bfd-38fe-88c1-a76a4b5a6c2b | -13.00858 | -56.89862 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ae70afb-9b6d-3823-8020-898adeb4671f | -17.81624 | -44.5144 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d825dc7c-6c7a-35b7-8db2-ff9a10ece94c | -17.77158 | -44.49547 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70d03ad1-b381-3539-8622-9d78ec4c8a97 | -15.67448 | -52.73901 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b12db4e-3a27-3316-b96d-2d7f37ee6c6d | -19.37778 | -44.86174 | 2025-08-28 04:10:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d510fff3-92cb-34d8-bbf1-4ceb2e6fde3d | -20.52789 | -43.96712 | 2025-08-28 04:10:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0df78f86-79cf-3316-9a19-a286edc22705 | -20.68094 | -47.07945 | 2025-08-28 04:10:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec7bf341-5302-3ec0-ad82-37f8ba86eba7 | -17.81019 | -44.50964 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea7429c5-6f2f-359f-bf5b-637a1bccdd5e | -15.08167 | -48.51514 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd47b571-913d-3c62-bd09-ef0609503bc5 | -17.54502 | -46.62199 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 132ab683-109f-33c7-86be-8c0e1584ede0 | -18.45095 | -46.92987 | 2025-08-28 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65c35b40-0f93-3fc3-89a6-61d760d0db8c | -20.1421 | -47.37809 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 377a3b78-0408-360d-ac0b-0d2e82b1e781 | -17.77173 | -44.47308 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46f2d4a0-a075-3249-b588-3b6041bb0f32 | -20.36978 | -46.1889 | 2025-08-28 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a560e356-3444-3b68-b91a-02b310f91d75 | -16.36867 | -43.78951 | 2025-08-28 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08ff3631-ade9-37c6-be39-228e4e576950 | -12.99441 | -56.90309 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0a5aabe-9f14-3e16-9f09-3fc1c9d8c7b9 | -12.99184 | -56.90906 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4029ec41-871b-3b9e-99bf-b444c4ddd40b | -17.90814 | -44.25545 | 2025-08-28 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eba7f15b-bc3f-3b5a-8dcb-877b9cd23e99 | -17.81293 | -44.51382 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e23570fe-71ab-3d8c-8166-674c068f6123 | -21.02749 | -46.23334 | 2025-08-28 04:10:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7c740143-3fc5-3957-9c01-83e28e3e23f9 | -15.66998 | -52.73469 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f755c345-0418-3275-ac24-9873324ea1a2 | -14.44332 | -53.19798 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95321dcf-7e2e-3ba5-8841-92c1c063d898 | -21.02477 | -46.22894 | 2025-08-28 04:10:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5b88331-3fc1-32d9-b23b-0be12658d72c | -14.32365 | -53.28264 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b800150e-6c6a-3dd2-9bcf-d023c3f07c92 | -19.37447 | -44.86115 | 2025-08-28 04:10:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cbab0be-280f-3442-8d85-597970168555 | -15.66806 | -52.74441 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f969026-bd9c-3e4d-9f63-988207374c51 | -12.99303 | -56.90963 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1234783b-b735-39bc-90cc-db06f3bc8c5a | -16.95523 | -53.52302 | 2025-08-28 04:10:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac9ba1c1-773e-3bc5-822e-554a6280b214 | -16.65826 | -44.08528 | 2025-08-28 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b67363e-4748-3bc1-8d68-70f93e62988b | -21.60712 | -49.70036 | 2025-08-28 04:10:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4557fab8-3058-398f-89dc-fccbac5b68c6 | -19.12306 | -44.01638 | 2025-08-28 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c8da673-432c-31f9-8d29-b473818b6147 | -14.33581 | -53.25034 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3877766f-6fc2-348f-8c0f-55203b5fa1ef | -20.13507 | -47.37709 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15bb2668-e1ce-3ae0-97a3-9a194036d4c2 | -21.1454 | -46.97337 | 2025-08-28 04:10:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c24c58c-9ca8-37ca-9d5a-d21a7e368159 | -12.99326 | -56.90252 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c85e4ce6-c9b9-3dad-be66-ffd1b1ec2cef | -20.11733 | -44.34667 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7af1ac06-1975-3acd-b571-ddb7c599eebb | -15.62891 | -52.75263 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e91ecf2-01b5-308d-9527-ba7d961893c6 | -21.89782 | -43.31064 | 2025-08-28 04:10:00 | NOAA-20 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 305fc207-9e10-31eb-ae9c-9cbc5c3e1f4e | -14.34869 | -53.35677 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8819bece-2681-31d8-87da-0746b9b329c1 | -20.14911 | -47.37926 | 2025-08-28 04:10:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcd35764-a734-3692-9807-f2ad26a2979e | -14.33072 | -51.91438 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5829e53c-0bf7-3ad4-ac0f-7bf00156b07b | -20.81148 | -42.42036 | 2025-08-28 04:10:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f0bb315-bb46-3c9e-82a2-32ad7150706d | -18.13157 | -44.45353 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e00ef3c6-83a3-3fec-a7a4-58ba61fbce48 | -15.62003 | -52.71678 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3917e503-b2a2-3b3e-b9cf-faa4a6a63bf0 | -17.75775 | -44.49679 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f780939-94f7-353e-aef4-712124b9e5b0 | -16.80944 | -41.22898 | 2025-08-28 04:10:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 669a51ad-cf50-31a0-b214-8ad3295bb4c1 | -20.13578 | -47.37295 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1506627e-f645-37ce-89c5-2965e8091a32 | -17.99252 | -45.94104 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7b60051-92fc-3ecd-a211-9ac920e754c6 | -17.54774 | -46.60594 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab351269-094a-36e7-a084-4b432c40fe0b | -14.33129 | -51.91148 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05bbbc2c-cb5e-36ac-a6dd-c1084bae2ca2 | -17.5513 | -46.62729 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 705a9ca9-6f4f-3363-8476-37c0752d3ec7 | -16.15418 | -40.34843 | 2025-08-28 04:10:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0eb1adef-6d40-3b93-b1b4-45d3574c5a4c | -19.15812 | -41.82715 | 2025-08-28 04:10:00 | NOAA-20 | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b3ddb9a9-9f95-343e-b819-e26de096ba01 | -16.54549 | -42.34609 | 2025-08-28 04:10:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20948297-6375-3b0d-8d27-6ad9e475c2fc | -20.14631 | -47.37454 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dd5827a-88ca-3606-b50a-9ae09c0b782c | -21.60856 | -49.70246 | 2025-08-28 04:10:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0dafec0e-102f-3d3f-b6bb-224bfc185175 | -14.28974 | -53.0502 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ae00e42-cf92-30cf-8515-ce787335ebe4 | -14.36413 | -52.09025 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9529276-f616-32b8-9e82-b1de92b1ba69 | -20.25373 | -42.0085 | 2025-08-28 04:10:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c729333-1d29-3afb-b06e-215d466b069a | -14.43863 | -53.19328 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c44d38b2-0da3-30e3-af79-2efe76cea78c | -18.15773 | -44.4171 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cc82b14-ae10-31c1-9428-14eed9ad944e | -17.77216 | -44.49181 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558f6b42-2a7c-35e6-b169-41b4508e5a2e | -15.67674 | -52.73611 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d24e590-625c-3cc8-8397-eb8d2ae67270 | -18.08108 | -44.06193 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbfed05e-d1fd-3e0e-b9d9-746a1ea31664 | -18.08051 | -44.06553 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea8696c2-ed49-3643-a212-77a4c44c70d1 | -17.54435 | -46.626 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10c80487-688e-3f27-9813-fb47f030c4fa | -20.1146 | -44.3424 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7fea7032-a98e-3ffc-b7a4-7a29bebd4b82 | -13.00574 | -56.91175 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67cf424d-b7ed-33af-845c-6c951bf5e48a | -17.30475 | -45.11439 | 2025-08-28 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d99d4b7-5d24-303e-9708-b68b09361512 | -15.67721 | -52.76006 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a63b078-c380-38ea-b85f-6b337cb65fa3 | -19.46835 | -42.6261 | 2025-08-28 04:10:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ab300d71-2dbd-3319-b178-0744f1a0a9ec | -19.97216 | -47.52228 | 2025-08-28 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec8b2442-933e-303e-84d4-3158e25c4659 | -14.33512 | -53.25379 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 786c7e26-e10c-3ae5-a23b-f35894c92530 | -19.27742 | -43.74094 | 2025-08-28 04:10:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 300bd8ec-d051-3f79-a167-281c383d6820 | -17.77409 | -48.50438 | 2025-08-28 04:10:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 920a5915-c7ae-3a3b-bdbc-6c317a72b10d | -21.03609 | -48.62918 | 2025-08-28 04:10:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 484be6f1-418a-3868-b126-2996f64657b0 | -22.6763 | -44.42383 | 2025-08-28 04:10:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 144dc708-a867-3719-8a62-353454041ea6 | -16.36536 | -43.78895 | 2025-08-28 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2caf7557-df11-32c4-a5db-6320a676286c | -19.25261 | -42.04642 | 2025-08-28 04:10:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf5e46fa-3377-35d2-bce6-18f3f36c4bb7 | -14.33186 | -51.90858 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b55579e-491f-35c0-a7a5-aa2ed085551d | -18.05645 | -45.17342 | 2025-08-28 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9102e232-bfe2-371e-9df1-e6e475a5ef09 | -18.25226 | -47.66372 | 2025-08-28 04:10:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfc85dac-560c-3ff5-9f41-cb6659dfdf6d | -17.75675 | -44.48169 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afbd494b-b1ab-3702-ae43-34c731f800b2 | -19.28246 | -49.75802 | 2025-08-28 04:10:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2409769b-90d7-36be-9a53-04776b07dc9d | -21.13341 | -45.88158 | 2025-08-28 04:10:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a7fab88-37f6-3c55-93ae-843c84db21a0 | -14.33112 | -51.91418 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ba19eec-fb3f-3ed3-bb05-4a3bffe956f6 | -17.5457 | -46.61797 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41fcb7b3-4b31-321e-8067-4b1326666670 | -18.99321 | -40.29179 | 2025-08-28 04:10:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 90a4d68f-ed33-3653-b058-6e43a645a55a | -15.61992 | -52.74398 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b364dce-9c2c-3aa4-a986-ed8494b4ee72 | -18.0772 | -44.06496 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec5f612b-f287-3007-8f30-ca5d84d07670 | -14.2666 | -53.08205 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea0c0ece-2605-313b-9061-a6d2b077f256 | -15.6206 | -52.74062 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 112c170b-30e3-380f-9c69-35148c657df1 | -21.13491 | -45.89345 | 2025-08-28 04:10:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9ca8103-2b95-34f2-bcb2-f8695674238c | -21.61392 | -48.93023 | 2025-08-28 04:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README45.md)
