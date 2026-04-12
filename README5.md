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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c27c144-20ec-3e92-8222-ff1098fb34c9 | 2.0977 | -60.53009 | 2026-04-12 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc993ac4-3079-3678-b0d9-9032a75e3f78 | 1.37799 | -60.65741 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44361a9e-da9d-3038-91df-e0d1c8965762 | 1.65206 | -60.14199 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6c8c704-5e73-3cfd-85a3-2613893d7ea9 | 2.37092 | -60.96523 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4590553-d944-31cf-a6d5-062ceaa90aec | 2.1083 | -61.25497 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d3441c3-fdb8-3dbf-bbfe-b45c6544ddb8 | 1.37092 | -60.65855 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eaffe7b9-5edd-3a44-99cd-d1f2dc2754b8 | 1.28106 | -60.31376 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40976c28-3d56-3227-ba17-4ee694a19ab0 | 1.35034 | -60.66588 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6402f535-7c93-39e5-a2e4-7ff6fc9a3af6 | 2.02391 | -61.09853 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| abc0bd75-b82a-359e-8a4e-d07fe5401b76 | 2.3697 | -60.95764 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e76b28-6594-3f85-99c1-b131ef4361ec | 2.01987 | -61.0953 | 2026-04-12 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4b9e4a4-8c58-3e88-a4f3-038ab89383fc | 1.27746 | -60.31433 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9b851a6-b695-354c-a9aa-a20dc40f4c48 | 1.36122 | -60.68858 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81fa21b1-b3fe-3290-adc4-6fdcfdd8e5fe | 1.27938 | -60.32672 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f487c994-ce99-3a9a-b0a5-2f16eea84478 | 1.28509 | -60.32758 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34b3b46a-f8d8-38ed-a66a-49a9ce107fde | 1.27321 | -60.31076 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd802ff-1957-361a-9efc-01793a9a3fc7 | 1.37572 | -60.66594 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379db52a-9633-3e95-aa9c-073dca55fd56 | 1.3809 | -60.65286 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df1dcf19-f8e4-3216-b536-c548917fd2ac | 1.90493 | -61.10101 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75ea922-6907-30d0-bf91-de5807f7dc5d | 2.53344 | -60.35113 | 2026-04-12 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82dd7f86-fa5f-3b02-932f-d8c5a32d6feb | 1.37282 | -60.67047 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af512115-05a0-315b-8612-5fdee378d496 | 2.66815 | -61.17622 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86e8213b-3b41-32d0-b49f-cdc1dea13585 | 1.34617 | -60.66247 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5a88606-5a10-3f3c-8400-8726af1c6e9b | 1.30215 | -60.65976 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f401880-b122-3a1d-83bf-1c808b31dff2 | 1.28658 | -60.32559 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c02ab12e-ad52-312c-b765-b4a4ef5d1b25 | 1.28234 | -60.32203 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d4257fd-7c93-3eb5-bc60-f456787df4eb | 2.37783 | -60.96414 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dca05e42-2e19-39a7-89a2-92a1011ebe99 | 1.28309 | -60.3152 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e970f07-a806-37e6-869d-2d2050da4c96 | 2.37316 | -60.9571 | 2026-04-12 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e5e8399-8e80-35dc-9a90-7d2185611586 | 3.91681 | -61.64817 | 2026-04-12 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce6d6e0-6d32-3589-842f-9fd9a6eb679a | 1.16339 | -60.67634 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c33122d-d559-3d10-868e-fd8b257bfcf9 | 1.37219 | -60.6665 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fec5c795-afc6-31c1-88e4-b0f4be44407f | 1.37446 | -60.65798 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42101bfb-cce4-3820-bc35-44a9b6c2da70 | 1.27874 | -60.32259 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3299671f-1900-32f3-bc90-7031d4056506 | 1.70514 | -60.31575 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6e39dac-b8f4-3b85-8fa1-5850098b9fb0 | 1.34681 | -60.66644 | 2026-04-12 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bf88fa0-26d2-3c88-9df3-92f1b7ca1c70 | 0.42356 | -60.50982 | 2026-04-12 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97934d07-2822-3e13-858d-36e0a89c3d10 | 0.42716 | -60.50925 | 2026-04-12 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54dd7ae9-927d-3c73-a537-570008066842 | 0.42652 | -60.50512 | 2026-04-12 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9516105-c7cc-3b53-8732-e6991e810ddb | -12.97381 | -54.68433 | 2026-04-12 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c7ab813-7bcc-3790-a4c9-5671aef9ce8b | -12.98016 | -54.68514 | 2026-04-12 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36f9fefa-5eb8-3f09-ac66-644aa50a8d9d | -9.66208 | -65.72849 | 2026-04-12 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec69749-c061-354a-9ce7-982b1634987b | -11.20338 | -56.87889 | 2026-04-12 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8b363e3-b720-3e77-878b-f34e80e5e3c4 | -11.20379 | -56.8755 | 2026-04-12 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4538876-8d32-3989-9fec-5def23ef33de | -11.80134 | -43.62264 | 2026-04-12 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| adfd592c-9cec-3102-bf49-73e5a2f09fe1 | -9.80199 | -37.46387 | 2026-04-12 05:53:00 | AQUA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 187ce818-0178-3512-a160-6c9e8e9bf3b0 | -11.7941 | -43.61468 | 2026-04-12 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d7a0330a-394f-34d8-af0a-bd67148ac6d7 | -9.80056 | -37.47389 | 2026-04-12 05:53:00 | AQUA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 5db139f7-0b53-32e2-b725-36afb2841412 | -11.79933 | -43.63473 | 2026-04-12 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 53c918fa-4088-3a46-983f-818f5e7e2140 | -11.79121 | -43.62098 | 2026-04-12 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ed99b9d2-16fe-3921-8907-bbb287fa9059 | -11.79216 | -43.62679 | 2026-04-12 05:53:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 32af6c74-8f0c-38f3-850a-ccc9260b45a6 | 2.03501 | -61.09658 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2afa22c2-4503-3a69-a98a-9534638d0ebe | 1.37062 | -60.67065 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 268c623f-689a-34bd-8666-c15b4cbe8f68 | 1.37491 | -60.66285 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18401830-3f7d-3727-b306-7f539295a6bc | 2.6741 | -61.17469 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b42136d2-3cc9-3ac7-9beb-39855a840f88 | 2.0182 | -61.09665 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fab4ca1b-acf9-3d11-878d-c70255364bb3 | 2.54119 | -60.35254 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dc3f53-eea2-37a2-944f-c8c9637ae00b | 1.2795 | -60.3184 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca41bd22-f855-3649-bb54-5330773a4236 | 1.37976 | -60.65844 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34b2eeb6-6775-3edd-b6c4-15d7b886f384 | 1.27275 | -60.312 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a650a48-0a4a-35a5-945a-867918442f0b | 1.3062 | -60.66109 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f35da6-bc26-3ab4-94b9-d6e50d3f97c1 | 2.37633 | -60.95755 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfb5da89-3487-3409-8420-9d08848be6e3 | 0.42673 | -60.51162 | 2026-04-12 06:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74fdd587-14fd-3c35-b79e-67781a450401 | 2.03553 | -61.09972 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41ce488c-615b-38f1-b43d-6196aae77f1b | 2.53739 | -60.35372 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dc27846-f738-3bf2-9c53-1460d4320c3e | 2.01834 | -61.0928 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d138cc7-78ad-3a14-bf13-fa532fba3edd | 2.09701 | -60.52885 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be336d95-2db1-3641-b286-103724b56f5b | 2.01887 | -61.09597 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a18131a9-7d04-36df-819b-a61dceac3e55 | 1.37436 | -60.6594 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b90305e-2990-3616-8030-cd2a1dd22f1a | 1.30078 | -60.66197 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e5b6d7-bfbd-34bc-b7ba-dd122b09a744 | 2.67181 | -61.17763 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f7c0fa7-add2-3e98-88bb-4fd6b4f5982b | 2.02927 | -61.09425 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f041b2c-a40f-3f46-a35d-cd455aa28b21 | 2.02512 | -61.10139 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce24e079-8467-3b92-ae7a-a963b33fa9c0 | 1.35326 | -60.66646 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2110fd04-9324-31b6-be3b-34a0b70223ea | 2.01719 | -61.09032 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47f56c5b-6cf4-3e06-8e24-a6a72c334fde | 1.27215 | -60.30832 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a716e95-eb12-307a-b250-189166e4d0dd | 2.37111 | -60.95844 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dccd909e-fee1-3f90-8877-c9194e8dfab0 | 0.42613 | -60.50797 | 2026-04-12 06:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac28c5b4-64e2-3710-8e6c-61c54598520a | 1.30221 | -60.66049 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a61fa3e-9351-3b09-807f-f49a9b4cd94b | 2.66898 | -61.17558 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 762abed5-e25a-38ad-97e2-fb02dcbbe13e | 2.09756 | -60.53218 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7cea132-17ee-343e-9b88-94b63a7d4685 | 1.37006 | -60.66723 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19822080-2e65-3326-8a05-6770c3ca617c | 2.01769 | -61.09349 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2320b92e-9746-373d-aac0-8975943fc891 | 2.02354 | -61.09192 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c215c31a-aae9-392b-acfd-ff63d51342f8 | 1.30763 | -60.65962 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afb9827d-8200-3406-a05b-a9d00212dea5 | 1.27891 | -60.31477 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 633bd649-e881-3b4b-b06c-728b55925b9e | 2.0298 | -61.09742 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53ccd313-66d0-3333-aaf8-08aa4dc03f2b | 1.3738 | -60.65594 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 321b75c4-65bf-382c-a65b-9cbfbd2e39d8 | 2.02407 | -61.09509 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a86ef164-f550-37e1-aeb3-d70253313ae1 | 2.38249 | -61.4578 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7e448d-c0e5-3163-b507-f59fef46ea7e | 2.0246 | -61.09826 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b3c56fd-aaef-3f27-9537-aca39d7333d6 | 2.38201 | -61.45484 | 2026-04-12 06:12:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1e8a3a-66ea-32d1-8239-975e6d6f49ed | 1.35606 | -60.68365 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2146eee8-e065-32cc-9c9b-366766074018 | 2.53681 | -60.35028 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f4a6969-24a8-3f64-97cc-6010854148ac | 1.37547 | -60.66628 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b980da2e-893b-3123-ac3d-ef5823df293d | 1.34729 | -60.66395 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d27420a-afae-3290-b65c-c35236a75a26 | 2.53577 | -60.35351 | 2026-04-12 06:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d1cdd84-8e40-371f-99d8-237619dc37ed | 1.21551 | -60.44505 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddd9ae04-6f58-396d-81b0-268b14d35a1b | 1.35662 | -60.68708 | 2026-04-12 06:12:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 558565f0-687c-32ec-9507-37d2b2115ff4 | 2.67131 | -61.17465 | 2026-04-12 06:12:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
