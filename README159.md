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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a6b11a5-25a4-304b-9cf4-1ce7d7e49641 | -7.712 | -46.2531 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 274.4 |
| a1c0e329-5324-3df3-b702-010ee3f7f5ce | -10.8093 | -48.8229 | 2025-10-05 13:40:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1cdfda08-8e1d-3566-a7d4-649bb405ef6d | -7.7743 | -42.6103 | 2025-10-05 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 185.9 |
| 9f6e899a-2834-30ed-9e11-91a71ee849dd | -11.5264 | -46.742 | 2025-10-05 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| dc51bc54-e448-331f-9b7a-edd12a46ce3a | -11.7912 | -48.0448 | 2025-10-05 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a4a59fd7-0ea6-3dd7-8c4e-2ffb63e2c888 | -12.5863 | -54.7679 | 2025-10-05 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| b0dd9ac2-2d62-37cd-9f57-aa40a59f6aa5 | -8.5761 | -46.3266 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 52cfd590-25e2-32ad-a691-d98e109b0b63 | -17.9408 | -57.5928 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| b96a6bc4-83ba-3453-9fcc-ef6db471f598 | -12.4673 | -45.4925 | 2025-10-05 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b6cf31d9-d292-3b8f-abb3-269c5d0494cf | -15.9829 | -50.905 | 2025-10-05 13:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e5264073-a21a-3792-b2a7-dc0b8fde1066 | -7.6993 | -42.5708 | 2025-10-05 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 25b3e8d6-d7b4-32b4-9b3f-744807927249 | -11.8225 | -45.0827 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 390.8 |
| efe49f74-fee2-30cd-9795-7ebf00b7f4a9 | -7.0367 | -42.8036 | 2025-10-05 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 65c6088e-1657-35cd-b17b-ace47078a6fe | -6.9858 | -42.3109 | 2025-10-05 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 088e78bc-f2b1-30fb-9f77-0421ae1a1354 | -13.7476 | -51.2883 | 2025-10-05 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 31a30056-8208-3961-9cd7-7f1c667bc4b2 | -7.7308 | -46.2513 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 82a791c9-1a78-3cbd-8f3f-e92223aab51e | -7.7306 | -46.2737 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e9ab5d07-9263-3b54-93b8-20df449d1fc8 | -9.9313 | -50.8898 | 2025-10-05 13:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c1fc3d2b-af22-3c99-8996-6782d65090ad | -7.4279 | -46.5016 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| efecad1e-181d-3462-a925-612bac21fafd | -21.6882 | -50.0788 | 2025-10-05 13:40:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 25f1bc89-6a92-3384-bc89-cc68fcfe5500 | -15.6019 | -52.4888 | 2025-10-05 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| cd9bd90d-7d55-3027-850f-a1177623fbc4 | -18.2569 | -53.3329 | 2025-10-05 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5638beba-4f7a-3c03-823d-2a730385a9d4 | -15.6015 | -52.5102 | 2025-10-05 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| c3d64c3c-0dce-3448-82bb-9434b368755e | -7.7311 | -46.2289 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d91fc52d-5fdb-3b97-aed8-11410476cdb1 | -9.5794 | -46.106 | 2025-10-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| c0ea4107-6046-3f55-b5e5-35424e03ff29 | -13.728 | -51.3122 | 2025-10-05 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 225.7 |
| e857d062-6aff-3ec8-8057-d3496b337f8d | -17.921 | -57.5952 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 0eab384a-c384-3e84-9b11-c01b91348edb | -10.1943 | -45.5339 | 2025-10-05 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 32bd50ff-db1f-3060-af89-1fb3f2e69b67 | -7.7123 | -46.2307 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c34b1aba-4a60-3dd2-bec0-4422451a95c5 | -11.8038 | -45.0624 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| bd2c295a-ec49-34a8-bf22-012aa6c84527 | -11.8418 | -45.0799 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 003273d5-522e-301c-835c-7ed6433cb7fe | -10.93 | -47.1106 | 2025-10-05 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 587e3cf3-8842-3b22-bb97-702a119fc318 | -8.5953 | -46.3022 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5ed2ac1b-1e96-37b7-86e2-b87db94b937f | -15.582 | -52.5129 | 2025-10-05 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 177.4 |
| e3c396b0-5123-37b0-b757-fc50a402b10d | -6.7866 | -41.5882 | 2025-10-05 13:40:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 4ae4a95a-31b6-39d2-8058-fd6c02236923 | -11.0978 | -49.8513 | 2025-10-05 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 724987f3-49a0-3ba8-b22f-43a3dbecc3e6 | -6.7164 | -42.8337 | 2025-10-05 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 29a404d0-eb34-3fd2-9d7b-1c70b065e0e2 | -8.6138 | -54.976 | 2025-10-05 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| adfc4ee8-0720-3fb7-b772-22744f0e380a | -7.6622 | -47.367 | 2025-10-05 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3bd88ffb-446b-3e18-9547-74a47c6736e7 | -7.4464 | -46.5223 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 60024200-bf45-3a7d-8037-616fd5e4f55c | -7.4672 | -43.0438 | 2025-10-05 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 3814be5a-2645-3012-bdb8-71a7c950353b | -12.3993 | -45.0183 | 2025-10-05 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| fc1301cf-a8bc-35f9-bb37-415923cd899f | -8.5596 | -47.6813 | 2025-10-05 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 234ded84-4a7d-3f12-866d-50f44a7733f0 | -9.5791 | -46.1286 | 2025-10-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 13b8495b-cb29-3926-986e-3343a2fa8b9e | -13.7473 | -51.3097 | 2025-10-05 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 271.9 |
| b3c7e4e3-b8a1-3350-a2d2-60dd7be8e52f | -8.4683 | -45.9106 | 2025-10-05 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 802ec956-6afe-3de9-9b8b-acb3f8d9b128 | -8.4872 | -45.9087 | 2025-10-05 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e06db2ce-aaba-391a-91ae-19f7b0a80108 | -8.5407 | -47.6831 | 2025-10-05 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 80e2c2b2-4c2d-3428-85f7-6200c012aa02 | -11.7221 | -45.3508 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d00e4a7b-55bc-387e-a692-dc09f3c7a1ca | -15.5824 | -52.4916 | 2025-10-05 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| adf1b97b-90f8-3dfa-866c-c0b993385ebe | -11.2429 | -47.7827 | 2025-10-05 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f3328ac7-689a-3461-a5d9-b87cc3c4b63c | -7.7935 | -42.5845 | 2025-10-05 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 5929730a-24f8-382d-a786-ad13704ed8da | -8.539 | -46.2855 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e9bccb69-378f-38a7-8ee4-a920905df5b5 | -7.7932 | -42.6082 | 2025-10-05 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| 78b85c11-6bf3-3774-8d5e-9014cdc96756 | -11.4298 | -43.4833 | 2025-10-05 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 4dd1182b-0bcf-32c7-8065-360d1948e509 | -9.9556 | -43.7632 | 2025-10-05 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 8979f51c-acef-3f13-a861-09ea9aa4da94 | -11.7029 | -45.3536 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 0f4622b0-7dc8-35f2-bdbb-93b1abc9ebc5 | -16.0774 | -51.0642 | 2025-10-05 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 46d7441c-79bf-30fe-bf85-4b4830ea8d49 | -7.4669 | -43.0674 | 2025-10-05 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 5356fc06-3066-35f5-a051-1b2ae16a8462 | -11.8033 | -45.0856 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 276.4 |
| 36842fe1-81b3-38e9-af46-0be51b7af331 | -18.1968 | -53.3638 | 2025-10-05 13:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 098194b1-ea27-3774-b44c-3c5f218e3e7e | -11.526 | -46.7645 | 2025-10-05 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| b2789d1a-da49-3439-8484-be4fef4e3057 | -7.4276 | -46.5239 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9563c692-167f-350a-b66b-d10cad905186 | -7.7746 | -42.5865 | 2025-10-05 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 95a88f36-8710-35e1-adc0-84f5cb7eb93e | -6.6129 | -43.7317 | 2025-10-05 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4af8f0dc-d78b-330d-9899-8b69e6318bb7 | -12.5866 | -54.7474 | 2025-10-05 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c1ec7b64-8c00-3a81-954e-85f325a178a3 | -7.7118 | -46.2754 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5ddd6127-7abe-3780-b5fa-e9a87e57189a | -8.1699 | -44.1608 | 2025-10-05 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 9d71c762-cccb-3bc0-b8e7-eef3e2a4a85c | -7.7933 | -44.1304 | 2025-10-05 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ba149635-8b31-3269-90d9-015bbb3148d3 | -8.5393 | -46.2631 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9d13d92b-2c6f-3b49-ad32-8d0703d699bf | -6.6546 | -41.601 | 2025-10-05 13:40:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 462e8373-06d6-35bc-938e-e0552e3aa32e | -17.9661 | -51.1474 | 2025-10-05 13:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ab1d5ace-1676-3be2-98ae-b8222d57744c | -8.8803 | -47.6061 | 2025-10-05 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6e8e8ef1-7db1-3f50-a033-c1c9d8b15d1a | -12.5733 | -48.1393 | 2025-10-05 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 56ae4f53-00fc-3ba5-9367-6ff4ebc6f5ce | -14.0037 | -44.9376 | 2025-10-05 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e2742b3f-fca2-31ae-9b26-a74760b2749f | -11.0911 | -47.7573 | 2025-10-05 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4dd48fd8-f201-394f-8cf3-dc151e875d7a | -6.7167 | -42.8101 | 2025-10-05 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 9fb11b73-1be5-3697-b0b4-a2f7deed0ff7 | -17.9404 | -57.6134 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 8da6a33e-2699-33f4-a7b8-8138f6b7fc58 | -11.8422 | -45.0567 | 2025-10-05 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| aac3414f-5cf0-349d-9b5b-b9cfbba92ed2 | -7.0369 | -42.78 | 2025-10-05 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 197.5 |
| 9cee795f-776f-3beb-bcf4-69d7a666d282 | -19.0155 | -50.6045 | 2025-10-05 13:40:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 151.2 |
| 45a16b7d-de0c-389f-949b-e534fb1b83ae | -10.4557 | -48.3827 | 2025-10-05 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 54488bcf-3d91-332c-aee2-eb911baa49fa | -8.595 | -46.3246 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 36f89b7b-33d2-3a5d-b74c-d8ce522f8e17 | -17.986 | -51.144 | 2025-10-05 13:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| db71481c-6bc1-3674-8d38-e8d9333d32e3 | -7.7885 | -44.5228 | 2025-10-05 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 20155120-55b4-3bed-b95c-08c345d0b7dd | -9.2973 | -46.0026 | 2025-10-05 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2394c35b-9c39-30f1-baf4-4d487ada572e | -8.5578 | -46.2836 | 2025-10-05 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 869daa3b-04cc-39d1-b520-8f49735ca89a | -7.8047 | -48.0558 | 2025-10-05 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b95b0eb7-b2ac-3604-b01d-f36f032cf8f9 | -17.9602 | -57.611 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| c8cb219d-11c5-3f94-9988-8dcf1d1b9e92 | -16.0966 | -51.0829 | 2025-10-05 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 108abafa-bddc-3992-b65c-4e24f7339b81 | -7.8127 | -42.5587 | 2025-10-05 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 9887783a-683e-3134-8ea8-28c34825fb7a | -21.6888 | -50.0559 | 2025-10-05 13:40:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| f735510a-ca29-31a0-84e2-823db0303359 | -11.0316 | -46.6946 | 2025-10-05 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| e581401f-ff10-399f-b087-c3b75ec913f8 | -12.5926 | -48.1366 | 2025-10-05 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| afa9c343-afaf-39fa-b0a3-8d5003344a95 | -6.7048 | -42.1712 | 2025-10-05 13:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| dfcd6682-1c07-313a-8b1e-9890e7710cb2 | -17.8417 | -57.6254 | 2025-10-05 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| bf8b738c-df4b-3b36-92a1-8526dac3fb1d | -6.6976 | -42.8354 | 2025-10-05 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| ba0ee73b-c103-3ab4-b6e1-7e79463612ac | -7.7938 | -42.5607 | 2025-10-05 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 4e3d80b3-6adf-3bde-bc52-92c85b93910f | -9.6287 | -46.6394 | 2025-10-05 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| d3651eac-d3df-3520-a979-f0df11f93d98 | -7.7554 | -42.6123 | 2025-10-05 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |


[Clique aqui para ver as próximas entradas](README160.md)
