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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f983d22-4ddb-368b-ba70-6f553ac49868 | -4.4521 | -55.071499 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44ebd1c9-1f5e-3f50-96a8-54b0ea4ebe92 | -3.822 | -58.881699 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24b48821-b569-3b9c-8301-e702731e2365 | -1.2164 | -54.543499 | 2026-09-23 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905ecdff-879e-3ecf-b2fa-cb1e564742a2 | -5.6161 | -45.2271 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96116f42-07a1-3096-9878-97aab5d21f62 | -10.0403 | -53.7687 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9907c5-74a3-3fae-8cbc-e6c4ad88ac69 | -8.3576 | -50.850101 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d34a31c-64a8-374d-abf7-a5f7e108c952 | -4.337 | -55.652 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f248f8d5-f69c-3a6a-9a3e-13b9803a47e2 | -11.7849 | -50.9767 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 051d0cbf-43e9-387b-87d4-bc37eb3f5b41 | -2.5486 | -49.094898 | 2026-09-23 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82aebe0-3aee-342b-a4e9-d743babd4cc0 | -5.8088 | -49.156101 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5061d2-2246-37e0-89c2-ee3760520596 | -3.2565 | -53.949902 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a20cf573-b383-344d-a3be-6a3a7944b543 | -10.377 | -54.399601 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be823f47-0398-35ea-a171-ab138c990e0b | -6.3736 | -55.275101 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7085b18-ca68-325f-bde3-14a997cce29b | -1.2196 | -54.557098 | 2026-09-23 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8fc15ef-6cda-3b0f-bd6e-d48e45dd5bf3 | -11.7178 | -50.777199 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f70a5f7e-6127-3c86-9353-56fa0a0e9931 | -11.3065 | -51.362202 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51737170-ce1d-3eb6-9593-b72ff1c0dcf5 | -11.8899 | -45.739201 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e59904d4-1bf1-36e9-b06d-6aafdb67bae8 | -11.7778 | -50.063999 | 2026-09-23 00:58:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2a1e309-0940-3204-a977-def177152c7c | -6.3282 | -43.927399 | 2026-09-23 00:58:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d62a1d28-c9f2-3afa-a653-cfaf5f68fff2 | -11.708 | -50.779499 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34b4e435-9b79-3527-be57-13651b53f408 | -4.0428 | -56.306801 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0afabe-330b-382a-abda-2cf28ad241e1 | -4.4492 | -55.013699 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f587c08a-ce7f-385f-b316-9c673d43cab2 | -2.9552 | -54.0751 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f70788ee-219e-3cc9-97a7-d0df17e05655 | -6.7431 | -55.087299 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea94599b-dc5a-34f6-8d93-e26e85860a3a | -8.1509 | -49.540798 | 2026-09-23 00:58:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead5e85a-483a-34b3-b907-b6bf83e8e3aa | -11.6799 | -50.924999 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9787787-23b1-369d-b7ba-612478f96384 | -5.8801 | -52.043701 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8efd3f1e-f373-374f-9251-4e26c23c2527 | -9.5652 | -47.951801 | 2026-09-23 00:58:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95d03f40-6ce4-3020-aed7-c76b49505e51 | -6.6176 | -59.8979 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9520ebc-5d42-3a99-8a96-83edfbd19cd6 | -11.7114 | -50.794201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c77896a4-998b-32f1-98f6-0caae412bc1b | -3.0188 | -57.918201 | 2026-09-23 00:58:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9fe87b-4eb8-3480-80c7-6d85a329e907 | -3.6061 | -60.571499 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae7e1bca-00ba-313e-8f0f-e892f461663e | -1.8244 | -55.7085 | 2026-09-23 00:58:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974cf7b8-9a94-3282-a9ae-014c30829416 | -10.7018 | -48.716999 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a263d72b-3238-36a6-a144-6d97d83e4216 | -6.3186 | -43.929798 | 2026-09-23 00:58:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f42108d9-817b-3cbb-8c93-edf7f0f5f5c6 | -5.2701 | -60.185699 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44cc8e0-4766-3a10-8842-1403e34392a3 | -5.8146 | -47.763599 | 2026-09-23 00:58:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a13581e0-4614-3a65-b127-289a67ecbbeb | -8.2236 | -62.8209 | 2026-09-23 00:58:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9f9bc6-97f2-3316-8fec-09371a1aea36 | -4.2931 | -49.112499 | 2026-09-23 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30cb6341-dab8-36ff-9f51-dc8b7470d12e | -7.1336 | -43.060902 | 2026-09-23 00:58:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d1301838-8196-3b2f-8db7-e7153d1ee590 | -11.1101 | -48.310699 | 2026-09-23 00:58:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3ddfe5e-da61-3548-8f10-8e7e55aa3aa2 | -6.4501 | -59.973598 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37fe8453-3fa7-30a4-9782-df0dc9aef73c | -12.812 | -50.908798 | 2026-09-23 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc90dadd-1e2e-3a23-9126-fa69a8569cf7 | -14.7594 | -47.152599 | 2026-09-23 00:58:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7174d55e-d442-3501-98bd-19c2fdf98339 | -8.6243 | -54.6157 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c0c0d1-a3c6-3c52-97c5-f1fb56d43377 | -5.8936 | -52.1017 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19272fc3-bc75-3a3a-9d93-54d3746781b9 | -10.4501 | -51.275501 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f46e0887-b332-3a9c-8a14-f4f3359c32c4 | -7.0962 | -52.749001 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ef221a-be7d-37c3-afea-a6855691f943 | -6.0405 | -53.271999 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1182ebc0-311b-3ecb-8061-21fe97e4c228 | -9.7292 | -53.942402 | 2026-09-23 00:58:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7e1b19-a73b-3a63-8712-6c21c9a7048e | -5.1781 | -56.181702 | 2026-09-23 00:58:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b0272b-7f4e-325f-a1af-acbff65d50b1 | -11.7093 | -50.917999 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7040d6-5f51-3bba-8e0c-a3431fc3440f | -3.4587 | -59.548401 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37b457e7-8ad7-3144-873a-bc6d6c660143 | -6.6175 | -59.991901 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 900516cd-da75-3648-8bd1-ec4eda38f9d1 | -6.4529 | -59.9865 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86ed8ba4-16b7-3d4d-b7b5-715573068d40 | -4.2981 | -49.133499 | 2026-09-23 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95062c8a-cddb-3ec0-b881-bbc5ea04c630 | -6.0271 | -55.336899 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c2a722-6970-3392-98f5-65d11151da9a | -1.9137 | -58.261799 | 2026-09-23 00:58:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 234c50d4-0d56-345a-b625-41cb39599176 | -8.585 | -54.624401 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a4db53-b1d3-307c-bc89-fc474e5985d1 | -4.5805 | -45.6507 | 2026-09-23 00:58:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d6a5d57-5d81-3508-bda2-9b8e940a0603 | -4.4607 | -47.915699 | 2026-09-23 00:58:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7ea380-a860-3a05-bd70-e2f320e7327a | -12.8624 | -50.8587 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8dd45815-c997-358d-a26d-174a5f08239d | -6.6259 | -59.936199 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a630e66b-a5f6-3588-b655-c156a965dd02 | -4.2253 | -48.610802 | 2026-09-23 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd2652b-c612-3855-92fb-cc41f185eed2 | -4.0543 | -56.312199 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e9b2af-e10d-3d05-adf8-6e399778daea | -4.5625 | -54.922901 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 401ed275-91ca-385a-b8be-5f874f92b64c | -6.6426 | -59.9193 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab5bf1eb-074c-3e30-ad95-2a1b220dbae9 | -12.4051 | -46.969101 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fded0819-4acb-31cd-b19c-269922a4b904 | -3.9577 | -59.3493 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee12063-953d-34ea-82ff-26adea40f4ec | -10.7561 | -44.8181 | 2026-09-23 00:58:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 22ef05ba-be6c-369d-8011-afa4de112a43 | -12.8022 | -50.911098 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 671eb497-61ab-3989-bb17-c26b2f223b6b | -4.2684 | -56.256901 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746fc677-5f5a-3e2e-b079-fa09bd64c819 | -6.9271 | -46.5368 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a62ee9bb-eddb-3c33-a030-837d5f163890 | -6.6078 | -59.900002 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf3b678d-e3ea-3276-9368-1562bf10e7bb | -9.701 | -58.128101 | 2026-09-23 00:58:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3464095d-0191-3523-828f-4e852b4c0258 | -11.518 | -45.332901 | 2026-09-23 00:58:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97de1c5f-f055-3fc5-9331-2d7d8b5248e6 | -2.4706 | -57.905499 | 2026-09-23 00:58:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 278d424a-6a56-3e34-872c-36bd12fa11b7 | -11.6735 | -50.941799 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d172437-43f0-337f-a687-96f7f517dc46 | -10.8682 | -50.1507 | 2026-09-23 00:58:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d69511e-9c87-376a-be64-1ac5d3611b2e | -6.0852 | -57.614899 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf3be35-78b6-350f-81bc-22db526d56dc | -3.0402 | -54.399899 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6b7c236-ab1f-33a7-b77e-3d3eefa46131 | -2.5662 | -57.511799 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1a7eeb-a91e-3761-a4cc-ea93158c0d3a | -3.2156 | -53.9519 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c42ec1f3-c66a-33f1-8922-742f0de13d04 | -10.2666 | -50.2281 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2af978d3-428b-38d0-8132-64f4022709a1 | -2.9136 | -57.772202 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63d96a80-7f93-3c27-97b6-2957a66f2d7b | -6.7317 | -55.082199 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b9bd63-a712-3905-a1d4-454ead779a8a | -12.4191 | -46.9422 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb04c194-f292-3e06-b247-9b37c15e8348 | -11.688 | -50.915401 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 776915f3-94ea-3f5f-bc12-05683ac655b0 | 1.3989 | -50.743099 | 2026-09-23 00:58:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2437596c-b3ea-36c5-b86c-020849d9f26a | -6.0389 | -53.265099 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6aa4ae0-aeb4-3e31-bf83-262d91c799da | -6.128 | -59.9492 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5362e6a-ff70-3a80-ac07-d020f709b3c6 | -9.2396 | -59.5634 | 2026-09-23 00:58:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60186a5c-6a5a-39df-aa98-c072f1053ff2 | -14.7569 | -47.142601 | 2026-09-23 00:58:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 237cc5ff-25a7-3f37-b42b-0a85d5536d19 | -8.153 | -49.549599 | 2026-09-23 00:58:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bd40ea-2cf5-36b8-9cf6-9901594c906f | -5.8774 | -52.120602 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991aa179-dcee-39f5-be6a-f78993b38c43 | -3.8554 | -58.801701 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95330ed7-4ba3-324e-8a1f-c8d128c6361e | -4.2838 | -48.597099 | 2026-09-23 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d09ec1-3622-326a-8248-e806da1e46f6 | -12.7989 | -50.896702 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87c9cfc0-8177-32d1-943e-3403a928bb3e | -4.7456 | -48.030499 | 2026-09-23 00:58:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3af9eeb-e717-3222-8e6d-692b082b2fff | -6.6021 | -59.968201 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
