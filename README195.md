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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beebe368-1140-3fbc-882f-ed17f2d468b3 | -2.40099 | -51.30322 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35843741-5ee5-31b0-9043-dd0f6389c0d1 | -3.57604 | -54.6806 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dab111b-a0df-39c7-9b4b-e172f3bdb1ba | 1.69009 | -55.61146 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c80f60c-1138-305a-a93e-6c81cc759288 | -2.73106 | -57.46358 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 693cd239-440c-3382-bbdf-2d55631f6e70 | -4.55042 | -54.97034 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 035d0d42-2452-3ede-b3fa-c69cc3647ac6 | -9.30046 | -47.46796 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 53901d30-a6bd-337d-9b0b-eac99b9a8d64 | -6.69064 | -59.96274 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52670e5a-11de-3e9e-9e0d-d72fd6e1a4d7 | -1.61637 | -55.12241 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7149a25f-d96c-3bf6-b38d-6fb331b1a9e1 | -2.58676 | -56.16787 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70cab35c-596a-3bf0-90fe-ffcf9f98082f | -3.46551 | -59.26347 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c543b35d-8bc5-3ecf-b101-d40a55507a97 | -8.3276 | -49.12438 | 2026-10-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0833fab-4da6-3d1e-b36a-77501b4b372c | -3.02523 | -54.05885 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d1dd1cf-0755-3489-a26b-466d0dd3c508 | -3.57004 | -54.67686 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fbad428-7355-3c45-90ae-9114b5690b62 | -2.42892 | -56.68482 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f896f77b-1efe-3029-9a9f-c1f706ca493f | -3.555 | -54.66819 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b111a45-bb90-372e-baf9-0f20eef15901 | -2.01832 | -61.27064 | 2026-10-09 05:23:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6dc94e1-a8ec-344c-b4c4-123be9062b09 | -2.58336 | -56.14428 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da7a98a6-fc05-3a17-9249-57b52419cde4 | -1.30644 | -54.18789 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a47d9ad2-ccbd-336b-b0c3-4d80ca1b447e | -2.84728 | -59.11271 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e32773cb-0f86-3bc2-ba2c-46087c38e5b9 | -3.08453 | -54.30604 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bb376bd-7c83-37a7-b8cb-f40c075cfdfe | -3.64954 | -54.06218 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f60f9afa-5f77-39ff-b384-70dd18aa37a8 | -2.74427 | -54.10578 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ad34580-9941-3956-8da7-d3fa14c85003 | 0.53553 | -50.89789 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| de81e8cb-732a-31d0-b1d9-d3b6188d9b6d | -2.74281 | -54.11518 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56894102-c8c8-3fac-b6be-d975a17cb1e5 | -3.35536 | -50.41247 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5b7ca62c-622c-33d5-992c-5721c431fe85 | -4.35906 | -55.22077 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9e1ff9a-6a0b-3687-9dbb-71e79d4c82f0 | -6.99368 | -59.10446 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c095bf3-e8d0-3b2d-a6c2-c4646e46ba27 | -3.08245 | -53.96907 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e9821e-ad2f-3909-ae3f-346543718fa8 | -3.74638 | -59.4405 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7de7b81-47d6-38fc-9bce-1cc0376c7288 | -3.53253 | -54.66491 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b44aa5b1-b300-3c1b-9182-eb5612ec9129 | -3.7386 | -59.44644 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0712de24-5c96-3de7-9007-3b3c829961c9 | -3.77677 | -58.58717 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7a1ebb60-1e13-3c54-93ee-460d07273f68 | -3.01777 | -54.08217 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79343b03-0f9b-3472-9ae2-081540542ffd | -4.46178 | -55.40363 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 307c2083-b8bf-3a42-92cc-dd50ef7c17c5 | -6.44809 | -59.94874 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8446e85e-9e73-367d-84a0-b75202334972 | -3.27993 | -53.83218 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e30d608-234f-3e13-b09b-ac0793e066ef | -3.79992 | -56.99442 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6786e864-b0d2-3035-8f57-72ddceffbfb8 | -3.2505 | -50.40242 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b61c71ff-4308-3115-8621-dc8f0740a4d1 | -3.01007 | -54.08097 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eb9ca19-a027-36ab-8544-66b80597f704 | -7.85795 | -63.40002 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca4aa809-b6a2-39ec-8e69-23e0094028eb | -3.07675 | -54.28385 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0016c85-663f-3c72-bcbe-bb3919521e7b | -3.35199 | -50.40751 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e80e4319-3f73-3193-ad21-98c028f12df8 | -3.00395 | -54.08269 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbe6db31-90d7-32a9-81e0-2343856cabe9 | -2.12913 | -56.69459 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de77c666-6d4e-3309-be41-af91004cd5c7 | -3.74301 | -59.48304 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5161a3e-6396-3049-8a15-e63171c13a8a | -3.08213 | -54.29615 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b63f4b7-e079-3b07-ac60-8e054d966d37 | -2.84512 | -54.12836 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dfe1abe-505e-3464-8a0f-dca5f623637b | -2.74591 | -54.12046 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8382413f-aa30-3e87-905d-67c1f1c1a986 | -3.02908 | -57.64256 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed2b0462-94d7-3b8b-b343-46bca650728b | -3.51091 | -59.21357 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf89304-fabe-3d06-9b02-939c7166d853 | -3.07469 | -53.96791 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8327d8fd-ae52-3aa4-be14-b516740cc87f | -3.69509 | -60.5508 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68e6eb88-4652-3717-8acc-9f8fd958aba9 | -4.07994 | -55.37975 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07be8804-a022-3dcf-a3bf-28c1d43a3a97 | -2.84162 | -57.47399 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e52125d3-75cf-34d6-a52a-42abb20fa0c2 | -3.51943 | -59.22204 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c5d6fb8-b107-3ee5-922e-79664a8e2105 | -2.99167 | -54.08566 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ce5fd1-94f0-3825-9e21-4e26d8bb020e | -3.10485 | -53.95262 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6e4f90e-ebe8-349e-852e-cc33232e2374 | -8.98619 | -45.90373 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ef54487-9e8c-3890-9deb-3894db01bdba | -3.91874 | -55.8568 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37966ccd-7b0d-353b-af6a-6612035a8644 | -3.9249 | -56.02952 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1d9723f-bc08-3251-9ba9-9a9c216f43e6 | -3.27684 | -54.06216 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 822ef0db-b57f-3b11-b5ba-b9cee8274b15 | -2.50149 | -56.06237 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 03880b25-c8cd-394d-a84a-e584ce0bc95a | -3.21086 | -53.86502 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a792f5d4-7471-3143-813e-6d1153454065 | -3.05717 | -54.20922 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76408e44-ad6d-3d73-a95d-ccfbcdae31a9 | -3.97511 | -59.6274 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6eccabe-39db-3d7d-b33f-5dbf72e4818d | -3.62652 | -54.23523 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dcab11bc-ab64-3c4e-aa39-bdfb15471896 | -3.92227 | -55.85736 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 539c0807-8d51-32f3-bbe0-32de289f47f4 | -2.23864 | -51.92419 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc65d57-6ae7-31ba-b700-1751f0026d09 | -3.21235 | -57.83789 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b81d5804-3b52-3ce6-8efb-9c7aca8ce3aa | -2.90053 | -54.02516 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af987676-0da0-34cd-a923-9b360d1c5e6e | -3.00182 | -54.12124 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b9eb186-3e8d-3e9e-97ff-26fa81bff92d | -2.50062 | -56.18153 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e0a44d9-fa59-3c18-a104-98e02f38a48e | -3.15462 | -50.59394 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c41bc1-0aa8-31e7-a59d-3f31e0be036e | -4.31592 | -55.62432 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa59f9b-de02-39b8-b204-29a6f5293c6b | -3.78007 | -58.58769 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae9c0e30-5d8b-373a-915d-dacb044678b4 | -3.22211 | -61.1512 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6f4ce21-1052-3112-94c8-9d2969fd02d7 | -9.24926 | -62.30638 | 2026-10-09 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f313e6c-28cd-3cf1-93b3-a7b2cf1aff6c | -3.29707 | -54.08485 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43fa7f09-d770-3f11-9d22-0d23272bf6de | -3.70412 | -61.33088 | 2026-10-09 05:23:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94156b17-ea2c-3ecc-9c06-8f3a58cfb9d7 | -1.05479 | -53.59063 | 2026-10-09 05:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21bd0093-82ef-3007-bc9f-c14798aa7357 | -4.28604 | -49.08999 | 2026-10-09 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45d2bd7c-b099-364b-b4cb-db5813744687 | -3.00694 | -54.06365 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f4f8aab-5b9c-3805-b752-07a5ea80fe21 | -2.58444 | -56.18285 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94155795-6456-39cc-9598-8aadf4e4c757 | -7.88948 | -61.78219 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ae7105-49ad-399b-b4e5-28748b985854 | 0.94352 | -50.19716 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc88341d-989c-376d-a778-1e33cc933d8c | -8.24952 | -54.7301 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac1cd59e-b08e-372b-a0d1-bb8805d84267 | -3.93191 | -56.03061 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7298c4bf-af3e-3e28-bf5e-248816a4a9ab | -2.55544 | -57.43646 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f694d24-7810-3969-87ff-5f977b51386e | -2.74063 | -54.12928 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1368af19-77ea-3af2-80bd-f8997d46f362 | -3.55452 | -54.69574 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 58a3d087-422e-32e0-ac0d-00a43dd26ccb | -3.01295 | -54.06189 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0cb1ab3-8ca3-3cb2-bd5b-84bb7e8382a3 | -3.0032 | -54.08744 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13563497-96aa-314b-996b-c655bd7ea992 | -3.28851 | -51.57056 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1f371bf-e2d1-3989-b673-1abe08264c57 | -2.81513 | -58.28722 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b35de39d-2c49-3ce2-aaba-d56e989243a5 | -3.18236 | -58.8423 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f653e2c-9039-3561-8812-3d95cb2b4ce1 | -4.35388 | -55.22715 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ddd8343-5e50-3358-a036-7b23c948138b | -4.52127 | -54.85969 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec2ca50-ae10-38ac-9cc2-ae3e6666bf9a | -2.58277 | -56.14804 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5524ef01-6258-3dc7-bd71-c52db4ef0ac5 | -2.76296 | -57.69271 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda4df5b-34de-3408-8959-0ca9bb34013f | -3.90501 | -59.59465 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README196.md)
