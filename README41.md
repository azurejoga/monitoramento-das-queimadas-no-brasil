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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a26d929-ac07-355c-855d-a2c13d55409b | -10.8323 | -47.50138 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47a27d05-d866-3723-b41d-f6e709130d21 | -11.22456 | -55.05717 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84a0fc22-af17-3d6f-9685-132abda3e2f7 | -11.62208 | -47.31231 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b67794b-cddb-345a-b1cd-b42d097436a3 | -6.2377 | -44.76769 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02954cdd-a084-3647-aa79-5550fa04fa79 | -8.13698 | -61.21664 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6accb0e7-704b-3881-985e-c5d420a2e43c | -6.49539 | -44.3956 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 526c12d4-33e9-310b-b7a6-f8bab5f0af0f | -7.62005 | -42.69561 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e5016a5-cffb-362d-a2f5-e374ee395d0c | -10.02211 | -51.10701 | 2025-08-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 670f712b-215c-36ff-b28d-634f09c7471c | -12.66606 | -48.18929 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f96caec2-8b63-3ae0-9a66-6d4974d62890 | -8.70897 | -50.37201 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392bb8dd-3149-33df-8e73-934d5cbe548c | -9.46316 | -60.30494 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a5be166-ed1c-3827-8b31-ba1813c45004 | -11.16354 | -47.15054 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3bab2e9-d626-38c4-9ec0-02f31b0b9a1f | -10.49561 | -51.61564 | 2025-08-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f63c09-2e69-315a-a68d-6646b8fa6929 | -7.04912 | -44.36253 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa8f0a7d-c149-3368-9dc9-d2e3516f30e5 | -12.71039 | -48.15888 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3922d2e-bcdf-32a0-b906-c24adb8e6573 | -9.41833 | -60.57528 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51dd05d6-6b89-3f9a-bdd9-a90ab9ac09a6 | -7.63524 | -42.72303 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36a8426f-dc26-3f0f-acaf-aa98dbec7a20 | -9.44394 | -48.24924 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 559df284-9a51-36e1-a965-9e2b9d6e9dfe | -8.4386 | -43.65698 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8342fc44-cbb8-3540-8a79-4d0f1fa71871 | -12.83566 | -48.16869 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa67955f-8918-3f69-9174-c875f9ee8ec0 | -13.17563 | -43.52751 | 2025-08-29 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2893d424-fb93-34ce-822c-9a04deb4f38b | -11.92577 | -46.69866 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b332b4-3f22-37be-84d1-364082e03904 | -8.90893 | -47.32696 | 2025-08-29 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9da9d047-0291-3a3a-b8e5-e959e1018c2c | -10.46481 | -57.93694 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 55b310fa-0ba9-3851-af06-c691008fd296 | -9.3136 | -57.69745 | 2025-08-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd4d8bb3-767d-3d47-a02d-7c4a147ebafb | -12.84583 | -48.09916 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e497510-b0bd-33a4-bda4-e7d2063d3c1b | -8.17676 | -61.37933 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6dd1573f-2662-3a35-924e-a7da2e271a3b | -6.88335 | -43.61999 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a91f2335-5cc6-3ca7-bd53-137981a20024 | -12.7045 | -48.14941 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c81c726-82a8-380c-b3ca-3bfd57fb3e2d | -11.23032 | -55.06055 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a67a92cf-94f0-3579-84de-4d8cd7099001 | -11.40796 | -46.90997 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b323f1c6-892c-33f1-9d98-9b2de235fb4e | -6.16418 | -44.18819 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42f3c085-60be-38a0-8020-50660a88792f | -12.69794 | -48.1945 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 2906214d-d938-30ea-88ed-92c86e0c0323 | -11.31635 | -43.55296 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaad1e6e-4c9b-36c8-b7d0-b533bc1b29d7 | -9.16416 | -59.55524 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e04235-fe7c-3594-aa4e-faf72ce13ddc | -9.78645 | -64.2499 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 68d87ba2-a425-3b12-b669-41de14315220 | -8.71227 | -50.37254 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b33601a-ad2a-3b12-8a34-ffbb9de39ede | -6.40099 | -45.21409 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507d8588-62af-39c5-85db-c34e40701048 | -10.85508 | -47.4963 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22c2cffd-8746-3085-8845-232ea2fbcb66 | -9.24569 | -59.78958 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6347e66-a544-31ae-96ed-de6a49efe913 | -6.22362 | -43.33237 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd0d6dae-0a36-38cb-834a-54a58675465f | -12.90461 | -48.13941 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2231d49d-9451-326c-931e-b75cb68146a0 | -10.97706 | -46.91829 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 1b09c769-48e0-3ebe-9e9a-3218ea219a36 | -12.92544 | -48.14649 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0a930c3-610d-3f26-a571-760e44fbea8a | -7.73199 | -50.29021 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83a94d5d-4a49-3097-9463-8f9a42d4187d | -6.30115 | -42.48975 | 2025-08-29 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cb6dd4ed-ec83-3d62-bc54-866157a23bfd | -11.63778 | -46.38174 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d0d1d25-5551-39c5-b2fa-81d0612638d9 | -11.24356 | -45.00999 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01e088bb-d792-3b90-9166-55dc89876c18 | -6.8817 | -44.45901 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad9e6dea-ea3d-3bc0-94c6-3dd21bab3949 | -11.3374 | -43.28708 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4396ad8c-e7ec-33a2-8915-191996bf98d9 | -9.45845 | -60.56191 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d062be6d-d1fa-3b1b-b355-35a37e8e79bb | -6.53196 | -44.10997 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9af8f32b-f39b-3d60-8be2-227c4293d4a3 | -6.14471 | -44.43044 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3bc147e-f5f6-31ed-af59-f4fa65b974ca | -9.15458 | -59.57724 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844a1a93-1f8e-32b5-a60a-426709c550cf | -7.04605 | -44.35459 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e4276dd-e663-3fab-92b4-f94cda5963b9 | -10.38463 | -45.16785 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4faf2731-e707-321d-a603-26629d9caf1c | -8.48033 | -43.68052 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28014d5c-9165-3f07-b98d-372ce6fa7da9 | -9.94251 | -46.69999 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1ca92eb-b962-3b81-b8ef-ec66859bc102 | -6.48802 | -43.53349 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77d895ac-7a9a-34f9-ae0a-5d0e29c7c1c2 | -9.17237 | -59.57057 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d826a47-4d38-33ea-9aa0-27c384467902 | -11.30774 | -43.54666 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f99b59a9-4ddd-32fd-98f7-1b4908345441 | -12.41692 | -46.47843 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db09f0c9-827c-3c09-a4e3-a0f7c07793c0 | -12.83861 | -48.17338 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37b53a3f-8b3e-3fbf-9270-f0826ef30b22 | -10.4501 | -57.96497 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbde89b1-8ebf-3cc8-9081-62624de7e485 | -9.656 | -48.33044 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2e78d67-7fff-3509-abe0-8422170f1d3b | -9.49923 | -45.38114 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1314d4b0-72f9-38f2-8afb-dae5d2433b8e | -7.96837 | -46.37498 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84bf20cb-a5c9-3eac-bd64-79019867a873 | -11.08512 | -44.77443 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d5cb0c-9c83-356b-a842-57f21c06b862 | -11.09312 | -44.74707 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 391a3dfe-6ac9-39fc-8d50-d29670e75ea2 | -9.67711 | -48.33007 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 559ff40f-f635-3e14-b08c-5797ee0bea58 | -7.72705 | -50.30008 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aebf4719-98c1-3777-a056-5fad40e02926 | -10.47891 | -57.9663 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13c2f65d-92dd-3a14-9156-c2b9f7a3fffb | -7.72869 | -50.28968 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfaf6c58-bab7-3302-9413-3ed3def817f9 | -10.37509 | -57.83182 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 920cd545-3ce2-39ad-8e18-a7165ca10897 | -9.9379 | -44.02108 | 2025-08-29 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b3a33a0-88f3-3316-99ae-4056fd1534a3 | -6.19368 | -43.3234 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa45fe58-3518-3ecc-99a5-68ae1ab1d76c | -6.12468 | -43.30143 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4d971d26-ad60-3f6e-a642-82aad50a0928 | -11.08671 | -44.76252 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a258fe2-a332-357c-981d-253fe37ad235 | -11.03294 | -45.06794 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e58b7f-27dd-3e26-8fb7-e72478a90df2 | -6.26761 | -43.81209 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2bf5207-5d13-3d13-9956-e95710f7382d | -10.97969 | -46.90035 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f7680c8-571c-3212-ae42-6a7664eefb50 | -11.06013 | -44.76675 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f5c023a-b0a1-3d12-9fb8-73352939e86b | -8.17851 | -61.36998 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73a0c9ea-eb0d-3a0e-b454-02d0ebcec797 | -11.46179 | -47.30939 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff6f428c-2a2e-3807-869f-1e1f5a843778 | -8.70512 | -50.37495 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a98b339b-6482-3d5b-ae79-e63866f18ad2 | -7.16427 | -44.16175 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 332e4811-fb83-3df1-83eb-9fc6089f07ec | -6.89043 | -44.45644 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fa7ab31-3494-3252-9a9c-061f2964b2ab | -6.54502 | -43.92709 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| fcc72066-af4f-3361-b8f6-83e85c360046 | -9.17175 | -59.57398 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 003e20a6-d321-3951-a6b4-32c9394289fa | -11.12532 | -45.11972 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32282e91-83bf-352e-98a0-88b136d9a3cb | -8.45209 | -43.68962 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f2baecc-3a70-3c91-b960-f678de622efa | -8.18893 | -61.38161 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 620732bb-6ff9-3a7e-990c-ba300bffe270 | -9.16709 | -59.56931 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d5b6cf-0ba0-3939-aa7f-494caace6614 | -9.46728 | -60.56437 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a7d438-9d93-3c39-bd63-c081de3e0223 | -8.45734 | -43.71648 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7462030a-c9fc-336a-9003-d7d00c570526 | -6.56642 | -43.69148 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ddb3b56-53fe-34ab-8bd0-e2e5456d9565 | -12.68848 | -48.18476 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5899d08b-f48f-39cd-b16f-e671f230589c | -10.98406 | -46.89645 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 03e89d7b-5656-3ea3-a3ed-c57bbd905109 | -7.63279 | -46.54547 | 2025-08-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd7b515f-89a0-31b6-b11e-2b3f843e6f90 | -11.87914 | -46.39972 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |


[Clique aqui para ver as próximas entradas](README42.md)
