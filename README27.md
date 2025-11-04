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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eb75863-833f-399d-b41b-88279870b54a | -2.84403 | -49.82801 | 2025-11-04 05:22:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 105a8ec5-b72c-3b8d-a2db-fa589bc0a431 | -3.44775 | -50.21924 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de977358-926b-3d82-8c13-3226f5f4b81d | -3.57585 | -50.64326 | 2025-11-04 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906471bc-c3b0-3c0c-8878-34dc5d25a2d6 | -20.64129 | -52.8737 | 2025-11-04 05:25:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3ef9d39-53d6-30b2-b4cb-4f2205b27573 | -20.64089 | -52.87806 | 2025-11-04 05:25:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd24d903-048a-3a82-a282-796b639b2f1e | -15.69326 | -59.00957 | 2025-11-04 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0c4ced9-9882-342b-af34-90e79fc71c05 | -19.97298 | -57.23323 | 2025-11-04 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d5b8a5a-b229-30e6-a0b9-5b4b131479e2 | -3.9139 | -47.697 | 2025-11-04 05:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 66037beb-7773-3e3f-a786-04edf452bfc7 | -3.9324 | -47.6962 | 2025-11-04 05:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 8645cb0f-2278-35d0-a033-59e2a74909ef | -3.4386 | -50.2368 | 2025-11-04 05:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b179508b-eb09-3f99-9a64-a322411a198e | -3.9139 | -47.697 | 2025-11-04 05:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fef68f28-300b-3197-8c3c-6068d23a3ae9 | -5.03054 | -43.6184 | 2025-11-04 05:48:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c4c96ee3-04db-3f0b-99f7-e0b83498ce09 | -5.05744 | -45.90886 | 2025-11-04 05:48:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9fc3049e-7283-3a09-b359-e8fd664deec0 | -3.40915 | -44.43066 | 2025-11-04 05:48:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1bb1306a-3c38-33e1-a398-fa17a7473164 | -4.59181 | -45.58252 | 2025-11-04 05:48:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aae0d093-93a7-3df5-a9ad-87f4d5df8d16 | -5.03187 | -43.60964 | 2025-11-04 05:48:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb9696a8-5b3a-39dd-82dd-8dc741b1bce1 | -4.02723 | -45.46099 | 2025-11-04 05:48:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 81d6cbef-fb79-38fa-9a4f-adeb4fa23497 | -4.4705 | -43.22375 | 2025-11-04 05:48:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9253afcd-1147-3415-b80b-1e8b1c719960 | -5.35971 | -44.73592 | 2025-11-04 05:48:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 695daf54-1ad5-301d-9cc5-810f6974f73b | -2.31636 | -48.588 | 2025-11-04 05:48:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 84ecfe50-0912-36fc-92b6-2d676d35c814 | -3.43153 | -50.23839 | 2025-11-04 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| cd557350-069f-3c00-a5cf-9747fc7b1870 | -3.42804 | -42.54008 | 2025-11-04 05:48:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cab64ad7-eabc-3e00-b2fb-2701865775d0 | -3.90889 | -47.69232 | 2025-11-04 05:48:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| de6d097f-d9bd-3fb6-9a0f-c31a692e44e4 | -3.41697 | -44.43845 | 2025-11-04 05:48:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bba4e495-cd35-31fb-a62a-6abdb89ddaef | -3.40776 | -44.43985 | 2025-11-04 05:48:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 05ab5e8f-1778-3ebd-ab1f-8b32ee3cda51 | -2.37274 | -47.71504 | 2025-11-04 05:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5cf5e281-5ac2-3d1d-aa59-a80b6f96dc7b | -4.46918 | -43.23249 | 2025-11-04 05:48:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ca4ac113-0206-3562-a041-d39c0aea32f4 | -3.41838 | -44.42925 | 2025-11-04 05:48:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81f31991-2d8f-3265-b3df-c7636d9ebdb8 | -3.91984 | -47.69404 | 2025-11-04 05:48:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5015f3ad-981b-3281-8c34-4a0f65b50428 | -2.87195 | -45.28926 | 2025-11-04 05:48:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5512966f-6168-3c71-88a7-919ce4e0fac3 | -5.74831 | -43.39131 | 2025-11-04 05:48:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8baa090d-c91b-37ed-810c-33c4c0e03062 | -3.4386 | -50.2368 | 2025-11-04 05:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a753adad-d690-3b04-92ae-ce0df08f1e80 | 0.83613 | -59.32681 | 2025-11-04 05:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c38862cc-46f5-30a1-90a3-96ad2149a5e0 | 0.9723 | -51.21267 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 62e14a4b-d7ee-3366-9eb8-a0bc173e9d68 | -7.77941 | -42.21741 | 2025-11-04 05:50:00 | AQUA_M-M | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4ad4ca64-5d8e-3af4-b128-795ecd2b222e | -6.46781 | -43.2232 | 2025-11-04 05:50:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e858a44-3f31-30d2-bbd1-3ac05c688c46 | 0.84044 | -59.32613 | 2025-11-04 05:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d938afe-c703-39a3-86b1-2c5ff8d1915d | 2.60233 | -60.12918 | 2025-11-04 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2297b736-ec72-3905-b05e-b5bc0272fd4c | 0.84604 | -59.33365 | 2025-11-04 05:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef0768f-d59b-3c89-a103-6ecb7df8c108 | 0.96504 | -51.21393 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4af24441-6b39-33d7-9015-fc401ac66ae9 | -6.83669 | -46.2944 | 2025-11-04 05:50:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ac5f4184-da11-3293-9df6-bcbc9bce893e | -5.61269 | -45.96773 | 2025-11-04 05:50:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 57102878-6202-3dc6-9db7-e47c0f6f17f5 | 0.9802 | -51.21333 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42316710-5156-307d-a142-3e45aab22673 | -1.76796 | -53.55228 | 2025-11-04 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 593ec01a-3738-383b-8383-982ea04305ff | 0.97346 | -51.21994 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e95d59e6-0d70-3951-a99f-c3abcbebeb37 | -6.41646 | -43.065 | 2025-11-04 05:50:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0e71d30b-8d0b-3dab-80bb-50c84fd55fd3 | -2.641 | -54.58052 | 2025-11-04 05:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02ab2d48-f7c2-375a-a237-ef6717cdfaf3 | -2.6417 | -54.57571 | 2025-11-04 05:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f4f9b754-2e0b-3471-8782-348978d5a61f | 0.9657 | -51.21585 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7cc76a8f-39fa-38ce-9dcf-bbb7bc0357aa | 0.97295 | -51.2146 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c7dc9df-3186-3f0d-99ef-bc49ecaeef09 | 0.97173 | -51.20726 | 2025-11-04 05:50:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dcac407a-21be-3c11-8f97-545c054ad1e6 | -6.60814 | -43.75957 | 2025-11-04 05:50:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e8fc409-06b6-3975-a3c1-b1f107edc547 | 1.08481 | -60.32163 | 2025-11-04 05:50:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2f1d1f5-517d-338c-afca-9eecca45536f | 0.83549 | -59.32275 | 2025-11-04 05:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa71212b-ec6e-30b6-aece-71eab50d9d1d | -6.84619 | -46.2957 | 2025-11-04 05:50:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 53b63ba6-52c4-3aef-982b-8a8773906f15 | -2.63728 | -54.57865 | 2025-11-04 05:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aeb84a04-7d40-3587-bce3-138d133c883b | -2.63801 | -54.57388 | 2025-11-04 05:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c4ca15b1-cf51-3eb2-b4bf-2b926c84144a | -6.41514 | -43.07388 | 2025-11-04 05:50:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f1663e6b-fa42-32b7-ac13-4b3cd36eb2d1 | 2.47738 | -60.20333 | 2025-11-04 05:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 820006b9-7661-33d0-9d84-3837bae9071f | 2.9507 | -60.8443 | 2025-11-04 05:50:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47de6889-828d-3113-89fc-49b508394eee | -1.76136 | -53.55132 | 2025-11-04 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b86df40b-21f0-3265-bb5f-1308fd557e04 | -2.63544 | -54.57478 | 2025-11-04 05:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d257be9e-2c8f-3763-898c-3b1244306a59 | -6.40764 | -43.06371 | 2025-11-04 05:50:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0a3f5341-4872-34f5-bef0-ba45c5c15ea1 | -5.6111 | -45.97796 | 2025-11-04 05:50:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| abee8684-1fcc-3812-acc6-ee10a1773f4f | -7.61594 | -46.47588 | 2025-11-04 05:50:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e131093c-b1e3-3863-a00a-1dd59c95da65 | -7.06725 | -47.36374 | 2025-11-04 05:50:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bff2681b-55a6-3817-acdd-6dca4b2bc9ef | -7.61754 | -46.46553 | 2025-11-04 05:50:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d4cc730d-d4e6-3204-9fc6-2adab3b8920b | 3.35762 | -61.11147 | 2025-11-04 05:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbf5ede5-269f-3a8f-a247-6d7fcfecc4b5 | 4.38539 | -60.46506 | 2025-11-04 05:50:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e5461cd-a3c2-3b01-a990-5863ef0f3880 | -11.8409 | -43.72735 | 2025-11-04 05:52:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d62f783f-3833-3c1b-9963-7acc22b2cb27 | -10.94179 | -44.19667 | 2025-11-04 05:52:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cadbbab7-0040-30ec-9f9a-d9435c1d0fac | -10.93106 | -44.18928 | 2025-11-04 05:52:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 24eb56d3-c053-3389-a60e-2a55216f2886 | -12.01658 | -43.85087 | 2025-11-04 05:52:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 950989e8-5faf-3719-93b2-275cd73c66d7 | -17.0173 | -41.2865 | 2025-11-04 05:52:00 | AQUA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| d37abc11-c36d-384d-98a7-231dd15c6529 | -11.84347 | -65.02194 | 2025-11-04 05:54:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7e5b66e-a485-300b-b5ea-68c073d68bc3 | -9.84445 | -67.7794 | 2025-11-04 05:54:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0d109b-c18e-3430-b0de-4da2f7f0a3db | -11.95995 | -64.8904 | 2025-11-04 05:54:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8197bcfa-0273-348d-9ece-6e8056ad8d3d | -3.4386 | -50.2368 | 2025-11-04 06:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9520f3d4-82ec-34fa-96f1-ae57d8091dcc | 0.84034 | -59.32801 | 2025-11-04 06:09:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f384e8bc-cc70-3847-886e-9a1e28a52996 | 0.84075 | -59.3306 | 2025-11-04 06:09:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cf9e2da-fe51-3749-a112-d684b19f52f7 | 0.83988 | -59.32512 | 2025-11-04 06:09:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd45cc13-d7db-38f1-9dfe-19a03c93dcea | -3.4386 | -50.2368 | 2025-11-04 06:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 80a4f5bc-bfa3-34b2-8c44-0d2249aee878 | -3.4386 | -50.2368 | 2025-11-04 06:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 20b155bd-93f7-3f95-9707-7ea7bdf10283 | -6.60285 | -37.5052 | 2025-11-04 11:19:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 70a0f72f-ce24-35f1-9b4c-40dc3a43a8f4 | -7.76032 | -37.41273 | 2025-11-04 11:19:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5f614d88-e7b0-3bbf-8938-1e9d62736ce3 | -6.59396 | -37.50999 | 2025-11-04 11:19:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 5341dc8c-a00d-37e2-ab26-7adb2c3397a2 | -9.24822 | -36.9376 | 2025-11-04 11:19:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e57663ca-5b59-341d-aa51-8d56c5a52e7c | -5.81424 | -35.5696 | 2025-11-04 11:19:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 66959b4a-ef54-3037-bf4a-afb09e814379 | -7.59393 | -37.29449 | 2025-11-04 11:19:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| fbdf7f18-b694-3d1a-b7e3-869066aa2365 | -7.63691 | -37.36784 | 2025-11-04 11:19:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 23e4d3cc-5164-36fd-afc7-6a08759b7193 | -6.7765 | -37.88797 | 2025-11-04 11:19:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 390a9b16-e551-30c6-a394-9c51fc4cc365 | -7.64324 | -37.36216 | 2025-11-04 11:19:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 61.6 |
| e24411c3-59e8-3625-90af-1214210eb277 | -14.56873 | -41.89531 | 2025-11-04 11:21:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 33.2 |
| a6e35e76-2fcf-310c-9dfe-b57c6474d519 | -14.564 | -41.90067 | 2025-11-04 11:21:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 92e08d4c-2cc8-307b-b5b1-4cd3624421a3 | -13.53472 | -43.18028 | 2025-11-04 11:21:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 3457010f-a7a8-3513-800e-e267c4b88d82 | -13.75207 | -42.73028 | 2025-11-04 11:21:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 087590bf-de35-38a1-a48a-0de2f49bc994 | -3.411 | -44.4459 | 2025-11-04 12:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 6fbf51c8-8ba3-380f-89c1-2f3859ac0c7d | -3.411 | -44.4459 | 2025-11-04 12:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 3d8b2352-ea5a-3c40-a31f-e95346812612 | -3.411 | -44.4459 | 2025-11-04 12:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 0beece4c-0992-3e74-a71e-b1fc08754bdb | -3.4111 | -44.4231 | 2025-11-04 12:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |


[Clique aqui para ver as próximas entradas](README28.md)
