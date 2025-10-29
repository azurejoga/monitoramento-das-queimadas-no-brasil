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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9aa8506-ed44-310c-a275-b4c6b7eb1c3d | -10.74637 | -44.7574 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 905bed26-1081-37ee-908a-d873ea3f2c77 | -5.75246 | -43.39124 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da7e1345-e028-32ab-ae2b-25450f47670d | -9.88924 | -47.44764 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c0fd28-a5c2-3ca3-9d35-195e901c7e5d | -9.50713 | -46.9593 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f11df40-fec2-3acf-b688-378c9db2e37a | -8.50872 | -48.27747 | 2025-10-29 04:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd8bd9f-d434-3ad5-adfc-b972c5abe460 | -5.61626 | -47.11419 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d0e61345-24c5-313a-ae8c-e791342dc562 | -7.30856 | -43.96227 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8289804c-e2af-3de4-b4d7-a2100b22ae74 | -9.49323 | -47.00214 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1408906-e914-3dfe-9c9a-dc611d0c800e | -7.33113 | -46.62858 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46a551a2-39cf-3b7a-95bf-20990d7fc189 | -7.08789 | -47.25151 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 960eb4e1-0d62-3470-b78f-34d7af8e32a6 | -10.64396 | -48.00303 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41064ee7-9c04-3a4b-a15e-8af5fc412b12 | -4.87185 | -48.52627 | 2025-10-29 04:23:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 188b9eb0-7336-3ac5-aaeb-0a78c5c2f99b | -7.96273 | -46.7413 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43bc0b60-be1d-3a13-bb20-5d37380b80af | -10.35598 | -47.5617 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbb204c6-a230-30fb-a40a-25be67d47721 | -5.93135 | -42.69184 | 2025-10-29 04:23:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b73b7b7c-fb75-3498-ba6e-32603dc11f5d | -8.47062 | -45.8668 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae35cb4e-2b5a-3bb1-a0a3-8e567fa7ca7a | -10.85245 | -48.64351 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ad98df0-1bbc-3d69-af37-9fe2493080d7 | -8.26045 | -46.34961 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b0e650e-5deb-387c-bd84-c388ccd50af5 | -5.19774 | -46.14864 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf6852fd-fee0-3b3a-9e3a-914155af9e43 | -6.29655 | -41.88633 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| fbd03d66-b2e2-348e-9dc6-b4560a2be4ff | -9.92594 | -47.67129 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a155be-17c6-3918-a885-ecf223a23819 | -7.35003 | -45.14323 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64d523a8-f831-318d-91bc-061cdefce4b1 | -5.54975 | -42.70327 | 2025-10-29 04:23:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d6c16ed-dcd4-3d41-a2cd-263299b7a694 | -6.11457 | -41.71255 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b92b2148-ff7a-393c-b54d-29b77434e474 | -7.98322 | -47.36509 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30152a98-9679-3e0e-965e-639bbf874702 | -6.79813 | -40.97521 | 2025-10-29 04:23:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d22cf8b-6bc8-34f4-b996-70db5125ee1a | -6.90877 | -42.86797 | 2025-10-29 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ce5116da-c285-368a-91ab-7a118bba371e | -10.54834 | -45.0494 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df3f77f9-a92a-3c7e-bf83-9c0c993543f9 | -6.10174 | -42.47055 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 45af0a5c-c740-3e82-b0a0-d8a8128c0aa7 | -10.52131 | -47.72377 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba907e61-e47e-3a49-b21d-030c5e7f7355 | -5.42336 | -44.42872 | 2025-10-29 04:23:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d52d6a2-659d-3b38-8320-deeaa52c1cd3 | -4.91554 | -47.32351 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce1b3046-8411-3f5d-937d-37dc529f678b | -4.63503 | -48.69809 | 2025-10-29 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa4c3919-f28d-365c-9f22-ff457c4ee7f7 | -6.12239 | -41.7095 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0f65f195-93a8-36e1-8239-2e625afc79f0 | -9.54132 | -46.91992 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb1f182-3011-381b-84b9-6474cb071794 | -7.07818 | -44.93962 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f862d6ad-0a8b-3a4c-bb3c-dca850dcc2ea | -8.30809 | -46.83368 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c52ab4e9-c4f8-3273-b568-75f09f7f7872 | -6.16381 | -43.75966 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9b49604-70e2-3058-9725-5a9e88c6f3ad | -6.42359 | -42.32515 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5776c9fe-fdaf-367a-8a48-e9cff4b5daf1 | -6.86195 | -43.44337 | 2025-10-29 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e8c1065-5414-3343-b10f-9d18b43a62a8 | -10.459 | -46.38398 | 2025-10-29 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a75e49d7-acd4-3d85-88a8-e416bd8e3f20 | -9.94341 | -47.09042 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6001145-2142-3b58-bd45-689211fb9261 | -8.54464 | -45.70238 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac881882-70ca-3c26-ab42-ae4f0ea30081 | -6.1539 | -41.67889 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe0a5c24-856c-3aeb-a6b0-ada9f63f341d | -6.82469 | -46.37174 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55e277d2-a03a-35a1-a70d-fbe9a21d230e | -7.24027 | -45.26141 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18c063db-9909-3f29-9451-44aace43b39e | -10.84126 | -44.42134 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b7a2aa1-9dd1-3d4a-97ff-de6e256e4f42 | -10.56304 | -47.79359 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 442e0eeb-1e30-3d80-915a-c0e8812ca539 | -5.34874 | -48.16589 | 2025-10-29 04:23:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e441e44-cbca-3cfe-99e0-d46a9c445bc0 | -9.88863 | -47.4514 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 875c94ac-1c3c-3f8b-a4c5-2b72a0dd47f1 | -10.61264 | -49.61209 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c90417d-7994-3c52-93b4-d0a874c9bc01 | -7.34149 | -42.46961 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6cd65aca-74f5-3cc8-baab-db6b933bac73 | -7.31317 | -47.81942 | 2025-10-29 04:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1afde9c-3d29-3bf2-b0c8-e7854609660f | -7.80135 | -46.46468 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69e83367-459f-316e-b2f7-88c0d034ad14 | -7.44822 | -49.41337 | 2025-10-29 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 754d1077-329a-3c03-b691-6c4f9f2ca47b | -7.09398 | -45.24855 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fff05ac1-8197-38bc-b720-3442f63c3549 | -6.14762 | -41.56989 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 180a95c9-f1c1-3caf-ad20-86bc0bf039dc | -6.23722 | -42.76408 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c58ac236-d7fb-3c81-8395-81b97724f1c3 | -5.81706 | -50.06422 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cef9a1d-ac21-3450-90fe-9c8525840fbd | -8.0247 | -47.39561 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a272608-7766-383f-a8e6-43f464dd0102 | -9.91261 | -45.92978 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9be1c194-5e82-36cd-b312-0dc7c2ca100f | -8.7624 | -46.51424 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df890b36-23d7-360c-a206-1bfc112462d0 | -5.19315 | -45.62664 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e6db95c-2f9a-391a-a5c0-b28d96f92448 | -9.18324 | -48.84447 | 2025-10-29 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fee4413-d81f-3b34-b59b-13873c5f3c97 | -6.09262 | -41.78379 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d152d2ad-bf75-30b1-b04a-e3d0d52cba55 | -7.19273 | -46.75046 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8356d20a-38ed-3044-bd8a-2f8276e2f168 | -10.77619 | -45.10771 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67031251-93e0-3fab-8ff7-61c2a4866fe6 | -5.52488 | -45.43284 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5f882a6-8d88-3ca6-aa49-37514a8b026b | -7.50138 | -46.74353 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab68080e-7c01-3569-94c9-8eaa771bb7e9 | -7.79796 | -46.46414 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a25c084d-4b3d-368d-bd91-d5426924be77 | -9.80834 | -48.14444 | 2025-10-29 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3939d721-456c-372b-ba1a-a23ba9b298f3 | -9.33811 | -43.10153 | 2025-10-29 04:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28f4af65-1895-3af5-8c77-a6e1f4e536ec | -11.27181 | -45.5266 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96fba29c-d6a1-3de7-bb4b-d3f75640f8ae | -10.65914 | -47.99765 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d11244b9-3b7c-32e3-b49f-9d8fefb4151f | -6.13895 | -41.85119 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43fa65c1-4e2e-308a-8986-d605ce6506f1 | -8.00628 | -46.20996 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1d8c26a9-9929-3a51-900e-3eaf880f8ea8 | -7.36344 | -47.63685 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9e667d9c-f41a-3cad-8714-4e5e67258fbc | -9.44586 | -46.90788 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7c82d18-5060-30fe-83ca-a4c9ea82a64d | -7.69026 | -46.89556 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b5024ac-0400-34c7-9e24-86c637e25412 | -6.15061 | -41.57448 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 201aa3f6-e34d-3ace-b147-6e61ab5464bb | -10.39022 | -47.11782 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 831e9ca1-e6fa-334a-8095-bc8b54d5029a | -5.41306 | -45.21746 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b4413ae-b06b-367e-b21f-1ae0498a49e3 | -6.12531 | -41.84483 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2725a137-b6aa-3131-8233-3f6ced452f54 | -5.59538 | -46.23795 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07826322-5a71-3ea9-ba93-e9ecf121bc1b | -8.21478 | -43.8062 | 2025-10-29 04:23:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f4818dd9-b2ed-3c55-bd69-8209d658cae5 | -6.27942 | -42.87719 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae75aa14-86d4-315c-9ad1-6f96a010b88b | -10.5028 | -47.72849 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 207db471-9256-35dc-bd16-73fa5e17382f | -10.95486 | -47.61615 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be1e4918-a320-3a55-ba10-e161dd430ffc | -7.44467 | -39.26858 | 2025-10-29 04:23:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 465b2a7e-528d-394e-bd05-9977266a3300 | -8.1901 | -44.45112 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc764388-3e6b-339e-8dc2-cfed1c536b7f | -8.32617 | -46.15514 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7aa4781-8c5a-329a-b27d-678c48700ca6 | -6.34645 | -46.36732 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03fb16cb-d4d5-3a88-999a-4b1b3d5b9dbf | -9.9032 | -44.91487 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71ea6583-560e-33f6-a636-7a5708e7ea97 | -6.27237 | -43.88824 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34b26a79-8ee8-38cb-9567-23d1bfebbb26 | -9.49205 | -47.00946 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 31df7d96-1f84-3483-900f-e77c0255b3a3 | -10.75279 | -44.75076 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac8c818a-b8e8-3f03-a4ec-f0d61d915c51 | -8.18343 | -44.45006 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14d0839d-db28-357f-a0eb-431847212ab2 | -10.88474 | -47.99484 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e856445-5350-3fc5-a083-74c3328509a7 | -10.46454 | -46.39218 | 2025-10-29 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0b178bb-cf2f-3607-bb87-f3cc1b04104e | -7.32512 | -46.72995 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
