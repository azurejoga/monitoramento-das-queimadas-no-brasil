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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c538185-726d-32cd-824e-61da271d6863 | -3.10245 | -53.76053 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd026265-05e0-3187-a248-4136bf42edfd | -3.92757 | -54.57998 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a6f432a-10cb-3e4c-9caf-70cec7fdfb9e | -3.08782 | -58.03003 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6160da49-0819-3ac7-81ab-5a76744fbdc7 | -3.17298 | -50.45885 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b6cd50a-fcf9-31ad-b51b-f20ee1ef589a | -3.10342 | -54.2797 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dde7b292-ac7e-323d-8037-73b1e7db0a60 | -3.03253 | -54.0757 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3b30cc9-9c98-3bd6-8fbb-40537fc26e78 | -3.53376 | -54.67352 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 910323d9-e0ba-3a0b-8d3b-72a221007ef0 | -3.10823 | -53.76836 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79407a55-9673-3339-826a-cf928d064d68 | -3.52573 | -54.65652 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33c02fb7-3c19-3cb5-8a3b-296849518b5a | -3.26638 | -54.05617 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbabfddc-893b-3dfa-a3a5-d7d4eaf9e9db | -3.30408 | -54.04493 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 739439e2-6421-3f8d-bd91-cb2a304892fb | -6.72506 | -55.06519 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 078b42a3-9d02-3c03-b40e-e3fcd6f771fd | -3.03203 | -54.07898 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c968578a-1250-32d8-9ce7-f79e121253bc | -3.01828 | -54.134 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceb1061d-f34b-3c2b-a865-a4424976dd68 | -5.21896 | -60.04884 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09a6539d-8396-3190-8ea3-e7472356a6bb | -3.87007 | -55.99926 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a6a2dee-24bc-3146-8caf-8d65ac778544 | -3.02743 | -53.92802 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a7b4dc2-66c4-387f-b87d-f02489dbc61b | -3.08576 | -54.29012 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c9293c-bfc1-36ff-a768-1d75d79aa843 | -3.00743 | -54.06183 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07df6350-9e16-35ec-a620-f7dbefa224c1 | -2.76878 | -54.07836 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb1c195-632c-39fe-aaec-b2c786d759eb | -3.56549 | -54.49315 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6e2ef3c-4142-37de-b3c3-c047e02caabc | -4.37564 | -54.74857 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fd496a5-274b-3e39-97db-fec73a089af4 | -3.10527 | -53.77837 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c536f08d-880f-3a85-bbd8-6e2e35af2000 | -4.44999 | -54.9762 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db5e8f41-e1b7-3a10-bd88-40f55e50703f | -6.52283 | -55.27977 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e22a908f-2b0d-30db-b97f-cfaf56462d1a | -3.69111 | -55.95914 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fbd66b0-3cbe-3225-b6af-da5c4457fe1a | -3.07906 | -53.94953 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e56ab46a-f64b-3039-9788-dc46a4050e86 | -3.27936 | -54.07847 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20cc453-01f8-30c8-8817-4fbb451146c6 | -4.37003 | -54.75081 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71975180-b59d-3b33-b815-38cf3d411a0c | -2.84985 | -59.11269 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7a8a6ba-c2cc-3fce-a36a-2536994dfcdf | -4.06695 | -59.83512 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff777acf-8bc3-3ad4-80c6-01728c7e5306 | -3.03765 | -53.9331 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07724671-644f-3b52-ae39-a891ef26deec | -2.96013 | -59.3258 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f01a1ef-537e-3dfc-9a5d-699ef7364c8d | -3.64136 | -58.94226 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98e9c4f5-0d37-3403-a133-0fc615bc62ed | -3.66874 | -60.61415 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b722cbc-b179-3b70-9223-bdb87caf61b9 | -2.47081 | -56.09859 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77b70837-7633-3b01-b2b0-f832eedae911 | -3.01225 | -54.06594 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a67a3dcc-a132-3e98-9677-e38fd6d46c4e | -3.07864 | -54.26598 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 428a8288-2790-357c-9be5-bf559fce7949 | -3.1215 | -53.79149 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c84e72da-398d-39bd-823f-a2ac66f754ec | -3.29413 | -61.01598 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68459e6b-9f20-3b03-9e43-16e62eefaad8 | -5.29844 | -60.09655 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a7f141e-7ed2-3e87-9fd7-6bd8eeb7868e | -3.00966 | -54.11934 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1a086c07-2ea6-361f-867b-5dee4b993442 | -7.38371 | -55.21696 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2134ed0-80d3-36f1-b667-84ff088b41b1 | -3.0146 | -54.08652 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fee0ddf3-4e88-3034-96a1-bddccbc9ebec | -3.1039 | -54.2765 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05df2420-a4f3-3158-b4a2-892f9447d73c | -4.09172 | -52.07343 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8d4b94-51a3-3f9d-9237-bbf7da4b61d6 | -3.1619 | -54.74222 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a27de4e6-441b-3a1e-a28b-003b4a6f7cad | -3.29481 | -54.0709 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b375982-cfc2-38b0-b5c3-db6e270c2231 | -3.16771 | -50.59007 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 695066fa-8628-3a27-bbb2-61e013280f98 | -3.08815 | -53.94402 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 270a98b1-788b-30c3-86d7-621ff913e34b | -3.01668 | -54.75027 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b80745-3a75-39a6-ac18-65709cf081ed | -3.77633 | -59.25444 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d375f575-0aeb-3f3b-bf48-2799f02a756f | -3.53622 | -59.47714 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e599ebdf-43ac-3e4d-a44a-871f81dd0b27 | -3.18811 | -50.56535 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 300cdc82-b575-3db7-a24a-ccf68701d9d4 | -3.289 | -54.07332 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75b5058-b9eb-34c9-807c-f4bac3d85d27 | -6.7338 | -63.04337 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 882ee432-4bbe-31b9-aec6-a27fe31b195f | -6.80414 | -55.30202 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf3898ba-7329-385b-b0a7-f915022c8e6b | -3.6646 | -60.61755 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2100558c-f58c-3d9a-8969-77348e7f3119 | -3.11859 | -54.1792 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 6d32ebff-f041-3fa1-8ed3-b6b5c2cb8074 | -4.07234 | -59.84919 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dcc0a3e-5cf2-3b38-bc19-56dd7b77a151 | -3.58997 | -54.68445 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46bdec04-581c-35da-9307-4f4aef47f468 | -3.49195 | -54.62131 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9eed399-286b-3928-8f8c-7f1e7d997f94 | -3.53937 | -54.67109 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89f59a16-8876-34df-8657-7baf07eed159 | -3.03229 | -53.93225 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc6c529a-8f3f-357b-aed2-41fe2a13267b | -7.3258 | -59.89865 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 835d7346-c142-366e-b4b8-214739de729f | -3.47135 | -59.57605 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8565f78c-b0ab-3ce7-bf9e-27f3d667ab68 | -3.02671 | -54.07823 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8b52e21-6d96-3c69-aad9-459f70822994 | -2.93713 | -54.17389 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bfeb8f5-aad3-3773-9066-849041224144 | -2.78419 | -54.08394 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9674a52d-8e46-3ded-a5b0-78fc526f3947 | -3.09474 | -53.73804 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c2512f-a068-3894-b875-ec1c94b77958 | -3.70959 | -59.65845 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea10ef6-fef3-3bdc-a566-96626eee2a28 | -4.30872 | -54.7971 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f162416a-6bfe-34ce-ab1d-3a1d2f991b17 | -3.29699 | -61.02027 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a85cd4f6-9e9e-32d9-87d4-a9f19c6aeeea | -3.32374 | -58.2311 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c934efc-3271-39fa-b12f-c0eda0f58c12 | -3.29239 | -54.05011 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67750de1-60f1-3e9a-b32a-50098ec94477 | -3.65321 | -58.88989 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d8f5b2-c6c5-39fb-8c15-6668dd987577 | -4.77367 | -55.74562 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6e36431-d0cb-3706-ba4e-1ede8614c01d | -4.15474 | -55.1478 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d4a262f-9f36-3009-9012-ec16edf0d27a | -3.29668 | -54.0368 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6934a9c1-77fe-3815-8f7d-5dc19cde247a | -3.26074 | -54.02125 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b992282-30ca-3d9f-8ed1-b9b295d63197 | -3.27833 | -54.07169 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dca57e3-419a-3709-9aaf-3c11b81ee490 | -3.54065 | -59.47324 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c6021d8-d517-3f40-81f8-5a2a49bc13c7 | -3.11366 | -53.76921 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2506d037-04f0-3e7c-9758-ad01709fd1d5 | -2.6073 | -57.5844 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea4b2d57-98f8-3590-aefa-9d218cafd880 | -3.01843 | -54.09715 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1c9e7899-a7b5-3172-a443-6b2a06573bc8 | -3.28671 | -54.06608 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38e4207b-9dc0-3b30-8b26-f3b360628b7b | -3.04226 | -54.15427 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36063662-2cc6-34a6-b7e0-d3ced106c8c0 | -2.8825 | -54.17875 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3345014c-c11c-3cd9-94f5-c7c7160bba9e | -4.1556 | -55.14203 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac2b3245-0403-341d-869e-1d8dd3a3699d | -3.00782 | -54.09552 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ab28f27b-4ccc-3ce8-b384-34929fbdd673 | -2.84861 | -59.11901 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 073450de-5739-3b25-9254-c4e21e6f6868 | -2.97853 | -54.04618 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f0de1a-7a92-38a8-9e23-8aed1c26dec3 | -3.56939 | -59.4939 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d2cc9c-8689-3971-905b-45fce2ca5533 | -3.54018 | -59.50055 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3ef87f1-2de7-3010-b961-64599dba20f4 | -4.53937 | -59.92665 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef0cde7-ae99-3ca0-9b9a-1efb8c0f783c | -2.86289 | -54.16571 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 367939db-07da-3827-b055-e80d9fabad10 | -3.99066 | -59.22008 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 944f2b9c-ab66-30e1-b9fa-cbf100aa0131 | -3.07801 | -53.95639 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 71df1816-08b4-36d6-b752-acdba332b403 | -3.03479 | -54.52449 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89a80c00-4892-326a-b826-15399e35d766 | -3.00929 | -54.0857 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README192.md)
