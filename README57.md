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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b08eeff4-0b65-33d7-92d0-9a6ee7fe0cd9 | -8.86542 | -46.98755 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9170e17a-5155-3eae-abe5-3828c49a78da | -6.74406 | -58.57867 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ab1aa5-18d5-30a4-9d36-b0ac441949af | -6.88693 | -43.74833 | 2026-09-17 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a09ba91-9982-3a1e-ae51-f8d0cda6366a | -9.86788 | -48.34799 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c216ccb9-4caf-3676-aa7c-4e9d9645a2bd | -4.10489 | -56.34179 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 901f70f5-e1c8-3f90-8215-b8b0c7a556f1 | -2.90086 | -54.18243 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbe1cf55-f225-3ff8-a4bc-5fa12e84d4a9 | -6.30897 | -55.15544 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08ee37cd-aa47-3c0e-9624-8e315d94193a | -4.5164 | -54.94181 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bd84128-8ea7-37f4-906c-d9e6a0784e81 | -4.51256 | -54.96609 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ca61772-294a-3856-ab60-2aefaea356ac | -8.85892 | -46.98353 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44e71320-eee4-33b5-a0a3-b65eb03bdff9 | -3.59998 | -59.06612 | 2026-09-17 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f01bced-9239-3143-9d0e-93bc40b5a5d1 | -8.6103 | -44.4772 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2cc7017c-b61b-33c6-ab7e-aa150f64bf8d | -6.84539 | -62.89524 | 2026-09-17 05:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d303e71-fe3c-38e0-814e-2010cd282282 | -5.85954 | -52.12245 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf2079b-26c5-38c4-89ee-3f695f089250 | -8.38916 | -42.20517 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 72377f25-cd8e-3495-8246-4a1ede67f73a | -2.90976 | -54.16948 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8fcde7-16aa-39ac-86cc-06ede08bb105 | -9.0351 | -47.75592 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d619359-8eb6-3bca-bb6e-ae0d46dc72ed | -4.57242 | -54.90416 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b1e3715-aef3-32b7-b3a6-f8ae61a3261d | -9.61446 | -45.35925 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89f86b01-93ae-3f36-8595-20fc1a71e40c | -3.44231 | -50.66323 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e211b8-6b42-3e01-a7ef-99a2d89ad2a6 | -9.8934 | -48.38714 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63a8a304-019f-3d1c-a8dc-e20026cf339a | -5.77621 | -45.09109 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1d981ef-6496-30e1-8449-0321c1681c58 | -7.5758 | -44.92143 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 202cd594-50de-3627-ba37-9135bd6f8249 | -9.84106 | -48.36657 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49f81ade-9f43-36fe-b2a8-0e0fc5853353 | -5.7686 | -45.10235 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| b258342e-da8c-31b2-ab96-97a4a32cd4d6 | -7.91549 | -61.55938 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8460c264-dc5c-3b8d-9014-c907bc87a441 | -7.0394 | -42.07434 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0460d49-ea48-3c60-9d9c-ab625bf50f83 | -3.48097 | -54.68686 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac3a7fc5-a366-3eca-9aa5-c9383ca0a530 | -1.81734 | -54.93486 | 2026-09-17 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e6e397c-1bde-30b4-83d1-db85c2ad6b38 | -7.38054 | -44.51144 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc3ebcf4-ffca-3412-a50c-28f84f20e1a4 | -5.88703 | -52.09081 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 442e93a1-64a3-31af-a3d6-a38d73f15443 | -5.14443 | -47.60135 | 2026-09-17 05:16:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be0b7b9b-b76e-3497-b458-45317071f913 | -6.84455 | -62.89998 | 2026-09-17 05:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5855e13f-accb-38e6-b299-2fecd6eb58f5 | -6.81242 | -59.16159 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e576d06-01aa-33c8-b979-aa955af2fc22 | -3.48485 | -54.68391 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc66733e-a67e-365c-b9d2-6ff1d6fc3945 | -5.90332 | -59.93336 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab30e28-d4aa-37ab-8b7c-36139f93e2f5 | -3.47877 | -54.70074 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a65c35-b3e5-35c3-a2fb-fdbcb560884c | -2.89973 | -54.16791 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 292c8907-2e29-3545-8275-03d369fe5560 | -8.26618 | -42.18024 | 2026-09-17 05:16:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7ce13c8-5d62-3c38-a46e-35cc565dbb78 | -9.62171 | -45.35097 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ba1fd25-c207-30aa-8667-08695bc1b1f9 | -2.97226 | -54.15385 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839848fb-d330-35cb-ba58-ef0722a28c94 | -3.26614 | -54.26461 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15a5bc00-bc09-3ace-98b2-390219c7ce88 | -10.36953 | -46.89094 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 984ab549-95cc-3d78-aca0-221f339aec3f | -6.90636 | -59.02219 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56943da9-1616-349f-9db7-afebc35503bc | -3.70318 | -58.85731 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e59b435-7d68-3e13-ab2d-9b818cf8f5a7 | -9.46049 | -45.45342 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12ec3175-ab48-32c4-939f-37390250e523 | -5.91095 | -59.94147 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61efd783-463b-30d3-9460-d38cce6973dc | -2.90307 | -54.16843 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c36440c-19de-313a-b317-c3a11ba42228 | -3.81423 | -55.88886 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17bb1b6b-7c69-3649-9225-4ddce5ba7d55 | -5.15647 | -55.94128 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe76e22a-c9dc-3270-af0c-c3ee1769b678 | -7.00073 | -43.32765 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4566b553-0f99-3857-94b6-d7ab9b29afdf | -3.54978 | -48.17713 | 2026-09-17 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae6f4b77-131f-3cc0-be0a-9bab09e7197a | -9.11182 | -45.73049 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6c632e55-2f70-3f50-aa8d-e65500bb4b4b | -7.58726 | -44.92891 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07345fff-ef74-3bbf-9a9a-1335aac977ac | -3.59243 | -59.06489 | 2026-09-17 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52132189-f8d4-34b8-939f-4ba3785b16ae | -5.15147 | -55.92981 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 909ba02b-b1b5-3810-8d3a-0b26c750e4a5 | -3.33906 | -54.17168 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9812a7d4-848f-3a1c-8a46-dc52d4714318 | -7.45484 | -46.16439 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f846380-5894-3b63-8c66-f97565a38c7a | -9.55774 | -46.60316 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7701f629-2d3e-331a-b3e7-62d65b46ab69 | -4.57187 | -54.90766 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe8e55d7-55bb-322d-8c9a-5ce57e6cdb28 | -9.87415 | -48.37803 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b8abfe1b-5d9b-344d-82cb-56dd35ee70e7 | -4.13537 | -54.41758 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35b249c3-5089-3a7a-8adf-dee31a9e5902 | -5.96892 | -57.7812 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92dec3e3-351b-312e-8743-0abeec52adc4 | -7.04113 | -42.07212 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5d9a9c49-ead3-301c-81e0-c23d9ee2c053 | -7.87747 | -54.7218 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f418f72f-17a1-3e45-b7bf-4809aed44283 | -6.04264 | -44.03496 | 2026-09-17 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 206045ee-d33b-3410-a0bc-e49fe040cd3e | -4.54134 | -54.93505 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21351026-2349-3c7b-be3e-062c08c85a2a | -3.5423 | -53.99311 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c91a002-ee37-31c4-bf8a-d63400e05aa3 | -3.27058 | -54.25814 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aade736-cdff-3630-8bf5-b9e71070bf68 | -8.3702 | -54.7378 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50b4b67-1188-37af-b304-6f4eea79d6da | -6.90138 | -59.02991 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cd523c7-eac1-3f95-86f5-e29c8d0e0b9b | -9.11775 | -45.73127 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 27aac9c9-b4f4-3801-8797-7fd0c22bf880 | -5.97761 | -46.63012 | 2026-09-17 05:16:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a03bf96-b7c0-382b-8b4f-34c48e62e6c2 | -8.85934 | -46.98044 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb781313-17a9-37e3-80ad-7b55cc252f64 | -3.47936 | -54.71859 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2e917ab-8998-37aa-948a-0e9fbdeaccd0 | -5.14205 | -55.94612 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c93d2a9-c6cd-3ffc-a729-2e8684448ff4 | -4.88263 | -56.06535 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ea1f0bf-06b5-3336-b0ba-945d1ba21f0e | -3.45041 | -57.97255 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40b490d8-9cd3-3f3e-bd77-0c16fa97818d | -3.81403 | -58.89374 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 101121ac-35d1-34df-a4af-7bc6037c95aa | -7.11556 | -55.12726 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ff02c28-2b0e-3103-9c53-332423cd4c18 | -7.58184 | -44.92285 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe7b5789-68a1-3d15-811a-a78afa5289ec | -4.53411 | -54.91613 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c2e5e9-4603-3491-a41f-00ab9bc9a1b2 | -6.16058 | -55.71329 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7820a84a-a2de-3413-a4af-a2e722053989 | -6.43427 | -60.01379 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e694b896-4b05-38dd-a3b6-1c1930587eca | -4.54522 | -54.93211 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63c6719c-cd12-324a-8467-f4f660efa531 | -8.49199 | -57.65026 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c020fd69-9d9c-39c6-bc7a-55ce14614eb6 | -9.8446 | -48.37794 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 197332fc-017f-3101-94d9-a6b2502df9da | -3.04688 | -51.27635 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea0fbad8-e1aa-3711-92bc-3c94b244e62a | -8.86083 | -46.98022 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31f48c51-a495-3885-ae99-35feb2933ba8 | -3.54515 | -48.17639 | 2026-09-17 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0848161e-1a4c-323b-b571-a29b4dfde595 | -3.03134 | -51.22791 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ff0d423-8d27-3ed0-899d-000fa3d478ce | -3.48433 | -54.70871 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2abd7049-067a-3249-af40-022ed28fc58a | -2.19217 | -56.84156 | 2026-09-17 05:16:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38ca06f6-1c3f-3605-8ffd-b49b43208e74 | -3.0815 | -50.56963 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b40b99c1-3b4e-3371-827d-6f3702b702bd | -2.09064 | -56.42611 | 2026-09-17 05:16:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2719dd1f-513a-3ceb-b767-7201d888e5a8 | -9.77141 | -46.54481 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b06781fb-92ea-39b3-b1cb-c9da1a23013d | -5.76158 | -45.10951 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1179132e-6b3d-3cc2-a016-58e8713462c8 | -9.45942 | -45.45172 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ffda5bc-c784-35bb-ad04-d26aae4cfed6 | -8.41317 | -54.73282 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c557df-450f-3b30-850a-828b025092a8 | -4.53078 | -54.91562 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README58.md)
