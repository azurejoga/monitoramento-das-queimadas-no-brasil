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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 020de0a1-8f64-3945-972b-7f351f478bb8 | -13.9862 | -54.3928 | 2026-09-01 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 261.8 |
| aaa1ad90-b3e8-3820-9446-00ec01ad5547 | -11.2577 | -50.605 | 2026-09-01 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1c410f86-5045-3b73-8f97-cb5c4ee4deab | -13.3367 | -51.7666 | 2026-09-01 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f1e0e7b3-b987-325f-8038-4e63e2ca025d | -13.4707 | -57.0574 | 2026-09-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 6bcbff2b-74cc-301f-a702-7cc0174b8e44 | -7.9611 | -44.275 | 2026-09-01 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1ce936cf-ecfb-3d3a-8cc9-488c1e973baa | -10.3394 | -49.9547 | 2026-09-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 05d2cbf0-3c53-3837-b96e-cdba01b1ab71 | -8.163 | -55.4266 | 2026-09-01 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 96a5908c-d339-3e19-b5f4-b46ff2211324 | -17.1351 | -46.8284 | 2026-09-01 15:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 990f10c5-2c4d-3198-b623-ef219d1d7713 | -10.7409 | -54.0196 | 2026-09-01 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| bd3778e4-0faa-30ca-85dc-b1826455c782 | -8.499 | -55.3051 | 2026-09-01 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cef42e5b-6ca6-31de-925c-931f64bc882f | -14.4007 | -52.5226 | 2026-09-01 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 11d36d51-1135-37ed-b6b4-a6f6d9dda4b6 | -14.6535 | -53.5642 | 2026-09-01 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| fb7739b9-fcab-3eca-a0bc-c66391126632 | -7.5526 | -60.4651 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 702c3976-4b0f-3f7c-a921-647bb9ac23ae | -13.9859 | -54.4135 | 2026-09-01 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 7cf8b2ef-3237-31f7-a7ba-3595700a703b | -14.5634 | -52.0344 | 2026-09-01 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| bc07d188-1fab-3d02-aced-fb1879df8a78 | -14.4397 | -52.4964 | 2026-09-01 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 07d2e701-93ce-3db3-a61c-e66e2b7a661f | -3.4979 | -59.0409 | 2026-09-01 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 98642227-e88a-335e-97c9-ad5e41a15e7f | -14.7302 | -53.5966 | 2026-09-01 15:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c48d00cd-95b1-3f60-8646-c8a42558013d | -7.2934 | -60.5713 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9c05dca1-1f3d-325b-826b-8d3364e2ca35 | -7.5658 | -61.3811 | 2026-09-01 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 275dfc32-5b8a-350d-8064-95af7ea05974 | -17.1146 | -46.8556 | 2026-09-01 15:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 0afc445b-497c-35fe-b53f-78ee7385ff5d | -13.0897 | -45.163 | 2026-09-01 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a3e98134-2e94-3aa1-b7d6-8889507f0d0e | -6.6037 | -58.5779 | 2026-09-01 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d00484e6-f4d2-347f-a5ad-9fe875f0bdb2 | -10.3574 | -50.0171 | 2026-09-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| f9312042-91e7-3b3b-be95-ca84f5533a80 | -6.8018 | -59.4201 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8d7e27fc-b285-34b7-8426-46f14b55e59c | -11.7216 | -47.6327 | 2026-09-01 15:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| dd40fd22-1162-3261-a96b-39d3e450f6e1 | -5.9635 | -57.6899 | 2026-09-01 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 02976af6-43a8-3dd7-9004-4115076526cd | -11.0437 | -49.6635 | 2026-09-01 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 02bb116c-b31a-3902-bce9-c4ed4458f29b | -13.4519 | -57.039 | 2026-09-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 692.1 |
| 6e5a4b45-6daa-31f5-acf7-63b79e731233 | -7.9425 | -44.2538 | 2026-09-01 15:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1d865e56-043f-361b-bef8-d4acd864d3c9 | -14.5623 | -52.0984 | 2026-09-01 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 30c0d5d0-862c-3242-8d98-d4460981891a | -3.8792 | -44.0346 | 2026-09-01 15:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9d7f7915-2c5e-3937-8043-25a1e2d9e29d | -7.3488 | -60.5691 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 455ee611-a0b7-36cd-8fd8-e12e2ead0321 | -10.1453 | -50.3592 | 2026-09-01 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 44d8eaee-c6de-32d8-a6b9-5531a9ae7382 | -5.9451 | -57.6906 | 2026-09-01 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ca575603-dd84-3f7e-9235-de1adb1a191d | -11.2693 | -54.0129 | 2026-09-01 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d9150aa0-650f-371a-b2a7-4923564d7268 | -13.3374 | -51.7241 | 2026-09-01 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 76eb773f-91c0-3bff-8cab-ebf282337552 | -14.9193 | -56.3237 | 2026-09-01 15:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1ee71c93-e369-349b-8b9f-5c9ce9c0ae15 | -5.5648 | -60.2121 | 2026-09-01 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b2074eed-e161-3cb0-aa8a-700228a638a8 | -8.5792 | -54.6758 | 2026-09-01 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f4053af9-dff3-3fcb-8c71-7ef95edca0bf | -14.4011 | -52.5014 | 2026-09-01 15:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5fc9b101-3adb-3aa4-9464-8400d255b688 | -13.3936 | -51.802 | 2026-09-01 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0b75c9b6-1e78-3375-b8cf-abd90f69c463 | -11.112 | -51.5536 | 2026-09-01 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 760402cc-c659-3f9b-bf0e-a6aa2b410dcf | -7.5289 | -61.3825 | 2026-09-01 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4705752e-5b4b-3a90-b60a-8e3399d11ca0 | -13.3946 | -51.7382 | 2026-09-01 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d535eded-8c2e-3c97-a03a-6efcd0c8ccb8 | -8.8954 | -70.8571 | 2026-09-01 15:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d138a4ec-df6c-3397-be35-551e44d0df2c | -15.4202 | -41.2232 | 2026-09-01 15:20:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 422.9 |
| cbfcea71-34a2-3192-95aa-034d52899a87 | -16.1523 | -46.6749 | 2026-09-01 15:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 93c262c1-04b1-34ac-8b19-008d4add2b37 | -10.1538 | -45.6982 | 2026-09-01 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a00e4559-8176-3b34-8a04-2b83d4d28646 | -13.9474 | -54.4179 | 2026-09-01 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a948f79b-dc53-3046-af5d-d3af5dffd660 | -3.5161 | -59.0597 | 2026-09-01 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7ab3fff5-50e0-3e28-85b0-559198c48a5d | -8.7628 | -46.4642 | 2026-09-01 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 237db4ee-af7d-397b-a77b-f224af0e98e6 | -6.9513 | -59.0859 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| aa054ff1-7311-36cf-9a2f-29366e289c18 | -13.394 | -51.7808 | 2026-09-01 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 289f3f51-9c88-3042-975b-1b939f401fce | -6.9112 | -59.6467 | 2026-09-01 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 98aad7dd-14d0-3aef-9e3c-09bf565b7191 | -11.258 | -50.5836 | 2026-09-01 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 29cf4a3d-ab20-381a-a52a-22e09a212362 | -17.1351 | -46.8284 | 2026-09-01 15:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 130.4 |
| a194d9e9-fb46-3b32-b3b5-f42354a687bb | -7.4735 | -61.3846 | 2026-09-01 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b51b03e2-de03-3c52-94b4-3eafa5fe180a | -10.3391 | -49.9762 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| fcbf9f0e-3b31-3724-a4ff-ec94cc926d3a | -14.4394 | -52.5176 | 2026-09-01 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| aa81390a-f5bd-3674-8858-7cf1bcbe3eff | -13.9474 | -54.4179 | 2026-09-01 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7b39a474-5cac-30cf-8b75-b574f89328f0 | -4.9788 | -55.8417 | 2026-09-01 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0b867c9e-5cf4-33f4-9349-209a619e1ee0 | -3.1998 | -61.161 | 2026-09-01 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 3cd70cb1-1094-31f6-94a4-3941607a95d7 | -13.4325 | -57.061 | 2026-09-01 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f6f75c29-cc87-30cf-a878-1a968d4275b4 | -7.3673 | -60.5684 | 2026-09-01 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 350d7b9c-f08e-358a-8d47-96e914f8b95e | -6.7514 | -55.6654 | 2026-09-01 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5e378e80-f226-31c6-ba68-1102bf3a4249 | -11.2879 | -54.0317 | 2026-09-01 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c55a90b4-cc53-3d81-bcbb-018e416eda19 | -11.2767 | -50.6029 | 2026-09-01 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 595f6c7c-1662-3733-9efe-8258cf0dc640 | -5.9452 | -57.6711 | 2026-09-01 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0635c64e-2c2c-36a5-bbc9-1f68e5a365c2 | -3.1266 | -61.2188 | 2026-09-01 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| daa58f11-2897-31ca-ab97-870f3ff9a383 | -13.4516 | -57.0592 | 2026-09-01 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2dada075-7209-3c3a-8488-5488dcbf109b | -8.7628 | -46.4642 | 2026-09-01 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c7530714-fb42-31e0-a791-3751a8600491 | -1.4394 | -54.2169 | 2026-09-01 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| dd818e3a-a762-3c52-9815-5f1dcaf50e63 | -6.369 | -54.7655 | 2026-09-01 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ff8d7de7-c544-3c15-aac0-8e096eb156af | -10.7593 | -54.0589 | 2026-09-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| aca650ed-c8cf-3be2-9b3c-bfadd0bef642 | -10.7407 | -54.0401 | 2026-09-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.6 |
| b3408911-6d5a-377c-a9be-cbb9510cdbf0 | -11.2577 | -50.605 | 2026-09-01 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 71465c9c-e5ed-3ee2-b58d-c39bee675c02 | -6.8757 | -59.3978 | 2026-09-01 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| e98bebdd-59f9-396b-9dbc-b4f683fe1428 | -6.8017 | -59.4394 | 2026-09-01 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c410f1d7-8e0c-39da-9fc7-0d3f72c060ab | -10.8818 | -45.3534 | 2026-09-01 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 435.3 |
| 3c153841-fa15-3814-8245-071db7876d26 | -11.2298 | -51.2456 | 2026-09-01 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0bde26bf-a244-300e-b16c-ed6ff48705a3 | -10.3577 | -49.9957 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 541.4 |
| fee737e1-66e6-3d83-a96d-a51490be7c10 | -7.18 | -73.1185 | 2026-09-01 15:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 06c28521-c1f4-3c92-aff0-ee21ae527240 | -11.6967 | -54.6081 | 2026-09-01 15:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 89002783-476a-3e2d-80ed-eb9781c61706 | -10.1352 | -45.6778 | 2026-09-01 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| cce51768-35c5-37d7-ab61-5640c7bf6e7e | -11.7216 | -47.6327 | 2026-09-01 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0dacab07-7f66-3f5d-adc6-599cad1a2bd0 | -7.9048 | -44.2577 | 2026-09-01 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 04c2684c-e68c-3989-a697-fdfa96ce4ae2 | -11.1691 | -64.831 | 2026-09-01 15:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 204c437e-281f-3894-9d8f-527272b901aa | -10.3574 | -50.0171 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 278.1 |
| 44da4bc1-9307-3998-a778-7636c8b5c022 | -7.566 | -61.343 | 2026-09-01 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 1c61cda9-d2db-3805-a932-4273711d89bc | -7.8716 | -47.0838 | 2026-09-01 15:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 02b61755-8c3f-37ec-8acd-9739f6e35147 | -8.7817 | -46.4623 | 2026-09-01 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 7fb4a9e6-7ef9-38cd-a6fd-b19041b0055a | -10.7409 | -54.0196 | 2026-09-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 342e1af4-d811-3b9c-a571-7213434ed8b0 | -13.4707 | -57.0574 | 2026-09-01 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 19117aca-8c06-3aef-bf96-09e8f046a3e5 | -3.1267 | -61.1811 | 2026-09-01 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4439b529-f145-37f4-ae59-b7c74e21a88b | -14.4007 | -52.5226 | 2026-09-01 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| e9cc3d87-0be1-3150-812f-298f0dfa2665 | -9.9741 | -46.308 | 2026-09-01 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 1e6982ea-f01c-3112-82c1-403b6f1ee210 | -10.8206 | -50.7159 | 2026-09-01 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 84e1577f-afc1-3b31-99fe-362ef9b59640 | -14.6535 | -53.5642 | 2026-09-01 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 0cd52e5f-6b80-37c5-ac5f-9bcbf041a2c5 | -7.1123 | -42.7727 | 2026-09-01 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |


[Clique aqui para ver as próximas entradas](README108.md)
