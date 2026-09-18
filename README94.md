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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5a34c04-43b8-3f4d-b09f-b00205d29e61 | -10.6755 | -50.262 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c0684424-bd22-3fd0-8b83-3d9ba8d58234 | -11.3437 | -44.0141 | 2026-09-18 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8f628f9b-3659-332d-abfa-52866c6fd752 | -4.5587 | -42.9523 | 2026-09-18 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 02a7a640-e274-38d3-8adc-2653c23b4193 | -7.5494 | -45.6839 | 2026-09-18 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6faf700f-3cc9-3034-a8ba-497614fe7ec7 | -10.5178 | -46.7366 | 2026-09-18 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 06714781-19ec-3a7f-8fac-94a60a1023e3 | -10.8087 | -50.205 | 2026-09-18 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 54657773-d882-319e-b0d6-a149e325dbfe | -8.4675 | -44.4984 | 2026-09-18 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3b6d0a27-898f-3815-aa1c-9996d4865251 | -4.5961 | -42.95 | 2026-09-18 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| fce83550-593a-3cf4-8c25-1999b8129136 | -9.8316 | -48.3854 | 2026-09-18 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| eeaae968-e499-3b28-a74c-6295af4817e8 | -12.5497 | -50.7332 | 2026-09-18 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 8439935f-58b4-33e5-a22f-c300a4dc1c74 | -11.8115 | -46.8158 | 2026-09-18 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c73d8858-e15c-32be-bdd2-c4d2c556d510 | -11.8556 | -50.0006 | 2026-09-18 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ee79b7d7-786a-3438-93ad-b4eadd726536 | -12.5688 | -50.7308 | 2026-09-18 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 377.5 |
| 6ee34fab-e101-31c2-9dd7-cacdc6ac68c6 | -13.6341 | -46.9304 | 2026-09-18 12:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 130fc079-2b3f-3429-bc2f-252a6a3bf2cd | -10.3307 | -45.3112 | 2026-09-18 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2eac15f7-8816-38fc-8924-53d6c6458e42 | -13.4303 | -51.9036 | 2026-09-18 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 354a636f-2a08-326f-b7a0-2cb693b04b56 | -7.0164 | -44.6413 | 2026-09-18 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 82c94a7c-fac5-3059-867a-5311eb439a7d | -7.3546 | -44.6334 | 2026-09-18 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 242457ee-46f5-3cb1-a270-b6e29a26dc56 | -11.083 | -48.2875 | 2026-09-18 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ace86233-43d2-354d-a6b3-ff526ed66f5e | -7.6577 | -46.0788 | 2026-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b03fa045-16d7-30ec-a8b2-e3f19ec1d890 | -12.998 | -46.9381 | 2026-09-18 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ec8a40ec-1413-3cbf-a7e2-0619ef2bfccc | -10.6755 | -50.262 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 837d9aaa-cb41-3c09-b276-669982c67934 | -10.6758 | -50.2406 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 6f2a65f9-86e1-3a1c-90c9-1861018757ef | -8.4672 | -44.5214 | 2026-09-18 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| cc92fcd8-7e45-3257-b471-e68369315088 | -10.5966 | -46.5474 | 2026-09-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 362a31c5-7706-3ff5-9907-f1b59db1a5bd | -9.9505 | -45.336 | 2026-09-18 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 52353f87-8abb-357a-9729-63bcc1259710 | -4.5587 | -42.9523 | 2026-09-18 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 85e9be5a-8a10-302b-b22b-9291e403a9f5 | -10.3769 | -49.9723 | 2026-09-18 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4fa24775-31ea-332a-989c-e2a197d0e67d | -11.0643 | -48.2678 | 2026-09-18 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2ba9cc30-f3a5-33a7-8077-b2c21c4c14b4 | -7.6394 | -44.3995 | 2026-09-18 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9c96de45-58e3-3de7-b4b8-8a69779bf933 | -7.5494 | -45.6839 | 2026-09-18 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7b87f007-e314-3ee6-85e0-66bd4c1a9a1f | -9.8316 | -48.3854 | 2026-09-18 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 046d81be-bda0-3075-a0db-de395dc7e11e | -8.6817 | -45.4359 | 2026-09-18 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b8b64e89-1645-3d70-8748-4bf207bd002d | -11.8115 | -46.8158 | 2026-09-18 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 16d197fe-7497-3a6e-b0ea-29a7362c8a70 | -10.6944 | -50.26 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5f3fdc92-aab5-33e6-9929-c9398361ca31 | -10.5178 | -46.7366 | 2026-09-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 32f7b081-73e5-3345-886f-38a9f97c5b64 | -14.1737 | -45.1641 | 2026-09-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b7585216-a67c-3e53-8a68-84669f492c9d | -14.7497 | -50.2865 | 2026-09-18 12:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| fb39ef18-b306-3140-a30d-f4a946805f66 | -7.0352 | -44.6396 | 2026-09-18 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 960ad9ae-0311-33b6-b965-f1b4cac115e7 | -19.5539 | -47.6346 | 2026-09-18 12:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 0c9e0349-deed-3ca9-82f0-f303392181cc | -10.6536 | -50.4778 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d9edbc05-4dfe-3ee1-89af-3f1f528f38cf | -11.875 | -47.5902 | 2026-09-18 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7e70eb01-1a1d-336b-9f26-0089b270524c | -11.3437 | -44.0141 | 2026-09-18 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d5c90a3b-b757-3e47-ac4c-0f99751af06e | -19.5545 | -47.6113 | 2026-09-18 12:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1a5bf49d-2dee-398c-ab55-3bc53768f4e2 | -11.8753 | -47.5679 | 2026-09-18 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b3b38ea4-1384-3b46-bb3a-598810dcc4e7 | -10.6533 | -50.4991 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ec6fd4a3-03a6-3457-9f81-879f67ae61de | -11.2975 | -43.3851 | 2026-09-18 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f6d4db36-4864-3f92-b6d0-34e7a919ee6e | -9.8505 | -48.3834 | 2026-09-18 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 0bca59c4-4f22-331e-992a-e8b2af3699e7 | -8.4675 | -44.4984 | 2026-09-18 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 5a4a48a1-9892-3d68-9e8f-0284996fd81d | -10.6726 | -50.4758 | 2026-09-18 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 199.3 |
| d8f9caa8-1da5-30e1-a632-9969a03bdf28 | -7.6574 | -46.1013 | 2026-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| cff9beae-722b-3e5a-9efa-0747ee4c560a | -14.7303 | -50.2894 | 2026-09-18 12:50:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 48bbeeac-9016-3b76-bb59-701cb8bed7dd | -11.064 | -48.2898 | 2026-09-18 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 32c00ca3-a9fc-338d-acd6-db1cf8977ec1 | -14.1732 | -45.1875 | 2026-09-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bc0cea2e-633e-3ad2-b65f-6b01145b4251 | -11.875 | -47.5902 | 2026-09-18 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 96586f39-936a-368b-b3fe-0e640b1c4362 | -13.6531 | -45.97 | 2026-09-18 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4d8355d4-8d29-3b5f-bfb7-68f14f85a497 | -8.452 | -45.7092 | 2026-09-18 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 894c26c9-3a84-37ae-9ce5-d0bf804c7990 | -19.5539 | -47.6346 | 2026-09-18 13:00:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 9c075453-5d1e-3e3a-89c6-842185150a8a | -8.9138 | -45.0232 | 2026-09-18 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 0cb55a0d-bdc1-34b5-b8d1-6a5c8fb4b13f | -11.9118 | -50.0585 | 2026-09-18 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3988a7f4-6343-3803-a353-2de88673cc51 | -4.5774 | -42.9512 | 2026-09-18 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 3366af42-c0c2-3fc2-8161-7c90512a0e58 | -10.8276 | -50.203 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 2f698097-6c69-3aab-8544-267ba976bf17 | -13.4303 | -51.9036 | 2026-09-18 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 2dc1ff9a-87fb-380c-aa22-215ae721bedd | -11.0636 | -48.3118 | 2026-09-18 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5fb2a17d-8b0e-312e-bcf7-802975a169c5 | -9.9502 | -45.3589 | 2026-09-18 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 59bda0d5-dd40-3adb-821c-f6e0145300f8 | -10.6376 | -50.266 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6742953b-b55b-3248-a2fe-6991f65a5d54 | -10.6723 | -50.4972 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 56e0e6b2-c812-38fb-acaa-b5d30d30a199 | -11.3809 | -44.0788 | 2026-09-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 67aa0768-e905-3402-b770-735bd10e2a7b | -14.7497 | -50.2865 | 2026-09-18 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 810f1268-88b4-31b4-bd74-afa89d72265d | -11.8115 | -46.8158 | 2026-09-18 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| de551bfd-c920-33a7-af09-d312685db471 | -10.809 | -50.1836 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |
| a4f739c2-6851-31f9-9c53-e82fc9cfd464 | -11.064 | -48.2898 | 2026-09-18 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2161d79f-6782-37bd-b340-9435cd8a4dbe | -10.6755 | -50.262 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d4b28867-2f07-3045-88a4-2594087df2a1 | -13.6341 | -46.9304 | 2026-09-18 13:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e15eb71b-52bd-3af3-8588-ff24a7588160 | -13.2485 | -46.9226 | 2026-09-18 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 47315d37-4dcb-3fe0-8d73-9a0a4c9432e8 | -14.7307 | -50.2676 | 2026-09-18 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| da833cda-16f1-309f-8ddc-77160bdc1d8f | -9.8316 | -48.3854 | 2026-09-18 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0089196a-1b12-3069-914b-f378d69395ef | -11.2975 | -43.3851 | 2026-09-18 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| c0455b16-3248-362b-a202-8930f6801b63 | -10.3769 | -49.9723 | 2026-09-18 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6f7ac436-94b6-396c-9fc2-ed6a92b28dce | -13.6148 | -46.9334 | 2026-09-18 13:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 779d4b30-92c9-33ef-877f-168a97c307fb | -8.4675 | -44.4984 | 2026-09-18 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 904d6ca8-6374-351a-bd1b-d112514c10ce | -10.6187 | -50.268 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 4e55cfa0-7f7c-38fd-a243-1dacb75be376 | -9.8505 | -48.3834 | 2026-09-18 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 245065e1-d130-3bb4-92e3-4d0a18e36682 | -8.4503 | -45.8448 | 2026-09-18 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ad08b722-dfed-31a3-b910-860bb778273a | -7.6577 | -46.0788 | 2026-09-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 0a23eac7-9fbb-3b47-8d2d-94544fe67515 | -8.4672 | -44.5214 | 2026-09-18 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ff7b0615-e3db-3bf8-b6a5-3f934fa88fba | -11.2971 | -43.4088 | 2026-09-18 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 43168128-3e8d-3f7c-93c7-c9c53bc0a85c | -10.6758 | -50.2406 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b7e3050c-4635-3b93-a4f2-ad77fc7b3c2e | -8.6817 | -45.4359 | 2026-09-18 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| b147fba9-e565-38c6-979e-dbe3c688dc3a | -11.0643 | -48.2678 | 2026-09-18 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 9b0e3a93-1e53-3310-bf6b-42f2b603aba5 | -12.998 | -46.9381 | 2026-09-18 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7e7526c9-748c-38b5-bb6c-c0dfd79329ff | -14.1732 | -45.1875 | 2026-09-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fbe093c0-d046-3e05-b442-ef7cd01ba79f | -10.5178 | -46.7366 | 2026-09-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.0 |
| f39d1db8-0fc8-3b0e-a316-f70777d5d809 | -7.6394 | -44.3995 | 2026-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 909540c6-f551-3e07-9cbf-d51fdd8db09c | -7.0352 | -44.6396 | 2026-09-18 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| a95b0b90-bda5-3b66-a2cd-39d0c31cfc50 | -11.3442 | -43.9906 | 2026-09-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 2bd74e62-ba29-3d58-a649-6b3ef27c6918 | -11.083 | -48.2875 | 2026-09-18 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3cb8e4ca-fdd6-3085-88dc-cab35d59632a | -10.8087 | -50.205 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 435.1 |
| 91267982-5556-39bc-836a-984f4b2e3c47 | -10.8279 | -50.1815 | 2026-09-18 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 328.0 |
| 91098875-abc7-3efe-80d3-76a0cfadae44 | -14.1737 | -45.1641 | 2026-09-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |


[Clique aqui para ver as próximas entradas](README95.md)
