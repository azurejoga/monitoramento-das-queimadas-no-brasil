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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8067ebb3-69c8-3144-843b-2261e766e24a | -11.1723 | -51.294 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2a5e1527-9b09-35f1-afde-43ed0ae5b4e8 | -7.991 | -46.4954 | 2026-08-30 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b8624e54-2284-3cbe-89c5-5b402ee5ce80 | -10.7647 | -50.6579 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| facc89ed-845d-3539-8db6-97e02edb3ef9 | -11.1726 | -51.2728 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 89563de3-4b71-3626-bdf3-cd1552011686 | -8.1345 | -45.4923 | 2026-08-30 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2e786694-d8aa-31e0-a149-91c91003bb11 | -7.0437 | -42.1861 | 2026-08-30 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 30208526-c6cb-326c-8018-bd442336140b | -14.5634 | -52.0344 | 2026-08-30 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| feb16b26-6184-3665-ae63-d9f0d0274e6a | -15.5579 | -56.2733 | 2026-08-30 13:50:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8aab2152-b7ef-32b0-bc2b-dbd672222a4c | -15.4048 | -52.6437 | 2026-08-30 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 828c239d-e074-316d-a95c-5896b6833696 | -14.4197 | -52.5413 | 2026-08-30 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 93fa94b1-43d9-3007-89c9-65455688548f | -11.2317 | -53.9958 | 2026-08-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.2 |
| a1e7b440-4310-33e0-96fc-5406c0385a2f | -14.1456 | -52.8082 | 2026-08-30 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a0b3bb01-02a2-3c29-8db4-41858d70801d | -8.5971 | -54.7553 | 2026-08-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8d36e07e-0de4-3c27-84d4-99d3b393b189 | -13.856 | -54.1175 | 2026-08-30 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 5a045c92-9a06-30d1-9c22-a4a04d98ac89 | -12.3619 | -48.1903 | 2026-08-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e2aacac9-516b-3f18-bfb7-b502468fca13 | -10.7649 | -50.6366 | 2026-08-30 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a3962e90-b28e-355f-b5f5-aed0bdbb0648 | -10.9216 | -50.2571 | 2026-08-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 69d27f0d-0102-3f6f-baf4-19b952efa124 | -3.6398 | -60.5656 | 2026-08-30 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 23769ec4-72cf-31b6-bdf2-bcce32463d83 | -3.6215 | -60.566 | 2026-08-30 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c344a5d6-b74d-344c-a3b2-c9af8788f372 | -7.4949 | -55.3462 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c3c4ece9-715d-3e7a-99cb-8355597c358d | -7.5137 | -55.3051 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fb780e2e-2eba-36f8-86de-7b33d31fa825 | -11.2506 | -53.9941 | 2026-08-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 000f63d2-ccf2-3371-a72a-38aea150412f | -7.5136 | -55.3251 | 2026-08-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 842e828e-ebb7-3df1-a10a-3f4595cd1179 | -8.0098 | -46.4936 | 2026-08-30 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2085095d-74fd-35cc-a9e4-e821d58d164f | -11.2443 | -45.3497 | 2026-08-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| abbaac21-8d2a-31c7-970a-620b64002bf9 | -3.6398 | -60.5656 | 2026-08-30 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 35978e02-33ef-3e63-b2ad-3686e3a7db6b | -13.3223 | -51.4707 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5efd6826-116e-3393-b7df-0aface82246d | -10.7454 | -50.6812 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ad86e86a-d893-37c3-8ff1-c93e99dca291 | -6.8753 | -59.4557 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d5fd7cc9-172c-360b-9ccf-d5429fb86bdf | -8.6158 | -54.7541 | 2026-08-30 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| cf2faa4d-29c1-3237-bcdd-3f276da75c8b | -15.2283 | -57.6517 | 2026-08-30 14:00:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 62c7d3e2-af3c-392b-aa10-a11523846572 | -8.5971 | -54.7553 | 2026-08-30 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ec0d9b45-f308-38d8-bc6e-7ca3c4528f7d | -6.9361 | -55.7157 | 2026-08-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 00cd3d4f-4013-334f-a649-784c05293093 | -7.9425 | -44.2538 | 2026-08-30 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5d4c231f-58ca-3694-bd74-b934d34a3d79 | -13.3425 | -51.4042 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 137276d4-7fbd-30cd-a1eb-b20c30da409c | -11.1723 | -51.294 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 76710d02-701d-3bc7-9e53-efe9f4919de3 | -13.856 | -54.1175 | 2026-08-30 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| bc650159-d168-368d-b29b-b0a492f5c4fa | -11.0627 | -47.1385 | 2026-08-30 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 1e83dd99-0130-37f5-b9b4-7afe9d2bceac | -13.8749 | -54.1361 | 2026-08-30 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 9588f89d-a2ba-334f-addc-417f1378cde7 | -11.3619 | -45.1724 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 07bf1d58-f2e3-35a3-87b8-5f4e0a6d6cd3 | -7.9907 | -46.5177 | 2026-08-30 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 63669530-6292-3b26-8cab-f9900f98360e | -8.5969 | -54.7755 | 2026-08-30 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| f09b0490-af04-3601-959a-66a587db41f9 | -11.2443 | -45.3497 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| ff7a1a14-2135-3833-9ca0-d777587397e4 | -7.5661 | -61.3239 | 2026-08-30 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e155801d-0287-382f-b07f-7e6c9e82b059 | -14.2985 | -51.7286 | 2026-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| a8bccf72-92d2-3d41-908d-d3fa963043b2 | -7.2932 | -60.6096 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a19aa5b2-a433-3b4f-922e-634c8f4df9b9 | -10.7839 | -50.6346 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 24313474-d9b2-3fe3-bc41-39738edfc308 | -11.2503 | -54.0146 | 2026-08-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 190.4 |
| c326f6f2-b647-334e-a1b0-db4fe37c0ea8 | -6.8613 | -41.6532 | 2026-08-30 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| a4ba632e-2ed1-36db-a835-4cd3f88393ba | -11.2485 | -45.0963 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 94f42bac-6198-3486-902e-f7e03d43e7f8 | -7.4949 | -55.3462 | 2026-08-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8f4ebff2-c23a-31b8-832b-94404dcff3c2 | -9.8927 | -60.2752 | 2026-08-30 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a10925dd-1f6e-3f64-a08d-559e436bd536 | -7.9838 | -45.5072 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| db31b0fa-a350-3b2b-8f7e-103566f9124c | -8.739 | -45.3844 | 2026-08-30 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1dc23f5b-0a7a-3741-b2a3-a5b84d85dfd5 | -7.546 | -44.3395 | 2026-08-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 0d58bbcd-8bd2-3026-8759-9394fea1f479 | -9.1533 | -59.5027 | 2026-08-30 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 763624b9-173c-3212-ada2-72ce4cd0886b | -3.6215 | -60.566 | 2026-08-30 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0861a6b7-6d29-35ad-916d-6a7820b8cca4 | -11.2446 | -45.3267 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 5bfff816-d60f-3c34-afb2-15658161b0db | -11.2314 | -54.0164 | 2026-08-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 57854526-ca3b-30cd-9829-b9a7e90aa0b9 | -9.0673 | -64.2548 | 2026-08-30 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2944ddd3-eebc-3f6e-a00b-9d1f75e34590 | -10.1538 | -45.6982 | 2026-08-30 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b9e19be8-20f0-3620-9b06-eb008e2b0771 | -14.1456 | -52.8082 | 2026-08-30 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 1074991d-c8fd-391c-b126-e22971424774 | -11.063 | -47.1161 | 2026-08-30 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2b3f76ad-c94c-3e83-97a9-e00d6edf9cd9 | -12.3619 | -48.1903 | 2026-08-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ed9090d5-8c3f-38bb-b9d0-dedc792ae01c | -7.5644 | -49.5857 | 2026-08-30 14:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1bd611ca-cdd2-33b4-863b-ed2674fb8f6c | -14.7605 | -48.7245 | 2026-08-30 14:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 162.6 |
| d5264172-7d01-3129-adeb-3dc178e06fcf | -10.7434 | -50.8302 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| da3d1f8b-c64e-3776-b4c0-710447bc8d21 | -11.2294 | -45.099 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 246.5 |
| ae04e397-fada-3964-864d-a5a038073257 | -7.2933 | -60.5905 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a16705ff-1fb3-3bc3-a1b1-cb4354cec381 | -7.495 | -55.3262 | 2026-08-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 23a325e8-2126-3b7b-9195-bf7f871f1eb4 | -6.7699 | -55.6644 | 2026-08-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 572c3dc1-7b61-3799-bb0e-94532b2c81b4 | -9.7832 | -46.4202 | 2026-08-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 9a5a9757-5aac-364f-adb1-f05b85ed0a4e | -10.7407 | -54.0401 | 2026-08-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| e2bb50f4-030f-306e-bfe6-19c4eeb09851 | -3.6216 | -60.547 | 2026-08-30 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 4c43c18d-12ce-354d-9890-a62d10200ba6 | -10.7644 | -50.6792 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 6666d9cb-b4b8-3b4d-9f20-4e98306f4246 | -13.3943 | -51.7595 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f866d3c5-594b-3e69-880a-c8a38b3eaf36 | -7.9422 | -44.277 | 2026-08-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 339.8 |
| ebfce40e-09fa-3f0d-bd67-0ebb22c18234 | -13.3422 | -51.4256 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3bc66606-2ad1-3e21-b125-d3d83240f082 | -14.1649 | -52.8058 | 2026-08-30 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 9062555c-d8d8-31a7-a4ac-51f6d541e7ba | -13.3419 | -51.4469 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b8999acc-86d8-35db-9d32-b184ef0ceb68 | -5.4876 | -57.1416 | 2026-08-30 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1a669c43-dbdd-3cc8-a409-f81ad9c0f6c7 | -14.4197 | -52.5413 | 2026-08-30 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 206.3 |
| eb2cb24b-00c8-3198-bd28-ec8210d9a1c4 | -21.038 | -57.8074 | 2026-08-30 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 15cbe6f5-1d9e-318c-ad37-1837193a2c9f | -11.0057 | -49.6677 | 2026-08-30 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a633a97f-07ad-36cd-ad05-6962fe3b6873 | -6.8799 | -41.6754 | 2026-08-30 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 931161ef-a33e-3425-b69e-145d9923cab2 | -6.8569 | -59.4564 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 79b6c9e3-f04e-31d3-8e8f-8a1143e2ee7c | -5.871 | -57.7715 | 2026-08-30 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a772f48c-1955-3933-ac6f-b41c75fe0424 | -6.861 | -41.6772 | 2026-08-30 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 273.1 |
| 524a7e82-cc91-3cfb-8627-db2f533e5c5d | -7.9419 | -44.3001 | 2026-08-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 311.5 |
| bb5b5fa2-b3e4-3f2b-b4b9-28c48c6840ad | -11.2829 | -45.3214 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 8a7e804c-d944-3086-ab8f-881b10cf6253 | -7.991 | -46.4954 | 2026-08-30 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 60d5fa13-945f-32ef-a6e3-27afc9a441a7 | -13.8752 | -54.1153 | 2026-08-30 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| d81d7915-54a8-3737-a400-fda3869ef816 | -11.2317 | -53.9958 | 2026-08-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| edab5f82-1b78-353d-b7ec-e3fb5bae77e3 | -8.5968 | -54.7957 | 2026-08-30 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6707d10a-a324-33f7-b8ce-8070b4a34544 | -12.9221 | -45.8582 | 2026-08-30 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 6cf397e7-0a08-35b0-944c-8bb05f0e8b3d | -7.6964 | -61.1473 | 2026-08-30 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2bef1dd8-a682-380d-9fd1-c806feba62cf | -7.3118 | -60.5897 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 2dff34fb-9d03-3768-b69e-30a2cc36bccf | -8.1534 | -45.4904 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| aec7cfa3-5660-3ecb-8483-c73b24cf86d5 | -10.5598 | -50.4236 | 2026-08-30 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8f56433e-f94b-30bb-af07-3df2f76ddfcc | -4.9605 | -55.8226 | 2026-08-30 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README83.md)
