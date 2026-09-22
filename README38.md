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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 896a9374-a67f-3da5-8033-51bd5b37e181 | -11.67387 | -43.46046 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d687788c-0059-3922-ae67-c03a25763960 | -7.50224 | -45.44614 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 00f8e59a-5f9c-3bd9-a6a6-83a56fa67bbb | -6.66722 | -47.37844 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6307d7a8-2317-3254-bd49-f256805b27f3 | -6.74111 | -45.46104 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 983099cf-fc94-3f24-80bb-c1c1bce2bd06 | -9.05228 | -48.77745 | 2026-09-22 04:02:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14510f7-a015-3fc3-baef-518c1df9e9d6 | -11.41106 | -46.80062 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0590fb1-f045-3e84-babc-c8d26fb4ca31 | -8.78492 | -44.30186 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4464e333-e4bb-3da7-aae4-e3507325a37b | -8.43114 | -47.48249 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51392c81-4efa-3587-bdad-d02a6a05544a | -7.91153 | -36.49482 | 2026-09-22 04:02:00 | NOAA-20 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 22ad3695-c524-3370-8be8-aa79669043f2 | -6.97411 | -47.49903 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24c4aedf-3d19-35bf-b8ac-6978d131a51d | -7.90324 | -49.01433 | 2026-09-22 04:02:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71d4d9a-af68-3642-9225-b91a7ef32fb2 | -11.15219 | -51.11551 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca00b4f6-689b-3e80-8be7-ed1cd7ea7527 | -6.97531 | -47.49638 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b6404e5-0db5-3ee9-8887-48a99605857d | -5.7841 | -43.77666 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f9eae7c-cf27-3494-a582-e7626050a775 | -11.41899 | -47.35345 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd0e2876-7939-3416-91cb-7d187ff650a0 | -9.89002 | -48.45928 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31c466e3-6a06-31f0-81f3-9880d1733b79 | -6.18565 | -45.32522 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250a86ee-184d-3a87-b648-966990e2ea58 | -7.42995 | -42.11581 | 2026-09-22 04:02:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07657b86-4ba5-378b-9de7-77ab73ac2e8d | -8.78528 | -44.27547 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 986a4b9d-d727-3a7b-b90a-9bef3dc27b62 | -8.43168 | -47.47948 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c9052b1-3ceb-3f23-ab24-c82cf9ab5fd7 | -8.33416 | -47.53627 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2992ff1-8309-33ff-b492-b3fc1ee941fb | -9.90364 | -48.44455 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd78363c-e94f-37fc-94f2-4815e8824b67 | -8.43565 | -47.48644 | 2026-09-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae8cf612-6fcb-3dba-87cf-0b0bd3f41e56 | -6.00818 | -47.90449 | 2026-09-22 04:02:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 078fb654-d946-3fd7-81cd-781340b0dd31 | -6.00573 | -45.24768 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d49728f-00b1-39bd-9bb9-8b2c8300b5a3 | -6.9757 | -42.58816 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d58c4f28-86f1-3a92-a23b-955f6bc3eb2b | -7.59081 | -43.42347 | 2026-09-22 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43b01a8d-4c43-3104-91c3-07cb0fa29634 | -4.64063 | -50.99587 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a915c15-6169-3fde-a3e1-7f81b4f38329 | -5.78472 | -43.77301 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57ef0dc9-4fb0-3dff-9ed3-4c09a8bc5449 | -9.27241 | -46.18275 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ed98baa-164a-38ac-abe3-fbfc541a1c5e | -5.98257 | -44.72279 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d63911c-319b-30f0-90ce-99047105b69c | -8.7581 | -44.26361 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67a2100b-e3ca-3a97-a7f8-fdbc832cf20f | -4.64729 | -50.99746 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8baea8ed-77e0-36b0-9a5c-f3c1d45367e6 | -6.6002 | -45.87449 | 2026-09-22 04:02:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f853af56-be0f-3ac0-8324-cb2f7814f489 | -5.78124 | -43.76864 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cd78794-6389-37c1-b69c-4bb61a517422 | -8.10402 | -44.44828 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69913002-7d0b-38b9-b5c9-b8b7fa2c9580 | -11.0278 | -48.33063 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 658ede23-d042-3954-82e3-5f1755643473 | -13.07646 | -42.60509 | 2026-09-22 04:02:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ce35086-0b82-3a64-bde5-ad6c71804a3a | -9.02707 | -44.91065 | 2026-09-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ccc3a39-9773-3bcf-b9e3-a7b71d930369 | -6.93238 | -42.89138 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21f7379a-758f-3884-a9a3-bd1a819e3218 | -5.69771 | -50.01179 | 2026-09-22 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b81f533-5e07-31f9-badf-7eea79f16ef4 | -11.42383 | -47.3539 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c9a9ba9-16ed-3e8a-9e26-ab6f790abb57 | -6.99633 | -42.17813 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8c052ba-aa52-3f07-8f6b-8f5079059232 | -6.16189 | -44.18058 | 2026-09-22 04:02:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98ffe856-a319-34ff-a5f2-3e6f8134db41 | -7.3534 | -45.34553 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4f6d11e-37c7-38c0-916c-94cd9d12d4af | -11.68203 | -43.4573 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e285f589-a51d-38b5-93ba-47e8e6c4e222 | -11.14857 | -42.84447 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4301fc1-8b8f-3cde-9830-b45908f2cf44 | -11.09417 | -48.32872 | 2026-09-22 04:02:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f86d36a-cb0f-30df-8052-9742b6d385f5 | -7.3511 | -45.34761 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4a1b853-12e5-3ebe-83d8-ffcbd15b0f59 | -5.79428 | -43.86652 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97492b86-0ac1-3806-8851-c38514e5e3bd | -7.50595 | -45.45133 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 420cb9d7-230b-3c54-beb5-8ceff95f2e89 | -12.56236 | -45.97233 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a0883875-fec6-3dfe-8ab8-e8549aad2f0c | -11.326 | -51.35868 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bc431c32-53c6-385d-a7fc-af701b90ac1e | -6.00121 | -45.24685 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b1937f6-fbc1-3b82-8af6-36502f8aec97 | -9.71985 | -47.76417 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f327e202-886b-3a3d-92f9-21133d9b0649 | -6.97494 | -42.5927 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef8d02d5-c0b7-31a2-a28b-2e50362f873e | -11.44147 | -47.34029 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| be25136f-f32a-3f67-81bd-b74df6041daa | -11.10666 | -48.31855 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c499410-60d8-39e2-8be1-83b1f009cc4f | -6.59695 | -39.1404 | 2026-09-22 04:02:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 3f86c4a6-f3cb-3833-854f-834573bc12e8 | -10.20205 | -44.1571 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c5a73a80-c3cd-3bd8-bb84-e4a36514f19f | -8.34383 | -50.74696 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a649938c-5084-3eb5-886b-f5611a0b4a06 | -6.00879 | -47.90097 | 2026-09-22 04:02:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a90a7f-2714-3ad1-b7c4-64d47a6f832a | -7.13777 | -48.44265 | 2026-09-22 04:02:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f245ed5-5b89-3962-b7dc-3b3e9824ae3e | -10.2494 | -45.4987 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bacd6518-e34f-33d8-a97d-db1bad1b08b0 | -12.60129 | -45.09147 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a6d4101-1270-3b67-8764-cefbb1a786ef | -7.51198 | -45.44313 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd602b83-14d2-3f02-907d-e86260f0382c | -5.9811 | -44.73142 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58161c07-5ea7-3281-a626-3fb9e475b13a | -6.57854 | -44.14922 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5061f170-54e9-383a-84b7-c1ba99095144 | -10.02091 | -45.21289 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3f8615b-f727-3844-b8b5-8b6c3ab76bb9 | -8.78022 | -44.30486 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf957d79-6ae4-361c-96c7-0111ee211c4d | -11.44054 | -47.34517 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 692dac96-1a1e-3e86-a956-2d3d80b32ca3 | -7.9427 | -45.64688 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60778584-72b0-3370-bfee-6d32e6628eb6 | -7.50301 | -45.44168 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf187cdd-934e-3051-b293-a68c288c62a7 | -10.48268 | -36.89698 | 2026-09-22 04:02:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc6cd82d-8ed7-36b0-a685-a5ff9b08db9d | -5.6266 | -43.37143 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35c29d99-861a-3823-81d9-86895c562075 | -10.25193 | -45.49843 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb77304d-bb96-3427-b4c7-002ee40558ba | -5.98694 | -44.72356 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abfe985d-6550-3fe1-ac52-6f2f383895d0 | -5.75045 | -45.08395 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 492c0099-4c7a-3596-9dbf-b84216ef19e4 | -10.38719 | -48.90015 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08acee81-0729-3c9d-b1c9-b50c5610fb45 | -8.92595 | -50.90393 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8399a73b-625a-389b-8fec-3ac620513252 | -6.44535 | -48.44611 | 2026-09-22 04:02:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54342705-2edd-3002-852f-926ef589f491 | -5.74644 | -43.73219 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f90a8c2-8bd6-3622-932b-7f8693084300 | -7.08855 | -42.07215 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ebea3c0-a998-343f-a99f-b374fc0af8db | -6.1126 | -44.31886 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4020e9c5-bb11-3804-9261-be77db3dd262 | -6.78256 | -48.67667 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe80826f-d0f7-3630-a2ba-e104e43e00d1 | -10.3838 | -48.90096 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3b05d6-de77-373e-91eb-e296682086c0 | -6.4433 | -48.45764 | 2026-09-22 04:02:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a202dc2c-af95-3952-a717-3c134548ac88 | -9.71878 | -47.7701 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 054b39a3-fb60-333a-92c6-78dad5912414 | -8.10467 | -44.44445 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bdd3131-fde8-3de4-bbbb-e496c09c9e30 | -9.27257 | -46.18107 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcc47c8b-63ce-314c-b7ed-48f37c1ff999 | -9.88474 | -48.45839 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a33b679-5b23-3f19-b125-36de37a8aadd | -11.94965 | -46.51627 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d0779b9-0107-36f6-89e1-c904af17b56e | -10.20777 | -44.1475 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35f3b47c-a2d0-3f68-8b85-ab0d88d48568 | -6.90705 | -41.69897 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3602a609-322c-3eaf-b056-82ab53a30e64 | -11.32429 | -51.36166 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fef4be84-9fae-3faf-a338-52221b6dca1c | -10.38048 | -48.91812 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1809f1e1-ecc1-30aa-b2f5-24ed2cc816d9 | -6.93684 | -42.91166 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b222cdd2-e837-3b07-a166-73a701128806 | -6.97356 | -47.50599 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a508f29f-8993-342a-8bed-a7ce723daddf | -6.90976 | -42.89544 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f981707c-7ed6-3a3f-aa4a-d1d4e2ff1a07 | -11.662 | -43.46296 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README39.md)
