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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ff70677-06e1-359c-a9dd-1590588ba500 | -3.42901 | -39.15022 | 2026-08-28 15:48:00 | NPP-375 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b6044c53-b45e-3e00-a7a5-5157b3568053 | -6.06001 | -44.88549 | 2026-08-28 15:48:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d0affba2-a67c-3e7a-bbe9-f98c12f9a185 | -6.95468 | -45.2362 | 2026-08-28 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 843b48bf-b00b-3c26-9dcd-02694e0abb94 | -3.41844 | -43.37902 | 2026-08-28 15:48:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f0ceb6ec-b6d1-3962-bb96-656689a4fb18 | -6.90259 | -43.64411 | 2026-08-28 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 872f394e-16b5-3312-b419-549a968ec071 | -3.43189 | -40.64341 | 2026-08-28 15:48:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f40d57fd-fdf2-33e0-b62a-31e2fd57730a | -14.2102 | -45.274 | 2026-08-28 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c8d2f6f1-4d9e-301a-b243-577b7e7f5d26 | -6.7267 | -59.654 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 40c17446-ebf2-38d1-bb80-3bd8dcbe172a | -11.1922 | -51.2284 | 2026-08-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6c7f5c24-dd82-3330-b231-11d10deb19e3 | -10.3334 | -50.4042 | 2026-08-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| fbac0498-43ad-3c54-a131-be71e36c4d7e | -10.5596 | -50.4449 | 2026-08-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 977b6b5f-8f26-379b-8a03-dc46a5350abd | -6.1472 | -57.7995 | 2026-08-28 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 4e2701a3-1b56-3214-afc0-b51476d079de | -13.8752 | -54.1153 | 2026-08-28 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 177.2 |
| a36fb118-77c0-3c67-b629-8313b29d6402 | -10.937 | -50.5118 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 83f36476-d8af-3283-a12e-6c39d173fe35 | -8.6881 | -49.5353 | 2026-08-28 15:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 54d432e8-53fd-3e7a-984a-325c4508e3cc | -6.8358 | -59.9379 | 2026-08-28 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 0eb959b0-105a-3f19-9634-dc48850fe227 | -10.5719 | -57.495 | 2026-08-28 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f5945b0d-dda0-34d8-ae2a-97ee66f50a9d | -6.769 | -58.7066 | 2026-08-28 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| a6069748-a05c-3b8c-af4f-114c50e4588a | -11.0247 | -49.6656 | 2026-08-28 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 1d665fbe-dea4-304c-9c1c-ef446951b420 | -10.9216 | -50.2571 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 992c5d4b-e7c0-3547-9580-22bbd1d31349 | -10.8463 | -50.2224 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| bbd311e0-0584-3238-8c09-573fbce8cc9e | -10.899 | -50.5159 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 597335fa-507d-3f27-a13f-c03a40821959 | -8.9418 | -45.748 | 2026-08-28 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| b7bd78f9-a60c-3f73-8b26-d6cb8b04265d | -13.3226 | -51.4493 | 2026-08-28 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cd5cdb41-875a-3089-a2ec-5d6398ed8c81 | -8.961 | -45.7233 | 2026-08-28 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 9e5673a9-7d6d-3d2b-b02f-9eb95d12719e | -8.8372 | -49.6291 | 2026-08-28 15:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0a41a5c9-3095-34e2-b691-cc1f8895eb84 | -10.8422 | -50.5219 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ba4227d6-6559-3362-b7ce-d5b1b0a6e1bb | -12.2281 | -50.5578 | 2026-08-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6f6094eb-98c3-3286-806b-01b85aa4a3c2 | -8.9421 | -45.7253 | 2026-08-28 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4f70958e-eeef-3a2d-aa3e-c3e374488f56 | -10.918 | -50.5138 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 2886ac42-196f-347b-aa25-0024af9148fb | -6.6727 | -56.3634 | 2026-08-28 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ffd1fe52-9597-3d67-8627-1b0483f33a28 | -6.1473 | -57.78 | 2026-08-28 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 295682ef-3b54-329c-81e3-7ebda7bf45dd | -6.7647 | -59.4601 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d59b69d3-a8f1-3c5e-a69b-ba427d3b70de | -7.3665 | -55.1534 | 2026-08-28 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c2348685-d86c-3ead-8e9f-1bd3f866a7be | -11.2128 | -53.9976 | 2026-08-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 52932449-20cf-3ead-b71b-66c4f7cf66f2 | -6.9872 | -59.2582 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7e13dcb3-90fa-3181-a1c9-1a5fe772c76a | -10.9556 | -50.5311 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b7a32658-a5e0-3fb8-a15c-4ab338db5fcd | -6.9335 | -58.9707 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 263163bc-8a5e-3aef-8bb2-01145afc0d41 | -12.3999 | -48.2073 | 2026-08-28 15:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| d32164a3-4b15-3a78-8807-a4f34b8f35d8 | -8.9607 | -45.7459 | 2026-08-28 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 03a5ead2-9f14-334a-8251-c8b875719431 | -4.9582 | -56.277 | 2026-08-28 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3ddbf1e7-2354-337c-b210-982a95817c54 | -8.8187 | -49.6093 | 2026-08-28 15:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 509da8af-c128-3f23-8683-ac01c21321ef | -6.8257 | -55.6218 | 2026-08-28 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ce56f4b9-1c7b-32e2-959d-f46627a161da | -10.8993 | -50.4945 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 085a6b30-f767-3bf5-a150-d419713b5ada | 1.51 | -55.9638 | 2026-08-28 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 297826e0-278e-3793-aa92-d8d4d09036e2 | -11.0057 | -49.6677 | 2026-08-28 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| aae9ef76-39d0-30a3-a5bd-67920f3a3bc7 | -11.1732 | -51.2304 | 2026-08-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 36174184-0e7f-3ed5-ae9f-e5c584cc7a1e | -11.269 | -54.0334 | 2026-08-28 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 7c5bd70c-dcc5-3e48-98c0-72b615c945c6 | -10.4981 | -64.5005 | 2026-08-28 15:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 8bd82123-d549-3127-bdff-7fd0c073768d | -4.903 | -56.279 | 2026-08-28 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ead34268-fa13-3df9-8f45-d73e5a056f8b | -10.7839 | -50.6346 | 2026-08-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 86de7cb9-06d9-372a-a53e-8bd20840ba5d | -11.025 | -49.644 | 2026-08-28 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2b219ca1-7fef-3f61-811b-b1e54a929c78 | -4.9031 | -56.2593 | 2026-08-28 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 27fab5c4-4e83-38b6-8974-1e803281fb62 | -10.7409 | -54.0196 | 2026-08-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6eea9ce0-aab4-3460-a75c-01d9380ece5a | -10.7649 | -50.6366 | 2026-08-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4632a20f-d46d-3ee0-8ee1-b4e459511547 | -10.7593 | -54.0589 | 2026-08-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ba02ec94-1cb4-30dc-af40-8def387bb656 | -7.3479 | -55.1544 | 2026-08-28 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1777ea0e-b772-3ca9-8a3c-1e9e1d0fca44 | -9.1525 | -49.9639 | 2026-08-28 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 43a2b2ec-60c4-3f70-bc25-930350dcc942 | -14.2302 | -45.2472 | 2026-08-28 15:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 9f986e6a-a0fe-32dd-b60f-80af42cbec8b | -10.559 | -50.4876 | 2026-08-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 03024449-1d86-34b9-b611-65f080e80f5f | -10.3526 | -50.3809 | 2026-08-28 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 01e48b7d-870b-370e-913e-c22c91a8f860 | -8.3718 | -62.697 | 2026-08-28 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 90d78579-3adb-312f-a716-f077554f21e9 | -6.8388 | -56.4146 | 2026-08-28 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| dab28e96-2998-3925-90ed-94d264f35c6a | -6.7831 | -59.4594 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 904f3fac-e5dc-3f9f-b83b-5a18ff067b9d | -11.8243 | -47.1954 | 2026-08-28 15:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 7f1341e3-8ad3-36ea-9da5-b4d0505efb8e | -15.3251 | -52.7607 | 2026-08-28 15:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0a1f5116-a8e4-3358-baba-7cc38dc89292 | -10.9592 | -50.2744 | 2026-08-28 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 446fc0bb-5e1a-318b-9c03-787af721e04f | -8.8184 | -49.6308 | 2026-08-28 15:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 532baf1d-b3ca-34d9-8ee9-dc867ca2b22e | -8.3717 | -62.716 | 2026-08-28 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a3ec2b9b-8fcf-33e6-a972-881f57e911c3 | -10.7787 | -54.0163 | 2026-08-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 09ba946f-261a-3e96-9d2c-8810184104e7 | -8.6694 | -49.5369 | 2026-08-28 15:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 8ddf4024-cc80-3ce8-aa0a-62df3d3c62e2 | -10.7598 | -54.0179 | 2026-08-28 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 78425534-6a5e-3a22-a81b-c22753a3411e | -14.5827 | -53.1744 | 2026-08-28 15:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 147961d9-4241-3c16-b987-6366241e5b17 | -6.8541 | -59.9564 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6baf8dd6-0a02-3419-af62-c3007dd84048 | -6.2693 | -53.1322 | 2026-08-28 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| a8512343-67d2-34b7-8e27-1801f953d404 | -13.3981 | -51.5251 | 2026-08-28 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4c61268a-4342-3102-a59d-b47ec02192bb | -8.3902 | -62.7152 | 2026-08-28 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 1610c8c1-1c06-3e64-88fb-70afbd123437 | -6.6729 | -56.3436 | 2026-08-28 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8008e9d1-3ddf-3c8b-a39f-c4d7b1985ff7 | -6.7451 | -59.6533 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 09bb02ab-78e1-3c80-bb09-6e43dc691bc3 | -6.8542 | -59.9372 | 2026-08-28 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 24082982-de78-3629-a7e3-68d7fe0db081 | -12.209 | -50.5601 | 2026-08-28 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5ceaa141-f438-368e-a3df-eb67bbfe88ed | -11.0224 | -51.1827 | 2026-08-28 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 891055f4-aab8-399c-a0a5-74f8c3c5c8a5 | -6.695 | -58.7291 | 2026-08-28 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 10b5b363-8458-3319-9180-918e89c74746 | -6.7107 | -45.169 | 2026-08-28 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 7de06eaf-a965-31b0-a314-8004f87f83e8 | -10.3898 | -61.1925 | 2026-08-28 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ec3535a2-15ab-3b02-a5a0-1123c51e0b17 | -10.7598 | -54.0179 | 2026-08-28 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 2bf63140-14a3-31d5-b44e-3b507714d10c | -6.7832 | -59.4401 | 2026-08-28 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9297f775-1e0c-3f65-8535-177f5d2229a2 | -16.1641 | -58.5851 | 2026-08-28 16:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| eafbffae-1e11-3b9f-a13e-f3f5b26c6c8c | -6.8015 | -59.4586 | 2026-08-28 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f6032d74-f0dd-34f7-8464-f2f2ee4019b8 | -7.0057 | -59.2575 | 2026-08-28 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f3625677-511a-33eb-8a73-cd6c0fce2478 | -7.3479 | -55.1544 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c1e1c3ad-382b-314c-a5a0-a04e1e1e5885 | -9.0278 | -69.569 | 2026-08-28 16:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e0a6f6b4-0352-3875-af54-422511013bdb | -6.1472 | -57.7995 | 2026-08-28 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4cc7bd83-fa23-316c-bd02-6248f5eb60da | -10.7839 | -50.6346 | 2026-08-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9ae76097-a7ca-38ce-a5b8-0bdbc92bace8 | -14.4842 | -52.1512 | 2026-08-28 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7a266812-2144-3038-8214-23459411f733 | -11.0224 | -51.1827 | 2026-08-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1779bb50-40f4-34b6-b2cc-9d9ceb71bf19 | -3.7729 | -58.9002 | 2026-08-28 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 785a09a0-0da0-30aa-9766-7f27dbeb607c | -6.8357 | -59.9571 | 2026-08-28 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| c5c9a972-e4dd-3f67-a294-1850d041b0de | -7.3665 | -55.1534 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| c4cc777d-1e0d-34ee-ae69-2090a28181c2 | -12.3999 | -48.2073 | 2026-08-28 16:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |


[Clique aqui para ver as próximas entradas](README88.md)
