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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96591b3c-7039-3684-a62e-e0ec07e50571 | -9.96142 | -64.95961 | 2025-07-16 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 066a6828-f074-3dc9-877d-17f3be875c09 | -9.02579 | -61.23567 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dec5981-ba29-30a8-9ebf-3df64a1c1531 | -9.65094 | -63.44207 | 2025-07-16 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9e48147-1a8d-3f1b-83a2-df45a79a8217 | -7.90177 | -55.42242 | 2025-07-16 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc234d22-111f-3e7f-8852-ae740e301dab | -13.16094 | -50.7748 | 2025-07-16 05:31:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eddc95a3-2355-3420-a67e-40af478a6e50 | -10.57409 | -49.11715 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25431f11-c471-31b4-9c03-221149540304 | -11.87511 | -55.44772 | 2025-07-16 05:31:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 977187dc-3c4a-3e0e-aeea-fb09a3438d2a | -9.95342 | -65.09528 | 2025-07-16 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f86eb59a-d945-36ac-bb03-a364283111ba | -7.90562 | -55.41999 | 2025-07-16 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e0cdc7-723e-3ea1-bd9f-882c38c55902 | -7.89979 | -61.52122 | 2025-07-16 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5292864-1ed6-3e84-8a20-a3ba3517d88f | -8.68876 | -64.12232 | 2025-07-16 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72433eb6-239a-3546-975c-25eaf3fbba17 | -11.94199 | -63.84707 | 2025-07-16 05:31:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2471ef3-d2d4-3935-b042-962ca88d7920 | -9.71454 | -61.29221 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c3f4ed3-bda9-391b-af2f-81260eda6db0 | -9.70599 | -56.1823 | 2025-07-16 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 762fb85c-e512-3617-a581-b5e45b0950a8 | -10.05872 | -59.09907 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850d56e3-10e2-34f0-b2da-c93328faaf96 | -7.90099 | -55.4193 | 2025-07-16 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66892a6a-ce8f-33b4-9b94-c9e9815e4a3d | -8.69215 | -64.12287 | 2025-07-16 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7fff115-a5e1-342a-a867-ceef8894d865 | -9.86731 | -60.29502 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7275746-2a5a-3775-9d1e-822a10f6419c | -10.05697 | -59.11059 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13816cdf-5f20-39b4-9b5b-fe765fab073d | -13.15719 | -50.77383 | 2025-07-16 05:31:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 828173fa-cf75-3081-b82e-636162ac8d4a | -6.9114 | -52.85472 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15543e8c-f3c6-3a3d-9ee7-dc762789ce2d | -9.64704 | -63.44505 | 2025-07-16 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 507dbcf7-6db7-329a-9867-9bb08eb55428 | -13.15421 | -50.77403 | 2025-07-16 05:31:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c106d76-dc39-30dc-9637-aa69dc3a735d | -6.90548 | -52.8574 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 843f2ab7-3133-36b5-b7e7-e8c7fcada43f | -10.65144 | -49.47745 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e6601a1-6537-3d26-be8a-aca8595c5216 | -11.94475 | -63.85115 | 2025-07-16 05:31:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b11c12d-d312-36d4-848c-1f50129ab8ee | -6.88159 | -59.32659 | 2025-07-16 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff68e14-50da-338d-b272-77a983dc5bbc | -10.5669 | -49.11619 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 471b9cef-58af-365e-a7ea-2261567fd0ad | -9.02069 | -61.22369 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25125734-33ce-33e8-9d8a-6118ee987a31 | -10.06052 | -59.11327 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f0381d7-e608-36f0-9a57-92f8e002f265 | -9.01674 | -61.2268 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841b23e4-c083-3a07-9f69-3cf7af7a160a | -10.05765 | -59.10607 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c02e0142-5c32-3aee-89ec-baffeba3c5ad | -9.66425 | -63.44423 | 2025-07-16 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04630400-6dad-3683-b3c5-df2af12e67f5 | -7.18865 | -59.83734 | 2025-07-16 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c2e8d4-a179-3c4c-b814-c34f86e8f96f | -10.65506 | -49.47974 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4d0cf69-439b-3d45-ae64-2124d8e2a31c | -9.87084 | -60.29557 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12d9d166-ba46-3a8e-a884-648343a2658b | -12.62497 | -54.2289 | 2025-07-16 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 593e4b7c-aa59-3e65-a51a-e842f3eebe89 | -6.26791 | -57.40005 | 2025-07-16 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ce95b8-6a28-3de2-b6f6-04133b1e0b38 | -9.7151 | -61.28854 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec659007-7e34-3432-8e65-3d4c2df79c75 | -9.02746 | -61.22474 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe375942-3409-386f-825c-276bdc8001aa | -9.65037 | -63.44559 | 2025-07-16 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c110e81b-1c60-3e3e-90ea-c3347b20fc76 | -10.05457 | -59.10094 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f24ab63e-f105-305d-94e5-bdd5a216441a | -6.9109 | -52.85836 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b0fe1a2-2913-37fc-93ea-c060660cff07 | -10.05431 | -59.10305 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 804b96ed-b18a-31ee-b93b-0af305cb717f | -10.06117 | -59.10875 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21b43a14-5f62-39fd-8ebe-8ef6d65776f3 | -10.8988 | -49.21212 | 2025-07-16 05:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5341387-3307-3ed6-9d47-8a6bd0e40f1f | -5.14887 | -60.37488 | 2025-07-16 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f96b0a68-6fdf-32f2-86ad-a2d7cfaec5e9 | -9.02013 | -61.22733 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e38fb4e-da1c-3d9b-814a-678c64d3997b | -6.63036 | -56.28358 | 2025-07-16 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f90fd7c-5dcc-3671-aba0-c1aabec28cee | -10.89302 | -49.21581 | 2025-07-16 05:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1917611c-c704-3766-87a2-a739af510637 | -12.62539 | -54.22555 | 2025-07-16 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e3df4a0-936a-3a97-9e7c-fec1df4601f2 | -10.89794 | -49.21951 | 2025-07-16 05:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 088daa53-0659-3ef7-a717-c8e7bca919c1 | -6.91633 | -52.85926 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77a1b902-467e-353b-899a-ac9d710e8c89 | -10.05807 | -59.10363 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc2c59ff-9cb0-3076-ba75-b2fb54940f7b | -10.90016 | -49.21709 | 2025-07-16 05:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57b33afb-7108-32e0-8948-6a172587ee4c | -7.34816 | -49.60498 | 2025-07-16 05:31:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 115f9b28-c15d-34e2-9a0a-8bac0bef0307 | -10.64803 | -49.47863 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bcad130-678b-31a4-a50a-f0a13f01a3b7 | -9.62631 | -67.21077 | 2025-07-16 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5184ef3d-db6d-364b-b0a8-9cd27e8d2c5a | -9.70409 | -56.18446 | 2025-07-16 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fd851990-e11a-3d07-9ef2-0f6cef32df20 | -6.91733 | -52.85201 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 696b04ce-785a-384b-9d77-97d12c100a4e | -9.01336 | -61.22626 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b6233ad-b196-39c7-9f52-9c6631c97bf8 | -6.62608 | -56.28292 | 2025-07-16 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 841372c1-856a-36ab-971f-43fcf6f1088c | -10.05742 | -59.10818 | 2025-07-16 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b074ae49-404d-3f16-816f-39524e6cb4af | -9.02464 | -61.22057 | 2025-07-16 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 209b8cbd-5da8-3566-8aa8-71553e83219f | -6.91684 | -52.85553 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16fb2e4e-361d-3850-be8f-95ef45d849e0 | -10.10371 | -58.22194 | 2025-07-16 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4a879fc-4717-3d21-a07e-55a4474b0db6 | -7.34142 | -49.60412 | 2025-07-16 05:31:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe40e960-4d6a-37b5-b28a-df18e2601f6d | -8.5585 | -64.19468 | 2025-07-16 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447646c5-10c0-3119-a629-8539e46ed126 | -6.92228 | -52.85639 | 2025-07-16 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f14a9887-5808-3bdf-a264-4d8b1f93fd2b | -9.36171 | -58.83881 | 2025-07-16 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915f71c7-2ead-3d95-b4b0-80ae9cebed42 | -9.96549 | -64.95638 | 2025-07-16 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ee68e7b-bcdd-3bdb-a797-1932439f4d60 | -11.8744 | -55.45322 | 2025-07-16 05:31:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1affa77-acd3-395d-9779-f3e9a21f6a17 | -10.65584 | -49.47274 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fb52985-2dbf-3b4c-b0a8-def33304994a | -9.70538 | -56.18686 | 2025-07-16 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64dce33b-8700-356f-8ce3-af45fa19edf9 | -9.96204 | -64.95581 | 2025-07-16 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da0efb86-7d43-33c5-b165-645e8617f6ad | -10.64441 | -49.47638 | 2025-07-16 05:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7e2d327-5632-3f52-957b-1435ef1fbfbd | -14.42864 | -58.89466 | 2025-07-16 05:33:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0d20ac-6d67-357a-bd99-0f03973d111e | -18.65512 | -55.72409 | 2025-07-16 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b0578c2e-9336-3953-a169-eb3eda5ce49a | -14.31056 | -52.74536 | 2025-07-16 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75daaffd-7501-39dc-a4b6-d32906e4c01f | -18.65548 | -55.72073 | 2025-07-16 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 29679696-88f8-33d7-a1a5-4967b398ab20 | -18.65585 | -55.71736 | 2025-07-16 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| af89bfaf-9558-322a-97dc-f228681b7ea9 | -14.42459 | -58.89423 | 2025-07-16 05:33:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331e4fd3-fb9f-3482-9659-981df4f4a96a | -21.04026 | -55.98703 | 2025-07-16 05:36:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3984b40a-54ce-32a3-9d4c-a368210c77aa | -21.79006 | -52.75922 | 2025-07-16 05:36:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bd5fe06-fca6-3250-9453-505ea9351acc | -21.96022 | -56.07748 | 2025-07-16 05:36:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22f23a47-3d4f-382e-844c-e5bfeb0e45de | -21.79662 | -52.75992 | 2025-07-16 05:36:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 166954b4-6b77-3637-a66c-0d236d8e516b | -21.95583 | -57.59021 | 2025-07-16 05:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dfe2dd77-9554-3374-8660-cd7cdcea1144 | -21.96069 | -57.59089 | 2025-07-16 05:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 778fee83-4d27-387f-8cf6-7bdb92fc81e9 | -21.96342 | -56.07885 | 2025-07-16 05:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e38b920-1231-3bbc-8595-9a843b228256 | -21.0399 | -55.99062 | 2025-07-16 05:36:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b99c295d-5791-3792-89b5-f480eaaeb08f | -28.69613 | -55.97891 | 2025-07-16 05:38:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| d647a966-a385-3894-a8b7-add8e7d0ddf2 | -28.69496 | -55.97995 | 2025-07-16 05:38:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 1f893293-d57a-37b6-a624-d8e41e73602a | -13.0146 | -45.0593 | 2025-07-16 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 05681da1-2a39-3f73-93c1-671e02131eeb | -6.7194 | -44.3231 | 2025-07-16 05:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 86b906e3-6d61-36e4-81ec-9d1e6e161099 | -6.7194 | -44.3231 | 2025-07-16 05:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e39ca134-dda0-3993-a90c-e694126759f4 | -9.70879 | -56.18473 | 2025-07-16 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d53207d3-91c2-3216-9996-0167b7bbfb4d | -9.02203 | -61.22262 | 2025-07-16 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17488fc9-6d9e-3727-a2c8-519f0a9c680d | -9.70835 | -56.18439 | 2025-07-16 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f2eaba3-37cc-39b2-a417-e211c50cd2bd | -9.02126 | -61.22825 | 2025-07-16 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71a1deb4-7347-39f7-9fd1-0950e9da42e3 | -8.5583 | -64.19378 | 2025-07-16 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
