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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f853717a-28a2-3896-b589-6872e8aeaf87 | -11.7409 | -45.371 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 21e5fd23-1ca3-3d42-a16e-51bf85eb0b41 | -9.7463 | -47.7144 | 2025-10-07 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5832b90f-73ca-3ad1-8d75-569b1a283de5 | -11.7837 | -45.1115 | 2025-10-07 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d62fab64-4c23-3109-b61e-220f2da0efef | -15.1553 | -45.7067 | 2025-10-07 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b8d1c44f-f304-32d1-8ccb-f2d3fe86cecf | -11.0265 | -50.8854 | 2025-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| e260f83e-45f9-3906-8654-6cc1458c958a | -8.2346 | -49.8734 | 2025-10-07 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 94040630-6b01-377a-a4ef-00eb11cd7d65 | -19.5789 | -44.6198 | 2025-10-07 14:00:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f5449282-85f7-32be-a42b-2ff7f36c72ed | -9.6804 | -45.6645 | 2025-10-07 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| c13fe69f-047c-3083-bfe9-6994c4af0736 | -13.0026 | -51.1052 | 2025-10-07 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 55f84b06-154a-32aa-8e4b-aed8f842b801 | -8.4824 | -46.2912 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5776e282-8224-3e11-9ec5-b19640b816ec | -8.6519 | -46.2964 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b3bed5df-9feb-30b5-8b19-22c7a615d81e | -10.4245 | -45.3907 | 2025-10-07 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 329.3 |
| c468e1ca-1228-3f4d-aa9b-7e1131cd8b0c | -8.5207 | -46.2425 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a47f0c5f-2710-331d-9f79-7d2461f907c5 | -9.1975 | -47.8381 | 2025-10-07 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2dee4521-e391-38b8-91fe-8bd30d01c864 | -8.5941 | -44.9209 | 2025-10-07 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f0e777ab-2b50-321b-8a2f-b5c595816713 | -16.0016 | -50.9456 | 2025-10-07 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d3e6d78b-1b2d-381f-9f5c-041c7ec6b702 | -8.0866 | -44.791 | 2025-10-07 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c8fae192-7210-3e61-acf0-e75cb9c551ae | -13.7923 | -45.7859 | 2025-10-07 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3967c9f9-4e0e-3c4f-91f6-5c7b1159c2c1 | -13.0747 | -48.002 | 2025-10-07 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8df148ad-86ce-3629-a9a0-8eab3f03fcd8 | -8.6521 | -46.274 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 74342561-e32d-36ea-a478-32338a994379 | -11.8447 | -44.9176 | 2025-10-07 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 711fd615-692c-378a-899f-aa0dcceb97e5 | -7.6932 | -46.2548 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f5511f1a-ecee-3b34-97d6-4eb4c7d4e3f6 | -12.3351 | -45.3746 | 2025-10-07 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 4db0b354-5f1b-3f97-af7d-69df80f4c847 | -12.7637 | -50.4921 | 2025-10-07 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| b3a5828b-1836-3675-8cc9-0fe48597c629 | -15.6202 | -52.5501 | 2025-10-07 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 64067bff-c95f-3922-b530-f7374e717efc | -15.1548 | -45.73 | 2025-10-07 14:00:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3908f078-d362-363c-b581-807d73393035 | -14.8641 | -51.4373 | 2025-10-07 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 514ea4be-2b3d-396a-85b0-adb46e9285ff | -9.2979 | -45.9574 | 2025-10-07 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| b6bcbc54-1050-3f4d-8f7b-75f31115e117 | -8.8794 | -47.6722 | 2025-10-07 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| daabeb7e-58c2-3663-8920-56f12e8a5900 | -9.1978 | -47.8161 | 2025-10-07 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 7277804e-8525-3078-9f4f-2057f5c547b0 | -8.5395 | -46.2406 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 3b14cb01-085f-37b4-a5a8-f59d6be8fa11 | -9.7463 | -47.7144 | 2025-10-07 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 97fe8fca-213f-3063-87e1-edbfe692fdf4 | -11.2436 | -50.2645 | 2025-10-07 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 76cf5d9b-3a4e-3507-a69d-3c74dd303c91 | -9.2976 | -45.98 | 2025-10-07 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4a16a9be-6163-3f1f-b0c9-013fcedb7041 | -11.8029 | -45.1087 | 2025-10-07 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 46e0fa37-3095-3a6a-83cd-46ad20d02590 | -18.9846 | -47.8282 | 2025-10-07 14:00:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 112.8 |
| fbab8151-9cfe-3e4b-a17c-a54395de4644 | -10.0868 | -50.5141 | 2025-10-07 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 579bad38-ac8c-3e12-b360-76dbdc8017a1 | -9.9018 | -50.2341 | 2025-10-07 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 38b7d489-7ff0-32db-8cbd-946429361d45 | -11.8635 | -44.938 | 2025-10-07 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 1fdccf74-1aa7-3322-ad94-e51b4cda1fb2 | -13.0939 | -47.9992 | 2025-10-07 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| a0bdc196-e937-3e40-9512-a0e89e76f4ac | -11.0451 | -50.9047 | 2025-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| db9ab91a-7cbf-377a-99dd-5a979e8a138a | -9.2973 | -46.0026 | 2025-10-07 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 424d6a8d-1057-3ac2-af16-fb063077f0f1 | -8.8903 | -46.8081 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 95657039-1612-398e-b614-307a65986e35 | -8.1879 | -44.2283 | 2025-10-07 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 9b8305c3-35c1-3ea5-a328-2d722fd73014 | -7.8119 | -44.1516 | 2025-10-07 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 467702bf-86f8-3985-ae23-0111418855e6 | -15.6097 | -47.2555 | 2025-10-07 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8d732272-d865-3305-b4f3-2dcb16d988f8 | -8.5584 | -46.2387 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 2ad8837e-c21f-3ba7-89d1-07e94d55cbbf | -11.6855 | -46.3593 | 2025-10-07 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 376dfef4-cac3-399b-9708-3b2690d0e792 | -14.8645 | -51.4158 | 2025-10-07 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9c80f217-661e-38c1-aa8c-03757ec16f13 | -10.3665 | -47.9978 | 2025-10-07 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ab454b40-3cdd-320b-a67e-d84859bd890c | -8.1882 | -44.2052 | 2025-10-07 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 5e771f5b-79cb-387f-83b4-b7a75ad31238 | -18.2856 | -45.4587 | 2025-10-07 14:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a9ea6e01-4b28-37b2-9cfe-f5e1b0ab5c9d | -12.9106 | -54.7147 | 2025-10-07 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a215048c-8569-396c-a1be-cdb2b5ea2b64 | -13.0009 | -46.7795 | 2025-10-07 14:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a0b251c9-32a4-3d79-9709-f60a182f476f | -8.8618 | -46.0949 | 2025-10-07 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3242be2e-1344-3be0-af17-9142aedb371d | -11.1644 | -54.8804 | 2025-10-07 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 258.3 |
| 7bac77b8-7a41-3e86-8920-ca36342f21b3 | -8.4821 | -46.3136 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 4a8a17a0-7b74-3173-9a67-a2610cd39d0f | -7.793 | -44.1535 | 2025-10-07 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9cb76a0f-f1fb-3f82-b62b-14daf004b2ee | -8.1615 | -43.3465 | 2025-10-07 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 5c25b45b-ecf2-36a1-8ddb-9b387fb85a84 | -9.9398 | -50.2091 | 2025-10-07 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d02c0f10-9278-3bed-b067-f338a7bd1b9a | -15.6003 | -52.5742 | 2025-10-07 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| de432537-d678-37fb-a369-683112f82456 | -12.4916 | -54.7364 | 2025-10-07 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| dad32920-6691-3f4b-9d4b-2db43ab933f2 | -11.2433 | -50.2859 | 2025-10-07 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 11db73ee-4b4c-375e-9c77-6389542de468 | -15.3737 | -47.3201 | 2025-10-07 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8c302528-9323-32bf-bfd4-c5c6474a2d58 | -11.0262 | -50.9067 | 2025-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 866f554d-a98b-3551-8497-cdbbfe1c487d | -8.6397 | -47.2769 | 2025-10-07 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b9717651-e985-3ed9-bc16-96c64c2b64cf | -12.9101 | -54.7558 | 2025-10-07 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 43c4b9b6-7e85-32e3-a453-0aabec3ce46e | -7.4666 | -43.0909 | 2025-10-07 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 30ff27bb-506c-30b7-bdb7-d4104eb771b1 | -8.5007 | -46.3342 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c7936c07-11b3-38c4-b48a-dec56b4047bb | -6.9704 | -42.0023 | 2025-10-07 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 1bb59b30-1fe8-3e31-8cfc-4f3cad6731c5 | -12.6159 | -44.7519 | 2025-10-07 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 312.5 |
| 8545c492-5721-38c4-b155-88808a70b6ee | -19.0295 | -44.7327 | 2025-10-07 14:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 166.5 |
| dd7fa2d4-e775-32e7-a115-e03fd92bcd2b | -11.0448 | -50.926 | 2025-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 149a3da8-9bdd-301e-b2e9-a407c9e2cbfd | -11.2623 | -50.2838 | 2025-10-07 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c8e77dc8-e622-3b81-9b94-be3f1a2c127f | -7.4672 | -43.0438 | 2025-10-07 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 2f8bef66-6a1c-3725-bf5b-99c40e6a6d53 | -10.4054 | -45.3931 | 2025-10-07 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 311a7c68-c4d1-3168-8cb6-1e21f2ce9aa6 | -14.3144 | -45.8579 | 2025-10-07 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d09334d9-af1a-3d8b-a375-7645680012ca | -9.9207 | -50.2323 | 2025-10-07 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9fbe65ee-76d0-3191-bb79-5df418ed4886 | -11.6859 | -46.3366 | 2025-10-07 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c8b710b9-ab5f-3cd8-9eb1-9d2ecf9e6231 | -12.9837 | -51.0862 | 2025-10-07 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d91025cd-1fba-3f1b-b5ff-a2d6fb597cd7 | -15.8091 | -43.7597 | 2025-10-07 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 8424ce9a-7ccb-3236-b592-ae5cc4f0157e | -8.8717 | -46.7878 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 860dc599-d3ac-35fe-bf04-a4fcf87c063e | -9.9204 | -50.2536 | 2025-10-07 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 22ad2e5a-53fc-394e-8b60-be2aaf5bbf97 | -14.7088 | -48.399 | 2025-10-07 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a1370e1f-1b0e-397b-98b3-619e93ebadaf | -8.5393 | -46.2631 | 2025-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ee20f1b5-b4ea-35e9-ab4d-f16e3c490b9d | -8.9759 | -47.4864 | 2025-10-07 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 089a9732-f196-3c93-ae9e-56cfec6f149c | -10.1573 | -45.4701 | 2025-10-07 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 686a0239-6767-3621-8a8d-cad4af1e303c | -7.4669 | -43.0674 | 2025-10-07 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 367f2b4c-639c-39ce-b868-620637cb6f50 | -7.6648 | -45.4471 | 2025-10-07 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f21dce2f-800b-3412-80fb-71461f7e163d | -8.1618 | -43.323 | 2025-10-07 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| dd36dbf9-558c-3370-93ba-0a665dd6eda1 | -10.3854 | -47.9956 | 2025-10-07 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a86b24fe-a779-3f77-903e-6c07e312e649 | -11.4678 | -43.5011 | 2025-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 75e124b8-2d86-310f-b04f-248ff9e0320d | -11.2228 | -47.8516 | 2025-10-07 14:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| d305ce43-4966-3df1-a919-e430307db104 | -8.921 | -47.3595 | 2025-10-07 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 5c62f767-02cd-3180-b8c2-dd303091e6f0 | -12.9816 | -46.7824 | 2025-10-07 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 50948c9e-bd37-38c4-ac9c-79425073069d | -8.1894 | -44.1125 | 2025-10-07 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6727fd09-5001-36d5-a7c4-daf34df914b5 | -10.7468 | -46.6634 | 2025-10-07 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 259.1 |
| dddde622-9efd-3559-9767-443442b93d32 | -11.0454 | -50.8834 | 2025-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 73908b21-7087-3ac3-b336-a9034ab2ddf0 | -13.2232 | -51.6744 | 2025-10-07 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5a3898a5-6fb5-36db-b8c2-8238ba3c953d | -10.7278 | -46.6658 | 2025-10-07 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |


[Clique aqui para ver as próximas entradas](README126.md)
