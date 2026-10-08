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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d36cd75-d7cb-388c-8054-89b63eaa0d36 | -2.3926 | -57.890701 | 2026-10-08 00:48:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efd88b4f-5657-36fe-a1ce-1ecea054cba4 | -3.236 | -46.950802 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f9c61e-6d17-3d9f-a0b0-8eacf70a5227 | -3.7293 | -57.1348 | 2026-10-08 00:48:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1921db58-d7d3-3fe6-a942-88bacab5f828 | -3.8518 | -55.989101 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 535918aa-31a8-32ed-a057-9d4c7894aef8 | -3.1064 | -53.7869 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 592cd5de-7e26-3b98-96b5-a58b7a17010f | -3.5122 | -54.667 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64c55e2-807f-3b43-9f45-711bd9e8658c | -3.2869 | -54.0369 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33581caa-85dc-3b3c-839a-1d5f7975e0c3 | -3.0077 | -54.122601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a27b9641-7557-3110-bf11-7927581df295 | -3.0494 | -54.0341 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bbb5ab-34da-39e0-9001-3ba869c3fcf8 | -6.0945 | -49.420399 | 2026-10-08 00:48:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96852cf1-c02e-3ee6-98f4-803cb00a7a15 | -12.8105 | -49.827099 | 2026-10-08 00:48:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29f8f4dc-f72e-3069-b9dc-f0f2d3bd6aa3 | 2.1197 | -50.825802 | 2026-10-08 00:48:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 82292e02-e083-350e-9da0-8f189bc3b932 | -3.5489 | -59.487202 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d912cdb-3449-37bf-9f4d-b358ef76cb6a | -4.4262 | -55.162399 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a69a2a55-c16a-38b7-bf7f-ce5d4943454f | -3.538 | -54.644299 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27539293-a9a4-3216-b632-8a3fdc7dc509 | -7.6052 | -46.762299 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9927d133-40fb-3c1b-869f-31cf82dccc36 | 1.7464 | -55.587299 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c28d606-b28c-39d0-821f-28aad645fbda | -3.0448 | -53.878201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8aba98-7188-369d-b71b-4e764ee8adea | -4.1404 | -54.032299 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cb54ef-237f-3d36-baf5-138f28709ccd | -3.2026 | -50.564899 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75db482d-8db7-3c6f-90c6-2d2968b82b6c | -6.1486 | -51.942799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b63ce63-c198-3c65-b921-d93e6d94b03e | -10.4333 | -47.273499 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5fcdc21-1b1a-3e21-ae8f-e3ee32cfb7fc | -10.9753 | -45.401001 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b52f6d36-74f2-3353-8cad-1ff63cb20111 | -5.8528 | -57.573299 | 2026-10-08 00:48:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47fe5f9-e28d-3f70-81b5-a5c900661ac2 | -2.7569 | -54.1068 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c90cd7d-fc04-3d1f-9f48-1dfe0854992b | -19.0993 | -45.398201 | 2026-10-08 00:48:00 | METOP-C | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0f6f73d-95e2-3b35-bcd6-c95566fdc069 | -3.0303 | -53.9049 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27b3bee-769b-34cd-b8fe-56ec6f450494 | -2.9109 | -54.104401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 767a1c93-15cf-3d0d-a086-8c83714da0a8 | -2.9437 | -54.112999 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a4f72a-53bf-3afc-86a8-ceaf145795ca | -4.771 | -55.7383 | 2026-10-08 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1db09dd5-ffd5-39dd-9408-b45f6866a8ac | -3.5642 | -54.487499 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a22440-f257-39e7-bd21-f3c8fa1493c4 | -2.3855 | -57.9048 | 2026-10-08 00:48:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 198f4173-b7aa-3e9a-8835-a7567078faa7 | -5.8499 | -57.560299 | 2026-10-08 00:48:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9850fee2-17c3-3ab7-846b-52a797dcd42e | -4.0503 | -55.318699 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c93b3e-f2ae-3d20-86c5-75252e00151b | -3.2408 | -46.9711 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4c292c0-49f2-3baf-a078-4b3105f736b7 | -2.5775 | -56.169102 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b42d10-8db3-30f8-8070-17bcade66dc3 | -2.9979 | -54.124699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9130179e-9253-37b3-b3f4-a409a7bcfcee | -3.2505 | -46.968899 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c38499-379c-33fe-9d68-3f44c0357b46 | -2.9991 | -53.903999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5762450-ce50-3aa1-a3d8-a0c0d9beb6d0 | -3.0555 | -54.151901 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baef73bd-2637-378a-8b97-eec28b4b7016 | -4.369 | -43.812401 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3146eb-16f3-3824-84a0-17ef37339b99 | -3.0043 | -54.243301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff73c4a-ccd7-31a7-a479-cc640b55e1df | -2.8693 | -54.1931 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ce052c-cd11-355a-9d22-8bb01eacd4c7 | -9.8306 | -44.778301 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f753c10c-6957-37f6-bb2e-d6dfcd00c042 | -3.1594 | -54.7449 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210b2d78-0e59-38b0-af12-56b0dc504a86 | -5.3432 | -50.990799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3946bf5b-ee35-3a73-b407-3989c7b67904 | 1.7061 | -55.6278 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4f051b-9e7a-3f55-abaf-62c54bce1fe8 | -3.5031 | -54.626701 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6b7810-9836-3f02-85b3-f5388b3fbdf7 | -3.0515 | -54.224701 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 254138c0-e2fd-36e1-a530-da33394bd54c | -2.4787 | -56.141499 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768a9dbd-cbb1-351b-8a40-c4214e1ad73e | -3.1664 | -58.643902 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac23b7e-d66a-3db9-beb4-96c92cc33baf | -3.2249 | -54.307499 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9cc4c4c-652c-3d93-bb7d-1e940b369406 | -3.2984 | -53.861099 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58bebc0d-c1a5-3fc0-b7c7-62c31cfe6211 | -3.3019 | -54.0574 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a6e67e-d405-3a71-9f6d-9a68ecfc4077 | -3.3117 | -54.055199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e6435c-90d2-35cf-a938-4b8671e3d47f | -3.0239 | -54.238899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15afd00-e41e-3c04-89c4-502a0f46325c | -4.7143 | -47.450298 | 2026-10-08 00:48:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f185407-3b9d-3907-a7a7-c4ece7c3c04f | -7.8852 | -55.023602 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 882a3725-e264-3bd6-86d7-77ba41deed28 | -1.7932 | -57.103802 | 2026-10-08 00:48:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ace736a1-91e0-365b-a816-1c9ae6bb18aa | -6.1405 | -47.941399 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce335363-733a-3451-b657-f9a0667368c1 | -7.2147 | -55.098701 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11cdc3c0-bbf1-3a49-91be-47acf271ad3a | -6.671 | -55.098499 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cdac0dc-08c6-3e1e-8799-6bbe3b3f73de | -5.1703 | -45.341 | 2026-10-08 00:48:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5463c2-6003-30ff-94ea-a8bfdd64befa | -3.0929 | -53.728001 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 884c6eff-a401-3715-8656-4e4b73bbe3e7 | -3.5141 | -54.675098 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f879901-276a-3582-8176-7bc711b7ea9e | -3.103 | -54.269699 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f706917-e2e2-3135-a5db-4dcdde06a015 | -3.0221 | -54.0956 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79c0720-8e0e-3a93-8f62-cfdc4ad2c2da | -3.5337 | -54.670799 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eedd0b0-fde9-33a6-8333-0c103a5bd466 | -3.299 | -54.09 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 737af8e3-f748-3fc2-86e0-3b5238568496 | -2.765 | -54.097198 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4431374a-0ede-3f97-a04f-7a71c2e9ff4a | -5.9756 | -55.386799 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 648013fe-a11f-3f4d-b6eb-ec425199ea4d | -3.0031 | -54.147499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6cb094-543c-3bf7-be2f-6e74962d8ba3 | 4.0978 | -60.565201 | 2026-10-08 00:48:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| abe2993f-46b4-3b16-bde3-b46f5b112115 | -2.8613 | -54.2029 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c074df9-8921-397a-8bb5-9455b4a2e802 | -1.7133 | -55.445202 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba499e31-4453-3378-bb03-5d6f346e76a3 | 2.439 | -50.826099 | 2026-10-08 00:48:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 89906c4e-b56c-3433-a609-f857f9fae634 | -5.6953 | -53.488701 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582b85ec-4106-3910-8a2a-d2f4bbc27e41 | -1.5021 | -54.836498 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138f8778-0252-36ad-a5d2-8ec7727ea342 | -3.2233 | -53.893398 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cab5ee-eab6-38cd-be5f-f178cca03933 | -1.5315 | -54.830002 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a599d02e-f166-30be-a9e7-eea04153ce94 | -5.7705 | -52.364799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db355221-c4b0-3c91-90fb-98744a741b62 | -5.9812 | -55.365799 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97cff559-468d-3c20-a7ba-09ddeac74ae0 | -6.2074 | -52.8381 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2b7a18-a013-333d-baa9-1dd93ac16f0d | -2.7531 | -54.044701 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e99ca90e-cdf6-34d0-8db7-34da4dc067c3 | -3.53 | -54.654598 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4407e794-71a5-3c68-97e7-1b656a0e55ce | -2.844 | -54.127102 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39819321-32cc-3d98-9e0c-77ef29c3b7cb | -7.3777 | -46.243599 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39bebec2-fbf0-37c6-9048-67ff0d8f7227 | -6.1245 | -53.064098 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e33cac0-d8e6-36fb-ba68-136bfdfcd119 | -3.5841 | -54.575199 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb1aa94-120d-37c2-b563-555ab1fccc58 | -3.5373 | -54.686901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9477b3d6-ac48-301c-be7c-3b19ea13b8fb | -3.2091 | -50.548698 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 436a2b94-5096-3e26-8ef7-0dbbdf8c67cd | -11.6367 | -43.6838 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8acacb7b-6820-3462-ac01-6bb5a132d268 | -3.0723 | -54.180099 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa5cb0c-35fc-3716-bc8f-2e9475b04845 | -4.8145 | -46.827702 | 2026-10-08 00:48:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31db320e-b501-3f68-9ec4-cb1140081a3a | -7.2119 | -55.178902 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73b2eb86-4ced-315b-bb1e-e0df6894243a | -2.4885 | -56.139301 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51b8d614-9ddf-3da9-bc48-3dc492952548 | -5.8345 | -52.056702 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e84d6e2-8ada-3dfa-9ed5-ae5327d104e2 | -3.0798 | -54.258701 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a83e5d3b-29af-3b92-a35d-0dd417df4f51 | -4.0542 | -59.834801 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ffb555e-446c-35cd-a42b-677b85b21d17 | 3.5405 | -51.2822 | 2026-10-08 00:48:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README41.md)
