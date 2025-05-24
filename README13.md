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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8890d4fe-6d6b-30a3-ba45-430adace16ad | -5.42713 | -49.08337 | 2025-05-24 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37d0ada-c5a9-3f2e-8768-ec3ada91d1d4 | -8.07274 | -47.12666 | 2025-05-24 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ba604f-d00d-319f-a9c7-216b082d50e6 | -5.57592 | -45.19537 | 2025-05-24 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdaee8c0-c71f-3ed8-8651-98f15744a9b3 | -10.37062 | -57.50203 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9985404-254d-30e0-aeea-cb4003f122ba | -7.0661 | -44.93507 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 881d5359-8aad-3700-9432-84bb59a843c4 | -12.07025 | -47.35284 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93ae2685-884e-3c3c-94f9-b8bfac002bdd | -7.6586 | -46.10472 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e32605cd-eb1c-326d-903d-268e267011a5 | -7.66233 | -46.10658 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2d55de8-75f1-3096-b652-660e49b98cb9 | -12.08087 | -47.34866 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b941a9c-b546-39a6-bdbf-b2343f38e9c4 | -6.49475 | -47.49189 | 2025-05-24 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb95c643-9481-3db5-9308-4032d5836e40 | -6.63328 | -55.01068 | 2025-05-24 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2602a7c-488e-3ed2-95fe-2ae662bb0fe5 | -8.75368 | -48.03429 | 2025-05-24 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 995d09b5-bec1-381c-bfa0-31476de84c20 | -6.23161 | -43.37037 | 2025-05-24 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb8300c2-c78a-3c6f-9b91-4ab3e59c4de9 | -12.0752 | -47.35357 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b87fbf9a-6147-3953-975e-d2e5022822cf | -9.92129 | -59.90839 | 2025-05-24 04:57:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7caf0269-2dff-39b3-bf71-b58b18e6e00a | -10.55125 | -42.43447 | 2025-05-24 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 402c7517-74ab-329f-a691-81f099e2c7be | -10.65949 | -49.4776 | 2025-05-24 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26b6678f-e547-3138-bcce-47bec5306e32 | -9.96642 | -49.80962 | 2025-05-24 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4658808-0158-3c8c-b9f6-c32fa061e6da | -8.07852 | -43.12196 | 2025-05-24 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d3f6ea21-99ff-345a-9892-ee10616ec272 | -10.2993 | -57.14121 | 2025-05-24 04:57:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afeecef3-740b-32b2-9c2c-6d636086fff8 | -5.68731 | -44.12374 | 2025-05-24 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0011bfa-11cb-3160-82be-c6a2b8882219 | -7.06762 | -44.93753 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb62c5cc-1a85-34e7-a110-9a9ecdb1163a | -10.76616 | -55.26447 | 2025-05-24 04:57:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cce1fbcf-8993-3269-8782-08eb9c4aceca | -10.3166 | -47.04685 | 2025-05-24 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a7c7004-7023-365c-ab72-b1904d36d9ca | -10.05529 | -59.35834 | 2025-05-24 04:57:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd267902-3ba2-38c9-af0a-7511ab67ef9e | -7.07345 | -44.93538 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07e31614-746e-36db-9ab8-5d0d6b416268 | -8.75304 | -48.03886 | 2025-05-24 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e072bc24-8519-34d1-9f4f-b7ee63bb42cc | -7.07146 | -44.93637 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1773a663-eb09-33ef-9e1b-cf2441cdcf61 | -10.30614 | -57.14235 | 2025-05-24 04:57:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 246d0e07-1a7e-39fd-8a75-38b049e19500 | -11.47438 | -48.02873 | 2025-05-24 04:57:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502ced97-243a-30f9-8826-ab6c459dd087 | -10.75847 | -54.7878 | 2025-05-24 04:57:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a39b289e-03f8-385a-b17d-a724f74dff48 | -6.69972 | -44.35652 | 2025-05-24 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f76ce15-1e44-381a-8eef-1819404e248d | -9.38057 | -48.40109 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f351729-985b-3939-a2cd-1ad69eeebfe6 | -7.20855 | -43.12965 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6226913a-d564-3a55-bdd4-d18f56e10b38 | -9.07606 | -49.66529 | 2025-05-24 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51650d16-bc76-39b5-94f6-3c0068c3d232 | -10.55562 | -42.43243 | 2025-05-24 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dfd36b5e-57ac-31b0-8c58-412910ac6759 | -8.75818 | -48.03497 | 2025-05-24 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f351b28-e690-37d5-89e5-397f4724ee83 | -12.07592 | -47.34794 | 2025-05-24 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 229f5516-a35f-35e3-83ca-eb1e44162d2d | -9.42043 | -58.30484 | 2025-05-24 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 223826aa-9c05-3029-99b4-aee543981bd6 | -9.80976 | -48.25703 | 2025-05-24 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e23690cf-e1a3-336d-b6bb-c403468d4b2c | -6.49542 | -47.48727 | 2025-05-24 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1b51da-5db5-3cfe-bf45-97a43f51133d | -6.63273 | -55.01417 | 2025-05-24 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372e2e4f-b5ae-3bc0-a7bd-d19d563e9ff0 | -7.19577 | -43.13328 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ae11c9f-2643-34d6-bd04-0aa938b200e1 | -10.36999 | -57.5059 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5681a069-9b0c-36d9-aade-424b4c283f7c | -7.65314 | -46.10683 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e80591f7-dbe8-3669-b325-009652d0ad46 | -9.81205 | -48.03679 | 2025-05-24 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee894441-7d25-3290-ad93-a8a4497b0969 | -6.21816 | -43.35415 | 2025-05-24 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d0ed6a6-09b2-3198-bdd2-b7cd7883f5ff | -8.31641 | -55.10873 | 2025-05-24 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30f8d40e-92f6-336c-b0d7-9256137399aa | -10.94733 | -48.15306 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b98137ba-4399-3218-b450-b009a78c5e36 | -10.93778 | -55.31704 | 2025-05-24 04:57:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e74608a-6aad-3e40-b945-ffc646a9a18d | -7.2086 | -43.13051 | 2025-05-24 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ac4feddc-515d-32f5-8000-d2cf819fabd0 | -9.4193 | -62.32436 | 2025-05-24 04:57:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afdcb25d-f9ff-3e00-8837-84cd31234b0f | -10.37087 | -47.98833 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 21a1e042-7187-3bc3-86a1-46d90c4761c1 | -7.07299 | -44.9388 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13861cc6-5496-32f1-9891-0330a6a81abe | -6.70176 | -44.35538 | 2025-05-24 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5a4de3b-812c-3e94-a452-827c23544fc0 | -6.49683 | -47.48995 | 2025-05-24 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 429108dc-0aab-3936-bf2e-9f7d574aa34a | -7.07194 | -44.93295 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11895167-1c9f-3052-a05b-5a48c403c405 | -7.8 | -46.2259 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91aea44b-022b-357d-a857-7fb5f9bccc59 | -9.77268 | -57.96188 | 2025-05-24 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d948ce5a-b848-38f5-a3bc-6aedb3269cca | -11.08312 | -54.77839 | 2025-05-24 04:57:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd7392ff-d1db-31eb-88bb-86388fe5f805 | -7.0685 | -44.93088 | 2025-05-24 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c7a3b37-247b-37fb-af8b-b382bbb1b2f5 | -10.36098 | -47.99177 | 2025-05-24 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 364169b3-d311-31fd-8f52-792985dacc82 | -10.37125 | -57.49815 | 2025-05-24 04:57:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88b26282-9005-37c8-9d86-45b429b80a74 | -9.96185 | -49.81265 | 2025-05-24 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2103705-c133-3019-8978-9ab4848ec28b | -10.53739 | -55.72135 | 2025-05-24 04:57:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ca97aa-cf8f-34ba-b722-0c3fabd2e54a | -10.53408 | -55.72082 | 2025-05-24 04:57:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 066a2017-e392-3926-b677-8e24a21edc78 | -9.42115 | -58.30055 | 2025-05-24 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cae668a-bbd7-3d74-ae03-8a89bc9ab71f | -11.56375 | -47.45229 | 2025-05-24 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7a110812-f037-3307-a25d-f6d5a6136426 | -6.70021 | -44.35278 | 2025-05-24 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 322cdf62-dd5c-31f9-9628-df8bf445c12f | -7.57688 | -45.86446 | 2025-05-24 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d51f0843-bffb-3f54-9d04-593ae9b6a032 | -11.14474 | -53.93156 | 2025-05-24 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae7cc849-2b44-3fa0-a385-cd30f3119fc3 | -10.03168 | -48.70108 | 2025-05-24 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6ff194a-21c5-3992-b9e1-3bfd9be71291 | -9.09082 | -49.64904 | 2025-05-24 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 967673e9-857c-3d49-b3f3-9efe55fb36c0 | -14.03031 | -55.13525 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7154e64-8033-3792-a50c-904a12e540d3 | -12.37059 | -54.89673 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3174145f-a2ff-3a13-a75b-6c0871938227 | -13.37421 | -54.26324 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2717733c-7f8c-34dd-8280-0cc41bd8d3b4 | -12.40381 | -49.98791 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3336939d-17c0-3fd8-8845-e995388b3358 | -13.85134 | -59.72371 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b21cac1-1252-3e8a-876e-c8150af28e3c | -13.78442 | -54.3115 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e086873-49d3-3f4b-a4f5-7afd54779fed | -12.66898 | -58.21501 | 2025-05-24 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4ee11a5-57b7-319e-96d0-1c90b8458a2a | -11.75145 | -54.23248 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 723321d3-3ee9-3b85-9087-f6045c9d4e2d | -13.86533 | -59.73093 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bdf3a61-8536-32ca-aef0-ae873ecb04f9 | -13.85327 | -59.72123 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 984ff007-8331-323a-88f7-6e63aeabd9f3 | -13.15748 | -56.81822 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 16b715c5-c5c3-3c69-908b-bb084da1d7ec | -12.84142 | -47.39148 | 2025-05-24 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dc13f1f-3ac1-337b-bed5-a07548a5e754 | -12.38414 | -49.99339 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e18363d-2738-3314-9897-fad20c549adc | -12.13881 | -54.65638 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4db6785-001d-3f6f-99ac-643ea34fc9cb | -13.85583 | -59.71985 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d784c6-1abe-3526-8306-0b257621218d | -13.47289 | -52.28344 | 2025-05-24 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ad80ea4-8608-3499-8f11-703503f1c8cb | -13.15415 | -56.81768 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a4432bca-63ce-3274-b009-91e3bb664bb7 | -17.34327 | -51.90859 | 2025-05-24 04:59:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7670635b-5726-3161-86fe-dd8f1adb9503 | -12.83534 | -47.3967 | 2025-05-24 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 245d3fe1-3c92-3b52-b35c-a795438ca3dd | -12.40651 | -49.98496 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 083e01bf-1308-30a0-b3c9-4416e3935f2c | -13.98864 | -56.01963 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49b19038-38db-3899-893f-192ad00e19fa | -12.41908 | -54.38075 | 2025-05-24 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6610180-9808-3fc6-addc-a9a1fa76f585 | -17.15795 | -54.00369 | 2025-05-24 04:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1be3ab41-417f-3da4-9d31-e2f88b6ac923 | -14.02754 | -55.13113 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5660c6be-be3d-3618-9862-61d1d2dcb251 | -17.15737 | -54.00779 | 2025-05-24 04:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83d9b905-fbee-3295-a2c2-931acc8b3675 | -11.36213 | -55.12815 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ebdfe68-99ed-3cbc-a869-c4f3fd67277a | -11.75869 | -54.2299 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README14.md)
