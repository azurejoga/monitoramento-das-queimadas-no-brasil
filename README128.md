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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afbffec3-b081-3380-bc92-d3c6d356adf8 | -6.8263 | -55.5421 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 758bcaff-ca0e-3f4e-a07f-ac809a9d408d | -6.7484 | -59.075 | 2026-09-21 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f5a736ad-f6fb-3402-bff9-e2a8b8371b5b | -12.4012 | -47.0255 | 2026-09-21 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 343.7 |
| be77cdfa-3bd3-3b99-a3ee-2c7e6ec7d302 | -9.8307 | -48.451 | 2026-09-21 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| ef41620f-d7b6-3548-b638-a42bc432c609 | -13.2033 | -51.7193 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 609f68f6-9007-3c81-853b-34512afdb89d | -10.9361 | -50.5759 | 2026-09-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b3857485-8473-3a77-aa9c-18c76fc060c7 | -5.6781 | -43.4125 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| dbfee4e3-ff58-3eca-88a6-88921533b4fc | -11.3419 | -51.3606 | 2026-09-21 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d69f34fe-e929-3cbe-bc0c-ec13076c82b8 | -3.3183 | -57.8677 | 2026-09-21 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1750ec15-6fc4-3ac1-b290-935cf0c93744 | -13.2596 | -51.7973 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 87d49196-ab40-3541-a93d-5f6ad3e85fdf | -10.7652 | -50.6153 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 195232de-263d-3803-882c-1d04b2da2086 | -10.7655 | -50.5939 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| a302dac0-1509-32a0-927b-a2637d574599 | -6.8448 | -55.5411 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| efe525d6-253a-333b-afd6-ad66842541f8 | -11.8014 | -49.8129 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d53c8beb-5995-3ba8-aaaa-7a26ea6d8c04 | -3.7856 | -60.7335 | 2026-09-21 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 0635324d-fa3c-3652-b532-66f710a3e7f0 | -6.3748 | -60.0128 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| bf503f31-bc76-3fa1-8c1b-4b30defdbde4 | -7.5059 | -46.2269 | 2026-09-21 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 02f71f9d-db93-3e58-bd42-e6b0565058a8 | -10.3917 | -48.8915 | 2026-09-21 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 58eeee60-4208-3bfa-b8bc-823e39cef6c6 | -12.0451 | -50.064 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8eba5f03-ea6b-3ea5-9490-9195d0555173 | -13.2794 | -51.7524 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| eeb06e99-6c73-390c-b02a-a5e349244b92 | -9.5594 | -66.0359 | 2026-09-21 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d5ae55c8-afe7-3fb0-bfc9-c106db0be5ac | -3.753 | -59.419 | 2026-09-21 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 20cb9189-de89-31c0-9c56-819bf0dc3873 | -6.0196 | -51.7893 | 2026-09-21 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c1851d95-1192-3906-9182-8fe81baed40d | -11.7823 | -49.8152 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3cd7dfce-9b8e-3514-a152-2619c2346bff | -14.0993 | -52.1163 | 2026-09-21 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| a298e1df-711d-3b05-b0fe-7efab47c9175 | -11.3603 | -51.4009 | 2026-09-21 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 78dbfbca-555a-3eeb-b09c-d22771e1ab0d | -12.5412 | -50.0676 | 2026-09-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b314bd54-3438-3421-a36b-d62e0bfb1d03 | -12.3025 | -50.6774 | 2026-09-21 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 231.5 |
| aadd77df-f245-37cc-a89c-b991249fc9da | -3.4554 | -50.6136 | 2026-09-21 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2266b8fa-5b50-327b-b36b-b627731c88b8 | -10.7842 | -50.6133 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e8f1ee62-56a3-371b-852a-8787ecb08584 | -6.5571 | -45.5434 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 4ff672f4-64e5-3ba6-961d-ae6662317e08 | -7.4092 | -44.7885 | 2026-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 4f5d0656-ba1f-3f5e-bd8a-e53869ba46cb | -13.9118 | -48.5669 | 2026-09-21 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 311991c2-8ad6-3162-8d69-9587bf6567ec | -6.3196 | -59.9956 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8c35b0fb-a5be-37af-80cc-c42ca73cbd2e | -5.1984 | -56.1103 | 2026-09-21 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ecd4f725-2bab-3bda-8fea-0b109deab303 | -5.7504 | -43.7091 | 2026-09-21 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 257.9 |
| ef901558-2579-3087-ad5b-4ee43a78ce6f | -10.3914 | -48.9133 | 2026-09-21 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 671b6c0c-b7c6-3190-8cb5-b6d8e3453545 | -8.7914 | -48.7285 | 2026-09-21 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c055bf96-3398-3814-b87e-d721656564b8 | -10.7463 | -50.6172 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 35d46300-7788-386f-95eb-eefa341e116a | -8.1871 | -54.7824 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7036a13c-fee4-3392-9399-9caa87b98be6 | -11.8715 | -48.9792 | 2026-09-21 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 74543e84-afd7-31ad-9b94-9f6a3000e970 | -3.6449 | -58.8647 | 2026-09-21 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 94d72af2-c872-3a06-aea9-50b92a9b52a1 | -15.4471 | -48.4566 | 2026-09-21 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| be4d0e8a-372c-306e-8ee4-5c326a2643cc | -8.0279 | -61.3626 | 2026-09-21 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0c7a6dbe-3ac3-3c02-8063-3fec253d5c2d | -6.9037 | -42.9105 | 2026-09-21 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 780f3641-da68-332f-bd29-697ef69cc11c | -3.4554 | -50.6136 | 2026-09-21 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ba1c824b-ec1f-34b2-93c4-32d367a1984c | -10.7626 | -50.8069 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 749d1d23-77c5-363c-b050-d813e81facf1 | -10.279 | -50.2391 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 93dac13e-906d-3bc2-8fd3-6c548c05a529 | -4.4303 | -55.0867 | 2026-09-21 14:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6b8221dc-8c13-3109-bd4f-fe5bcee72cf9 | -6.8466 | -55.2817 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| cd302e99-0333-322c-88a3-99904ea672bf | -6.4301 | -59.9916 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c6666ce1-e678-337d-8217-3ab471738c19 | -9.247 | -57.1488 | 2026-09-21 14:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a0d66e8a-2f59-30b1-a79e-c20e4bf45e9c | -6.1653 | -47.5052 | 2026-09-21 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ef11a554-f0b3-3135-b347-a86d22b5f52e | -9.8307 | -48.451 | 2026-09-21 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| a2fd393b-ec6c-30ce-a605-dd43d4ea8aed | -8.1686 | -54.7634 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8b29d578-da57-3700-bbef-3dba38389b2b | -11.662 | -47.7737 | 2026-09-21 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5303ce0f-90d6-3b70-ba29-bbdca9783441 | -5.6223 | -43.3701 | 2026-09-21 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 5d3d5043-dce7-3048-a85d-ace2405888dd | -11.3419 | -51.3606 | 2026-09-21 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| a5846717-1b8a-3b7a-b5ab-fa15f2bf8cbe | -13.0678 | -50.6256 | 2026-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b99c0c17-3235-3f64-98d3-26372c6f25c4 | -11.0412 | -54.1362 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 7ba40ce4-de4a-3818-8fa7-3c3ecee24dc8 | -10.8002 | -50.8243 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f835e44c-5223-3fc9-813c-bdb52fdbedba | -10.4919 | -51.279 | 2026-09-21 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 61402bfc-99d9-37f9-8999-9738a1458d16 | -6.4486 | -59.9717 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 3f96278c-9d50-3fe5-844a-cee9f2de99ef | -4.5774 | -42.9512 | 2026-09-21 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c4a4dd99-f5bb-3e22-9591-9d7cac49f4f0 | -9.4567 | -45.4178 | 2026-09-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 255.9 |
| 54e844c7-80dc-3cb2-b54d-873e2acb7497 | -10.2982 | -50.2158 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| da70535a-095d-3327-ba72-88add4b1d60f | -6.7484 | -59.075 | 2026-09-21 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b3a8524f-49fc-31ee-be6f-2d74d0ae05e0 | -3.2162 | -42.4833 | 2026-09-21 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 7ee799fb-18bf-3093-a07d-bf8021309042 | -6.5569 | -45.566 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| be2240d8-e04e-3b26-8629-6d019e05ce83 | -11.5496 | -51.4228 | 2026-09-21 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d6568fea-9d81-38d7-b4ab-f3d8f87412e9 | -6.3196 | -59.9956 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bae88afa-84b1-310f-ad2b-2a7fc5f1fc2f | -4.9535 | -45.1374 | 2026-09-21 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c9b88f73-4685-3171-b4bc-49ad975615e4 | -8.0279 | -61.3626 | 2026-09-21 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f4cc22e7-9ba1-3d4e-8c4d-77e5767c67ac | -10.955 | -50.5738 | 2026-09-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1e5d5c20-45bd-334a-9485-c6729de57623 | -6.6761 | -50.9381 | 2026-09-21 14:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ed954918-4034-3e7a-a4de-c6a3a00fb89a | -5.8274 | -47.7898 | 2026-09-21 14:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e694b311-f781-35a6-9780-4ba28385fa1b | -10.8924 | -53.9652 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ad3d3e20-f50b-3637-a3d0-4a3b3719d2d0 | -3.753 | -59.419 | 2026-09-21 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 028ec637-7168-3388-905d-c980acbe2c36 | -3.0507 | -50.2702 | 2026-09-21 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| fa5a51eb-310c-3b66-8bff-2d3183e85244 | -14.0993 | -52.1163 | 2026-09-21 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 688e482b-9cb1-3fc1-ac87-7cceec514a99 | -9.3986 | -48.3213 | 2026-09-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 66527184-8052-370c-8c52-d8e7250cb743 | -8.7534 | -44.3053 | 2026-09-21 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 0c88cb1d-cc15-3e8c-890e-fc524918ebcb | -3.6631 | -58.8835 | 2026-09-21 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 352abaf3-30a9-35ac-9c7a-69683208de1f | -10.9112 | -53.9635 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| bb9e2af8-7c67-3de0-8946-0819b4b43bb3 | -8.7723 | -44.3031 | 2026-09-21 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 348.0 |
| 99e139f3-2531-348c-aff4-48cf2a235ea3 | -6.1175 | -59.9452 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ed3aedff-e1b9-32b0-a198-d0fb876acb8c | -13.9118 | -48.5669 | 2026-09-21 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9b80c227-abc7-3ec0-add6-aeeaea6bbb70 | -6.3918 | -45.2175 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f2a34ea0-71ae-34e2-bad1-08286018c9ea | -6.4671 | -59.9711 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e3334024-1f0b-3296-9263-5a650030e874 | -8.0465 | -61.3427 | 2026-09-21 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b475941e-3b84-313c-ac9a-f71b2d29f6cd | -6.4107 | -45.1934 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 60df51c1-4a82-30fc-9367-e010bb69011c | -5.6599 | -45.4976 | 2026-09-21 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ad508260-eb13-3be8-9a8a-6701ab687efa | -12.4012 | -47.0255 | 2026-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 4f6900a5-8424-347b-ace1-20424762da12 | -9.977 | -50.248 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b010c1e4-8c8c-3dd0-bd9b-7812814d338c | -9.238 | -46.1894 | 2026-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ff594f95-6df6-351b-ae20-9c82a14738ce | -9.2759 | -46.1852 | 2026-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 136cddd7-f2ac-308d-be05-f182b4bfa1e0 | -6.001 | -51.7903 | 2026-09-21 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d619c92c-e8ab-3df3-a53f-8e1c0c873820 | -10.8735 | -53.9668 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0a12e7c0-9802-3e3b-8344-443ad60e6cf2 | -10.9361 | -50.5759 | 2026-09-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2e295fd2-ba64-3ca1-b41c-db28c79da97d | -6.5571 | -45.5434 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |


[Clique aqui para ver as próximas entradas](README129.md)
