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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e19cd1e-e2b4-3498-92f3-21d1b9373b50 | -10.92018 | -69.41307 | 2025-10-12 06:25:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8995020d-8af2-3753-bf22-0cb3f49a6675 | -12.29734 | -64.03185 | 2025-10-12 06:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9b2fa2d-93ac-3530-a3db-a0af153c6a0c | -12.21231 | -64.37192 | 2025-10-12 06:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad035fba-4be7-37f0-9b39-9eb1e0433157 | -12.20716 | -64.36101 | 2025-10-12 06:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d78aad56-f9bf-3ecd-a7b3-48a500269349 | -12.2129 | -64.36686 | 2025-10-12 06:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d79f523-ba51-37c1-97e5-f53432ee2b3e | -12.21349 | -64.36181 | 2025-10-12 06:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24847364-682d-3294-9ec7-7a044f872a84 | -8.65799 | -70.02621 | 2025-10-12 06:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97e685e3-f34a-3b5a-a166-861ffc1ce99c | -8.66418 | -70.02709 | 2025-10-12 06:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65bde532-77fe-361c-b9a7-baa99ac3d858 | -10.63799 | -69.51785 | 2025-10-12 06:46:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd63e591-9902-35ff-b60b-d507e2b95f22 | -10.63867 | -69.51221 | 2025-10-12 06:46:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1992320-6862-3dac-95bf-15102467b824 | -10.73162 | -69.45081 | 2025-10-12 06:46:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddc05c9c-420d-30d8-ad84-5e2a4247a536 | -9.01419 | -67.43604 | 2025-10-12 07:26:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0c8dda04-ad84-366b-ab59-442902ed5cfa | -12.20732 | -64.35802 | 2025-10-12 07:26:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1d8e9fd2-2860-3c66-9d59-9bc7c3962793 | -10.63581 | -69.50792 | 2025-10-12 07:26:00 | AQUA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ccba26f9-0282-3d11-bc14-b9c275f73742 | -10.72911 | -69.44612 | 2025-10-12 07:26:00 | AQUA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14d9559a-696b-391d-8cb2-00e9921277ca | -15.2393 | -56.8801 | 2025-10-12 08:30:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 331156cd-4708-3739-b0fa-95aebb65fc9c | -10.1898 | -44.5934 | 2025-10-12 11:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ca08c885-3754-3a50-8b23-eb4a752dfc07 | -10.1894 | -44.6166 | 2025-10-12 11:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 49506286-6a70-3a3c-a980-76f69d2885b6 | -10.1894 | -44.6166 | 2025-10-12 11:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 724e5204-b986-3286-9b81-e83a27b75d3e | -10.1704 | -44.6191 | 2025-10-12 11:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2aa7bef2-d87b-3cdc-be53-adb6a17e24c3 | -10.1704 | -44.6191 | 2025-10-12 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| c5176fdd-8844-3508-8bdc-9ebf00673771 | -10.1894 | -44.6166 | 2025-10-12 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 77b10e98-b10d-35f2-8ff4-b2cd2b93fe22 | -10.7906 | -43.9537 | 2025-10-12 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| f302b565-5a00-3a85-b9ed-9d55bad01a32 | -10.1898 | -44.5934 | 2025-10-12 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| ea1a147b-ebd1-3d40-9349-b3191533ec57 | -10.1894 | -44.6166 | 2025-10-12 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 294.6 |
| 365e0268-8cfb-34f5-997b-3dc3b15b36d8 | -10.1707 | -44.5959 | 2025-10-12 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| e9e29375-003a-3fa1-bfbf-c7372b58f7e6 | -10.1704 | -44.6191 | 2025-10-12 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 189.6 |
| aff492a1-50cc-3e0b-8fc6-f630b53858b9 | -10.7906 | -43.9537 | 2025-10-12 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| ca0a793f-1bde-3369-9cb1-8245b6d18124 | -19.0319 | -57.5382 | 2025-10-12 12:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 42cd0ed4-4387-3d3f-b5bd-dc0aab2e3775 | -10.1898 | -44.5934 | 2025-10-12 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 164.4 |
| bef287bc-ba29-36bb-806d-0290b62e3230 | -10.1704 | -44.6191 | 2025-10-12 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 550.4 |
| d6a16f06-b18d-3ffa-9e54-d1ba672e9c0c | -10.7906 | -43.9537 | 2025-10-12 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| ea8e99f3-94ca-30f3-89d4-9548683aaa9e | -11.3629 | -44.0112 | 2025-10-12 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 896efbe5-403f-37b3-95b9-040caeaa6269 | -10.1894 | -44.6166 | 2025-10-12 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 673.1 |
| 430a5686-f8bf-38db-a9ed-f3e79a54ab53 | -10.1898 | -44.5934 | 2025-10-12 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 312.2 |
| fc637e80-b285-3dc1-8faa-8a7f4540feff | -19.0319 | -57.5382 | 2025-10-12 12:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 256f5f95-91b8-39d2-be22-dd7889b5ae5c | -10.1707 | -44.5959 | 2025-10-12 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 262.8 |
| a037e2f9-07dc-36bc-acc1-993a5e4b3ff5 | -12.4714 | -44.2612 | 2025-10-12 12:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| d7872aa5-05dd-3f99-9561-68b28b625051 | -10.7906 | -43.9537 | 2025-10-12 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 7f1aed13-0206-312a-97c5-d1c6b3072c16 | 1.84534 | -55.84307 | 2025-10-12 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f5c66010-acb1-3262-b455-be3a3b320597 | 1.15424 | -50.9101 | 2025-10-12 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d74cdaba-870c-3a12-ad60-a01e624c99b1 | 1.1618 | -50.9001 | 2025-10-12 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d6d1838a-70a1-3d99-8993-aeb7ce78e2ff | 0.37052 | -51.11044 | 2025-10-12 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7ac6463-e6d4-3447-b6f5-53bf9f35be0a | 0.37179 | -51.11922 | 2025-10-12 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 432f38b1-830e-316b-b075-02df36454a83 | 1.84992 | -55.87585 | 2025-10-12 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ff581dbb-cd93-3cd9-b6ba-f8b8354c63d7 | 1.91358 | -55.76063 | 2025-10-12 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| aea5a7d1-00a0-3627-8fb8-e1b4d677614b | 1.16432 | -50.91764 | 2025-10-12 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3de22832-a899-3829-844e-399e7c0440e2 | 1.84762 | -55.85942 | 2025-10-12 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8ac216f1-c10d-3aa0-b2b0-a3dab97658c7 | 1.1555 | -50.91887 | 2025-10-12 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ca9b746-c57f-3d46-8c5a-98ce397c1987 | 1.85223 | -55.89238 | 2025-10-12 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ee647a03-4f2e-3455-8d98-dbb73e73ad07 | -1.20433 | -49.26065 | 2025-10-12 12:34:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6eacd272-c1e0-38fb-a715-ad63feffb4f3 | 1.81951 | -55.83 | 2025-10-12 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 064a700d-a038-3f06-abcc-2629afa29b83 | -1.20571 | -49.25102 | 2025-10-12 12:34:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a7f9824c-1499-3aee-af68-f48dcf7f4d4f | 1.16306 | -50.90887 | 2025-10-12 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 2013eb31-127e-3a95-9ee2-38ce3193f54b | -4.4191 | -43.46942 | 2025-10-12 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| b8be07f1-6202-3ead-8296-8dc119000dc9 | -8.40693 | -45.05484 | 2025-10-12 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1c735ce2-33a9-34df-a665-c2cc790382a0 | -8.54786 | -50.17467 | 2025-10-12 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 65587b72-2895-36be-b190-e6e66b23723b | -5.27932 | -43.40088 | 2025-10-12 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 29607160-dffc-3bd3-9a93-47a619f247e8 | -6.24251 | -44.63936 | 2025-10-12 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| de57693e-e9d5-36f9-855c-9dde0171d23c | -4.82455 | -43.1349 | 2025-10-12 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4a1e0bbf-88bc-31eb-92be-4a1bced534e8 | -5.29551 | -43.37817 | 2025-10-12 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8fc7aac6-1da9-3d96-b631-8b929bfae6fa | -2.44163 | -49.36937 | 2025-10-12 12:36:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 99070aca-6105-3f2e-8c88-53a109d33c25 | -5.29665 | -44.45498 | 2025-10-12 12:36:00 | TERRA_M-T | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f0c01d25-559f-391b-955b-092984c296a4 | -4.80953 | -43.15685 | 2025-10-12 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| be81c402-9ca2-354d-8ada-1b6edc9dacae | -3.21636 | -50.21777 | 2025-10-12 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 44e23cf7-02fe-32cb-9d55-c9ac72091df9 | -5.29202 | -44.44909 | 2025-10-12 12:36:00 | TERRA_M-T | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 26af90bb-bf6c-3822-a624-058a139d28f4 | -3.65678 | -49.51655 | 2025-10-12 12:36:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6186296b-1e3b-3c21-a4b5-879d45d7f288 | -5.2802 | -43.37622 | 2025-10-12 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d7f6eb70-9f65-313a-a576-978e0888ec7e | -5.28334 | -43.37089 | 2025-10-12 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 3d754188-d485-376b-aef2-f71cd94d94ca | -3.60374 | -42.75924 | 2025-10-12 12:36:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a4ae35b8-12c7-3afb-b74c-3693f42ad5e7 | -7.50875 | -44.60227 | 2025-10-12 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 1f04885d-44e9-309b-8cf6-a8ed005e979a | -8.47062 | -46.19686 | 2025-10-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 9aad8436-a43d-359d-86c7-f2e637f72f42 | -9.06855 | -45.89238 | 2025-10-12 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 149dd3fb-4a76-3731-90ba-84abc756bc58 | -2.44026 | -49.37914 | 2025-10-12 12:36:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a884735-a737-3dee-b8bd-ff917a8d360e | -1.90305 | -51.0123 | 2025-10-12 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 347d97fe-9928-3c16-9c9a-ed6e91fd7d40 | -8.54311 | -45.42215 | 2025-10-12 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2c3176be-cd88-3bf6-8099-9a64841449f7 | -8.47211 | -46.18378 | 2025-10-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 47bc7934-a063-37d2-9518-aefdbc2e793c | -8.40376 | -45.08005 | 2025-10-12 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 55a94527-0335-3fa5-9696-5cd834b93718 | -8.54024 | -45.44484 | 2025-10-12 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 67cdb3a2-491c-3826-8970-9ba5dc6927b5 | -6.17804 | -44.86659 | 2025-10-12 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 8718839b-7541-36b8-ba4c-e6136cab8ca7 | -8.48733 | -46.16642 | 2025-10-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 59db2de4-acef-33d2-a406-a95d9f7b5f81 | -4.61802 | -45.77706 | 2025-10-12 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 30.0 |
| fcdb5570-b982-333f-8aac-522438b8312e | -8.54974 | -45.42978 | 2025-10-12 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 17e9355f-bc73-39d5-ba7b-7d60dc985260 | -8.38959 | -45.07931 | 2025-10-12 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 33053343-6fc7-3f02-8ac9-83e57071f1a9 | -15.01346 | -45.57401 | 2025-10-12 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| eb730dc4-2f04-37e2-a999-2cfcac99bd89 | -15.02498 | -46.28429 | 2025-10-12 12:38:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a757f139-e2e2-3d0b-9cf0-b4de777d3ee2 | -12.46528 | -44.27438 | 2025-10-12 12:38:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f7424241-94e5-3222-b241-7ad750545fa0 | -14.9647 | -46.69213 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b025cbe1-04ab-3e45-b5b1-edc452a35ae3 | -10.17304 | -44.63221 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 349.7 |
| 07ef02f3-d582-378e-8f15-1349782c1089 | -14.7692 | -46.13432 | 2025-10-12 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 324.0 |
| 50d8a6b0-4b5b-3a88-a9f0-9d0bb6e82058 | -14.93203 | -46.73695 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6023a0fe-229e-3bc9-8d32-67985e9fecf1 | -14.97561 | -46.71764 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 42bb4092-ab74-3186-a724-e8ec0ac3ad54 | -14.7757 | -46.1147 | 2025-10-12 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b2b7d43f-1cba-320d-9acb-5de82faad9b5 | -15.01392 | -45.56874 | 2025-10-12 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1cfea45a-72f7-3ac7-bf5c-0846edc9f7c6 | -10.19131 | -44.60636 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 516.8 |
| a7a4e4ce-36dc-3b90-973d-60e38ce5e8b4 | -14.77301 | -46.14015 | 2025-10-12 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 3c35cfd1-95cc-3907-b895-a2e6b8ea4c7e | -15.02782 | -46.25911 | 2025-10-12 12:38:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 150e2dfa-4d18-3dff-86fd-17fcc0efb1ca | -14.75497 | -46.13273 | 2025-10-12 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 83dcdd4f-78cc-32ea-94e8-f534046a4cdb | -14.97165 | -46.7 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2b036f01-1fca-3174-a8af-8503ef7b0bfe | -15.03185 | -46.26612 | 2025-10-12 12:38:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |


[Clique aqui para ver as próximas entradas](README46.md)
