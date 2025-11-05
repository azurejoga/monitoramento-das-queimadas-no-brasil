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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb82ed90-df21-3839-92cc-4f45aed0334e | -7.05589 | -45.06237 | 2025-11-05 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 119c14b3-783e-3e36-90fb-8cc47cf009de | -8.22228 | -45.72166 | 2025-11-05 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe217f97-367d-3bd3-b081-ecfe515e78e8 | -6.2735 | -42.56779 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b7f7598-3efe-3b17-89cf-e02b587bc64c | -6.07007 | -43.25356 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81c0e4c3-81d1-364e-81d9-de05e20713bb | -7.27708 | -46.06734 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58877c7f-823f-36df-b3d7-53b8787e5820 | -7.94138 | -49.73973 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66b13f19-b802-3ddd-96a6-86c0aa133fd6 | -5.23786 | -48.50672 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f94b7372-ecf2-3e98-9980-49c661762e60 | -7.83799 | -38.2429 | 2025-11-05 04:14:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00586890-289a-3693-9696-18f6b45b88a6 | -9.5453 | -42.86337 | 2025-11-05 04:14:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 40b7956c-41e2-3c6f-843b-285bf07f5066 | -5.76718 | -46.1701 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99acd8f8-5072-3c0d-ba6d-f84dffed8413 | -9.73463 | -46.36082 | 2025-11-05 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01b254fc-7b77-39dd-a359-a3c273ecf42f | -12.33105 | -41.09558 | 2025-11-05 04:14:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 182f3e50-0bf2-3c38-8aec-bcc4d1614ee1 | -9.06144 | -48.83749 | 2025-11-05 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a92356a-756e-30ab-ad6b-df9f1764f9a0 | -6.51836 | -39.68943 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e90ae2c-095b-313a-97f0-7d54aa903bb8 | -11.84123 | -43.73255 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1098057d-7825-339c-8544-81c58919586b | -7.86887 | -46.79347 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4629e47a-80b0-3063-b4f9-b753b90e6c66 | -6.63598 | -44.53833 | 2025-11-05 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17f39663-fe80-3807-a328-522adc89f554 | -7.04025 | -41.45557 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2271c0bc-0007-36e1-b706-d4b9480160cb | -10.35474 | -47.7096 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5215328f-bdef-3753-b98e-df034ad05d86 | -8.20535 | -43.59097 | 2025-11-05 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 172cef05-63aa-3eba-993c-399dc00c11b2 | -9.0494 | -47.00024 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017ba257-daa2-3c7b-906e-ee3a2d9cce1d | -10.3812 | -47.75602 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f9c2383f-845f-3020-8444-fa360f5aee65 | -6.14606 | -42.38397 | 2025-11-05 04:14:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 703e4285-190f-352c-b7cc-f30b4f87a5a2 | -5.85964 | -43.99866 | 2025-11-05 04:14:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62755585-570e-3aed-807b-b3705270f054 | -6.2067 | -43.27208 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a44be0a2-4bc8-3b0f-be01-1088928b6c64 | -5.52087 | -46.23252 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a15fc2c1-7d6d-3bd6-9157-10570c1886b4 | -10.53195 | -44.17538 | 2025-11-05 04:14:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 375f2f4c-6907-3043-84f7-00fb94cc2c54 | -12.39575 | -49.90086 | 2025-11-05 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9279c8f-34e2-3a39-8fa6-38eba8302e58 | -7.90036 | -45.5653 | 2025-11-05 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 164d4aab-fa28-37a9-816f-3441bfc613f8 | -7.27774 | -46.06332 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a74f9da9-410e-304d-8d2b-2eee2bc9c71d | -6.43379 | -45.65973 | 2025-11-05 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa138d01-a14a-3f4a-add4-f19b743339b8 | -7.24042 | -45.26676 | 2025-11-05 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b38ca9dd-20c9-3b5f-928f-d6a243fb2ee1 | -7.7264 | -46.5923 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29372117-c028-3cbe-b040-97a3ce8d7d36 | -8.21421 | -43.81297 | 2025-11-05 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50621dc0-e00c-3c01-8d1d-1721f6386d4f | -11.19189 | -47.46817 | 2025-11-05 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec1b6f3e-f9d3-3b16-ad64-9b934c7b1dfe | -9.7118 | -49.38255 | 2025-11-05 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb1e27e2-e1df-3edf-b5a0-3c1fe179de39 | -6.55212 | -44.4701 | 2025-11-05 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d953121-5bb9-3e3d-9a71-c37575de8ae1 | -9.87561 | -47.46257 | 2025-11-05 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d93bfc7-037c-3411-9675-996abbde83a2 | -7.87322 | -46.7898 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed042fd0-c675-3640-8623-2c2aa09c2e57 | -5.64433 | -46.94232 | 2025-11-05 04:14:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb5cd5bf-48a9-33a6-a86f-5109a415c373 | -11.84455 | -43.73308 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8eb2905-bc32-3b5d-bdb1-ad798a876aaa | -11.00847 | -42.73172 | 2025-11-05 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1b80a6a4-bf17-31af-b80a-1cefab458c78 | -6.53538 | -47.80756 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77c0db8-5230-3f6b-9c88-46e60101a05d | -11.84841 | -43.73008 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe16c988-2ace-3119-98c1-56d0d6aeab15 | -7.11059 | -46.52785 | 2025-11-05 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fa8fae4-e00e-35c5-bbd2-e6f6dbbca876 | -12.26264 | -43.07154 | 2025-11-05 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf11ca44-d114-32bf-8dc3-52aafd30f8de | -9.04365 | -47.01249 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99da7559-e13e-3e5a-a22d-0f43818108f9 | -13.56645 | -42.76258 | 2025-11-05 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 688150c0-a429-35c1-90a4-9239c38a262b | -10.40958 | -44.38881 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6c92b7a-8e99-36a1-9658-8c43f74d796f | -6.37362 | -42.40575 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3e47c779-18c7-3b72-aedc-0f3a1289aa18 | -8.86097 | -49.88437 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4dc2911d-140d-3fc2-9976-a84d3d6a416e | -8.08929 | -42.94639 | 2025-11-05 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 24c0b46b-32db-3790-84cb-2b2ecbf62f14 | -6.26634 | -42.57022 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aeb3082a-59f0-3766-ae50-4189623e983d | -7.03219 | -43.80864 | 2025-11-05 04:14:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c3b3d15-bdf0-33f7-bd86-d40277599931 | -10.99491 | -49.54953 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc8857ae-d877-30d1-9ccb-6ef817e8b235 | -5.65084 | -46.42516 | 2025-11-05 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4349ad5e-a00d-3271-9dc5-5701e7132b19 | -8.68967 | -40.54086 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bc355ee8-3773-35cb-8211-de5a3af67f21 | -6.09956 | -44.43893 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c3ae36d-1b98-37b0-9f20-de2f620eb16b | -12.90697 | -45.09404 | 2025-11-05 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4fa6d86d-e44b-39e6-8fab-3580a4e83acb | -11.265 | -41.08054 | 2025-11-05 04:14:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72b44d13-e1f4-36cd-a027-92c1177032bb | -7.78751 | -42.2229 | 2025-11-05 04:14:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d9e44e35-4c2d-3e59-86af-7fec218956a0 | -6.37198 | -42.41621 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e7ba6a4-cafd-38d8-8369-7df45d439c5a | -10.07354 | -42.73824 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d1b52524-d0a8-375e-9a65-c7ada88b6482 | -12.33913 | -43.65242 | 2025-11-05 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fdebaa4-88f0-348c-ae5b-95527265c761 | -11.8451 | -43.72955 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3208176c-11cf-3e4f-937c-0102fd15fe77 | -8.1953 | -44.44131 | 2025-11-05 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67aa9473-71c2-3bbd-b21f-f6518bb780b5 | -7.3338 | -46.29316 | 2025-11-05 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 222e0ff1-24da-3c83-bb40-d68d14d2c3ad | -8.21146 | -43.80896 | 2025-11-05 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bfc1547-4e1b-30f1-8ac4-5e0ee760dca2 | -8.94894 | -40.83955 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05f235f0-259c-3613-8370-399605c4ce21 | -7.72278 | -46.59168 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b810517-dbff-3fbd-8938-d761b5d5e3e3 | -8.85661 | -49.88361 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d84787c-e89c-30b8-a60b-2d2a7100401f | -7.71117 | -47.18514 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d775d1f-10bb-3c07-a9d0-2ec67c099d95 | -7.3863 | -47.13127 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40e1ed20-3681-3df5-a2fe-d9e442242e5e | -11.84786 | -43.7336 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82346fdc-e937-37f0-a9ec-76b5bad54f5a | -11.37335 | -43.13848 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a09aefd-baf2-3f26-bdb8-0d4fe2e289c3 | -11.84565 | -43.72602 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54c40df3-d29a-3c76-ad69-d27ea2aa2eca | -6.38798 | -48.05383 | 2025-11-05 04:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aba9c93-bf39-37e9-81f1-95e68dcf8775 | -9.21055 | -48.5978 | 2025-11-05 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e843db4b-20c5-323f-a883-934ac2787364 | -12.20674 | -44.34659 | 2025-11-05 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb16f21b-282f-3f64-9832-094e388c130a | -7.94125 | -49.74119 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b917b36a-215d-374e-aa98-56cbbd8e2d00 | -5.15494 | -49.8784 | 2025-11-05 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c07ed510-6883-368b-9ba6-b4ff2b8dc588 | -6.77136 | -44.84679 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27a57b05-48cf-3623-a664-a72305477779 | -5.65383 | -48.02145 | 2025-11-05 04:14:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96ea08b6-6143-3cfc-897f-3185087646a3 | -12.23794 | -50.29303 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ed7583-dace-368d-956e-aca080bdb236 | -9.0487 | -47.00451 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 862a3954-f902-3f4a-80b1-7a41ea8a08f2 | -7.28325 | -45.45586 | 2025-11-05 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9824015-830b-3729-98ff-824ef78436ab | -10.31068 | -42.41565 | 2025-11-05 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e5d5f69-7f78-315f-b20c-36d3d4e4f3f2 | -7.5458 | -45.84476 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d2c2ff-59e2-389e-88ed-8a4c8cf20b36 | -8.0926 | -42.94691 | 2025-11-05 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| ad5509e6-e66b-31c9-99ba-bf57f0e99ffc | -5.9147 | -44.01829 | 2025-11-05 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eadbcc3b-ac7b-3888-8fd1-8e80321432cf | -8.59069 | -43.75182 | 2025-11-05 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea5d8415-3c5a-3d9c-89a1-31c13b6d1de2 | -8.95534 | -42.66229 | 2025-11-05 04:14:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 56e23234-445c-378a-b30f-5a086a974760 | -7.16244 | -40.10223 | 2025-11-05 04:14:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 686caa01-a5bd-3c8d-b064-856cc360f1f8 | -7.28732 | -45.45263 | 2025-11-05 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aef182d9-a119-38bd-86b7-42fac0db6ec6 | -11.46355 | -45.15068 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a87e4549-98f2-3005-954a-6b02b3adf4ad | -8.3048 | -49.65431 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c96deb18-8136-3068-99bf-721e63bbc20a | -12.68192 | -43.16949 | 2025-11-05 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1df7dd8-d5b7-3f6f-b094-69ea362b0469 | -6.43316 | -45.66363 | 2025-11-05 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d00b1e-e00d-3ed4-a2ad-7019c8e190db | -7.03684 | -41.45507 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 57ebfced-1d4d-3f48-ada0-b8dae08e2a36 | -6.37529 | -42.41674 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
