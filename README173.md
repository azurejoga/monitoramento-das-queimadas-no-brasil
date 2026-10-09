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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c60c82c-c3c1-3cc3-ad22-ac8be58c032f | -12.22886 | -57.09708 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1809fde2-8db9-3a0c-bc60-80d107bea077 | -12.23392 | -57.08924 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ff1bcfd-3b25-3c88-bee2-2f2d1507ba33 | -11.38627 | -55.0972 | 2026-10-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c72a89c9-ee21-30b0-82cf-048c87520c82 | -12.23974 | -57.09906 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b87cfb0c-672f-3aba-8698-688f2ad457b9 | -13.96546 | -53.98681 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43be32d4-76e9-368d-81a8-223bd4a1e92a | -14.00697 | -48.76482 | 2026-10-09 05:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a51f29b-42cf-3bb3-a270-d08a68ce6981 | -13.1693 | -54.31529 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2da67d09-fe11-3e7d-8ab0-b7b3fa926067 | -13.15697 | -54.34969 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ca12232d-6a1c-3944-a213-c95747d8c2d2 | -17.17579 | -51.7452 | 2026-10-09 05:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03e3e99a-d4a3-3e36-a9fd-7585b5389549 | -13.18637 | -54.35823 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c208ad03-b38d-3689-a22e-3e12e009e164 | -13.20855 | -54.36922 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6b2afa2-82d4-39c2-a71f-26b652cf59fa | -13.18262 | -54.3175 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2762a09e-b255-3b2e-a922-dc3650bf9431 | -13.15704 | -54.32784 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29f615e7-4b1f-3e40-ba63-61e5210a6507 | -15.7342 | -50.80082 | 2026-10-09 05:06:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aba1bb3-9856-3986-9403-a0bc66aa1812 | -9.25308 | -62.30458 | 2026-10-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89c9ad53-1ef2-37ea-bb71-a0b4a3022332 | -13.16264 | -54.31419 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8133715c-c08f-3c90-b20c-7ab3fc195ca7 | -12.67489 | -57.32721 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1697480-82a4-3676-8024-8ac334ec5a03 | -11.78761 | -46.80433 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91b6725d-a4ec-3fc2-a119-e22ac230a1d9 | -15.07765 | -43.11473 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 0ea4cd3f-185b-38a0-aeaa-fad91c9b58c1 | -13.18524 | -54.36533 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3212fef-ccb3-3319-9999-49a5c528a023 | -13.16118 | -43.28068 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 444a6454-4b10-3a6a-a62e-b8742703b9d8 | -12.22958 | -57.09283 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1afb3893-1c82-3b2d-bf0a-ad029dd5d21e | -10.24385 | -59.02406 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb58623-5561-3f9b-b211-81092ba41def | -18.32766 | -42.37951 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 0d825571-ee06-34b8-ab09-e1ce904c1a37 | -14.05257 | -43.82935 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9d75b04-8cd3-385c-8fc5-60de726ba6e1 | -13.16696 | -54.35135 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7e1d2bad-f343-31d8-a728-c373aeeec346 | -13.1642 | -54.34724 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a6bc4c1-1488-3d59-ada8-bcaed20ab6cc | -11.35458 | -55.09935 | 2026-10-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1669fdb5-133d-3690-840e-5d1bca161753 | -10.67657 | -58.73839 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 516e6d63-b953-37d2-9858-dd924d3b69a8 | -10.84749 | -54.02547 | 2026-10-09 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929e855d-f16d-39ea-a2ff-41e12f99a36f | -13.17043 | -54.3082 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fa62b02-1ffe-3d79-b4ea-c7a2f6bdc252 | -16.12422 | -43.74876 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 777d80cb-9202-33ae-b450-b0fa1b9d9f80 | -12.22015 | -57.10435 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a315c0bf-cd24-363a-976b-a1266fad66c8 | -11.79948 | -46.78533 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf43baab-fbe2-3936-bdc6-57672d61ef36 | -11.78365 | -46.7989 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca3a0899-8102-35da-aec0-b658694da536 | -12.2354 | -57.10266 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5f03c26-c63e-3f15-9b68-a0a0d811e29f | -12.21072 | -57.13786 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6d26376-185a-3315-b283-f86b8c632b6d | -13.16987 | -54.31174 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b55d7ce8-75ef-30f0-be76-b547fab83643 | -11.75447 | -61.06893 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a096cf59-3377-3360-8d88-b60682fc5e09 | -14.87375 | -50.30512 | 2026-10-09 05:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3bcad95-e44a-392e-ac2a-5280455d7ac2 | -15.56394 | -44.51395 | 2026-10-09 05:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19ff50f5-343c-302f-bc4d-516a7049f20d | -11.97137 | -57.6109 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39ad7e6e-9b21-38c4-a511-2f7eba3e46d9 | -11.75445 | -61.06078 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5eae4a8d-d561-3906-b3ef-e236d7f87a7c | -11.46012 | -54.29971 | 2026-10-09 05:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce501515-27ac-3411-a264-f2b744c98c5e | -10.67371 | -58.73875 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2dbc6c4-defa-3b92-91f4-6cc93639d4d1 | -13.20522 | -54.36866 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0aa091-cd68-3bdc-ac40-7f3b8e1b0651 | -13.19466 | -54.37056 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f43c2bf9-6c9f-37e5-94b4-bd0814919de5 | -13.1671 | -54.30764 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48269311-103a-395b-9493-e2c8e0596337 | -13.17581 | -54.36012 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e89eca2f-3f75-347a-b92a-4ee437feb24c | -15.10672 | -43.63455 | 2026-10-09 05:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 988328e3-6880-35b2-8cfb-89e7471e9b73 | -15.44303 | -45.44271 | 2026-10-09 05:06:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a275f4bd-2d2c-3f0e-b5c1-37e8e860c233 | -13.50084 | -44.37457 | 2026-10-09 05:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44ca9612-1853-39ad-8a6a-029ee71ed798 | -11.48659 | -54.6157 | 2026-10-09 05:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08ecf37d-58f4-36a1-a3d8-7b9144bb0b11 | -16.58941 | -46.75649 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26ac6050-0457-364e-8202-3f2a9bff2349 | -14.94641 | -48.10298 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00959921-4d58-39ef-b22f-b16243976e1a | -13.12176 | -46.3256 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc67565f-1953-3ff3-b345-b097fa5cee3b | -13.20189 | -54.36811 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e04a79-b9f9-32be-9e70-3002536d432b | -13.16306 | -54.35435 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 883b9990-3ab6-3ff9-bf88-c03b28cf9a04 | -13.17305 | -54.35601 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15be9888-6097-3e3e-a38e-9cf4a6e2a2ae | -10.98656 | -54.21886 | 2026-10-09 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b451d505-6fdb-3438-8585-1bec9ccdfcd4 | -12.23831 | -57.10758 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 470669e3-b5af-30bb-995e-5f45e0110b0d | -15.44701 | -45.43904 | 2026-10-09 05:06:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af81b286-bb8e-3850-8eee-87571fc03eb7 | -11.97058 | -57.61544 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1e27f740-c5d6-37a7-ac7b-3899254b0b81 | -11.74797 | -61.06985 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 35f0832c-965e-33da-a061-8531c7c552a9 | -10.67722 | -58.73478 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48b42b36-a51a-3850-a94a-b873fed88c7c | -13.15477 | -54.34203 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6670011c-e0b3-3241-8809-d0c0d432fd3b | -10.85109 | -59.11693 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65b35087-baaf-32bc-b142-ab3d46fc9734 | -12.23177 | -57.10199 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 020f9a8e-a7f1-3e5f-9340-b80841659298 | -11.78894 | -46.79424 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3fb0405d-c03b-33dc-a749-85d94b7ee945 | -12.81586 | -44.64493 | 2026-10-09 05:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e317a935-e338-3044-828d-b718eba0d068 | -15.21875 | -47.89518 | 2026-10-09 05:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30b28a8c-876b-31a6-a932-5541c1f8d236 | -15.56351 | -56.40584 | 2026-10-09 05:06:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9a85fd7-5a84-31e6-98a6-3bf85365b075 | -16.12387 | -43.75203 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5947809d-eacc-3043-a097-da182173db15 | -15.07792 | -43.11853 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 3b9c8ace-463f-333c-81b2-ffdae571403c | -12.22742 | -57.10561 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 31a7dec7-de97-3df7-9ab1-bbc4b4ae9700 | -13.50624 | -48.5999 | 2026-10-09 05:06:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 028944de-8ea4-3f55-a807-2e36c7e98772 | -12.21652 | -57.12576 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8733b661-669a-3103-9028-b00b7e888b74 | -13.20636 | -54.36155 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c8ac3fa-fa1f-3a15-869c-87d6046f0694 | -14.97022 | -50.38639 | 2026-10-09 05:06:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd5d3a77-0ba3-3fe0-82f9-895cbb275594 | -14.13548 | -50.34 | 2026-10-09 05:06:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67ad7618-bcc2-3776-bb30-5caa4335a02a | -15.78182 | -44.68421 | 2026-10-09 05:06:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd9bed10-4331-34a6-a7f6-345e8f51ea5e | -10.67434 | -58.73513 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db0adc1-b03e-3afa-8704-d0b381eee681 | -13.1919 | -54.36645 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f51d7829-198a-3169-bfd9-a83ae1fe7d5d | -12.22595 | -57.09219 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b0824277-ac43-3a92-8ec4-6cae48628751 | -17.36652 | -48.17598 | 2026-10-09 05:06:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c949be3d-5c7d-3bf7-a989-0683b9e6b2c0 | -13.1503 | -54.34858 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 875a4053-dbdf-3041-8b4e-8728d8fe649f | -13.17532 | -54.3418 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dbffb58-690a-3dc0-bed7-316d7e71abee | -11.98633 | -57.61359 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 536cdb14-97d9-3cf0-bce1-06cad80dbba5 | -13.16752 | -54.3478 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afc116f8-a477-3f7b-a8a0-9cc781e62203 | -13.18857 | -54.36589 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 478e4e15-d358-38bf-a961-2819b4f28a8d | -12.17656 | -57.0967 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d175360c-63af-3c81-90b5-001f6bbb63e7 | -13.171 | -54.30465 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 119d0c7e-2047-398b-9040-cf393a16df3e | -11.14735 | -54.80734 | 2026-10-09 05:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a5553d-d862-3a2d-975c-0ca71c78f5ed | -11.57517 | -49.7769 | 2026-10-09 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec2e2bd9-2eab-316f-b420-0ec5d586e8aa | -12.25193 | -44.75214 | 2026-10-09 05:06:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed83aa3c-78cb-30e4-8567-ef926ef85f1e | -12.20561 | -57.10187 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ac2ada-04f3-307a-893f-cbd00e699d0a | -15.95548 | -41.08054 | 2026-10-09 05:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b71fb0b9-36b7-381d-9027-74bb7bcb20f2 | -11.66401 | -56.76787 | 2026-10-09 05:06:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 824296b6-ab6d-3632-8c1e-c8a8127c9cb2 | -14.05303 | -43.82523 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 372c0735-c69a-3142-a37a-88f53efd85d6 | -12.19981 | -57.13593 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README174.md)
