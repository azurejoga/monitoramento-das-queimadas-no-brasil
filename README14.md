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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a92ba610-d540-3011-b88e-0bf7fb225a0c | -3.53997 | -47.37719 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc356869-487d-32c7-8860-6342de3a42b0 | -3.91347 | -42.4156 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a2dfb3d3-c240-35d2-80b7-4e971b28ce4a | -7.6997 | -47.28779 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffcaaa4d-dba7-39d1-8f4c-a80f6583019b | -8.07875 | -50.10715 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36894bb0-3749-3e59-aad7-764eb89a073b | -8.07324 | -50.09917 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a318d63-a9b2-391d-8481-caa6b6d928cc | -3.35635 | -51.5993 | 2025-07-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f453c367-4196-3b91-a9ac-10a518f0e112 | -9.53839 | -40.33011 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 517ce062-4b61-3f5a-94cf-3c68d26b6524 | -7.29066 | -48.32099 | 2025-07-20 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c0c1c40-9067-3833-8b65-2f3208a522a4 | -5.65041 | -44.35195 | 2025-07-20 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b586e5a3-bb78-360a-a8ae-d00c1476d65f | -3.27443 | -48.81362 | 2025-07-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acfe7c51-369b-3f04-9899-31af14745622 | -3.12692 | -47.00944 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc0912af-b9fc-3af9-8e6e-333b2a2aedd6 | -3.35698 | -51.59536 | 2025-07-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62835a6c-595e-3dc9-a160-4c185b5363bb | -7.26141 | -60.12004 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c4d6c6d-28a6-3206-986e-f89c5d49cab5 | -8.07435 | -50.11356 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82109987-b099-343e-858b-ee83c75bed52 | -3.12634 | -47.01311 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37972711-fe9b-34ec-a8b8-c25b55af4ca3 | -2.98001 | -49.10851 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c438c89c-1e24-3994-851d-e91f55cea655 | -6.92905 | -44.8378 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 402701f5-8b0e-37e7-99e0-fa801e98d6f5 | -3.13714 | -47.01102 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 479a2eba-f702-361a-99b9-e2456cefbafa | -7.69911 | -47.29171 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c5f77f00-3923-36f1-98d4-ed373f5cff9c | -4.25423 | -48.54767 | 2025-07-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 288cbd59-2d52-3612-9bfa-402e85edf385 | -9.63759 | -40.60483 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 725ecc1f-0c51-3d60-88a3-c161ef8f4cf3 | -9.1143 | -48.11627 | 2025-07-20 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8cebe85-4b85-3750-91f6-b89a20cfb69f | -8.74257 | -47.72967 | 2025-07-20 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce3e045a-8c1c-3e9e-83a4-667a50006466 | -3.91415 | -42.41112 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d935b2d7-712e-3c0c-a6f7-9f3e37549173 | -8.01365 | -43.68482 | 2025-07-20 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0bfb5bf-bcb6-3fc2-85b4-4330179bb28d | -7.69501 | -47.29508 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1acc9c1-5d8a-33e6-856a-5090aa82dde4 | -4.58954 | -43.31498 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bece61db-3b15-3518-ad86-5a9c7c74768a | -3.68712 | -47.4403 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03fc5f0d-ee4d-3fde-a58d-1849bb931f19 | -3.92244 | -42.41694 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72c8ee03-c5f7-303b-9adb-d00861c755bf | -7.48764 | -44.719 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cfb2aa0-4e5f-3d1b-a647-49b5c821cac8 | -9.11372 | -48.12006 | 2025-07-20 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e52b2d6d-a1e8-3064-91db-ad9107370252 | -8.07984 | -50.10021 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9d0a8ca-4d58-3a26-95f6-91d8fa0f57dc | -5.87113 | -45.20993 | 2025-07-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a2b806e-7b24-360a-831d-5ea371605bc0 | -4.25478 | -48.54422 | 2025-07-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60f11959-3e66-338e-a9a8-ee9412dfcf21 | -4.96394 | -43.23838 | 2025-07-20 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdd36cf3-41f6-3571-8cb7-ebd99d34307b | -4.82073 | -47.31704 | 2025-07-20 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d09285b0-7453-3c0f-8538-bc53fe54d7c7 | -3.27773 | -48.81414 | 2025-07-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ffec87e-81a8-3758-af6c-91cdeb08b7e2 | -8.08866 | -50.10873 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 157ce827-715d-3c6e-8f24-dd505c28252b | -7.42787 | -44.27802 | 2025-07-20 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d5a63d9-2fb4-3cbb-91f7-9b5b2e31ea00 | -4.25092 | -48.54715 | 2025-07-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 842b49f3-4b19-3904-9383-ecd382f05046 | -7.47513 | -49.45375 | 2025-07-20 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef445d13-69d7-3d15-8952-481e441e27fa | -2.63861 | -47.30582 | 2025-07-20 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89e4f4d4-6a21-3b0e-8b49-d873112069ca | -10.6689 | -46.7853 | 2025-07-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 94829217-9fd2-3fb3-9ab4-f7effe8e3ece | -10.6496 | -46.8101 | 2025-07-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 228f05a2-487c-3c78-8d43-666dd1be336c | -10.6499 | -46.7876 | 2025-07-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 5ad87e63-68c1-3553-828e-4e61ae283c2b | -10.6686 | -46.8077 | 2025-07-20 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f1d05e1b-9d51-335d-b2da-853663914c72 | -9.91864 | -48.00695 | 2025-07-20 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af506da7-c18f-3652-99e9-78f8cdbbc583 | -16.12936 | -47.49151 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1714c39-a51c-37d2-84d0-08641f96776a | -14.74699 | -48.28367 | 2025-07-20 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76317351-e262-3d62-9f11-65ba897c7160 | -12.03152 | -63.78096 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac03c61a-6085-3a37-9b6a-548adcf0122b | -9.91325 | -55.53065 | 2025-07-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6134f858-7593-378f-8e9c-3a0265ea306d | -10.97004 | -45.1036 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 11fd7f84-d74f-3e83-9130-89c1e58531f0 | -16.39419 | -48.99333 | 2025-07-20 04:40:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f65740be-2496-3184-afc2-11ccd103eb67 | -11.57867 | -47.85765 | 2025-07-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c910c954-b87f-35d8-9247-bfbb0f17bab7 | -12.68058 | -46.83309 | 2025-07-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edbee2c2-411d-366f-8b0d-4575e489ef6c | -13.5434 | -43.7075 | 2025-07-20 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67042f53-9088-35f4-9206-8505b398769c | -10.65799 | -46.80328 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 55dd424a-b966-346f-9ba0-f5faf97b2515 | -11.81381 | -47.50992 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0767d91c-8d32-36f3-a8e3-308171efc7d6 | -9.01724 | -59.5408 | 2025-07-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| add37b16-5abe-3c95-a56c-9c73a3cc75a1 | -11.82959 | -47.50354 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 345ac3e4-42d3-3e6f-803f-312a0cdb1ebd | -12.03278 | -63.775 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 52d72fb9-3eec-33f5-8708-a9b2372dd787 | -11.3631 | -48.72746 | 2025-07-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e2e0825-002a-3b25-8a60-fcceac69b396 | -11.55421 | -47.08931 | 2025-07-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 438989db-ae55-3408-ad69-0cd6cf9a7c80 | -12.35539 | -50.32147 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6875ab9d-4c56-31d1-8ea4-96ecdfb81a9d | -10.87701 | -56.09512 | 2025-07-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9934541e-a3d5-3ca9-8bce-7d9c6f6a5772 | -14.4792 | -46.35642 | 2025-07-20 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da2b1b4d-8aa8-3e1b-aa3f-ae1875790bd8 | -10.97418 | -45.10424 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 851d6da7-a5b2-3727-a313-6433085cadd1 | -12.3753 | -50.32466 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a94fad-715c-3d90-823b-67322f438c83 | -10.5486 | -49.49462 | 2025-07-20 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5687aff1-dfb3-3254-86a4-6838eeb854c4 | -9.77371 | -48.75079 | 2025-07-20 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b1cb350-9b08-3024-b428-f6ac80a12f27 | -12.52215 | -57.2404 | 2025-07-20 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0965182f-7161-30db-a0c1-4236302408f5 | -11.83386 | -47.49976 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d67f5c-3d61-3834-8962-a8ceffd400f6 | -10.38308 | -62.77039 | 2025-07-20 04:40:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c05243a5-6d5f-329d-a446-7f63741f34b4 | -12.68635 | -44.33218 | 2025-07-20 04:40:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c060a41-acb3-3f74-8430-2231dbe7ede4 | -9.01787 | -59.53739 | 2025-07-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43882a93-bea8-36eb-a4b4-fa35baf752a1 | -12.37697 | -50.33582 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1647cb7f-34c5-31c0-81b4-0f64c503556e | -11.36253 | -48.73124 | 2025-07-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6de7bd1d-f4b7-3693-a40f-ab934241a4a5 | -12.0158 | -49.52718 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b154241-241f-3eaa-99ee-843e9cad871c | -9.62366 | -49.02163 | 2025-07-20 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 803680ea-9df3-3edd-bdae-9a9e2b84e994 | -12.35487 | -46.42784 | 2025-07-20 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc596520-4a40-39a1-9eb8-ea81097c55ac | -9.77089 | -48.74655 | 2025-07-20 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63bc7c2c-6c0d-357c-ba7d-2fff520566c0 | -10.32265 | -48.52621 | 2025-07-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54137c1b-60fb-3f12-8788-84494eb282fc | -12.72163 | -46.40492 | 2025-07-20 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938168ba-299f-39eb-9aaf-01be42305317 | -11.80955 | -47.51368 | 2025-07-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0553d1b3-bab2-3fad-9ce7-90b724352c4a | -10.87766 | -56.09137 | 2025-07-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe037f80-e2b3-3e2c-98eb-674a2efb914a | -11.62577 | -50.73078 | 2025-07-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ea47bb7-8304-33e0-a1b5-d88e6f463134 | -15.24979 | -46.96777 | 2025-07-20 04:40:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27bdf4e5-26ad-356f-9921-e462a884f7b1 | -13.89844 | -43.87083 | 2025-07-20 04:40:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd1c92b4-45ee-3db9-8200-01b6ff17607d | -12.36708 | -46.42561 | 2025-07-20 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00e102f7-b0bb-368f-b309-e012f4424cd5 | -10.96537 | -45.10671 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a99726c-6167-3cd1-9643-a851d70a7249 | -10.67163 | -49.68452 | 2025-07-20 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df76a191-126b-3b9e-9dd2-346ed241883c | -10.65864 | -46.79876 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| bd308e7b-a22f-3b03-be92-bd79ef4a473c | -11.95835 | -46.75437 | 2025-07-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c58ca364-3aa3-33f4-9c8e-d0656c4c4c11 | -9.80242 | -48.56275 | 2025-07-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baa57cc9-9e3a-31f1-ba66-aa8a274d81b6 | -12.37862 | -50.3252 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 090346df-32fb-3762-a75f-295b3bf731cc | -9.47241 | -57.83314 | 2025-07-20 04:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80a15340-be5e-3a53-894b-8f24e8ceeed6 | -10.63264 | -48.09467 | 2025-07-20 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3577d7cb-4a43-3185-8778-d9973ecde655 | -10.69099 | -46.78517 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8c64656d-1140-3376-92ef-1ccb3aaf7522 | -12.34488 | -50.32341 | 2025-07-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d0786c7-77f3-3c60-bcda-8ce6aae8900f | -10.64993 | -46.80662 | 2025-07-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README15.md)
