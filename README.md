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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee27c67a-18cb-3625-879f-e55f1552dc2f | -13.4234 | -46.8503 | 2025-08-28 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1907c3f0-40e6-39aa-b484-eb931f2af59e | -10.4736 | -57.9563 | 2025-08-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f9e9a8f4-8918-38d1-b3cd-60070e06aca7 | -8.9478 | -65.9802 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cf3407a5-fc06-3f0d-94c1-27897c522e61 | -3.2485 | -43.4406 | 2025-08-28 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0af32438-d814-35b6-b35d-085656cded66 | -5.3285 | -55.8878 | 2025-08-28 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f6647200-d452-3289-a50d-a05d8b171bff | -9.3169 | -57.6967 | 2025-08-28 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| afdb9384-16ff-3220-9e3e-a41e33628fa4 | -6.8772 | -43.6152 | 2025-08-28 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ac7b936f-4661-3eeb-be89-10e046d689b5 | -9.1339 | -65.788 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 543.8 |
| 9c135a39-29ca-3e82-8fb7-4b5ffe95bd43 | -9.134 | -65.7694 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 347.8 |
| b6a718dd-01c9-3e94-a6dd-89ae190e4141 | -8.948 | -65.9429 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ed93c1b8-8729-3456-9c50-2ecfefe1e72f | -13.1837 | -45.2865 | 2025-08-28 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 3388bebb-21f1-3100-a004-677ba8150844 | -9.1154 | -65.7886 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 363.6 |
| 51a5fd8f-b78e-326c-b88b-b7906d747013 | -9.406 | -60.5711 | 2025-08-28 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| c9ff1067-6ad7-3f13-a7bb-57f6437b6cc4 | -9.1363 | -65.2835 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f99f4645-8221-31a4-86c2-1ee4a5c55fc9 | -11.3526 | -43.5187 | 2025-08-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b10a7483-bcdb-3ac1-9dc7-5328ffd798f5 | -9.4862 | -51.9595 | 2025-08-28 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7e2813e5-7a8d-31a7-a42e-00e05fb2ed81 | -3.2299 | -43.4414 | 2025-08-28 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 205.0 |
| f652cfc6-728b-3d22-9f58-da4465137ad2 | -7.4283 | -40.079 | 2025-08-28 00:00:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 104.4 |
| f18732b0-c027-3815-8fb1-1ea717033f74 | -9.181 | -60.8131 | 2025-08-28 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7283755c-3bbf-3bf0-b6d5-01f205e4a061 | -8.9665 | -65.9424 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 08ad508f-40a2-3948-a64d-59bf8b6a6e29 | -21.6626 | -48.797 | 2025-08-28 00:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1a27791f-9074-33a8-87bc-38eafd3e783e | -3.23 | -43.4182 | 2025-08-28 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ff680627-ff65-33b8-97ff-b8c56b00db8f | -9.1338 | -65.8067 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fcb49fe7-6a4c-3e28-abdd-0269ffd05d77 | -9.1155 | -65.7699 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 229.1 |
| c679ed6d-fcc2-3eca-8821-a7844fc7e228 | -8.9479 | -65.9616 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 42d3153b-e02e-35ec-baca-cecedb54ad96 | -10.4738 | -57.9366 | 2025-08-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| ae4d24a2-d936-35ae-95d7-d62f08c0506c | -11.3521 | -43.5423 | 2025-08-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 70e27fd2-c660-386b-9475-8da4c0b0d7a9 | -11.2189 | -55.0585 | 2025-08-28 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 7bf4f282-7f22-39c8-a570-8cd5ca37cf53 | -9.4676 | -51.9403 | 2025-08-28 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 214d83bc-d2e4-3c66-803d-f9839cd161f2 | -13.1842 | -45.2633 | 2025-08-28 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e0f3da7a-5ea4-30a7-9049-2c934bfdffc5 | -7.3542 | -59.6476 | 2025-08-28 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b1aca7ba-37c6-3839-9e02-619d6d6aaa0f | -10.8421 | -60.8009 | 2025-08-28 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d455a895-fb54-33ea-9150-66d450540a20 | -13.4427 | -46.8473 | 2025-08-28 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 2e635c88-0432-32bb-bd3b-ef9cf4c52e9b | -9.4864 | -51.9387 | 2025-08-28 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 322.2 |
| bab1d9ad-8f9a-3f9f-b17c-39a08926b261 | -7.6242 | -60.8448 | 2025-08-28 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d1be3d66-cf4b-3170-995e-92ad66b77fb9 | -13.7566 | -51.9053 | 2025-08-28 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f724649b-f822-37c0-889b-7034ec6a59fb | -4.8079 | -47.2604 | 2025-08-28 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ee439cfd-6e41-3817-ae64-cc41403d2013 | -9.4867 | -51.9178 | 2025-08-28 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 675d2c07-80d1-3cce-9207-f853cbaca1b5 | -8.9664 | -65.961 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| e216a062-e6de-3d44-9269-711ce47989b9 | -11.2378 | -55.0569 | 2025-08-28 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9d10463b-219d-368b-82e1-c7be3d949731 | -11.3334 | -43.5216 | 2025-08-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| a89c673c-84d0-3ea7-b28a-8b8e7e7f73d1 | -11.3329 | -43.5452 | 2025-08-28 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| fe37deee-09ec-300e-bad6-121826be7d25 | -12.8032 | -48.1516 | 2025-08-28 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 81039bfa-3998-382f-9c34-09e19b47cc8d | -4.7893 | -47.2614 | 2025-08-28 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 559df996-b04d-317c-bbbe-f77e16cec56b | -9.4061 | -60.5518 | 2025-08-28 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7b2b6223-5d08-3ff7-b905-1002f6cb274c | -6.9129 | -62.9366 | 2025-08-28 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ea5a76a4-c114-3ba3-b9fb-0c65701eeab8 | -9.1153 | -65.8073 | 2025-08-28 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0fa291dd-430e-346f-87ef-363606a3970c | -20.12327 | -44.33901 | 2025-08-28 00:07:00 | TERRA_M-M | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c1b81d09-36b7-385c-84bc-8e2d60ad2ae8 | -19.91409 | -41.57378 | 2025-08-28 00:07:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7ce5a9b6-859a-3aca-a4c7-de4309abafac | -19.90626 | -41.58506 | 2025-08-28 00:07:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 500f4d05-7cd9-3b48-8746-6afe99910964 | -20.25425 | -42.00274 | 2025-08-28 00:07:00 | TERRA_M-M | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| c43ceef0-af3d-3131-8d32-be83d85e8ef0 | -19.79479 | -44.94442 | 2025-08-28 00:07:00 | TERRA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 82c35a65-5745-3938-917a-fdd85865cb6b | -21.64949 | -48.78323 | 2025-08-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 971ee4e0-dcef-3c26-a7bc-3757f71d3572 | -20.25557 | -42.01307 | 2025-08-28 00:07:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e6caeef2-6cc9-3777-8921-f04c24d253b8 | -20.40643 | -45.11137 | 2025-08-28 00:07:00 | TERRA_M-M | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| f446b52f-185d-3b65-be98-1daec082b3e8 | -21.49784 | -45.49825 | 2025-08-28 00:07:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8d363d70-ea00-3352-b60c-6e4e72fa8447 | -21.65585 | -48.82173 | 2025-08-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b60dc801-bc39-30cc-817e-ec206b34c288 | -20.56303 | -41.61879 | 2025-08-28 00:07:00 | TERRA_M-M | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 1730bccc-f8e0-30d1-b697-cb69545b2ba0 | -21.20269 | -45.4072 | 2025-08-28 00:07:00 | TERRA_M-M | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 2afe4fd6-a8ae-3997-bb79-f8742d332779 | -21.653 | -48.78984 | 2025-08-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 2604578b-03b4-3786-a195-6579ab7cb655 | -19.91536 | -41.58355 | 2025-08-28 00:07:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 25edf053-df56-30b0-9dac-8b661e95a498 | -20.14627 | -47.37301 | 2025-08-28 00:07:00 | TERRA_M-M | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 53184017-a8f4-3e32-a7a3-8ed3e2e58371 | -20.11622 | -44.33365 | 2025-08-28 00:07:00 | TERRA_M-M | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 94337485-7757-3d53-a00c-08b0205ec80f | -19.24995 | -42.04852 | 2025-08-28 00:07:00 | TERRA_M-M | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| c019bdcd-804d-3181-8231-b804a2147107 | -20.11264 | -44.34111 | 2025-08-28 00:07:00 | TERRA_M-M | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| ec58053a-9154-3400-be4d-5daaeb415119 | -20.11779 | -44.34775 | 2025-08-28 00:07:00 | TERRA_M-M | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 553f0ef9-f4e7-3abe-8be4-8eec78f3398f | -19.11812 | -44.02868 | 2025-08-28 00:07:00 | TERRA_M-M | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7664aa1-93ef-3b9a-8345-3798408065ca | -19.98263 | -44.1965 | 2025-08-28 00:07:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| fd686cb8-1082-374c-b1bb-9655d774df7f | -20.56173 | -41.60865 | 2025-08-28 00:07:00 | TERRA_M-M | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| f179ea7d-7c0a-3263-abbe-5a00f518d8ae | -21.65213 | -48.81536 | 2025-08-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 5321307c-245f-31a1-ac59-9ac6ea96dc67 | -7.94823 | -42.65346 | 2025-08-28 00:09:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| dd0f9c23-bce3-3196-a084-1cb9bb2b3d1c | -11.33635 | -43.52578 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d16a08ba-c66e-383d-b2af-6a6fc0795a22 | -11.33763 | -43.5354 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 092cbd26-fc26-3423-8eaf-3c452145355d | -9.48779 | -51.93647 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 8d5520f2-0a8b-3f62-abdd-bcf101ca68be | -8.45962 | -43.69168 | 2025-08-28 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 19b81b13-136c-319a-a1e1-43d7f78a10a9 | -13.62905 | -48.23392 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 36295bcc-6f15-3eac-8056-5b7dc7118643 | -12.06262 | -46.62649 | 2025-08-28 00:09:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 12713db1-6500-347a-9d98-a5cbbbc939ce | -17.54645 | -46.63194 | 2025-08-28 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 9f29cfb7-918b-343c-bc6b-38df659349d4 | -16.37079 | -43.7927 | 2025-08-28 00:09:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2658df3c-5067-3be9-8568-ae53b32273ca | -17.54433 | -44.3835 | 2025-08-28 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ffaf9064-3920-3d13-8ce6-aa489ebdbe96 | -12.96135 | -44.56442 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43215a26-9be3-3e4b-8774-c20586acb898 | -11.81268 | -46.82221 | 2025-08-28 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 759673e2-9703-32f6-b2b3-ef04e4a2b5c9 | -11.32849 | -43.53668 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d43c4321-d30d-3728-a439-f3311e273a94 | -13.74822 | -42.50186 | 2025-08-28 00:09:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c2353ee0-3f1f-3bb3-9d59-3c58ef2764b4 | -13.23151 | -40.95811 | 2025-08-28 00:09:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a307a789-dab1-3ff2-aa8e-8da8adfa122f | -11.33891 | -43.54502 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| c7d3dd65-60f3-324b-8e72-830f5367e82c | -11.32595 | -43.51746 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ac635ef2-8522-328f-9ff0-7388d9ef135c | -8.46089 | -43.70094 | 2025-08-28 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea76f31f-bb93-350a-b0a3-a2a73a92156b | -13.078 | -46.32144 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3d257194-b2f9-3a44-93cc-3246dda1890b | -9.13763 | -45.22881 | 2025-08-28 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b75f6873-6da9-3756-a65d-7677b39983cb | -12.95294 | -44.57694 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 19bd83f3-18ec-361b-a792-68e5b43eb621 | -13.50403 | -43.63986 | 2025-08-28 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 235533f2-ad4c-339a-8ac9-4806877f801b | -8.91077 | -47.32629 | 2025-08-28 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 69bb186f-0977-3d13-abac-3c5ee14c763e | -17.74152 | -42.68071 | 2025-08-28 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 81b4e060-0625-37bb-9cf9-cfebe58a7edb | -12.93106 | -46.33807 | 2025-08-28 00:09:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 385dcb36-a385-3aba-8e6e-95e5e7e20561 | -11.35529 | -47.85583 | 2025-08-28 00:09:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| cb8799da-9daa-3782-9c84-9ef86c5f96d9 | -12.44591 | -40.80844 | 2025-08-28 00:09:00 | TERRA_M-M | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 501d9070-8b57-3110-8358-0cdf44a859cf | -13.61329 | -48.23223 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ceaba12c-1c7c-362f-8bdb-98dc1d97fbb7 | -11.27995 | -43.31002 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 15da2051-55f2-3d21-8e1f-184c464f8fcc | -9.86294 | -44.68369 | 2025-08-28 00:09:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README2.md)
