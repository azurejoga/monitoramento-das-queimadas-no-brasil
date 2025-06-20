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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212fa93f-089d-30f2-8609-0795359dc616 | -9.31823 | -47.79373 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e97f98b7-0e80-3586-8be5-f5af0f203d11 | -5.78195 | -43.45606 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7a3c392-f1c0-3261-82a7-275a58df3756 | -10.47591 | -47.05303 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 60e72476-7e68-3bae-9ecf-b30b56915b87 | -5.48991 | -42.14584 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 368c45eb-e669-36a1-9f35-2ee573ab5ae2 | -11.3161 | -45.20103 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a439767-badb-34bb-bc2f-15ac27d8b839 | -10.52768 | -47.58451 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e37df0c-de41-30d5-80f6-098a58528cb1 | -9.95692 | -46.632 | 2025-06-20 03:38:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b120b94b-7705-304a-9fcc-666f0521cb64 | -6.4888 | -42.84971 | 2025-06-20 03:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ad0c7ca5-b905-3fca-810e-e07dcf1ce0e7 | -7.15104 | -44.06047 | 2025-06-20 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7823ff69-398f-3c8a-8c52-c9fab73904ab | -6.66661 | -44.24632 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df7ca535-c23b-3f14-a920-6062e8aa8e70 | -10.69508 | -37.05059 | 2025-06-20 03:38:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fce7ee9-5fce-3cb8-872d-69a0c89fc589 | -11.31519 | -45.20235 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 872a9bfa-78ce-3b97-b66d-464c4f229f0d | -9.30328 | -47.79644 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 678b90f4-c26b-36d1-afdf-e0188b106ba7 | -11.88302 | -40.95449 | 2025-06-20 03:38:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1cadde62-27d6-3ff8-9953-823e0f704de1 | -7.01997 | -44.59756 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 719cae3d-7d15-3538-86fa-c91d551651d2 | -9.30521 | -44.72809 | 2025-06-20 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbd0ca3a-9984-39b0-9a8d-c647d61472e7 | -10.49211 | -47.03519 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 047a1c28-66cb-35f2-ba83-8c32bfec0e0c | -10.48455 | -47.03907 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8240e332-3433-3165-b694-a0095cb0f2bd | -7.21901 | -43.06524 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 638343f0-af6d-3b18-b724-a7d16a287483 | -9.31929 | -47.79425 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88a1d4c3-fdfc-375d-adf3-967e73e318b9 | -10.51864 | -47.58612 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7663dcdf-82df-34c9-ae87-575e54355b1e | -11.9518 | -58.7574 | 2025-06-20 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 71384494-be23-3cc2-925e-adb0157014fe | -11.952 | -58.7376 | 2025-06-20 03:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2dd26347-6567-3305-b91b-e8a8a8adcc25 | -10.4754 | -47.0325 | 2025-06-20 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7c2414fd-9590-3a3c-9b74-64f35512b131 | -16.3047 | -58.2676 | 2025-06-20 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| e46fecf3-a94b-37a6-8180-b0db2410a4b6 | -7.2219 | -43.0682 | 2025-06-20 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| b14f40e3-66af-31a4-928d-7c4cca489512 | -12.21316 | -45.53221 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38471492-00e5-30d1-a2e1-35a54efc3f13 | -11.47133 | -47.28848 | 2025-06-20 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd78b640-d0d6-3cd9-b8d2-e1b55ed98abe | -12.20822 | -45.52699 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f41acbe3-cec0-314d-a6ac-4be91a087302 | -14.4359 | -48.92083 | 2025-06-20 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e3109e5-aef8-3ff8-81f3-b69e23b8e567 | -12.20658 | -45.53511 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecafc10f-691d-3db5-890a-a8cef9fb449b | -11.15396 | -46.64299 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f78cfcb6-0a5d-39db-9083-1c418473233e | -11.57285 | -47.87432 | 2025-06-20 03:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d844ba72-8495-35c9-a066-eedc4a2ba9f6 | -12.20741 | -45.53103 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| befca155-f91a-31c1-8bd2-5af46e43a574 | -11.13004 | -46.66417 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07894ca0-bc91-315c-9dfc-fb6cb4231817 | -14.44001 | -48.90221 | 2025-06-20 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c808ea-8bef-3ee5-b83f-e1cbde9b9c3b | -13.39296 | -48.45008 | 2025-06-20 03:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88439312-4a9a-354c-8be6-8dd20f264578 | -12.75507 | -44.41004 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 128e4ebb-2a75-39e5-ba76-d7e551681080 | -15.4016 | -47.81413 | 2025-06-20 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a942453-05d3-355c-82b5-e1a0e2511f15 | -12.21825 | -45.53969 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c749bbf2-5fe0-38f1-a49e-839b829f3ece | -12.26627 | -44.60837 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 160b2786-29ea-3c48-8bb6-2f3603deafb0 | -11.14266 | -46.65582 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cf5aad26-8819-3d2a-bf89-0def3eb44bba | -11.46906 | -47.29963 | 2025-06-20 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8558deba-632b-31d6-8985-8a5ed579b5bc | -12.78152 | -43.91525 | 2025-06-20 03:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2d133a5-523b-3718-af53-a46acba60c09 | -11.80486 | -48.09366 | 2025-06-20 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64ffa09d-0f4d-3078-a325-07a8a7a0e863 | -12.34577 | -49.31248 | 2025-06-20 03:40:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ea920e1-ba83-3c17-a7f3-9e92eee02b59 | -11.11999 | -46.67136 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b88fad44-e9f5-3d23-bdbf-08d544f6a5d8 | -11.13624 | -46.66586 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8a3f1d8a-fec4-3d62-9b57-217850702509 | -12.75732 | -44.4102 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8f52b05-a347-31e4-aeb2-144cb0a38d16 | -12.21984 | -45.53149 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e267696-6c8b-304a-b551-a4cbe0d98bfa | -11.14252 | -46.66719 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fd931701-4654-38f9-8465-edd52e7bad13 | -11.134 | -46.64467 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a577efa-7671-3b56-bd49-198bce11e27b | -12.21329 | -45.53436 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acb2d23e-8793-3b37-9fe8-d96fa8ac86de | -12.21234 | -45.53629 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00fd1ec0-2a5f-3740-ac56-ab9bbce5601f | -11.12524 | -46.67799 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b10218b-49cf-3a77-8fb4-92102ac3cb23 | -11.13443 | -46.66448 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c12e6ba1-0ecf-3cdb-be9c-0c4a0fd018ea | -12.76038 | -44.41111 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d222aa56-a507-3fac-8773-42b9f54967f4 | -13.26038 | -46.81686 | 2025-06-20 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8058b2b3-8102-3ad1-b848-f27a6348d6ec | -12.21974 | -45.52932 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12ceae12-e34b-3fb3-a19c-6796e74f1cb0 | -16.4685 | -45.00902 | 2025-06-20 03:40:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1fa31f6-8968-3190-b2e0-233b289ae69b | -11.47666 | -47.29549 | 2025-06-20 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce5e3aa8-cffb-37f8-a447-4901ae4afb46 | -11.13933 | -46.63942 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41e2947d-b4bb-3b56-93fe-94846358ef7c | -12.34733 | -49.3052 | 2025-06-20 03:40:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f40cea17-d88b-309d-bb2f-6fa62d2a8be4 | -11.11792 | -46.68192 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a8e9d62-5410-390d-b3e7-cc6efa42a607 | -11.12725 | -46.66772 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b8dd55-1ef4-37ef-a718-0d445ee4ae85 | -13.57651 | -44.26941 | 2025-06-20 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 031585c0-4f37-3a48-ae50-feed9ac3742d | -12.26719 | -44.60862 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d057c73-cdee-3aa3-8b90-e5adbbd97c39 | -16.46784 | -45.01229 | 2025-06-20 03:40:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d82fb9f-79bb-35d7-a05b-f4355d225216 | -11.15294 | -46.648 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8fb389f3-a7a6-3583-a4f4-c4a36024a965 | -14.4281 | -48.91856 | 2025-06-20 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 522c2109-4768-3d67-9d96-8d5310838221 | -11.12803 | -46.67407 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bfdf01b-f0db-396e-a1b5-5f0c32fc00fc | -12.26862 | -44.60141 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3739230f-b137-359e-93c4-f3bdd358a168 | -17.57476 | -47.50269 | 2025-06-20 03:40:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc55bf4-e42a-3e4f-ade3-6d83afe9e3e7 | -11.131 | -46.65942 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ccd3496-71d1-3992-bf8c-5f4d650e8232 | -12.22063 | -45.52741 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 741bf761-b30e-3b39-8569-b83504ad892f | -15.4054 | -47.80947 | 2025-06-20 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf80982-6414-3911-8606-cc4ddfb35b01 | -11.47019 | -47.29406 | 2025-06-20 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2bc480b-271f-3d77-9de5-a2933a44829b | -12.21487 | -45.52623 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bebd267c-e479-30e9-8d17-050a9b8c8c02 | -11.14563 | -46.65186 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01928a86-0b9d-3397-8d11-ef5993aa04c5 | -11.14068 | -46.66595 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 047b3448-f495-3bd1-be54-edcaf11dec65 | -11.13724 | -46.66097 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 67dad691-286f-3c4a-a501-3aa3827622b6 | -13.38486 | -48.45519 | 2025-06-20 03:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeea9d4e-851c-3a4f-8ac3-afcd8a65b34a | -11.12914 | -46.65811 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2d71ec0-e137-3008-bbe8-40ef781f4b91 | -11.79812 | -48.09214 | 2025-06-20 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a312ba61-788f-36d0-98ee-c333d8893ae9 | -15.40282 | -47.80832 | 2025-06-20 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e2c2a8d-530f-3efb-bf5b-d21cc6227df7 | -11.80066 | -48.08694 | 2025-06-20 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96c56d4f-2adc-3284-8302-da15dc59d7dc | -12.26791 | -44.60501 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a0219229-74c3-3859-90db-711560869f8b | -12.35445 | -49.30687 | 2025-06-20 03:40:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c779008d-1083-3efb-a6d1-ea246adb8889 | -15.39762 | -47.81513 | 2025-06-20 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf4b1319-3dd8-3282-8994-ae76ed0654cb | -12.20754 | -45.53316 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 967f432e-1fb8-3093-93ce-e3792552ff09 | -12.21905 | -45.53558 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f67da1d-07cb-3289-9989-bfa7a6c30f98 | -12.7657 | -44.41219 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 517cf1af-9558-3200-857d-ac7e1760aae6 | -12.26557 | -44.61198 | 2025-06-20 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bba8981-a941-3164-b9c6-5d40a2258125 | -11.12906 | -46.66899 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0df5138-fab3-3b2b-9f7d-f72278d5c484 | -11.46258 | -47.29822 | 2025-06-20 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77f5aca4-52c5-3417-86f5-1adf6433fcb0 | -11.14354 | -46.66219 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8f276aeb-38f0-3708-9aff-e605cc3a125e | -12.21892 | -45.53341 | 2025-06-20 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb5ffc35-6953-3849-b57a-417df6d01fd8 | -12.75797 | -44.40682 | 2025-06-20 03:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c1e3d97-ac85-3f5d-99c5-7401bac07947 | -11.14033 | -46.63436 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e55a6b0f-8a61-3c7c-bb9e-c7441ac418c6 | -11.13605 | -46.63459 | 2025-06-20 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
