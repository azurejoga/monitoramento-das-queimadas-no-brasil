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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f58fd4e6-86b5-3d31-b749-2c7a21256e71 | -6.31329 | -57.75125 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc4f2225-638a-3216-81b0-c0693878b4fd | -1.27143 | -57.03522 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc9ce9c-81d1-3b7c-a776-75b4cbf51b81 | -5.77331 | -45.1052 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 03882d0b-5176-35b6-8a4c-f08b337c2346 | -4.11097 | -51.0773 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f14a3858-54fb-35ae-9c95-9af29becbfa1 | -5.83738 | -53.84758 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa6d2c9-6572-3fd2-9f4c-534b209cd715 | -1.1607 | -54.20363 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fe89460-9b5e-3d1a-a7bd-aec4e097bdbc | -1.62665 | -54.92174 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 472bfab7-a6bc-3304-b83f-c388ea378310 | -1.22064 | -54.55694 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f147a29-24c1-3e00-9a19-4b4a1757f215 | -6.61148 | -59.92445 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 271d55ae-c352-38f8-9991-d386ec1ee840 | -9.25875 | -46.24303 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1669471a-4f56-3d44-bb50-4665da85ee63 | -8.46038 | -48.69212 | 2026-09-24 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1302f67d-3a23-3449-84b3-a9c4b056d817 | -9.25408 | -47.34709 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 78da6ea9-1497-3247-9164-d56cab0599b5 | -4.53781 | -54.96943 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0d84fd2-9d42-3233-946d-bc75c359b996 | -8.23407 | -54.67225 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92f973cd-d8e4-308f-84cc-0aef369a8d63 | -6.28661 | -56.04004 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50b9d5d9-d26b-3253-9c2e-c5d6fa015a8d | -5.21557 | -60.05399 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c3d9a2a-1da3-3c09-bbfd-d5b8c72a7a85 | -5.10985 | -60.26326 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d276455f-3d5d-3c6b-bfd7-6813a8cee754 | -3.68882 | -60.56365 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3901e2fd-5868-3742-a952-3c0df5f7f6c6 | -4.28439 | -48.6118 | 2026-09-24 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac2608f7-b859-38f9-ac6f-57aa5f755f88 | -4.52784 | -54.97182 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59209576-9dcf-339e-9794-f095309d41cd | -6.7216 | -44.15481 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| befe81ab-412c-3a6f-bac6-736757848294 | -4.54059 | -54.97347 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d0936a0-9e52-33dc-ac46-78ac6ec29186 | -5.29873 | -56.09993 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 397d2102-75a0-3767-b126-30591268161f | -9.5334 | -45.36595 | 2026-09-24 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f4df229-cd21-3cff-b31d-4fd7732b3be0 | -6.88178 | -59.85877 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db6003ff-4142-392f-b376-492cd022a2a1 | -9.23998 | -47.3774 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 825b3609-e079-3e47-9b89-71ffa91b5f76 | -1.62607 | -54.92537 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9add64c-1d04-3d58-80ea-aaea57f8f91c | -4.55573 | -54.90041 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12b9a05e-ed1d-312d-8adc-a127913c902c | -3.06193 | -49.57109 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4139632d-87a5-38e0-a51a-27b2eacba07c | -6.53278 | -51.50463 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9fab8fa8-318f-3b07-8092-7586dd0ba587 | -3.49232 | -59.19709 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97c1064e-ab06-3cca-a0e4-6985e2023a42 | -8.25126 | -54.77818 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4fa3b90-e2f6-3ab1-96bc-c29cf89004c2 | -6.6727 | -58.55611 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7257e43e-8621-328f-83fb-880ae7558edd | -3.9138 | -59.66678 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 663a181d-c484-3efd-93bc-dae3b5316c61 | -6.40173 | -46.2018 | 2026-09-24 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d695707-b5b3-364c-867f-725848caba75 | -2.89994 | -54.09686 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8f7e9a59-af78-364f-b2c7-a2a1cd963ad6 | -2.81736 | -51.33804 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acac522f-cd36-3c39-98f9-c0368a77c99e | -6.08672 | -57.62568 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 62c8e0fe-84c4-3fb8-8561-336d8ecc8e48 | -9.23588 | -47.37164 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6835bfef-473d-3cff-b34b-722298f5fbb0 | -6.92465 | -62.90601 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f54bb5c6-1ec9-3c53-962a-161667fa92a2 | -7.44062 | -49.83188 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76719b7a-5b73-370f-962c-719a20b37535 | -8.20931 | -54.72166 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47650512-0b12-3df4-a763-fdfb9e218527 | -5.10621 | -60.25837 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7bbd9ce5-90fa-309e-833a-d92892b25312 | -4.98446 | -45.55021 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9284f54e-a1ef-37fe-98fe-00971e19cff5 | -5.95329 | -51.7956 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd01095a-bc10-3451-8920-a3e15231222b | -9.26261 | -46.25362 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d5c3b97-aa51-3c00-833d-a6d8038a0e35 | -3.71974 | -49.04986 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 890c3e5e-e3b3-394e-a2d5-0ffeebe4ce99 | -8.1233 | -54.81469 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6918e2b-8029-385b-9f40-e2ecb6a13d91 | -1.98748 | -56.54113 | 2026-09-24 05:04:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1b81c9d-4851-3b52-881f-b0837c4ecd09 | -3.21388 | -53.40195 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1cd25fd-8d09-3586-a76c-921102368327 | -3.74706 | -59.28789 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2462485a-b9d2-3491-bc8a-efc1a8f1d853 | -9.2639 | -46.24417 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8f549332-0122-3a6e-b185-f0a6da466c64 | -4.11742 | -51.08252 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3f0a807f-4395-3717-8bb0-e1c72c05e613 | -8.12551 | -54.82215 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b40c74a3-5db3-3344-8b35-c0668ecbcc3c | -4.89095 | -55.97514 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d365da-59af-3672-8015-4ee0ff1115f9 | -5.81626 | -57.74129 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07257b30-c3e9-3fad-9ad7-e9019973a2de | -6.15972 | -57.72745 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56013c5e-c75c-3353-a9e1-762bb43b23f8 | -7.47674 | -44.57534 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff621648-096c-385d-8db2-230fafbc63c7 | -3.45139 | -50.07472 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8575aac0-70aa-3566-ac10-ffb95e31b28e | -2.94962 | -52.14562 | 2026-09-24 05:04:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eee7fab-1465-36fe-a292-b8170338025d | -8.46069 | -51.48139 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81865286-b572-3cbe-9322-528848e4bbc6 | -3.00005 | -54.17321 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92da6cf1-f070-34ce-9092-18291eff9431 | -6.35618 | -58.29008 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb20bd00-3893-3772-bb1d-e3770609f08a | -6.64554 | -50.93402 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5de45db-efb9-3570-a820-fc0c9547de56 | -3.16974 | -60.6591 | 2026-09-24 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de8b1c3-1688-32f1-81c6-41d60ef48985 | -6.00085 | -57.69104 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7d074a7-0a69-3b24-9e3d-912535c7fb94 | -6.24064 | -60.04042 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea521543-abcf-3fe0-a0c1-57ac956e8d9e | -4.89753 | -56.23625 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3175ac4-7fd1-3175-902e-cd9f301433ce | -4.17805 | -53.66399 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e16bbb3-3fe5-36e4-9bf0-b57aa50a8c42 | -6.15963 | -57.70554 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32ba6869-5866-342f-a3ba-5ba750c5b561 | -7.55686 | -55.02258 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6a88506-5019-3fa8-b616-5526225aa7bf | -9.02259 | -49.81019 | 2026-09-24 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 860102e0-d651-3f90-b3d4-f11917466a3c | -2.82434 | -46.70433 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75daabe4-da08-35df-bb1b-886fedb9c15c | -7.5541 | -55.01859 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 485d4a95-741d-388c-9cbb-4f4b044a073a | -3.58667 | -59.07474 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3c08af3-3b9f-379e-be95-289abe9684bf | -6.14009 | -53.14901 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cb79b08-13d2-3feb-8716-a36451dd0ec5 | -1.92517 | -58.26231 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ea7399-1015-331e-9c45-8a40542440b7 | -6.46085 | -54.9931 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8fd7478-cf44-3ec7-99c1-3bde2043cd17 | -3.6767 | -60.58056 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bebd5da6-6c0c-3db5-bee6-69c64f1ddc58 | -6.60796 | -43.73588 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6d95269-f47a-3e4f-a985-b0423343670e | -3.4493 | -50.08796 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1a1a50b-d1ab-34ca-b896-680233ec40f5 | -3.45601 | -50.08254 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df58540e-aff9-3e65-b1a2-9b726ed4d536 | -2.78083 | -51.36731 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a48a0fb-2fbc-36a9-87dd-d209fbc59f85 | -6.65181 | -55.07385 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bbc33bb-d448-3799-8a47-f1182b89e46d | -7.19839 | -47.458 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9272ce3-d472-3a92-900b-3c42102a2761 | -4.02707 | -59.85011 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f61bd867-c7e4-333e-9334-c191567db323 | -5.8425 | -57.62828 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36b2f8d3-7982-31eb-a193-ac8dd37711c9 | -6.10261 | -57.71081 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15c4d691-16be-3a8b-a769-0a6229015abe | -3.71201 | -54.20388 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dec9ef0d-252b-3184-b39a-acd311c92ce0 | -3.4544 | -50.07972 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 21cfc6bf-975c-3d55-895a-f7f432dadb49 | -5.81357 | -57.73784 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea1f3ca5-43e8-360e-ad07-604432a99c71 | -5.59309 | -60.2047 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1adac75-fa13-3599-8fb9-eb05efc2df34 | -3.44556 | -50.07641 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 478f9da4-d0a7-3e48-abc4-0c0f5e3a2162 | -7.0485 | -62.93392 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3eb0a65-ff00-364f-bb47-ad5db34a89c5 | -10.08007 | -46.00739 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8785eced-0af3-3dff-b00b-fec4ae9b2a1d | -8.91889 | -50.8875 | 2026-09-24 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ff6c33-99ba-3795-8132-758f067285d5 | -3.7092 | -60.55304 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0ac5bfe-7cff-314d-ba95-e940584f8bde | -3.68277 | -60.57206 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc06e21c-b78e-33d3-bbc9-52a29fbf7ade | -3.90072 | -60.59031 | 2026-09-24 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c298086e-9958-3c1b-9b72-c3dad76d60d7 | -2.73876 | -51.54535 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README69.md)
