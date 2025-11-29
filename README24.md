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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3aec4f4c-e008-38f3-af31-e5db0765415c | -12.39235 | -43.67476 | 2025-11-29 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9a43daf-3e10-3f89-ad52-a961a320f047 | -8.03807 | -43.13757 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 98b24af3-fc07-3eb8-b2ab-66dc40b397e9 | -12.39104 | -43.67143 | 2025-11-29 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b72501c-4f27-370e-b449-a7d41f8b797f | -8.66773 | -44.22355 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4af778e-27b9-3399-81b2-4af059f3b6df | -8.14001 | -49.51312 | 2025-11-29 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 55ee5a64-1510-36d4-b1ce-d8e0b2e8d3ba | -6.60012 | -43.68726 | 2025-11-29 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59ded4af-19a7-37dc-8368-3f94bf18e08a | -8.79509 | -40.43184 | 2025-11-29 04:44:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4018751d-6573-3e60-838f-d3bcca335189 | -8.16513 | -43.19044 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 87f875e5-bb45-30a6-b60c-049279aa5ac6 | -7.45223 | -44.75216 | 2025-11-29 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d2bd62e-4cb6-3649-abce-4b0df3d0e2c9 | -6.60439 | -43.68788 | 2025-11-29 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 415c3fbb-d549-3547-a7f4-17140de473d4 | -8.03872 | -43.133 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 35219c8f-55e4-323b-bdf2-9d90d326f358 | -6.4729 | -47.5258 | 2025-11-29 04:44:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df247d8a-367c-3ee0-b5f6-e10ec1738518 | -9.95186 | -44.31179 | 2025-11-29 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bea18f9-4355-372c-84f4-f1e55a06f532 | -8.16884 | -43.20686 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 45ac39f5-9835-37ed-a7fa-c253f2a31715 | -8.13669 | -49.5126 | 2025-11-29 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8a6ef8fa-1e48-3503-bcd3-b07c009342ec | -8.67199 | -44.22408 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a095e42d-0d6e-35ea-bb2f-86fbab3de788 | -8.04391 | -43.12908 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8497da63-feaa-3e25-ac9f-eaab4ad6ec1f | -8.04779 | -43.13429 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 22cd9fc8-d44f-35cb-a439-6c163f4d2489 | -8.16432 | -43.20619 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 43620508-d62d-30f5-9d3d-feaaa2c94a5c | -8.03938 | -43.12843 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d609cfeb-4793-3b63-9515-750adfc040df | -12.455 | -54.45052 | 2025-11-29 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46b6347c-2d75-364f-a19d-06a3f4883fca | -12.39301 | -43.66983 | 2025-11-29 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a540b120-3840-34f4-914b-11f6c6cea230 | -8.02966 | -43.13168 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 31844fc7-1f8e-33cc-9bfb-033789747859 | -8.17134 | -43.18865 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bb83924c-9441-3532-8090-7ab0b19aa818 | -8.67253 | -44.2202 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e5f30e6-6975-3d65-8250-c3ba35722a2c | -8.17219 | -43.20536 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| d334e79c-2158-30d4-b770-322645cb57c9 | -8.66879 | -44.22018 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0f39c30-26cb-3875-88c4-6a231ed65240 | -12.38769 | -43.67414 | 2025-11-29 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6835c888-9e84-3e51-b773-038081cdd1bf | -8.16316 | -43.20406 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 78bef60a-57dd-3cf5-b0a6-b46960e74273 | -8.1625 | -43.20861 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 446f12a4-7fec-3e1a-9ed0-4c2604c53b21 | -7.4699 | -39.96177 | 2025-11-29 04:44:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 993e7e7c-45cb-30c5-9b29-6a4d3aa62898 | -7.45676 | -44.74933 | 2025-11-29 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 276e50b6-5659-3d14-be29-0b2382f08599 | -12.45869 | -54.45117 | 2025-11-29 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c732adc4-2a50-3c4c-bcac-5cccb56dcc11 | -7.46382 | -39.96468 | 2025-11-29 04:44:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97cb5126-f075-3ce3-9692-7d686ea41cd2 | -8.66827 | -44.21971 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a36d772-2d95-3783-ad14-fc150430fa43 | -8.04326 | -43.13364 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4255b892-0bc2-3918-9aed-955f72fa9177 | -11.87309 | -49.86502 | 2025-11-29 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 115d0cdd-6886-33d6-874f-b60d5499ca04 | -8.16768 | -43.20472 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| b14ca390-a9b0-338c-b305-8ed66f50bc74 | -8.03419 | -43.13234 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3a9ed16d-538f-3ecc-bb03-aca020019a11 | -8.16702 | -43.20926 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| a3022163-3b6b-30f0-b406-ae6b66efc727 | -7.46432 | -39.96099 | 2025-11-29 04:44:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 937762f1-a05d-3481-87d8-46b4e44fe03e | -9.95435 | -44.30939 | 2025-11-29 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ae82c84-cb41-3185-8643-4a4aebd67b6e | -12.39041 | -43.67636 | 2025-11-29 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abb35101-0714-35a4-8f32-35fcd17c40bc | -8.03354 | -43.13691 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e9f7ec7e-f21b-334e-88ec-f81c9608ac07 | -11.80024 | -44.17419 | 2025-11-29 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd264875-d313-3b21-bc37-f61fb41cfb8d | -8.66822 | -44.22404 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39496d0e-bdd5-3f36-b0cb-d288800faa6f | -8.67248 | -44.22458 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30b6a89d-9d25-33b7-ae59-afe5b30bd679 | -8.67305 | -44.22069 | 2025-11-29 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 400ba6bf-aaf9-346e-b9be-f4a484216fd0 | -8.16833 | -43.20018 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 77657066-0fd9-31c7-a4e5-c078336ec7bc | -18.49395 | -49.99742 | 2025-11-29 04:46:00 | NPP-375D | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d16eda9d-2113-3442-bc11-58317c42143c | -16.76167 | -51.35278 | 2025-11-29 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44945562-a0a8-3de3-9f7e-bd6037ed3949 | -19.12544 | -52.70894 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6459288e-054d-34cb-8651-e02df21e9c19 | -20.21351 | -47.54697 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f72b161-98ad-357a-808b-26cf8c24cfef | -17.61549 | -46.66462 | 2025-11-29 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 351724d5-c1a9-3246-a92b-34cc7ba2cdc3 | -17.60777 | -46.65965 | 2025-11-29 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f072e2ea-6e6c-3637-9229-3d7f68cdf3d9 | -18.79961 | -48.02322 | 2025-11-29 04:46:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6018980a-056b-3b8c-86db-75419d0c36f4 | -16.50919 | -54.60452 | 2025-11-29 04:46:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff9c493f-710b-3827-b585-3d01ae123930 | -20.44887 | -47.51212 | 2025-11-29 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31102bd7-51bd-3b86-8b55-ad7e32db5a6f | -16.76444 | -51.35696 | 2025-11-29 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc437c00-f3bd-3faf-ab93-9f4ceffbbc16 | -20.2102 | -47.54087 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ffb3971-bdb9-3149-aa21-6f4e62ba9288 | -14.48476 | -46.99474 | 2025-11-29 04:46:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1c0eb1f-569e-3f5d-841c-a33470edf101 | -17.49064 | -57.12524 | 2025-11-29 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e352584e-dd36-3b71-99fc-3c1441959a5d | -16.67645 | -46.65449 | 2025-11-29 04:46:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5c05489-e389-3456-b098-3826c5bfe2dc | -18.12142 | -47.14427 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31f5615-5ed9-3dfe-8980-96bffb451845 | -20.17959 | -52.37456 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a30a8875-0afb-34cd-aebc-3a48ee615455 | -16.67694 | -46.65083 | 2025-11-29 04:46:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faa53505-57d2-38df-a0a6-b73efb5e642d | -20.18119 | -52.38618 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ca751569-6aa7-3b4d-9273-d5445efcda6c | -19.11821 | -52.71143 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16c5673f-212d-3d36-b365-e8b264061578 | -15.71249 | -50.0055 | 2025-11-29 04:46:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ee4412c-14ee-3bf8-b0e0-bd70db213b06 | -20.98312 | -48.62526 | 2025-11-29 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1620a09f-15de-379c-b4b6-713a5ebe5917 | -18.1382 | -47.14101 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fa42923-1579-3345-a597-1b880a307d2b | -20.1851 | -52.38308 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 06393649-bc24-317a-ae64-2888d953acb0 | -19.12212 | -52.70835 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a206ce8f-fff0-351d-b1aa-0ba59697261e | -20.98247 | -48.63021 | 2025-11-29 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3f651bff-8326-3925-afa5-f14ed966e76a | -20.17902 | -52.37823 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ffb6a35d-40c4-3673-a92c-c0296f21e906 | -19.72158 | -49.53251 | 2025-11-29 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7ceb1d60-e302-3786-bced-935beba70665 | -20.21422 | -47.54149 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20698665-c5cd-3d71-93aa-18f31fa7956a | -20.22027 | -47.52643 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a0a457c-9ccf-3ed0-bd6c-f9d90bd28543 | -20.18567 | -52.3794 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8ced1611-d9b5-3543-8b7f-e842348211cf | -18.12285 | -47.1335 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78d68d47-8552-34d4-866b-22367b2a4d6a | -20.44532 | -47.50773 | 2025-11-29 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fd66a8c-7ed5-3270-9b7f-9d75d3e149d1 | -21.12177 | -48.41225 | 2025-11-29 04:46:00 | NPP-375D | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eddf784d-a52e-3022-9fcf-62859858dfde | -18.13418 | -47.1405 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6557713c-3660-3ba5-a7d6-d820381a6e58 | -15.09661 | -43.25131 | 2025-11-29 04:46:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb1fd1c7-85b1-36f7-8d71-b981cff4591f | -19.12153 | -52.71201 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb833603-0d2d-38d0-bce8-9a2c0e173446 | -17.98691 | -54.67741 | 2025-11-29 04:46:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c3bcc7e-e563-316b-98e8-4d6aa3fc022f | -20.17569 | -52.37766 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 93b627d6-974d-3472-9180-77d3d558a61a | -17.10609 | -50.07565 | 2025-11-29 04:46:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7306b15c-18bc-3161-b789-081ecf303f3b | -20.44935 | -47.5084 | 2025-11-29 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51cbb56d-98c7-38ff-bde6-2080548e9b63 | -20.44484 | -47.51146 | 2025-11-29 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 79e5c1b7-f468-3108-9429-41cfd268c2c4 | -20.98565 | -48.63566 | 2025-11-29 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5c2d1032-f17d-3bf7-a60a-ae21bda32446 | -16.28342 | -43.91566 | 2025-11-29 04:46:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d7cd65f-ee2a-35a9-ab9e-b4dfbab30132 | -20.41521 | -47.22139 | 2025-11-29 04:46:00 | NPP-375D | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08cf692d-cb40-364c-8bca-e5e34b17d5f8 | -17.61139 | -46.66403 | 2025-11-29 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8565c3fd-2597-3d09-b76c-fdd1ada7e573 | -20.18452 | -52.38676 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 102808fc-6a47-3193-923e-4fb24169e199 | -18.61932 | -49.18916 | 2025-11-29 04:46:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bdc69b94-566c-3f0d-a5df-1658ff839ae1 | -20.18957 | -52.37631 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cbce30f3-9e98-3953-8554-7deb8a350be3 | -18.86332 | -52.11651 | 2025-11-29 04:46:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dde15f62-9a66-3cb9-879a-3c7db6588b00 | -20.18349 | -52.37146 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 883a4f6f-c2f4-3d6a-a595-b17890009bae | -20.189 | -52.37999 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README25.md)
