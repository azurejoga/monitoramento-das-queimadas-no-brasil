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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90918d52-1885-3ca9-9810-8dedfb245260 | -12.88426 | -48.27205 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39f8580a-6a30-3759-a8b6-a8e32091d7ce | -11.85838 | -58.81537 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f749fb82-4718-36d1-8147-88c8a0ddd4bb | -11.74349 | -59.30004 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54d86e2-98df-3451-aade-f079aebe083b | -12.17719 | -53.66573 | 2025-11-01 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10084813-2c89-3331-8c73-8c6ff3d7f45e | -11.33436 | -54.38374 | 2025-11-01 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64d81c0-a820-3978-8a3f-40d185eb7308 | -15.55653 | -51.49697 | 2025-11-01 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66c503a2-8e83-333e-befb-852224ea4c09 | -11.73179 | -59.306 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8e00a9c-4e67-3f5d-ae83-3aeab7974fc6 | -13.84481 | -47.06507 | 2025-11-01 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e5cae51-3f00-3ef9-b619-07fb09635a74 | -11.97509 | -60.73054 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb441094-dbc9-304a-ac57-208b20571bea | -12.3008 | -48.05275 | 2025-11-01 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137cbf4a-fdc6-353b-8a8d-48136a9715ef | -11.38709 | -48.92989 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3162c7da-f48e-3e15-bdb9-f4a3c773e289 | -11.38243 | -48.93124 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c83b112-7b84-3b85-a98a-e78b409a24e8 | -13.21222 | -43.13247 | 2025-11-01 05:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d859dcb-29ec-32ee-8bc6-5045c6ad2fe4 | -15.02918 | -56.45635 | 2025-11-01 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5ac4b90-53b2-3caf-ba81-d44690ab389d | -12.87453 | -54.74662 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a343b8-2347-3069-b4ca-4408f10aa950 | -13.02953 | -48.2574 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b437208-ad27-39ea-bd53-679d44801db0 | -13.32519 | -60.7183 | 2025-11-01 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 111a9c65-07d8-388e-9b52-d1cb5b1ec950 | -13.02995 | -48.254 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18f8d6b3-b2bf-33fb-8756-a60c725fac9f | -18.19984 | -54.01799 | 2025-11-01 05:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da6eefb8-72ef-3812-ab4f-d5d6db817979 | -11.38213 | -48.92928 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 048610aa-5e5f-36a7-ac61-15be92e01dd6 | -13.72348 | -51.45673 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6ed1e50-f1b4-368b-b21e-81ecaf96dba9 | -12.08811 | -47.88036 | 2025-11-01 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a2bc056-7e14-3c33-ba0e-b01e701c4cf8 | -12.30135 | -48.04834 | 2025-11-01 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2be4f44-f034-346f-8f5a-4ed438ff5b3f | -11.38313 | -48.92568 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 502591ac-e5eb-3aa0-93d6-fdf1492432d3 | -12.88994 | -48.26951 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35182057-9fac-38a2-b461-cab9f681d6ac | -11.97597 | -60.73384 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d7a269e-50ac-32cc-b31a-7fa4d2e23659 | -16.19572 | -56.60058 | 2025-11-01 05:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2ad64cab-ab9c-3a36-b895-ac1b1d11f9ed | -12.87394 | -54.75061 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cff80ab-27a5-3805-930a-9d8a8dceb838 | -13.71917 | -51.45613 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1e5bca4d-e22d-3bb1-b83b-99a5a4590762 | -12.02293 | -63.75478 | 2025-11-01 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba2fb3fc-0934-34f3-81db-e44ae46c8370 | -15.02862 | -56.46006 | 2025-11-01 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee2b0b3-33b1-3d86-92c6-42f81365735e | -11.73141 | -47.46745 | 2025-11-01 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41052a6f-642c-39f4-8d3e-0f158a2e7a88 | -21.77009 | -55.95694 | 2025-11-01 05:12:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f4407b-1085-3d4d-b676-48f33cfecd3c | -21.16172 | -57.42915 | 2025-11-01 05:12:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36b7e4b-1292-3dcd-a129-ec6ca45d292f | -3.234 | -50.5789 | 2025-11-01 05:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bc44f172-f72a-3a35-a781-d380e1c00adf | -0.42897 | -51.76209 | 2025-11-01 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf3c077e-66b6-3ca6-81b9-33c8b8d7fc7d | -0.42949 | -51.75885 | 2025-11-01 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93cffe6f-77c0-32bc-9037-df5b33897065 | 0.84854 | -59.82467 | 2025-11-01 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2d19e97-d1e9-36c1-86dc-1ccef187c87c | 0.67892 | -56.87165 | 2025-11-01 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bda04712-4315-3d08-9d90-39a6e84d940e | -0.43373 | -51.76615 | 2025-11-01 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 862538bb-4672-3a1d-8a25-b9d04a48ce8d | -0.439 | -51.76694 | 2025-11-01 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca33b28-a146-367c-b9c8-6b5edbb2be99 | 0.84523 | -59.82518 | 2025-11-01 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28abf823-6a8d-3374-945b-be4ec03309f5 | -3.06528 | -51.2543 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45435151-4184-393c-8da7-29d61815351b | -4.64647 | -47.95876 | 2025-11-01 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1969615-4503-3b5b-9e87-60fcf9610b1d | -3.2301 | -50.58175 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 85995518-1899-329d-8a52-d40d2739ec14 | -3.22289 | -50.58951 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79768571-8ffc-3f3f-83ad-05370f7977a3 | -2.46616 | -54.75418 | 2025-11-01 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d42d5af5-8112-32cb-a7cd-c539d429f767 | -3.01795 | -53.9656 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac34f274-bea1-3ca3-ad2e-edc7c79ac033 | -3.60459 | -50.6264 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd18e728-3833-3967-a451-3a53c0d5df22 | -3.23541 | -50.58694 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddc29f6e-09ec-3d9b-8761-c44a027abf35 | -2.97597 | -50.38499 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89e2d8c6-8e92-3343-8d93-1ecb9ace4b6c | -3.22353 | -50.58516 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c6566e49-5876-3c34-8ab6-70dbdebd1f99 | -3.60396 | -50.63062 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e667b7b2-754b-336f-bb92-fad71c636615 | -3.22415 | -50.58084 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bb0f3349-419d-3361-82f3-1d46ddd2aace | -3.52782 | -53.0008 | 2025-11-01 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cf60128-3b9c-3bb5-b8a1-8138df9fb0cc | -3.01722 | -53.9706 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caa7d2b5-5bb3-3b65-b3ae-42a6ab641dc1 | -3.22946 | -50.58609 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 382f3019-2467-39ee-815f-339a62ee90de | -3.15829 | -50.82724 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 486ffd79-375f-31e7-8ba9-7940652f728f | -1.85328 | -54.54966 | 2025-11-01 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9e14212-5779-3551-ac5c-da7ea874249c | -1.25937 | -54.09571 | 2025-11-01 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a52c84d1-167b-373f-a8a1-84e8f209183c | -3.66571 | -51.71697 | 2025-11-01 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49eb6d6e-40d0-3faf-bef8-e0ddcf8617d9 | -3.01564 | -53.96907 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea86e1e6-3d3b-34cc-9aef-a8d73f68fea4 | -3.22883 | -50.59043 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 789cb220-4fb0-34c8-82c5-4aac6138e185 | -3.22002 | -50.58646 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33f1c15c-60f3-3878-aa93-07831811b4a7 | -3.48879 | -52.35606 | 2025-11-01 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453ddc57-bf27-31d6-b6bc-c24a68044665 | -1.25864 | -54.10034 | 2025-11-01 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20fa1bda-af6c-3be7-987f-a25ffe155a05 | -3.15769 | -50.83141 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88cbabea-e71f-3fb8-ab18-65fa1868cb36 | -3.66659 | -51.71768 | 2025-11-01 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36744e5c-be38-360e-b8c6-9d6d57061476 | -3.03796 | -53.79616 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c7a9f82-da88-3a46-ae21-989296674342 | -3.15895 | -50.82895 | 2025-11-01 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f7f62a0-db84-30e6-93bf-6e56957d1cb7 | -3.48831 | -52.35934 | 2025-11-01 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc1ce1c9-24ae-35a5-953d-a1cea83cb5d8 | -3.07096 | -51.25513 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d0ef1d-9e5c-3a7c-9641-c8301936d205 | -3.0377 | -53.79502 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cbc3aa1-9eb0-32b1-99cb-07b3594835ef | -3.65711 | -50.18981 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0305e61-3fd0-3dd3-b579-9aff38f220af | -1.84813 | -60.0069 | 2025-11-01 05:27:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d29e9d0d-98a6-3687-ba66-7d0e0276743a | -5.14667 | -60.37397 | 2025-11-01 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d398ee83-6355-329a-a6bd-dcef750f3b3a | -3.53289 | -53.00166 | 2025-11-01 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5afc1ac-9f93-330b-8795-afd941c9599a | -3.02035 | -53.96979 | 2025-11-01 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e6f9307-380c-30ad-9710-0a4504db4d1b | -1.20192 | -54.16634 | 2025-11-01 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe02913-9d23-3b19-8e8f-bfd7e3a79597 | -3.46805 | -50.9435 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ac1666a-0a08-314f-87a3-077696742a8f | -1.82135 | -55.36076 | 2025-11-01 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6b20bf-7da2-365b-aaed-d14de46423f5 | -4.2736 | -59.65689 | 2025-11-01 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5003002f-d40b-3e76-ad9f-5ec7fb5140d2 | -2.92619 | -51.46635 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 477ea973-617d-3c04-9ddf-969fcc20db0c | -3.46869 | -50.93928 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97bf992c-c5b8-39f3-8f9a-3f8191f1fc06 | -1.85397 | -54.55218 | 2025-11-01 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29af4f01-d640-3657-bff9-956d5e58d283 | -3.07156 | -51.25116 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5869e1e-2732-3bbe-bffa-c65da96ac096 | -3.65645 | -50.19432 | 2025-11-01 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9586f2f7-b127-3bc0-842b-f78c66c50e4b | -3.07215 | -51.24722 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ea025c-4dfc-3ce3-9f4d-fcac07f1468c | -3.07605 | -51.25983 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15198428-76a6-3e31-864b-904d8de9a299 | -4.63922 | -47.95874 | 2025-11-01 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ecc387-7534-3f12-b543-66e5c1a4e75d | -2.05011 | -52.0783 | 2025-11-01 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ef26c39-33b0-321c-8799-8111e174f253 | -2.04482 | -52.07748 | 2025-11-01 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16c7cf7b-8943-3f44-8d78-0fc1a5fe10df | -3.06588 | -51.25034 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0715f9e-2eab-3f48-9c3a-2217860f39e5 | -1.54264 | -55.40278 | 2025-11-01 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b30b24ba-63fd-3ebb-95ab-69a04fedb9f4 | -3.07783 | -51.24811 | 2025-11-01 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f15a01-8d3e-30cc-acdc-c2261429dfba | -1.78131 | -55.53398 | 2025-11-01 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5778712d-fe08-3ec5-864c-5e90a684f75f | -11.73696 | -59.30969 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e6bb651f-fbe2-3495-adaa-462ca9289c38 | -9.92546 | -65.27846 | 2025-11-01 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a733b3a-8fae-3746-a886-2ce4334fe0d4 | -8.86148 | -49.8814 | 2025-11-01 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99279be0-3db2-30bc-b1fb-f0a310972a78 | -12.02494 | -63.74862 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
