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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3af828e6-a02d-3b7e-90c5-e60ea78c44f2 | -6.69434 | -56.16162 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86ef943c-5f73-38d2-bdc6-0e905b083dae | -3.48668 | -59.57498 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fafd10f-e191-3571-a679-3adb84b2f022 | -5.38962 | -42.94869 | 2026-09-22 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d6a8ceed-c8d7-354d-9bc1-a3d4b2f1dbd9 | -8.3952 | -50.24613 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37d342f2-3302-33a8-b882-6086114657c9 | -4.22027 | -48.61581 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ec2b288-dc77-3c5d-8183-8a837a93b0a3 | -6.85971 | -59.90342 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b5aeb7f-4dc5-390d-b885-fcb4586d8425 | -3.35578 | -50.44777 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80aac8d0-9a1f-3a0f-87dc-4a51f725b268 | -4.95998 | -55.82022 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b31f3f-da89-3277-bdbc-e38a23c11a57 | -4.27264 | -55.44489 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e60b96c-4067-373e-967a-b5e5fb61a1da | -6.33715 | -55.28044 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f45748a7-a34d-3682-aa68-2a85c13a9ead | -11.41331 | -46.79687 | 2026-09-22 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05f25cb0-9842-3a59-aa55-60ecc15a510b | -6.30834 | -57.73441 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5dff4a4-9aa2-3714-8b66-339de72770a2 | -4.93944 | -55.82042 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ba4fba-26da-3e32-a42d-68fd9ecef442 | -8.8183 | -48.76208 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b50b6bcf-6925-3888-bc0e-5a9706f24dc9 | -3.91774 | -55.75416 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec0f9159-80ad-3b55-aa72-bb19278292f9 | -3.4925 | -59.57262 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0a9931-6583-3a9a-bae2-662bc5d2fe0d | -3.12818 | -51.59933 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1099ddce-b6dc-30af-b92a-8f635a21a62d | -8.3075 | -50.37994 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ad27dce-554f-36ad-9e1b-a3cdc0e8182a | -3.77263 | -61.19228 | 2026-09-22 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5640d73f-2d16-3ffe-90b8-0b0d433ea501 | -7.57915 | -57.67871 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8c43a39-735b-3ec8-a655-b5b0b8ba258c | -9.25752 | -46.6208 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4951ae17-d812-3719-80fc-4653dc989f68 | -7.39929 | -55.22955 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 705f1fcc-f2a1-3b14-a65d-df2284a647c2 | -4.53422 | -54.97505 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41da965f-fd58-35b7-93ce-0adec50711a7 | -5.27467 | -49.33967 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed45ad6-5f0b-3823-9004-ace5d38d2a1d | -7.51589 | -45.44631 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fa5a07d-cfc9-3312-8114-b633084adf6c | -6.35032 | -57.77603 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0c38134-0893-3d3f-8633-e8d468c67d32 | -7.0625 | -45.25522 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e2a5ac0-0d23-348e-853b-3e959e571a36 | -4.77851 | -55.70085 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64f51640-a738-3004-a615-10e24059cc54 | -7.31964 | -54.94387 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 135162fc-f5ec-3190-885f-d6abb751a776 | -6.13052 | -59.95976 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 297e285c-7f71-3a81-8447-748f0f0a3de5 | -3.20762 | -53.94495 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d758f0a-a42f-3d1e-9a9a-3f9721fceadd | -10.38305 | -48.91278 | 2026-09-22 04:46:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe68d41-84e3-31df-8b9c-03af3b66fe77 | -4.43296 | -55.35062 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cb95ee2-c8d5-3fcb-96bf-b865227a46e7 | -7.58206 | -57.68781 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0ec8b2f-fcf9-3f83-b259-657e3d5dbd05 | -5.27412 | -49.34331 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65972743-3ceb-303d-9bb6-8eb1fc73f014 | -5.81937 | -57.73573 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57180afd-43e3-3b86-969d-bd90de0f70f2 | -7.59427 | -57.66842 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea89d7f-1344-3de4-aa7d-558684aecf0a | -6.47132 | -48.45792 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bccf41de-69dd-38c2-aab4-47747b24fcfe | -5.77738 | -50.18876 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bff39cf9-437c-36b7-8b25-0f9429cff3a6 | -6.62019 | -59.915 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 37582eac-36ed-3e3f-9398-2803a791e408 | -3.71424 | -60.55541 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7a155fd-731b-3fcc-bad2-93887c7a5a5c | -5.76258 | -45.08243 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5614cb9e-a5dc-394d-b0d5-ad6627b4f2ed | -10.93992 | -47.85789 | 2026-09-22 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a7cb703-2ef8-306e-986b-7ffae867ffa3 | -4.26022 | -60.0091 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d79483a8-0f71-3f11-beac-81ed50d4e455 | -5.21107 | -56.07545 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7c41c32-29a3-39e4-956e-afd36211906e | -8.78867 | -44.2735 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4a1f3283-5cd9-3d52-98b5-602737cc9ff3 | -8.41933 | -46.86843 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 933b657f-3291-3640-a4d6-864c90e65887 | -8.61089 | -54.62564 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5a89447-602a-358e-8198-e996dbec3a99 | -3.27257 | -50.02255 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4a859c8-cb4a-3f2d-ab87-8096866b9579 | -3.82031 | -58.89172 | 2026-09-22 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8908e688-43d2-3c0b-8ae4-061df5a72d48 | -8.1166 | -54.80195 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9930ce4b-22a7-3bf4-b086-82efae19a170 | -7.41989 | -49.85036 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cf3d8fc-6b0a-3724-bea0-76a4288473a6 | -3.40352 | -61.2968 | 2026-09-22 04:46:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d61651a-a190-36d0-9655-d3ff85097688 | -4.13897 | -50.22527 | 2026-09-22 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7471e4ac-c6bf-35e1-8d03-e49565bbcf7d | -6.83458 | -55.53936 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ae8be9b-e2d0-3acd-9265-e81e72c136e7 | -11.14925 | -42.83566 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3ccf38c-edac-3d0f-980c-aa78f4388a6a | -10.68881 | -48.71183 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d5f3e3e-3671-3e88-89df-b41a0fde575c | -3.95156 | -47.61839 | 2026-09-22 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ba150c-aab5-3b40-998f-a479775c03b8 | -10.68533 | -50.76657 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a1a55d1-ac8c-3a66-9134-6f3aaf8fd53a | -4.6575 | -42.08802 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 014c867d-2ecf-3fac-9b3a-cf4adca1ada5 | -5.84906 | -53.53049 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 590c017d-5e7b-3f0f-b00c-7b5e72bf8934 | -8.62288 | -54.61924 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 650e5aa1-e0e0-3b0c-9787-ce05ce949d50 | -5.8842 | -51.57633 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 811f4c1b-8012-3e72-bad7-78cf9c2c229f | -7.54799 | -47.32563 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cddb916-e662-32fb-a8dc-fc996a730437 | -10.12594 | -45.54728 | 2026-09-22 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 647a17c1-4e3d-3082-a0e3-bb477974537a | -6.89453 | -41.69509 | 2026-09-22 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02dba5e3-2106-3f6f-ae1e-5b5abe7f831f | -6.68328 | -50.94941 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb2d259-be6f-3b24-8205-773252154048 | -3.91958 | -56.05243 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 156efb32-95c9-342f-8bb1-5514e33ca280 | -10.45383 | -51.34559 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ccccc70-12ed-398f-994d-c7272caca299 | -8.00279 | -44.80387 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cab7d17a-cc82-3963-9048-24794cbbf761 | -3.3811 | -50.44136 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb6c3ea-700a-33d3-99ba-feed54e4be62 | -6.57584 | -44.15987 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 17490d02-97b7-3767-b0fd-3bc1cba83cb1 | -6.69831 | -56.16231 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c943caa-b13e-3c13-8cdf-ffbf9bf674f4 | -4.22715 | -48.61688 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5ea03ed-9d83-3962-a615-8cd371b06c6f | -5.86682 | -52.12005 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f6f09ca-0d5d-3e4f-b3ad-14336e6367a3 | -5.75328 | -51.93344 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eec460e-8845-360f-855b-eb69b00add77 | -9.56742 | -48.42798 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0035c1bf-e413-3fb9-90ee-b4116ad364d2 | -11.3821 | -44.22927 | 2026-09-22 04:46:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 488b6188-0e20-3d32-a4d1-72cc15974a8e | -3.05602 | -54.41471 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9641d725-5966-339d-9ae4-bc554f3bad26 | -6.92243 | -59.63345 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89f6dbf3-70a4-3826-86c0-091c4155224d | -3.05338 | -54.4024 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d98ff54-f04c-3f7c-b16a-70144ff9acf6 | -8.76237 | -49.96626 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9da144d3-5fed-3e82-bf16-91bdcb8cce31 | -11.34219 | -43.37521 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3e100d-7660-34fa-bd90-20ede24d711d | -9.89931 | -48.48566 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b056ad86-a550-3305-bd25-852c6a51bb0f | -10.69973 | -50.67189 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cb660f8-2487-366c-ad76-dc21b04a82cd | -6.38336 | -55.28316 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ca3bb85a-15bb-39a4-9e36-95c3746363ea | -3.34224 | -59.86476 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1541c4f1-7f61-3ced-8769-ae8a6187fdef | -3.68726 | -60.57809 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18283a87-8f2d-3c8f-adc2-ac683987154e | -6.34257 | -59.95251 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1485ce49-94cb-38ae-9fa7-d9ce933a0a37 | -5.82673 | -52.20046 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838d0236-37d7-3370-af09-7be39232bba7 | -10.73837 | -50.81519 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beef78a6-3e14-37ea-a173-5d5d79a3e12c | -8.90328 | -62.377 | 2026-09-22 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a5ede49-adc5-389f-b05f-03d35137dcd9 | -5.80939 | -52.09658 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15b2aa55-479f-31b0-91b2-ea4a5f777f45 | -6.79373 | -59.94847 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f655346-7ece-3085-b44b-bd6a26aa6fd1 | -5.33936 | -43.30337 | 2026-09-22 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3f751a9-9212-3ca8-afa8-d3bbe5313280 | -9.05731 | -48.77757 | 2026-09-22 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4ad9f72f-7198-35e0-b443-e978498b9cf4 | -6.5765 | -44.15503 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e08b7d7b-d6ad-3d2e-b921-7f9cf49ca1fc | -11.02395 | -48.27825 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75d948f1-f721-3332-9fb6-fe52b72dafab | -6.45529 | -59.98674 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e714bd29-ba09-3dd0-9c36-c3792a32cedd | -3.68596 | -60.58567 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README57.md)
