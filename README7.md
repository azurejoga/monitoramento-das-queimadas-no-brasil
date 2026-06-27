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
| 0db48bbf-fef9-3c94-93f3-314610f018c3 | -12.6046 | -57.8942 | 2026-06-27 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 49a7d694-b940-3e0c-9f29-2ff770b290a2 | -14.8694 | -54.5388 | 2026-06-27 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e209a910-d538-3c96-bfc3-e3a5ebe7032b | -12.4651 | -58.5009 | 2026-06-27 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8c03eaf5-9650-378b-a061-19fefbb8bd33 | -12.6236 | -57.8926 | 2026-06-27 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a5ee9188-1dcc-3483-a23e-3e5affadab3a | -5.7758 | -45.0599 | 2026-06-27 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3465adb1-866f-3687-b399-1c3fa8ab3702 | -12.4654 | -58.481 | 2026-06-27 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| efd57427-0ad6-3634-8f94-16fe2032ae89 | -12.8359 | -44.3422 | 2026-06-27 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 78c847a0-ee56-3559-83c4-e1cd0ba70084 | -12.6048 | -57.8743 | 2026-06-27 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8de67ee5-c065-300a-8d5e-ff9944a0a7b1 | -12.6046 | -57.8942 | 2026-06-27 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 89ae06c8-f222-3b87-bb9b-29b434b6b340 | -7.7361 | -44.1823 | 2026-06-27 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 451ffa6e-1777-3fe4-83fd-5c33b5ddb92e | -12.6238 | -57.8727 | 2026-06-27 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 9b6e550a-092b-30d4-8f83-f61670ae7a1c | -7.7361 | -44.1823 | 2026-06-27 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fdee14e2-7603-391f-9e34-ef77f4205532 | -12.4651 | -58.5009 | 2026-06-27 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ad410405-676d-3e90-8d24-6e91b29b1cb1 | -12.8354 | -44.3657 | 2026-06-27 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| c59a2971-219e-3ff3-97da-b316718a3ade | -12.4654 | -58.481 | 2026-06-27 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ea07650b-6323-309d-9eb2-5b45d05b2e86 | -12.8165 | -44.3454 | 2026-06-27 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d04942f4-48bf-30ba-8896-8f7cfa9b96b2 | -14.8694 | -54.5388 | 2026-06-27 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c19d621b-123d-3af9-b5f5-f1fc52cf5112 | -12.6236 | -57.8926 | 2026-06-27 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bd93cd83-0383-3abf-9422-950c1eb64a53 | -12.6238 | -57.8727 | 2026-06-27 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 0539f4f7-4e61-3f89-919a-e281032ec1d7 | -12.8359 | -44.3422 | 2026-06-27 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 41fd52e8-a342-3b62-bfb3-f5158047d10e | -12.6046 | -57.8942 | 2026-06-27 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e73bf03c-5532-3add-8cda-6a009b056493 | -5.7758 | -45.0599 | 2026-06-27 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4eccf2a2-fce9-3e12-a4a7-9af113ba53d0 | -12.4651 | -58.5009 | 2026-06-27 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e749dcaf-9f48-368b-b21b-7ffa26e11b6c | -5.7758 | -45.0599 | 2026-06-27 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d5e187f0-b0cf-3899-8087-2ce3b7cc9a5f | -12.6236 | -57.8926 | 2026-06-27 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1ac543b5-5b61-3744-b7dd-ba260353a4c5 | -12.4654 | -58.481 | 2026-06-27 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 22e33122-2b16-3a61-ad08-3cbb3acabcd7 | -10.474 | -47.1218 | 2026-06-27 03:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 311580a7-258c-38c5-a25d-991499ef3215 | -7.7361 | -44.1823 | 2026-06-27 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f023f14c-6ed9-389f-bba9-c1669094a2ff | -12.6046 | -57.8942 | 2026-06-27 03:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7e2e8d14-39c6-393f-b4cb-b2616a35a152 | -5.7758 | -45.0599 | 2026-06-27 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c07be5d3-3230-3a87-b8ff-4fa45d696dd0 | -10.6195 | -50.2038 | 2026-06-27 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7a308f75-bbe4-3908-99e1-176d5a988e60 | -10.6192 | -50.2252 | 2026-06-27 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fd0c578b-bbbf-3e9c-b700-816dbd84c92f | -12.6046 | -57.8942 | 2026-06-27 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0ce6d11d-2ea0-3502-8971-8f120f12b03f | -12.4651 | -58.5009 | 2026-06-27 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ccf3c9fb-2ccb-376a-bb73-c885a359c770 | -12.4654 | -58.481 | 2026-06-27 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 61f66755-8bd8-363b-ba34-8c96b8507cd6 | -10.6382 | -50.2232 | 2026-06-27 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 391d8fa8-e63d-3214-8a31-dbfbd755a57c | -12.6236 | -57.8926 | 2026-06-27 03:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 971fe5d3-29a3-3ba8-a7e6-c6a5ee20aa0c | -10.6385 | -50.2018 | 2026-06-27 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b4c12624-2f07-3040-b0d5-121dd3a2bccf | -7.7361 | -44.1823 | 2026-06-27 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bbe61491-ab08-3de6-bf2d-2db1a88af18e | -12.6046 | -57.8942 | 2026-06-27 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 93ee7b89-7bc0-358d-ac11-53c67a50d938 | -12.6236 | -57.8926 | 2026-06-27 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d79391b0-8a6e-3668-9393-611b4da49cd8 | -12.4654 | -58.481 | 2026-06-27 03:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9232d110-db43-335b-a31e-03d5cfad12da | -12.4651 | -58.5009 | 2026-06-27 03:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| bad76b52-e348-3734-986b-b2df4549c184 | -5.7758 | -45.0599 | 2026-06-27 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 231d545c-6b73-3f2e-8149-faf2fd0b8534 | -12.8359 | -44.3422 | 2026-06-27 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 06bc2a3c-25ca-3fdf-aeef-47d8335dabd1 | -12.6238 | -57.8727 | 2026-06-27 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| f4c3fc6f-9e06-3176-9e07-3756964d5a43 | -12.6046 | -57.8942 | 2026-06-27 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 64b36122-e230-3352-9aef-cf8f35355496 | -5.7758 | -45.0599 | 2026-06-27 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8c54993a-2ebf-3f59-a371-1f99a5f304ad | -12.4654 | -58.481 | 2026-06-27 03:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 16262209-3d55-3367-b90b-e8a4a1809ea0 | -12.4651 | -58.5009 | 2026-06-27 03:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 95c3f7e3-bdb5-36e7-8949-af604ae25746 | -12.8359 | -44.3422 | 2026-06-27 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 68dba1de-75c2-313f-8bd3-5cf286da6083 | -14.8694 | -54.5388 | 2026-06-27 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 92e94a1f-e6cd-3029-8a45-7f2db37b48bb | -12.6236 | -57.8926 | 2026-06-27 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6bc1e2c5-f506-3c06-844f-e9d6c69519eb | -6.97148 | -42.8972 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b803e8a9-90ec-39f0-8b00-a53d109079e6 | -7.73674 | -44.18559 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31971a14-1e49-384d-afab-bb86c6318baf | -7.73885 | -44.18036 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c3607532-bd2a-3ea5-be96-9536620a6e63 | -4.98338 | -37.22913 | 2026-06-27 03:36:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54151492-f0b8-3a74-87de-b19594679c01 | -4.14659 | -43.65438 | 2026-06-27 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7137b9cd-54c2-33ec-a988-2584f82e4808 | -3.87004 | -42.96991 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80d68811-a125-3acd-8d32-3953a0e2133a | -5.7887 | -45.06474 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56994c78-8109-3bce-8e92-da2e8c1bf683 | -3.8707 | -42.96606 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ce848797-05b5-39d9-bb71-e277d0356380 | -7.74319 | -44.18267 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 72834225-db26-3144-924f-f1af1a580ba6 | -7.74796 | -44.6203 | 2026-06-27 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eaf65452-598c-3402-9582-d8640c2825e2 | -6.97625 | -42.90144 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| faf5efa9-7010-3f77-a49e-6c7265cb5d90 | -5.7786 | -45.06365 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 465cbe43-7211-3947-a435-424da826e178 | -5.13404 | -42.88041 | 2026-06-27 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93447766-fa96-38fa-bd95-5ec0096d05e1 | -3.31171 | -42.49025 | 2026-06-27 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6bd32fe-79c6-3772-94e2-c02055298f80 | -7.74382 | -44.18551 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4c90013b-9288-34d3-aa2f-37432843ff2d | -6.97685 | -42.89804 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ac282ef0-e7d3-3652-811b-ae03c5ba1175 | -7.7439 | -44.17874 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| aba1e883-9a93-35a4-b7d0-e7a865d7df38 | -5.7896 | -45.05981 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58c62d69-325d-32af-b112-b3087f62e236 | -6.98279 | -42.89562 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b227dd7f-3332-3092-8579-797811ea0577 | -3.86765 | -42.96646 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 20094e2f-e146-36de-9238-5180d97c684c | -3.87331 | -42.96738 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1653388-7994-36d4-844d-14ff8780a38a | -6.99921 | -42.77047 | 2026-06-27 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11305ab5-5b0a-3962-8cfb-325d8701e809 | -7.00274 | -42.78152 | 2026-06-27 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2966bfda-54fd-37ca-a08c-d470ff4c8775 | -5.12855 | -42.87938 | 2026-06-27 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8959f21-455c-3c34-9be0-3a7585a4dc26 | -5.7714 | -45.06789 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 637ddca2-a8d7-392f-99ee-12a9a4cfe2bd | -7.73747 | -44.18153 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ba8a1163-2a66-3889-b72c-3c83c3704fc7 | -7.74873 | -44.61609 | 2026-06-27 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea79757b-7b73-35a4-a1e0-bea32033d6a7 | -4.1407 | -43.65342 | 2026-06-27 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3248aad9-32a1-3bfe-887d-59aacd78fa27 | -5.77771 | -45.06875 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 66ee844c-1587-35d1-b867-8e7e0f0d6a93 | -5.77948 | -45.05858 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7f491813-1c97-325f-bc33-fbe082a8bb88 | -7.75389 | -44.62128 | 2026-06-27 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9569ed7a-a2bc-3747-b6b4-702f10a7de77 | -3.3114 | -42.49418 | 2026-06-27 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c79de89f-3b89-355d-b935-dd45d23d9cf9 | -7.74956 | -44.18022 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6c11899e-e96e-3fe1-8909-50a747e459da | -8.4907 | -44.74083 | 2026-06-27 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75cd0e66-8406-3b67-a91c-ad79d6fdb0d5 | -3.86701 | -42.97031 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fae69404-abae-39fe-bbbc-470cdaa406f5 | -7.00333 | -42.77816 | 2026-06-27 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2aab02b3-97b9-3dac-a20a-0b02e01277ee | -5.78779 | -45.06979 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8a92c146-eec7-32ae-bdb8-2d2ca1e9355b | -5.77517 | -45.06805 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 41b81d18-2dde-3ada-812f-7a6807b34457 | -3.31199 | -42.49055 | 2026-06-27 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f9aec1c-e968-3176-861c-aead1bd17f35 | -9.4007 | -41.02543 | 2026-06-27 03:36:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f1ddd33-cdfe-3ef6-8e71-bef9ac47a4c3 | -3.86437 | -42.969 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7b530ab0-215b-3690-87cd-29c5dab8dd08 | -6.97744 | -42.89466 | 2026-06-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b6224de2-ce55-356b-bcc8-1085df6b1f5f | -5.78331 | -45.05881 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1678fd2d-5d85-36a9-9a30-2c9247cb05b8 | -7.73958 | -44.17645 | 2026-06-27 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cb15b1cb-bbda-3cc1-a483-cdc4ad98dae6 | -5.77609 | -45.06296 | 2026-06-27 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0e4d0953-5e6b-3f56-8307-059352fc4b1a | -3.87268 | -42.97124 | 2026-06-27 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0f27d78-aff4-3fc8-a92e-16b0e097facd | -3.31109 | -42.49387 | 2026-06-27 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
