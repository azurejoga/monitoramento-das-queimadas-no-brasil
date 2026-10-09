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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffc36684-63bc-3b26-a268-75ecd86f2da7 | -7.3913 | -44.7477 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2b55733-147d-3c90-bb29-e2f37675e156 | -7.413 | -44.752201 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2e7599-44ee-38de-bf45-d15cc1cf9726 | -3.292 | -53.9935 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b631c3-a10b-3e91-bf32-51c083777161 | -8.9127 | -45.161999 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04d527e8-7c9a-3307-94b1-23b6bf78b7fc | -11.0893 | -44.055099 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecdde53d-4b52-3d98-b2a3-1610286a5ef4 | -8.79 | -47.2696 | 2026-10-09 00:06:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70d4420e-8c5d-31d2-8a39-5bfa0b851c5b | -4.7541 | -44.009998 | 2026-10-09 00:06:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cca3e4c-d940-3377-b913-c0c65d977b9a | -9.1208 | -45.834702 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 41f7a141-08f3-3c5b-a7b2-2b04c9c10740 | -4.5599 | -54.206001 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd311e12-5eaa-339a-92c9-7a2f8301ecce | -2.2265 | -58.0965 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24de00b5-d1f3-331e-b6b0-acc2a4069fec | -3.2325 | -52.249298 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34582bf-a70d-31f2-bfa1-05314c4d8228 | -3.0005 | -54.761299 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4965ee0-47a9-392e-ac8a-9252e371b2ed | -8.9087 | -45.1894 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1789cbf9-6ae7-3026-8253-747030298ae7 | -4.995 | -45.306 | 2026-10-09 00:06:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1630dfff-58ee-373e-a2b0-610ead48bab1 | -3.7194 | -59.428001 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9a47e2c-4e7e-38dc-b9fb-08e77bced2cb | -13.2126 | -54.360001 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9dd2fdc-097e-3561-9e6d-143d3519367e | -7.212 | -55.167 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28f7732-dd12-3397-893a-c24d54cacd74 | -3.2941 | -54.002998 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0b722f-db2d-3fc1-bd6d-4f3862fdcbb6 | -5.7137 | -41.7677 | 2026-10-09 00:06:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53d1e432-4f04-38a9-8d25-38a8a6d730c2 | -4.2855 | -49.0952 | 2026-10-09 00:06:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85013e7-52c2-36b2-a154-cc0b8981acbb | -3.2017 | -53.864399 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5a4529-ceea-368b-9ba5-e4228ef9412d | -17.8365 | -52.347099 | 2026-10-09 00:06:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5ad57eb-4c62-3594-9c3e-cafd7f7b03d8 | -3.3466 | -50.415798 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb21b802-663d-3ad6-9dfa-d53949f5a951 | -5.3813 | -45.949001 | 2026-10-09 00:06:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5640abc3-e247-3b59-8f32-0f43a2784a58 | -5.9645 | -55.3489 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52eb2c46-8d25-3981-a274-d314aaeaade6 | -2.9467 | -54.1492 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c3a72fd-d498-38fe-9b6c-021e5815b716 | -2.936 | -54.101002 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f6f736-dcd9-3d9f-8af2-e9d3bfc89617 | -6.7272 | -55.0952 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d449431d-3108-37c7-a835-bc565bbdb44f | -3.2869 | -49.511101 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74965eb0-bb2a-3b1c-89d0-69344ef7aa3f | -16.993799 | -41.179298 | 2026-10-09 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d62ebea-daa8-3380-90de-1f3f611e89f1 | -2.7511 | -54.1012 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee26d657-5839-3933-a364-baa200dac310 | -8.9047 | -45.216702 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6542f2d8-9242-3177-b576-a7ba785b4a44 | -1.1034 | -54.1782 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4147b9a1-ac32-3263-b5ff-1a11192d553a | -13.7311 | -43.863602 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f14f701-2998-31d5-b903-d1176ba71950 | -3.8106 | -44.5993 | 2026-10-09 00:06:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d27bd6e7-1059-326c-96c0-4ca876d58145 | 1.7504 | -55.560902 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1700807-fad7-3bf1-a18f-cf553d92b308 | -10.8747 | -44.809799 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6defc1a5-d11c-3349-81b0-398afc0427fd | -13.1675 | -48.1339 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36582714-8aec-3558-9008-126f9aa71880 | -4.9847 | -44.995701 | 2026-10-09 00:06:00 | METOP-B | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 129d1112-fca5-3aee-b692-ee62271fff47 | -6.382 | -55.247398 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ef23b6-cb0d-35b3-9aea-746cea5094cb | -15.3424 | -42.770802 | 2026-10-09 00:06:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4aeb3e26-8957-31ae-b7f0-871723139311 | -9.8945 | -44.813599 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cdeacdfe-fc0f-3572-9177-69a2a408f599 | -5.6917 | -53.4743 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1569f5b9-0e08-37c7-8197-bf006b396a29 | -14.5505 | -50.033699 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0cdb252a-020c-339c-b914-b2abc53a78a4 | -2.8239 | -54.1054 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c838e3cc-dc8a-3f37-8ccb-8d2f6a9ae81c | -13.1582 | -54.341499 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 599c308b-45a8-3ed5-9408-de0072914024 | -13.7526 | -48.127499 | 2026-10-09 00:06:00 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d14442f2-4ee2-330f-8c83-e91ccd42bb2f | -3.3451 | -50.409 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b30c4e-7ead-310b-a299-bc1856c3b492 | -7.2315 | -55.162899 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebdac7c8-5da2-33d2-8812-cc96c872f2dc | -9.8925 | -44.805099 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4c5596-ae15-3431-a1aa-a88e5346921a | -8.9145 | -45.214401 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1d55342-7a14-3088-b189-09c404d66931 | -14.0538 | -43.829201 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8536942-7434-3b06-afd7-90da7d4b27cd | -4.9972 | -45.315102 | 2026-10-09 00:06:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04bb7edf-5f76-3f11-98eb-8ef965b3f3de | 0.5195 | -50.777302 | 2026-10-09 00:06:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ede8e924-2e4e-3936-aaae-79098c611d1f | -3.9859 | -59.348 | 2026-10-09 00:06:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea32f97-c476-3781-af25-7eb8bf2dcffd | -13.2566 | -43.9991 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3ffcb12-a5cd-3bb7-a7cf-79951272bbf1 | -17.834101 | -52.334702 | 2026-10-09 00:06:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08615eb0-f83a-3cf5-b40b-b272469be35b | -2.3754 | -48.220001 | 2026-10-09 00:06:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e78d752a-f498-3739-af0f-f5f53082b099 | -3.7637 | -58.557899 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f82da2b-fad3-395e-a5b1-d7234d53af40 | -3.2129 | -50.554199 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c389d1-ed4e-3142-ad98-3d3420451dbb | -3.0889 | -53.957901 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8e52f4-9676-3f22-ac32-566f65422cd9 | -19.870001 | -48.318901 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afaba575-3fef-3961-baa7-fc493b6e31e7 | -3.1005 | -53.779202 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ccf83f-23dd-3c61-89e5-2dc11ac1bbe7 | -11.1984 | -45.311501 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99aaf53b-9f01-316a-ae54-88813ad81416 | -11.859 | -43.555401 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a76f6512-0ce1-3444-a414-bb7220d37656 | -2.9326 | -54.132099 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 423b3a4c-720a-34ff-a9d7-0c214b077784 | -3.7437 | -59.446602 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 564adc52-db71-3fb9-87f6-397c94ce4f52 | -9.8982 | -44.785702 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04621feb-f503-3733-b0ee-402cadc1dac6 | -13.1833 | -54.365898 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6c77307-e57d-34ab-b08d-738bad440e0d | -3.0793 | -54.2841 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61f2327c-9920-3f59-bcc3-b7f72f30883e | -3.2114 | -50.547298 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3695b7b-9026-3210-8135-0023d9980c4e | -15.3349 | -42.7827 | 2026-10-09 00:06:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c35ff083-553d-38e3-8420-7cfeed24e703 | -2.5107 | -56.155899 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4352b0ab-0cf3-356c-8231-21e3cae1492c | -2.2549 | -45.4398 | 2026-10-09 00:06:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eeb3bbab-1539-379c-b5a6-7877ebe2c756 | -13.8694 | -43.792702 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c313af7-e859-325d-b8cc-13b772d9d686 | -10.6974 | -44.494701 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89bd5147-bef1-3cd6-9902-bb45eec53ae1 | -2.7413 | -54.103401 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74af6f2f-7578-3458-85dc-a9267ae39f12 | -3.1217 | -54.151699 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2eb186-2951-365c-b037-b4354a5740ab | -17.8244 | -52.3367 | 2026-10-09 00:06:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1d0e543-5627-3f9f-96b1-25fe83aebf6d | -1.121 | -54.1647 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 504a0191-1696-37d1-a4ca-9cf101e31d32 | -4.8039 | -56.1227 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d56327-01fd-3728-a101-33415867507b | -4.9466 | -49.4207 | 2026-10-09 00:06:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8567438-2c2c-3bf5-85e1-6195f27fe64b | -11.4655 | -43.379398 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18eca592-38fe-3e43-9203-bba193f29aa6 | -0.998 | -47.647099 | 2026-10-09 00:06:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01d27fa5-2e80-3347-a65a-ea1d1819ec4c | -9.869 | -47.48 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca18cd94-511e-3eeb-bd8c-558e8ebf3e1d | -5.6947 | -49.081699 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad73dba-e620-3dbd-9ee3-286ee08908ee | -9.769 | -48.18 | 2026-10-09 00:06:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f27914f-73a8-3dd1-8ffa-4cf4be4f6f69 | -5.9702 | -49.711201 | 2026-10-09 00:06:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8de7099-0386-38ed-9337-773b0ac94831 | -12.0204 | -43.495701 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b384349e-8426-35ad-8b3c-cdfac519c2c5 | -5.6181 | -44.838699 | 2026-10-09 00:06:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a889dc41-8bb1-3ade-9396-e29fcf6f6790 | -7.219 | -55.151901 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54729b17-4e77-3b6a-9ac6-23cd23c5715c | -2.0664 | -56.8727 | 2026-10-09 00:06:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f777cfc5-e804-35a3-98b8-9822ae5855f7 | -8.3406 | -49.117802 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3054d2f-7948-322d-9d5e-12518523bb16 | -8.9633 | -47.532902 | 2026-10-09 00:06:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fab9755-2c15-3232-8dda-457ebce3fc8d | -4.6305 | -50.9501 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e54e63dd-4cd1-3491-8350-d1722b57ee49 | -1.1078 | -47.7672 | 2026-10-09 00:06:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17603e2-c7af-3793-91a9-aa9a4c251357 | -11.7623 | -45.471901 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2026bb0e-9985-3322-993f-052722ef106b | -2.7533 | -49.522499 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9bfab0-d16b-3ec0-945a-b6c58b645bc5 | -7.2217 | -55.164902 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d981c41d-f224-3c09-9b56-6a99350f0548 | -4.1476 | -47.987701 | 2026-10-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
