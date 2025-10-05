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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be887064-194b-39ef-a9a4-d64f2d4fddf2 | -8.59811 | -46.28445 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b8d5de9-8ab2-31b8-9d42-36a38ad37b1d | -11.11516 | -49.86221 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17794449-f6bf-3944-be69-30591847f5b4 | -8.55033 | -47.66758 | 2025-10-05 05:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5bbd6f-f84e-3a78-a194-48115cb470fa | -11.11628 | -49.86235 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab66fd2-7c78-33c6-9393-f3687771bbed | -9.33167 | -54.51725 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f92bf3d9-35b0-308e-bbc0-9e53e1520d87 | -9.33102 | -54.52168 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abb008df-d414-3b3f-99fe-3e9569db0a91 | -6.16936 | -44.58781 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0ff4093-6d8b-3178-8cdb-f17d029b7f20 | -11.83399 | -45.08336 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb051605-4ad7-33c6-88a3-3715a51abecf | -8.65238 | -54.95955 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96e0e049-2f28-3561-b255-ea965666956c | -7.62884 | -45.48561 | 2025-10-05 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a56b3b5-7fd0-3e7f-aa8d-a66367c3aadb | -5.51955 | -44.21399 | 2025-10-05 05:14:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7a65d86-c0e8-3320-95dd-65e9cba92372 | -6.14316 | -44.57762 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2536c6e-8f1a-31c8-8f83-61f748d403b6 | -8.669 | -64.10519 | 2025-10-05 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 888ece82-8d79-3a09-9f82-83d39808aa63 | -10.46377 | -57.49319 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ffb6026-6e76-3ce2-afdf-942fd126eee6 | -8.42649 | -70.13256 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32e26a1c-f5a5-3e53-a857-fa953e04c0bf | -11.1159 | -49.86545 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9e401b7-9d98-3379-b71c-822b577ef6e0 | -11.5346 | -47.6773 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97bc9f9f-8074-3498-a71f-5e71c76a8f5b | -11.82672 | -45.08457 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0dc2dd84-4089-34d2-9dba-5b69060acbf5 | -4.68477 | -46.82393 | 2025-10-05 05:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dd64c08-adcb-333c-96c3-75c0de2e49c7 | -8.58108 | -46.31687 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c1cc0fef-8987-3d5a-b240-e75812719e54 | -9.29761 | -45.96586 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ad801a9-47fa-32c0-8667-5e66e5797e15 | -9.32491 | -54.5117 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f83fa25-1e51-3d87-8a70-f8ec62dcac55 | -10.21684 | -54.12316 | 2025-10-05 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d90eccd1-1828-3ebc-8676-3798ca68f0e3 | -8.60117 | -46.28097 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3ac2db09-fcbf-3c50-8158-dd328ce6a573 | -11.76139 | -44.7503 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42e2d881-e040-3a7e-a02d-8b1249493547 | -8.54214 | -46.32151 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aa2bcfb-d4c0-3a10-b13d-049a4f84bf67 | -9.29846 | -46.01264 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d87cf92-a157-3f0d-a674-285d4cd06efe | -8.6188 | -54.96291 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd96d13c-b99d-3eb5-bccd-6ffe4bceed9a | -9.9136 | -50.19004 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9237101b-5ffa-3b78-ad96-0b2049699dd8 | -5.00165 | -47.2163 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f5e51ae-de7e-3a3c-b744-b946ddd3af84 | -8.58241 | -46.30668 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| deba8708-91ec-32c7-8afe-8aa84793baad | -8.56905 | -46.26152 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01a3f3de-94a1-3e8b-8ea8-d49de18a0d68 | -8.60503 | -46.28054 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a08fc2f6-9a3b-32b2-9a59-4271eb4cb2f4 | -11.81969 | -45.06482 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9db634db-363a-32d0-96ba-caca308eb34e | -9.65348 | -45.85594 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8885726-c9b5-3c65-865e-69ddd47bfb88 | -11.77751 | -47.94149 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f6dcea-12e0-3ae7-beb0-1845bc60ac28 | -9.06192 | -47.02038 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cf96da5-d15d-3e68-880a-7b032b2b4d5a | -11.08315 | -47.91607 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 524682bd-1f00-3de4-bd7b-294790adf856 | -11.23176 | -47.80725 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b38b7f05-8825-3437-a602-79f7f17a42c9 | -9.15192 | -59.53458 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04059dd5-c881-37a7-9792-836509109bbe | -9.1931 | -62.5295 | 2025-10-05 05:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78273dba-c4db-3bb1-a023-4df51d447b67 | -8.8657 | -46.84718 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40d73016-4a04-3d7b-8afc-78feff3a9f19 | -9.33232 | -54.51283 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485a8ea1-a721-3233-ae2d-8637a2037b75 | -6.25578 | -45.3499 | 2025-10-05 05:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8563fa8f-da9c-3efb-9929-66b3edb9dea0 | -5.96418 | -43.5173 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 614bb7ed-1c39-3cf8-873d-82eb2fa6931c | -9.83988 | -59.47434 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ac9b8bf-fd5f-3b3b-b265-e0abc2d4a919 | -8.50604 | -54.59731 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e77a0d7-7f44-314c-84c4-468757ccaac4 | -9.91044 | -45.96184 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904cac56-e427-3c85-8126-01798dc4aece | -5.98988 | -44.36331 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca6a791a-30e9-39d4-a07d-d8fc3a1e3a83 | -6.84438 | -45.48369 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 802fa565-0abf-3277-87d8-122607da7c87 | -10.46699 | -57.50431 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20f3c1eb-58aa-3a70-9e21-7b92214da36d | -10.05145 | -49.20338 | 2025-10-05 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c3ff52-86a8-3f94-aad4-f2b1da92f9ce | -8.73911 | -50.65839 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b11cf14e-8257-3b00-b50e-b7841aeddd32 | -8.59253 | -46.29902 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cbc55e0b-f332-33e0-87e9-138ccc32d55d | -11.02979 | -45.5808 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcd4dd5d-e9c0-3ddd-9abc-ae2b4b063aae | -9.29994 | -46.0006 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 248f73a0-9eba-3604-b992-b30a25ff8b95 | -6.84388 | -45.48876 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 053b4790-b69b-3d43-bd7a-f3a57ef8b331 | -6.02182 | -44.02584 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d9b5cd-e9d6-3a89-b36c-2aaa59493eef | -10.99831 | -46.52529 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33ef0b56-f1b2-37a5-bca0-65bfba90b24e | -11.70918 | -47.5077 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac25de1-07a2-3813-8224-a130efc3ad12 | -10.84767 | -47.97104 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da5e56ee-9f94-3f05-9117-02b962c8ee2f | -8.57291 | -46.33052 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9c35b54e-178d-3610-bac8-00a6bd00843c | -11.23226 | -47.80315 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3363e35c-7b0f-3cce-ad51-288c716e755b | -11.81327 | -46.85587 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e82b5b3b-7706-34f5-85b2-368e95106c9b | -11.10426 | -47.74246 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ed638cc-24b5-3ed0-b604-88882ed038ca | -5.92072 | -43.33146 | 2025-10-05 05:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f5f66528-48bb-3cb2-9e62-a9625ec955ae | -8.65598 | -54.96008 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a38cab8c-4761-3184-8597-3c73a4cbca94 | -8.56164 | -46.26922 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 213d43a1-e1e7-32cd-89aa-b67e46473f1b | -8.55608 | -47.66853 | 2025-10-05 05:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e89e213-1246-386d-bae1-ca90d7a815ea | -10.94679 | -47.09031 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f1e51bf-e47b-35c8-b14a-c4a883ccc3bd | -9.34585 | -54.5239 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caeb90c1-044a-30c6-8baa-0c1e0a1c6109 | -5.78529 | -45.79458 | 2025-10-05 05:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 013f63c9-d5ad-3903-847c-a0520d873e3e | -6.1829 | -44.58965 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40534f86-7035-3f4e-a5e8-254f56247c6a | -11.86774 | -44.95313 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac930069-72f8-3ec0-bc1c-e1713d55558b | -5.64571 | -43.9109 | 2025-10-05 05:14:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92eca43c-2e56-3317-b9b5-f5b161c1c9c3 | -6.18119 | -44.60207 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2303f909-61e4-36f8-9fba-4ee1380bb973 | -9.80103 | -48.28244 | 2025-10-05 05:14:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b06fa729-d9d2-3461-835c-7e8e6b4a6be7 | -11.02845 | -45.58121 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64cac610-9d79-3f11-9083-80cbf571d021 | -11.11506 | -47.13679 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30694de2-ba99-3637-8017-2c505cbd3f02 | -11.81555 | -46.86197 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 564a7167-bf72-3a88-b398-583c50635339 | -10.39192 | -45.42024 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9686a5c1-3372-34c9-96f7-2ddadaab32b9 | -6.18434 | -44.59506 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12fde452-1f18-3067-ba28-b1683ea312f6 | -7.62812 | -45.49101 | 2025-10-05 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3565bf2a-a0d7-31f4-8da7-4d307e1512cb | -11.14727 | -47.92774 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 217d8ad6-2846-309d-b3c2-796a30ce557d | -7.79225 | -44.55065 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7df01f-818c-3da5-ac3e-84b5e952c225 | -6.16504 | -44.56891 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c1d0ef3-ea7f-33fa-9a23-52d05c02118e | -8.86403 | -46.81297 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d53ad381-d0e7-3d2f-b6bf-8b1d50c01d5d | -7.84791 | -56.54905 | 2025-10-05 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80dba379-434a-36bb-99b9-930408bcf10d | -8.54727 | -46.2814 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e5593cbb-cbd7-3b85-9276-5e8727514969 | -9.14436 | -62.37015 | 2025-10-05 05:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c02364a5-1961-3fe7-8233-88c897a0f112 | -10.75636 | -45.33949 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9521124-e70f-353e-8c0e-0ae310a5c272 | -11.1408 | -47.91594 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2198a461-6c75-3d34-ae49-604adef6795a | -6.1736 | -44.60719 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a14874b-5a83-30d2-b07d-2fdc390ed02e | -10.9423 | -47.07529 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a74c558-d6f9-3875-9ad7-ba36ed4f8046 | -9.33343 | -54.5311 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3ca968d-599d-3913-9b39-fd732701e7da | -7.79918 | -44.55151 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d4de965-5342-3dc7-aa00-c9a9fabcd3dc | -8.86504 | -46.80791 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aca95ed-ed43-3be7-bf14-88e4840df7c9 | -5.54176 | -51.438 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02411e76-f685-33ae-92b0-d2b9071d0e4c | -9.63801 | -63.24411 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f31b566f-57cc-30aa-a62d-47852fbdd487 | -8.62056 | -54.97576 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README126.md)
