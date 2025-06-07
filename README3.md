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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dc1c53c-aa89-3311-9de5-be5a494f3bd4 | -11.2548 | -60.7957 | 2025-06-07 00:40:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1398e859-65c5-3bc6-9e04-4e2bbd24ac2d | -7.7361 | -44.1823 | 2025-06-07 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| dc7eb718-7568-3487-bd58-560ad25aa323 | -12.5238 | -58.3378 | 2025-06-07 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 6d261b7c-3c42-3ce3-828a-1d0794bdf276 | -5.6379 | -43.7175 | 2025-06-07 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 3802d462-2c45-3e4c-9eda-8818edb982ff | -13.4733 | -56.8557 | 2025-06-07 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5b0551ab-a56e-30a3-b4b0-15f7aa4645ad | -7.7364 | -44.1592 | 2025-06-07 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0db05a6b-aad1-3c8d-baf5-d88614284051 | -6.9605 | -42.8816 | 2025-06-07 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| c9f8a5c5-8e87-305b-9fc0-52ff98cae66e | -7.7176 | -44.1611 | 2025-06-07 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 519fcf6e-1a98-3934-9f3b-2676ec022aff | -12.2938 | -50.105 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f62c10e-ff5c-3c68-bace-2e16e71bd716 | -10.3013 | -57.135101 | 2025-06-07 00:47:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 737aa140-56a3-3927-88f7-c28873b875ca | -13.0942 | -52.277 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd8ba6c0-7075-3a45-a846-731a5bc81bf1 | -9.0685 | -47.145 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9643800c-ed51-3cab-8528-62ebbf3007ad | -10.8846 | -54.305199 | 2025-06-07 00:47:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48062833-891b-38f8-972a-c72e2fc57cd9 | -6.9476 | -42.888802 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fef5a00c-dede-36be-80af-115518f7be6e | -7.7164 | -44.174702 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88c0139d-9dcd-3a65-9108-efe8a89dd46d | -12.5337 | -58.349701 | 2025-06-07 00:47:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c92c5d58-90a5-32ef-ba82-447266f756eb | -13.4668 | -56.864899 | 2025-06-07 00:47:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4fbe52d-64a8-346d-b674-e824bbc3a770 | -6.3081 | -48.492802 | 2025-06-07 00:47:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe034bd-9d80-39ef-8870-9777c5837847 | -12.9643 | -46.759701 | 2025-06-07 00:47:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fabf9a57-0139-3e08-aa68-f646f472f8f9 | -13.4698 | -56.828602 | 2025-06-07 00:47:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82651688-8ed5-30b6-844b-838983cce7d7 | -12.284 | -50.1073 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50a26bcf-ad01-33fd-aa98-27612866ec4c | -11.8152 | -44.251598 | 2025-06-07 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf8ec57-f302-333e-a922-215a3b17b07c | -9.4029 | -48.445999 | 2025-06-07 00:47:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9828d35-8b0f-39c8-a121-04bed33f93ca | -11.7842 | -47.4105 | 2025-06-07 00:47:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72a74b29-3017-3a8e-bb74-435bac1c1783 | -13.096 | -52.285702 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93704578-0717-397f-ad9b-9d5c38dce79f | -7.0154 | -44.600498 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3268854-2fc3-3471-a502-2f26b24599cd | -14.7254 | -45.0755 | 2025-06-07 00:47:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79d7eb48-ccc7-370a-875b-b4ab0e8333a4 | -10.5018 | -53.658298 | 2025-06-07 00:47:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebbb8df9-80ba-3387-b3c4-6cbbbf78ebba | -10.5038 | -53.667999 | 2025-06-07 00:47:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5825bb2-8ce2-316e-b7b7-938fe6b5e720 | -20.928699 | -49.1008 | 2025-06-07 00:47:00 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18cae57e-9c36-3c39-b67e-7992a051e319 | -12.2723 | -44.5989 | 2025-06-07 00:47:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72657c7d-f480-3071-b78a-7fe0e5dd48b1 | -11.3682 | -56.5448 | 2025-06-07 00:47:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2329f67-4f9f-3085-bbb5-873d8ccaad3c | -9.5463 | -47.774399 | 2025-06-07 00:47:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51c3de90-d563-3983-aa92-4cea0dde571a | -13.0691 | -49.242802 | 2025-06-07 00:47:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25f608c5-0fcd-3945-841d-effd8712087d | -11.808 | -44.264198 | 2025-06-07 00:47:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbaaa849-23e0-3a57-b907-9a588922a5fc | -10.494 | -53.670101 | 2025-06-07 00:47:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be34705b-cd79-3dae-ad72-c9d863f102a2 | -7.0181 | -44.611801 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7bad2bb-c6ef-3cdf-96f6-b67d9502d68d | -8.2158 | -48.978802 | 2025-06-07 00:47:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 42637beb-9cf9-39ca-a3b5-e7c8baa221cf | -7.7388 | -44.181702 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf2494b2-d1c1-3fc9-bc99-1c52042f9da0 | -7.9041 | -50.364799 | 2025-06-07 00:47:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f0de5c-f20f-33f9-a6bf-a834cd1fddef | -12.3282 | -52.479401 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba980d1e-6e3d-33e2-91ee-64ae558038bb | -5.6399 | -43.729198 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb250572-fe61-35d6-ac31-54d36a63fdfa | -7.7193 | -44.186401 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fdd33380-8708-3230-a200-01a49b101023 | -8.1725 | -46.4995 | 2025-06-07 00:47:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 472b8d1a-bf98-378a-8ada-d96c345ef7c6 | -7.7233 | -44.160599 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa62a88-32b2-3c1e-8ddd-0d8dc9a6028d | -6.5952 | -43.888699 | 2025-06-07 00:47:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56ed57c3-96f3-329b-b783-1ff912dd82d8 | -7.2093 | -43.114601 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 053d024e-7f53-3208-a6ae-3478be0156aa | -8.4465 | -46.479301 | 2025-06-07 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acf5fa5c-e958-3267-ba2b-9f16c4996bf1 | -12.2809 | -50.092999 | 2025-06-07 00:47:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 085eb02a-04db-31a0-bbd0-98777795d38b | -7.8607 | -47.893501 | 2025-06-07 00:47:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7dfa805-f5dd-3d68-822e-746ba7671fb7 | -10.4997 | -53.648701 | 2025-06-07 00:47:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dab7adb0-4ed2-33c8-9054-bb71bb08d945 | -10.709 | -48.787498 | 2025-06-07 00:47:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af032904-1974-3280-b158-2e13bf8b856d | -9.0801 | -47.150501 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a812e45-3b9a-306b-97d1-155511a4e8d0 | -12.288 | -49.525101 | 2025-06-07 00:47:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b196c4a9-620c-33c0-9c1f-f99522f0283d | -12.338 | -52.477299 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7c3d55-54b2-311e-9a92-a1f8f980cb64 | -12.9545 | -46.7621 | 2025-06-07 00:47:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b976fc7-ab5e-3041-9d9a-b58aefc11588 | -12.3361 | -52.468498 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6344fc1c-9434-3df0-8e92-247935687c11 | -8.4485 | -46.487801 | 2025-06-07 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52dc7a49-fba0-30d0-a9ca-c888a82c4ca0 | -12.7876 | -48.725399 | 2025-06-07 00:47:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4431ac3-8822-37f7-a232-6e7b9e16ae63 | -12.7861 | -48.718399 | 2025-06-07 00:47:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d753f65-313a-3732-bfde-a23d53f6c6c8 | -17.812599 | -51.011902 | 2025-06-07 00:47:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 585474af-9c1f-332a-a89b-5e614c050916 | -8.4583 | -46.4855 | 2025-06-07 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1648ea6-695b-3504-9d08-6700c7799283 | -12.7763 | -48.7206 | 2025-06-07 00:47:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00d3f5c8-1b86-3170-9576-0871716b3610 | -9.0703 | -47.152802 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8848e1-b172-3793-bd4a-564fc87365e2 | -8.1745 | -46.507999 | 2025-06-07 00:47:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4466532-8097-3c88-8506-14c13343088b | -17.2612 | -42.6604 | 2025-06-07 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6f7546-6af1-3fdd-9e0d-c57829eafdc6 | -6.2381 | -48.547298 | 2025-06-07 00:47:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9dd4eb2-37c7-3c37-82db-2461f285bafb | -9.556 | -47.772099 | 2025-06-07 00:47:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 599a522d-3f16-3b31-a23d-69bea33e172b | -7.7136 | -44.162899 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff1c526b-e7be-3ca8-a7a1-b79a3c4bb40f | -20.927099 | -49.0928 | 2025-06-07 00:47:00 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c2fc33b4-4f36-38fd-8baf-7afae256ead2 | -11.3712 | -56.560101 | 2025-06-07 00:47:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee154a7-3e1b-3d82-9fa2-c2492fadd47c | -13.0707 | -49.249802 | 2025-06-07 00:47:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4918be-28c7-3d71-a049-3a5f45fa3f6e | -12.5199 | -58.330601 | 2025-06-07 00:47:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08b2f9dd-15e1-368c-830b-fffa1434c455 | -6.6666 | -47.730099 | 2025-06-07 00:47:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 739e037e-e498-3dd3-89a0-debad6094c3b | -7.7107 | -44.1511 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15e8d845-d025-3c6a-a33b-a37067132ea0 | -17.2682 | -42.647099 | 2025-06-07 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b71b5839-a49c-3fac-a611-6bae14c95936 | -9.4013 | -48.4389 | 2025-06-07 00:47:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63bc990c-c314-3155-91db-404dd89a1322 | -17.258499 | -42.6497 | 2025-06-07 00:47:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b6597a7-c26c-306b-9da0-061c8459ffbb | -7.7262 | -44.172298 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 593034a4-da92-3778-a4ce-ae413b34b575 | -11.2495 | -60.757401 | 2025-06-07 00:47:00 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07b80eda-c2a1-35c0-9fa4-d04b2872912c | -12.7845 | -48.711399 | 2025-06-07 00:47:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bf6156a-6e1b-3b8c-9f43-d53b9d085385 | -12.4796 | -54.4189 | 2025-06-07 00:47:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d0a35d8-ae77-34b4-8d94-faeacf73bf6c | -8.2076 | -48.987999 | 2025-06-07 00:47:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b2bb17c2-9115-348c-a5a7-635c00f6cdc0 | -6.9646 | -42.915798 | 2025-06-07 00:47:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3d95453-9232-385a-a717-107b712970d0 | -11.7825 | -47.403198 | 2025-06-07 00:47:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17a64125-94b8-3503-b041-c8887e96dd9a | -13.0789 | -49.240601 | 2025-06-07 00:47:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cbf04a11-faa6-3f5e-8f18-c6142a8631c4 | -5.6366 | -43.715698 | 2025-06-07 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab3e55c-7fd1-329a-bb86-25a165f1ddcd | -13.4634 | -56.847698 | 2025-06-07 00:47:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b840325-0daa-3051-82b4-08a67a7b99dc | -13.4765 | -56.8629 | 2025-06-07 00:47:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9869f7-ce6b-357c-8854-69c986810e53 | -17.8144 | -51.020599 | 2025-06-07 00:47:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ee22aad-cbb4-3d48-bad4-9df59ad1e25d | -12.524 | -58.351601 | 2025-06-07 00:47:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e710c5c-88fc-32e1-9803-17c792c25f5e | -12.9661 | -46.7673 | 2025-06-07 00:47:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7193a6b5-594b-3520-ad2a-35a67d2b4298 | -18.2358 | -47.939602 | 2025-06-07 00:47:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1362d31a-79fa-36c7-9983-6cd171a5fbe4 | -10.8823 | -54.294601 | 2025-06-07 00:47:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d768c8fa-b9c6-3111-b19e-22040096f191 | -7.0084 | -44.614101 | 2025-06-07 00:47:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5e39fa-201a-3eba-a684-24c4cc0abf8c | -7.7204 | -44.1488 | 2025-06-07 00:47:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8128d5d7-3eb4-3b0b-b799-e09b6e1d6251 | -9.0764 | -47.134899 | 2025-06-07 00:47:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f85dacf-d59e-3240-8e18-b08a3f308404 | -12.3263 | -52.4706 | 2025-06-07 00:47:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df471e70-63a0-31b7-b742-ce61f43dfeef | -11.7808 | -47.395802 | 2025-06-07 00:47:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06363bb3-19da-3f76-ae9c-6940e1126d14 | -10.6546 | -49.3629 | 2025-06-07 00:47:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
