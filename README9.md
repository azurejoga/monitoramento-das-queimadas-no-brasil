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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e9b42d3-86d4-3ffe-833b-9d73779933aa | -12.569 | -47.0938 | 2026-09-18 00:39:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 742ba2b3-2b82-3265-97ad-c4a4068d2cbc | -3.4356 | -58.1866 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4991e88-48a5-3dcb-b03e-9c27ca5d3c5c | -12.6416 | -50.8741 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 890f1ea4-d4ac-34d3-b892-bd7576edcdb1 | -4.5048 | -54.9613 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5991ff29-83c1-3743-98ad-2995dc1ac06d | -3.2097 | -53.9473 | 2026-09-18 00:39:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d36c9aa7-f222-3b51-92f2-dd9561ddcbdd | -10.6516 | -50.256901 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3ab17b3-0764-3b27-b3b3-80508d2b30e7 | -9.7022 | -54.825699 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b78e037a-9d7e-39cf-ba8a-0fb469f97ba8 | -12.4446 | -50.659698 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e32185e-f2f1-3124-ba54-3668a2729cae | -3.362 | -50.460999 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995b316c-0549-38a8-81a6-eeade40bb2a3 | -12.3111 | -50.8326 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d02404f-2449-30b1-8e3d-fb3e55b2328d | -3.9571 | -56.124699 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358d37fa-b0b9-3ee6-a533-de503caacca7 | -19.5481 | -47.631001 | 2026-09-18 00:39:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd59d8f3-5273-3b0a-9d4a-54e501fb6f75 | -13.3867 | -57.016899 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3fb7b4d-a017-364d-abd8-680a33155b6f | -12.3218 | -50.7491 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd9770fa-2c29-3af9-af45-db3fd66f189a | -3.9216 | -55.9244 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ab30d83-2768-33d3-9815-f173eba35411 | -9.9412 | -45.3209 | 2026-09-18 00:39:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdcbb5d4-b3bf-3b13-9d22-b51335022449 | -5.7521 | -57.5844 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71379dfc-f1ee-3cc6-8575-d505bbf5b773 | -8.8677 | -62.400299 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3110a4be-f083-3426-ae22-812642a7747a | -12.4084 | -50.680599 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7227a4f8-0bce-30ab-a0a5-2f9655f84a11 | -4.5066 | -54.969299 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef7c4bc-44bb-3032-8563-d540e9c05536 | -5.7938 | -57.632599 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 014e382b-b6f3-328f-84e7-fe191bd1e7c7 | -10.8205 | -50.187901 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 307208ec-0d05-3d8e-85da-f27ab1460fad | -8.9043 | -62.4286 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6c5e30-54a0-3cfc-ba64-066c0c9813fd | -28.347401 | -52.174702 | 2026-09-18 00:39:00 | METOP-B | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7188d26a-82e6-3a65-8ad6-b9f32014b520 | -12.4544 | -50.6572 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8f02676-e38d-3609-8a51-1b3797567ab5 | -3.5917 | -59.062099 | 2026-09-18 00:39:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92a1dddd-ada2-31a0-aa98-3c100e037080 | -2.9013 | -54.1726 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dea8aed-67c0-3f2c-9685-cad6443c9965 | -6.5148 | -49.902699 | 2026-09-18 00:39:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34394326-ae4a-35fd-b525-a48221e43de8 | -8.8798 | -62.409698 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f40d781d-6dc9-31d2-aaa9-76e0f217097f | -8.9416 | -51.459999 | 2026-09-18 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f478b8a9-d22a-37b9-ad27-a1252c7886c5 | -3.9199 | -55.736801 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e78d7dc8-db6d-399b-a2e9-d431359a2b59 | -12.4349 | -50.662102 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b236f37-0f09-3b64-8394-42aa390afd74 | -2.9635 | -50.3367 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3634d397-b7b9-32a6-bce0-7e68b7692e3c | -6.1262 | -59.952999 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 081118ee-6d5a-32a9-a995-87a3cc671f89 | -11.6707 | -54.458099 | 2026-09-18 00:39:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3eea65b3-5458-348c-85d1-850fdf796f7f | -3.4402 | -58.2071 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41e06b63-e173-37ca-8320-a6d39d2fd47d | -12.3748 | -50.712502 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b042cab4-4700-3290-aaa5-2b3bfef101de | -3.4731 | -54.687401 | 2026-09-18 00:39:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1a5631c-9a59-3734-97a6-d94ace07c5a0 | -3.9588 | -56.132 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ab7277-c200-3e20-a389-b92dfe63ca72 | -5.7537 | -45.104401 | 2026-09-18 00:39:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d846c1a-55b4-3ad2-afa4-9965454a9f61 | -8.9092 | -62.403599 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae8605a7-8bb8-3d8a-ba0a-002034ae38cd | -12.5304 | -47.104198 | 2026-09-18 00:39:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3943e7e-233f-35a1-871e-eaf6200ffca1 | -12.1721 | -46.997398 | 2026-09-18 00:39:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e09d2a1-a0a3-3a3f-a530-8ebf3c83e79b | -11.0209 | -54.145802 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb524af0-7fa7-3264-ac20-69172722eed7 | -5.1749 | -56.1758 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92740cf2-3204-3b57-a416-0f35aa3bd429 | -6.1343 | -59.9431 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08a2fec3-7511-32de-84ed-311ffa476cd7 | -10.6352 | -50.2742 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c1f5262-9dc3-321e-a6aa-e1d44e4b0ee4 | -14.888 | -48.144199 | 2026-09-18 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a32d1cc-7ec5-3c52-ac40-4dce7a4b3db2 | -12.3695 | -50.690498 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8844d34-2121-3d6b-8391-e1e00537a866 | -4.4267 | -55.518799 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48966d2c-fa00-3cbb-98fb-780add5d9328 | -3.4401 | -57.977901 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19c173ec-e813-32db-92ad-d6db0aa9a089 | -2.7059 | -57.6031 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6094d94-9af5-33d7-94c6-128f7f16dfd7 | -3.7238 | -60.617199 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee8f424e-ec33-374e-a052-a7535ff9f428 | -15.6369 | -52.725498 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9dbe809-bdb6-331e-aa31-3279ab0bab67 | -5.7856 | -57.641701 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed5a30e8-63fa-3196-9826-f6fb0ec45047 | -6.0159 | -51.769199 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67fafea-4548-352a-8a63-2a9ce5479fcf | -8.8921 | -62.419201 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0f3f75c-7a6a-3830-82ad-3fed3b5fc244 | -3.475 | -54.6959 | 2026-09-18 00:39:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38bb0564-b5e2-359c-8a9e-8c4dcf7bd33e | -6.5208 | -49.885101 | 2026-09-18 00:39:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a4cb27-cdd3-3818-a24c-b47c03b23553 | -8.9892 | -50.167801 | 2026-09-18 00:39:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b12cb9-a16a-3273-9a63-75710b5d9a55 | -12.1575 | -46.980598 | 2026-09-18 00:39:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03e67480-428a-3c14-a251-0d36f92552f5 | -12.2607 | -50.752899 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df71b4c2-5bda-354c-ac78-2fde4e52a49e | -5.3709 | -56.0411 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1faabe1c-8cbe-3e21-878b-29b19ae906d5 | -21.4536 | -48.6703 | 2026-09-18 00:39:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| edd908f5-8dc6-3977-957a-f681a0405ee5 | -4.5325 | -56.071301 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0febf4f-52cc-3c1f-8c1b-0139a6dbce73 | -10.6733 | -50.471802 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c151058-7d0b-3530-a4fe-e762c8ac0a82 | -3.9199 | -55.917 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61bcefd6-965c-3774-a6f4-067f4e7365c6 | -20.0996 | -57.204899 | 2026-09-18 00:39:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 85bd35a1-d68b-324c-a32b-c54cb4982a22 | -10.6486 | -50.244499 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecce37c4-e2e1-38a9-893e-84194dfe08b0 | -2.8957 | -54.193001 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6d5c136-486f-33d9-a20b-b3d6f5b2fe08 | -4.8823 | -56.068298 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c9e31f-c943-3b44-8f9b-ec9b86482b02 | -5.8908 | -53.513901 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f797f962-d2c7-3ab9-8ca0-5a4b9c7cb103 | -4.4365 | -55.516602 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a31ceb31-57c0-39b0-ad46-8693e6c3b7b1 | -4.4772 | -54.976002 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d32414-47ad-3a23-b9ea-bdb168ccabf2 | -7.6714 | -46.0965 | 2026-09-18 00:39:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c1a5c9b-3422-367a-b37a-b0312d5a47ce | -2.7529 | -57.6287 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a206d0b-ffc4-3460-bff7-4a4c43a9db30 | -12.3208 | -50.830101 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5397dfab-c41c-34e3-a9a6-43ef35a9e773 | -8.9442 | -51.471001 | 2026-09-18 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1234abd7-e874-3319-a627-bfc34ded5e3f | -4.5112 | -56.068501 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728c3a5e-6609-39f8-a8fd-6678f3bf0f26 | -2.8172 | -50.455399 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5def89-dbf2-3e34-b191-9da6dc56b701 | -5.7333 | -51.749901 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e101197-4059-390f-b5cd-993665e2e4ee | -10.6509 | -50.4646 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc51dfe-ab7f-3a91-9e94-45688309f9e6 | -21.068199 | -48.459 | 2026-09-18 00:39:00 | METOP-B | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f4feaebf-5009-33e1-bcdd-3a5426a8707f | -11.5218 | -46.876598 | 2026-09-18 00:39:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 306041e5-3595-30de-8baf-010ce36e27d7 | -3.3778 | -50.440899 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f561811a-6ad7-3a02-b55f-2291d4315194 | -9.4871 | -54.474201 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc77ee68-7861-3610-9c65-3d53a6f513cb | -5.6624 | -60.2262 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbed8ede-3bf9-315b-a5c8-bb59e5edd490 | -7.4954 | -55.0079 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a0c101-a5de-38be-9a92-6e1112e2dc40 | -14.748 | -46.2206 | 2026-09-18 00:39:00 | METOP-B | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2946632-64ee-3698-a064-ddc3fcbebe62 | -2.0584 | -52.171799 | 2026-09-18 00:39:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b741ac-5f16-3023-ab0e-2f76e786fe8f | -12.6397 | -50.908401 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 589df981-fad4-3148-a71b-3416e51781ca | -9.7201 | -54.813801 | 2026-09-18 00:39:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b86824f-0687-343a-8b40-6c2478851810 | -28.349001 | -52.182499 | 2026-09-18 00:39:00 | METOP-B | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 341a0687-7f64-3d1c-84eb-54a2405caf10 | -8.9189 | -62.401501 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7738aac-e706-36ef-b3c4-46bb39b8faf0 | -8.8847 | -62.432701 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5f5161f-f8c0-330f-8c49-f02bf62b09c6 | -12.4014 | -50.694 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9eda994b-3937-322f-9337-a4a3baabf43e | -2.7044 | -57.596298 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7078808b-07fe-3c9a-8cf5-82d304b4fa47 | -19.172001 | -48.762901 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f19c592c-535e-31f9-bf91-7d050f822073 | -12.251 | -50.755402 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 843d2bb7-edbf-326f-8bc1-67eaaf349a35 | -5.7505 | -57.577499 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
