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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8755aa6-8fe5-3ddc-aad8-f1df8557f047 | -5.6036 | -47.49543 | 2025-10-16 05:08:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb874dbf-88da-3f4f-8f62-e2f29ac71956 | -6.48184 | -48.76497 | 2025-10-16 05:08:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2816f95-8ec6-33fe-8f9d-4b0c46031ecd | -10.33638 | -45.17546 | 2025-10-16 05:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426275b5-dacc-3a85-8fdd-36e5e03a9884 | -7.94878 | -44.14319 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0a5c06cd-32fc-3da5-83cb-305a3fede08f | -5.92508 | -45.4389 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a253c659-efa7-3d0e-bc7f-cbbe8e34e697 | -11.50182 | -44.06673 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d398402e-38a8-3552-b2f3-7be300842eff | -9.36515 | -46.94588 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7985088a-9590-3941-a789-7a20a0814d1d | -8.42023 | -44.73308 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 093fc3c7-8bf5-354b-aeb3-3524ddbb6fb4 | -9.59669 | -63.99466 | 2025-10-16 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa26d4a-b7b5-3094-9942-868d24135995 | -10.66597 | -45.33082 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3efaaf8-a784-3c5d-b578-c73d114c6fd6 | -6.04521 | -41.93539 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5e164d97-ddee-33b0-9319-be0fd23a4738 | -8.40905 | -46.26274 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2f0261a-fe48-31a9-bd0e-724c5c308e31 | -7.64657 | -44.08892 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b5bee029-3dc5-370a-92de-0db37451e0da | -5.88308 | -42.77925 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7a8997c6-80eb-3975-8e69-ae9d3bddb960 | -4.84522 | -48.77097 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56a5dfb3-849a-3292-be31-730b5fd27a72 | -10.87549 | -47.93608 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edcc048d-8f43-30c7-af70-dbdc4047c08f | -10.12753 | -52.34173 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7588c5b9-3e42-3c03-bd81-58719e550c42 | -8.55651 | -44.58984 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 173765a8-6722-3682-a047-41601366b937 | -8.21224 | -43.98892 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39dbae79-11f5-3339-a5cc-59d85121e58a | -7.20298 | -45.48667 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35e051c4-4567-3cb8-a62e-89d10b561c91 | -11.45352 | -44.17737 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b468fff-8df9-30aa-9063-f5031e07834b | -7.47685 | -42.7507 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 39f67029-a096-376f-86df-70fdfc85516c | -8.39718 | -46.265 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 345993b0-1f30-3ce2-a022-2e4f49900a72 | -10.26982 | -47.88822 | 2025-10-16 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9bf7af0-93fa-3c66-a035-8be3a09e5a61 | -5.68204 | -45.10313 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 424f169b-1f8f-3a1f-b89c-be06f671438f | -8.46911 | -44.19486 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bf54a6d5-269d-39a9-ac5a-6f671e659718 | -5.33118 | -43.94305 | 2025-10-16 05:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4af1d47-440c-3ed7-ade6-1a2ad6df1bc3 | -6.07297 | -47.12673 | 2025-10-16 05:08:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62f6b33f-341a-3598-84a3-a4aab1b6905f | -8.40087 | -46.26294 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9ca1d644-c14b-3e61-ace3-793ee6cfe749 | -8.39767 | -46.26127 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86b9cb78-6e26-353e-a072-c538132d377b | -8.45084 | -44.18329 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 141927b6-7928-32b5-81d6-1d37596f551c | -5.67905 | -45.10069 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ce0c00ab-0941-352d-bcb0-eb6da298743e | -10.64504 | -45.24159 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 630d406d-ba8f-3ace-be74-3f67317626ae | -8.25518 | -44.06723 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687022a5-bd7c-30bd-82f9-3bfecc1fb861 | -7.1155 | -44.72683 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dd2a0bd-5a8c-3008-bb4d-6cd9429ba6a8 | -10.70166 | -44.4312 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 84ba088f-af6e-3765-9ccf-30a4b68ebd7e | -10.13572 | -44.54889 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 669a57cb-bce2-3d9f-b27e-b657f7efe9e5 | -6.24439 | -44.01436 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4087870-5ab9-34e4-a3e5-82fe21781ea2 | -5.87597 | -43.8599 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dceccccc-d4e8-3a15-8cdb-553e4c97fb89 | -10.6207 | -45.25005 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d93e3b08-de69-332b-9878-072311026f7c | -10.81061 | -43.94191 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65b339e0-ea72-3d73-ae8b-8356c6063556 | -7.95595 | -44.13853 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14574006-ae5d-3e33-a557-431e67576d9f | -12.03355 | -47.6614 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028e5883-dbcd-34ef-ab2d-7a2afaaa5689 | -8.47041 | -44.18507 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1e10d035-43e7-3190-9964-097e8d44f2f3 | -7.46529 | -42.67654 | 2025-10-16 05:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c3026b0-b141-33e7-96b4-e0f9c574b023 | -7.94438 | -44.12615 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d50ff25-0628-3de4-b9c8-55f4cf3d57d7 | -10.04863 | -43.82881 | 2025-10-16 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64f70a11-77b0-3cc1-9f43-72da3e7d1199 | -5.4219 | -44.23295 | 2025-10-16 05:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c033fdd-b888-3f65-bb4a-5419d15e953f | -10.12543 | -44.57944 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6b9b63c-7a04-3d64-9dc1-d6046a66362a | -7.48197 | -42.74987 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1b022156-4e4c-3b2c-838e-bfb90667bb08 | -5.32831 | -43.94172 | 2025-10-16 05:08:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f690440-e439-37fc-b807-0832473f441d | -10.27507 | -47.88881 | 2025-10-16 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ff1d98-34f6-3338-8377-54d2e7bbda8b | -5.4748 | -42.9444 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 60c53cf1-5c29-3d68-b8e9-2e6fccb2469e | -7.61461 | -46.47571 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e825b4c8-c7e2-3790-8f03-349bbd68da55 | -7.48353 | -47.03117 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed3c598-95e1-3f9f-a3ec-0a5470b8e6cd | -10.83079 | -44.00442 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c50b15b-f415-3254-bcab-e46b87da142c | -6.17877 | -44.3011 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee59345f-e1d2-37d5-996e-6d1d761f97f1 | -8.06434 | -45.42143 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 828b7820-82c3-3627-a663-f6b345e12d9a | -10.12733 | -44.56375 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 987de546-03b3-3e50-bcab-1c5abed52413 | -10.65191 | -45.25419 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fb1a36ab-8a35-3aeb-b9ff-d898612d4772 | -5.87565 | -42.82502 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb14b786-cb58-3870-8f5a-faeaafcd0917 | -3.81743 | -54.07431 | 2025-10-16 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03deb9b2-501b-3823-b3fa-5489d31b89a4 | -5.50941 | -47.30165 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f6cbe2e-9a5b-3291-a873-f95f7cab87c8 | -8.29109 | -43.42742 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 731390ee-a5a4-34e5-8d4c-4e69c86e486e | -10.83637 | -43.95682 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750f4c14-d347-3fbf-b3e4-6742a84aa427 | -11.57787 | -44.06349 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1c2d685-5279-35b8-b5b2-f76937c0ecf7 | -8.19757 | -47.01601 | 2025-10-16 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7a5fb5f6-e35b-30e9-9fc4-c41a6dcb1fdf | -4.62271 | -49.55772 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 272fa1a4-3c44-3b29-814d-02b3b331752f | -9.37022 | -46.95004 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75ae8e8a-3916-342d-83b9-9630155e83c6 | -11.20758 | -43.99801 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76081ec8-58a1-3a5d-a7cd-ffd599fc8fe3 | -8.07014 | -45.42361 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 550318ce-4a03-34ad-9ee3-c26dfec6f715 | -8.4646 | -44.17908 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5ba761f4-102a-3edf-8d4a-e02cd57fd499 | -4.89049 | -48.5885 | 2025-10-16 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4379e3a-79a5-3694-ae82-d6c36aa7bf0a | -7.84846 | -45.40739 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed742640-be0e-3d70-b039-f4c8abe06abd | -7.07945 | -44.94581 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0864cbe4-fc2e-31cc-8504-cc6cffdf209c | -10.05943 | -43.85397 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24374ca7-ce18-35ca-8ea0-764f5edc4e9c | -8.06959 | -45.42792 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a933779-498e-3a3e-9e88-d5d8398eb872 | -5.87513 | -43.87175 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 668f9025-502d-38f2-ac0a-97d435417e77 | -7.93007 | -44.13514 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c89268aa-5155-3337-9669-7eae7be0841b | -9.49504 | -46.55842 | 2025-10-16 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801cbfca-1a9f-3037-9834-d512ff926bf3 | -6.22457 | -47.03804 | 2025-10-16 05:08:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4297177-a16d-3b9a-ba07-2df0c026d0cb | -5.87671 | -43.85469 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5034f972-d19c-3869-8495-f926784201b5 | -8.11553 | -55.2865 | 2025-10-16 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043a3487-85dc-389b-b0bb-b32e2277a852 | -5.47042 | -42.92612 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2e045ee2-bf52-353a-9fc9-cec6f4a0769e | -4.29982 | -50.39789 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ab340395-26be-3d4f-9bb0-1f3d1e5067a7 | -11.58325 | -44.07651 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2eed079-74f5-331e-bc99-0cb0d694ef33 | -6.25857 | -42.89809 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a049e295-6b47-309a-9d53-fb6cc65ea158 | -5.50433 | -47.30086 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cf33846-9dae-3621-8f67-01427826992c | -11.57109 | -44.0626 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64bbe64c-9963-37cb-8c57-3c7114b58952 | -5.69145 | -45.09829 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9fa6b78-2dde-32d2-b460-1a1399e83649 | -7.19884 | -45.48442 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 721165d4-d811-3436-96d7-4d003046b089 | -7.47516 | -42.76341 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 659c6707-ffd9-3566-b837-68a0f274a176 | -14.78962 | -59.252 | 2025-10-16 05:10:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0281389-ce0d-314f-a99d-ce0506573510 | -19.02866 | -47.52149 | 2025-10-16 05:10:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ff29205-5e74-3ef9-988b-db4358c493b1 | -11.37736 | -61.20985 | 2025-10-16 05:10:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42f1325-3365-398c-985f-dd3d166b6723 | -15.88658 | -43.46122 | 2025-10-16 05:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06eca185-8091-37cd-9392-148c178e8e26 | -12.42692 | -48.69633 | 2025-10-16 05:10:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1912cf60-4073-3b53-b99d-66b50c09c190 | -11.98146 | -58.06414 | 2025-10-16 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b28edfa-2b13-3b5a-83ca-e1ca2f7a6503 | -15.77949 | -43.65117 | 2025-10-16 05:10:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3bb274b-a444-3829-95b4-ec7f65be1d75 | -12.06361 | -51.20071 | 2025-10-16 05:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README80.md)
