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
| c1b800ba-5cc4-3ce7-b2d2-e4b43e607cdd | -21.25185 | -49.17683 | 2026-07-07 04:27:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 98a52753-a176-3720-96b3-2d99aa02338a | -22.37914 | -49.79221 | 2026-07-07 04:27:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d1ee34c-8021-3971-a28c-b0cfa47ae763 | -19.14768 | -47.64593 | 2026-07-07 04:27:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d27c426-c52c-3a72-9939-f59bb02f9dc1 | -23.56298 | -47.51505 | 2026-07-07 04:27:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ac419f02-c531-349e-80aa-082f4f49c224 | -21.06279 | -47.26149 | 2026-07-07 04:27:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6709a3b-ada2-33bd-94f3-84fc41efe92b | -18.08802 | -54.03157 | 2026-07-07 04:27:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16600c8b-d4ab-3c59-9fb3-87ebb01c6313 | -23.5663 | -47.51567 | 2026-07-07 04:27:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3ab56956-2edc-3ef1-b9f8-7c1228e14923 | -18.08783 | -54.0275 | 2026-07-07 04:27:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d445d4aa-4bf4-390c-8ab0-2e8fcd698208 | -22.02825 | -48.22638 | 2026-07-07 04:27:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7859d5c4-ab03-33cd-8cd2-27fb2f379f01 | -19.06185 | -52.88725 | 2026-07-07 04:27:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8091c2cd-789b-30e2-b533-06906ce41450 | -20.52818 | -43.97187 | 2026-07-07 04:27:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8558b9ca-c188-3dd2-9211-210e7a4966fe | -16.52697 | -47.73918 | 2026-07-07 04:27:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c492d4d4-4bdd-3d5f-95db-bef633289ee7 | -20.52465 | -43.97134 | 2026-07-07 04:27:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b0c6ae24-b97e-34b2-a047-f13002e86be8 | -22.82887 | -47.15134 | 2026-07-07 04:27:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ecd73dc-9062-322b-82dd-3be67ad8bab2 | -21.05946 | -47.26088 | 2026-07-07 04:27:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af892e67-f3b6-363e-81bf-8aa4964ca128 | -22.79096 | -49.34269 | 2026-07-07 04:27:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fdc3b0e3-685f-3f73-8d8b-e9cfafd12864 | -22.78753 | -49.34199 | 2026-07-07 04:27:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b62193df-e262-307a-aa7b-8fa0d5b833fb | -18.54991 | -46.82134 | 2026-07-07 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1937108f-6a8f-33c4-8670-e8ffcc26ee0b | -19.06534 | -52.8927 | 2026-07-07 04:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c2ff212-ab20-31ce-8243-8b5474508a47 | -19.85153 | -49.07124 | 2026-07-07 04:27:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d3c7c44-6fef-3c1b-b636-7e58b588e2b0 | -22.02552 | -48.22192 | 2026-07-07 04:27:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50565f62-54fc-30bd-9ce1-56cf170ee2ab | -13.2783 | -54.3469 | 2026-07-07 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 51f32320-e678-33a6-89c5-29fc7f5b38c2 | -6.9326 | -43.7032 | 2026-07-07 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 174505a0-8897-38f2-83ab-5857b8f645cf | -6.9138 | -43.7049 | 2026-07-07 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c974b5ee-004b-37e3-aade-7ad9b3b9dbce | -10.9397 | -43.0593 | 2026-07-07 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f7cc8e8e-94d9-3639-bcf5-7d86f1921c43 | -6.9138 | -43.7049 | 2026-07-07 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 47fe592a-e239-3d13-a182-5cfdfd4c5784 | -5.50768 | -44.07568 | 2026-07-07 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83937919-6332-3838-a75c-34a497904478 | -2.79704 | -48.57727 | 2026-07-07 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b746d76b-0e40-33ea-a0a7-69a756ec3188 | -4.76854 | -41.79565 | 2026-07-07 04:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d3ffb6a1-0526-380d-a6b5-8ffd8360575a | -4.34738 | -47.76724 | 2026-07-07 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea03def9-dfc3-300f-a8ba-5e428b8a3f1a | -2.97967 | -49.26785 | 2026-07-07 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc3dc937-e244-3e62-96e5-1fe61f13ff72 | -4.2719 | -48.64017 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b918d522-9f2f-391b-a260-0028966978e0 | -5.75402 | -43.26745 | 2026-07-07 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 854bf5b2-e085-3f65-842e-fd3fda8dcc81 | -4.42856 | -47.73222 | 2026-07-07 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0c87a41-e048-3640-8a76-37425ef4ed6f | -3.15223 | -48.58737 | 2026-07-07 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5f6cced-6d0e-3fad-8f52-bc476072cc09 | -4.83253 | -44.05748 | 2026-07-07 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5462c311-fa01-3a52-8051-e550a66974fc | -4.57214 | -48.0273 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc8bf7a4-a238-309b-be7d-4ccaa1a5031d | -2.8846 | -42.95218 | 2026-07-07 04:42:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6b55990-39f5-36ad-bda3-96beffb787ac | -4.29012 | -48.35215 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6b6196-dc46-3e9c-955d-c7d8dd780d35 | -5.82971 | -43.48261 | 2026-07-07 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57a7d7b5-fce2-31ef-bc87-945aedab5164 | -5.83092 | -43.47448 | 2026-07-07 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29880656-3906-3cf7-8c2e-ca1a1bcf7f15 | -2.32347 | -48.58355 | 2026-07-07 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5996104f-91ab-3516-9e62-d872bd60d282 | -3.98244 | -48.42832 | 2026-07-07 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec5c506c-ddc5-350d-ac2f-b5ceaba2fd05 | -5.8178 | -43.59119 | 2026-07-07 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f803335-7244-340e-a9b7-1740891dc4c7 | -4.82794 | -44.06045 | 2026-07-07 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bcd31614-21ff-3454-a01e-99fe8cf338bf | -4.34458 | -47.76315 | 2026-07-07 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 485cb5ee-b701-3123-8059-7c7a30419db4 | -4.8818 | -44.37065 | 2026-07-07 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdb72866-94a7-3747-ad4f-48bed24e45e2 | -3.8758 | -42.97739 | 2026-07-07 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3685f6c8-a546-32eb-a69a-f69ea7984a67 | -4.86744 | -48.9144 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b1774d9-3dab-3889-b0d0-0367e3efa2e0 | -4.82847 | -44.05688 | 2026-07-07 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49ffa0b4-6887-3c10-a9f0-138a18c8bb28 | -3.87386 | -42.97578 | 2026-07-07 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8fb83ed-93c4-3f5d-9dbf-8ef3bab97335 | -3.19588 | -49.06238 | 2026-07-07 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e3d0c1-7e12-3471-bd95-b626ed431dc9 | -4.57604 | -48.0243 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1ce878-d836-3976-ab15-e0d1c59f2e59 | -3.87446 | -42.97169 | 2026-07-07 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ca51d75-fc79-3210-a6d4-75df3d918f7e | -5.40902 | -45.18952 | 2026-07-07 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e7ad816-3e23-3b35-b395-353578966b9c | -4.28155 | -48.23323 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3730dbbf-a77f-3653-a1ea-97ed3af06e09 | -5.50304 | -44.07869 | 2026-07-07 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 981862fd-adad-3499-a89a-57d3ec93af78 | -5.74966 | -43.26694 | 2026-07-07 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aeb7d5d-0e4e-3ac6-8f78-f0f61fef49a5 | -4.71221 | -47.97959 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1adb4207-309c-3fb8-a200-10eaee68cec5 | -4.2857 | -48.35861 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a0708c8-cf53-30f4-a673-6b6b96045fc6 | -5.31063 | -43.69051 | 2026-07-07 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d254fd2-59b0-357b-a45d-5ae6f95e64e2 | -4.28269 | -48.24769 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecaafa86-f826-3acf-a0cf-0db334befe4b | -4.8304 | -44.07177 | 2026-07-07 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 724d645d-fe6b-3196-a782-fad0e31677c0 | -4.28238 | -48.3581 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c044ce8-7408-3925-9c50-bc57f93479cf | -4.06858 | -46.3793 | 2026-07-07 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d60a52a4-f012-3beb-b586-eb823c872977 | -4.28487 | -48.23375 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 708acd12-b392-39a4-9398-f8db6a572fb8 | -3.87877 | -42.97234 | 2026-07-07 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c05890e7-bd87-3df5-95ec-7ce5bd55bedc | -4.15002 | -43.10226 | 2026-07-07 04:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b25631b-6761-3dc3-b640-90fee9cc2c9f | -4.28957 | -48.35563 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 635b3efa-c666-3b5f-b552-3915fa6ec78e | -3.19643 | -49.05894 | 2026-07-07 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 755afe10-5ea6-3fb7-bf99-2c96525fb3f8 | -4.34794 | -47.76367 | 2026-07-07 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e5047e9-3b63-3ded-86ba-4e4fe4e5c29f | -3.87643 | -42.97331 | 2026-07-07 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f04ea78-1ee4-31a2-bc44-d573f5bbd185 | -3.97913 | -48.42781 | 2026-07-07 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 267c1c82-dbab-37a7-b4b9-4969548b1c54 | -3.5107 | -48.03802 | 2026-07-07 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844cfdce-078c-3ac7-a1a3-a40a658b0c7c | -4.15063 | -43.09823 | 2026-07-07 04:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc015eda-ce11-33d5-b973-c62e863aa6a2 | -5.83031 | -43.47856 | 2026-07-07 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cfe5f83-13e7-386c-bc57-da5986c12583 | -4.57548 | -48.02782 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d182dc12-dde8-3c9e-a523-9272dffb8d0c | -5.50713 | -44.07936 | 2026-07-07 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d93c576-194d-39ea-8ff9-07e123b8e6a8 | -4.28625 | -48.35513 | 2026-07-07 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e318aa5-8354-33bd-a8b3-c6735215af70 | -2.32677 | -48.58406 | 2026-07-07 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16921c0f-2504-3f8a-b15e-3de77f7d037b | -3.15553 | -48.58789 | 2026-07-07 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc71bb6c-a0d4-3d91-9334-a9a93760dfec | -10.93625 | -43.06065 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7cdb63eb-06b6-3ee7-b522-e0e7c279171b | -11.66944 | -44.55475 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| acd7185d-7b56-33e4-a4db-0fec8126f502 | -6.20766 | -42.5161 | 2026-07-07 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e12a533a-6715-330f-bbc3-349315edb105 | -9.37561 | -44.72115 | 2026-07-07 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd4764d3-3c3c-3f7e-844c-1ea3a8cea4e3 | -12.75369 | -44.55604 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a09ca1a-d1f2-3c8a-9a1d-a7d76a2d945c | -6.92802 | -43.70048 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f1fcf03-a820-3c64-a412-87e5a5d2c138 | -11.67001 | -44.55053 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a98bcc36-4a1c-3ce6-beff-c9c716397020 | -11.44334 | -52.92614 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8912e32-ab25-3e57-849d-28b39a2424eb | -5.97725 | -43.62054 | 2026-07-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17222dc2-8940-3666-b89e-b71ca8c4c4c9 | -11.69154 | -50.3853 | 2026-07-07 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5954a147-4b05-3ace-993d-6080b6ed2018 | -11.6634 | -44.56677 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32d17894-04f2-31ea-89bd-8f5bbd2099b9 | -6.59835 | -51.69411 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e2f9bc2-028c-3114-b59a-81b98d5b1512 | -11.67321 | -44.55958 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6287c259-e739-3684-94ed-481013dbe030 | -9.1992 | -45.31783 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b97d67e-1919-3270-a6ae-e0f9dc71ef9f | -10.41514 | -46.83515 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61cf5561-6550-3838-8592-c40faa0e4839 | -11.66397 | -44.56255 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ab961be-554d-3792-ba36-230ef8c68d58 | -9.37507 | -44.72499 | 2026-07-07 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 586ef11e-03a8-3940-8dd0-5283f9969557 | -5.62475 | -47.09914 | 2026-07-07 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a653dc1-208a-336e-94b6-06b3e647d3a1 | -5.78193 | -46.16529 | 2026-07-07 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
