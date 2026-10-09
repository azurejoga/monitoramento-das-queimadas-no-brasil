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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38e488da-803f-3570-9201-bf6b9ec57df1 | -12.0127 | -43.462502 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebfd9691-1804-33ac-9773-73f91661eb5a | -16.934 | -42.1063 | 2026-10-09 00:28:00 | METOP-C | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6167013-0e2e-3586-b2c6-aa794f6833a9 | -13.2364 | -43.398998 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7610865-8dd6-309e-a23f-3b6f7aa0b8ff | -11.3995 | -46.684299 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b30dd663-78ac-36d0-9213-57e5ca4b2c26 | -6.9419 | -43.674099 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e638a986-8802-3e1f-b269-597f28c0596a | -7.5112 | -47.3297 | 2026-10-09 00:28:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 815ef948-a563-327c-91c8-981e4fca175a | -7.1489 | -55.124901 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1553ec-a902-3b7a-beb8-7658969b7593 | -9.859 | -47.481602 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8aadef-70e3-31fd-8fc1-4e5ccfaa4bcc | -11.763 | -43.543598 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80914b7c-e986-3193-a34d-9abf231f1196 | -9.2663 | -47.450699 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c0d01ce-14c4-3f9a-9aed-9b27da1c1ba8 | -4.0737 | -44.119301 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f92f0251-6064-3b59-8025-772e6f6d7a97 | -11.7842 | -46.797798 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb9ed506-9016-3617-871e-704f5c66529b | -9.2826 | -47.431099 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3487fc2d-fac2-3a8d-ae77-82a1b02556d5 | -12.0078 | -43.486099 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da5f73df-142f-30f4-b0d7-597b5e30a293 | -16.9632 | -46.362 | 2026-10-09 00:28:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d1943244-46c8-39d6-8cf6-d4e257170967 | -8.3016 | -45.722698 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2c67ce3-4d0b-32fa-9972-50b5775bf219 | -5.967 | -49.713501 | 2026-10-09 00:28:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46306967-fe48-364b-9a58-d1bd99d900a0 | -5.3863 | -44.217499 | 2026-10-09 00:28:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9edba322-42bd-331f-b702-6abbfb45bfab | -16.919901 | -40.894299 | 2026-10-09 00:28:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbb23fd6-3d48-36b3-8d09-a0e4fb694e12 | -7.4084 | -44.7505 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2eddf463-a1dd-3414-bc9e-0a27e1306562 | -4.6307 | -50.948502 | 2026-10-09 00:28:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f4c234-9889-3502-a33c-94149710955c | -10.1575 | -44.683102 | 2026-10-09 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6834842e-8d39-3588-8945-d106f42448f6 | -5.2541 | -50.154701 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d39caa13-3c94-315c-abf7-c1f8e626819a | -5.2759 | -47.917198 | 2026-10-09 00:28:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc176b07-6dff-3c3a-bbd6-c7c7dffc6bf1 | -2.8713 | -54.159599 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06230c74-ca11-3631-854a-4dd4b95ddfc2 | -11.7695 | -43.5271 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9db5b248-e7a9-3b75-ba52-7be2549a8fe7 | -15.963 | -40.829102 | 2026-10-09 00:28:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93ee3406-c2d1-338c-8957-31e311a85dc0 | -14.5479 | -50.028301 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f11070f-b45b-31c4-a465-a2baf6bc3e3b | -2.4985 | -56.1744 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bdff3e8-6164-3e6b-96e6-0313e3339221 | -9.8692 | -44.8657 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 19be6d04-1383-3997-a67f-36b737d29baf | -10.0209 | -48.032398 | 2026-10-09 00:28:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cefaad5-4aa9-3903-a604-183e54b114e1 | -3.1086 | -53.805698 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece3ebc0-3dd2-3119-9219-a7f887af4a83 | -6.1175 | -55.7019 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18bfa07b-c75b-3d24-917b-64ee4872b839 | -3.8512 | -44.138302 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f672f0f-302f-3803-8799-3b0ebbbc60a9 | -2.5146 | -45.403599 | 2026-10-09 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a11634f8-d08d-3024-9afa-10e3264a3618 | -2.8156 | -54.139198 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f19b83d3-5147-377d-b342-ec7bac045408 | -4.1207 | -46.871101 | 2026-10-09 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17f09325-7639-350d-9a14-33f6bda0fba2 | -11.4705 | -43.3941 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66be5f68-cb13-3bf3-b97c-8d703965199e | -3.4178 | -54.550201 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c17f2b40-eae0-363b-9cce-93c6d47faf4b | -10.0227 | -48.0406 | 2026-10-09 00:28:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe729199-9c41-3426-a5fe-a4fd5089e6ee | -14.9567 | -41.4268 | 2026-10-09 00:28:00 | METOP-C | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 21cb3694-bf39-393f-a697-41b7001d7aaf | -2.8267 | -51.279499 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315a9b53-89c3-3f30-9ebf-cde977e5d890 | -11.8545 | -43.582001 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb332ce-ce2d-3ea1-bd2c-abdd88a74b9a | -13.407 | -43.7384 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 790c2155-0200-364c-94ca-a5528c94b995 | -9.4452 | -45.8582 | 2026-10-09 00:28:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5b3304-c552-30f6-bb2a-56a712ace457 | -14.7825 | -42.896 | 2026-10-09 00:28:00 | METOP-C | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4bf41ac5-468a-3eb5-af35-7e6ee87bc2e3 | -8.9668 | -45.158798 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0341f0-14f4-3c9e-ab37-0b52076603bb | -3.2441 | -54.046001 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e62dc8f-113b-3e09-b0f5-ac3aa5765a00 | -8.1917 | -46.419399 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49b7a17d-eee1-38ce-b12d-ff090a333058 | -5.5044 | -43.044899 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9df7fcc2-c69c-3917-9760-1fc7e3d1ab86 | -9.7965 | -44.773201 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eaff5fa3-857d-30c6-bac1-92986702e3ee | -18.326401 | -42.372299 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18b8541d-2e9a-36d3-8dae-37014ecc834e | -13.1434 | -54.354198 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1951926a-3997-3251-8bb6-cb5b756ce986 | -9.0813 | -45.118198 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 902fb0ab-8e24-33d0-a0a8-20e2401095c6 | -8.1949 | -45.797501 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f162d9a-b00a-3017-bfb6-d6823ebb27db | -3.8002 | -49.948101 | 2026-10-09 00:28:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825b235f-8008-31e3-9104-0649c86ad182 | -1.1009 | -54.1539 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9ed43a-6494-381a-a473-18d055084041 | -7.4888 | -42.8368 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 564ef469-588d-3bcc-a981-1d8d7872e80b | -13.1866 | -54.370098 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d12aa946-8f8b-39ae-8eed-de7fdedcfde3 | -15.7877 | -50.134899 | 2026-10-09 00:28:00 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7fa53342-2b63-3f7d-899e-cf589cc09db6 | -8.8995 | -45.224899 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 746c0b38-5e22-30fb-a6cc-714ce28d5d84 | -13.8825 | -43.834202 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6af902e4-2a0a-373f-9100-39222c181228 | -7.5071 | -45.764599 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6904064e-1ef2-3d28-b08f-33bc71480b93 | -9.8688 | -47.4795 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 715416e7-ceb7-30f2-a2df-c1122da8a671 | -9.8723 | -44.879501 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 554bab12-1cbf-3b73-96cd-80dacf230c68 | -2.4845 | -56.0672 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4890660a-382f-3f59-99ca-5eaa4a3b2438 | -2.8262 | -49.508701 | 2026-10-09 00:28:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5159022d-264f-3dc7-97ac-d039fb8004a3 | -4.2747 | -49.0886 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d86ac3-a5a6-332c-b3a5-1ed7185925b0 | -5.8786 | -43.408501 | 2026-10-09 00:28:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf20c226-046b-3977-a526-c6b23ce63dcd | -3.2859 | -54.0047 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4fc4b1d-b2f7-3ecf-ad4f-93df3ebc96a5 | -8.3048 | -45.7365 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1545297-cbad-3f74-beec-84fc66885e09 | -11.7856 | -45.5956 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af15f1ad-3277-3cb7-b77b-8fdf1184978d | -6.8336 | -39.330399 | 2026-10-09 00:28:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 77da3153-6e35-3883-b623-5aa063d64b48 | -8.203 | -46.424198 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb98e768-6128-38c4-965b-ac9a48329d1f | -9.0286 | -44.393799 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be136402-dd13-3947-be63-f8495957f5d3 | -11.8316 | -43.5275 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 605beec8-0f67-363b-ac9b-34258031c09a | -3.8414 | -44.140499 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49ee8949-4ae4-32ca-b709-cecc49ec0307 | -4.9126 | -43.249199 | 2026-10-09 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2f1b490-bd0a-34f6-85ed-2988161bfba1 | -5.6885 | -53.473598 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21acd00-f4bf-35c0-a9d5-d56761c5bd6a | -4.614 | -49.224602 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d05b3f2-b4e6-33e1-8528-a73b53025ce4 | -8.9652 | -45.922401 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d09910a2-4435-3899-bf8f-d7acb4e7e295 | -13.1581 | -43.2826 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 124a3ef4-9eb2-374e-8f8d-f32039569b3b | -7.1534 | -55.146198 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3acd6e1-086b-3532-bc06-7e2e094be44d | -6.891 | -45.910801 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5b393d-193f-3e0f-9911-025f8cfcf183 | -11.4093 | -46.682098 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c29fe650-50de-36b7-a199-acfaf7c6c64f | -5.4097 | -44.629299 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a55e3d62-6bfb-3395-ad93-34eedc9662cf | -2.828 | -49.516701 | 2026-10-09 00:28:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d97a1c4-0a19-384c-804f-96ac3172d2e0 | -8.1918 | -45.783699 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06e44cf1-df55-3c91-804f-671c71737d7f | -3.2191 | -54.299599 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4830d38-aea2-3b3f-87af-4389ed0ccf33 | -13.4038 | -43.7243 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b337692-e2c4-399e-beba-cb7b674eae47 | -5.2381 | -43.979599 | 2026-10-09 00:28:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6631718-72c8-3953-9395-1fb3c5655c47 | -3.0998 | -53.949001 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608e8ee1-42f1-33bc-af5f-2a3142a7ecb2 | -3.4793 | -50.484798 | 2026-10-09 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0888c17-08c2-3c09-9031-4c0e56b1777c | -13.3771 | -43.878601 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdd3df3-01f4-3b19-a919-58c9e22f76f9 | -16.755301 | -45.236198 | 2026-10-09 00:28:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 093f152c-00d8-3784-afd4-c475270d1187 | -10.4109 | -48.884499 | 2026-10-09 00:28:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10b409d2-e96a-3395-b64d-6420514c08a3 | -4.5073 | -45.814499 | 2026-10-09 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c161d17-066c-3488-a3b1-41b931fc9983 | -6.1236 | -44.148499 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecba3537-e722-3df5-823e-6ce3c069cf8a | -3.1019 | -53.776199 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90ec5fa-166e-3056-ae7f-e4706f394299 | -11.9931 | -43.467098 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README29.md)
