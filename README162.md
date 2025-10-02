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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23542155-2b95-3f39-add8-b96aa443fefa | -8.5204 | -47.8167 | 2025-10-02 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f2aa66c7-e7d5-34a3-bd03-5e38b10f1f56 | -6.7814 | -45.5929 | 2025-10-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| b2ea29de-27b9-3e5c-86f5-0a8121274aec | -9.4275 | -47.5501 | 2025-10-02 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 00b6699f-dcb1-3c36-acba-764c848264c8 | -15.7905 | -43.7155 | 2025-10-02 14:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 418.1 |
| 5c9a7a22-a348-3285-ab26-27252a1413b9 | -6.7163 | -44.6216 | 2025-10-02 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7842e863-24a0-3cde-b5bb-40602f2b41f9 | -13.3611 | -48.1159 | 2025-10-02 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4dcafe2a-4c6a-362a-9d73-638f05684d1e | -9.336 | -45.9305 | 2025-10-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 0ce1b4f5-63c4-31e6-8108-abc4a53f8b0c | -5.3956 | -43.596 | 2025-10-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 13810bd8-61ea-35d1-9cf7-66afdb76aa64 | -14.5937 | -48.3281 | 2025-10-02 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 3150b26f-e455-34a5-bc6f-596ec84e951a | -6.7816 | -45.5703 | 2025-10-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| eba4d945-5d74-3301-ba2b-7db68e616b28 | -12.917 | -45.1215 | 2025-10-02 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 8a862372-8f58-3f1d-9278-58c9f2776b3e | -8.1702 | -44.1377 | 2025-10-02 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 169.8 |
| aff4e9be-a911-3778-8a85-0b54c75bfb85 | -8.8165 | -46.682 | 2025-10-02 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b570865b-5afa-345d-8680-54188d7653e8 | -9.9031 | -45.978 | 2025-10-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 89d5bb7e-eb87-321b-9951-707cd554b62b | -4.3713 | -43.0105 | 2025-10-02 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a4e53bef-e928-38cd-8c78-224244d17d16 | -11.6059 | -50.159 | 2025-10-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 0769796b-a05a-359b-83dd-b562d058eb90 | -18.1968 | -53.3638 | 2025-10-02 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 143.0 |
| d68fbf3a-5c6f-3764-845e-cf73d4ea2971 | -15.3067 | -45.0713 | 2025-10-02 14:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 308.7 |
| e72a6ea7-f67d-3bee-9309-7cbd8d23036b | -11.8104 | -51.7746 | 2025-10-02 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8bd9a506-8fa4-3b0a-bf1f-4766ede35b33 | -18.1782 | -53.3024 | 2025-10-02 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 254.3 |
| 21cb0a30-3105-3dad-b700-72ba3ebbb067 | -13.1747 | -47.7869 | 2025-10-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ccc23c95-03ab-374f-9fd9-bd17363a50e9 | -10.1845 | -50.2487 | 2025-10-02 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4e6f6a3b-0bef-307c-bbca-d4038821dde0 | -5.3769 | -43.5973 | 2025-10-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d8cad051-d5a8-3acc-9e66-b043fb7bc55b | -8.6722 | -47.6924 | 2025-10-02 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 900ba261-3e4b-3ced-b223-4c5307ee3ce0 | -5.6236 | -43.23 | 2025-10-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5d0af477-192f-36d4-bf8f-e36b8139acf3 | -10.7319 | -47.6461 | 2025-10-02 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 5acdd20f-2a25-3250-ad30-d1c3a0f15665 | -10.937 | -46.6618 | 2025-10-02 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 1ededd15-06ee-3a9e-a6e7-4cd90edd161a | -8.5272 | -47.2437 | 2025-10-02 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 211b0226-80ec-3c04-8257-b7d06cdc7d9c | -6.7626 | -45.5944 | 2025-10-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 6e45c8db-e3a2-3298-b512-338cd89a2570 | -5.7575 | -42.9387 | 2025-10-02 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| cf8d3ab5-e678-35d4-940f-c71e6ce028ea | -13.7958 | -47.5587 | 2025-10-02 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d35039ea-9ba0-3254-8d40-91e0a1887734 | -7.0178 | -44.5036 | 2025-10-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b1df9cfe-27ea-3551-93a7-b304885b3148 | -11.8242 | -44.9901 | 2025-10-02 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ef286b38-3011-3b9e-9703-fb16c4ed5bd6 | -11.8291 | -51.7937 | 2025-10-02 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 86d0f061-8250-3f1d-a23a-b072c1f1cc1b | -12.9363 | -45.1184 | 2025-10-02 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 8b4ae0a6-ddb2-3112-aa72-5f750d00f108 | -8.8929 | -46.6072 | 2025-10-02 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4caeddd0-22bd-3ee5-bdc3-8e3e2f6aec8b | -8.1513 | -44.1397 | 2025-10-02 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 276ec22e-fbd2-3247-b6f0-e9a3d8b25157 | -11.8101 | -51.7957 | 2025-10-02 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 0ac58cf4-a8a7-3be6-af14-e3f6a6cefcf4 | -6.4945 | -44.2962 | 2025-10-02 14:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 64fde5af-8c69-36bb-a037-98a0e038ed37 | -7.8188 | -46.7783 | 2025-10-02 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8a579dde-a1f2-3d9d-9080-92e6e1750d1b | -13.9779 | -48.1346 | 2025-10-02 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 1d02542e-a7ec-381c-846b-d9b573682cc7 | -9.4412 | -47.9448 | 2025-10-02 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8019dff0-3c1a-300a-84e5-a2dadc76958a | -7.7311 | -46.2289 | 2025-10-02 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b856c12e-c79d-3de5-ae98-fda982ff144c | -11.6318 | -45.0415 | 2025-10-02 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e1f855e8-eafc-32b3-af8c-9a5911eff80b | -11.0518 | -46.6246 | 2025-10-02 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| b064cd72-7ad0-3f4d-85ac-fac052c8f4d4 | -9.9376 | -43.6953 | 2025-10-02 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 0189a778-0146-3f78-bbcc-0a520c0755e6 | -13.7876 | -51.1974 | 2025-10-02 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 184.9 |
| d02cdb3c-8003-37c8-957f-44aa9123fc11 | -14.3119 | -45.9736 | 2025-10-02 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 15d98c1c-ebba-3ee1-98a4-e2dd7b9a35ca | -5.3193 | -43.7636 | 2025-10-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| bc01f366-64e2-3310-939b-ec40aeecba53 | -9.3392 | -45.7039 | 2025-10-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f9ecacf5-1ddc-377a-9915-3d07c3ea995b | -13.5841 | -51.8845 | 2025-10-02 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 7d223b7a-8d02-3722-804b-ed9f20c5c138 | -11.0225 | -49.8167 | 2025-10-02 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 447eaeb0-65b0-3773-8209-0ee7b0635d44 | -14.2924 | -45.977 | 2025-10-02 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 3aa87dbe-8bf0-3d1a-b3de-9052ab21ff1e | -6.1796 | -43.907 | 2025-10-02 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 73957afb-7714-36c8-861b-3a7d17fdb444 | -6.2411 | -45.3198 | 2025-10-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e04dad75-5e87-3df6-98cd-25899b413dfc | -7.8879 | -47.3031 | 2025-10-02 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 8f7515a0-98b3-3040-b1a1-54fdd4e5aff5 | -12.5001 | -50.2453 | 2025-10-02 14:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 058db76c-a888-3ab1-b85d-65baeec466fe | -15.287 | -45.0751 | 2025-10-02 14:40:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 476fa416-44e0-351d-9c85-40cd255a2c93 | -14.8261 | -51.3997 | 2025-10-02 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 4fcafd08-6fe4-3cb4-96a5-48a57cdf41fe | -14.3139 | -45.8811 | 2025-10-02 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 860ffaac-80f2-3a87-a8ac-9ac4a8ca2ec2 | -13.3131 | -47.5876 | 2025-10-02 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fd78f50f-b20e-3682-90e0-dd58e60eae9d | -8.5773 | -44.7623 | 2025-10-02 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d4121602-ba03-3b99-ad81-14095d1d9777 | -14.4255 | -46.115 | 2025-10-02 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 285bd61a-28ed-379a-b6ed-442a82e8df82 | -7.8882 | -47.281 | 2025-10-02 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 1328d753-39e9-316e-b629-b4acce8ae425 | -5.826 | -45.7334 | 2025-10-02 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 84c6cc39-82bb-3e48-a0da-8430719636eb | -18.1972 | -53.3423 | 2025-10-02 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 2c525d56-5e78-3d19-afda-3be9b05a20fc | -12.4998 | -50.2668 | 2025-10-02 14:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2cf85e2a-d820-33f4-a34c-158bdc84caea | -11.5869 | -50.1612 | 2025-10-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 176133c9-db4d-36c6-a17f-ef2772a43c72 | -9.8896 | -46.9226 | 2025-10-02 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f69fff3f-27f8-3306-8c91-bb8b67085631 | -7.8092 | -47.6399 | 2025-10-02 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0d918946-ec14-3731-a9de-cc5f125af590 | -7.0176 | -44.5266 | 2025-10-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6eb80ee4-c44f-3de5-a82f-83df87f03717 | -6.679 | -42.8136 | 2025-10-02 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 0230f50c-a871-37d2-9687-894795a05518 | -8.2105 | -47.0084 | 2025-10-02 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c1a023eb-7f5c-3688-a1ae-65a0d5dce557 | -7.8185 | -46.8005 | 2025-10-02 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b69ec5f7-ac23-3ef9-862b-ecdca238b704 | -9.9383 | -43.6483 | 2025-10-02 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e3d01069-acbc-3303-8f5d-05aa7fcb605b | -13.7873 | -51.2189 | 2025-10-02 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 31c155d1-0b9c-3ff6-82a6-d319a21f5909 | -9.4371 | -45.4656 | 2025-10-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| e95ad418-d608-3d05-9717-3c77578e041a | -9.4086 | -47.5521 | 2025-10-02 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| ff0b9ed6-ac13-339e-a1f8-adfe64e915b3 | -6.2408 | -45.3424 | 2025-10-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b987cbfc-5e56-3e0a-9d9a-a8a7df67ced5 | -13.3089 | -47.8118 | 2025-10-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 5b5888bf-07c0-3a97-b726-45e88fd0f8e4 | -11.1175 | -49.806 | 2025-10-02 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 77dce9c8-f026-3aad-8da5-bc6e2ebcfe0a | -8.5201 | -47.8386 | 2025-10-02 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 83fc8a1d-04b0-317e-b2ad-88b8b26656f1 | -6.0235 | -44.5632 | 2025-10-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 24e6a0d9-649d-3de9-9146-83e3cbd61270 | -15.3185 | -46.278 | 2025-10-02 14:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 7b6d8ab7-bd5d-3943-8a0c-a26fe52a0103 | -8.2094 | -45.5301 | 2025-10-02 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e5a09f66-199f-3d78-9c51-210fd3b049ab | -12.7627 | -50.5567 | 2025-10-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 9fdf429b-3215-38d7-8a9c-8dc28453ce72 | -6.8004 | -45.5687 | 2025-10-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |


