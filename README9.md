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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fec50c0f-c166-3a47-bc5c-1554cbae544b | -4.80772 | -43.53466 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00dc844e-0de2-320a-a678-71f11703e6da | -3.30008 | -42.17582 | 2025-09-25 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b4566de-3da8-3bbf-a447-225b3bac00a8 | -4.6068 | -43.91798 | 2025-09-25 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 802b6980-122c-3263-98b2-71fd97673adf | -5.25999 | -37.66753 | 2025-09-25 03:40:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1c9169f-475b-3451-9989-8cca1ab5242a | -4.745 | -43.6172 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cac9ca7-01d1-32b4-98ca-1feff20b91d6 | -4.48669 | -41.45813 | 2025-09-25 03:40:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9cbe6ef2-0a0d-30d7-9782-1c64c9148a1f | -6.07118 | -44.08187 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c467ae92-48c0-3635-8e50-067aa9117293 | -6.56551 | -41.36333 | 2025-09-25 03:40:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c6019541-8b89-3e6e-b1b3-eb28eecddb1e | -2.91713 | -48.30298 | 2025-09-25 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b92e57b5-01f2-3bd6-909c-cabe5e6cec3e | -5.01582 | -42.79728 | 2025-09-25 03:40:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1a902c6-2a25-3f42-8f9a-820f723f1505 | -5.79034 | -42.80968 | 2025-09-25 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6db36fef-79fa-3343-9ef7-58645d64446f | -2.92432 | -48.30422 | 2025-09-25 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 831056df-86fa-3a68-9e7a-5a94cf301db4 | -3.23588 | -46.80413 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46cfaff1-c586-38ad-b241-f259c5bf6ebf | -5.7684 | -44.27707 | 2025-09-25 03:40:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b3f43fb-5f72-3c1d-b35a-fc53db57bd5a | -5.08826 | -37.6079 | 2025-09-25 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ff0bbac-6dc1-36d9-a5f2-7c84d8182b87 | -4.86653 | -37.45676 | 2025-09-25 03:40:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4032bdb7-91b3-3809-a88b-cd162f167c40 | -4.60205 | -43.91358 | 2025-09-25 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6df29758-1d51-330c-b453-624808e245d4 | -5.78543 | -42.80909 | 2025-09-25 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4a30decb-7a50-3277-9055-b29dc881e253 | -4.77644 | -43.20778 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d2de3b2-b9fd-3412-8c99-89d076acb16b | -6.30422 | -42.53533 | 2025-09-25 03:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 318d05e2-dab0-331e-8192-928331a92c5f | -6.90057 | -38.57204 | 2025-09-25 03:40:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d5c27ae-0dc0-33fd-99af-115610d2cb26 | -3.78914 | -41.74662 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fe0abd0-a86c-3b5d-b669-6100f23f946b | -5.7503 | -42.61443 | 2025-09-25 03:40:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a760f4f5-d267-35f0-ac05-5369b4999914 | -3.43961 | -44.48245 | 2025-09-25 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| caf55438-473e-3fa3-ac13-e9ac4a1d6351 | -3.4383 | -44.49011 | 2025-09-25 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e94bbda-796c-3800-9e62-a6f6e3dbac55 | -5.7847 | -42.55655 | 2025-09-25 03:40:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e859d5a1-c067-3022-92c4-a30e598984ee | -4.80556 | -43.54729 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b139912-231d-3973-92d8-2c17cf23c46b | -5.95391 | -42.91048 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 31b20588-bc3d-363d-bae3-184baabfe67b | -5.24538 | -43.07762 | 2025-09-25 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da443747-d79a-355a-9407-550a8d089515 | -5.70428 | -44.99442 | 2025-09-25 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ad6671c-7a91-3511-901c-f2ed8a5a70e4 | -6.56986 | -41.36414 | 2025-09-25 03:40:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 01f57b6e-24eb-37d5-8f5f-c1c3e89f9cbf | -5.95489 | -42.93369 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 15fc715f-f9d1-3f98-9d1f-c6e6cb8ca708 | -3.78146 | -41.7351 | 2025-09-25 03:40:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b912f039-37dd-35df-af91-d2738c809b42 | -5.759 | -42.5629 | 2025-09-25 03:40:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2cc78ba8-4eb7-3bd3-8f41-9ed145e3de29 | -3.90083 | -38.59349 | 2025-09-25 03:40:00 | NOAA-20 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 303b7566-a206-3a87-a1f3-eb9b7761096d | -3.23508 | -46.79926 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c30268c8-d005-3fc6-89fb-959ee159c461 | -5.41846 | -41.31311 | 2025-09-25 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90e010bf-8996-3d1e-87b7-4338f452cbf4 | -3.29919 | -42.18118 | 2025-09-25 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4652f890-ef87-3444-b477-52cf5af39eac | -4.74492 | -43.61852 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8df5707-c5ae-32b5-b707-31019da37aa8 | -3.61267 | -38.76444 | 2025-09-25 03:40:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 62371b0b-036b-3019-8259-35ebe9a4ed43 | -6.57054 | -41.36015 | 2025-09-25 03:40:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab0b2c57-62ee-3554-b113-2bd1d3abb494 | -5.93355 | -42.9273 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f2b94f3c-8a0d-3c21-94b2-1d29428e02d9 | -2.82935 | -46.72782 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 931f24ca-7d00-3e84-ade3-7c70a34c1fe6 | -5.23237 | -43.69842 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dc30f5f-b1de-3dcc-9531-58cfa2996149 | -5.60865 | -43.00037 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 81a85701-db5d-3a57-ad3f-2bfcbb4f08ee | -4.01117 | -43.27244 | 2025-09-25 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 386dc95e-863a-3846-a98f-5e221a90c020 | -4.76768 | -42.70921 | 2025-09-25 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6e08c03-d33b-38a2-bd4e-03843c10de35 | -2.91509 | -40.3866 | 2025-09-25 03:40:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| bee7cb87-b0c7-36ba-b7d5-1eec4e8d517b | -4.79417 | -43.04115 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b0e6094-02fb-3d29-802c-8574854626b2 | -6.27813 | -39.68923 | 2025-09-25 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 355d533d-f381-3887-9027-12a876ecca47 | -5.23344 | -43.6922 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3825162-db3b-3f98-89bb-4e863a458257 | -5.38798 | -42.2924 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fe4dde71-0ae3-3e9a-a6c0-02d95186d5a7 | -4.77 | -42.70527 | 2025-09-25 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a740fd9-d4a1-3de3-a7c1-1284f8f41325 | -4.80254 | -43.53365 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b6f8300-08d7-3004-b377-05653aaef9ec | -4.56427 | -41.49658 | 2025-09-25 03:40:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46523702-732c-3f38-a03e-6d18b3563eda | -3.81166 | -41.55557 | 2025-09-25 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f94a72b4-cfb0-3c1c-8dc3-fecd7e22b69c | -4.6719 | -38.40708 | 2025-09-25 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69934f4b-bef4-3d4f-ba90-88aa99d76e13 | -5.38887 | -42.2873 | 2025-09-25 03:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 91a4486c-76b5-37e4-b7a1-88a4ed223118 | -3.43895 | -44.48629 | 2025-09-25 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fc7136d5-d047-3554-a458-f667ab07fba8 | -5.72519 | -42.61662 | 2025-09-25 03:40:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c702c2f5-e057-3ea3-b03c-732fe6c2072b | -4.00599 | -43.27157 | 2025-09-25 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b1b4ca5-ddf1-3aaa-84da-8e375b51db8f | -5.93748 | -42.93389 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2a2ec0d9-acc6-3606-aab5-227429836ccf | -4.80038 | -43.54624 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af131ecd-e5cd-32fc-97ff-1a6a65bce1c2 | -4.79368 | -43.04405 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c37aa462-081e-3c09-adca-3432b5649f87 | -3.23414 | -46.80468 | 2025-09-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df031b88-4c2a-3f0f-8484-cfe38f419240 | -5.60792 | -42.99918 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2528dd7d-1447-30a2-9de2-d8be87b90a15 | -6.0765 | -44.08255 | 2025-09-25 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d600eab2-7d28-30ac-a304-2a466152d3e5 | -6.30334 | -42.54048 | 2025-09-25 03:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4b26ffa7-93ac-3a73-a24e-f730b91908c9 | -5.95279 | -42.90262 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 900b1444-fe75-3d6a-a692-5947e3a753af | -6.32083 | -41.88654 | 2025-09-25 03:40:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a83cea75-808e-3757-8d24-7d359b97b550 | -5.909 | -42.99329 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f58f9392-d5de-3278-b9e0-51074ebe07a6 | -5.93643 | -42.92393 | 2025-09-25 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0eaad245-99fe-3414-93b2-212737c5417b | -4.78153 | -43.20864 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a6492f9-1193-34c4-a32c-51b49d64340d | -4.01065 | -43.27555 | 2025-09-25 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ee68312-a2f1-324d-8a51-fe211e17ba91 | -3.80704 | -41.55483 | 2025-09-25 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 687bded2-2df4-3108-92e5-e0cb0e67d24c | -5.29377 | -35.5658 | 2025-09-25 03:40:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50b77e6c-d3cf-35c6-a4dd-dff0c34ba3ac | -4.79682 | -43.53582 | 2025-09-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3400699c-6f0a-3016-b4d8-858d3bb9d564 | -3.7455 | -38.95564 | 2025-09-25 03:40:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ad5ca87f-21ed-3bfb-9bed-d4266ebaf6c4 | -3.30097 | -42.17046 | 2025-09-25 03:40:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3fa60bf2-e53f-31a8-af71-31d40e974c8f | -11.63664 | -45.35278 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fa6fb49-3364-3bea-9298-1beec3c8700f | -6.689 | -44.62114 | 2025-09-25 03:42:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aba13a3a-392d-3763-a4e6-b3c797a94be0 | -7.37685 | -47.04895 | 2025-09-25 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9c54da2-14fd-361a-a3d9-f4b67188637e | -6.426 | -43.08902 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b45a8caf-1554-32c3-b27f-17f4d3a44ff8 | -11.64386 | -44.43229 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 038ed1e9-33a0-3832-bece-a4bd9d41bcd8 | -11.01909 | -45.91333 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22730dcd-36c0-37bb-9974-4453a8792598 | -11.63604 | -45.35597 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919e5400-30c4-3157-aa19-e30e67bda666 | -7.26162 | -44.91128 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c16e6a4c-1c2f-394c-ba41-858350be1459 | -10.18909 | -44.84857 | 2025-09-25 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92faf143-712e-3c55-bb19-a8e768e17361 | -6.39536 | -43.53172 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93edd6ad-5f60-3891-a9c7-c5b04e7505b0 | -11.64492 | -44.42668 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f3e6f6-a17d-3eff-ae2e-a9b843fe0096 | -9.05839 | -40.52443 | 2025-09-25 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3207e803-0f8f-38a4-89cb-80aeeb1be414 | -10.93525 | -44.27226 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac221047-2331-3b23-a886-a460135170ee | -10.80207 | -45.3843 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a363693-a67e-3074-a51d-e7539971c989 | -11.90858 | -44.78045 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c467dad0-6da0-3539-9b7e-9384d6245c15 | -11.41792 | -44.92617 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fb80bd7-bc1a-3b29-9b5d-868a825443b8 | -7.58991 | -42.33414 | 2025-09-25 03:42:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f95055ed-0e6c-39b5-a48a-e92f922722d3 | -10.59317 | -44.07819 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3cf4da2-8aa7-3f46-8734-e9b610e7a6d2 | -11.92737 | -38.33123 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4da99d70-9f62-3052-9c23-8bbb2b61024e | -12.0545 | -44.82819 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fe33853-336f-3f6d-af34-d6f82420e84b | -11.7845 | -45.57142 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
