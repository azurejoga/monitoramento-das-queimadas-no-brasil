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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6754816-2334-3e5c-83d2-77bd59ec101c | -11.0991 | -54.0285 | 2026-09-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d27f6715-388c-3df3-843f-f952276c9e11 | -11.1714 | -50.0151 | 2026-09-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f3d9773e-0848-377f-ad90-8efab782f446 | -13.2249 | -51.5679 | 2026-09-26 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2204239e-905a-3d90-873f-ff180cb2fada | -12.9457 | -51.0695 | 2026-09-26 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| aab967fc-c39f-354e-8271-b8a4d6f01607 | -13.2057 | -51.5703 | 2026-09-26 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 0a101ea6-5196-3e41-9e1f-0933af10be50 | -12.6651 | -47.2795 | 2026-09-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| e7b8bc54-f0b7-3861-80b2-2be4ea7949d5 | -13.0853 | -47.4199 | 2026-09-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| a28393f8-c3c6-39d8-ac00-fec64f1e31ee | -15.4322 | -41.5199 | 2026-09-26 14:20:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 151.4 |
| 5e57151b-b16a-3420-8dcb-90b92a366e59 | -12.9461 | -51.0481 | 2026-09-26 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7019f68f-a2d7-3537-8910-3996389f9cd4 | -11.9641 | -57.6081 | 2026-09-26 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 024fe0e8-423b-32ea-9cbd-b515472ce702 | -13.8154 | -51.834 | 2026-09-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| dbbc5a8b-da98-3fe9-97e6-218e9811a851 | -10.9358 | -50.5972 | 2026-09-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| ad58e071-4322-391b-8985-ddaf9438b3cd | -12.7032 | -47.2964 | 2026-09-26 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| c19b0bd3-6406-33f5-b305-6fc6316e1691 | 2.8913 | -60.275 | 2026-09-26 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| fd9fa1aa-28cb-385e-baac-3ffb12029639 | -11.1183 | -54.0062 | 2026-09-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 73b6fca5-87be-3008-b636-4e099542f2aa | -15.4322 | -41.5199 | 2026-09-26 14:30:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.1 |
| 9791b139-47c1-3a8f-934f-e0ccee8771e9 | -12.6655 | -47.257 | 2026-09-26 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| ed6d0f8c-294c-30f0-bd34-99b7d6e7babb | 1.6383 | -55.9427 | 2026-09-26 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 5e691240-b360-3f46-8c59-9b5c53f5a8c1 | -11.9643 | -57.5882 | 2026-09-26 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4711950a-6112-3b0e-ae4e-e3fff27827b1 | -15.9268 | -56.2513 | 2026-09-26 14:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 8fc219a2-c3c6-3f71-b709-91ba5efd21d6 | -13.5484 | -52.9227 | 2026-09-26 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d536fde4-87e7-352a-881e-97ebf3b8b1e9 | -15.9265 | -56.2719 | 2026-09-26 14:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| c42f6ec3-be9f-3665-85f3-fc1580e05da5 | -12.6651 | -47.2795 | 2026-09-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 63fc05ca-2013-38ed-9ebb-4c8671c64983 | 1.6382 | -55.9624 | 2026-09-26 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 01ac6e23-29a9-3233-af0e-3928b4a07930 | -13.0853 | -47.4199 | 2026-09-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 1084775c-b772-3eb4-83b7-f8b06571c050 | -11.983 | -57.6066 | 2026-09-26 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 01d7c5f8-8e6e-3e2c-a146-b8cece3c9ce2 | -14.7475 | -45.6191 | 2026-09-26 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9d60e4b2-2a0c-3506-baa5-e1bef4717704 | -11.8014 | -49.8129 | 2026-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 024debd6-fb21-3cdf-bfb7-cf5861537d5f | 1.2794 | -50.8718 | 2026-09-26 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 36f8031a-666b-32a1-8eb4-deb114cca758 | -12.723 | -50.6475 | 2026-09-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 184.1 |
| b1cb2103-5eee-3747-bf84-4e41fd082b59 | -14.7671 | -45.6155 | 2026-09-26 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c4ce3a10-e4f0-3876-9fca-c416eefc8099 | -12.8059 | -54.0255 | 2026-09-26 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| bc648844-4075-3b02-9231-b4803f8281ad | 1.6382 | -55.982 | 2026-09-26 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a1c2782f-fe65-337e-a2ce-133b5a284041 | -12.0171 | -50.647 | 2026-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ff53e56f-4923-30dc-ae31-68adb4f8a057 | -10.7115 | -60.7312 | 2026-09-26 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7711d2c0-d3e1-394a-8980-379745bac2f8 | -12.6844 | -47.2767 | 2026-09-26 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 48563219-2231-3b48-ac14-dae8cff99791 | -11.9228 | -50.5938 | 2026-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 995ba8d6-cfde-3834-9e62-cd587e0e325c | -11.9418 | -50.5916 | 2026-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| bdb8aaf5-f770-32f6-b56d-2e9629ebb585 | -12.0556 | -50.6211 | 2026-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 57649c9f-80eb-3c43-a79c-4c9c726f5f9f | -6.2401 | -41.6153 | 2026-09-26 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| 92ea4523-74d9-3e80-87e0-aad37e547ad6 | -13.5352 | -40.6285 | 2026-09-26 14:30:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 162.3 |
| 9d781a9e-1851-3978-8036-25971a2e4bae | -12.7226 | -50.669 | 2026-09-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| df0226df-9554-37ac-82b5-fbe2a5c8c13d | 1.6565 | -55.9621 | 2026-09-26 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 02879413-3a24-3e85-8a15-f97b7959f648 | -11.9641 | -57.6081 | 2026-09-26 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| c39f63d8-ed76-3fd7-980a-1dbff21f4993 | -6.2587 | -41.6377 | 2026-09-26 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| feef58b0-3d3b-3dc4-915a-b385e2284db3 | -10.9547 | -50.5952 | 2026-09-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fe1f8ff6-5d97-379b-9175-9ed0b83110b6 | -12.9457 | -51.0695 | 2026-09-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| c3365f69-3d1f-323d-945c-607424225d8f | -13.5295 | -52.9039 | 2026-09-26 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5ce5ef69-d9b1-3173-8f9b-071cec27ff93 | -11.118 | -54.0268 | 2026-09-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4837696e-9db5-3afe-9d81-4715fcde5974 | -11.9832 | -57.5867 | 2026-09-26 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 980c1014-ff35-3e81-b37c-7b6bf467d89a | -12.9461 | -51.0481 | 2026-09-26 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 84e93f92-adcc-3119-8913-3ff7df3b34d1 | -13.8154 | -51.834 | 2026-09-26 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 67381355-7ea4-3654-a835-12a42ef97edb | -11.1183 | -54.0062 | 2026-09-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| eb7fa2fd-df88-3d4c-936f-77f59670924a | -6.2401 | -41.6153 | 2026-09-26 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 333.9 |
| ab470b7e-de6e-3d29-85fd-9c4fb900c298 | -14.7671 | -45.6155 | 2026-09-26 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| b86dc9b9-ac56-3466-96c5-d97b15164bf3 | -12.6071 | -51.9595 | 2026-09-26 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 62802397-fde3-3000-8642-8f1554561890 | -13.5295 | -52.9039 | 2026-09-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8bceee3e-6b24-325c-b529-fa820c9f044d | 1.1316 | -51.185 | 2026-09-26 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 05c046f8-3183-373d-9f61-de2016ce869f | -12.9461 | -51.0481 | 2026-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4349b51b-2af5-3095-ad30-95c356155ba4 | -11.9418 | -50.5916 | 2026-09-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| fb6b8241-173f-3492-9ff6-cb1167c77695 | -11.9641 | -57.6081 | 2026-09-26 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 5adfd086-f112-318b-9d71-e859f25515d0 | -12.7226 | -50.669 | 2026-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1072b096-e0b4-3154-bd18-c62af9c34b93 | -10.7114 | -60.7505 | 2026-09-26 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 388bdd27-10dc-39a4-b06b-6276212b530f | -14.7676 | -45.5922 | 2026-09-26 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5bb6b42f-e1d0-3546-ab17-f9fbfddfa4f9 | 1.6382 | -55.9624 | 2026-09-26 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 79f29691-380c-3434-88d1-f3d03fad0baa | -11.9352 | -49.7752 | 2026-09-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 34fe822b-67bb-3b6c-a9b7-0ea852f06a7d | -11.9228 | -50.5938 | 2026-09-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9a8c9f60-6d1e-3f25-9db5-f7164997f4ce | -14.0232 | -52.0624 | 2026-09-26 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b20b2249-7015-34ab-9783-e4694e2bc253 | -11.0991 | -54.0285 | 2026-09-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 1f388058-8fa9-3a65-a9e6-4c6954b70310 | -11.2831 | -54.4213 | 2026-09-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a5ca6b52-6cb1-3a6e-b752-3d4aa1d65617 | 1.6199 | -55.9429 | 2026-09-26 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9d526feb-ed08-337b-bb3a-50f5d9a07c4d | -11.1183 | -54.0062 | 2026-09-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 66e7ae02-443d-3d03-97a4-cd0e598a73a9 | -2.9579 | -50.3988 | 2026-09-26 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7a43b964-bab3-3951-882d-22b654ba415b | -13.8154 | -51.834 | 2026-09-26 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f28f7071-0e1d-3c71-9a41-1ec3267f7311 | -6.2399 | -41.6394 | 2026-09-26 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 7415b0f0-255e-31ac-9696-31a8c575d419 | -13.2592 | -51.8186 | 2026-09-26 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d9f29ce8-fa05-3ec3-943a-db3ec8f20c15 | -12.0277 | -49.9583 | 2026-09-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 883e3aaa-1070-3d2f-88f8-00c23ab759b9 | -10.7115 | -60.7312 | 2026-09-26 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 37afd360-a82e-3922-b20f-97c43c51e123 | -6.2587 | -41.6377 | 2026-09-26 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 99daa393-464e-37cc-88bf-c1311046e3c6 | 2.1083 | -50.8375 | 2026-09-26 14:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9019c0d0-d004-399a-b477-72fdc6a9909b | -11.118 | -54.0268 | 2026-09-26 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 051c99fb-f3ad-3704-baea-1af8ac89524b | -14.5121 | -41.4228 | 2026-09-26 14:40:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 161.2 |
| 7e04f2e9-b82f-37df-8bca-9682e2a7adf5 | -14.5317 | -41.4186 | 2026-09-26 14:40:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 248.4 |
| 368332a9-7d28-3fba-be59-c89f2af925f3 | -16.3724 | -42.5672 | 2026-09-26 14:40:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e3c3f83a-45fd-3d22-85e2-5e08bf21733a | -2.9764 | -50.3983 | 2026-09-26 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4be94745-76cd-3b6c-8063-4415de53ee89 | -12.723 | -50.6475 | 2026-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| e9c09abb-5b5e-3437-85cf-198967597c6d | -12.6655 | -47.257 | 2026-09-26 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 071247e5-5e6c-3578-b454-534440c3b071 | 1.6199 | -55.9626 | 2026-09-26 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3c5f7528-5351-34b5-8ff6-06a503803b75 | 1.62 | -55.9232 | 2026-09-26 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 59e0358f-9927-3cc0-b5fa-254aef889a69 | -11.9643 | -57.5882 | 2026-09-26 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c5c5ece4-06ab-39a0-9384-2c7da632f91d | -13.5484 | -52.9227 | 2026-09-26 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 4275296d-9efb-36aa-98f6-4367384f46cf | -12.9457 | -51.0695 | 2026-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ebd90e40-4e5a-346e-a014-017b0ad3e826 | -11.8014 | -49.8129 | 2026-09-26 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 4c762c93-2262-3b8a-ad67-d158f0223bb7 | 2.188 | -55.8167 | 2026-09-26 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8058d57b-f6f8-320f-a35a-93aefec8db23 | -12.6075 | -51.9384 | 2026-09-26 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5e82a292-4933-3071-a4d7-dc7ef3898063 | -12.8059 | -54.0255 | 2026-09-26 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4c470777-b720-3f08-b0d5-97c1c29cc59b | 1.6565 | -55.9621 | 2026-09-26 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| cfc4de6f-8850-3681-a82e-a77105b6b79e | -13.4012 | -51.3328 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6963da5e-3e2c-3010-8f39-fb50b72d52bf | -11.1183 | -54.0062 | 2026-09-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 1bad5d30-613d-3fe9-aa67-5cfcaead6d02 | -2.9764 | -50.3983 | 2026-09-26 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |


[Clique aqui para ver as próximas entradas](README36.md)
