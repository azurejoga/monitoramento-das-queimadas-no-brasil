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
| f7dc6712-6ff0-366e-8e17-61fd2e6292e4 | -11.37271 | -46.69552 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 048506dc-cd5b-36b9-b9b1-fbed8465953e | -6.84206 | -58.59244 | 2026-10-07 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10b3b99f-4029-3b7b-ba92-b2ded8341e35 | -11.37899 | -46.69196 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29ef00f0-1593-3236-ad7d-3138a1229516 | -8.14816 | -64.07479 | 2026-10-07 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d755534-c519-38e0-ad0b-20793978d7e7 | -9.8028 | -48.92085 | 2026-10-07 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2ab0472-fef5-340f-9262-1b850b178a8f | -11.37318 | -46.6916 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08e9aa84-e613-3fdd-aebd-1f735d9562dd | -11.50297 | -48.47672 | 2026-10-07 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8543d8be-ec6e-38bc-b0d4-4fc3989043a3 | -8.53244 | -55.37388 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ccf357a-4972-3568-a47a-efa50ba8ec73 | -9.11941 | -67.82925 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ccc8cb3-4a02-3653-96db-866bdbd6ee94 | -8.53861 | -55.37469 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d0c8250-a70b-3a0e-84a8-6b29d028ef32 | -8.97539 | -67.51033 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9daeaa7b-7a59-3b3d-9aba-a9f27c569be0 | -6.84617 | -58.58913 | 2026-10-07 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 595285f0-6fa3-38cf-be83-681201daee80 | -9.14343 | -65.3009 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 851f53e4-8225-3114-8e5e-58304e395086 | -9.10725 | -65.35497 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46e2b714-3d6e-34ac-be9e-a006fa1cd028 | -7.89706 | -54.72167 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25cda1f9-5fc7-3d9c-a8a2-e22fa307f25d | -9.15571 | -65.94554 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 90952635-3b79-3082-a957-ad0288062ddd | -9.06271 | -65.48267 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f92d369-9d0f-3be0-8594-e2647a6ead0e | -8.28841 | -50.27432 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 43cd6828-b57c-3a99-b51f-511682800b5b | -9.16104 | -65.94648 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0200fdad-d91b-338e-a091-704bb9881957 | -9.09099 | -67.68349 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a095bafc-054a-3e19-8f66-6873f9f7681a | -6.95199 | -62.94276 | 2026-10-07 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78965feb-0090-36a4-a11f-51dcd4c35ffd | -10.99707 | -45.42267 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a21b0fc-6306-3cc9-9b2a-cc3427fd8c2c | -10.48317 | -50.42706 | 2026-10-07 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 686aa52d-6802-3145-ab77-8dead4b548e1 | -9.11295 | -65.35278 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 779cb7d4-6eea-31c1-b65f-ca63cfcd7f8b | -11.70833 | -43.66205 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2ff3d492-6aab-325d-a19f-b9bcc822d01b | -8.9101 | -49.97419 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca27dd54-8f82-33d6-842e-3ce7464f420b | -11.33427 | -46.66544 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b3aae83-71d2-3a9c-88b4-138ca6e923bf | -11.37364 | -46.68774 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39ea9ec5-dc0d-3994-82fa-c2630a98d99b | -8.97619 | -67.50597 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307babfc-5937-3c88-b72c-fe5143287f46 | -9.23657 | -67.88729 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5e4583d-7dad-33b2-9416-8c43a59d95e0 | -9.28992 | -67.90225 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0529501c-379e-37ec-a907-257ad449594d | -13.18029 | -48.14001 | 2026-10-07 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92a3faea-109e-306f-99a6-1697c963d988 | -9.2691 | -50.66533 | 2026-10-07 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85ff9c48-d4e4-347f-87d1-c1c338977a47 | -8.69213 | -68.71352 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5b4568a-807f-324c-8780-51c947e8fe02 | -8.53527 | -55.37418 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a399bff-021c-3ffa-b8ca-36cf99515e73 | -8.54195 | -55.3752 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26f71ac7-d908-3c42-9eef-910aa99c8a46 | -11.22661 | -45.26944 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4db40dc5-7c36-3cd7-8eb8-9c2dd9bfcdc7 | -9.52111 | -54.73954 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0cadedf-0064-3240-8293-3ad75ab1a6f6 | -8.74833 | -47.87685 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54bd5ce0-35f8-3a65-ae64-bea81afda1c8 | -7.75159 | -54.79236 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcef99bb-597e-3bd9-bf07-b5db69c8ccf5 | -9.51713 | -54.74277 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50d8a395-ea64-348b-b02c-6a8c74977080 | -10.85742 | -50.68413 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a789d3a4-66da-3bff-9a2a-0638f7b81c6b | -9.51769 | -54.73903 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e593ca51-d1ad-3e9e-8d8a-2b513ed92a46 | -7.74729 | -54.94667 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c9dc05c-746b-3e46-89be-7ac98d6e9d44 | -11.57832 | -48.4376 | 2026-10-07 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1468d03d-7dd1-35df-a98c-0bc56fc59ceb | -13.39285 | -43.87711 | 2026-10-07 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5282a0f4-b0c7-3470-ba68-43381543b30b | -9.11519 | -67.82842 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fae4479-764c-3f14-9944-706998436a9a | -9.16327 | -45.11499 | 2026-10-07 05:06:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d41b676-2e64-3ea4-89b6-3834f1066f10 | -10.9811 | -45.41093 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20bb8a14-a8a8-3d54-be85-28dddd00fe4e | -9.60941 | -67.4822 | 2026-10-07 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c56c33b4-49a8-36f0-a3e7-17dfda0dd78f | -11.33505 | -46.66687 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88ae4633-ee74-3682-995d-2fcce7773f9f | -11.67708 | -43.62556 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3184dc64-1057-3901-b410-d3ba6c5593bc | -9.87928 | -44.80304 | 2026-10-07 05:06:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f55f4c-9f53-3ff9-ad22-7f16625f85e9 | -9.33567 | -63.6791 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0af9f989-b3a3-3ce7-bfd7-14f7f0400d3f | -9.50723 | -67.16476 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df954ffc-6304-3fe3-89d5-5d7dfcfca709 | -10.86236 | -50.68047 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dd403aa-e81e-347e-93a9-487459e1fe56 | -9.87682 | -44.80332 | 2026-10-07 05:06:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc0bcd9a-4ac7-3a20-843c-f0137191ea2b | -10.13329 | -46.84781 | 2026-10-07 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33280cd9-ffd6-37d5-a0b5-242893db47c5 | -7.44703 | -55.57546 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8af15a18-7148-3221-a340-712b6a3f129b | -8.289 | -50.27015 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 30f14c97-6fc9-3083-a2dd-7626560c2af8 | -10.6196 | -60.48483 | 2026-10-07 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39159752-63db-32f3-968c-5da107540056 | -8.63421 | -67.05382 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02907e06-0881-3483-b27b-3ce829547062 | -10.97972 | -45.40875 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d6c85e-a337-3b10-8b66-9ecd25792762 | -8.54249 | -55.37165 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75cf70b6-cc33-320b-9ad3-b3c5970ad293 | -9.47172 | -62.38538 | 2026-10-07 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1399d5e1-6404-39f5-826a-4aaade1a09ca | -9.21138 | -51.87845 | 2026-10-07 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca9ec7ce-a0ba-3578-8e4c-9fb6f7c2fa29 | -10.96786 | -45.40197 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae249b84-273c-3f87-b0ae-734d8ccc463c | -9.15759 | -65.94688 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 440df640-e164-3e14-9f25-8c623f6dc42e | -8.63344 | -67.0579 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5358b70-52f1-37dc-a139-467fcc0cd964 | -10.22157 | -44.64271 | 2026-10-07 05:06:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22133136-0176-3b17-a37c-242acad04edd | -13.50435 | -44.37017 | 2026-10-07 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7e52245c-f9b5-3ea4-a787-1a316fd1f72c | -12.47511 | -51.28961 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44f40343-2edb-39f1-8e98-928e066152c4 | -10.61887 | -60.48919 | 2026-10-07 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b56645b-0c79-30cc-ba64-14da5652508b | -9.52583 | -67.41653 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd251f5c-010a-3b26-b667-6984bbe9adfc | -11.75364 | -44.93642 | 2026-10-07 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a766b888-6db3-369e-a223-09c24e0e3daa | -11.36637 | -46.69969 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c0e9c02-2c03-3615-b3b3-f8c3e5d60522 | -10.47875 | -50.42643 | 2026-10-07 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f4aa05a-0bca-34ab-b09a-9a5672426071 | -9.52 | -67.41546 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e236da-e462-30a5-848d-a0e86cd60f57 | -9.13431 | -65.29292 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f91b6dee-3b3b-3516-8289-3904b56fedbd | -7.74955 | -54.95436 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad32d18f-9914-3761-9d52-76a9dec093a9 | -8.74618 | -47.8752 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26d44442-2d82-3660-b1ae-e5601b9ef597 | -9.22788 | -67.89208 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb37b2e2-e18c-34eb-abbb-1d97b1727a5a | -9.1604 | -65.94993 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2732003f-f788-3f5a-9e2a-aeaa9fe56d8b | -10.97919 | -45.41338 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2d60ff-5e9c-3507-9488-921af4b23395 | -9.14972 | -65.94802 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4e90016-9df6-3be6-b529-562dd80d5c58 | -9.25791 | -45.64415 | 2026-10-07 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c028c7b6-90fc-3884-b9cc-79973931cd45 | -7.89761 | -54.71802 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07cea278-08fa-3791-a4fa-67a01c34c762 | -9.1665 | -47.58191 | 2026-10-07 05:06:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b3b30a8-30b7-3d9f-9151-93cf194bf80d | -9.23733 | -67.87481 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e544fa85-0002-3025-bb12-a2a38e07d1ee | -9.51657 | -54.7465 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3c14c1-66db-3d4c-8362-50b0f4738eef | -11.00773 | -45.43947 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0d4f0db-4785-3e57-9af4-767ac1bfc484 | -10.4876 | -50.42768 | 2026-10-07 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ef936be1-43bd-31c9-83cb-5557de523b38 | -9.22966 | -67.89072 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 03973908-4d83-3ac1-87d7-08c2dbc7da75 | -10.85207 | -50.6571 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2000e67f-ca56-331f-80da-29053227ba0f | -9.14378 | -66.05473 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d3b5995-8cd5-3d55-a8dc-8c0e2ba60f2a | -11.3812 | -46.67345 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a2dea3c-e2e9-3f54-9dd4-0d975041e454 | -9.29055 | -50.31463 | 2026-10-07 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c63443-9504-3748-b180-ef621384b50e | -9.55031 | -64.8148 | 2026-10-07 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b23f1dbe-1c0f-37c2-9431-bde3b25b62e9 | -9.44102 | -67.09921 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022a01bf-872d-3e85-947c-3ad20c5a2df3 | -12.08251 | -48.11728 | 2026-10-07 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README95.md)
