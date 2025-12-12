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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b08ed9b4-098b-3fbe-b685-b50ed9aad414 | -2.4848 | -47.772202 | 2025-12-12 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e4b6402-5580-3f26-95d9-01269ed636ad | -20.3836 | -41.319801 | 2025-12-12 00:14:00 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67f96582-9615-371a-b527-16248c254c6e | -2.9698 | -52.708199 | 2025-12-12 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f306c8-ddd2-3516-beb4-b9ec080d58c4 | -12.4151 | -57.984901 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 750cf6df-1644-3495-b462-f1c20f4aafe2 | -2.2095 | -45.379501 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0048ba85-6b3f-3399-822f-d5ab01bba039 | -2.4242 | -51.933498 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d46be34e-4538-3227-8060-e11fc97189a2 | -1.24 | -46.743099 | 2025-12-12 00:14:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d3135c-8d1d-31b1-a103-1bc6b83c4747 | -2.1393 | -45.652302 | 2025-12-12 00:14:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0f9b937-eb28-3325-8ed3-ffe26bcad233 | -2.4324 | -51.9244 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ae3e21-9f1d-3ce4-ae48-e16959eee387 | -6.1054 | -41.280399 | 2025-12-12 00:14:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cc5b97b-e2ab-3392-b570-d2437609322d | -3.0237 | -52.8106 | 2025-12-12 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06917d45-d7da-35af-9384-3db80b3371e9 | -2.8917 | -53.0014 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86242b11-4960-3703-89a3-18a2fb8d5e2e | -6.115 | -41.278 | 2025-12-12 00:14:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71f973c8-96ee-31f5-878a-200e5589b2ff | -2.4504 | -51.913101 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c808c0-f3f2-3cfb-94ed-0070649a4094 | -20.9562 | -48.7575 | 2025-12-12 00:14:00 | METOP-B | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae2ca9c6-edc4-3b82-9ae7-d27fbeaf2852 | -2.5322 | -45.5742 | 2025-12-12 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5cd247-c379-3201-b264-aab9cf5dd416 | -23.3016 | -45.637798 | 2025-12-12 00:14:00 | METOP-B | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8fe6c654-e921-35d0-a08f-4d7c735533bd | -3.6789 | -52.521099 | 2025-12-12 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca80a8be-81ab-3838-bb0d-e4599338fd78 | -23.2999 | -45.630299 | 2025-12-12 00:14:00 | METOP-B | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f31fa893-af62-331a-b2b0-43cee3e85ec6 | -12.4091 | -58.006699 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e62330a8-149b-30b6-bb1d-502cb893c4c4 | -3.6255 | -45.369598 | 2025-12-12 00:14:00 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 510d0c94-034e-321c-a215-d8d960cdd6bb | -1.4432 | -46.8223 | 2025-12-12 00:14:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34a9f2f8-f200-380d-903f-2be77130e0a3 | -12.1996 | -49.532001 | 2025-12-12 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41d5d822-7b8f-343b-a160-a6c738dd64de | -2.222 | -45.389198 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 289e6b69-8a9f-30ff-862f-eed0affb04c1 | -2.434 | -51.931301 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195656ad-210b-32ab-9a64-a47eaa16a16c | -2.6555 | -51.636101 | 2025-12-12 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 644e1b6d-b802-3717-8311-d5fa6cca763a | -3.1225 | -54.1665 | 2025-12-12 00:14:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746e7513-070c-3b57-91bb-f67a16ec9ad8 | -1.441 | -46.8125 | 2025-12-12 00:14:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9727747-ccf1-34bb-8465-c64d8dd34340 | -2.9359 | -53.0149 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e370df6-d05e-3962-9f38-493a67685032 | -2.7477 | -52.9561 | 2025-12-12 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6943b1f2-27d5-3548-a5d0-045ed55efc41 | -2.2275 | -45.412701 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c39e25c1-8392-3b8b-b827-a3c6b92a2553 | -2.4829 | -47.763802 | 2025-12-12 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84851cdb-5362-3167-8f41-dc6ffb5be6ed | -2.2248 | -45.401001 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5571e35-c521-33a7-bcc9-ed41bc3bc114 | -2.4809 | -47.755299 | 2025-12-12 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a0ebee-a7e6-376c-abaf-c274b425f729 | -12.4053 | -57.986801 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0ff3693-1e52-3ae3-9f9a-1f485813d5f7 | -2.8897 | -47.786499 | 2025-12-12 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3769f3-5ebb-326d-8ccf-44a8a1671202 | -3.1341 | -54.172699 | 2025-12-12 00:14:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff9393f-9eec-3d76-b6c9-63f318bc161b | -20.380699 | -41.308201 | 2025-12-12 00:14:00 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a6569f1-be5a-314c-9acc-8e99d3e57601 | -2.2193 | -45.3773 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd66033c-2e17-3eef-a501-86b10681df02 | -2.4438 | -51.9291 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 297ed8b5-be6f-3fbf-98a0-89644a96a91f | -2.6929 | -45.691101 | 2025-12-12 00:14:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4725b363-3e76-3545-909d-b11c7123b1cc | -2.4226 | -51.926601 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d75318f-0c4f-3bc8-b787-93a0e1837cdd | -2.2318 | -45.386902 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff621e5-b8c8-36fa-9ba6-f3478d470bde | -3.8118 | -50.601898 | 2025-12-12 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8174a38-9654-339d-b3a8-b4994a77d149 | -2.1367 | -45.6409 | 2025-12-12 00:14:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e842b1a4-ae55-3919-8486-cf06a36591b2 | -3.621 | -45.394501 | 2025-12-12 00:14:00 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93d6c4be-8f22-33fd-8bb8-d76069c6b31f | -3.2361 | -47.457802 | 2025-12-12 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c86cc6-6890-3c33-84d0-8e1571e7f11e | -2.4277 | -51.903702 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d791722-4b96-321c-8a31-554ee3866d42 | -3.1322 | -54.164398 | 2025-12-12 00:14:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de9388ad-aaf2-3d35-8cbf-7c8a486f30f0 | -6.1005 | -41.260899 | 2025-12-12 00:14:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5e6f070-8660-3920-953e-ed1483b98453 | -2.4293 | -51.910599 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c56146b-edcf-30b5-83f0-7bde9fff5138 | -3.6183 | -45.383202 | 2025-12-12 00:14:00 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78100079-9e18-3409-bb0d-95488ec25f95 | -12.5066 | -58.305599 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d54a786-7ee2-3556-a381-30a60d67bfc2 | -1.7907 | -45.7439 | 2025-12-12 00:14:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 946c6dd9-5891-32f3-ad14-a9c281acd1bd | -1.4674 | -46.257301 | 2025-12-12 00:14:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab7e3cd4-952e-3703-b5ff-5700cecac2d7 | -2.8819 | -53.003601 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8b29178-9007-32cc-be51-02c80991614b | -12.4189 | -58.004799 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08817091-ddec-3759-8460-c43a2a48a7ec | -2.89 | -52.993999 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913d7dc4-a527-3853-bafd-708e564b2dc5 | -2.7493 | -52.963402 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb9fa57-a43c-3345-9288-6e066cd862bb | -2.4179 | -51.905899 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdf6586-7ddf-319f-8075-30c9e8ca021c | -2.8313 | -46.7309 | 2025-12-12 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb603e21-818a-3fc2-865b-d9dc116f7ec1 | -2.4308 | -51.9175 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2941ec1d-842c-31b3-a149-3296021562b0 | -3.6371 | -49.472698 | 2025-12-12 00:14:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 375332e2-c62c-3ddc-9517-8198904f8893 | -3.8713 | -50.955101 | 2025-12-12 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8abc1418-f272-31ce-b21c-894c0ca6b3ae | -12.6187 | -58.049301 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7672102-6643-3bd9-bae2-079b18e84b46 | -2.8291 | -46.721298 | 2025-12-12 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec8b010-c4ae-3bb8-ab59-f5873ee4f655 | -2.9457 | -53.012699 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 077b7909-7449-3078-a7ed-935622992aba | -3.0454 | -52.998402 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab805568-e647-35b7-bf14-174db23b8b51 | -2.8802 | -52.996201 | 2025-12-12 00:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac175e1-3625-3bdc-a43d-a9f8830ee01e | -2.3293 | -45.762798 | 2025-12-12 00:14:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 951fa448-4afe-31ba-a6ad-27da553c77a1 | -1.7933 | -45.755299 | 2025-12-12 00:14:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92603ae9-3897-3efc-9410-44116b37300e | -12.4228 | -58.0247 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45f5df75-6126-381f-b643-a9f05ce63669 | -4.3715 | -43.611698 | 2025-12-12 00:14:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efaae9ac-0f6f-3d2a-9773-caeb7c518394 | -3.4795 | -50.862999 | 2025-12-12 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529794a1-fc60-3b5a-a13f-b5cc4899c30e | -3.7996 | -51.367001 | 2025-12-12 00:14:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6695f8d0-174b-3b88-b0b5-e9d7208b19f5 | -2.6903 | -45.68 | 2025-12-12 00:14:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6273a2-c066-3186-8279-46b114a15368 | -2.2345 | -45.398701 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c420710-201d-3158-93c1-b772b424e487 | -6.1054 | -41.2388 | 2025-12-12 00:14:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 495f9811-4109-3a69-80ea-a3a7bfb175a9 | -12.4248 | -57.983101 | 2025-12-12 00:14:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4acac450-132a-3a0d-a15b-51382632cc58 | -2.6663 | -45.7089 | 2025-12-12 00:14:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3633bf-1fba-3883-8aea-c756f63978b3 | -2.4406 | -51.915298 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd2aa060-6698-3b3f-8781-94f7cc0db3d6 | -5.4667 | -47.081001 | 2025-12-12 00:14:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dbf7c3d-1325-323a-be8c-bc31d32a4b54 | -2.2122 | -45.391399 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 931869a7-7b81-38fe-8570-929381558eb5 | -2.8917 | -47.7948 | 2025-12-12 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf47a0f9-2ca1-3182-afbd-09e986c41f8d | -3.6281 | -45.380901 | 2025-12-12 00:14:00 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe62bbd-0470-3746-a6b9-7c8914c2cb5d | -2.525 | -45.587799 | 2025-12-12 00:14:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f22f173b-cb5c-3b29-a2e9-1028be134701 | -2.7741 | -45.554401 | 2025-12-12 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8da0f718-8643-3dc4-bb2f-be3235dbb877 | -2.421 | -51.919701 | 2025-12-12 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9e03eeb-ee11-300f-a8b6-bae7574821e3 | -2.215 | -45.403198 | 2025-12-12 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6ebcab-bb3c-3946-85ef-c30928ac28b6 | -1.2423 | -46.753101 | 2025-12-12 00:14:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526bb742-7121-3dbb-b168-4234fcc1ac2a | -2.5481 | -45.201302 | 2025-12-12 00:14:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b93d1fc-bce9-3554-93be-296eb7ce295a | -2.6689 | -45.720001 | 2025-12-12 00:14:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38eafe72-6a91-3595-80e3-a344413447e2 | -4.745 | -43.0576 | 2025-12-12 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ef7934e5-6a24-30d1-a88b-25c513678cc8 | -3.0696 | -45.7917 | 2025-12-12 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 4fbf988d-771d-31f0-9dea-a44d69449122 | -3.0511 | -45.7924 | 2025-12-12 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| dd84a56f-f6c3-3809-9b9d-22602357d992 | -12.4133 | -58.049 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 251.4 |
| f7435c57-acd6-38d8-960a-6cef2b73dd31 | -12.3946 | -58.0307 | 2025-12-12 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3430a323-a52c-3d10-a681-8a2da4c21150 | -4.3856 | -43.6381 | 2025-12-12 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a5e98454-575c-35b4-a8b1-f99465d092f6 | -6.112 | -41.2649 | 2025-12-12 00:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| dcdd285a-524b-3418-80a0-e3f27b703d4e | -2.1419 | -45.6644 | 2025-12-12 00:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |


[Clique aqui para ver as próximas entradas](README3.md)
