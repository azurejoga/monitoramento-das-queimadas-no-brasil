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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ec19fec-67d2-388f-8aec-a73aaba49c0c | -9.39833 | -48.4535 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5bf719e1-6349-3b77-a1b8-e62617fbb3d3 | -6.93687 | -39.62688 | 2025-11-18 04:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b05eb5b7-43e5-34c3-adf8-52d7066591a8 | -7.94855 | -46.82612 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95cca06b-0c09-3638-bf4a-a5fb3bb9df15 | -4.18177 | -44.24022 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99e3f24a-fcc7-359b-9598-dba44499273d | -4.97036 | -44.67926 | 2025-11-18 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2fda664-568b-3797-9a7d-753e374d7fa0 | -10.38254 | -47.50255 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1cb389a-80e7-303a-b7f1-1b6e9a1eea8e | -3.49213 | -54.05125 | 2025-11-18 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6ca29ef-2a1f-3fe9-8a67-2fe597e88e4a | -4.27301 | -44.24453 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 590216e0-41f1-37c7-858f-0454cd9cb5a8 | -6.08634 | -41.67904 | 2025-11-18 04:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 58fd7f4d-64e1-3dff-8154-e675cc6bf2a8 | -4.67065 | -45.99466 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 732cacd5-91f6-3d48-bec3-836d21f7d7e8 | -10.8053 | -48.09126 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fc7b046-90a9-36a0-a3e7-2bb10b55ab5d | -6.83604 | -46.29793 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57de8a7b-e50e-30b5-989e-053bb2a71057 | -10.82835 | -48.03878 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db514f5c-f394-3e0b-b5b3-ab5024b7fbcf | -7.54328 | -47.05084 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb3b80cc-cc00-39af-bdd8-33b8e419e361 | -10.85847 | -44.09611 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 234084c0-9db1-39d8-8d38-97db5dcbb012 | -8.93763 | -49.84516 | 2025-11-18 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e00fae8e-cedb-3342-a78a-07265b271f4c | -10.91655 | -49.41152 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34a0d565-afe0-3aa0-8e35-08b878bd1c56 | -4.44534 | -47.99169 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cfec9cd-b7ca-3520-927e-361af89b6cbc | -5.39517 | -44.46743 | 2025-11-18 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 395dfe7c-fc7e-39c3-acbf-34179184eca8 | -7.70378 | -42.94009 | 2025-11-18 04:21:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 69e1959d-3bbf-30ec-9a62-71dca6db8f69 | -6.83456 | -46.29795 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0a4eb49-ecd3-326b-a434-900cce97dab4 | -9.74236 | -43.94737 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 603042bd-d84a-3fb6-a87a-e0d02f9941ea | -4.72604 | -46.37606 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f7b5277-da04-3eab-befd-0b4e512644b8 | -8.57536 | -46.49164 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 652dcd78-fae2-37e7-9bf9-9a3e31a91131 | -4.7506 | -46.3995 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b5297d-133e-35b9-b517-0a556297774f | -3.25101 | -50.69146 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec512581-418a-3e96-8ee6-768cb6b13762 | -4.18231 | -44.23679 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d7574370-3b56-390b-9051-504babea0700 | -4.61563 | -41.7329 | 2025-11-18 04:21:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 918a8a95-179c-3545-8e55-27dba029c1ff | -3.18749 | -50.65317 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 12302690-cf12-36b9-a819-cd8785519837 | -7.3621 | -46.20844 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b3e5bf3-5522-3dd4-bfdf-31c0988c34f0 | -10.74763 | -45.14846 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1581bb7-6340-3230-95f3-7da93cd57449 | -4.67368 | -45.80068 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d214890-72c8-31e1-8698-6cac1a97c882 | -9.05853 | -45.42406 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09d9c494-656d-3d2a-a420-453ec8eb11f3 | -11.26579 | -41.04027 | 2025-11-18 04:21:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 70536f22-b140-3206-8dff-d06024d11d96 | -9.0347 | -45.20609 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98f6f93b-2222-3346-9348-43ced29a2ab8 | -8.22147 | -48.30471 | 2025-11-18 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aacb2558-8a2a-32bc-b7d7-e83996409010 | -4.42906 | -45.54498 | 2025-11-18 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c0dfe0a-a824-3ffd-b16a-297af497f38b | -6.09506 | -51.26976 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 900be784-c636-391a-affe-abfe271920ea | -7.4338 | -48.93563 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b03366f-51fc-35e5-8d8d-c69b28e7515d | -4.19935 | -44.23591 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc6aee4a-3c1c-3e25-b6f9-2f969d1926a8 | -8.74209 | -39.12653 | 2025-11-18 04:21:00 | NOAA-21 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f543bf0f-39f6-3f4a-b064-74ef869f6b19 | -10.12179 | -45.54161 | 2025-11-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2392266-e444-3669-9865-4cb3df09593d | -4.53784 | -44.46624 | 2025-11-18 04:21:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef8c2203-2e14-3d71-b286-54bf00c5fd69 | -8.29394 | -49.30508 | 2025-11-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff0ba75c-63b3-3b2c-a46f-df86e3c879cd | -8.29762 | -42.25838 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1a7be2c-ae21-34b7-ae15-192fe0ff0523 | -7.9262 | -42.76991 | 2025-11-18 04:21:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1874dca-7445-3e29-97e5-a0d8e7a67454 | -7.67337 | -45.34021 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d0d366a-231c-3f23-921f-3acaa8904e38 | -6.95114 | -41.5322 | 2025-11-18 04:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 531cadb8-3b36-3e76-bcb3-0e1735238db4 | -7.21179 | -46.40258 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f49b3c09-733b-371f-bae7-02c67f2be1ce | -10.7917 | -48.61026 | 2025-11-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b349c6-7383-368e-880e-f8e28df0a2c9 | -3.75532 | -50.94844 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6800673b-3eed-39e0-b684-6990e5114c95 | -12.30296 | -40.21389 | 2025-11-18 04:21:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25099e2a-6f38-3078-909b-a2ec02e4da9f | -3.65194 | -50.22711 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61308b33-8864-3139-abb5-ab2c7cdf0aec | -6.00166 | -51.51662 | 2025-11-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ec49eb-c818-349c-bb2a-63a773387028 | -4.45403 | -44.21999 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea2ef5fe-40cb-3b3b-b3f2-aac22a8ab80f | -7.30428 | -45.75759 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d1d48e1-086c-3c32-8af9-d05efde19ef6 | -4.97697 | -41.85283 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3d432335-b7f0-3148-9b3d-bc6e6902c8fe | -6.53878 | -42.20682 | 2025-11-18 04:21:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d5cdcf6b-480d-3a89-a84a-6fd0d0e1f9f5 | -8.47294 | -47.98633 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5758b24c-bdf2-3b5a-8791-246d70a2a9fe | -7.43682 | -48.94095 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 849a5e89-c279-3539-9cbc-2cdef51ff299 | -9.87665 | -44.1851 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a139e41f-e956-3e2b-82ba-91531aa6800b | -6.72262 | -46.31773 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca857d5-e976-341c-a129-6befba7c61bf | -9.87776 | -44.17792 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e4eb358f-9146-354e-846b-3e8894c59327 | -3.06748 | -51.36575 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddb76fcc-9d6c-3d1e-a14a-b6397b834f52 | -7.43338 | -45.19849 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb0e5c3-0975-331d-850d-7f51806fa1b7 | -5.41026 | -44.06409 | 2025-11-18 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d187582-c9dc-3611-a619-741fea59985a | -4.01593 | -47.41974 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1476b209-4f6e-36c9-bc99-eca62309ddad | -6.57839 | -43.81392 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a7921509-5239-3abc-a650-2304757ef42b | -8.57258 | -46.4875 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f63122a-a4b0-38c5-87ed-00ec4c07bf99 | -4.18891 | -44.23781 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee96a92-88e6-30f3-afe8-3c5830e7fccf | -5.47299 | -41.40172 | 2025-11-18 04:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 62aeb583-48ae-347e-9a66-3fe65e8cf54f | -7.56652 | -46.29244 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c44c58da-0f9e-3123-8979-8777a8e6ea8a | -4.49843 | -46.69448 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c986b93-d80c-3dc3-80f2-e1b61f9b20d8 | -7.54895 | -47.05953 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bee3222-38ac-3945-ae61-c077b121539c | -10.09597 | -47.51438 | 2025-11-18 04:21:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6d312d2-dbb2-3f73-9b78-3b683d3bb5f8 | -8.31698 | -43.93647 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88fb66e8-f598-350c-9526-8d74ee1a1844 | -4.76789 | -44.92787 | 2025-11-18 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ddce135-fecb-33ad-b0e6-98661c56b06a | -5.3636 | -44.86188 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a0822dc-f06e-3306-9ec8-bf3b1dffa269 | -4.78342 | -45.62248 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9aa2c7e-ad15-39a4-bf93-546f90f02859 | -3.66273 | -50.21588 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 27007c81-7dcd-3eba-bb86-1a89f9c5edf3 | -3.16021 | -50.16641 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9b01068-7479-3bd2-9183-138efed752af | -4.97315 | -49.77208 | 2025-11-18 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af51c54f-cd61-3bd9-8e22-0bb453cc7c73 | -10.34576 | -48.9238 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 268b0db4-c703-3949-9345-4d6437905406 | -10.51103 | -43.96438 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66bedeac-f068-389f-8123-4903b79c3f1a | -4.34551 | -44.34738 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8f1dcb4-c8ec-3f6f-8c3e-07e860a49143 | -10.51778 | -43.96542 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d089f64e-119f-34a6-be70-e77a6464d250 | -3.76521 | -46.47072 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 835e099f-4708-3d31-8306-1a0faabe966f | -10.68314 | -44.26254 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56a96745-6d21-3ad4-aadd-9f1cfeccb898 | -10.62101 | -42.31604 | 2025-11-18 04:21:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0fa20216-fbff-30ef-8a07-eca94f736538 | -8.54451 | -46.04721 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 096ecf4c-7462-3b47-987b-449262b196f5 | -10.52227 | -43.95861 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a450308-e70a-338e-91af-a2763282fdc4 | -4.97697 | -44.68028 | 2025-11-18 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 602f8544-fd11-380a-8e85-09da2e480154 | -6.41661 | -47.44329 | 2025-11-18 04:21:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e34078-8cc7-3a16-8c2c-28528a034085 | -5.63535 | -43.92987 | 2025-11-18 04:21:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| daa29ff3-b643-39fd-b625-80faa05b39bf | -6.67685 | -43.77174 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f085632-2252-346a-bd9a-3a607fe0a8e5 | -8.98271 | -47.73078 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 249c408e-246a-35b3-914f-9f8ca8af49ac | -4.53701 | -48.4051 | 2025-11-18 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a3b1647-3a26-3a3d-a51d-93304b46f96a | -8.29261 | -43.96169 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff72fa4-d6aa-38e1-b6f0-db7538e8e8c5 | -6.61343 | -41.46444 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad9f5017-21dd-3b46-9aba-2b45104d6601 | -3.94106 | -46.20899 | 2025-11-18 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
