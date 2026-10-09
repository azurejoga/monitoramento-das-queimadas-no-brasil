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

## Dados Diários - Página 288

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56948146-66f1-3d07-8b7b-b457cc6a58c7 | -12.3384 | -47.326 | 2026-10-09 18:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 899f4ae3-00c6-38cf-8a8e-2800d65fb4eb | -11.0558 | -44.0796 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 7922989b-299f-3ca8-8526-86dcc185da0f | -14.0647 | -44.8098 | 2026-10-09 18:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| df9527b6-d8ea-3cc7-b7f6-0ec23b5241d1 | -10.4524 | -47.3024 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| b4809a0c-4c03-3583-b13c-288811e45a23 | -11.911 | -41.4058 | 2026-10-09 18:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 64fa9c8d-9b88-3dff-851a-30afb1e440b7 | -5.2683 | -47.8892 | 2026-10-09 18:10:00 | GOES-19 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 566a1506-af69-33d3-bfbd-23d4ab3fdd86 | -9.8828 | -44.794 | 2026-10-09 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bf395eb5-7560-3918-97fc-bee0053281a9 | -3.2945 | -54.0006 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 9e2c78c1-da1c-3423-9fe8-8c5709310a0c | -2.5721 | -56.1449 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1fbbe276-b1b1-384f-9558-052c9eeb6405 | -7.0892 | -52.6753 | 2026-10-09 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 241.6 |
| 25a77b92-a721-328b-b422-172cd85675b5 | -11.5874 | -45.3931 | 2026-10-09 18:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5a6d5bae-b81d-3cfb-924a-1e8da0cd6dd7 | -3.5156 | -59.2324 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a992cd73-db53-347f-9c4b-18448fcb2164 | -10.9796 | -45.2026 | 2026-10-09 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d4a1ef2f-e16d-3688-8dcb-a9d427f798eb | -2.5689 | -57.4163 | 2026-10-09 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ab3860df-3261-3e61-9c11-d165e4f02329 | -2.8247 | -57.606 | 2026-10-09 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 09b6846c-3d46-32ac-94d8-acbb1b5cc773 | -5.8166 | -42.628 | 2026-10-09 18:10:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| 62219d77-3890-31ff-9fc2-a3ca6bbddaf2 | -16.9672 | -41.154 | 2026-10-09 18:10:00 | GOES-19 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| 002e25d7-989b-305c-9657-45a2ec31c853 | -11.2068 | -45.3091 | 2026-10-09 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3774ebf7-26ab-3ef8-a6fa-bbaeb0f7c34a | -12.0646 | -43.4071 | 2026-10-09 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| bc7d4333-8763-3625-9d96-359087419755 | -2.4623 | -56.0682 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c1f4d476-cd79-3e09-b2a9-7978fcbff26c | -11.8502 | -46.7879 | 2026-10-09 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| a37d2674-8cc5-3c46-a3b4-ebaed17cc3d1 | -9.9204 | -43.5802 | 2026-10-09 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 70d9f68d-ae10-34c5-afdd-23786f1da750 | -14.4339 | -43.9396 | 2026-10-09 18:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 34933738-e9ba-313e-862c-6f012246a2b6 | -4.576 | -40.657 | 2026-10-09 18:10:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 26823fec-3e11-3ad9-a94a-8c3ffd8df864 | -15.8531 | -42.0202 | 2026-10-09 18:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 285.7 |
| c55cbab5-9d81-3a33-9d06-959a45f6afa2 | -2.4577 | -58.0194 | 2026-10-09 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 2640895a-f7a7-3e83-81e1-3e12cc7a1a81 | -11.6974 | -46.7864 | 2026-10-09 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 459f6cf4-1f8e-31a1-80b8-cf3e268c8caa | -1.5101 | -55.9244 | 2026-10-09 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 2aacc7e3-97fd-3dc3-afc2-d4efd6e67ad2 | -12.2127 | -44.7224 | 2026-10-09 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b1c05124-deae-3b21-bfd5-bee01e8efffd | -2.4806 | -56.0678 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 93cf110c-3d9e-3728-8191-88e652c0fb84 | -2.1361 | -54.4671 | 2026-10-09 18:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 12b87f58-1d79-31b5-a477-2f2e791e446e | -3.1109 | -53.945 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 12e0ca26-533e-34de-aa4f-911cc14e3e4d | -13.3865 | -43.8708 | 2026-10-09 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| f1199ca8-4364-38ec-a6ef-3eb64bc3ef1e | -10.472 | -47.2556 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 7608322a-d40d-3996-9338-f422e3a13914 | -9.2781 | -47.4333 | 2026-10-09 18:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 47f45810-e2d5-393b-9855-5bb2d805f4b5 | -10.4717 | -47.2779 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 53c38113-d30b-3a79-ab40-bd0d460bcce7 | -8.0525 | -49.3969 | 2026-10-09 18:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2bd3ee14-cf69-3bed-82bc-ee304cbf3217 | -12.1435 | -45.3576 | 2026-10-09 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7b30dde5-74e9-3e69-98bb-8baca5de3af6 | -3.6435 | -59.3064 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2bb8101e-88cb-37c0-bdd1-0523ca41779e | -1.346 | -55.4523 | 2026-10-09 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1f6bdde1-4351-3ed0-a8c5-7e930cfe51e8 | -10.1766 | -48.0412 | 2026-10-09 18:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| fc962456-6de3-3ab5-af2f-a16ce7f72320 | -12.2145 | -44.6291 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| f781e3b6-9703-3ecb-9d22-0e26f40c1eaf | -2.8899 | -54.0912 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1a6d7e4d-0093-3f30-b1c1-bbdecd34f227 | -3.5893 | -59.0773 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b54d4c4a-d592-3867-8061-5ae6c3114d0a | -18.3132 | -42.365 | 2026-10-09 18:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 288.5 |
| 639a3d53-c298-3cbe-90f7-460e798e39cb | -13.3671 | -43.8742 | 2026-10-09 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 209.1 |
| fe371781-5993-3657-bd34-f2046783015b | -13.1639 | -54.3385 | 2026-10-09 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 570ad240-53a7-32e5-ae91-897867c41aea | -2.7335 | -57.4717 | 2026-10-09 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 335945ed-2609-3c5c-9c2b-499db869d683 | -11.0374 | -44.0355 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 467.2 |
| e4eed85b-9691-3878-aa9f-981234b44a3c | -1.3277 | -55.4525 | 2026-10-09 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 2211852b-a667-3f6c-a194-a17bb049037b | -5.2682 | -47.911 | 2026-10-09 18:10:00 | GOES-19 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 94aeb125-91f2-3e36-ab3c-f1acf277591f | -13.1641 | -54.3178 | 2026-10-09 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 4b23563c-5f98-3c72-a1f6-df0ef5b329b6 | -15.0719 | -41.7733 | 2026-10-09 18:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| 00f7147e-bcc8-3eb9-8a55-99642c7e897d | -9.3162 | -47.4072 | 2026-10-09 18:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 79ba52e8-c932-3419-bce3-477eaf327520 | -14.3801 | -55.0298 | 2026-10-09 18:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| a1475553-34cd-3aa9-b557-8c6d662d043b | -8.0766 | -45.6112 | 2026-10-09 18:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cddd932c-4e44-32c1-841d-0bd1c2cfd417 | -5.6932 | -53.487 | 2026-10-09 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c90f4ce2-0618-3461-a15f-f493b40ffbee | -3.1697 | -58.6244 | 2026-10-09 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 11e5cad7-0e7e-37ee-aab6-5f805ce22f98 | -3.5709 | -59.0969 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6236d44f-189e-3c16-a937-1e624a9cb732 | -13.1636 | -54.3591 | 2026-10-09 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 287.3 |
| c35bb8a1-0334-3d83-98ae-dc51dfa58ca7 | -9.1297 | -45.8179 | 2026-10-09 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 24d101ce-7d88-3a59-a23d-3ecb24008ef0 | -3.188 | -58.6241 | 2026-10-09 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 02ba8193-3075-349c-ab64-f43ce4abe2e4 | -7.5162 | -45.3024 | 2026-10-09 18:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 162e01d7-42da-3049-86d2-388515fae9af | -6.4611 | -45.7986 | 2026-10-09 18:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 59d01efa-857e-310c-8271-897741011991 | -13.1833 | -54.3158 | 2026-10-09 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 54290490-2916-37bc-ae88-af4a25ed6e2e | -11.075 | -44.0768 | 2026-10-09 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 40d992ed-956c-3c05-8601-a8d4c50fcdff | -8.3019 | -44.1699 | 2026-10-09 18:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8f769989-b479-3fa5-9b19-0bceca8e7df2 | -2.853 | -54.1322 | 2026-10-09 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fbc4e0a3-f306-322a-aa91-13d50e2219ef | -8.2063 | -45.7791 | 2026-10-09 18:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 4f991c41-4bef-3c82-851e-c52ae27facbb | -12.1436 | -43.2992 | 2026-10-09 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 5a485ef8-3c5d-3c0b-94f1-4505ce62615a | -9.9198 | -44.8585 | 2026-10-09 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| f08bbe14-9896-30bc-a034-97dfed3d4789 | -18.3335 | -42.3598 | 2026-10-09 18:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 423.4 |
| 5ec8d6e2-1fd4-36c4-a34c-973c11fbb6d2 | -2.8997 | -56.9423 | 2026-10-09 18:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 68275890-c47b-3612-ba12-6f6664536010 | -8.9311 | -45.1355 | 2026-10-09 18:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 5240da37-012c-3e8d-b840-a73e32eeb407 | -3.4751 | -50.3406 | 2026-10-09 18:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dca2b5d6-617a-3b0a-b8a2-7956077bb5ab | -11.9677 | -43.4464 | 2026-10-09 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 9c63b272-fc3c-394f-a4c9-f572dfa111b6 | -10.4724 | -47.2333 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9b2f66dc-1887-3b1c-ac9b-0e8b52fb7525 | -3.1879 | -58.6433 | 2026-10-09 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 983a40c9-00f7-3859-8641-9996426f38bf | -12.1952 | -44.6321 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| a81f1d16-a2e7-3bfc-ade1-4567ecd65d69 | -3.2157 | -50.5586 | 2026-10-09 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ff3f0c27-768a-33fd-b124-eb54a7560638 | -12.214 | -44.6524 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 677e848b-3d17-3775-8331-b0ec8485ab5b | -15.0713 | -41.7982 | 2026-10-09 18:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 422.6 |
| 532711d9-3928-3190-b738-41ffcd8e7be6 | -10.473 | -47.1887 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 5d17d6a8-74a7-31a7-83b5-568d2803db89 | -4.5745 | -55.7174 | 2026-10-09 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 67069045-dc3e-30fe-9f02-57b4156ce3d8 | -2.5492 | -58.0373 | 2026-10-09 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 8a9f30fa-2bc6-31ac-be9a-a5519326a708 | -1.3447 | -56.3979 | 2026-10-09 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f11daac4-b330-30e0-8c36-64b425ebb6d0 | -10.8594 | -45.5622 | 2026-10-09 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 812bb7c5-5b14-3081-8717-c369274c02bb | -3.1972 | -50.5592 | 2026-10-09 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9c25734f-039d-383c-8f0e-a1c671d79827 | -10.2317 | -46.8382 | 2026-10-09 18:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 36d09ef0-f9e3-3ebe-bfcf-a8fa74240e2f | -3.571 | -59.0777 | 2026-10-09 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c5a2c83d-c098-3438-88cc-643650eb6e43 | -4.7404 | -55.6522 | 2026-10-09 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6b2fb2da-82f7-3f0f-8067-4650c23db2cb | -2.4259 | -55.9901 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 66f0d623-9994-3026-9aef-76e99f9b48e7 | -2.0403 | -56.3895 | 2026-10-09 18:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 878a2d5f-624b-31f2-82aa-fc03d8a8aa6c | -4.7219 | -55.6727 | 2026-10-09 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 763d9597-063f-3fb3-b475-986a6bfb75fd | -15.2732 | -42.3699 | 2026-10-09 18:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 145.6 |
| b0fda88a-be7a-36c8-adfb-8bcf319672a3 | -10.8313 | -47.3456 | 2026-10-09 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d25f7c13-ee88-3b76-a634-29f92acf0078 | -3.1114 | -53.7839 | 2026-10-09 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 173463af-205d-3e49-9b6b-0a5a6dc1884b | -18.6464 | -41.3443 | 2026-10-09 18:10:00 | GOES-19 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.3 |
| 12b480b4-84c2-3ff5-ba60-33c28bc95570 | -2.4623 | -56.0879 | 2026-10-09 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 7a286227-0fe5-315b-8a5d-e2a3718e0bfb | -12.2316 | -44.7427 | 2026-10-09 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |


[Clique aqui para ver as próximas entradas](README289.md)
