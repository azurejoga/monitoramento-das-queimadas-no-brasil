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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d31c80-0868-3b83-a44f-5304702b4690 | -12.4875 | -45.4434 | 2026-05-15 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 713caf61-a394-34bc-92fe-6f927cd19ed9 | -12.6205 | -44.5179 | 2026-05-15 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7e67d421-09cb-31d9-8202-c46080eef955 | -12.6205 | -44.5179 | 2026-05-15 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 79893ab6-451e-31b9-9f67-f723ede7c441 | -12.4875 | -45.4434 | 2026-05-15 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 96d34cf1-5dd8-3007-a5fc-14fbe0803230 | -12.6205 | -44.5179 | 2026-05-15 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 287d4502-ba8a-30fc-9715-a03231200e2a | -12.6205 | -44.5179 | 2026-05-15 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b67fc049-d57f-3deb-b531-9a6fa3023ebd | -12.6205 | -44.5179 | 2026-05-15 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 562b436a-fdbe-31d8-a2a4-96301443c646 | -12.4875 | -45.4434 | 2026-05-15 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ad3f336a-2e65-3f42-9036-a8068e0bbe0c | -11.7561 | -44.513 | 2026-05-15 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fdf3df35-fe9e-39a7-be1d-7a4b30eb4670 | -8.7211 | -48.3222 | 2026-05-15 14:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0b614037-b0ff-3c6e-b3b7-72c000e6548d | -12.6205 | -44.5179 | 2026-05-15 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7f7392e4-d203-3976-8d80-2fe1cb32fdef | -11.7561 | -44.513 | 2026-05-15 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2733b654-45f9-3b7a-8cfb-ddca32be2600 | -12.4875 | -45.4434 | 2026-05-15 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 165ee738-0cda-36b1-9119-b7a7270b9470 | -11.7369 | -44.5159 | 2026-05-15 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 05d89d58-1ae2-38e0-94f2-ec913630ba92 | -12.4875 | -45.4434 | 2026-05-15 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dab3199a-6390-34e6-b219-3abc171fad33 | -11.7369 | -44.5159 | 2026-05-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7523bc73-24e9-33ca-9ddc-e19d65bf59e9 | -11.7561 | -44.513 | 2026-05-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2d1980d9-0d95-3ad4-b2d0-bf70cf8c9e3f | -11.7369 | -44.5159 | 2026-05-15 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b51bb708-5a6f-37c8-a827-bfd7bbe87ce0 | -11.7561 | -44.513 | 2026-05-15 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 5221c10e-c15c-3553-a2af-4b6ad4d12c54 | -11.7561 | -44.513 | 2026-05-15 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a78f91c2-3869-308d-9276-f7ad667d51ea | -11.7369 | -44.5159 | 2026-05-15 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b459c9ef-6277-36aa-9eb7-f81a60a4e20b | -11.7369 | -44.5159 | 2026-05-15 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d9b902f7-fc4a-3297-b1fe-7528c1bf3921 | -11.7369 | -44.5159 | 2026-05-15 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |


