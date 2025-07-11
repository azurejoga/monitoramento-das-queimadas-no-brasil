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
| e854784e-4ade-3cda-91e7-7f551688a9c4 | -4.61095 | -43.32118 | 2025-07-11 12:08:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6f69a4bc-57c7-3c4b-8628-aeaf60eecf07 | -7.64929 | -45.3846 | 2025-07-11 12:08:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56bcac60-ac66-37f1-bb8c-b8d3029fcc70 | -4.38691 | -41.9194 | 2025-07-11 12:08:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 89b077a6-e8be-31e0-a5e0-063e1d191c4b | -4.96477 | -39.92142 | 2025-07-11 12:08:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3e9576b8-f044-3830-b686-7660aaad8453 | -5.77645 | -43.6206 | 2025-07-11 12:08:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| aac45337-fd64-3222-aa78-1245b4fda14f | -9.17301 | -40.92373 | 2025-07-11 12:08:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bbbae701-778b-362f-ae23-addc39964bf2 | -8.071 | -43.13017 | 2025-07-11 12:08:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| a1eb288a-63de-3900-a974-129dd32ab8f9 | -6.12683 | -42.53103 | 2025-07-11 12:08:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| b3cea196-f5d1-3818-8ccb-399d4beb41e2 | -6.64758 | -43.19987 | 2025-07-11 12:08:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0dc368e3-3990-30a0-b19f-de60f88b676a | -8.15874 | -47.63206 | 2025-07-11 12:08:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4c575f58-0ada-3f05-adf2-9a10175881cc | -5.78859 | -45.1129 | 2025-07-11 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6dcc4eaa-22a3-3e97-a6a8-ab543930e6c6 | -6.15452 | -45.89479 | 2025-07-11 12:08:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6b83c5c7-2379-3089-8dde-9a8ea4b71ccf | -8.81465 | -44.55759 | 2025-07-11 12:08:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ce69a0ab-3607-3757-90c4-38493b7fef7b | -5.54173 | -43.90196 | 2025-07-11 12:08:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 847b7c43-508b-35d4-85f1-103eb51fb010 | -6.199 | -43.75041 | 2025-07-11 12:08:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b042467-c80f-39cc-b093-a32801b9c84a | -7.48462 | -43.93572 | 2025-07-11 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9ba9bbd2-d22f-3532-b18a-65b2d4cbf752 | -7.65074 | -45.3749 | 2025-07-11 12:08:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| d2d40c8c-26b7-3be2-92c0-3a42a1a34f38 | -7.19534 | -43.11642 | 2025-07-11 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5b0e333c-8ce4-3a79-b691-7c3f68d083ff | -6.85737 | -42.77329 | 2025-07-11 12:08:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ba5e44d4-c19f-39df-a6b7-aa1601522bea | -6.70762 | -44.32311 | 2025-07-11 12:08:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8433beaa-bb0f-311d-b086-2eca718aa697 | -7.64153 | -45.37352 | 2025-07-11 12:08:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 859b15ab-7c31-3279-81b5-d904324bce4b | -7.22329 | -43.12637 | 2025-07-11 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 3599a638-79de-3ef0-98ec-68743f2d11ab | -6.85229 | -42.80882 | 2025-07-11 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 61aa6ca0-37c4-3cb6-9a59-d505c41b3b45 | -6.1417 | -45.91498 | 2025-07-11 12:08:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3fd7e25c-d6ea-3e54-aedd-1b11066cb030 | -6.69194 | -43.92135 | 2025-07-11 12:08:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 49b1686b-1185-3d54-952f-ab7c148a2f98 | -6.84436 | -47.8545 | 2025-07-11 12:08:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73987e65-c8ab-3215-8b6d-56359d6cd36d | -6.88738 | -45.2367 | 2025-07-11 12:08:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 85cf5ea4-160b-3408-a25a-08eb396931dd | -5.55062 | -43.90321 | 2025-07-11 12:08:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| f3da1dac-7795-34bd-9c36-1575a9fb8641 | -3.97889 | -42.19162 | 2025-07-11 12:08:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6327f6c0-e45c-3dd0-9e77-3a5dfbf66dcf | -7.62711 | -45.35536 | 2025-07-11 12:08:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e56b0b95-6f17-343b-9cdd-b73a574eca4b | -6.44649 | -45.03297 | 2025-07-11 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 48fceced-6831-3bd6-bac0-2404f7eed02c | -7.63859 | -46.00479 | 2025-07-11 12:08:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fc107d28-ac54-30ae-9439-016c70fd725d | -4.84208 | -43.18647 | 2025-07-11 12:08:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 832a8132-7b14-378f-b4b1-fd20f8e66869 | -4.38819 | -41.91044 | 2025-07-11 12:08:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| eb5d808c-0a57-38ee-af06-24fb0af9e41d | -5.06808 | -43.72449 | 2025-07-11 12:08:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ae421f44-2b48-3aa6-b229-79a56b6e2d91 | -3.97094 | -43.27797 | 2025-07-11 12:08:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad5220cb-dda7-38eb-ad39-3b82942d634b | -8.06974 | -43.13903 | 2025-07-11 12:08:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 893ed0ae-1b62-3703-8b15-21950c26fcf9 | -6.14012 | -45.92572 | 2025-07-11 12:08:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0cb47dd8-0601-3af0-b464-4f9f6e5131b4 | -5.06037 | -45.10952 | 2025-07-11 12:08:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 205e9c06-b6e5-363d-9255-752e0e0eb1d8 | -3.98016 | -42.18279 | 2025-07-11 12:08:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ed8db869-134f-37f1-ad93-fd2ca3220157 | -6.74011 | -44.60505 | 2025-07-11 12:08:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab4b6c13-5c84-3800-ba23-c2f24901152f | -4.022 | -39.12206 | 2025-07-11 12:08:00 | TERRA_M-T | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 5d6c9151-10de-38a7-bae7-7237088e9ad0 | -6.08279 | -44.86813 | 2025-07-11 12:08:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 59fe85b4-6d8c-3a10-a8a0-95c3df380366 | -8.14818 | -47.63056 | 2025-07-11 12:08:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 09b5edc3-5795-3474-bb08-928ea3c78e33 | -6.67959 | -46.30509 | 2025-07-11 12:08:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ea94834-8584-3eaa-ba74-2a5efe6d93ab | -6.85356 | -42.79993 | 2025-07-11 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| b086e39a-f1ea-38e7-b2b3-d96c892dc56c | -6.64885 | -43.19107 | 2025-07-11 12:08:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 4530ffd1-d136-36e2-8237-89f83122569c | -6.85611 | -42.78215 | 2025-07-11 12:08:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 061e5d70-625a-31cf-816f-3d7d7b9a9e1e | -5.55193 | -43.89425 | 2025-07-11 12:08:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b9578e8a-9a70-3e15-ba86-d3df42e336b7 | -6.14019 | -43.96927 | 2025-07-11 12:08:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b91d0c35-b6bc-3300-b006-2a3d420bf127 | -6.85484 | -42.79104 | 2025-07-11 12:08:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 62bba10b-9268-3946-b985-9a57a0603a6f | -3.02445 | -40.02731 | 2025-07-11 12:08:00 | TERRA_M-T | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 26.9 |
| fa7f41ff-dca9-3308-91a3-235fffba8726 | -5.43006 | -43.19873 | 2025-07-11 12:08:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3b8cca26-c4f8-3b39-9b3b-2724810fea1c | -8.81596 | -44.5486 | 2025-07-11 12:08:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1cee3d51-ba23-36e7-bca5-4168d3a33969 | -6.13843 | -44.10642 | 2025-07-11 12:08:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fdee8b76-edcd-383b-a9ba-f8771b6d1a28 | -9.9148 | -47.8282 | 2025-07-11 12:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 603de4a7-ac24-3b24-b3ef-e7615bdc67d7 | -9.42888 | -45.77123 | 2025-07-11 12:10:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0996d4a0-9fcc-3cce-9930-b838a9315439 | -10.57591 | -49.13036 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ec2bba6e-ad4a-33f5-9c65-831f074538e8 | -10.66888 | -49.49281 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| afbe1d9f-87f0-358c-8ca8-dba6f19f8b01 | -10.67898 | -49.48398 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| e9c38f01-e66c-34a6-9d70-b1706cf39ee9 | -9.53466 | -46.29105 | 2025-07-11 12:10:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5f0f2844-96b5-3eea-ab0b-6684ab3d3125 | -11.43908 | -45.10291 | 2025-07-11 12:10:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ca275d21-a2b1-34c8-998a-384b0664fa4a | -10.51693 | -46.76675 | 2025-07-11 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae5abecd-f8de-392e-a985-a76fa0442d3a | -10.57343 | -49.14565 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2a5ead7e-7466-3980-a5ed-b41766b12308 | -11.37108 | -39.06932 | 2025-07-11 12:10:00 | TERRA_M-T | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| a65cfc1b-7237-37a3-9bc3-4c4745aef657 | -9.91229 | -47.8383 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5332c4ef-51b9-3293-8a54-7842130cd04c | -12.41756 | -45.35421 | 2025-07-11 12:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 42f16be7-bd7f-38c3-b4d8-bae35ce34dff | -10.50114 | -46.19777 | 2025-07-11 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53345919-c636-3005-bfd9-8276693e1942 | -8.89168 | -47.33897 | 2025-07-11 12:10:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 652e83ee-3311-3d79-ba2a-df6f031445bd | -12.40868 | -45.35288 | 2025-07-11 12:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 47809d0f-fc69-3316-a5bf-d845c9dc03b6 | -12.47008 | -44.49671 | 2025-07-11 12:10:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 84941b3a-ab6a-3e23-94d5-9d8f10936b14 | -11.32958 | -45.22016 | 2025-07-11 12:10:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 506d8bd7-9b84-32dd-ba75-8dfb984b29a8 | -11.32727 | -51.43024 | 2025-07-11 12:10:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0f5870ec-42d7-3e81-9b43-d41a9ac91322 | -11.87456 | -46.75776 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 79b34d65-d872-3488-a979-4c541fa7ca80 | -10.68051 | -49.49483 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| abca220b-7b1c-3cda-ba83-13baba884def | -12.47136 | -44.48775 | 2025-07-11 12:10:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e516d47-3ca0-3bb5-9361-adf90473ff14 | -10.62698 | -45.23202 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5b528ff4-eb6d-3e38-9b3a-59e013416f51 | -11.15374 | -49.69487 | 2025-07-11 12:10:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6c1dd084-d353-308c-8010-c4e16e214cff | -10.69159 | -48.30979 | 2025-07-11 12:10:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 97d49314-23b4-3c8c-9d87-fcaeb2d8cc76 | -11.84958 | -46.7585 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7cddc23b-d884-3f7d-ba0a-e322ca7212f7 | -10.69803 | -48.30286 | 2025-07-11 12:10:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5f8ceeb2-e632-3d30-8117-e71794111a96 | -9.91426 | -47.82543 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| cc8c91ca-2eee-3bcf-84f0-febd7fe15661 | -12.02512 | -49.51649 | 2025-07-11 12:10:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ad329f43-facf-310c-8ac8-baa7494ff145 | -11.85114 | -46.7481 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d73b9d35-6e50-3670-a4f0-72c90a9be169 | -10.6763 | -49.50018 | 2025-07-11 12:10:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 15121e4b-9b4f-302b-9503-228c906cea7d | -9.91618 | -47.81289 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8b890c5f-ec55-390f-93c8-9b7e07a7b57b | -12.40734 | -45.36201 | 2025-07-11 12:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d6a2eed5-d668-3fd1-ba22-c9fb1553dc6d | -9.92463 | -47.82712 | 2025-07-11 12:10:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 92f09896-4a3e-35d1-8511-238b7cecee1e | -10.95884 | -45.92086 | 2025-07-11 12:10:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f28d7b4b-47b2-3bb4-8882-aca199f0acb4 | -9.5331 | -46.30122 | 2025-07-11 12:10:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f16cc17-728f-3466-87ea-2e1fc9224832 | -12.25643 | -48.78586 | 2025-07-11 12:10:00 | TERRA_M-T | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2c952e3e-c227-3f0b-bac8-943a74fe4af5 | -12.1021 | -44.73809 | 2025-07-11 12:10:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f0aa79aa-587f-3976-b872-cf77d466a0ab | -10.5143 | -46.52891 | 2025-07-11 12:10:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f5d3634d-37f9-39cd-9ddc-d44f11ae4969 | -10.69586 | -48.31642 | 2025-07-11 12:10:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a2df423f-4f69-3e75-9cb9-0151b2a53140 | -12.47312 | -46.9096 | 2025-07-11 12:10:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 063ef69c-329f-3056-b346-daebcbc6991c | -11.94545 | -46.35568 | 2025-07-11 12:10:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b08b3c93-3b4f-3f5a-baaf-aaa964cafedb | -11.84162 | -47.50067 | 2025-07-11 12:10:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4072998c-5f3d-3d99-87d7-8aef2634dd4b | -14.91079 | -47.752 | 2025-07-11 12:12:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a3c1ba96-4331-3ed0-b2ee-098026d913a2 | -12.8894 | -49.16891 | 2025-07-11 12:12:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 19dd5ed0-9bd7-34d9-8cae-d0c42796391a | -13.87759 | -44.45516 | 2025-07-11 12:12:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README25.md)
