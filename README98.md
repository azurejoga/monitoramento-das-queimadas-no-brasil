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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a0fc2cb-1496-31d4-bc03-ff290f942463 | -5.84734 | -53.54899 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e87d744-2f79-3a02-9102-ff2026667323 | -7.80888 | -61.80823 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8d33e3-2ad3-3f11-b66a-e5b49f9a35e3 | -6.50095 | -58.38103 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f4d62e-7706-3e32-bd67-cf5ad696d5a5 | -5.93075 | -59.95389 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c3f81d7-fde4-36f9-b1e3-3157777732d3 | -8.79008 | -48.73876 | 2026-09-21 05:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 878db41f-3f51-3d48-947b-1a032d3986c6 | -9.17093 | -60.85251 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2902e2-a2a0-31eb-b08b-da1fc285a281 | -9.36479 | -60.31552 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 350b2e85-5753-331a-a93c-b5ae3bd86dc0 | -7.31775 | -55.60976 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33e8458b-5a8a-3a95-be10-d464be96b122 | -11.03116 | -57.24107 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90b18c85-c2bd-361e-8f14-95ad5e5849ad | -6.69277 | -60.00866 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6bad29a-1b72-389f-82a1-7f703f086265 | -10.71684 | -54.01468 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebbfefb1-9a13-3f5c-b00d-baa0f7013348 | -6.31388 | -60.00732 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcce5322-ae62-3d21-a0eb-34b1fcb3c7a1 | -9.11428 | -60.94707 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96058886-df0d-3de4-9d41-5ec4669a68ec | -10.74738 | -50.80167 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa97e74c-8b3a-34bd-a051-55597f55be63 | -5.84179 | -53.55119 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9166432b-97d0-38cc-aa54-302a6df31ee9 | -6.13053 | -59.94515 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a48d625-9f97-3091-b2d9-4cb0561df743 | -6.28465 | -59.92115 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d0b1c90-5376-3024-9810-00f4d744affb | -5.80623 | -57.73676 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01d29e48-f763-30f0-a126-4092c24a4dda | -11.03063 | -54.14362 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab855f49-e61c-37e6-a142-c93e5ffc8a90 | -10.31229 | -50.5577 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c409b100-e17b-34c7-9746-073b9cca8e82 | -6.15842 | -57.70921 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2222149-317f-3136-88f9-8c7153e9cfa1 | -10.4602 | -61.31063 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09315cbd-8fba-3ce3-bf84-c2bc2476647e | -7.81222 | -61.80877 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e3a379-9b70-31b6-9946-7a2ae0d05770 | -6.09887 | -57.62823 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7c4e7a0a-3bc8-3f4d-970b-5f20ffdafc59 | -6.72703 | -55.05982 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c457c185-5afa-304e-903f-2fceeca878d0 | -10.46593 | -50.27283 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0751654a-31db-3a7d-b176-3f4bad93ba50 | -7.58649 | -57.68375 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f943f7eb-28ca-3bb5-9894-df02f98f81b1 | -6.13515 | -59.93811 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d67e56ac-2b67-378e-b09b-311975f2e421 | -6.28812 | -59.9217 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e38089-8c9f-3ba1-bd0a-64a8ded3ff0e | -6.13399 | -59.94567 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9e51289-d895-32da-aa57-766749b99503 | -7.21574 | -60.68681 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e53a0b9-e8ca-3ecb-ad6e-8104312984e9 | -9.55894 | -66.04562 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac6f5aa-efeb-3d11-97ab-b4d79155b7aa | -7.55369 | -61.31899 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad25285-dd98-3121-86eb-b8be2349223b | -5.21176 | -56.10595 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 904e5e55-9386-3184-a821-b71a5b82cfa7 | -6.0964 | -56.46574 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6af2425-5e98-33fb-802c-044b0696b18f | -9.30307 | -62.31064 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b33b7247-cdef-35d0-85df-7db1dfd980b1 | -6.46239 | -59.98603 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2b16322-92c3-3700-ad9b-c1918cded212 | -6.74846 | -59.06032 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49f44d49-950e-3f81-b0d1-cd547d98f82b | -8.18053 | -54.77153 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86965acb-30d5-315f-951e-1b7ac9236c8c | -6.21383 | -53.57048 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68bbe5c0-d7f8-3baa-9dc7-580e4a536aa6 | -10.75326 | -50.80809 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c232a5e0-57c1-3711-bd26-58eb9ab8b4df | -6.70959 | -59.45686 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9f64801-b50f-3c68-8c73-3f0c6a3426cc | -6.46067 | -59.97404 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a675be71-cf51-3e38-ba60-f7a10cd84de6 | -6.74227 | -59.42342 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 437ecfe3-be7d-31b5-a951-4596f9542887 | -8.18265 | -54.73964 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9882b0a9-2250-3cfd-b582-54ae2a62f539 | -10.8747 | -54.08046 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97bf0a48-0f5b-3288-a461-0ef871e23cfa | -7.59594 | -57.67472 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23a0ee15-6a50-34bb-a94b-974c91fef01a | -9.23316 | -60.25599 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b676357-e184-3711-a856-36e5f652e65e | -10.80222 | -50.84224 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aa6de691-200c-34ee-9a4d-19b6638d1d3c | -9.56842 | -66.05595 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bbfd21-e0a3-3747-8216-0acc3e56deac | -9.37383 | -65.48007 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20905c1-d195-34ea-bc3b-2f36e81726e7 | -8.79579 | -60.79575 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7367680-8083-3738-9c22-825ee52b5ec5 | -9.18307 | -60.7734 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a141048-912a-3393-8514-e5e1dea701e5 | -9.55811 | -66.0281 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8423ef48-5539-34a3-a356-ffa13819c1a3 | -11.02116 | -54.14268 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15129593-a7ba-3116-9cd1-303927742bdd | -10.8832 | -53.97241 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be841a37-b077-3091-86eb-56dc43e40f23 | -5.82956 | -53.49055 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7934ea99-3c94-3c48-a2eb-fb1d7edb981e | -8.18784 | -54.70152 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f61db01-e648-32f1-9485-a30395f37457 | -8.85348 | -68.50916 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4fe21a4-3372-32b2-aa99-1f5a4ad6b874 | -5.94087 | -57.6965 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e50129bb-79a2-302c-af72-7ba4a7437b92 | -5.981 | -57.77176 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1909ffc-e8b8-3cdd-890f-9768d9813f65 | -5.82609 | -53.51476 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea7f873-571d-30b4-875a-95c33184bd84 | -6.25603 | -55.44104 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60fe8e5b-47e9-3052-936f-db525c308a53 | -9.56689 | -66.04262 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| debbc5ee-4af5-3fb0-b8a2-4063a6a78a90 | -7.56986 | -57.68646 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d9d2526-47c7-3814-91ea-467a293bb2e1 | -11.0298 | -54.15028 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a936b944-2b6c-34a7-a3d5-c1e5691480a3 | -6.10934 | -55.68808 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 404506a7-3518-3071-858e-0b0760ada1e6 | -8.18992 | -54.7064 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c55c790d-4963-3f9d-b8da-a9c8f6e8f4d4 | -9.93555 | -60.72922 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95e1879b-f39d-3222-a529-d83b5707fbc6 | -6.49719 | -58.38047 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17b302f4-3138-355e-9a69-814e1ed12296 | -5.84514 | -53.56416 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6e74429-d893-3412-84cd-6bd0ef8eb8a6 | -10.43298 | -50.26268 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93c0a390-bcce-3ea8-9344-b7d7d0a0686e | -6.77517 | -55.49585 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eba076d-e60b-322b-a6cf-45f5d00a5931 | -6.75526 | -59.11271 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11f22806-26b9-3878-91cb-6c91f7300a6c | -5.74295 | -57.57862 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31025606-ec29-3b32-af0f-aa27feffd402 | -6.29388 | -59.93044 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 744dfd9f-f6db-3c54-9e38-07782262b4fe | -11.02073 | -54.14598 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79130bdd-aa8e-3f51-9918-8dc0e49c3e42 | -6.75953 | -59.10908 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82193f9c-4304-3a06-8712-11e15147ba1d | -10.48686 | -50.29313 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b77e94cf-3dab-312c-ae61-4c440e57ee82 | -8.17643 | -54.76542 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a04332-3d18-3fd0-bae5-94d28993e8e1 | -11.12853 | -54.01442 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f645616-9e52-3261-85e1-63af4adc0ee0 | -8.91523 | -50.83831 | 2026-09-21 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275a642d-2688-3dd9-ace8-61a07f9755b9 | -5.89347 | -53.64232 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9c114cf-370d-390d-85ca-4b89cfd91376 | -8.78933 | -64.15263 | 2026-09-21 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a48f36c4-fa56-3609-ac2c-6eb90337f071 | -8.61298 | -54.59636 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a4671a7-a54e-3292-b952-aaa072e198b2 | -6.7591 | -58.94156 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 388254c8-3a30-316d-a64c-5f5fc67a5790 | -10.4029 | -50.22851 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37d1608c-1334-33af-a6bb-2df079a3d26f | -6.7265 | -55.0761 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8d07bfb-a1e7-30ab-94f9-b25b332a2b27 | -5.89305 | -53.64528 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63711b57-97cd-38d2-ad08-6f00e0ad0b4b | -10.42302 | -50.25462 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4da8480-3aeb-3c98-9c9f-72cea6dcc9b2 | -5.98175 | -57.76686 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d6b8ec8-465a-3d58-9916-713ad9792c4f | -7.57758 | -57.6615 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5c5cf1f-8b56-3573-8920-77113920fab1 | -9.0398 | -61.65579 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 668178ea-9815-3f7b-a283-31fe86a1c6b6 | -5.94014 | -57.70141 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 481ab227-6d18-3adc-ae48-91628342a82b | -8.18338 | -54.73428 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3b27ec2-680b-3514-8abf-6fd9d048735f | -6.18853 | -57.77304 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f749da9-ad34-3a92-8afa-c57422e323ce | -5.88439 | -57.72582 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 014e9b68-e513-3752-b32c-0731e4607ce9 | -8.1811 | -54.73294 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e68b55da-b98a-3a7c-95ac-8f1d70b231b2 | -5.21152 | -56.07801 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac9c011b-4b9e-3ab7-b45e-65c64add136d | -11.0318 | -54.1439 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README99.md)
