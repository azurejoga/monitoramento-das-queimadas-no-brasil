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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b284303-1860-3ecb-a710-f56a51b716b9 | -13.7296 | -51.45485 | 2025-11-17 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5957dec-fa1e-3b0c-a3aa-d6d697c82b1c | -8.83215 | -47.36437 | 2025-11-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09eb41e4-4312-3528-82e3-d50cf4b75f4c | -9.74624 | -43.9673 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23c929cb-a709-3fbc-b6c9-a4c1cbed72e0 | -12.80169 | -46.43698 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4528ab64-0270-3fcc-a851-88351abf916b | -15.13621 | -43.74722 | 2025-11-17 04:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b5abbf7-9720-37a5-a720-4759fca471c4 | -11.70794 | -48.86656 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d5db3b86-e729-3e5a-b70e-d1eb1277e404 | -12.41411 | -48.09632 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62354600-4d83-3130-8165-6eedc459fbc6 | -11.16124 | -47.46438 | 2025-11-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 795498d3-f0df-355e-8b1a-56f6547725a1 | -11.82343 | -47.5857 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c0227ff1-58c9-3ad9-99e2-56f932d52dad | -14.85893 | -47.37572 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57e21f1b-3b60-38e8-9e02-bf95276ef2aa | -11.84091 | -49.20991 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 78b6fedb-b596-32a6-8b6f-afee3af1f239 | -13.73291 | -51.45539 | 2025-11-17 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 136edfe1-01c8-3f54-a7d7-c590f70c05bc | -12.8068 | -46.44111 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24191351-7509-3dd4-b3ca-e95e1624f786 | -14.63641 | -46.56247 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ba5dcb8-cbaf-3b6d-8142-34a2fb6946c9 | -10.6376 | -44.60604 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adf685b3-32e6-3988-980d-062c24a6acc4 | -13.27749 | -47.29409 | 2025-11-17 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ce00388-89cb-3f43-95b9-6165ed4a7970 | -10.31129 | -44.27864 | 2025-11-17 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3cc3b6a-8171-3828-bd54-ca1a3a3b86be | -11.79173 | -45.2991 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ff003a9-74ab-373f-828d-bd0557f88bed | -10.5364 | -47.91864 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a816c6c-af3b-3333-b019-8c60b9bcb4e6 | -12.86843 | -46.43727 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7079bed-896b-322c-bef5-3dcd0872213a | -10.53948 | -47.91072 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03d62896-2a3d-339b-a5ad-e1386588e2d0 | -11.20461 | -49.41302 | 2025-11-17 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb6c8612-be15-3b87-a98b-1646342d8123 | -9.32726 | -46.57502 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11c0a557-e85a-3887-b112-a4b5a6ef8fd5 | -11.06044 | -45.15161 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55860fed-e628-3f36-84f6-c13ce2308dfa | -6.80229 | -59.1399 | 2025-11-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d74a5d6e-3615-3ccc-9b46-882500951ab1 | -12.86803 | -46.03394 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 574cfc36-0335-3b7a-8820-246771895ca3 | -12.80556 | -46.4374 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e814d4a1-c048-30e3-b552-aaffe8ad04df | -9.32743 | -46.57203 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| baea3bec-7bc1-3b17-8e6c-eb078a9a24a8 | -12.33462 | -43.65341 | 2025-11-17 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2719d824-0a56-36bb-8e6e-b780985e3467 | -11.00572 | -47.95857 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03421e2e-d0d0-3035-9dbc-dba2f3c19e80 | -8.86686 | -50.1901 | 2025-11-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62f2c5a4-7be4-307e-ab8f-4734a13d62e6 | -11.71189 | -48.86337 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aff924f1-a29f-348b-8ce0-a99cc1fb685c | -11.96845 | -44.30109 | 2025-11-17 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56a17836-a326-3068-b193-ef526375e3dd | -13.2818 | -47.29029 | 2025-11-17 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82809505-8c69-3669-8b58-064440123c51 | -12.21108 | -49.61113 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f576136-a566-3b28-a1fc-391f38c9d645 | -12.87778 | -46.05114 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08edc0c8-9819-3a5a-b0cf-0bb4d4a3cf18 | -14.69602 | -46.59494 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5ea379b-307c-39a7-a4b4-853f27f6011f | -9.85316 | -44.19403 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3acebaf1-a486-3f0d-99f2-52d785bb8354 | -10.53236 | -47.92189 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f5e8844-904a-3f94-be78-b32494b7aecc | -9.65683 | -43.89652 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddc3ac11-41bc-3cfe-a3cc-6e2064ff85ec | -14.85952 | -47.37144 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbbb1488-1688-35b8-92f2-cb96c5558cac | -10.15436 | -44.50827 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 397e5287-1203-3623-91f3-efe677fc6f66 | -11.34096 | -48.90104 | 2025-11-17 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eed37bc-77b7-3f30-b371-f24f0e9b3686 | -9.65393 | -43.91745 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7deb7bc-cba2-3161-b1dd-8cd3e662ffef | -11.20516 | -49.40944 | 2025-11-17 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e20f0760-dd93-32a8-a8d9-d22a02ad3389 | -12.22499 | -49.60965 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a31b4c6-714f-3c5c-8df1-553bba675f38 | -9.73816 | -43.96186 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3266113e-1c9c-3c63-bed8-e5d991a42ce8 | -9.33154 | -46.57125 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| babe8f52-287e-3082-a0d3-f65a01600a19 | -12.09657 | -53.27625 | 2025-11-17 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a501a193-ae9c-34a7-8a05-e56e7752356a | -12.81068 | -46.44142 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4baf0490-b150-3d0a-975b-80642f724e8e | -10.85398 | -46.74154 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eb663ae-bd70-329a-9280-a53a9a06d078 | -12.85157 | -46.47368 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 20116b73-5365-376e-a4c9-40c71ad48ff4 | -14.64612 | -46.55094 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3a5afd1-b8ee-3bef-8672-d130299a1a96 | -11.62507 | -48.48233 | 2025-11-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 739c8cbe-456b-3989-a018-76d15099dd50 | -9.44246 | -59.20769 | 2025-11-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a26a2da-8ba5-3a06-a18d-67cd303eb784 | -9.51603 | -47.26747 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af9f7e3d-24ea-3a1d-a94a-5ea42f14d18b | -12.87454 | -46.04541 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b85b666-afe5-301a-a025-c085b174c0ec | -11.95603 | -44.94115 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b9ffae9-cac5-333c-9d98-d4004e19e6da | -10.8604 | -44.09266 | 2025-11-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63505ecb-3bee-3eec-aa4e-16aee195eeed | -10.85271 | -46.75044 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102aa3ea-9c06-31d9-b5fb-b33352e3a2e0 | -9.41138 | -48.45013 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a33c4e97-96b8-3723-afbb-f03b5606d187 | -12.15743 | -55.42534 | 2025-11-17 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f1266da-c0fc-3eee-b475-7c6276595abd | -11.40624 | -43.32365 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3304def7-7c1b-37fb-bfbb-a05c4db32226 | -12.32479 | -44.22046 | 2025-11-17 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d044162a-ed7f-39ca-a2d0-edeaa2c70a02 | -11.78789 | -44.65018 | 2025-11-17 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3be64b45-7529-31dd-9234-85aff3b1dbdf | -12.79906 | -46.44033 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c4f0ae2-88eb-3ba7-9b1e-55562f6cd8be | -11.30126 | -48.51535 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b91b75d2-da2d-37e8-b17b-936dd53ea4ad | -8.87017 | -50.19062 | 2025-11-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0fd9426-529a-3ee9-9a56-172949e0de3c | -9.57574 | -49.1112 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d16516d-bae1-3cd1-a8f0-fe382ea23fbf | -10.53538 | -49.52241 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1cd9acc-3f91-3a50-97af-2d06e0a651d7 | -9.73211 | -43.97384 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bddd9a9-406f-3d07-8083-3014f38f1d0c | -12.40218 | -47.58516 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abfc1b78-9625-3b70-849e-3bb987dd8570 | -12.19465 | -54.26851 | 2025-11-17 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086a058d-ae2d-3131-a152-1266c7e7318f | -10.16637 | -44.52068 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5017aa6-ae07-330e-aabc-cf912311b0d0 | -12.48083 | -49.7785 | 2025-11-17 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09ce3822-42e3-31e5-a3f0-902449f1bb2c | -10.79477 | -47.64568 | 2025-11-17 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 947d6d5b-fa7d-32c9-aa00-83f9462b47d5 | -10.31394 | -44.29125 | 2025-11-17 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92287752-0f2b-34c6-9595-e92ee29f642e | -11.99476 | -52.47112 | 2025-11-17 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cadac70f-3726-3fb4-87b4-e17b06a95cec | -10.92588 | -48.68009 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66d21ad1-b02f-3f43-bdfd-6388c707b33f | -10.71391 | -44.5237 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6404ab75-a172-36e9-bb53-7f16bc89b1dc | -12.85741 | -46.45996 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842827be-75bb-39b7-a239-655a30b97b94 | -11.95199 | -49.85933 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5024b6-bca4-39e1-a33a-f95de62089f6 | -10.6527 | -48.16676 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f56825-c6e1-3784-b6ad-681853c78ddf | -12.33498 | -47.77077 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133f983f-927c-36ab-a9e1-92fed5a7886c | -9.15435 | -48.06397 | 2025-11-17 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77d0c733-7ebc-3181-bc77-9321debf3f35 | -11.04363 | -49.59911 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 214a6d28-8e82-3fac-9c4c-ee09bef163e8 | -9.33092 | -46.57557 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72cf739c-5859-35ff-b103-9fc27b81b3bf | -11.71114 | -44.44918 | 2025-11-17 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eefa9a99-e64d-3dbf-8f24-e0079b9f7042 | -11.01021 | -47.8555 | 2025-11-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f37d76ad-6c70-353c-ab2c-d7b0c1789e2f | -10.95022 | -48.67987 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bd072430-afc2-3ad6-803d-cc7f1083bac8 | -11.84036 | -49.21354 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 336ad89c-7b2d-34c4-bce8-d9870321d980 | -10.85767 | -46.74211 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8185442a-31ee-3b0e-bd79-f96b2a3fa07a | -12.22443 | -49.61324 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18d4813e-f019-3858-8bc3-dba4ec8f527e | -10.78873 | -44.32432 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df599173-9028-3fc2-b053-bdf5f42d4537 | -14.65197 | -46.53713 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2eb5d00d-28a2-3bee-9459-756b9d951a0d | -12.70126 | -46.77474 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 33df954c-454f-3a4d-ad83-9148c2348003 | -12.63828 | -49.13688 | 2025-11-17 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f0ba4e-5fb3-3f1a-af41-021ea66fb1e4 | -12.67249 | -47.16452 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddf08ff0-2a9e-3815-9503-2afd65603698 | -10.54366 | -44.92081 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35252310-17e8-36f6-aebe-2d34125467cf | -11.83981 | -49.21716 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README35.md)
