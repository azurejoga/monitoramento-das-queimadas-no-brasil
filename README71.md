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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 869ed0db-73b6-34af-9a83-2684a6b93e49 | -3.41035 | -44.84212 | 2024-11-06 12:40:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 01d9dbfa-db4b-3464-8b57-18ff71397b91 | -6.46361 | -42.2401 | 2024-11-06 12:40:00 | TERRA_M-T | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| ba44208c-76ea-36d0-94b8-03cbf1c7a130 | -3.39873 | -41.41096 | 2024-11-06 12:40:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| f491f569-fff8-3357-8b45-51c3a6389bfc | -3.40139 | -44.84087 | 2024-11-06 12:40:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53362053-6915-3610-92e9-c4e8cea25b64 | -2.25283 | -47.66646 | 2024-11-06 12:40:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3c9c6b72-9e56-3ba8-9d44-9d64495aac22 | -5.22347 | -46.7156 | 2024-11-06 12:40:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| aade5463-75f4-34da-89c9-cef0b7cdae33 | -6.49686 | -47.47548 | 2024-11-06 12:40:00 | TERRA_M-T | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 72d73126-cfbe-301f-bf8c-0645c827d448 | -4.75056 | -45.90943 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab015f3d-09fa-310c-8062-8c942cad0752 | -8.37791 | -43.62733 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0b7b0d4c-8ada-364d-bcfd-e17b66bae560 | -2.7936 | -48.57827 | 2024-11-06 12:40:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 4cc1f28d-ab4b-3ec0-a6d5-e328a0e06086 | -3.43339 | -46.21247 | 2024-11-06 12:40:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6bd6af82-351f-3446-9145-88f14c885ef9 | -2.96607 | -50.99175 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6d9c2bf5-abf5-3bfe-87dc-51968340ce4c | -3.37355 | -48.68303 | 2024-11-06 12:40:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c3363ea2-5d03-37a6-add5-29807b85cd6c | -3.75682 | -47.60371 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5351ae72-4759-3b51-aec9-fbb53fa977a7 | -3.64649 | -50.14085 | 2024-11-06 12:40:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a290daae-a3a1-3686-bbae-93696e588fc3 | -3.17347 | -46.60755 | 2024-11-06 12:40:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7f6c9a62-bca6-3706-8004-aed86f6b3fb4 | -3.1071 | -50.27788 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3e8ca68b-825a-3297-b25c-ea7d1d5310de | -6.36099 | -43.93336 | 2024-11-06 12:40:00 | TERRA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c32fd463-78f3-3345-af89-e3ed0f7ae7f5 | -4.13319 | -43.57499 | 2024-11-06 12:40:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| ce0a0851-2af6-3b00-9522-cb5c7345a8d2 | -4.54599 | -38.96339 | 2024-11-06 12:40:00 | TERRA_M-T | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 00939afa-7b20-3c5e-9803-50e847d0c942 | -4.58225 | -48.06959 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a5e3c926-70d5-3faf-9046-6cc30c0e3a56 | -4.19123 | -44.28459 | 2024-11-06 12:40:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0b7a466c-fff6-3a19-84e2-ad26df018d49 | -4.77957 | -45.95846 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e781ad29-c302-33da-b37c-6319f56c77a8 | -2.44632 | -45.83481 | 2024-11-06 12:40:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| caa8ac0a-cb02-37c9-bc08-49e6715cf056 | -4.3758 | -47.53322 | 2024-11-06 12:40:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6a2b8a3a-b6b7-3e8b-8c58-2350bbf3c161 | -4.37287 | -38.18081 | 2024-11-06 12:40:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 26.1 |
| de1e8df1-3b44-3bf9-87ae-0750ef8251aa | -5.26736 | -46.1632 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d729637c-3a5b-39dc-a317-bc62c9a9a20e | -4.40568 | -41.91706 | 2024-11-06 12:40:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 7c57b8f1-a08f-36ea-a93d-56e5fc18934d | -0.84748 | -48.58303 | 2024-11-06 12:40:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 134cd631-eb30-3462-ac19-32b5c16e23e0 | -7.44691 | -44.71944 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 37df8a50-6465-3414-a225-120c526e2a5d | -4.54892 | -38.94062 | 2024-11-06 12:40:00 | TERRA_M-T | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 784027cb-5ca9-356d-b09b-d8960d9e2774 | -4.85684 | -45.687 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 92992707-a26a-38ab-9fdd-e25c359d5f35 | -6.49422 | -47.49358 | 2024-11-06 12:40:00 | TERRA_M-T | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ba8ba33f-3be7-35dd-9abe-476e2ade36da | -4.30596 | -48.61739 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3aa7c5f7-5777-35eb-9ae6-27cd92060d37 | -6.64331 | -47.86178 | 2024-11-06 12:40:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59eade60-9215-34c2-ae63-f2d647b63edf | -4.20176 | -46.70224 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a80b11d6-0777-386a-8921-3823b622c0f6 | -3.08715 | -54.50518 | 2024-11-06 12:40:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 217fb8d2-d25e-3c20-8e5c-66e792a9400f | -9.07127 | -43.09322 | 2024-11-06 12:40:00 | TERRA_M-T | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| a326b839-7e33-3312-846d-c7f997db19d9 | -6.52303 | -48.43065 | 2024-11-06 12:40:00 | TERRA_M-T | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b0355404-75d6-3720-9a11-505144fd8d17 | -4.69292 | -43.73089 | 2024-11-06 12:40:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 563e2dcf-900c-3adc-ae43-b047f9abee54 | -5.95824 | -46.30114 | 2024-11-06 12:40:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 93882701-06f1-3035-8082-d1a6367bb1bd | -5.23697 | -48.13791 | 2024-11-06 12:40:00 | TERRA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a543f429-9b8a-3203-9375-dc9f233228c8 | -6.46545 | -42.22659 | 2024-11-06 12:40:00 | TERRA_M-T | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| dd310ffe-539e-398e-8f2e-ed9948fb1917 | -5.81361 | -45.96191 | 2024-11-06 12:40:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cafb792e-c50f-3f4e-962e-8bb12d300930 | -2.82153 | -52.92126 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 220.8 |
| c9841283-dd7d-3189-8057-5c65cb11f88c | -5.55502 | -43.70323 | 2024-11-06 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| f1ed1da6-d028-3a71-85b1-c8983fee4001 | -5.28869 | -46.26508 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4353bb99-624a-34e6-9623-8d9daa5e0276 | -1.52271 | -46.22723 | 2024-11-06 12:40:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dff64421-6f13-3251-b2f4-578620644037 | -7.45274 | -44.72669 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 537b670c-0eb1-3082-aefc-a4f8512370a7 | -8.11549 | -44.41341 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| f2aec5d0-7138-3b87-ad1e-d87f9240ce8c | 0.37894 | -50.95895 | 2024-11-06 12:40:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 82e009f3-990b-38a5-a0ec-6f643b18065e | -3.03616 | -53.26715 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4c0514be-3d03-374e-9ea9-dd4c2080d322 | -8.38795 | -43.62856 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d6c5004e-70b5-3073-b343-775e98c2d6e5 | -3.66471 | -42.3868 | 2024-11-06 12:40:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 1414342f-1c76-3ec8-bf23-642d67b53386 | -3.13484 | -44.2538 | 2024-11-06 12:40:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89a1e096-a2dd-3865-8bce-d00ba38d9577 | -3.33773 | -42.46217 | 2024-11-06 12:40:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 171fbc9b-71d2-3550-a414-ad68d4b1e68e | -4.34961 | -48.15836 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 32a72508-bf9e-36cf-a05b-8df6e166f8f9 | -6.27394 | -44.73086 | 2024-11-06 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d4f85963-7d6e-3d36-96a4-789bf6099971 | -3.03238 | -45.22056 | 2024-11-06 12:40:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3928c334-9907-3ff6-8b09-205499105850 | -3.69876 | -44.63084 | 2024-11-06 12:40:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0c20389c-39dc-3d45-a42c-cbd6887bb5a5 | -7.23418 | -42.88562 | 2024-11-06 12:40:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| b5c8f6ee-387f-3108-af21-cfc5210f2c23 | -6.94687 | -42.81594 | 2024-11-06 12:40:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 02cffbd1-0e0d-39ed-be40-df3ed42a3903 | -3.49898 | -42.10344 | 2024-11-06 12:40:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 262f3167-17c1-3e8c-9383-25393a3b9287 | -3.06428 | -50.49094 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 22dbb188-e5b6-357b-9f09-9ef1e79518f2 | -8.08274 | -44.44007 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7a044a2d-14c3-37fb-93fb-d7ce30065220 | -7.7846 | -44.07588 | 2024-11-06 12:40:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 66d23cab-07bc-3af7-8b69-2fff13c275ab | -7.44509 | -42.89429 | 2024-11-06 12:40:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| f1331b6b-b700-3090-8e6e-bc3ffaf5c837 | -4.346 | -43.78279 | 2024-11-06 12:40:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 85e6d4d4-d1b7-3d1c-94b1-c8415445a781 | -6.46833 | -47.54558 | 2024-11-06 12:40:00 | TERRA_M-T | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1acddd4c-0e15-39d1-9808-3b6fbf34c673 | -8.10458 | -44.42218 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a25544c6-76f7-3ed6-bd26-af6c938800da | -4.55437 | -48.019 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ec815355-14f5-330e-b2cc-cd8e7267dcaf | -4.51441 | -43.48236 | 2024-11-06 12:40:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e7b7c8c8-e660-380a-bcc0-f5c16009b038 | -6.51537 | -41.42398 | 2024-11-06 12:40:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| da831204-caaf-328d-bb42-c63145562550 | -8.32509 | -43.56607 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 060504da-7cb9-362e-a1d3-f5f49a2ae9dc | -4.39157 | -43.1138 | 2024-11-06 12:40:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 63138c2a-e5a6-36d3-95e3-a6b8c884a8f3 | -6.95747 | -47.85933 | 2024-11-06 12:40:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2862c871-2f7a-35b0-8afb-7d697816df7c | -4.77698 | -48.68389 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 265f0999-4f05-3acb-bb6a-c6ef1e64ed7d | -8.26509 | -44.84316 | 2024-11-06 12:40:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 7135d8a1-b134-34aa-a201-888849e8bbd1 | -2.25428 | -47.6566 | 2024-11-06 12:40:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5ad10cfb-9d70-37ed-8aa1-d54073ba9668 | -3.39502 | -41.41835 | 2024-11-06 12:40:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 39f32ff2-98b9-355b-8826-84a067699379 | -3.75821 | -47.59421 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 12930167-9bb0-3462-a1ef-4de37b97a41e | -3.12382 | -54.26658 | 2024-11-06 12:40:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 1b103c54-3c23-39f4-9b16-547d8fe43e57 | -6.53343 | -42.07401 | 2024-11-06 12:40:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 4ba93716-8fcc-343b-9aaa-37e553ef4a70 | -4.23566 | -48.53687 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f51785c7-ca38-3fe5-a703-fda6cdb2b5a7 | -8.16729 | -44.88478 | 2024-11-06 12:40:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1e2a6361-13ac-3138-86b5-524ee1a6b630 | -3.3969 | -41.40516 | 2024-11-06 12:40:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 86189de9-cd2e-374b-ae37-c37c43098765 | -6.54282 | -41.91724 | 2024-11-06 12:40:00 | TERRA_M-T | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 518c9035-f3ec-3866-8bb2-043268a722d9 | -2.92588 | -51.04564 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2aa23cb6-3664-3992-942d-850168eb9302 | -4.30157 | -48.62104 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| de14d647-aa26-3938-973c-bd95c509bc44 | -6.51797 | -41.41861 | 2024-11-06 12:40:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 187a891e-3344-3ed7-942c-2f739201fdeb | 0.38149 | -50.97701 | 2024-11-06 12:40:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 566bd7c0-df59-3305-9488-c63d9bfe8d95 | -11.24267 | -49.44439 | 2024-11-06 12:42:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 46800140-d120-39b8-8a68-d96850849315 | -10.05185 | -44.77041 | 2024-11-06 12:42:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 541fe779-368c-3b9c-b347-40bf780b2c9e | -10.59705 | -48.76432 | 2024-11-06 12:42:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6a1076b1-fed3-3d9b-9fff-a7f0820e227e | -12.01232 | -42.84863 | 2024-11-06 12:42:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 29.9 |
| cfcb306a-16bf-3f4c-9be7-6d546529eab7 | -9.74155 | -46.27789 | 2024-11-06 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5f66d9f0-391b-345b-9057-a7dd37aa22a1 | -10.61305 | -44.9157 | 2024-11-06 12:42:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8f959c31-801d-3d5d-8847-98a89f33446e | -12.1656 | -44.62263 | 2024-11-06 12:42:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a4fd3dea-21ea-3044-9ceb-a7feaad82d25 | -9.56563 | -45.16928 | 2024-11-06 12:42:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1527130c-c1ed-3a08-8f56-f5ee1be86511 | -10.7556 | -49.0634 | 2024-11-06 12:42:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |


[Clique aqui para ver as próximas entradas](README72.md)
