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
| d1fa3a82-bedd-3553-b971-1542abe109b4 | 3.18675 | -60.11908 | 2026-03-17 07:16:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 781eed73-72b4-39a4-b539-edd519fa3a6d | 0.84166 | -60.33999 | 2026-03-17 07:16:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 646898aa-1369-3aad-bbb1-0cf45f274954 | 1.33222 | -60.69993 | 2026-03-17 07:16:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9109e28f-0f64-3b31-8368-cdd18e02704c | 3.12354 | -60.75153 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 11a1b6ea-f001-3517-981b-f578f4554ac0 | 3.12488 | -60.76043 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 24.6 |
| fcd816b8-0bcf-33ad-8c96-b57ff960326f | 0.8316 | -60.33259 | 2026-03-17 07:16:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 160f1791-3afe-3cdb-a17c-7156e801d76e | 3.19681 | -60.12651 | 2026-03-17 07:16:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30b05e1f-261a-3f87-a8c5-cb530fd286bf | 2.742 | -60.43567 | 2026-03-17 07:16:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a020b5ae-378f-3475-91cf-b9aaa6443e38 | 0.84034 | -60.33131 | 2026-03-17 07:16:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6d78638c-0299-3d33-8b72-17bb559321f0 | -16.44541 | -58.1697 | 2026-03-17 07:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| bcea2517-6149-3263-bed2-4aa7b9863748 | -5.52782 | -36.8598 | 2026-03-17 11:28:00 | TERRA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ae320547-6353-3c86-9abb-7a55f8d17106 | -12.66152 | -38.9228 | 2026-03-17 11:30:00 | TERRA_M-M | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a7656b62-ef02-3fd8-a8bd-9c4a0f50e307 | -10.54021 | -40.08067 | 2026-03-17 11:30:00 | TERRA_M-M | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f398d470-ca6b-3818-bef8-ef3cf5fcd250 | -8.55741 | -37.01346 | 2026-03-17 11:30:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fa05bd29-2894-3712-b3e2-2840bc6dbc63 | -13.85766 | -39.46897 | 2026-03-17 11:30:00 | TERRA_M-M | GANDU | BAHIA | Brasil | 2911204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d7c9cbc1-14a6-3943-94b9-829f4a506360 | -12.6628 | -38.91369 | 2026-03-17 11:30:00 | TERRA_M-M | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| de37ff46-35c3-3016-bf39-9314fc113e41 | -13.5476 | -39.8937 | 2026-03-17 11:30:00 | TERRA_M-M | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 43cbd9d5-151f-359c-aac0-fc0217da70dd | -10.52874 | -38.35294 | 2026-03-17 11:30:00 | TERRA_M-M | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 876cb9f8-5053-34f3-8597-3449d58fc47b | -9.73434 | -37.16324 | 2026-03-17 11:30:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 17.5 |
| ca34e9e2-77f0-35f1-8798-1da285b518a5 | -10.97995 | -38.82207 | 2026-03-17 11:30:00 | TERRA_M-M | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a883c2f2-c3ee-370a-bb54-491a760f8027 | -9.48121 | -36.94265 | 2026-03-17 11:30:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 16.7 |
| fcf3b9aa-24b9-3cb1-acca-50d1e3bcbae7 | -10.55958 | -38.97812 | 2026-03-17 11:30:00 | TERRA_M-M | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 12bc58d1-65aa-3bf4-a44f-6b4491f1b3a1 | -19.09948 | -42.13886 | 2026-03-17 11:32:00 | TERRA_M-M | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


