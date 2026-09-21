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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de57afcd-8043-3366-a4bb-20adf622c29e | -6.11923 | -55.62983 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38f4c1f-e0e0-3824-bd49-8c3fd3f2db4d | -5.20703 | -56.11109 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4f21cecd-d133-3f75-b80e-22774977d095 | -5.85178 | -53.53426 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b65adba-79cf-3bb8-8f66-77b8a04b8cb4 | -6.14403 | -57.72549 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a53981c4-298f-3dbf-862f-0cc16702ea3a | -5.37303 | -56.05228 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c959b655-aa16-370f-9e7b-6822d7777c0d | -2.89978 | -60.05465 | 2026-09-21 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 584cfabe-e93b-3a85-899c-17a6eea64915 | -6.02525 | -57.83217 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e996d04-7e5b-3d8f-a1d6-68d60ea46df7 | -4.26293 | -55.77496 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e6f634d-261e-3ec4-9c54-48066711fc59 | -6.38033 | -60.01854 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 754add3a-b72b-366d-ad5f-e21f4eb22f7c | -6.12199 | -55.63379 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba54f997-86ff-3c7f-9008-c4f1e82e4094 | -5.88864 | -53.64138 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c95f84d-48bc-3013-94b7-dd9e8aaf8de2 | -6.55628 | -45.57194 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d57aacd9-9e64-34fe-9aec-d0ef8a2bac33 | -3.06739 | -61.27999 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f114c957-cf7d-35e9-81c7-e736eca6ac31 | -3.75411 | -59.42355 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2a0de0c-07c9-31ef-8e83-1bdc279cb95b | -6.6619 | -50.93364 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7212fa45-c999-3dfe-92fc-9f6902f392ca | -3.75938 | -59.41492 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 397cf457-abad-3b33-ad94-dd79da28f296 | -3.50123 | -59.18317 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8641637-c0e1-37ec-ab75-8ce58aa86d81 | -5.20251 | -56.07501 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760a96ba-b747-3c2a-ab4d-36720b4a868f | -8.37779 | -45.62603 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e1c94b1-1d68-3343-bebf-77db3be8744b | -6.41913 | -55.01096 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a161d3c8-6fe6-3d1f-a618-e6a8cf42b9e9 | -6.6503 | -50.92811 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e46ec2fd-462f-3445-88b0-eaf9c179539b | -6.44973 | -48.4446 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b0cd2a6-a971-3d85-a935-a5b0551dfc1d | -3.17859 | -58.59233 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1120541c-bc0b-3e94-8497-e9c9d41ea7ae | -5.84021 | -53.51679 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f082378f-ced8-3844-b1f3-ae23b2dbf770 | -3.47824 | -59.59031 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8ef3eb1-e073-37b2-bc0d-71fce5cfeba1 | -5.38301 | -55.90208 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47057d23-5d40-328b-a406-f62258e57556 | -2.96351 | -57.72279 | 2026-09-21 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 721150aa-11f4-35ad-a6c1-eb915ff83086 | -3.66175 | -58.57584 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0db71c91-f92d-3ed7-bbb8-e70b7b738fed | -3.05876 | -61.27863 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6808270-d016-3eb9-ad91-00a90795077d | -5.94116 | -57.69782 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 594dc83b-a1fe-33da-bc09-ec99b1119e19 | -7.42397 | -44.77172 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1d9b91e-22ac-369b-aec4-ed115b0a1704 | -6.20224 | -57.78037 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f74a6d1a-15d5-3cd7-8c28-58bec9e4404c | -3.78641 | -60.74605 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eac1949b-7f34-35fe-97a0-a5abdc6569fb | -3.1699 | -48.61392 | 2026-09-21 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1474ac27-3af9-3cb3-8acd-02330de0cfa8 | -7.43697 | -44.76859 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc5143af-7dd3-3fd2-94df-6d87c1e0179d | -3.64395 | -58.87357 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18a2703-660a-3698-bd43-a456072de0ae | -3.1826 | -60.65314 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63be8295-d62f-3a11-a316-f382a4a37fe2 | -5.85004 | -53.52221 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc222dc3-210e-3f2f-a89e-6844fee5a62d | -6.72369 | -55.08683 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ef9e19a-d8f6-3c25-a8b5-32e7a4b1efd4 | -6.41312 | -56.09998 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4273bd4-6e03-3486-bf53-758135fcdfb0 | -6.73701 | -55.08889 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05cd05c5-50fc-3020-a2a1-63adb265d332 | -3.39562 | -58.47733 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0047c37a-131d-3d0b-85e2-1b6d90c0eab7 | -6.39236 | -55.25048 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ca18a5-a624-3ee3-9844-adcfd61fac3a | -5.9225 | -57.68339 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28de7b10-3d3a-3b9c-a71b-eb7009fe03f2 | -3.34713 | -59.41985 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cfe643b-211c-3042-b3b9-983b5affb77e | -5.84947 | -53.5496 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 232092fb-dec2-3d4a-998f-ad4bd49f100e | -6.83081 | -55.53928 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78164743-af67-303a-851d-8b397dc9c550 | -5.21418 | -56.10867 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53a555a4-4992-338f-b4d2-d8f2f388f8ca | -4.53093 | -54.97434 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9762f1f-aa2b-30ec-8694-9cf30fbf3787 | -5.89898 | -53.64307 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a77895e3-b91e-381d-8dc1-9bf66d90339d | -4.0144 | -53.48952 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf483e8e-7659-3823-9ddd-0aa867f198c2 | -7.40247 | -46.15226 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ee0d16a-88bb-3149-a2c1-770d33e7eff0 | -3.65129 | -58.87475 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f5b4729-8484-35ad-a7cc-970f2f35a484 | -6.25878 | -55.43253 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f1e091-5e23-31b6-a4f0-b119c5d20f4d | -3.79957 | -51.36246 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f507561d-ddcd-34d1-9ed8-773e5ce52f9b | -2.74419 | -54.58627 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1497fc-3694-3d7e-ae26-71efd21e41dd | -6.34714 | -59.95847 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec633e8b-2cec-3a2b-ae2f-4e80433ff10b | -4.56596 | -55.75229 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3020ef5c-d6f1-32f2-b5df-b9e1cc44bb2b | -6.16003 | -57.95641 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c309b52-cfc9-3c05-8d57-609b48a6041d | -5.37641 | -55.90105 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b475047-00e9-3138-83b3-69ad45d7d2e2 | -5.80896 | -53.52026 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eeb2a370-eaa2-3c0a-ab29-0dcdbadbedc4 | -6.13781 | -57.72071 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3059699c-86f2-3737-9d89-114b9f13b671 | -5.8192 | -55.69891 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b017862d-b40e-36fd-b2d8-e21c0b6a8748 | -7.78056 | -44.82059 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34ca03a6-1d05-3cc8-b81b-76b01d6a4279 | -7.5199 | -46.22597 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7fdd1f-b66f-3066-b4b4-4153afc9ff2b | -3.44162 | -50.61327 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04ee7898-489e-33a4-b78a-0f487e8af2d9 | -6.29127 | -59.92137 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5962ef0e-fe4b-3e78-a704-0bf4dc135e1a | -2.8191 | -54.71428 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd83786a-8445-3ca5-a291-79be9ee83610 | -3.37355 | -52.79515 | 2026-09-21 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c830c4c2-e04e-3542-b731-0927138b2eb1 | -6.90979 | -43.72753 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c5b7752-42ec-3091-a80b-bd8c2fead693 | -5.92861 | -59.95328 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe460b5a-b1b8-379c-9b1a-6b9fdde5d8ad | -3.6035 | -59.05548 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3392b0e7-cfa3-3e25-8d6d-6a075fc62766 | -2.99605 | -54.1694 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d947dd4-c8a5-340e-80a2-30c9db004f84 | -3.68853 | -60.62804 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d403050-a9da-3a4f-ba5d-c3f0b240248c | -2.91398 | -54.19267 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b262240-9809-38f2-8ec8-d8ba90fee4a9 | -3.06242 | -61.28343 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e49661-dca1-319b-b685-ce2fe388b605 | -3.44316 | -50.60324 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b1715cf-23ac-3815-ac31-47c141bfb229 | -6.52479 | -58.30815 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c8b2b8c-84af-3403-97e3-038efa7f1e5d | -2.30069 | -48.58388 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72b59839-33f4-32d8-8ae4-be7e16eb3128 | -5.82223 | -53.52623 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6812da55-e7cf-358b-9250-19135048dece | -6.12997 | -59.95789 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcbe6077-cb5a-3929-9416-95d6eb643736 | -2.17461 | -48.32417 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abd532f1-1e87-3220-8297-772aa0d7d695 | -6.09044 | -56.4673 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5ed6a26-bf20-3c98-817a-a208205d9bc9 | -4.34015 | -46.37648 | 2026-09-21 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6adf7bee-9d9b-3938-b3dc-bf6771391ce7 | -3.44725 | -58.39599 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b343fca-b551-32da-801b-c6dca636e940 | -6.46901 | -48.44817 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d8e43e2-5f8a-3b46-a24f-70d4722cda36 | -6.41526 | -55.01396 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32fb4da2-c22e-3be7-ac7a-819a3763a3ac | -4.3618 | -47.78558 | 2026-09-21 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d4cc3e8-c331-3856-86a3-4de4db744df1 | -3.01107 | -54.18252 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dc2b818-b141-3f07-aaa1-8747eb07595f | -3.66434 | -54.26527 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f97486bc-044e-3a7a-8df3-3681ddf4ed6f | -6.47451 | -48.44358 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04173862-fd84-3232-94f3-e153185c9dc8 | -3.30431 | -57.86555 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d403ee1-6c4e-3f31-9ac6-53ce50ba0af4 | -6.10387 | -55.6416 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5acf4377-a147-3015-aa09-b49061c3c9a7 | -6.16861 | -57.70712 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22325077-cea1-358f-9de0-5a5961808006 | -4.55937 | -54.92197 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca43d00c-446a-340c-a3e8-8498337f5390 | -4.94316 | -55.82223 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfe24c31-c1ed-37c9-b7f2-4950051b9bba | -4.15338 | -50.23922 | 2026-09-21 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 592d7283-b1cc-3e2f-9d6b-43c520f7a0ba | -5.82171 | -53.5065 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3fd7393-3ea1-33ad-a5f2-69bcd5adbd92 | -3.48673 | -59.56242 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e19b3f2b-895e-3a11-b879-d1f4678a9ab0 | -6.06961 | -57.73259 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
