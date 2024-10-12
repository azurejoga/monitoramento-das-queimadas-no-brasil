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
| ada593fe-cbcb-379d-9f55-8f00badf6f28 | -11.82866 | -58.84656 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 25d3675f-305b-3a8b-9c2e-50a42d386597 | -11.82793 | -58.85086 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 524a1ed0-0397-36d8-a2a4-6757a0cb3dac | -11.8272 | -58.85518 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1afc57a4-ac12-32b0-a8f4-d596230a9e43 | -11.82575 | -58.84164 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4d045301-1575-3302-9d13-ea8aa1e9b5dc | -11.82502 | -58.84594 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| db733104-690d-31f9-969c-2b49116c37ed | -11.8243 | -58.85025 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca744d02-b090-364f-8b10-cf5462187e71 | -11.72221 | -59.29315 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 366166c6-de1d-37d6-b34e-6c60838a5875 | -11.72006 | -59.28335 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| babd498a-0497-380f-871f-ff70056341d2 | -11.71928 | -59.28791 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c931e614-0569-334c-8e62-0f328e88a167 | -11.71848 | -59.2925 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79344820-b5b7-324b-b609-2721dd544ae7 | -11.71712 | -59.27818 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e9ef381-39d7-319f-9653-05c7c8915170 | -11.71633 | -59.28271 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a6ecd0-ff86-35c5-903f-5e304d102033 | -11.71261 | -59.28209 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e14913-f3d2-3eef-803b-8b87a57efe02 | -11.66611 | -58.89639 | 2024-10-12 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81d1cada-2a58-36d9-8fbc-997a6a23191b | -12.96102 | -60.05714 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 320e839c-d39a-3ff1-9cfe-c092f121d339 | -12.67663 | -59.83149 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6c5f5ae-ab31-3bd5-a202-10967258dc35 | -12.67526 | -59.81666 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9a1f4c1-b7b7-371d-a11b-9447a0b44a34 | -12.67147 | -59.81598 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455861d7-bbef-3689-a9dd-0449ad771a1d | -12.66075 | -59.833 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1ba94af-0714-3a68-9ac3-9891d35004d6 | -12.65778 | -59.82751 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0426c03b-84d9-32e4-a0cb-59972af34859 | -12.33841 | -59.87566 | 2024-10-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40101f31-374a-3d40-8056-7529e98a7f0b | -12.96565 | -60.05308 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2190a08c-04e7-39c4-9c50-0b779738bc15 | -12.96483 | -60.05785 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78477c2a-05af-34f7-97e3-b74b92e2f4e2 | -12.9602 | -60.0619 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca786d22-9e53-3d95-ac77-2c4f4bf06634 | -13.74327 | -60.12263 | 2024-10-12 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| beb23521-158e-3a4f-98ce-6254b171b4fd | -9.35025 | -60.576 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a62fa8-991a-388b-9146-f424977fca95 | -9.34957 | -60.57988 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcee924b-4b94-3916-92c0-c899278a86ef | -9.28815 | -60.37954 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6cbcb2b-3cd7-3c0f-abe1-87b288380ef5 | -9.28423 | -60.8049 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dee6e46-1945-3e2f-81fe-3dbbdf559b2f | -9.27268 | -60.27266 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd10793-3e02-3046-9bef-a319ed6cd5d3 | -9.26795 | -60.82266 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3de742c5-7114-35da-9477-10ddbe35c85c | -9.26792 | -60.27574 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93707e30-5ba8-37eb-9455-b04ac4bcbdb9 | -9.2644 | -60.8179 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842d3942-7390-3528-b352-77cb9d098079 | -9.26369 | -60.82192 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dcf18d1-396a-33d2-af34-a1c02e163418 | -9.23574 | -60.36272 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f725b20-84c2-3efd-b7ef-738f430d1043 | -9.23508 | -60.36648 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a289296e-0ff4-340c-bf9c-dcf0f7e4e783 | -9.2316 | -60.36206 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d828809e-c1b5-35f0-a28d-89758c5ef9ae | -9.23094 | -60.36581 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22e2612b-e465-334c-996d-a39a09e65a36 | -9.20415 | -60.79083 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0eaa262b-8746-3e94-9328-85e9336c3df9 | -9.20345 | -60.79484 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7320ad21-40d4-39ef-87d3-89d8a35aaeba | -9.20275 | -60.79887 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fcf76f7-c108-3793-bf0a-f59d15172578 | -9.19829 | -60.69919 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03c7d613-40d9-3852-a594-c8ec24a72db1 | -9.19476 | -60.69447 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df75dd1e-cab2-38f4-af3e-1b72d18e87b1 | -9.19407 | -60.69844 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc30f60c-08ca-336c-8094-66408ba794a3 | -9.18984 | -60.69769 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 850079d6-c6bd-3fe0-bc4a-8693df0b5752 | -9.18914 | -60.70166 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc38a9c0-755e-3907-9670-676e0e85d7fb | -9.18284 | -60.76239 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d44961b5-6f95-3a79-b9d7-f11052cdb96f | -9.17901 | -60.35717 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7bb87c43-0872-35dd-a9c1-19cdc4c19a03 | -9.1786 | -60.76167 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8467dc1-e8b5-338e-b26c-032deebf9207 | -9.16007 | -60.39285 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f172b23c-b889-3d5a-a8cf-88358354e776 | -9.15942 | -60.39664 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 979ccafc-d7b1-344f-9904-78dfe9fa8e72 | -9.15592 | -60.39218 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17dfe34d-f133-3a1d-9269-a843f2c4d925 | -9.15527 | -60.39595 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f55d7c23-a681-3eb2-b5fa-5873128ea250 | -9.14392 | -60.66184 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a646b733-014c-3f04-ac7d-96ee7e8576fc | -9.08124 | -60.62251 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbbf3c61-94b2-3f69-adbb-c9d0343f9cd3 | -9.08048 | -60.57771 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b4ddd91-adfc-35dd-a82e-8102ce4dde5d | -9.07978 | -60.58163 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f57bfc-e86b-39bb-aef1-cdfcd6720fde | -9.07969 | -60.57832 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87a77453-9f82-33b3-8656-b462f1cb7dd2 | -9.07902 | -60.58226 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 443d839a-06c1-37ec-aea9-0b232e414112 | -9.07766 | -60.56917 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed55d7f9-3f28-38b6-95c0-f9de41b3c59d | -9.07681 | -60.56976 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 280b125a-b444-3578-b95e-d32d8a87260f | -9.07628 | -60.57698 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f33a443e-9af5-39ac-941e-b00106c6dac5 | -9.07559 | -60.58089 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d3d3c96-854b-3af4-8593-48c857c086eb | -9.07549 | -60.57758 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1b05b00-7724-3156-b217-7a9f4a37e866 | -9.07482 | -60.58151 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6e2736-a88e-3f4f-8d42-c4bfcc51484f | -9.07346 | -60.56845 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3df678f3-42ea-3dca-958e-1a966f0ad0e0 | -9.04937 | -60.45294 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0d89fa3-840d-3bf8-a8f6-43c7f5fb5f9a | -8.80003 | -60.15255 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7da064f8-ce1e-369b-9932-ca08dcd0ad63 | -8.79725 | -60.14402 | 2024-10-12 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7743bb90-0fa5-3878-9cf8-595a252d6701 | -8.79595 | -60.15166 | 2024-10-12 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b8ad838-cf32-3be1-97f4-dd8f05e98e3e | -8.79529 | -60.15558 | 2024-10-12 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82b4baf1-a7e5-3054-b43f-2645ddaa4ba2 | -8.79055 | -60.15863 | 2024-10-12 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e82c5f81-af1d-3a36-ad86-7683558edb24 | -8.74778 | -60.48563 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48d1af8-f00d-3904-ab5e-24b19c39945c | -8.74358 | -60.4849 | 2024-10-12 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7c2c55-3eb8-314e-ad49-216147141571 | -9.23007 | -59.74797 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7161c73a-c307-3f6f-bbc2-f92f9d0453ba | -9.22947 | -59.75143 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b6b29b-43ed-300c-bebb-55882e92cc5a | -9.2261 | -59.74731 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a08f4314-dbfc-3c53-b278-3f2cfededeb6 | -9.21791 | -59.7708 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00398ab1-e7e5-331a-9b01-01b3a05283ec | -9.21554 | -59.77021 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 073ea29d-5c9b-3d7d-97da-b071ff404ee8 | -9.21495 | -59.77369 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f966dbc6-325b-3037-a5ff-ad1ffc707d18 | -9.21394 | -59.7701 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff9e64b-028b-37b5-96c1-fad6a854b49f | -9.21333 | -59.77358 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 269ef450-ef11-3c7c-be81-ca60b82fca69 | -9.21097 | -59.77301 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa7d6c02-347c-36b7-95b0-060d261cce6c | -9.21038 | -59.77652 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a002f519-5903-3c94-af5b-595dcd8a3ad7 | -9.94845 | -59.79578 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78503665-d69c-3be0-8803-cd47d1de3dec | -9.94363 | -59.80027 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8eae036f-3f50-3f39-afe4-63ff09c32e41 | -9.93218 | -59.93985 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f0fc4cba-dc77-36e4-b57c-d05cd56882a2 | -9.93072 | -60.17272 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c537a79-56bb-313f-8ab3-02cc6319318b | -9.92669 | -60.17199 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b1e20f0-6da1-3d05-ad8b-94bea1852258 | -9.92618 | -59.90297 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e26bba7-0d2b-3f91-8d32-dd13677cdbf8 | -9.92565 | -59.83427 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ec02fbf-842b-36c3-a870-9ce247d07a14 | -9.92423 | -59.93848 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19f4383-7b8c-330d-89e5-f7af1bb59ef7 | -9.92202 | -60.17486 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6795f40-aadc-33d9-a803-4d22895880bf | -9.92102 | -59.90926 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 97797d3e-9132-352d-adfb-b48e4c8c507a | -9.92043 | -59.91275 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6d6a0ca-873f-320d-aecd-ae3b5f2f426b | -9.91081 | -60.72797 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3483d15-51f7-3cf6-a315-8ffd19a24db6 | -9.90665 | -60.31018 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53932c00-4d2e-370c-9d23-e57c97a3d88e | -9.88983 | -60.21394 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fce043e3-ff4c-3933-8092-e50caea89273 | -9.8862 | -60.82089 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfa5e116-a53f-34fe-8db2-d3865e6fb2ee | -9.88578 | -60.21324 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README80.md)
