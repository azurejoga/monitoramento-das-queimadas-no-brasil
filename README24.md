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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccc0ba4c-7f15-31ff-bb71-43f69f28d8bb | -6.32443 | -42.76789 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 510b5a7f-51fa-3bc5-9965-673ec8396b21 | -5.90762 | -42.80547 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 457eb11c-7d08-3d40-a35f-7059d930c663 | -5.3426 | -43.7453 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c8abc04b-9e40-373c-a400-974bb398fe72 | -5.5029 | -43.78512 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8290a3f6-2d61-323b-851f-e50869bf8fdb | -8.19923 | -43.98998 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7342f544-da7b-38db-92d7-6a8f26551ccc | -5.88277 | -44.23246 | 2025-10-15 04:06:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e09f9b90-0b79-32ef-a946-481579e83e40 | -6.79376 | -44.53123 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37054631-7dd2-3be6-85e0-8c1b348c15a8 | -6.22839 | -44.15895 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7fab70cd-ecc7-3884-a45c-c689fdfb5ad2 | -8.27977 | -43.6699 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 391ebea6-3b29-3e80-bd81-35802041373d | -5.90293 | -42.83465 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6728ab75-1fe7-33ef-9f02-4366f2337213 | -9.26152 | -44.36203 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d6fdde1-9a19-3ee7-8aef-747e5e98aca7 | -6.14458 | -41.76978 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 777346c7-8406-33b0-bba9-523972f8eef2 | -4.63815 | -42.52023 | 2025-10-15 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c68aee4d-88c0-377e-afe9-82ade52d23ea | -7.66832 | -42.37791 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0857d500-c7da-30ea-b7be-8460394f492f | -5.73351 | -41.31796 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe58cffd-0936-3f1d-b9a0-0fe68ecbece9 | -7.0747 | -41.94637 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6fed9f1c-54e9-3adf-bb8f-ab13d0262dcd | -7.50152 | -43.05927 | 2025-10-15 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ee1e348-3540-3308-bf15-870f8d0624e4 | -4.63567 | -43.7023 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1040d092-4ff4-3672-b208-e06d859bd491 | -5.62196 | -42.68297 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71eaa06d-de62-35e6-8fe4-4883a8aa6784 | -5.79791 | -43.88776 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d75b3b6-9bd9-3f6a-99a3-737d081b3050 | -8.20269 | -43.99054 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e70cab5-2b79-3442-9f1a-a2e358835b9f | -8.46002 | -46.16442 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3330baf-a578-3342-a724-d886c63c62e9 | -6.14182 | -41.76577 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb643966-13c5-3768-a844-6dc17ef2b359 | -6.43792 | -41.86962 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f65babf2-5253-3f6c-9e09-dedc20045e6c | -5.15939 | -45.16037 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28a2551a-e4bf-35d1-9b31-97df29dad600 | -6.20664 | -42.59825 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd1ecc2b-f57a-3b53-8d11-0ea00818d149 | -5.24304 | -44.47742 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a937d80-37d7-3503-a635-72ff63cab83d | -5.28916 | -41.0993 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 212bd443-8115-3dc1-b4de-ff1969c4dcae | -2.81125 | -49.21345 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cf989e41-fb66-39ea-8ee5-bd16cb06cac2 | -5.31542 | -42.91186 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9989b0f5-726e-3e10-9097-8317d4be6619 | -8.18029 | -44.0186 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce640f06-0ccc-3426-b022-3a329058f005 | -6.15947 | -41.71885 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b19b4899-7833-3698-bd0a-be6d1eed82e3 | -3.41954 | -50.25427 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aecce772-d420-35c0-9595-04cb1827fe30 | -10.16802 | -36.17054 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ede3410-43ad-328c-a2d0-c41cef238fc6 | -5.97833 | -42.86946 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c75d8e7d-89ad-3f1f-9a09-81d05de41b70 | -5.73134 | -43.82877 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b517a20-25ef-3680-882f-d27efb0dfce9 | -6.20328 | -42.59771 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b37cae04-815d-3302-bad8-4385401d5807 | -5.46914 | -44.65092 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42a2058f-b441-355d-baee-f5d29ff9d084 | -4.79779 | -45.71402 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 359a7caf-4470-324e-9f03-ec4b5960f2c9 | -6.57959 | -42.30452 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e01dfe4c-86ab-3557-82c0-ca93a4634d73 | -6.5898 | -41.51027 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a05767f6-b0ec-3840-aca9-11d892566dc5 | -5.31662 | -42.90447 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 770bb911-af38-347b-9efb-ca4f02f85c88 | -7.74193 | -42.45088 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5c41397-6f18-39cd-a993-fbf538bc6ab3 | -5.45852 | -42.36633 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 54ee9902-7038-34a7-9f2b-8d7fe26ad683 | -5.49167 | -43.78738 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70e5a764-6954-342c-a75b-c71ccc5a4e11 | -6.32385 | -42.7715 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38ea9497-fc2e-31e2-a658-dc834892a9b7 | -7.17221 | -42.20884 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa4863d0-af1e-386b-82a1-0b723e344402 | -8.30119 | -47.75676 | 2025-10-15 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd84f69d-0c7d-3593-bd5d-346c792cd931 | -4.31826 | -44.54198 | 2025-10-15 04:06:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69f6cc4b-969b-3383-a908-52c0a17b6870 | -5.85889 | -42.82748 | 2025-10-15 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b2b05a1-3679-3fd4-8f8c-4a826e5a1d72 | -4.29375 | -41.74014 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 322c09a5-c9c8-39dd-801b-fd7e3b1b92ad | -5.87964 | -42.84971 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24104493-3c90-3a6d-b3b0-81a1fac70831 | -5.91102 | -46.37841 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4caf8cf3-263a-3d32-9bd3-7818da189ba0 | -5.83446 | -42.3272 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d0e072bd-044a-373b-902d-793ed7d203b6 | -5.86685 | -42.82129 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e890619-fdf2-3879-8552-cdda74118e3d | -5.43823 | -44.22399 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 89a100c1-5e83-3691-9f90-bfd06fa732a7 | -7.95246 | -44.14567 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cbd7537-c97c-3cf0-adb9-a282a670bbda | -3.42385 | -50.26247 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a543a3-3ec5-3583-bdb2-4196c1843b5d | -6.89523 | -43.9607 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af6990fd-6b28-3ecc-927d-1c851c6cad73 | -5.431 | -41.34045 | 2025-10-15 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dde5630d-b0e3-3866-b6a6-537ed2f9e411 | -6.45461 | -44.58606 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d480dd41-1284-3554-b510-47af67e48258 | -4.89301 | -43.45881 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd65ef52-9ce3-3ea8-8e59-05ec53c9671e | -5.23011 | -46.23161 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea55d00-c766-3f1d-bf7f-bdb2451fa08c | -7.6722 | -42.37494 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d6ce97a-00b1-3979-9f65-75ec500a5040 | -8.24795 | -39.45691 | 2025-10-15 04:06:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a31a904c-a01f-3504-8587-2acd1f23c460 | -5.24741 | -43.46217 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c92a2004-f859-3ff8-8f2b-f35db8df0504 | -5.39123 | -44.0496 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b3223d2-dbdb-390b-8eaa-b8110536834e | -5.43463 | -44.22337 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2aab7098-054b-3883-b645-063a865f5c58 | -4.65696 | -43.12343 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a6c64da9-10b0-38a3-b1a9-686d0d2f925e | -8.12602 | -41.85118 | 2025-10-15 04:06:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e65bbce-8172-3262-8a81-434c3cf07fc1 | -8.2188 | -44.08806 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4cd25bc-1a4e-3490-81e5-76461ee5eb80 | -6.29892 | -43.57349 | 2025-10-15 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5db6dd6a-48e9-3f8b-99e3-be0affbabe5b | -8.24481 | -43.3424 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09877457-47ea-3604-a431-bd71611d801b | -7.5715 | -42.68801 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 544cd77b-7894-3820-b5e1-267201a76440 | -5.56975 | -41.32392 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86bbc40f-c097-31aa-a8a3-8eaa8fc731d7 | -7.0303 | -42.73654 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c87c9ea4-d56b-3872-b37a-5ee96b02f63d | -7.75136 | -42.45601 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4577c72c-1630-3ce3-9252-d1d6aca0b402 | -4.14416 | -42.21065 | 2025-10-15 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 99679100-d897-314b-945a-708a5cf1914e | -4.65919 | -43.13157 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7db1acef-6dbf-3242-a42f-dfe76b527107 | -7.25068 | -44.91657 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41bdc44-8208-3ba2-a4b0-e5512829ade8 | -6.33807 | -44.0195 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4dabc09-bf31-351a-a042-bb6fca115be7 | -5.47867 | -44.63903 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b405774b-06a1-3ab6-9564-a79513917888 | -6.68687 | -42.41608 | 2025-10-15 04:06:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d30bf81-3aba-3087-ab6d-cf382bf91567 | -8.1942 | -43.97733 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df5bbd40-f21a-3373-913e-3851d62c7078 | -6.95856 | -43.74824 | 2025-10-15 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31434116-4cca-3839-bfee-5c79b4da70cb | -3.42014 | -50.25067 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85dd1c49-3a37-3821-a53d-0d6fc7e4dc84 | -5.34324 | -43.74134 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99c9a522-ce9b-335a-9fca-915be147c396 | -5.56808 | -41.31307 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f5e93aeb-74b7-3589-9084-04c469941c59 | -5.40807 | -40.88483 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1c09df0-0c5f-39ba-8848-af116e37b83e | -7.57036 | -42.69511 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79dd0b60-9d7f-3316-832f-ba3a54a18b58 | -6.58021 | -42.96117 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1f5034e-7a13-3a17-8de7-06a84179b782 | -6.40775 | -42.57121 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff3e06c0-b6bc-3a48-a2e6-cc7bd2f0abf7 | -7.48064 | -42.15039 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d70e54bb-7557-3011-8111-85ea6af38de5 | -8.2049 | -43.99878 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 416ca689-4786-398c-a605-603978c60799 | -6.44136 | -42.53298 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1e33aec5-7464-3628-984d-7e90021503f2 | -5.13368 | -46.10876 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9975e9f4-9083-3679-a538-0ea6c95129ee | -3.83274 | -44.54916 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65bd4bc4-a90a-3fee-a9ee-36fb384bb37b | -4.14374 | -41.65943 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b3fafb1-33b6-394d-9d8e-d397c018ccba | -5.94445 | -42.31909 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 583b5460-4c01-364a-93bd-4dcd05264282 | -6.15341 | -41.77829 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
