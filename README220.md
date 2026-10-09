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

## Dados Diários - Página 220

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac1ca33-3879-30da-84c0-6799f0b2503c | -6.13746 | -53.51017 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61b9b6d-ff1f-380c-8986-8c099ec68e4d | -5.96995 | -55.36186 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28ee8f5b-e5fa-39b7-b959-231c692d4dde | -4.76753 | -55.67609 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b213be72-a56f-38ee-b223-b8d90194e33d | -7.17258 | -55.12843 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d78cff4-f4fd-399d-b849-c03865060d7e | -12.24108 | -57.08962 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33464517-4be5-36b9-8dcd-a231e58ed5d3 | -6.38479 | -55.27113 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93ac3642-ab7d-3424-ba1f-7d2c12f966c0 | -4.13273 | -59.89553 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a583ef-668b-3543-8422-28109c7924e9 | -6.31196 | -54.80619 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7d543cd-2650-35d8-9862-5adc64e9df13 | -12.83489 | -62.16911 | 2026-10-09 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fd87bf1-7f6c-3d73-87c0-7f8aeba2c929 | -6.41919 | -55.1972 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a48540-a68b-346b-9efc-68461b0e4144 | -5.96489 | -55.37039 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0156fa4b-672f-35a3-b1a6-2c637dc6bf9d | -13.1894 | -54.36581 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5768ef30-1b14-30ad-9b27-5ce0dd775348 | -5.70556 | -53.45269 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 673509a3-305a-3889-9149-923c6401e14f | -6.45228 | -53.69033 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b50eb300-b5c1-32f1-8c6f-50b8e260ee52 | -6.24287 | -52.68155 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71231b3d-9bf5-3647-8de5-96bfb931090b | -4.93033 | -55.86218 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64fbbcc9-2581-3492-85d6-3270db5a0c6e | -6.52618 | -55.26056 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f54ca24-9aad-3b0b-bca8-b43e488e91dd | -13.16756 | -54.36267 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ac1422f-df7e-3c94-a52a-f3b92db10d2a | -14.88037 | -50.29969 | 2026-10-09 05:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 311638a8-e335-39d3-9f65-fbf5404cac9e | -7.08347 | -52.68168 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37f20c1f-f83e-3701-95ad-fa1f435f4a7c | -5.70279 | -53.47182 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1506f70-a58a-3eac-b016-6c9f1300e6cb | -6.44188 | -55.04966 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa82119-59d0-3cdb-9b11-1fdd3bef1b59 | -6.12428 | -55.70261 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 751d9643-6030-3073-8e17-e7eb64f4e019 | -12.22346 | -57.08257 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 7c7d5869-8079-3563-a48f-70d80717aa2a | -12.21982 | -57.082 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ed448f5f-a750-33aa-b274-327f5da042e1 | -6.49818 | -55.31411 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 402ab2d3-94a0-3d00-9fa4-60f18cbb1b61 | -6.50923 | -55.40086 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dd237b6-b59a-3bb0-a3cf-ed25f4f41c34 | -5.70083 | -53.45598 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b4cd617-f547-3e82-93c7-51f98daee4dc | -6.39296 | -55.26781 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 585b230f-ad02-3440-9600-10de3813fe6d | -6.1722 | -52.86114 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2f2f06-96c6-32ff-839b-8c984790a66e | -6.49207 | -55.30392 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52c67b9f-5601-3f87-83d9-d6a46836e38e | -6.06676 | -53.60476 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3e623f-56c7-356f-b6e5-753422b9a36b | -12.22284 | -57.08691 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 11a2a259-5002-3524-89b9-1ac85a8b562a | -4.89572 | -54.98751 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0ad4b11-c8a5-3f79-89ad-fe04217a13af | -8.18236 | -46.37128 | 2026-10-09 05:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd85c005-73af-34df-9325-f4153f38ee54 | -5.69637 | -53.47557 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f776f83c-c2a8-3ada-a044-88e0f32e485b | -12.23076 | -57.08368 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f258f5c0-522b-30ff-abec-96428f8af15d | -4.19341 | -59.93819 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da8425ff-1a6c-3d33-9299-7b0593ebefa1 | -6.54284 | -56.05051 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15a634d4-0ac0-33fb-9e10-806af6b75c1f | -6.13101 | -55.68421 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c58e4bb-c8ea-35af-b77f-48660719b124 | -13.17193 | -54.36331 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed7f3dba-4f3b-3426-b1e9-7b8d3ef180a8 | -6.45174 | -53.69405 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c17bc53-37ae-3681-b5b2-517a2489c82d | -10.87885 | -57.08144 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb669b3-5154-362f-8123-2d5c2089d869 | -6.01359 | -53.49309 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b532e5c-3cd7-3903-a58c-c35d6f67c877 | -4.74424 | -55.65984 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0931e01b-42d1-31cf-9967-687b286f011e | -6.17282 | -52.85693 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19902909-7403-3b1d-a7ad-7db991104f7c | -4.29767 | -59.96554 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816c7232-1534-3d29-a9e4-ce99188b2cdd | -14.97407 | -47.54734 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edc2b051-9fb6-3661-800b-59a4ba5d2c69 | -6.12063 | -55.70206 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a915811d-a687-37d0-9a7a-6d3ba1b63cce | -4.06575 | -59.84115 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ef9258-c2d6-3bf4-a3a9-49fdf1ebbb56 | -4.06632 | -59.8376 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9690d03-c1fb-38b2-b866-38ff0828063b | -5.69869 | -53.46036 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71692f41-1558-31dd-93ff-e162c03339f9 | -4.11486 | -59.8781 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aee619c-da50-3c5a-b5e0-57b577797576 | -5.80775 | -53.42503 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dbad27a-2be7-3ac3-b0b5-3f9c00a62585 | -11.96983 | -57.61183 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea441a0d-e22a-36e7-b112-2010093b84b0 | -5.96659 | -55.3448 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b4a4920-8613-3bea-b46b-4d0314cbfcba | -6.49248 | -55.95943 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd1189d-9d4a-3688-9375-879af7434656 | -6.88132 | -45.9002 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9271b508-6e2c-30e6-bcb1-ba3783f02bc5 | -11.99647 | -57.60334 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41baf62c-dbc7-3b5c-bc6b-a4df3e04c068 | -12.19405 | -57.12807 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 380ac3d4-7f63-3026-8239-3787467a9711 | -5.88194 | -53.62154 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4d10d1-e1a7-34c7-8c35-4a304883cce9 | -4.80442 | -56.1422 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa2bfad-af0e-3edb-8b58-0983bb02678b | -5.99085 | -55.37431 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b1148db-6376-30b5-9b69-06680cffe416 | -12.23806 | -57.08475 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b82be964-d54c-346f-9f48-df8cb4a68b31 | -6.87863 | -45.91611 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c9bdfb27-8377-3051-b2aa-5881739c1202 | -12.22159 | -57.09558 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 675f9b91-e3d1-3657-9790-737dbc1e0a43 | -6.13057 | -55.68613 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c87f833d-992c-3cc8-9def-2df2ffc2b501 | -4.92971 | -55.8662 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f7de3c1-a063-3d4e-8692-4d08ef9610ef | -5.26321 | -60.17696 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925ad062-8735-3c94-9eb7-1114843b1825 | -6.88828 | -45.89628 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9b74422-2cbc-3a2f-92d9-03680786dbcf | -12.20508 | -57.13278 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6928bea8-d2eb-3a3f-a609-609eb11b9461 | -12.21307 | -57.10306 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cb69aa0-8649-30aa-95dc-a7f7a3bda6cf | -4.80855 | -56.13881 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea6d300-e432-35e5-8a12-1012162e3b76 | -5.16441 | -60.33015 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4943cbc6-369c-3eb5-9a1a-d535a6d95edd | -5.70027 | -53.45985 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c247882-aad6-3d9b-9a03-e1b5bfeef4de | -4.66105 | -55.94683 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c88e9119-7c25-3d5e-b802-590b0e5b149f | -4.06746 | -59.83051 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b750a88-2011-349a-a70b-8090cb2c004e | -11.9917 | -57.61097 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fb8069a-0454-3641-8867-741f03b547ea | -13.17249 | -54.35906 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 02979649-0302-3edd-877d-02721bd28504 | -6.42498 | -54.95604 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2afc35a1-dff7-33ad-b458-2507a4e4ace4 | -5.96422 | -55.37487 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a8a7a0b-0281-3e4b-be66-5b99d8230fdd | -5.70345 | -53.45701 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeca48a6-450f-31dd-a020-f5123ccf81a3 | -6.89613 | -45.89042 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c43f8a80-e448-37ef-a12f-4c732850814c | -5.22934 | -60.23751 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f620fda-9005-3bd3-be78-d40d9f679ffd | -4.30925 | -60.94327 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0052516-7cfa-3df5-b15e-48634010acbf | -13.19378 | -54.36639 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda25700-2c07-3895-8a52-d6a88999538c | -12.19417 | -57.13112 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f92a96-cd63-3b29-929c-641fa7be17b8 | -6.20406 | -55.21146 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc31b2b8-1d50-3698-9aae-6a213818e546 | -5.69274 | -53.47149 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14d97889-7014-33cd-adcf-63f90c9c663f | -6.00465 | -53.49585 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64e4b80c-e436-3d0b-a0bd-fc4bf7ea85c9 | -12.20082 | -57.13654 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3681726-730e-37de-a3bf-cd9a5f7d5c55 | -4.1934 | -59.40742 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a0609e-2b02-3401-8c3a-72db0787e547 | -6.4424 | -55.04292 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dcf9269-88e3-30b8-a2b3-4bcda39fe25e | -6.24407 | -52.67921 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d202291a-f48d-3939-8ab6-bb993a1d8bcd | -14.97382 | -47.54321 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86c99e32-5428-3b87-b0c3-c5b935ba54c0 | -6.35687 | -55.15038 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3088dbba-be5f-33b5-a580-4af9c8cecdf9 | -5.95509 | -55.35972 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83cfb57b-191e-3b64-97e0-eee09bd4da39 | -13.20136 | -54.37613 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bc82421-1200-328d-bb78-862f2af3c0fe | -7.18679 | -52.61615 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fae6e9e1-51ca-3a5f-aa7f-4fa7876b6c38 | -6.43296 | -59.96134 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README221.md)
