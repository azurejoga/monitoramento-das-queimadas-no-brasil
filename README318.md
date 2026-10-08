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

## Dados Diários - Página 318

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d15c2b4d-4540-3e2a-93dc-0ed4adf4cc8f | -9.87139 | -44.83119 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 09eb4d5f-4e85-3c72-b7bc-80d50da0ddf4 | -6.17238 | -44.85523 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b2d31d85-abab-3b8d-ad32-eb55587d09c0 | -7.84076 | -40.48371 | 2026-10-08 16:37:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 127ca1c8-802d-3139-b390-371b5dc7c369 | -19.82982 | -42.92773 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 762d0358-2cbf-3298-bf36-1af59fce349b | -6.36546 | -42.9113 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 371f8521-87b4-3094-a20c-14daeddb794b | -5.71783 | -41.65736 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f0d4587e-da38-31a8-976d-658116bf2ad4 | -12.02389 | -43.4533 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 313.3 |
| 0db04b0c-df59-3c3c-a53b-d7718166f94a | -18.55556 | -43.62727 | 2026-10-08 16:37:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49b2e3be-96f2-31c9-a526-e85aad399e0b | -7.86335 | -37.82208 | 2026-10-08 16:37:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1162c021-0022-32b6-bebe-526dcc230686 | -7.48452 | -40.64831 | 2026-10-08 16:37:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 215c0dd5-f196-30ea-b2d5-1b13206fdced | -8.32522 | -45.01682 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 38e0a340-9589-39d0-8f08-594f636c39be | -13.17894 | -47.86853 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77f6eaf9-7e85-301a-b746-d8d3859ed44a | -11.58037 | -43.68117 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 256.3 |
| c86eb837-55b1-3152-ae65-f77b1a9e5136 | -11.09553 | -47.51553 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ef376e41-f2ae-34a2-b48f-d14f69776e99 | -18.13343 | -42.06446 | 2026-10-08 16:37:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6bc3f4d8-403f-3547-8ec4-cc5bb4147448 | -7.82497 | -38.86183 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b64d51a5-3ca6-3a53-ad57-0ed970b601c0 | -11.20669 | -44.8645 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c26522e3-309e-3598-97f9-e9ebbfc5142c | -19.60481 | -43.78037 | 2026-10-08 16:37:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 464cfb05-d1b2-3895-b1ad-b6779dcb2b4d | -8.34485 | -47.66231 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0392b108-d172-3af1-be46-725e89699460 | -6.85175 | -41.739 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 8a2de0d2-9df9-333c-a4f0-dcaf1c97dd60 | -9.84815 | -47.85007 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ed701bc2-ee22-36b5-a544-2fd30ff95c84 | -10.96079 | -45.38954 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 674d6b9e-23e0-35f8-9489-e4b957cd3df8 | -6.88159 | -43.69381 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f9c18cc6-4c7f-3ee8-a795-4012191f8df7 | -7.25577 | -39.40927 | 2026-10-08 16:37:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e8b9da07-1ec2-3635-b9c0-9c66b0a41763 | -12.15739 | -42.2617 | 2026-10-08 16:37:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 08d48563-3a2d-3ded-bfc1-607ee7fbb1f5 | -9.43909 | -44.60311 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 31824823-9dcb-3724-924d-06afad2e08d1 | -5.72791 | -41.64591 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 9c1eca21-3570-3794-a0ad-9e0b3c45d84b | -5.96982 | -41.35448 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 53d3564c-6e80-3ec6-9672-a334538ba8cf | -6.32044 | -43.49195 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27adcd4d-6b5d-3da7-a021-ebf42da5314d | -7.13862 | -41.8098 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ca65be7d-2962-380b-bdf7-4e5c78c71698 | -6.7747 | -44.12672 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e20bd00-0dd4-30a8-bfec-6b1c0e96529e | -6.371 | -45.79576 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 87dfbe01-a5cb-3811-93c7-e094cdcab13b | -9.77834 | -47.81872 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f95c0809-ffc6-3fb3-b14b-f25edb894ee6 | -19.1432 | -40.47013 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80611504-58e4-368c-944f-22a46f424487 | -5.96197 | -43.90508 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c5607da9-ab85-3536-a4e7-7ab6b7fe6599 | -13.24223 | -51.65364 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d07be679-e3e3-36be-a566-d71c94c611d1 | -11.97271 | -39.04136 | 2026-10-08 16:37:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c90accb4-04e1-3188-877c-4e3152b1793c | -7.22796 | -37.94837 | 2026-10-08 16:37:00 | NOAA-20 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 815b9069-8d09-3ccf-a7df-f193e8913fda | -9.1022 | -45.12648 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 0061717a-c11f-38bc-aeea-71ff851c34f3 | -8.07465 | -45.61887 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3793af34-3666-337d-b878-57b6eb6efdea | -8.19305 | -46.37855 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9d5bc7b9-83a9-35dd-9e4c-d4d46fc36883 | -7.24473 | -44.53008 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fc7fc398-ce2a-373e-9807-eadbb8d6c9b9 | -6.37255 | -44.44476 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 522530d5-5924-35d0-ac81-fb7f378d2ff9 | -11.78972 | -46.78489 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 210eebd2-788c-391a-960e-13af430811e2 | -5.81434 | -42.50433 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f45913d8-57f0-327d-9d10-faef9c8c490f | -9.82288 | -45.69326 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 45bce5b9-b520-340c-8ec2-d836fb4e7b5f | -11.08639 | -44.0186 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c006f604-537a-3c10-a5c0-12f83257c680 | -9.85143 | -57.66689 | 2026-10-08 16:37:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c6435c0-e711-3cb2-a000-17582e253503 | -5.51176 | -37.4929 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ffbe09be-606d-3a19-bb93-bceabad6753c | -7.21271 | -44.28139 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 4350934e-edf7-3fe3-89d2-20f0641c32e2 | -8.60768 | -47.98733 | 2026-10-08 16:37:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a85e029a-7acb-3f5e-b6fa-17e7120b6ac5 | -11.20897 | -49.41789 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e67ccef4-0340-3759-b844-435a523de3c7 | -7.37347 | -46.22871 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5b3bf4d-0a69-3e6a-91d6-04a008a5a171 | -11.21939 | -44.85892 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 19ff25f3-6969-32a9-921c-944614114d96 | -6.38648 | -45.78633 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f555e7d4-b80c-3f13-bffb-79a533b6e359 | -6.18097 | -44.95548 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdd6f67a-78fa-3039-8b24-289174ebaef5 | -8.9348 | -45.18621 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9e6a4cf3-7b3f-3bb7-9e67-5e2bac99f756 | -6.38783 | -42.53531 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| bae28bd9-3280-350f-b208-9a26a3e7b938 | -7.1948 | -44.34331 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a18bceeb-3376-3014-9ab2-ad21a0512f63 | -9.98012 | -45.97144 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 3cca9a26-7efe-318f-b59c-2456ace186c7 | -8.75161 | -46.84348 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2ee2b3a5-8ed5-3dba-bdb2-4342f4b4481a | -6.15821 | -39.42807 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0d677773-8b3b-3b20-818a-e79173adb088 | -9.20373 | -46.53789 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4c00a796-9b22-369b-b0cf-f9564bb2a258 | -10.76114 | -46.59178 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9b46744-1964-3f5d-a8be-a57c9e124f39 | -6.22784 | -44.97665 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d77ea607-8587-39ac-8db2-11f07e21d0b4 | -6.8563 | -41.74305 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 3ba10b8e-b15f-3a13-9189-f68d36846bff | -7.2718 | -45.53817 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81052fe9-ccad-3775-9ef9-a13367e6cdb1 | -6.89499 | -45.89276 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 364d8a69-9ed3-32b6-97fb-f00823e8b9d4 | -6.37378 | -45.79179 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2a6f1f98-77b0-3d65-a15f-3d5f1a3770d0 | -11.65115 | -43.68034 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a3c056f7-387b-3b51-8ccc-02e3e62e6769 | -8.30175 | -45.7286 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51a3f43d-ce11-3631-b5bc-b66e47d43241 | -10.23835 | -39.20515 | 2026-10-08 16:37:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6a67096a-6105-3152-b268-2fe6fa9273db | -11.62045 | -43.65258 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| cbad168d-2c23-3ac4-b451-505f86daa832 | -8.3216 | -45.45901 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3399689b-45e3-3e71-8ddc-0035ca00bcbb | -7.88111 | -54.9948 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d6936d5f-52f9-3825-a343-dcfcfbb78018 | -6.3321 | -43.82764 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6689373d-3731-35d6-b5e7-d37defc08188 | -14.0072 | -48.75595 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 65c53e99-a966-3ccd-b461-8e8559d43379 | -13.12216 | -46.35909 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5afcd9b4-bdce-3d3c-aaf6-c3a41b92f711 | -9.89772 | -44.84784 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 08ef3d8b-467f-30f2-8311-033b7737afa4 | -12.23128 | -44.75291 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| db533e12-7855-308b-8779-b472741b3b37 | -7.23061 | -37.94498 | 2026-10-08 16:37:00 | NOAA-20 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2f8e4eda-3f84-3b0c-a72e-696eb438120e | -8.08469 | -55.30428 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 73a8a3a0-aac8-32a4-a18a-62b5583fb121 | -6.90889 | -43.93175 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e85bfac-c5b7-30e4-b831-0b773ec61863 | -19.32177 | -44.02147 | 2026-10-08 16:37:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1edf0bae-6391-3fdb-aec0-d00220ad0a5e | -12.32085 | -47.05191 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f9e2f6a3-5f4a-360b-bab3-fb88e81cee8d | -5.77316 | -42.07032 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 81b8da56-20f3-3518-9c55-402dc6ab3ada | -9.6216 | -57.88118 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1c241fc4-8f82-3d5c-8d43-57f708516b07 | -11.58592 | -43.67288 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7f17ddf7-f72e-312d-a44d-cc11fe7efcb6 | -7.60055 | -42.39225 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 864b1cd2-0f06-3008-87ff-56e55562cdb3 | -6.33487 | -35.15963 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0d8f29d1-1253-3418-b8ff-f33cb4bf4c12 | -6.68258 | -46.01521 | 2026-10-08 16:37:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e16f03e8-9b95-3fd5-9b4c-8c8c4ea7ec6f | -6.22082 | -44.86542 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 70c104b4-f556-3ded-8dcb-3779bd066b8f | -11.83891 | -43.52814 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 947fc2e0-bd01-3f0e-b581-40c11e349304 | -6.52441 | -45.40193 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9e8e08af-6fd0-3b31-a9f7-5ba2d94491cf | -6.45265 | -46.02021 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2cd001f3-02de-35bc-8b79-a8939e262cb4 | -6.05686 | -42.59714 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| be57b59e-50c5-3391-8aa8-f4bc99704512 | -6.52773 | -45.40142 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3e3f0f03-2c07-3087-b149-a6f175f75ca6 | -6.03757 | -37.28041 | 2026-10-08 16:37:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 393289a2-6fe7-32f8-8db2-586e66b84146 | -9.57732 | -46.8399 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| de26fb50-b01e-33b9-88c4-1da8ad8dcdb3 | -10.86646 | -45.55219 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |


[Clique aqui para ver as próximas entradas](README319.md)
