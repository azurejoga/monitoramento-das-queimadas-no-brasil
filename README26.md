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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17b59b65-c621-3937-840f-cfefa6e1756f | -11.1638 | -54.88188 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b660a40-44a2-386c-ad6b-f37e014dfba7 | -11.20252 | -54.91639 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb8ecaa1-003a-3023-8239-b5a2370f4a46 | -11.18131 | -54.90223 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ce0e485-7dda-31c0-8050-246df2964482 | -11.15968 | -54.86926 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86ce7e08-6738-3f35-a9bd-5e8c8c7b2200 | -11.21384 | -54.91772 | 2026-08-05 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ade1eaa-02f9-3096-bd21-f88205539441 | -11.16618 | -54.88501 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0654348f-1d46-34cf-8f4e-0f8a6e5137fe | -11.21057 | -54.89793 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b41fae6a-3298-357c-81d8-a4a62f38bcb1 | -11.19782 | -54.90805 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 265b231c-5450-383d-b1a0-6e9e2afba45a | -11.16995 | -54.87882 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74453172-7b9f-38fc-8e0b-d550bd6d778a | -11.19885 | -54.85325 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17b99102-4a5f-3403-85fc-7654fc77f813 | -11.19688 | -54.91562 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea71572f-13d7-3b02-9849-61b643ac7145 | -11.1851 | -54.91805 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb2f4a2a-cffd-3c00-9c39-8d2394b8dabe | -11.18744 | -54.89912 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed4eb22f-4d15-309f-80d8-d0de4f53e3fe | -11.18084 | -54.90604 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f7fdca9-9b37-3bf2-8a53-bb163a119f84 | -6.7227 | -58.92941 | 2026-08-05 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de3dde08-0d7b-3c6b-b94f-c4170f1a2433 | -12.16777 | -59.75558 | 2026-08-05 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27fac238-acaf-3e81-a07e-eb5bbbe69577 | -11.16435 | -54.90001 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79d3041f-bdb4-3a27-871e-bdf16dc1ebd9 | -11.19739 | -54.86508 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b376010a-89ec-3785-b96c-f471704bc191 | -11.16298 | -54.91122 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b2e6a8ca-8598-3bcb-a508-2ebbc66b0cfa | -11.16896 | -54.88652 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96731b12-c4b5-3291-affb-65aab19acd16 | -11.19216 | -54.90738 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ec8dbbd-14fd-3b78-a327-dd5d0338de96 | -13.24546 | -54.27211 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3d585d3-5523-367f-99e2-f6e64ac25ad6 | -11.17892 | -54.87487 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 763f0a4a-c2f7-3796-83ca-b172c09c3c57 | -11.17 | -54.9008 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ffc60cf-f01c-3ab9-ad68-09a81ae67038 | -11.19122 | -54.91496 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b992c7b4-929e-3ab5-af32-f3bf19a7b719 | -11.21008 | -54.90187 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a6ea2fc-c1b6-3fbd-9cf7-937e8b54fbf5 | -11.22046 | -54.91071 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86318a7c-3267-310a-b3bf-359a635b5cb8 | -11.21949 | -54.91841 | 2026-08-05 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ecf53de-cdf4-3afa-9a28-9caad5156722 | -11.16702 | -54.90145 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 83e3db8a-a702-3000-9a83-42f662df890a | -9.28287 | -60.64743 | 2026-08-05 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa88a611-01a9-3ba5-9385-e1b5fe2884f8 | -11.18412 | -54.87934 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04d8166d-7d17-3317-ad0c-62bd8943d98b | -8.38359 | -63.98146 | 2026-08-05 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba1b86f7-9025-3aa9-abfc-8d5a1de13091 | -11.19829 | -54.90424 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74a9777c-0850-357e-b864-f6b59af8bf45 | -11.22576 | -54.86854 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aacf9802-fe51-351b-9743-dca03bbb1672 | -9.48739 | -57.32468 | 2026-08-05 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 762353f7-4df1-3f09-ba07-8554319bc611 | -11.19358 | -54.89588 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f035d57b-8c09-3b18-b953-df818345c626 | -11.22672 | -54.86093 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a931ac5-b266-3a22-ac8d-819269ca06b7 | -11.16431 | -54.87798 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bad5b35-9ddf-3038-aac5-1dd125dd8791 | -11.19924 | -54.8966 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b303d1e0-2c43-36f2-a65a-f2f344d1b6e6 | -11.16606 | -54.90891 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dff54cf1-4650-31b0-ba49-1ec7c51c9d69 | -11.16751 | -54.89772 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5aa8f87e-f076-33ba-b901-8e33bf52bfe9 | -11.18606 | -54.86359 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3298c5a2-00c0-38da-a46f-e08c70fff6db | -11.92521 | -55.91079 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bbb298f-3c87-35af-b4e0-c61c9c275b24 | -11.18037 | -54.90985 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8cf8b450-16a4-3826-bcbc-ed726ea604ed | -11.16799 | -54.89399 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cb0bb5c-1d8b-3b39-a937-ce248051b2f5 | -11.16148 | -54.87637 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 808dd47c-bc60-39c6-b4e7-381bbaec4099 | -11.17097 | -54.87099 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6ffc75b-ed6f-373a-a52b-c48799149443 | -11.1775 | -54.88642 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac282d5b-6679-3081-b5ec-525c13454a18 | -11.21575 | -54.90244 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa281a87-3d2e-3b8f-b3ba-072a8b8582d4 | -11.21998 | -54.91457 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed6cc172-92be-35aa-b1b4-32ed64328689 | -11.19169 | -54.9112 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 561c1ed0-c9df-3d04-bdd3-0d153fbf2e37 | -13.24599 | -54.26762 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab7a9b7c-bbe8-3f68-8906-7bf151ce0491 | -11.91942 | -55.91365 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02916a6a-9fb3-3a09-ac02-b564aa142383 | -11.18838 | -54.89148 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a54a26ac-c6ae-35e0-8cab-889ebe854ecf | -11.20131 | -54.83338 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79dd6a99-c0e7-394e-b59c-a06845199894 | -11.17334 | -54.92037 | 2026-08-05 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e1b05e2-e581-38e8-8d46-1a467cb453da | -11.19222 | -54.86033 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f19994ab-52ac-302c-9808-afc20969352d | -11.17326 | -54.87414 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54f6be01-0f87-3ac7-bfb8-ab354ad4e875 | -11.16847 | -54.89028 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddeee175-e0ec-353d-a435-a7d5179d7e50 | -10.81726 | -65.09055 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5683daf-5da0-349d-a2dc-58c739418e11 | -13.24797 | -54.26633 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41ac234e-9050-3e0c-b2f1-08a238b68f4d | -11.17797 | -54.88261 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcb87978-b24b-333c-bd9d-09444548d84e | -9.95511 | -67.19753 | 2026-08-05 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4e57b64-2dbf-38e7-83e9-2647c07b5f59 | -11.22054 | -54.86419 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd88807c-fd23-3b14-b60c-a5292ecbaa7c | -11.91984 | -55.91027 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a05e36-2bb4-361b-8df6-67adae12f0b4 | -11.18463 | -54.92184 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c9adcd4-e766-3832-a810-483338345d50 | -11.18271 | -54.89083 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb512c55-a759-327f-8175-f61da32d54d9 | -11.16816 | -54.9158 | 2026-08-05 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 79aafad0-cc0d-3249-b5e2-131daf5f9d3d | -10.82001 | -65.09458 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027e822a-6751-3275-b984-ded7610dda66 | -11.19788 | -54.86113 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4862470f-1fe5-3722-9520-1dc1965c1b5e | -11.16532 | -54.87013 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bc2dda3-bdea-3806-9ff7-3fcbc498788a | -9.28219 | -60.65199 | 2026-08-05 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42209073-2e6e-3f93-b96e-36df9ed1cc7c | -11.34083 | -62.21505 | 2026-08-05 05:42:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0db4c0b6-fbc4-3077-a5ef-3e55d45fd5e1 | -8.65851 | -54.97527 | 2026-08-05 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d099aee3-a9fb-3d78-a533-01ef39a56401 | -11.20082 | -54.83731 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c246535-6391-3ff0-80e5-3c96a45a10c7 | -11.92026 | -55.90689 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69a0c51d-f904-3647-a1d9-936a68728e51 | -11.19263 | -54.90356 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea06090-68b9-3462-bc88-ed94595478d5 | -13.24747 | -54.27084 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| edbeadfb-ed6c-36f7-8fe0-c9d276e90291 | -11.18556 | -54.91433 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed03b099-2d4d-3b35-9003-da2633a74eb1 | -11.1738 | -54.91658 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ffc5fc6-36c9-3a75-aa21-441a0d586fed | -11.16389 | -54.90376 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb0a39e1-9e76-3854-99a2-30151d94e8d6 | -11.19877 | -54.90042 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75095df4-f54c-3dc7-9a09-30ee6ef69cc0 | -10.81395 | -65.09001 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f78292-4695-3d21-9e05-8d4cfb15ef8c | -11.16654 | -54.90519 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 97bbee15-036f-36fa-9791-e87bf14d047e | -11.17137 | -54.88956 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cfd4352-f6e3-3444-b763-f9f840b6bc9e | -11.16234 | -54.89325 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feaaed75-81ff-340d-9fb4-e7387caa78fa | -11.20818 | -54.91707 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cea4dd38-2d7b-3f87-86a9-39a63f3d55ec | -11.16281 | -54.88956 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e28e5955-d005-3bdf-ac5c-e3572093ea5e | -9.18364 | -58.0664 | 2026-08-05 05:42:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bafd1ba8-6e16-304b-88a0-6c2389b8ce30 | -11.16196 | -54.87244 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce47e337-77e4-3cb7-91c6-e6180fbe879e | -11.17046 | -54.87492 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612f56f8-1286-3119-b96d-d8914ad34149 | -11.16863 | -54.91199 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bc0f23a1-a534-35dd-92fb-028a6ec09fc1 | -11.18318 | -54.88704 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03606069-02b6-3d2a-808d-a58d79cdd53a | -11.35028 | -62.22478 | 2026-08-05 05:42:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80806709-787e-3f7c-bb6a-0daed8448005 | -11.16481 | -54.89627 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d369d0c5-0899-3c9c-a696-a750a8fcef72 | -11.16908 | -54.90826 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f8022f7-1f2b-3138-975b-032ff525be82 | -11.16808 | -54.86937 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d4f528-aa50-327f-98dd-61d732ff2ffc | -6.71604 | -58.94638 | 2026-08-05 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd029bdb-ee90-3205-869c-92a972c4eb94 | -11.18791 | -54.89528 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0136db7-e8db-3f34-affb-d9ba1d209540 | -11.16712 | -54.87724 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
