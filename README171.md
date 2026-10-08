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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a284ed3-02bd-3ad2-8032-33eb7bcd9966 | -8.62208 | -67.00316 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03f5aac-1616-38f5-ab88-b4e84f48eecd | -3.21896 | -53.9626 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e102490b-4c79-3d70-9079-44c1ab1b9956 | -3.08101 | -53.9465 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6720d0b5-16ef-3d6a-b10a-b4efd90724b6 | -6.62678 | -43.73032 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 322efdf4-b314-31c6-9472-b454e79571a9 | -3.28719 | -54.05662 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0909b22-e211-3fad-ac03-0d830769fb78 | -4.77981 | -55.72439 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 383c7922-0021-3ec4-a992-b8b87ac3a972 | -3.63793 | -58.94328 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1af46bbd-ae51-3bfa-9f5e-92e1bc965511 | -13.80845 | -52.79215 | 2026-10-08 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54bbb19e-39a8-3ec9-8786-fee90a7073c6 | -3.57525 | -54.661 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89905daf-3389-3767-ade6-f68baff55562 | -2.69876 | -56.5384 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7292aa5-c65a-3028-a333-30ed6d73978d | -3.25203 | -57.86922 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c63c6669-1149-30fc-bf95-0b279637289d | -3.85992 | -55.99994 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a883046a-7d4d-32e3-b29b-206d425be310 | -3.2662 | -54.02934 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b19f523-149e-3783-adee-db99fc0f12fd | -3.5365 | -54.66702 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50266ee4-1f10-32ac-99c9-6bcce79187f4 | -3.51935 | -59.32091 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017d9518-12bf-3960-b2ae-8b08498fec50 | -6.25944 | -55.99578 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 19dfb34a-cb05-39c2-9a10-39d2c6322da7 | -3.51524 | -54.66756 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6795ffc6-a6c7-3425-a4d7-ec3579e39247 | -3.02263 | -54.08929 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43faf88e-e90b-314d-894e-9ee6264b22d4 | -3.11795 | -54.17017 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dc57afde-e771-3ca2-8ca3-cbe9c9a301b4 | -9.25835 | -60.87764 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe71dfa-a59d-3ab0-b52c-64b1c5a42a25 | -3.9982 | -56.25679 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f37d8e-4de8-3535-b428-7378f60ce03d | -10.98632 | -54.22113 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33390106-0810-33fe-9c98-d67788175342 | -4.08368 | -55.33435 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f6c402c-641e-3708-86ac-e9884641fbc8 | -3.08958 | -54.28361 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a876d3-324e-3a72-9edc-25bf1e2d9d61 | -1.38251 | -56.89553 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ed4f853-6bcc-31ff-8959-91ecd6ee8cfc | -3.1655 | -54.73989 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 905802a9-df7b-3a5a-a6e7-32706280d575 | -3.00684 | -54.23658 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e75009-38e0-3a8f-b325-cb1ebfaab298 | -0.85115 | -51.8504 | 2026-10-08 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1675367-9292-3e7f-a0e1-7a157d602f7b | 0.44772 | -60.53466 | 2026-10-08 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8cd020c-563c-3b5d-8260-cb5824593e68 | -2.69179 | -49.05069 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b46f2c-03d7-3998-b8b4-b4f9b37dbab4 | -3.08565 | -54.23994 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4d14c82-c976-3f7a-9e2f-24888afe013b | -3.00321 | -54.12191 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cee96bf5-0c4c-3529-b365-77a1191d8069 | -2.85535 | -59.11895 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 768b330a-ad1b-33df-b8ae-5aa2761aef3f | -2.69259 | -49.0456 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b488505e-1c88-394d-9e1a-966e17b0330a | -3.5508 | -59.47738 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0db4b63b-418e-3005-af7e-eb2275aa415d | -8.61908 | -67.01989 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3beb3bde-5778-3f31-9675-5ef8a12e608c | -2.9539 | -54.13409 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aafe7726-80ad-3bc6-8b0d-5248c9a97090 | -10.85976 | -59.11361 | 2026-10-08 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10c5e146-e0cb-3b24-a0a6-f2c31329bdf0 | -2.76769 | -54.07954 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae1529bc-626f-3b64-8636-bf961e3b66e4 | -6.73268 | -55.11893 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b0e4259-fbee-30b7-b222-86549e05ab2e | -7.66456 | -44.95181 | 2026-10-08 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b0a0330-89fb-3a1c-863a-3646f8d8d91b | -3.09556 | -53.73745 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f011209-f5c3-3c5a-aefd-0ee273979956 | -3.2038 | -50.56503 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21ec1478-f86a-3413-9d4d-3573cbf3616a | -3.01072 | -54.1428 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c220140e-b6a4-34b5-a689-b32d15748382 | -3.3021 | -53.86919 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 659c4431-3fdc-3ca7-a75d-d2a2144ff6a9 | -2.98995 | -54.06833 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6738478-ba12-3104-95f0-a82dae44ba54 | -3.01462 | -53.90804 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dba78db8-cd76-38c8-b2cd-549c2e79e9cd | -14.93528 | -48.10889 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc8e62d6-b8dc-3644-b725-504ada7350e5 | -6.73444 | -63.04028 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a8d71b4-6f91-3a9d-96f7-89f504ef879a | -10.42822 | -49.92217 | 2026-10-08 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfbb9106-7d46-3283-b4a4-c9b31e8e2353 | -14.92215 | -48.11754 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecbcf20b-3adb-309e-807f-f084e2c4052f | -14.93486 | -48.1128 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c71f5fdd-be77-3c2b-a7d9-f47f91376f8d | -8.07713 | -55.29604 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e8cc30-4d68-3f86-aab8-d26dd97c2e06 | -8.07773 | -55.29216 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939bd2ef-3a25-3142-aa5e-2659b32a6a57 | -14.93917 | -48.11195 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e834887d-697d-300c-90e6-83d37fa74ad4 | -8.08583 | -55.30924 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a469c4d6-ed93-3100-be26-e04a26446cf7 | -14.93622 | -48.10009 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 181c25d3-2be5-336c-a15e-0c69daf57cf5 | -9.89336 | -44.81086 | 2026-10-08 05:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20c05ef7-37a8-3f8b-b8dc-a61689234d06 | -8.09164 | -55.31802 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 011ae8ff-be24-3db3-9b25-fe5461372839 | -8.07013 | -55.29498 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd2f9f13-d262-322b-bc76-4bbd7eb5d567 | -8.06313 | -55.29387 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3becfe3d-5398-34cc-b8c7-81cd7c4e64b6 | -6.48878 | -62.85698 | 2026-10-08 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a3752ae-bcce-3a25-b893-132152cb82b5 | -6.99345 | -59.12625 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef105afc-be3f-3415-b31e-8f60cc1a3b01 | -8.05904 | -55.2972 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 512f5b9f-1fd1-3f44-b333-9edb090f1552 | -8.06663 | -55.29443 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b70069a-e0d5-3fd8-aca3-3f23a9b96ecb | -7.44326 | -63.54149 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b89d0288-10d8-32ff-a01b-9bd8977b1874 | -8.20211 | -54.70511 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e6df6b6-e868-3f01-86c8-5a69316e48b5 | -8.08864 | -55.31709 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c669edd-8f2c-3108-a8f4-f3e68146ecbe | -7.75206 | -54.94775 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4695e48f-1af6-3ff7-ae47-c90db03aadf9 | -14.92922 | -48.10851 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3209e643-694a-3435-81d2-36061580ae06 | -7.75621 | -54.94432 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30b7d2b-fe0f-31dc-958c-e452bf412dcd | -8.28858 | -50.26845 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c73cc78a-59aa-3a2c-9435-2fee4a5e88fa | -11.23806 | -44.87803 | 2026-10-08 05:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25fe11fd-5c96-3c8a-af89-0f806ee5d32f | -8.07363 | -55.29551 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b69449-3899-39b5-800c-7b39ba1baac0 | -8.07303 | -55.29938 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df162d0-e8fd-3db6-a98d-285e0f8c718d | -7.75975 | -54.94487 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68275a41-7be6-3d48-9345-24e2e14e4470 | -8.11894 | -55.32972 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0435d7e-f22a-3fc6-ae1a-d49271a301e7 | -8.08643 | -55.30538 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efb8e25b-fb82-3424-ad25-17a45522b02e | -14.92309 | -48.10869 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11adba50-bdab-37fa-a257-11eaca9bac9a | -7.0049 | -59.12054 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 263a2e24-2e0d-32b8-97a5-db3006ba8c90 | -7.00088 | -59.12368 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97e55a14-a887-366d-83fc-e863ac470138 | -8.60646 | -63.0671 | 2026-10-08 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56f6897a-cf90-33ba-b792-b5a144db8795 | -19.99269 | -49.09008 | 2026-10-08 05:25:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fb6dac2-2204-35d5-a1e6-165a3b3c45bd | -7.43823 | -63.54483 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 82d13c55-a08a-3df4-83aa-a80fef1f7b84 | -14.92356 | -48.10431 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ef5cf6-b007-3428-9700-2298a7a7e892 | -7.755 | -54.95229 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0668fb48-338f-3333-9212-f13715680b7b | -14.92261 | -48.1132 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdb51e3a-491f-318b-b301-cc9cb632e0dd | -8.08922 | -55.31321 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3be2007-2be9-3926-b417-26c44c87bfd0 | -14.93265 | -48.1156 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35d5f62b-e300-3191-9bc8-caa737b3ef1b | -6.7338 | -63.04414 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2390178e-6362-32eb-a86b-1f95813c19ea | -9.90183 | -44.79896 | 2026-10-08 05:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3f306c6-cbd6-352f-8eb2-6c683c3c4d19 | -9.64607 | -54.4722 | 2026-10-08 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f43d00-96a4-3d4a-b13a-7bef54a69f9b | -8.17563 | -54.72729 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 581905b6-a290-3b1c-99a5-a79ed75436a4 | -7.43463 | -63.53998 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f86b8d4-eae0-3afa-961c-85dd0c41990a | -14.92335 | -48.08978 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b640af3a-7779-3fb9-9ec1-be8e63dfc0f4 | -8.24686 | -54.6526 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9f7afc4-49e5-39b7-81e4-603cfc5e45af | -8.07072 | -55.2911 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1539b5b-eaf8-3f6a-b89a-110c7d120dd1 | -8.08524 | -55.3131 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7796aa1-6018-3039-9272-cdb406263174 | -8.2997 | -54.70158 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7851ee8e-0952-3962-a9ad-9aec7c9e0ee5 | -8.08764 | -55.29761 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README172.md)
