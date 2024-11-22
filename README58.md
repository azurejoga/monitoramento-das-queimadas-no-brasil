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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6236362-73da-3ae7-a7d8-ff4170551b8d | -4.12014 | -51.05342 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d17ed5fb-3cc9-3a50-ad29-c80d98960c0f | 3.44302 | -60.40719 | 2024-11-22 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43aeb3db-a920-3057-a0fa-9342364d8647 | -3.11906 | -53.70306 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08c7cf78-b28c-3d30-b35a-cf2bf8d437e3 | 0.4404 | -50.77348 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cda0b5f-900e-34ce-a131-3db2c569ae57 | -3.10844 | -53.70701 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb1e1b33-dfd2-32d2-81d0-43d649311a4e | -3.29216 | -53.85495 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ca175dcf-3091-377f-b6da-510e98c1e482 | -3.66421 | -54.58781 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcaa1535-42c1-3822-8f2d-8616fc211f41 | 1.38418 | -55.94255 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c213dc7-cce1-3377-8ad5-bca7a07fe858 | -3.26996 | -50.62753 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3113a67-3a8d-33ef-bfca-286eaf6924a1 | -3.80644 | -51.26374 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39281a4c-3498-31c2-b1c4-c13edc4c1f2c | -3.73102 | -50.43316 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 080cc686-fd72-36c3-8658-3d29ee544bfc | -3.85755 | -52.35667 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1026fba4-09e7-351f-9566-f97e8dc7b929 | -2.6987 | -51.87007 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2af8c65c-73f6-3eb0-a0e8-dc10b6c19b9e | -3.86299 | -52.35748 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2324f5ea-1dfa-3aff-9391-b38d81d68cf0 | -3.58024 | -54.68191 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de5ed4ba-07a7-3b0f-831a-19a140e8573d | -3.5492 | -50.52039 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f9eba0-6ba6-325c-883d-5791ee14e7d2 | -3.23986 | -54.24763 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1c826b7b-53fc-349d-af40-a3e6c2498917 | -3.27998 | -53.81719 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 33cee822-6872-31cc-b3ad-41193fad84a2 | -2.69031 | -54.98743 | 2024-11-22 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3f84ac5c-7274-3983-898d-28d4df572483 | -3.50738 | -53.80514 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 82f000b8-9926-3d15-b954-35619781ebc9 | -3.5087 | -53.81136 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 227b3012-deb3-3926-bdad-f371d0397135 | -3.18519 | -54.31347 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a78f6581-e9bb-3e2c-a699-3061deea3891 | -4.14065 | -54.65807 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa854d07-d848-3bca-bac1-ca36ae66c52b | -3.22171 | -54.2322 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9aa7136-a0bd-33cc-bf3e-cd2728776539 | -3.68284 | -54.59069 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70c8e0f1-f498-37da-af27-38634e8db371 | -3.21545 | -54.24146 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b8d33478-970c-3a17-a893-3a944e2f001d | -4.18178 | -53.58009 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c978c674-db3d-3cdf-bef5-3597485f1a2a | -3.04382 | -54.84953 | 2024-11-22 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4357812-6662-3e62-9837-1d8e8303065c | -2.81376 | -54.01358 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f8b14f1-60fd-3fd6-b877-48d33d13eb69 | -3.22236 | -54.2347 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f39ae74c-ea5c-3586-a2f5-ace78d36a543 | -3.29294 | -53.84954 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 315758c0-84ed-3f0f-892e-fcd4e8026e6f | -2.50952 | -54.14896 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 244f0a6c-1a13-3742-8e39-a4e11d7f9a16 | -3.34294 | -53.33372 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a11f99a-c1c5-3269-a85c-39768ccfac75 | -3.00897 | -51.31153 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 183929e5-30b4-3bb3-a767-2557cf340458 | 2.38078 | -50.76405 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4558f4e4-a348-3f2e-aa60-88b874f39f37 | -3.00463 | -51.30623 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90fc94df-853a-3672-ae9c-85b269867966 | -3.1937 | -54.33281 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 150b13e7-346c-3a08-a453-d8ce086456da | -3.22709 | -54.23544 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77b70ac4-0a35-3f2f-aff4-cdd63d4d562d | -3.23584 | -54.24194 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6728eaa7-4089-34ae-acf6-64076189ffce | -3.22092 | -54.24457 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6247846a-1722-3250-8c00-7f71a16dbc7a | -3.85211 | -52.35579 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e618c3a0-5894-309a-9da5-11ec77cef4c5 | 1.38081 | -55.9446 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac753304-daa9-3bef-9398-989e7d7d1126 | 1.37688 | -55.94522 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055f1ee5-7549-34ca-a6a0-3d5eb692c8df | 2.3752 | -50.7669 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10d9db41-afe2-3283-ad00-4a9228203606 | -3.32219 | -54.77394 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38c4124-c9d5-3748-b84d-421b1e8d9188 | -3.09872 | -53.73918 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f688d18-24dc-3663-a1f4-8e71962f6dcf | -3.40969 | -54.02544 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f2b59a-2401-3123-95d6-4e11e8406cfc | -2.73778 | -54.38548 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 017c845e-86ac-3e27-afab-66dcb0e822ed | -3.23111 | -54.24117 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 182d2e6e-ff63-3544-b7b2-744f0ef3725c | -2.39309 | -53.71577 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c6c3505-6941-3b42-82e1-239682281cba | -3.54897 | -50.51946 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19a76e30-832e-3fb1-a3be-76127cf4cea9 | -3.1997 | -54.24944 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5be6dc5f-2cd0-35cf-ad44-0df17dc7824a | -3.21618 | -54.24389 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85d85d4a-909d-3fb8-af07-1debe6e273e9 | -3.23441 | -54.25176 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 2f8e5dab-e5e0-3028-9120-02b7fa286bea | -3.8472 | -52.35121 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1073b69c-f872-3b85-ae8d-de7d1aa48ced | -3.52365 | -54.6491 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cb1564f-59b3-33d1-a538-baab9ccc3130 | -3.57488 | -54.68607 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 14f35195-f17e-33df-ac81-7eb39d81020f | -2.91338 | -54.78076 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d4f82a6-e51e-327e-9b51-a708b86cf3c4 | -3.1111 | -54.293 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ca01d05-8422-356c-87fd-5afc18032365 | -3.26857 | -53.82655 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 06a3bef3-eb7a-33b4-8351-d1bc87239543 | -3.52091 | -53.79633 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28acb2a2-1c59-359b-9c02-28b655af6e7a | -3.20518 | -54.24525 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a2fdc89-2876-38cd-b6e1-465dc5793ea7 | -3.51799 | -54.68756 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52bd0931-06b2-3ab8-ad17-82461fffd039 | -4.19895 | -53.49536 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 567ad072-06fb-3bd1-88eb-8d1aae8f3aaf | -3.24459 | -54.24842 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| eb627cd2-4d68-3d1c-981d-5919cb81dd39 | -3.20444 | -54.25012 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0acb5c26-acfa-396f-8423-56d64d87dfec | -3.83706 | -52.25922 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 66dd387a-e091-3090-9f45-23efe367638c | -2.69852 | -51.86856 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79fae162-4cb0-3beb-8def-174617a6b9c8 | 1.374 | -55.95441 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4d9b34b-3e4e-3087-a0d5-dc28cdabe9bd | -3.75101 | -54.47116 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ea8635-a645-3b5b-9366-0d7becd637a7 | -4.20445 | -53.49314 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eced63de-2288-31db-91c4-ab38c9b8ca93 | 1.40064 | -55.91934 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30076695-3ccb-3a2f-a446-8c9f5d04714f | -3.56191 | -54.22284 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9a853334-4e8d-36b6-92a4-4bb1facde185 | -3.27503 | -53.83549 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffa4f980-2092-31f8-a069-b83b2d805453 | -3.25551 | -54.2401 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d5e85eb-64f0-3d02-bfce-2f9ba578b79b | 1.37287 | -55.97147 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a0c58ff-be66-31e7-8f00-22d3140b6589 | -4.1142 | -51.05242 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b542c35d-95a7-31c1-8b7d-37a0f08cfc8b | 2.5087 | -61.02587 | 2024-11-22 05:29:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2baa9290-2ac2-3ca2-8087-9915c229004b | -3.80817 | -51.99411 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9962a8c7-5b9a-33e6-aa82-4703e91c78f5 | -3.42316 | -56.42048 | 2024-11-22 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea615c8e-8619-3cca-a109-7b099257cfe2 | -3.3507 | -50.50512 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9c4d00e-8b8a-352f-af3d-5c159f9a2abb | -3.83101 | -52.2622 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 412dc011-40d2-3f26-9e3f-2055cc20e92d | -3.29703 | -53.85572 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bdeb874-32dd-32bd-8ff9-3286bae93006 | -3.55532 | -50.52126 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b96ac6b1-505c-325b-a12d-f5e26f1780b5 | -3.22968 | -54.25101 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 6bf5e4e3-4a39-3521-af4b-60af2d9656bb | -3.55941 | -54.59984 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff904ec5-3a20-34cf-9861-b007d1c75aa5 | -4.19937 | -53.49242 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55bc184a-cf4c-3a12-99b2-94071584ab12 | -3.80871 | -51.99038 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01e1a8d6-bf00-3894-ba78-b54cc89fd6e1 | -3.2832 | -53.84796 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3dedf709-7df2-3ee1-b489-fa96c78953e4 | -3.51338 | -54.68678 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 884eab4d-0e67-3b96-8e2c-7cb72d655699 | -2.34119 | -56.24619 | 2024-11-22 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dfd4996-fd5b-3c78-8970-0fe3340a91c6 | -3.19044 | -54.32204 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3633d778-8aac-36a2-a8a0-ca123dfcaf96 | -2.21785 | -53.73577 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bc2be60-4338-395d-a884-86e18fc02855 | -3.18049 | -54.31264 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bc76864-8be3-32d5-8c04-97c364347e8c | -2.37143 | -53.82641 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 056469c6-e980-3525-aff4-af9ab99d3393 | -3.24058 | -54.2427 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 28d07ae1-fa53-347c-b99d-65aaee696b6d | -2.95451 | -53.71593 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79cdaa4a-0381-3d2a-85e4-091f554d6aae | -3.22645 | -54.23293 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9a0585f-aef9-32e8-9186-876dba92ffed | -3.20846 | -54.25554 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e6766bf-7672-3614-add2-3dd99689fdfc | -3.00958 | -51.30753 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README59.md)
