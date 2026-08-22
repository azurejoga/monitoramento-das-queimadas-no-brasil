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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ee2ba01-e44b-3439-b163-da481b5b8d55 | -7.60991 | -60.97293 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 606c7969-80f2-3f97-be34-0a4b0322e1b9 | -13.98546 | -53.68101 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b45d1394-8bc9-39c8-be60-6b71aab459da | -6.74325 | -58.57898 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef561db5-5d56-3909-ab1a-ec1ac633804e | -6.89077 | -56.43243 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffdc436c-e2a4-3174-97c6-e203cad99429 | -6.11157 | -59.92937 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f92c8af-1eeb-3e4d-9b33-fc88a42c37ea | -6.93651 | -59.31347 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c10a7b4-4c83-36f7-9d7d-0867b0a37c84 | -14.00855 | -53.7109 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52c86471-6f5a-355f-8d2b-fd6bc6a87739 | -6.36982 | -54.94678 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fec4570-1f45-3c07-82ed-61f445f8105e | -6.25944 | -62.51964 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 364071fe-7143-3ed4-b19e-ecf058406965 | -6.92714 | -59.30844 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54fd403-ffa0-3a86-9e49-c99f662c76c1 | -8.54036 | -54.86132 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25a15f8b-2309-320b-a324-b182e2051ddc | -13.38315 | -54.36983 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33da7b5c-b01e-3084-8499-a879bf775fcf | -6.89251 | -59.03337 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258d36e8-8820-3386-985e-4d8693b9a811 | -13.99137 | -53.67201 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33d1eb3d-d5f8-3f41-bac9-26699567f9b5 | -6.37067 | -54.94909 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d68684fb-bb00-3909-9b34-0a56769be2cf | -12.84446 | -48.45928 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec3f7edf-7b7a-3c7a-a143-214e355f6e6e | -6.66645 | -56.33832 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1121fb70-cf42-32e7-ad2d-d59a27353c2d | -6.10877 | -59.9469 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e4e4dc8-4231-3df1-b33d-c1e00ced4a4d | -2.44899 | -48.56511 | 2026-08-22 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58ab45d7-7948-3d2f-95ce-b0b7f86d97f7 | -1.74528 | -55.25221 | 2026-08-22 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a8460c5-3eb5-3f99-907c-aa1dc453602b | -6.01334 | -57.79835 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7502a47-3c01-31ac-a0fa-76be0d23d27e | -8.55692 | -54.85066 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdca0ce8-93f8-3b52-8de0-e477e48cd650 | -6.81908 | -59.4118 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b1cb7c8-b3ff-3039-9e10-f107c58481f5 | -6.76269 | -59.4663 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eef32954-3396-3885-b8cd-fd89282a13e9 | -6.90029 | -55.71152 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ecfa1882-8a6f-3228-8819-044df0498d8d | -6.60398 | -56.36642 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c035209f-35a6-3db6-9537-3b7b5aca95ab | -11.47196 | -54.31907 | 2026-08-22 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b39be2e-a33b-3ff8-8401-6017a5320f5f | -8.62738 | -54.70026 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b098b17-2016-3d66-83f2-64cd0a7531ed | -6.76439 | -58.66084 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 271020c1-53bb-388f-b779-d802e608ec5c | -14.42816 | -51.8017 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddc66c55-cd74-391b-97f8-92459cdeb9cc | -6.96429 | -59.05184 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ddcbcb1c-d52f-3cef-b05e-e1d2044bae21 | -11.16191 | -54.02872 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eddd310-ac80-3e98-897c-50e2e7879257 | -11.16135 | -54.03292 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3b20bca-f048-3544-a93e-8e40a29a6f43 | -6.14044 | -59.89808 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d48ff76-e7dc-30dd-bf51-36b5fd783210 | -6.09716 | -59.91275 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bffa9d-2c23-3cbb-a2a0-d02a623362bd | -6.7633 | -58.6678 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a670c28-ed35-3ff5-b43e-c78a5c38e855 | -6.00104 | -57.81105 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da08bbb8-80e4-34ad-b021-bbcad60bf814 | -7.34134 | -55.70136 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c1f6f45-8830-37d4-947b-0a4c35cc9b6c | -6.76941 | -58.69371 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a74baa0-3fdb-3b3c-8bc6-6337d1068d09 | -7.25319 | -49.91798 | 2026-08-22 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42826760-c255-3762-97ca-16dfad775a9c | -5.90687 | -61.29372 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3484a14-2cc3-36eb-9e1d-45db5e8222b1 | -8.51328 | -55.32088 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54f872a4-a3a5-304f-9599-a0dde825234d | -6.37156 | -62.90765 | 2026-08-22 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c533ba81-5f12-3756-950a-422e9f4bb866 | -12.93918 | -56.62387 | 2026-08-22 05:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 55e4c6ce-3adf-308d-bd9c-a43cd6a2f948 | -6.9079 | -59.00031 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 41b7e6bc-aca2-35b8-8597-814677c516ee | -8.49924 | -54.86573 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57ef1ec2-88dd-31b0-9291-b80e0b331dfa | -13.3881 | -54.36614 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6514c4f9-9d29-3c65-8b75-db832daf9c3f | -6.68778 | -59.10348 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8a11bd-29f1-3818-8e8f-8218a89875f5 | -3.15559 | -51.10138 | 2026-08-22 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1488e7e-298b-31bf-9aba-c7ea70a56ea9 | -12.79772 | -51.48324 | 2026-08-22 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ba73bde-bf3d-3f57-a14c-b7a7be28a54b | -13.82679 | -53.99771 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| def88aaf-5ed2-3a6c-a04f-003da80e112a | -6.78712 | -59.44221 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0a6699c-8810-35ed-8eb3-1dcb49139032 | -14.00916 | -53.70605 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1871da09-635e-3232-9c75-ee3cd0b89d99 | -6.25234 | -55.42309 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95003cad-0faf-3d77-afe1-f8af148a2cab | -13.83064 | -54.00338 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94deb81a-fcd8-3158-b514-dece13b1eec8 | -8.62136 | -54.71359 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d5ca57-48ea-3e56-9f88-349761d7cc1f | -6.90128 | -58.99926 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e834a2de-6a90-3efb-a5c7-a1fc642bcd6a | -14.55771 | -53.05416 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18525171-5eec-36bd-ba9b-6f510bd72ff8 | -6.19244 | -52.37291 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10ef3309-734b-34e0-ae7f-cf8d57b70706 | -6.90074 | -59.00273 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c218ff8a-0b84-3cd2-8e90-634aa29906d4 | -7.36619 | -55.68712 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a0dda7c-8175-305b-8457-35b72390c423 | -6.94422 | -59.3076 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4f97dbe-4409-3f5c-8837-e66851795053 | -13.52364 | -58.11962 | 2026-08-22 05:23:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4c6978-dd0c-3888-9f06-91bc67d0fe66 | -8.59682 | -54.71355 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ecf0e07-a7b2-3c33-b49d-58c962945ebd | -4.58375 | -59.94313 | 2026-08-22 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bef53cd3-87db-3549-9de0-d1ce0d05d8ba | -8.62085 | -54.71711 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5369d864-8c16-385b-bed2-28f6e4ac6e2b | -5.80049 | -57.54881 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7d57fd9-9c4d-3f82-abe5-c905a98990e4 | -7.60047 | -60.9453 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4ac4b4-128b-3d9c-98e1-e2c1d18c1e53 | -6.79318 | -59.42543 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 327f8082-ab74-3ab8-9c96-057b19e6d46a | -8.61434 | -54.73388 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb10d5c-2a89-3a9a-924c-9ee0da3722ae | -8.56149 | -54.71888 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37dc5314-ac1d-3a28-935d-f73a633a14fc | -8.62591 | -54.6821 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0330087b-36e4-3130-88ad-4a2a6c49b38f | -6.78656 | -59.42438 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6bd1de7c-c7b2-34e0-a37b-9999b7f125c4 | -3.42524 | -49.48197 | 2026-08-22 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f6e5e9d-f272-39de-aac4-babe7ddb77a2 | -13.69132 | -51.8497 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fd1d9a0-f171-347c-be55-f7cfaa1365fa | -8.53457 | -54.81828 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a45dc39-860d-33e7-be39-da69a0751bcb | -6.76162 | -58.65683 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 01a02c8a-1859-344f-8432-ecf2920b49ed | -6.08711 | -59.95426 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e28dd4-7cb3-317b-b57f-077f15cd75a9 | -6.84721 | -59.42691 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e76fad6-db08-3e5c-9888-43196fa478e3 | -6.55412 | -56.55096 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 531b64c9-6a12-3bba-8190-79ffb43c43b6 | -7.44236 | -59.99924 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7159b974-bf7e-3916-b50a-97d6b4b5c2ec | -12.8307 | -48.4658 | 2026-08-22 05:23:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea06af5d-20ed-3eba-83b3-ee7e35340367 | -6.13877 | -59.90858 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6cc6d85-f8e7-3c16-80c9-44af1229e95d | -6.87703 | -56.63844 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fefc41b-7460-3469-8951-854c514edfda | -6.93375 | -59.30948 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d2b5bda-552a-34fb-b8a5-2cd040985cac | -6.75334 | -58.66624 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d6e7980d-a9ac-39a6-8c77-5b2d96f7ad8c | -2.45454 | -48.56594 | 2026-08-22 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 626fb45f-ed9a-3e69-997e-1524e07dbe13 | -6.84282 | -59.45461 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3f956a4-e580-356b-b7ac-a3227ca76419 | -11.82022 | -56.59187 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 136b7476-7e4e-3ee7-b0fe-82024a77b077 | -6.90292 | -58.98887 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69f274b1-4e4c-39d9-893a-8b6de2d841d2 | -6.44106 | -60.07947 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12e5483e-7e1a-3422-a25f-a560a8fcb380 | -6.7528 | -58.6697 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd2d5656-dba1-35f7-b361-cbf3bffbe395 | -7.37184 | -59.95224 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de92a7a-4e6b-37f3-804a-9ca4c4c9f0be | -6.81466 | -59.39691 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66b869fe-b0ec-3f3f-921c-c47c16ec29a5 | -6.94313 | -59.31452 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67395bb8-65f2-394e-a296-946c33be3c3d | -6.27266 | -62.53065 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99d3df29-5778-386b-87f8-f4f732503661 | -6.57428 | -58.98299 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4183680b-2600-381b-8b18-0932528d0636 | -6.12657 | -59.89946 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a3e5c3b-7fa4-3e34-8b54-569516780009 | -6.77577 | -55.69446 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c19c2e-943d-36cd-9f7e-e7a789c7255c | -6.85878 | -59.4181 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README60.md)
