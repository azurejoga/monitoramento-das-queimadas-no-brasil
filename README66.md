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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a0a6f34-006f-3b40-b1df-a58287e09cf5 | -6.62378 | -43.73137 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d55139ff-93d4-338a-b7ab-d75344502378 | -5.74933 | -42.05355 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b2e8fe8-c065-304e-adae-61716d15bab6 | -5.9864 | -40.94628 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c145c23-bec9-3660-974e-21625fa5f5ab | -5.26379 | -45.41051 | 2026-10-08 04:02:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 239031a5-0720-3726-b215-0b2b1debf1fa | -8.05694 | -44.80627 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5625bb27-e0ba-39dd-aebf-a798acfc3f11 | -5.75304 | -42.05416 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e34d5a7-76f1-31c2-b077-c621405b7d4d | -10.46737 | -47.24123 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a59d9bf8-5cbb-3451-b0ec-595f72cb3ddc | -7.46374 | -42.84888 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 030ebe73-df05-3552-999d-4c9d7bb9181d | -7.47433 | -42.85544 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7e853fd0-6a05-3a3f-9304-d9b002100575 | -11.23108 | -44.87761 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 314f55d8-b182-3d94-9104-4724eab38822 | -6.88072 | -43.69465 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c519206f-f394-33b8-ba42-8a0d0ce9ab4f | -3.19284 | -50.55389 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78538cb6-3aef-39b5-a487-ca0b4e47cada | -3.25709 | -50.40196 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61c862ec-8686-3efe-ac99-3dee2d866bee | -11.22069 | -45.26945 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b38dde84-d136-38d7-bb96-637f9ea31a75 | -6.82717 | -44.86629 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4effa114-9c7b-376b-a7c2-05bd71aee39a | -3.18875 | -50.57787 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94d0a45f-65d1-343d-b216-1099e7897f17 | -7.20899 | -45.35458 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b40dbb6-ba60-379b-b666-5f44c15ef650 | -7.18351 | -52.61951 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4333343f-4974-37cb-bc96-28e97ec822aa | -5.10844 | -47.1198 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f583abc-d934-3301-b299-fec5c98623ee | -5.26583 | -45.40889 | 2026-10-08 04:02:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62e20e95-9e17-3ab9-ab0a-33fdaf337483 | -11.78205 | -43.53368 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bcec9f0-2098-355c-b2ef-2fc093886551 | -10.30788 | -46.60098 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01648cbe-221b-3d1d-a804-7bf121d28778 | -6.8254 | -39.55309 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ba1c0652-9438-3073-9379-65920067b70d | -3.17945 | -50.55148 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dee9d2ef-ec66-3b1c-9e16-948516dbe02c | -3.1908 | -50.56581 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d370ba16-1064-38fa-8057-98149b5f7c54 | -8.60316 | -45.64183 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faa8cf08-a4e2-3d7c-b3a8-9595a691da98 | -6.92754 | -43.66279 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| caf881a4-e2e5-349a-9626-5c9fd08e251c | -5.7501 | -42.07186 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7d00625e-bace-37af-bd63-8c77af79322e | -11.26723 | -45.19941 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d12d08d-31d8-3f71-a285-d07744a34e17 | -6.88414 | -43.69887 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 04f24173-b340-3d65-b72d-8312064638e9 | -5.49416 | -42.85535 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a2531046-c715-3e95-97fc-a89c05ca2392 | -3.19178 | -50.57772 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf9cd6c0-6217-367f-bf1c-885c7357ad72 | -11.71039 | -43.66127 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5126e0d3-f65d-364f-902d-8c8f8ac0c9d0 | -4.22376 | -46.93442 | 2026-10-08 04:02:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e00965e-6a0f-3bb8-b29a-eeeee76e981a | -10.2883 | -47.99866 | 2026-10-08 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 555359af-d2f5-3b5b-aa40-8b70564ba7af | -6.95468 | -45.25191 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5591965-fd56-3b9d-9f23-f722e22889e7 | -5.54098 | -43.2224 | 2026-10-08 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1510faf6-0be0-3173-a7f5-4ca6c6d88850 | -11.84884 | -43.53372 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9792cd03-2758-342a-bd91-94e0c6166288 | -5.96031 | -40.93006 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf2bd3cc-93d6-39a7-aa85-af0b390c72b9 | -6.82652 | -39.5461 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb7a39d4-04e4-3d76-a284-0935d8aa593b | -5.48555 | -42.85901 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 382f92d3-a588-3af1-b793-fa4c04bcccd5 | -5.73622 | -45.15472 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26b35b44-9e1f-3c02-b482-a966c27afb15 | -6.63534 | -43.73708 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 5d73adb8-15d7-3b6d-9bbe-291ae5261dd1 | -3.15662 | -50.44454 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 001d5e3c-ec31-3277-a7d8-59d3d6d7a9b4 | -7.20452 | -45.35374 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a893c02f-2593-3c08-a4bb-12997554a004 | -5.72792 | -45.14871 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 71d73e85-47d2-3022-950b-f0d03f09638b | -5.43551 | -44.38617 | 2026-10-08 04:02:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c186e81-8c1f-325a-a968-21c27ff852fe | -5.26199 | -45.40326 | 2026-10-08 04:02:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d9ad3b5-69f1-3ecf-b2e6-6ea1df2aabfc | -11.77386 | -43.53687 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 263c150e-0806-3bba-8fd2-d3c565914962 | -7.12289 | -43.91566 | 2026-10-08 04:02:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c294163f-1a08-3700-9bf0-bff5d02bf84f | -5.98703 | -40.94236 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c9c826f3-af26-3740-b4ed-1a28ed2d1de2 | -7.05946 | -40.94544 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49958c84-d96a-3352-83f4-c481336f5944 | -6.88818 | -43.6995 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 095edd19-5c9d-36dc-972e-af8dfdf0c948 | -8.7298 | -45.15533 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f150a37d-3be6-3093-a387-8f9f98279d5e | -7.50792 | -46.58522 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54ced34e-e5ff-353c-8343-5801666e7ab1 | -7.46674 | -42.85419 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 885d9080-34dd-3547-8aa8-3a9135ed34fe | -8.22456 | -46.34298 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bb0fb9d-aa3f-319f-86ef-9e2d516f934b | -5.71779 | -41.72388 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4721b072-c202-3ed4-9ff4-7e683584f8b6 | -8.24749 | -45.43175 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6edf2667-f156-3fa8-b227-7661ef017e85 | -5.19994 | -48.21706 | 2026-10-08 04:02:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e3c72bb-f2df-3daf-a2f2-8523ab82cef2 | -10.43644 | -47.27463 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1e01ce9-0f3e-32e6-9a81-480854ba346a | -7.8324 | -45.48311 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cba1765-2b0c-3608-8250-a85a0bf5439e | -5.7415 | -45.15103 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4abedde7-f10c-33ad-a8d8-ea3ca9395c0a | -11.23973 | -44.85268 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| becfeb92-33c1-36d6-b74e-7e50504f645c | -3.16559 | -50.59203 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f82acc0-093b-36a9-b372-a04817647aba | -6.95193 | -41.49215 | 2026-10-08 04:02:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5b21cc39-746f-3088-9f2e-ddfd74e1ee2a | -10.76993 | -46.5771 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f39e47c-0531-397e-8cba-9119ef842533 | -10.30437 | -46.62026 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e80b4edb-63da-3867-b112-fc4953960070 | -11.24018 | -46.24984 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a9d8a38-5a4d-3eeb-88bc-6f8a68dc7c06 | -6.97533 | -40.0367 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0723a1a-b3d4-3f10-b395-a2b869571b6b | -5.1388 | -44.46415 | 2026-10-08 04:02:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0de4c747-1340-3fff-a095-7b22f1e68318 | -6.84905 | -41.77026 | 2026-10-08 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f303d2fd-1115-39fd-8d1e-8cc5f31e11e6 | -10.99841 | -45.42065 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 229e5956-03a1-31ca-9594-a0b8f7a99723 | -6.64679 | -47.91333 | 2026-10-08 04:02:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b53d4f89-82a4-3867-8aa3-05136aab0c5d | -5.97458 | -40.90851 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13ace449-9978-3cd5-beb3-05ca4acf11de | -4.29053 | -49.09723 | 2026-10-08 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 857d741f-47b6-3339-8c6c-a7159cd6856b | -7.10144 | -42.5331 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecc4e389-f422-3421-b224-20fee6472c2f | -6.95081 | -45.27411 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d1dbf01-5df8-3b84-add5-2f419702dd76 | -9.59171 | -47.78167 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0269f9c7-51b9-388a-907f-166ca5e0c6ea | -6.68185 | -41.76616 | 2026-10-08 04:02:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cee51ca1-d948-3557-b080-454c2cf17061 | -11.00194 | -45.42531 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dd033a2-4010-3575-8ffe-27686e085d15 | -6.92813 | -43.6593 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 309cdf2a-18b3-37d9-8ba5-0288da7a1f88 | -8.58575 | -44.86111 | 2026-10-08 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 808bad30-2139-32a8-bf99-861cab037ad6 | -9.81505 | -44.78098 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc2f09df-34f9-3e4a-bd86-cade4f3743ae | -11.21963 | -44.87233 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ede93df-50af-329d-a828-91eb0690f702 | -7.06702 | -40.94269 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1fa15dcd-2442-383d-8045-89c8a55bc456 | -4.31467 | -50.78359 | 2026-10-08 04:02:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83fbb2b5-174f-3ea9-a11c-e2387e1c91ed | -6.1331 | -47.93754 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 320ea907-cfee-3b98-aaf6-248fe5ec5d13 | -4.35408 | -43.79464 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 62075a48-978f-3e0c-ba21-c4dd748db998 | -6.83817 | -39.55875 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9acd0281-7133-391b-b91e-707d02011cb9 | -7.31377 | -43.99631 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65648999-0fe4-305f-8b63-8c0de4abe3d1 | -9.26461 | -45.63678 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e95ef4b-4966-3a75-917a-a60671fb933d | -8.64032 | -44.895 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba9edb63-396e-30a1-aacf-1983a9724716 | -7.27851 | -46.80362 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 955f720b-25dd-3aae-8727-944e1f3bd0fa | -3.36448 | -50.47528 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d42eb98-2892-3960-b5f1-1b089097d1b8 | -5.24603 | -37.58155 | 2026-10-08 04:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6f9aeebd-326e-3924-b3ff-4f0a533debad | -5.11367 | -47.12069 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0fd35b6-7720-3827-96d5-faccd9b3a403 | -5.57331 | -41.03596 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 813e666d-6889-3c20-bdf2-b8d31441c0b2 | -11.30202 | -44.83086 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ccc0b0c-6c7a-326d-86fb-3e9077c50481 | -6.32297 | -43.35968 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README67.md)
