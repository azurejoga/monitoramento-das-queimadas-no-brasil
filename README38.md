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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212f9712-44b7-3375-ac4a-7b6af3814ae3 | -7.97021 | -46.41378 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ed16f2a-7bb8-368a-aaf5-08ac61efc57d | -8.77752 | -46.59217 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b899b646-6da2-376a-a8ad-dfa6b6065ca6 | -7.40717 | -44.08456 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8a8f0b6-a868-35dc-a21b-d74c7ab7c6cd | -7.10518 | -44.31964 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 8449b67c-5a75-33d6-b9d3-549c0e77cc4a | -7.21691 | -44.75031 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d15ec9df-e037-3f11-bd5f-b83b3a7b0d5c | -6.95194 | -44.30122 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab148a7d-9783-3b3b-937c-9d6012011cb0 | -8.72968 | -50.37635 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0f94a83d-f885-3aa2-b773-bc32a381cea7 | -6.58612 | -43.63853 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f29f57-859d-3fab-a897-4700fdaf844d | -7.95304 | -46.41463 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5625a420-1d69-39e4-bd88-c7233d929f76 | -6.24169 | -44.76615 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9234e273-c661-3eaf-9986-ad175be7aa8c | -6.28816 | -43.53984 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aac3d9ad-8929-3f68-9712-2111ba5e0d0b | -6.21585 | -42.77434 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30e98bf2-6a33-3830-99a3-874ad75ba77c | -7.09968 | -45.347 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e98b7ea-df79-3c8b-8b1f-67d9034746ee | -3.48683 | -40.67435 | 2025-08-31 04:27:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89bea80b-c48b-3d15-9a30-5d959f03381b | -5.70179 | -45.95535 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81e24f20-e813-3f15-a077-e62739edd470 | -6.18168 | -44.20606 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 510812c1-142e-3dc2-a7b9-0f323b5294b9 | -8.2957 | -44.92433 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 350285f4-23a7-3c45-976a-03af88a96a08 | -7.62104 | -42.66064 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4678de21-ceaf-30c1-b6a4-7d9fcc1c1671 | -4.94077 | -47.58208 | 2025-08-31 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 612af9bf-e9ff-312b-9300-b3a6ac4efc80 | -6.18865 | -43.31656 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf6da9bf-55ab-310d-8eb6-7c783e4f4420 | -6.17558 | -43.56747 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43d0810a-c3fb-311b-bee1-056b07016d13 | -7.95958 | -46.35149 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8058d70-6e10-3eb9-b9c0-f8a489f45935 | -7.14578 | -44.91817 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb25250-4c26-343e-aff8-bf5208881137 | -5.4821 | -44.42074 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afbdcc30-7bc7-32ae-a261-af34b88e07a0 | -6.16693 | -44.0036 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00cecaf5-f83c-3c08-8cbe-880a865caf39 | -3.59884 | -47.52197 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d521f4d-fe40-3c56-b0cc-a77365b686df | -6.24372 | -41.81886 | 2025-08-31 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e187d768-c255-3607-acdc-7edf5c81a893 | -6.28463 | -43.53934 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d702d69d-eac4-3b28-9100-1803d381fe94 | -8.91826 | -40.4395 | 2025-08-31 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1868cba-b76a-3c30-9f51-6a4bece41e5e | -4.40817 | -40.69268 | 2025-08-31 04:27:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a662357-7490-3a99-817b-dc8dbf369305 | -6.45071 | -43.95674 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6813c39e-b8e0-366e-b5a1-9c8d8ba3e8d7 | -6.49067 | -44.07492 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f0d3840-0b68-3345-97e7-59ea996794bd | -7.71491 | -50.26802 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b388d558-e198-30cb-b00d-00067dec6c19 | -7.58534 | -42.71965 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62742e46-1a2c-317e-a151-6c2ac5dd7cb3 | -9.25171 | -47.05817 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dba24ad-94d9-3acb-9f06-fce8c9bf2610 | -6.24688 | -43.38213 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792d59d7-1754-31dd-9584-e5f3bc549590 | -4.22436 | -47.21245 | 2025-08-31 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd74bf0c-771e-3337-83b3-5edc011f8ceb | -6.65078 | -43.94609 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec95e85-1ce3-3424-bf56-b39832beb668 | -7.1255 | -44.59769 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2c37c2-7b0c-3df3-95cf-cc3eee615355 | -7.73509 | -50.26228 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3fbee42b-82e2-38bc-92af-d0e00f58351c | -6.70571 | -51.41811 | 2025-08-31 04:27:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 7cc7f590-936f-3c14-a6c1-ff6c4358e29b | -6.52017 | -42.94904 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92a3d924-0158-346a-8788-a758dd112910 | -7.41328 | -47.45235 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dfb90af-1691-38f6-9d61-bed4b55510f4 | -6.64753 | -44.25571 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18e15063-4079-3b3c-b198-31491d2516ca | -4.16831 | -42.03098 | 2025-08-31 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 754012e3-fae4-3ca5-8d70-11d7a0aca47f | -5.24998 | -44.45537 | 2025-08-31 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7896715-c1ee-3e95-bf04-8eb4b618ca73 | -5.79753 | -43.87146 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e11019-1b6b-3caf-89ae-6fc7b8373491 | -8.88713 | -45.09281 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8af0021a-ec6e-389c-8f49-4698916e1267 | -6.45011 | -43.96063 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e78fb2f8-d829-3387-a8a8-06556d3f2714 | -7.96136 | -46.42666 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f75e45a-81af-33d1-8421-4282890d2ec8 | -6.83731 | -44.25375 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9129c68-84d6-3eef-9d32-6d7e50d33e4b | -9.59456 | -40.35158 | 2025-08-31 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de23d0a5-7a16-33b1-8b3e-25423f6f2b0a | -6.17971 | -43.56409 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34bd8a6d-e0bf-3dfa-a02b-6618461b78ac | -8.3359 | -47.41095 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9a0b1f6-9300-3a89-98d4-8b846ef2d7dd | -8.49562 | -44.73832 | 2025-08-31 04:27:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e99c27ef-1412-3d01-955e-0dcf7ca9827b | -5.47812 | -44.4015 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 211805bd-9288-37b8-b88c-f3557625f0c2 | -6.92352 | -44.70971 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ddc0dd9-037b-3542-a3cd-268abbd774bf | -6.18509 | -43.31598 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5f426a79-a1de-3bb3-80c9-318db97a2a47 | -6.25462 | -43.37911 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a88f0fa-149c-3940-a7e5-7c125c59dfa2 | -6.46156 | -42.43159 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ccd3b89f-d240-3a1f-919c-98ae7d40de26 | -8.88907 | -45.08217 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d700805b-6df0-38e4-b9c7-8e0511f85180 | -6.28109 | -43.53884 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3535712d-4898-3f3a-a72a-831f87e217a4 | -6.5108 | -45.41125 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb590892-0340-3512-adc6-21ab5755b191 | -7.10575 | -44.3159 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5211a0fc-bdd2-38cb-9767-65a6ecf808fd | -6.62201 | -43.73529 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f651a2ba-270c-3977-88c0-2730d60ab4b9 | -6.47784 | -44.40966 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f2514c-29c1-32c8-aa04-aae0912cc412 | -6.57355 | -43.697 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ef1c0a4-52a4-3e62-80c4-d675feb1b30c | -6.17722 | -43.34376 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d38a3c95-ae49-372c-bc5d-ab54399d0acf | -8.03394 | -46.90942 | 2025-08-31 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716def28-9f10-364e-ade8-5f7631e2ff96 | -5.49396 | -45.44587 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49bda563-2191-3797-b568-07d4c4092c01 | -3.59539 | -47.52143 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac98cd22-4b33-398c-8311-1e6f1868c29d | -6.09665 | -43.33267 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fa4b24f-783a-39d9-a691-845e38b6ae13 | -5.8352 | -42.52781 | 2025-08-31 04:27:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63a5942b-917f-3a40-a6c0-c2b65af79104 | -4.48129 | -48.12035 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 625a2ad2-954b-3db0-a263-6a67ff9a48ee | -7.32507 | -44.3644 | 2025-08-31 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 607d6bb8-56b5-3b4e-a3a0-4ee92314c323 | -3.86928 | -48.04345 | 2025-08-31 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cf70d24-e437-3ffd-b19e-903364b4ced6 | -6.48611 | -43.56388 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d999e6-a22c-3e62-9516-f63dfedfcefb | -8.88882 | -45.0816 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24575a12-d09f-3272-bb75-2e13bb9cf792 | -3.28727 | -43.41515 | 2025-08-31 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1029051b-3134-3ac6-84d9-aa69f703f9ee | -6.21936 | -42.76855 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6919d0e1-b6bf-3b8b-b9bc-5d012cefb339 | -6.1945 | -42.76677 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| acdbc819-383c-3b0f-bf4e-6d6566fc9256 | -7.58228 | -42.7146 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cca28065-7ebb-3a38-880b-0d6e48bea5d9 | -7.76061 | -45.45684 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecc2b696-da1f-39e1-8e98-52d9ae0ca531 | -3.5165 | -47.20667 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d0d2253-5d89-3b81-beea-157a335eb054 | -3.81474 | -41.57233 | 2025-08-31 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cc07a01-1584-3fdd-921e-6add788285a9 | -5.53508 | -36.85552 | 2025-08-31 04:27:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d4fca80f-4f38-3c54-b17a-b986ef8f2a7e | -6.15417 | -44.13311 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b46d5c8-3bbb-3bbe-a20c-cdc9249f5afe | -6.96635 | -40.94252 | 2025-08-31 04:27:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7054282f-d089-3ed4-94ee-8ab76a4920d2 | -8.46134 | -43.63017 | 2025-08-31 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e312106-5b88-3ccb-bb86-f167ff96c93d | -7.20844 | -45.42956 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68933ea3-0689-3f6d-bc9f-a44daad31bcb | -6.99455 | -44.36126 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fcc953f-af83-3685-b111-4e54137f28f2 | -8.88733 | -45.09336 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de6a688b-af1c-36f5-a103-29e44f0415ff | -6.93485 | -44.70398 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a94be522-36fd-3aef-9eeb-6cb68ad849a3 | -6.94697 | -45.69471 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5664660f-7bfa-3ad9-86ff-85a04146feab | -6.18323 | -43.56464 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10fbbdd2-a6d5-372e-acc4-d79b5f860f81 | -8.96655 | -44.44156 | 2025-08-31 04:27:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8db8241-3f45-39f7-9d30-24ff8c2dc536 | -6.18139 | -43.34026 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76d51ce-a8c3-3ff7-874f-7e6af6f17b81 | -7.20008 | -45.43911 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 606e6b64-c62d-388b-831e-148a7b6fe466 | -6.17735 | -43.3189 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2ffb4cb-00b6-3a9d-81ec-bd971d511062 | -8.25971 | -47.18983 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
