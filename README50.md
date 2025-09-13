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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34d34b1f-f7cd-3599-a3d3-3106b65c9a56 | -8.08753 | -50.18629 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22a4b865-3d65-318a-aae6-01a990267e41 | -10.78341 | -50.55111 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2ca45f3-e7c7-3d98-b6d4-0efcd896628a | -14.60439 | -46.33616 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 899a439e-950c-327b-ae00-863ffdf00cca | -9.52253 | -54.63337 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f4d1a8f1-a245-3acd-a262-993f036bdad1 | -14.22169 | -46.2849 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 38c57a3d-6a13-34c4-b0f3-97244e31cda1 | -11.53246 | -48.2969 | 2025-09-13 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33bf6c0c-48a4-3b5a-98cd-2192fb31b076 | -10.11785 | -45.50326 | 2025-09-13 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1d8618b-560f-304e-8414-229bb811f19b | -12.69794 | -43.4589 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3185db60-9528-35fc-b52d-225b1a5500c9 | -9.90074 | -51.8946 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a061592a-36fc-3b60-82a9-b5cefa6026ef | -14.20257 | -46.26801 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 57bf5048-f70b-3039-a55e-67bd87d23375 | -7.6242 | -46.55108 | 2025-09-13 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23b20052-f99f-3ff4-89d7-275c92a95fee | -9.90195 | -51.89553 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d211162b-b786-3195-b062-cbdf833e38a7 | -11.17785 | -51.421 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8231df3c-a5bd-314f-b9f7-bad26a735472 | -11.6768 | -46.51104 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbfac69b-26c2-36d1-86a6-d6b9e3996aff | -13.26536 | -43.75675 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a053cc3a-14e0-36e4-bde8-675c9a60f581 | -14.25631 | -45.07223 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b8eae5f-2e87-3c1b-a7e6-bdfd8ad16ade | -9.90806 | -51.89299 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ff5a0a-2f99-3be6-8bec-d48d2db9697b | -14.17411 | -46.24163 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1b37e361-66de-3736-b1e8-de2675f71ac3 | -12.61984 | -44.19903 | 2025-09-13 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4409d34-6480-3189-9e7f-1257260f5bfe | -11.87332 | -50.56959 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9d713ffb-f11d-3fbd-9ea9-8e83a74e9398 | -15.44343 | -43.64387 | 2025-09-13 04:08:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa456fc1-f898-3ef7-902e-88abf58d6000 | -8.09869 | -50.18158 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 086f4ace-deee-3209-b53e-68154a382e0d | -13.91564 | -48.28168 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0978d135-d827-334e-b970-72e4d0ab01f6 | -14.19972 | -46.26324 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 84bb3103-31a2-36a1-9e30-f3ff571d3407 | -10.36882 | -50.50506 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c46aefd6-74f6-3dc7-8d77-4c368670047b | -9.2443 | -51.25884 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 202cb230-47a6-35f1-b9cc-2721e13a841a | -9.03737 | -47.03742 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 436c5f4c-324e-33d2-a768-bd2e12c61268 | -10.59652 | -43.02435 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 95a2bf30-2524-31ef-9ca8-10d20acbb6f8 | -14.23582 | -44.24995 | 2025-09-13 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b5d417ce-9c82-3436-aa7b-3f668a10f002 | -8.0947 | -50.17507 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b4c9093-02b3-362c-82ac-9b279e556a7a | -14.22455 | -46.28969 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e397027b-316b-3a46-8e99-cb12847c844f | -13.90589 | -48.29025 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ecb1b01-6b76-3cac-b424-a1900ba613c5 | -13.95064 | -48.18796 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 770be570-78ef-3824-8c73-bb6cba2bb7dc | -10.78796 | -44.78291 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0ab2af9-4886-3047-b74c-1f928e63cee6 | -9.9027 | -51.89158 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e23fb252-a8f4-392e-87c0-5ff6f4e470b4 | -11.40731 | -43.64814 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 728d7d53-2dfb-30c2-89ec-f36d58438082 | -11.41488 | -50.74643 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 030d1ba7-a3ce-38ca-8c90-00db1d652dd4 | -8.46899 | -47.25221 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 876def80-77f4-3f5a-8b8b-e26a932028b9 | -8.92019 | -46.142 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f0dd1c-0d7f-34e4-8b8b-00987d8120ac | -8.95423 | -44.45223 | 2025-09-13 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49c938d7-f7ce-3d79-b29b-d76302d4eceb | -8.24123 | -44.3552 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4bc3214f-1b26-3409-9e85-72701618ad40 | -11.1328 | -50.70479 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ec5db0a-0adf-33e7-a395-92154d4f2533 | -9.23914 | -51.2273 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58f6c28c-4076-3169-99e1-e8dd84176ab4 | -10.77193 | -44.77221 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb4ded60-eccc-3cc4-98be-37c1a663105c | -11.80716 | -50.55107 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 8238efd6-ee1d-32df-a615-43175c95dd92 | -12.99705 | -46.73625 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a65cf934-c58a-310c-aba6-dbe77ecb5156 | -12.12244 | -47.5918 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78064ef7-d775-3c47-a3ff-e8c4fed9bfce | -14.2103 | -46.26564 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b51f7c7a-7971-32e8-8826-77da3cfd712b | -12.83697 | -47.95099 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76d75740-dbbc-330f-b12e-adcdc86ca13e | -14.1926 | -46.28341 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d721c5c-f365-356f-a058-3b09f07d69bc | -10.15978 | -46.16266 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a6b9b8d-b9be-399e-924d-717d3981c49d | -9.5181 | -54.6559 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bbef3d9-4295-31fd-a081-fa9f4293bd60 | -12.80988 | -47.98774 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c1614ec-48cb-3ddd-942d-4af53c863392 | -14.21459 | -46.28354 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cfce185e-b1b0-3f26-b5b5-4daf916f7423 | -12.99578 | -46.73436 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5967163f-e576-351e-a3eb-0c1f203fd0ad | -15.83352 | -42.59807 | 2025-09-13 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ace7ff1f-125c-3b87-b7b3-04eeda67a006 | -14.46143 | -47.33247 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6faff33b-9b4d-387c-a84a-46f54d0a074b | -11.48841 | -43.62778 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84aed1e9-f4c9-3979-b303-035520857d14 | -9.41453 | -43.40746 | 2025-09-13 04:08:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6152d233-d2dd-3a88-8bd7-a334d877b0fe | -11.48347 | -43.61595 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0cdea9-607a-3afa-935e-65ea183433d6 | -13.67207 | -44.22573 | 2025-09-13 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7526fe5b-18a9-353c-90ff-0b4d26f8c5c7 | -11.18723 | -48.35457 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1540f0a2-2706-3062-b4bd-ca8ac9bb8c5d | -11.12299 | -50.70288 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41eafb65-f9cc-39bc-90ad-d651a35706ae | -11.20744 | -48.41094 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d25e298-c09f-3de7-ade3-193d8c640e4a | -11.20398 | -48.40601 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e112b8-8341-3565-9a17-5af6ab139346 | -11.74089 | -44.21169 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6477db03-4c35-3795-98dc-ceaf707d4fd4 | -9.66698 | -47.55067 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a946184-63fb-306b-b4eb-752a8e46ee88 | -9.50119 | -46.42415 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c9a9457-98a3-3aba-84ba-17e83ea4781d | -11.9919 | -47.76237 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f44a140-0a0c-35b7-b86a-5056117d9f0d | -9.03757 | -47.05987 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49263e8d-e597-3acb-8e24-f28127ed87da | -9.00624 | -45.78734 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd7a5416-7c20-3863-bb10-afb6cc92e453 | -11.74477 | -46.61519 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52fc287a-44a7-3e1d-931f-002436f8a639 | -9.25196 | -51.2465 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78026bdc-931c-31cb-920e-d04d5368643f | -14.28177 | -46.05872 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d9f8f39-cd10-39e7-bf6a-56fae799035a | -11.86853 | -50.56864 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| cceed0a5-0848-3f16-955b-82d0fa06081b | -11.13562 | -50.71695 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db12cdfd-85ef-32ca-9acc-20ac16802f6f | -10.76388 | -50.54733 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d5a5032-807f-3b47-a161-f02fc68c75b1 | -9.85907 | -43.1326 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55e7dab4-9683-331e-95c3-15a75cbae94f | -12.39812 | -43.82231 | 2025-09-13 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab733d7d-cedf-3160-8e52-d36dc2a1ba67 | -11.39898 | -43.52961 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce976473-14a4-3125-8b4b-7804113600f0 | -11.99527 | -47.76657 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d044b187-93d1-39fa-b389-8a0a6a811513 | -10.41089 | -50.61775 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38b0c5e4-09e3-39cf-8abb-99798ff38c75 | -14.21669 | -46.27119 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d9b9fb9-eacb-32b9-9ab8-748e49a5d68b | -12.10487 | -47.59932 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9737bf04-ebbc-3da3-9579-20514dea2d00 | -14.60865 | -46.33272 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9800bbf-709e-33a2-ad30-87b61a491416 | -11.44289 | -45.62514 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2587225a-374c-3395-85cd-aee8187ffe27 | -9.25244 | -51.23959 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb67fb34-0b81-3c7c-8e05-493cc111d623 | -11.4123 | -50.74961 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9cc6cda-274d-31cb-bb6f-5ba7f4ae9c7e | -10.76893 | -41.33804 | 2025-09-13 04:08:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f79fc127-b973-3dcb-b6e0-7ec65f78edf8 | -11.10813 | -51.41483 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9984a1cc-c744-36dc-9bb2-55854170c12d | -9.79177 | -47.79025 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 937d860f-9e29-3d9a-90a3-5e3f1d848ca9 | -11.77958 | -43.7607 | 2025-09-13 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec5c1a53-a533-3150-a9fe-b87b4b8a6343 | -12.83782 | -47.94619 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cab1958-f759-3b6f-acb0-4c6d1e1ad367 | -14.28461 | -46.06344 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd282406-ab80-33ce-bdea-e366c927cc86 | -12.94057 | -48.00304 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f971b229-7274-329d-86f0-a1074b898dab | -14.20468 | -46.27708 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a986e0c6-64a3-3d03-a6f6-d9ea0f13ad79 | -10.91667 | -47.20837 | 2025-09-13 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c155e0c0-02c3-33b2-ac07-59f9e386ab31 | -11.21095 | -41.59846 | 2025-09-13 04:08:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0002d8b-edad-36d9-9c07-ddbb3b1df819 | -10.33373 | -48.81437 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c99cec36-6cde-3958-90fe-f732c64047c9 | -13.2552 | -43.79899 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
