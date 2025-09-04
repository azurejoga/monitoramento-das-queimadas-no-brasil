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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a9a6e35-a240-34ce-aadc-cdf1a5adeee0 | -4.9951 | -56.256 | 2025-09-04 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 118e4d99-4039-30a2-83fd-fb457f3e4d49 | -12.5173 | -48.0584 | 2025-09-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e3c97b1f-df38-36f6-bede-4606baa6d953 | -8.0796 | -45.3617 | 2025-09-04 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 70e4098d-1e46-3947-92ee-f6f64d312432 | -11.6338 | -52.193 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 49de9956-3dc3-35de-a1d3-1b5e40c3a1a9 | -6.2773 | -43.5046 | 2025-09-04 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 6cc658b7-9fa5-30c4-aca5-58060e584c87 | -13.8457 | -47.9764 | 2025-09-04 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b9e096f7-699d-334c-ad82-d404e16800fa | -11.6601 | -54.5093 | 2025-09-04 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 112a43b5-68c4-343e-aa51-c07c6c0ea4c6 | -11.5969 | -52.113 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8d6f9de9-ea3b-32ef-8d77-e479070170f7 | -6.1665 | -43.3273 | 2025-09-04 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 81fd662a-2a15-3c3c-af7d-3d0ac3304c37 | -11.5782 | -52.094 | 2025-09-04 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 8eb53fe2-9a4f-3ec3-aa2a-cddc9fe1dfe8 | -6.2318 | -42.4278 | 2025-09-04 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 162.0 |
| a1f00dee-1b70-31a1-8ff5-bf24b23dbdee | -8.9034 | -45.7973 | 2025-09-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7c71d741-9494-36d5-96b8-10d2f520e7e7 | -14.5602 | -48.0654 | 2025-09-04 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c5194f10-5465-3f55-8a63-693c36d9d0b8 | -12.2344 | -50.1488 | 2025-09-04 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1d752684-2754-3d23-9912-1ca251f2b1be | -6.2249 | -45.0491 | 2025-09-04 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 58a0cb2d-f63a-30fd-80d5-044ea11fdc34 | -12.4593 | -48.0885 | 2025-09-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 70605aac-4f60-39e0-8678-0df7d5ee4165 | -13.8457 | -47.9764 | 2025-09-04 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 456f6a37-1f48-371b-877a-dacde8da0f1c | -5.9441 | -51.9796 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| a3486312-e54b-35d5-b50f-44e00dadacfc | -6.8754 | -45.5625 | 2025-09-04 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b18f8da5-28a1-3aa4-8a29-162ad1a402c0 | -8.9028 | -45.8426 | 2025-09-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 4b2b49bb-8366-3005-a075-047a2a11e92c | -7.7252 | -50.3174 | 2025-09-04 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5c1cf843-3521-30c2-82a8-83812017a805 | -14.5852 | -53.0268 | 2025-09-04 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b9ea3835-0a73-3ae2-b08a-34ddd5216b70 | -5.908 | -57.7311 | 2025-09-04 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 329d297f-1491-36af-a2b8-ba851a6616d4 | -11.5779 | -52.115 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 33f4aa63-d9d2-30cc-90ed-e86646efcaa7 | -13.8651 | -47.9734 | 2025-09-04 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 175d6063-59d6-3de5-b992-d5ba3395bea2 | -8.3829 | -48.3317 | 2025-09-04 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6a320d63-e5b9-35eb-b977-c55d53873e6a | -7.7409 | -48.7772 | 2025-09-04 13:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 113.1 |
| c7875bf8-1275-33c8-a97a-85ef813c5a9d | -8.8842 | -45.822 | 2025-09-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f0fcba15-3341-3529-bcd1-c75728246b19 | -10.1457 | -46.2424 | 2025-09-04 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 23391bed-86bd-3a3f-a038-dc5c55d22f3e | -11.0062 | -45.9072 | 2025-09-04 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ddd07a32-c81a-3051-8e1d-27f51093fad4 | -8.0417 | -45.3882 | 2025-09-04 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8241bc83-d149-3737-b14f-66754fcc1f40 | -5.7002 | -45.156 | 2025-09-04 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 056a4f2c-bf37-331c-948f-6d5cc845e909 | -6.0232 | -46.6784 | 2025-09-04 13:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 18b9ce51-27b0-33c3-8b5a-ebee7fd298d6 | -4.9049 | -41.7696 | 2025-09-04 13:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 272daac0-9cd7-31a4-8aa4-abac8ac09835 | -11.7385 | -47.7637 | 2025-09-04 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4e26b35e-97e1-3019-a3bb-2569da539b84 | -11.5972 | -52.092 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 7efab85b-aa05-34aa-93e4-a6b455b518dc | -6.2127 | -42.4532 | 2025-09-04 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| c7cec9d3-a721-37fc-aa95-e5ceb6752b78 | -7.2901 | -43.6929 | 2025-09-04 13:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dd410631-bbc5-34b8-9b51-31772203c61a | -5.7341 | -45.56 | 2025-09-04 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b75557a0-c3d6-3935-bde9-57d590128e87 | -5.753 | -45.5362 | 2025-09-04 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 83ed93e1-f4c7-3e73-a47d-65fffad16850 | -12.5173 | -48.0584 | 2025-09-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 6c148ad0-4240-3c11-b57d-fa4aec03c603 | -11.5782 | -52.094 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 190.4 |
| d709fea0-548a-3b2a-9bd4-ab20ca9e3598 | -5.6777 | -45.6089 | 2025-09-04 13:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 85ec6ffc-8f99-3b8f-91d1-bf2ac88f7e5b | -10.9867 | -45.9325 | 2025-09-04 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f5a308e7-9f27-351c-985c-d13ae39fb880 | -8.3644 | -48.3116 | 2025-09-04 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 815a1b1e-30c4-3ab4-9694-5d528c654aa8 | -8.0796 | -45.3617 | 2025-09-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 955ebe17-0a73-3dc8-b806-7a22eff504a1 | -11.6338 | -52.193 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 9c611459-a2db-3c47-9ee9-bbd2e83c0378 | -5.6963 | -45.6076 | 2025-09-04 13:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 74c16d8c-3c41-34d6-86d4-d1848d5f9adc | -6.7992 | -45.6815 | 2025-09-04 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5b61fdeb-2836-3ddb-a467-cea7f75025f0 | -7.9344 | -44.9207 | 2025-09-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 93cc241f-1d58-3eb4-8483-430352b52673 | -5.7528 | -45.5587 | 2025-09-04 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 14ed5597-a434-3ad5-98c0-f30711bc6faf | -8.3641 | -48.3334 | 2025-09-04 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 49639443-d544-3fc5-8cb1-d463b207505b | -15.408 | -55.9416 | 2025-09-04 13:40:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f033e08b-38ea-365f-8e16-c18f5a09713e | -11.6599 | -54.5297 | 2025-09-04 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d520fc2b-9469-32ba-9d3a-5b3e34b3a375 | -11.6525 | -52.212 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 5c49b843-0fce-306a-9daa-56af4ced4549 | -6.2205 | -43.5558 | 2025-09-04 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 4edb5558-42c1-3edd-a823-a02c9e28defc | -12.5233 | -53.8071 | 2025-09-04 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 26f4d802-311a-38f5-8550-0d4bd1e9ea18 | -4.9951 | -56.256 | 2025-09-04 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 060e349b-555c-30c4-a3a6-1aade5813b0e | -6.1665 | -43.3273 | 2025-09-04 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 18234cdf-507e-32b9-910a-e004e21b2f9c | -6.2038 | -43.3475 | 2025-09-04 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b4a24ce0-ae8f-3590-be11-1b31c7a05d39 | -5.9257 | -51.9599 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 41fe5390-c613-3bf7-aaa4-5976c4e3353d | -12.4981 | -48.061 | 2025-09-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7a16bdd9-954b-3680-9f5f-869a963b80d5 | -8.0799 | -45.339 | 2025-09-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 177.8 |
| ebda5da6-c848-3fba-93ae-011001c7ed4b | -7.9341 | -44.9436 | 2025-09-04 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 19acf1be-43d4-3ebc-ada5-6a029d1ee42b | -6.2315 | -42.4515 | 2025-09-04 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 225.8 |
| d926aae6-d105-35f7-8dde-311f1529b96d | -11.6409 | -54.5315 | 2025-09-04 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 31320514-b717-30aa-9d94-67edcc9ff202 | -7.2898 | -43.7162 | 2025-09-04 13:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| b8bed8ef-0d09-33c7-a762-772fd9735331 | -5.7 | -45.1786 | 2025-09-04 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 3319904a-c54f-3550-883e-ebd5559e1fd7 | -11.6601 | -54.5093 | 2025-09-04 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 8f81e6b6-392c-31bd-a70a-96d522f9a6ec | -6.2952 | -43.5961 | 2025-09-04 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c8f3f87e-bb55-3956-9ccb-82d633987f27 | -8.9031 | -45.82 | 2025-09-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 286.4 |
| 76cd11e7-c050-3bc4-9af6-880f93d789b9 | -17.0652 | -46.449 | 2025-09-04 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 9483e473-bc50-3060-a635-0bb3fa60e77b | -15.229 | -52.7101 | 2025-09-04 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e6ad8778-8b56-3b49-8045-9b5157c8ad03 | -6.2062 | -45.0506 | 2025-09-04 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6ce32823-9cf1-347a-93c9-972b91b3a954 | -8.9025 | -45.8652 | 2025-09-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 88917673-3c4b-3d8e-92dc-654687cb9185 | -5.8525 | -57.7722 | 2025-09-04 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 816b91c4-1425-385c-8e19-8eb0cd72a0a1 | -5.8206 | -46.3595 | 2025-09-04 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 981f0da9-eb22-3a7c-aadc-b45cfc89ff66 | -10.4658 | -50.3907 | 2025-09-04 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| c7ff27af-8e6f-34ab-9192-050b22fc1c9f | -11.5969 | -52.113 | 2025-09-04 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 5da3fc49-f0b6-3834-b429-a49e4c92f2e1 | -12.4785 | -48.0859 | 2025-09-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6a260ebb-3f88-3692-a35a-faceaeef8799 | -6.2251 | -45.0264 | 2025-09-04 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| a924638b-7194-3cd1-861f-d417b19ccc9e | -13.8457 | -47.9764 | 2025-09-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2c770fda-42d7-3021-904f-0666a93740e5 | -11.6338 | -52.193 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b9330fb5-213b-3694-bcbc-efab905251fd | -6.2315 | -42.4515 | 2025-09-04 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 287.8 |
| 8be82078-e34a-303f-b994-df71272ca430 | -6.0421 | -46.6549 | 2025-09-04 13:50:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3922fd15-e051-3bc1-9d55-8d38a2c7b438 | -5.908 | -57.7311 | 2025-09-04 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 1ccb69f9-688f-3db7-8ce9-5ca6e965463b | -7.2898 | -43.7162 | 2025-09-04 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| fc39f744-a2b6-3e88-b2c0-6acec668dd6a | -5.6965 | -45.5851 | 2025-09-04 13:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 595a3c89-9803-3429-bff3-61a55fa6a329 | -13.8651 | -47.9734 | 2025-09-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| f2b6cdfd-df5b-3bbf-a229-fccf88c10490 | -12.5173 | -48.0584 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 63e244f4-35d4-3f70-b437-ed7071f664ff | -8.3829 | -48.3317 | 2025-09-04 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| cb8c4d47-b467-3388-a7df-762d00d78d2c | -5.7738 | -45.2865 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3d6a5a85-f1ba-3a56-9281-8849b2a1358e | -8.3644 | -48.3116 | 2025-09-04 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| cc7a89b7-4193-3d42-a3ae-758ada7f6405 | -7.7409 | -48.7772 | 2025-09-04 13:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 104.3 |
| aacdb03a-20a7-3a30-98a8-1b9335863dd6 | -5.6963 | -45.6076 | 2025-09-04 13:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 493a49bd-0304-39cc-afb0-38c1ba1d9be9 | -10.1267 | -46.2447 | 2025-09-04 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5e14fa9c-9d12-3e9f-9dbd-72e5549fee7b | -7.9341 | -44.9436 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a65ad016-0d6a-3a0d-a2fd-23b867467745 | -10.4658 | -50.3907 | 2025-09-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 2c14ba38-a9e3-38d5-bbbe-1d552fd733bc | -12.4981 | -48.061 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7bbbe0aa-2dc0-36a0-a2fa-e67a52740a5f | -5.7002 | -45.156 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |


[Clique aqui para ver as próximas entradas](README107.md)
