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

## Dados Diários - Página 342

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2ccca2f-fce7-317d-b367-d69f41f2a431 | -9.88556 | -44.85688 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 917d98fc-63d5-35df-bb6e-71ebe4d7b1f3 | -7.56951 | -40.38356 | 2026-10-08 16:37:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| f783a9ec-af58-368e-a0c4-0b0228fe7390 | -11.76506 | -37.60162 | 2026-10-08 16:37:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 36e9734a-2d90-39f3-a733-5f510ad8d6fe | -5.5038 | -40.53485 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a6d609eb-ca29-31e4-b4e6-586a4555a8f0 | -7.47285 | -42.8615 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| a271e572-ea27-3bda-8cd5-fa6c0fad91c7 | -9.13453 | -45.82863 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 9f32adac-e726-3886-84bd-4915404be155 | -7.7914 | -44.57354 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2c158f2-99dc-3a19-b677-45310a34da8e | -8.95331 | -45.17228 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e0453e6d-1c16-3bb5-bd13-9050131a5a43 | -7.87706 | -54.96373 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9802a946-e96f-3dfc-9593-6b9ff33885b1 | -12.30913 | -47.06976 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a8a764aa-5eac-3583-a2c4-c9994342f065 | -6.31535 | -35.1382 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 78c89d5c-8aff-3dcc-96dc-e5a5f53ee606 | -7.19365 | -44.33601 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15b79fa6-5d3d-358f-b993-a20eb93616db | -19.67169 | -43.6553 | 2026-10-08 16:37:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8d2b2a6-f73a-32bb-9343-1ec242db448a | -10.3508 | -47.75737 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 84716603-3520-3889-afd2-154bf62248dc | -10.4717 | -47.24239 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 0f717353-33c3-3e4e-bfd9-ce5edfef8b10 | -11.30677 | -44.83057 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 85429ec0-3b5e-3a84-a77f-b290bde549bc | -5.98935 | -42.71216 | 2026-10-08 16:37:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| e6b78eb8-97b1-3068-b52e-d70e1592ad53 | -5.75663 | -41.62642 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4a825852-21b8-3beb-a40b-0049ccf9c6b9 | -6.31753 | -35.13126 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 32987358-c4c1-3eb0-9717-796cfedcca06 | -7.19085 | -44.34018 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 88ab2ac1-7c31-38d8-b549-d68698cf9011 | -11.83829 | -48.09041 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c625f17a-550e-35f7-ac6a-b023b0d7f517 | -11.90728 | -46.56227 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3a438b17-c5a8-3d58-9ef0-28fe8175f990 | -11.39101 | -47.56343 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ac37a510-f405-3882-b71c-c3b01e127749 | -6.88789 | -43.68897 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 19eae8f2-2bda-38e2-b1cc-f06752a56911 | -11.77192 | -43.53889 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c1b4f085-9a79-36d4-9ea6-79b4ba5b740d | -8.92872 | -45.1907 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 353.4 |
| 2cfe80d6-ba1d-3f8f-af05-67bb41110863 | -7.702 | -45.44432 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 761ea207-a124-3374-9ba6-84e4d2e2885c | -8.94217 | -45.14589 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9f24e20c-2daa-345d-b111-d4a55fa0fc47 | -6.17292 | -44.85877 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aeff2e80-9556-3405-87a3-79e148a918ef | -11.39696 | -47.55449 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aae3ac21-0fc8-3f8e-bd02-283b344e1382 | -6.95537 | -43.73644 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5900daf-5b90-35ad-832f-d15ac19dcb2c | -13.34249 | -43.96583 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6971c9a1-de9e-3bd8-9dcf-938bf46318ba | -11.86812 | -47.39326 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 667e9806-4e66-3197-99eb-0aafd32ab3f6 | -6.67309 | -45.37511 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 46a50d6f-8407-32dd-acfd-f6a5cb7a6650 | -10.42639 | -47.26161 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 379b96fe-ed74-3a00-b65d-bdcc34a8fafd | -8.79671 | -47.045 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7acc2158-dee5-349d-b713-911cd60fa2b4 | -7.75208 | -54.94928 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d146b95a-0971-3a6f-9469-55dce9ef6fd0 | -7.6971 | -45.43443 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7ab108af-6c6d-325a-86f1-8e6b1826ed68 | -6.70038 | -45.28827 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8082a93-97ef-3379-8b65-cae30d543133 | -6.89969 | -38.52701 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6b3df648-40e0-3c8e-b17f-277d31212ecf | -9.88001 | -44.86489 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 861b679e-bcfc-346b-b949-4872c3c891ea | -6.97087 | -43.90273 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09f706dc-7284-377f-9bb7-6aaf199ed2a8 | -8.1945 | -45.78125 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ccf9736-3b44-3f3a-8900-90af476542a8 | -11.26459 | -45.17844 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d82aa424-356b-363c-b132-9df9e59d1c4b | -11.23569 | -44.01637 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa4f236d-5442-39f7-a115-3ffebec9e327 | -6.21976 | -44.83649 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a9b1d578-7e03-357c-8b24-068fdf456642 | -6.22071 | -35.32349 | 2026-10-08 16:37:00 | NOAA-20 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2a4f4e3d-273d-3da1-a3da-34e59a5a0bd6 | -11.08416 | -44.02623 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 06d7e375-bfc6-32cf-9e29-836555816050 | -9.82735 | -45.768 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 39dc8e60-187c-327e-876b-45bd8d6eff5c | -7.8834 | -55.01228 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c84822a-dcde-32ae-abf9-c4860259266d | -10.51468 | -47.31894 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b149f7a0-abbd-3857-8738-87b016f2d306 | -8.84732 | -45.45666 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0c9f3d21-9c33-35ed-bd02-1f0cca12c0b7 | -9.13175 | -45.83264 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 8f67eea4-d406-3f06-88f8-f31a94447c2c | -6.38471 | -45.04515 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fca20564-5bf1-37cc-b65d-43962c2d88db | -8.24823 | -54.72579 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c8e6a289-1220-3fce-8045-27540d7629df | -8.29235 | -45.73358 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 267.1 |
| c90b73b3-87d1-378f-a101-4b83d1b13e50 | -11.20334 | -45.22154 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e1f1f0db-e346-3b04-9aa8-4702200aa45a | -9.78279 | -44.78415 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ff3bdd64-c63c-3b51-b3f8-979529e3d576 | -11.30122 | -44.83862 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 571c2334-a7dc-371a-ad10-c4f3e2b8fa4f | -13.37684 | -43.88039 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 1bf6e2e4-55db-3e0f-8a08-0839e8dbeaf6 | -12.3668 | -38.88241 | 2026-10-08 16:37:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 86fccd10-9759-3243-8253-afdbd6597588 | -8.891 | -45.61008 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4190de8d-b542-332c-bb2f-c229a610023f | -6.83909 | -39.56337 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d1d2278f-ae56-3c47-bc93-221243683932 | -8.74152 | -37.34071 | 2026-10-08 16:37:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ca78e84f-a349-3870-8f30-89897db32b82 | -11.24627 | -46.25432 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3b279697-86fa-3a8c-a55f-22b2acff7c15 | -9.69284 | -58.10239 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9f887bf4-5ec9-3c5d-978e-6e140ff0fc12 | -6.93781 | -43.66946 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d322fbee-f91d-3716-ad92-b95d380f0679 | -7.47513 | -42.85287 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| f12c0783-133f-3419-b9d8-20a395ad88b8 | -8.93491 | -45.16482 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6e2294ce-77eb-3b41-9851-b56f3ced20ed | -12.61703 | -44.54553 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c6a2c337-8ec2-3461-83b0-62c09d365a35 | -11.63267 | -43.59896 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 15aa4b04-42e5-3091-bdd8-d074306f26bc | -6.83228 | -43.64342 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0194b6a1-4a41-39a8-a663-6552cfefd57f | -8.96622 | -45.12395 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47981068-c87d-31e4-9f98-10d41f5630a4 | -11.86459 | -47.39378 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 699d030c-ab93-32bb-b0a8-d5a2f9104153 | -13.59032 | -48.59133 | 2026-10-08 16:37:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| caa56b6d-5640-3802-ac41-6896ab3a2d37 | -11.3476 | -46.72724 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 016bb0e3-6154-33fe-9e1b-2caa115fd9ac | -7.75565 | -54.9537 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 41de0f7d-59f0-376c-b18d-57557b91e997 | -5.09463 | -37.50412 | 2026-10-08 16:37:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4218d3bc-e069-3a96-9dc7-dd8313a7fed8 | -13.61389 | -48.19483 | 2026-10-08 16:37:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a03e714d-f609-37af-9d4c-72928e51ff59 | -10.89755 | -45.53297 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b5954fa7-453a-372a-a62d-dd6cdfedb282 | -11.78005 | -46.76697 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0aeefed4-2a87-3688-895a-04c1dd5c1c2b | -8.97096 | -47.56202 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81d7f412-02c8-3717-b4dc-e88ac34b4b3f | -6.07361 | -43.87981 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 00e73a41-6235-3e98-9b8e-8c2817a99f38 | -11.21089 | -41.57294 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f61b23b8-d193-33b7-a3f9-01d9d91e96a4 | -5.70873 | -41.72332 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0eec4696-2dff-350b-82a4-de9c05b470d2 | -13.34635 | -43.96885 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| fb43e098-ffb0-31ef-895c-e52142495cc6 | -11.77135 | -43.53529 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ba844e67-2f37-30f1-9ee5-a99cd4ead45d | -6.89314 | -43.69978 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8281b50f-e59d-3d1c-8d6c-05bb30338471 | -6.55939 | -44.13919 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c721972-0597-340f-94cb-66a3b44d8c98 | -12.21775 | -44.81987 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 15adc914-1e73-328a-8931-f16c0ee8f80e | -11.21608 | -44.85944 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7631a59b-8ea3-3b7a-87f9-3741132069aa | -19.70112 | -42.00858 | 2026-10-08 16:37:00 | NOAA-20 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24011aa4-01d2-37b2-8e11-7022b2e8632d | -19.4227 | -48.62436 | 2026-10-08 16:37:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 887fcd14-43fd-3b97-bfdb-cfa7cf4fda76 | -9.93607 | -43.56873 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 496e11c6-ee33-38b3-bb93-6c0c37433f7d | -11.0691 | -45.77065 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ff6963ba-4e04-3aff-b6c7-01238a95c7e2 | -10.58211 | -47.30551 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f37073e4-6511-35ba-83a7-e122522fa99a | -7.48066 | -42.81871 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 26e51796-bd15-3e9a-8838-b8c36ad2f17f | -9.19079 | -46.70545 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 86c3a725-b3aa-3bd5-87ff-31573c3beb30 | -7.88024 | -44.97052 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 65cf316c-217b-3e0d-8c2b-f07a5e6d611f | -13.98995 | -46.36633 | 2026-10-08 16:37:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README343.md)
