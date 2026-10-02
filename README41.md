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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cbc54f2-afd2-3777-ab01-e35fb57dfa2e | -7.0314 | -42.84596 | 2026-10-02 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 87ccf60b-06ec-39c5-b89a-f74bc7aa591d | -7.1653 | -45.00802 | 2026-10-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf25bd60-2add-3bd6-a371-7df317efa2f0 | -4.45385 | -47.92802 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 7988cdb6-4aca-3b5f-b6e0-f9a500042bf1 | -4.26297 | -50.74975 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 209a1f27-d5e9-34fa-a9aa-419db88389de | -9.76136 | -44.81009 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f20f5f34-877e-3796-813a-e017f45f1011 | -7.57334 | -55.14109 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 934473b0-0d66-3d49-829e-5a7618696c1b | -7.82991 | -55.13754 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e70362a7-6241-34aa-a193-e65fb8104d99 | -6.24345 | -43.7759 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 906d5fce-ae43-3c39-bb18-cbda6dcde4c2 | -8.91614 | -49.25617 | 2026-10-02 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c68dc61-82db-3e0a-995b-f4181e124160 | -7.20203 | -46.55244 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe276d16-fd21-35b0-a9b9-644dc957064a | -6.44626 | -45.96555 | 2026-10-02 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4632741-7753-3fbd-a7f4-91db632ca648 | -7.75139 | -49.20421 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff8881c3-b6b3-3a95-a80f-121e67e7b2b3 | -3.12535 | -53.75182 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cc733b1-ad80-3c28-b327-cb48d2b0e8df | -7.3448 | -55.58655 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a281c3e3-5865-328b-b4f5-c4bd4eb23019 | -5.54865 | -45.26467 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6ea6856-e7eb-3a74-a4b4-eee7694f51d5 | -8.96827 | -47.4478 | 2026-10-02 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c52f3b56-b5a7-3d34-9ed2-08986b9fe6e9 | -4.2942 | -49.09361 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9caf806c-42ac-38f6-b2b9-45e1b9e8b322 | -4.2732 | -50.78837 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1eead5d-7231-31ba-ab8e-43aebd86d0a7 | -6.89763 | -43.69879 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa40822b-c811-37d1-b346-aa0b9293abe6 | -7.52019 | -47.33839 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a884fb7-11f5-3ca9-8990-af7157236bb1 | -7.41208 | -46.61934 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3f8c2c0-5577-3013-9f64-7ce53e0e5afe | -6.3325 | -43.37906 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 555e9dea-30fe-3987-aa8a-0b79007c934d | -3.13308 | -53.7471 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8873e82d-6c14-3543-9c5c-74d012b375e0 | -5.55238 | -45.26528 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 846f8381-74ba-3f12-95af-573ebafd388a | -6.18022 | -53.18576 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d4088c-95aa-3f1f-b6bd-d042b6503bbd | -3.27977 | -53.84974 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0b6e796f-b71a-3422-9ac0-69a2671b2176 | -4.44687 | -54.91256 | 2026-10-02 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d02cbaf3-71a2-37db-9a22-4f588457554f | -8.08357 | -54.89106 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0bf4eca-6fae-328d-972e-3f9a00727dde | -6.33589 | -43.37962 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75097fca-6dcc-3d2f-b7b7-171ba6c0f373 | -4.25141 | -50.75148 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ca21e4c-4f97-3275-91c5-ed8c372a5493 | -3.14545 | -53.75554 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3697bea5-31c9-3954-95ac-9e8ada3cf01c | -8.38466 | -46.29501 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce70c370-96bf-3896-a184-17dec9296d53 | -2.60184 | -48.25687 | 2026-10-02 04:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04a927e-9f43-3ace-ab2b-6700e4c7b96b | -5.86527 | -43.59668 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26713d3c-a4c0-3db3-b99b-9ab207852d1e | -5.76486 | -45.15526 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f4e8701-4add-3254-8f11-cdd2e45645ce | -4.29331 | -49.09902 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 88264f46-b35e-326b-9215-b130df7fb8ed | -2.60744 | -48.25257 | 2026-10-02 04:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2084af4-93dd-391a-8289-bfa53d4ebd78 | -4.27384 | -50.78468 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e72ead8-8687-30bf-abcb-2bfea8dad57f | -6.33112 | -43.3826 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89c26af0-9e2b-38ec-ac9d-04f93f5b76da | -5.8983 | -53.50234 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 973f6a67-f819-38a4-a8dc-c38f6f6126aa | -9.73149 | -40.36008 | 2026-10-02 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23ec4fbe-80f2-387d-85ac-a10570aa041c | -4.266 | -50.76474 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d533b237-cfe3-3ee9-b8e8-d4e90f39a95b | -4.2982 | -50.77408 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1cb1b7a-6474-37c8-9de4-d902a9473161 | -6.18472 | -44.09545 | 2026-10-02 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 721c94fc-25b6-3ba3-9fc4-43700b60da08 | -5.75596 | -45.14031 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 88c69f9e-47a5-375e-87f5-1fb96611bb77 | -3.16426 | -54.1002 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d59f539b-986a-3f40-a24d-7e254648be64 | -9.74838 | -44.82389 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c83be0a-1712-3a66-bdf6-e9469b1ef73e | -8.15963 | -54.80121 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81a1bfee-261a-3e6f-8eee-774f474568d2 | -4.29632 | -49.09619 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 091b6394-87e5-32c2-89d7-eb1c19631bec | -9.90383 | -44.93975 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5f24a33-edf3-344b-807f-37b5f2eaabaa | -7.45904 | -54.99603 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa4eb4fa-e261-36c6-8373-37bef8c1c68d | -6.74386 | -46.89914 | 2026-10-02 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 265b5f7c-e408-3ef2-b1c3-f426ed8f4025 | -6.23907 | -53.14323 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b81d22a6-7f6c-36de-92cd-3ffe66973854 | -9.77304 | -44.80415 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b830766d-8795-3506-b026-dc75e9fa5dd4 | -8.02453 | -47.47322 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f35a7cd-0ee7-385a-a06d-73376c65280c | -3.98085 | -41.52053 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13c56539-c29f-3b52-b1cd-72bfd3a97836 | -8.96157 | -46.82949 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6655fb85-6ad2-3c3b-883c-487f16242211 | -9.8414 | -44.85494 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3277be9-a558-3dca-863f-b9c70f4b5646 | -9.46216 | -45.80196 | 2026-10-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e793450-359f-309c-97fb-50c0544330d8 | -9.52243 | -45.33324 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ccf52bc-a603-34a1-8a24-083c0635acd8 | -6.21915 | -47.47613 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 279981a3-93f6-39e4-ace5-65bbaea95cd1 | -7.1981 | -46.55177 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 728bcd70-2ae3-3e95-8494-d25756e339e9 | -5.7663 | -45.14655 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27c70055-a4d4-358e-8aaf-20c559c4c65e | -7.39413 | -55.22069 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| f47934d6-a8c2-3362-9fdf-d16c4c8b1e7e | -7.38842 | -55.21337 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| cd281223-9d02-3143-8236-8204d4d03862 | -6.90344 | -43.68451 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8caea457-f39b-380d-b9b8-fdf376e06b40 | -7.50993 | -47.33332 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dce5ecd-bb1f-3b51-8fab-751d4eb59b19 | -9.07416 | -46.7142 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20ab8b05-941f-3086-ad48-f70c3b702174 | -9.84115 | -44.8349 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dd65aea-4282-351a-9355-83811de3d6e5 | -7.83499 | -47.92688 | 2026-10-02 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b3e002d-a2e7-3383-a0cc-6384916ad0a8 | -6.1811 | -52.90464 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8375235d-9bfa-3a4c-bafd-f05be6d19150 | -6.42711 | -43.72314 | 2026-10-02 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12ccd3d3-427e-3906-8665-1ffbcafcf822 | -9.5011 | -45.32951 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a40b58b-3e6d-379e-81af-e40c1b9215d4 | -7.41462 | -55.60054 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b0ec1a6-9dbd-38b4-8b0b-811882a3525b | -7.18782 | -52.61673 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2460b5f2-4f02-3138-a8f7-2500ac875a85 | -8.75415 | -44.80859 | 2026-10-02 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 422b7b23-3296-30cb-92df-e0e20f25d12f | -6.14683 | -47.26543 | 2026-10-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 965480b4-d4cd-3ac0-9a04-f5abd93778ac | -4.27448 | -50.78096 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ba6311f-08f5-370e-a6c3-573046caba12 | -3.18466 | -54.10458 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a93cecdd-b1cc-306d-aff6-1d0adea54a91 | -6.90404 | -43.6808 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4af5b0e6-ad53-3b41-950c-6ea4fb77f257 | -8.00961 | -47.43643 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e23ffba2-8e13-35c9-86fd-f14c8143d125 | -6.43961 | -55.62742 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af799d55-8168-36b0-9d34-bc9c8aabb2ec | -5.73711 | -43.28471 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fa9c8f97-020e-3423-9b7a-7cfff657bdef | -5.95435 | -38.62961 | 2026-10-02 04:14:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b8fc831-cdf3-37c7-ba88-67ba1381b578 | -7.75266 | -49.20678 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5e966a5e-e998-39af-a8ac-62dbcd88c3bf | -9.52174 | -45.33735 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a552f50b-b29c-3f14-a277-96005111c0a8 | -6.70906 | -44.8364 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1f11dfc-9f4e-385c-a6ac-915efda18b64 | -2.57187 | -49.99979 | 2026-10-02 04:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee4d94f3-261e-3779-af3d-0b09df6d1f19 | -6.14886 | -52.80618 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e43d0b9e-3340-3f94-b468-086568d51b58 | -4.0622 | -51.11983 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b0c2d61-56b1-3c87-b09d-7be4eb2fcf2e | -7.74675 | -49.20336 | 2026-10-02 04:14:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2bdad902-db43-3328-9237-377147e1d176 | -4.29638 | -50.78477 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76976443-844e-36f7-9b54-e37905c4ea4a | -7.63281 | -55.04977 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3da339f6-929c-360b-807e-09269210f79b | -3.97699 | -41.52346 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa346db3-d2cc-35a6-879c-79d5ec7a186a | -6.21983 | -47.47218 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83cf8647-d435-3b51-967d-292dae0769a2 | -7.51341 | -47.3378 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a9bc14-a022-3873-89ed-dc8a27a6b9f2 | -7.04958 | -55.64769 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 756b9318-1626-3d9b-b1ab-62c6c6963cde | -4.26836 | -50.78376 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eeee39a-7886-389e-88fe-4f0ad185f25e | -7.63167 | -55.05579 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64605fd8-5a82-3b1a-be28-635e642c2dc1 | -6.74446 | -46.89563 | 2026-10-02 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
