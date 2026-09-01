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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9ff0ff8-8984-3ca9-8703-10db0ab586a0 | -6.88414 | -59.44966 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad70252-b4af-3986-b0b6-443df612b7c7 | -8.58772 | -54.76746 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd068a1a-df97-3c65-b506-2ff9128884e9 | -7.35041 | -60.57667 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ccf2fff9-92e4-3098-ac9b-c2ea3add83ff | -6.43014 | -53.56318 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb3fca58-632d-3b8a-a312-275d70964e93 | -6.86309 | -56.57136 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 514083bc-9dad-3a52-a2ec-873d95cf6bdc | -10.82391 | -50.71534 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 817c4c44-f583-3d44-8993-863eee49068a | -7.04346 | -59.22881 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d6d4d66-e0c9-3435-be74-72dbef26d086 | -8.78487 | -62.48159 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5811abd-4cff-38e1-97b8-f3f40e8a254c | -7.2847 | -49.82015 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062c261d-4bb7-3e99-bd91-459d2abc7a13 | -8.7913 | -62.49549 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4325950-1fc9-37ca-b5c1-60429147c092 | -7.50171 | -55.3589 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d13829b-84fa-3e53-8b7e-040bf0985105 | -6.80769 | -59.7729 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86a97733-7763-3ff9-9f56-60f4c49c1d41 | -5.2558 | -55.91216 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c4b6a1a-5958-3a69-a2b7-70182bc17f0e | -8.41261 | -44.99532 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbdf4295-cadb-3df4-9940-e093d5ba3324 | -10.75671 | -47.97841 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 002b8ec8-3e93-3897-991e-a564db07d8c0 | -6.69533 | -55.41512 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e1cdcf0-34a8-3c32-b6aa-7236a2c634ef | -8.50271 | -55.31605 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6861503-5a5e-3e47-89b9-d461d9a89898 | -4.96981 | -55.83865 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ad1ab26-d92c-3601-afe9-e614316e0808 | -4.37047 | -55.43504 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7653f70-2110-3040-9923-5222a5d94ecd | -10.32832 | -49.95528 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b1971fe-4159-367c-be81-a58bba0206dd | -6.97543 | -59.5975 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b47c276-1fa1-3a5e-8688-139ae364efee | -9.15766 | -59.54014 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa06c9bd-f1a8-3bdf-9d7d-63c055155a61 | -7.01665 | -55.64784 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 872fb790-3e2c-3fba-b0d0-817e88f18156 | -7.48 | -61.38449 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e935f5c-a9c1-3d1d-9672-0dcf70d05011 | -5.95178 | -57.68849 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c9cf009-6b3d-3a6b-9322-4d7e134c9253 | -3.34131 | -59.43 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2234e484-af7f-3723-bde9-5456189d7f27 | -9.1677 | -47.82951 | 2026-09-01 05:16:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 507849eb-4b2a-3770-9e31-411dce5ff0a2 | -9.94839 | -53.99517 | 2026-09-01 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e27bd070-a849-34f2-9dd7-703f46a1d619 | -7.56995 | -61.36975 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e614c6a-8555-33ea-832c-8c5bfabb5871 | -3.20808 | -61.13627 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64680fcc-f36b-3da2-b9eb-6dffbc068b7f | -6.26107 | -55.37899 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7170cde3-099f-31c8-bd2d-0cf27baeb84f | -6.82914 | -59.57537 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 619d4caf-13f8-3b7b-b87e-adf1c732877e | -4.15431 | -60.7199 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14b496cc-eb0a-3656-9ef8-b75562bc81c5 | -5.48844 | -57.14141 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cadbb653-b328-35c5-8aae-c250c1f7f36e | -10.35814 | -50.00858 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 56889177-6cb2-39c6-811e-9901f4bc408b | -8.71026 | -52.36684 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4242c532-8875-3c5d-9834-12aa381bf83b | -5.24915 | -55.8898 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77dc4d60-d843-36d0-b1e8-2d7b0f2a75df | -8.61434 | -54.82043 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aec71e6-3a61-32e9-b9cd-6c76d6aa5f5c | -4.85222 | -55.83447 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c862d8-d591-33ab-97fc-05ba6518ffee | -6.25228 | -55.43461 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2f6b163-0c9f-377b-b022-cd1da378cf08 | -6.24841 | -55.43755 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5ddc3b8-5c24-3c43-af88-1b44d84bd7fb | -4.15265 | -60.70441 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b4c3b02-272a-3ba3-9980-7b037a9e425e | -5.59288 | -60.23358 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b61a628-a383-3ecc-807e-5ab6119f9deb | -8.61944 | -54.85474 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d546042-5f4b-3a01-b47f-30294734dd7e | -11.26336 | -45.11446 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90aef589-fadc-39f0-9919-0a08ba3cb97b | -6.8069 | -59.57168 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3f2ea66-df5e-3d84-a116-aa9ad61dd269 | -3.63376 | -60.55265 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37efedbb-74b9-385c-903e-76fa63b4a82a | -6.88319 | -59.40962 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41c02fe4-bef6-3020-817b-3f1ca725bf86 | -6.85182 | -59.46209 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53e5d2fb-0880-32b1-a651-b0727b6b402e | -7.34959 | -60.58154 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| feaa0e33-d58c-314f-a2f1-29892702134c | -6.70309 | -55.40919 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91d0ec66-6059-3fe7-b280-b2375696da6c | -5.95238 | -57.68478 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b790183-5f4e-353d-87e6-37f8e6a76bfd | -11.26041 | -45.11867 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aca74743-581d-300d-9d72-7a3592ad31ae | -6.96293 | -55.64657 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee15726f-c46a-3fbd-aa4d-f250be029d48 | -5.89483 | -52.25634 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3e843c2-ca89-3b15-8250-cbeac496a11f | -8.59396 | -54.77218 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ccce01d-44e6-34ed-857f-eec5a61acaf2 | -6.59082 | -58.59729 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39a258cd-e80c-32d7-97dc-4a42b413b75b | -7.05233 | -52.71914 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51c83159-d6f5-3aa8-8796-4a2da4accdf0 | -11.32261 | -45.15879 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b2311f8-25a4-357b-83c7-29c4d85ed9b2 | -8.27994 | -54.92944 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4cbacdaa-a879-3c61-8e4e-3c7cd4bf11f1 | -4.15616 | -60.70879 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d995b368-7350-3062-813f-d7bfebc6bf15 | -7.42132 | -49.74075 | 2026-09-01 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aeb206e-f4f3-3838-b186-8d3f9b00ee39 | -6.93521 | -55.62793 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a036ed-c89e-3c2b-99d1-5183861c4403 | -5.87128 | -57.77983 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b04534a-fddd-3d8a-b030-3ab06fcdefcd | -3.61894 | -60.56533 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7bc39c5-1e04-3ce4-9c73-0848e8232bc3 | -8.46091 | -57.64673 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d5c7a0f-ea3b-3023-9dc1-bf09f8d51b98 | -6.80884 | -59.09005 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94390740-fddd-3cb8-a339-429cc058e7e8 | -7.34269 | -55.18943 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc138992-872a-3140-a7e8-d91ff11d2453 | -9.38786 | -60.57228 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b36a9d60-6a26-31a2-9e20-98165a23525d | -8.48938 | -44.74037 | 2026-09-01 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 953bd96d-7263-39a3-99ab-faf1ec41c031 | -7.62284 | -57.61939 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba4c7307-ce3d-3101-8b4d-520d4aaf040c | -6.59855 | -58.59444 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1112a4b-6c03-359e-9c54-8ae0e7702382 | -6.62135 | -58.38777 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69681c0b-c699-3605-99f2-7100e9ecaf17 | -6.13414 | -55.64354 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1b5cab8-6f8c-3226-9b76-67275ca0ec1e | -9.44421 | -45.68127 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cb75c40-7b04-3777-bb72-73df30ad2fe8 | -7.57514 | -60.47921 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dcb7e0bf-6a30-3d81-ab39-0ceedca4d5fa | -10.03663 | -44.70067 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd502bf1-272f-3dc2-ab8b-2fefa77ec563 | -5.95702 | -57.67788 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5889689-3804-318d-b1a5-e686cc9f52a2 | -8.69414 | -54.6895 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6af92653-7790-3dac-98aa-325a0328c260 | -8.50493 | -55.3018 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44a21ef9-d808-3eba-9cb8-e00c35f9a7eb | -6.92469 | -55.62983 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8a4733-9464-3128-a4cd-b6577d14067e | -10.69366 | -46.25705 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c090262-57bb-3c07-8c96-49de87ba87d0 | -6.94851 | -55.63004 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12549965-98ee-337e-bf6b-1a9c89085d0d | -6.75848 | -59.4395 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f86f8a-e9be-3982-8b9e-e582307ed14e | -6.94741 | -55.637 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86bc061d-724c-3f42-9c72-887bf331881d | -7.35496 | -55.19862 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a1f8fe-9971-39c6-85e7-cfd069475912 | -9.44624 | -51.56728 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df1e6038-d7b8-3045-9375-897b6da30f5a | -10.15166 | -45.68847 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a474ab69-8471-3914-8d99-469eab356a66 | -9.14194 | -61.09728 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd68d085-a734-329d-97ad-f3ac6aad91cd | -8.61668 | -54.69283 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec23df69-3cec-3025-8f23-16c29cee7499 | -6.80764 | -59.56725 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 730efad9-9a86-3d1e-b672-64a6a5e5a15a | -10.02511 | -44.68777 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a7914ff-8f5c-3b45-9d5d-9017560d451c | -7.18917 | -60.67499 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b17787e-ab46-3d0e-82bc-05db6f4a54fc | -4.96096 | -55.85144 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fee3b89-6571-3801-8816-fbc6fc70033a | -10.95459 | -49.76857 | 2026-09-01 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 124cf9e1-06cd-38ad-a977-280b1b033981 | -4.96925 | -55.84211 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 361e4d8b-5c8a-3a28-8fc4-2238170c04f6 | -6.79325 | -55.66993 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ee782f-af16-3cde-81d7-bcb830f3e122 | -7.63375 | -55.29276 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6984cad3-4aca-3b4b-b2b9-a4e42b405036 | -9.39923 | -51.60742 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e0bbdcb-8217-31ab-a4f6-a01f56d7431d | -7.28052 | -60.65675 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README54.md)
