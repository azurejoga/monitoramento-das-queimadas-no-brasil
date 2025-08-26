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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6428d2c-538b-3ab6-afc8-50744f5aad1e | -11.148 | -44.8005 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe6a7f80-857a-3777-b536-0596b3219b42 | -7.57915 | -47.48943 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84405548-ce0f-3904-96e3-5370f40bf028 | -8.56069 | -55.25825 | 2025-08-26 04:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec9f3c80-491c-3354-9212-f3b23de5e6e1 | -9.8483 | -46.45514 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18877ac5-b3a7-38e5-8006-f07c8eea5f81 | -8.28687 | -47.22774 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e64b57e-e12a-3075-a979-35755d4ad3d0 | -11.25628 | -44.97791 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74b13021-0421-3ebc-a532-612d0676c457 | -7.53372 | -50.54094 | 2025-08-26 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a06faf03-051e-3d44-84c1-48619f03a597 | -4.96452 | -55.811 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 880cfaee-8d41-3ef0-942f-6b1dbb1370b7 | -11.15575 | -44.77252 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bbe6f88b-109a-353e-b2e2-4d4070f87cde | -5.81125 | -42.3057 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 126c6f55-8893-3171-a178-27f3c7a8200d | -10.81845 | -46.3785 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60c10e69-fe2e-36e6-95bc-a728317a015a | -7.30542 | -44.52898 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e5c4238-d38b-3628-b2d8-07b84229f8f4 | -5.06305 | -45.46724 | 2025-08-26 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e26b380-ab72-35b7-b697-084a1da15acb | -6.76263 | -42.99184 | 2025-08-26 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e1e8333b-ce5f-385c-a8c6-277e3758a934 | -8.24667 | -45.10637 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e62078ce-01c0-397a-aaa6-531014273554 | -6.69543 | -48.38122 | 2025-08-26 04:21:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7a84cace-728b-3f7c-994e-ffd3cfd9df8f | -10.80724 | -48.31697 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b08ab5bf-e012-359c-9d0c-2575d56ff10f | -6.28782 | -43.84088 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 974cf556-7976-3ad0-9b51-c4bb5e831288 | -5.81472 | -42.30623 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b00363c2-dbda-3b6c-9b40-3f040b92a393 | -5.82583 | -46.3556 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 147fa3e4-1764-3293-85d5-500f22d08e36 | -10.43761 | -47.17567 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1557aa51-ba42-3efd-95a5-46fa4f54c52c | -7.63387 | -45.23359 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 687dfc11-5a0e-39e1-9c46-23a62a6af02e | -11.13913 | -44.69265 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b256f5c-d197-331e-be4a-360681bdb6aa | -4.02582 | -49.53402 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f16fc38f-0098-339d-b111-42f0dabbdb3a | -6.42355 | -44.5643 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 830526f2-0944-30de-8168-1edf6387bd60 | -6.98393 | -46.93216 | 2025-08-26 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b7759ad-da26-3c0c-bd2f-39a57e892e86 | -5.57058 | -42.6245 | 2025-08-26 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| dd3859f2-026e-3e41-b38c-4690a49ae36d | -6.14097 | -44.38456 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b2143f9-3ca5-3e27-bbb1-bdd5466a619f | -5.75944 | -53.77562 | 2025-08-26 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2448bcc-e240-380f-b2e7-246c0cb6d748 | -6.33337 | -47.65661 | 2025-08-26 04:21:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19fd3d5f-939d-367a-8129-9b3fef00eb1b | -3.17091 | -49.48172 | 2025-08-26 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ce6835a5-7b12-3323-95ca-ac2bce49d360 | -10.53773 | -46.79704 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9181c08-620b-39fe-8a85-299adbe5c737 | -4.96192 | -55.82608 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 587b0059-e690-3ebf-bf6a-b495c30304e0 | -6.19084 | -44.15422 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41cbde02-e156-3e72-877c-c8736d633078 | -4.84911 | -42.89023 | 2025-08-26 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b18dbc36-4cd8-3bb5-95d8-7fe0092dd81c | -10.53612 | -46.78563 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658afc13-39ed-3e66-8393-40e13b2b0c49 | -11.20963 | -41.59624 | 2025-08-26 04:21:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d15a8903-68a0-3ce2-8808-c9b2f37ea860 | -7.74306 | -50.29665 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff064ae8-bf63-3fd9-bca4-dc9dfa491aec | -6.75959 | -42.98803 | 2025-08-26 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 34f80d33-98cb-319b-9b61-72fc6191e2a0 | -10.76475 | -47.05479 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62d294ec-cf76-350a-8861-52c7e748af73 | -8.23936 | -47.45086 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69582a0e-a228-375d-944a-743a4ae0b35f | -9.25327 | -56.90625 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b9a6f99-8043-310f-b876-6a79f7244d80 | -10.38218 | -43.46588 | 2025-08-26 04:21:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0632ea5e-bad2-3bbf-bc72-49dd520dd97a | -9.40638 | -48.24923 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a3caf07-8ac4-3d3b-9030-2bed23801348 | -7.85273 | -46.74047 | 2025-08-26 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02a51233-93e2-39ed-9692-2210366cf624 | -10.80656 | -48.32105 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4369c3a0-2921-3cd9-84f1-a8c533bcb15b | -6.56404 | -44.213 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0be2f98a-7e42-37bc-a7ab-18c97fea7205 | -6.03086 | -43.98981 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f15caaa-c7db-3140-bdbd-5186c0c340b2 | -7.86801 | -47.95115 | 2025-08-26 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a1671cd-bd26-389e-814b-5fe1f1bfff72 | -6.88639 | -44.99711 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d78c4cbb-b2dd-3bf0-8156-91b7d74b4800 | -8.30423 | -47.23067 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50493ccd-6472-36e1-996e-acba87c80bf5 | -6.51757 | -42.97369 | 2025-08-26 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbca2ae8-abff-34ad-b277-263089f131f5 | -8.55998 | -55.26213 | 2025-08-26 04:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5c8cc91-f27e-3a97-9d4d-6ff5e0296121 | -5.6352 | -45.2532 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ea3393-e30e-332f-ad9c-d411b27c9c50 | -6.06685 | -43.99229 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdf8cc5b-2904-31f9-a5fd-010b29ce1b78 | -5.9631 | -50.06549 | 2025-08-26 04:21:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd148322-bb1b-32c2-8de2-142f75663884 | -11.16021 | -44.76589 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 216cadfd-4674-3068-834f-a139a0bd9be1 | -7.65644 | -44.9838 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d4bc20c-34dd-3683-9286-f88d7aaab0fe | -11.15461 | -44.75768 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e573d05-c6ea-314b-b4ff-921eb7d0e529 | -11.15296 | -44.76841 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2cef7596-0231-384a-9359-eeba26d8896d | -6.06631 | -43.99578 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61f693c6-d120-39b4-97f0-7814e2fd2701 | -10.81511 | -46.37794 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83641224-afc2-329c-8347-67762f747990 | -7.54226 | -45.65741 | 2025-08-26 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 867f1d08-69d2-3666-9948-53c79ee02120 | -10.74722 | -47.05551 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38034b25-947a-3d13-b15b-06c8cd87b4f7 | -11.14681 | -44.76377 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 902b4bb6-82b1-3943-94c1-90270d2b7f75 | -7.15882 | -44.17032 | 2025-08-26 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8584ebe6-380e-34f8-8789-dc950d1c9430 | -7.46633 | -45.01078 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e58eb2c8-9522-3ced-b164-76da05c5e3b5 | -7.58268 | -47.49002 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 784cd89a-7cd8-303b-a8dd-f778f867c671 | -7.45961 | -43.84965 | 2025-08-26 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96ddd71f-7778-3a53-8a9e-95949749e7ba | -5.87415 | -42.41488 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 672f0977-4d38-3a6d-be3d-5cc1b4902268 | -6.69614 | -44.01922 | 2025-08-26 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5baee3d-c874-3e7b-940b-8dc152ba77fd | -3.2555 | -46.91607 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d075aff8-c77b-3e48-a97a-c327fc0ec5a3 | -7.59221 | -45.22359 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 812811ee-c463-3925-9f45-23a7d316e10f | -8.11466 | -47.1302 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4de25f8f-9cf9-393b-a9e0-3fc77f53b727 | -7.59165 | -45.22708 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c3ad4f6-6eb9-3b19-b21c-2f9ff939b69b | -7.89739 | -41.90833 | 2025-08-26 04:21:00 | NPP-375D | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b89bb294-fe84-391f-9423-7b9072d3c83c | -11.26127 | -44.96783 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 815b05b6-5b84-32cc-ba7d-f4e9ddfac2f1 | -11.15796 | -44.75821 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4625619a-52cf-3449-823a-aeecf212d7f6 | -11.16411 | -44.76285 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 447e7751-1ff2-3404-bc3d-e35a8db29644 | -10.76136 | -47.05422 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98946273-4847-31bf-810a-cc5cf4a1ec02 | -11.14292 | -46.3367 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88608730-836d-3718-a29c-ff0927c569c2 | -8.3327 | -50.56837 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3398cf5b-0ac2-3d83-a09b-e54df3ab5e60 | -8.07436 | -45.01467 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52f47c21-aa8a-35e3-b027-d1113623511b | -10.4404 | -47.17997 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f88b5d1-ac06-30bd-9142-ac5344061777 | -4.96092 | -55.81366 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f2441ac2-001a-36e5-ad60-38624c4cf8cf | -8.1112 | -47.1296 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 247414fc-2a6a-3f21-9e35-a90f6a3c0f36 | -8.37528 | -48.0252 | 2025-08-26 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ede89b5f-24d4-3d80-a88e-6cbff4b776a7 | -6.19749 | -44.15528 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9822d05b-50b7-34b4-b97b-af8085350424 | -6.62231 | -43.08662 | 2025-08-26 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4768141d-fcd0-38b0-8070-9f42d8451035 | -10.53714 | -46.80068 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ef6a9a-14f9-3a0f-8aa0-7a47306bf4d0 | -7.74004 | -50.29959 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70a9a420-d753-3a58-83c1-4b7865b73381 | -4.04464 | -43.34417 | 2025-08-26 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51654b69-6db8-393a-ae78-6129b4b0a553 | -2.93077 | -53.69804 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 183a0be5-d412-38a9-af80-36f57619237c | -8.29382 | -47.22892 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8a92bc8-a23d-38c3-8e0c-43299f06b103 | -5.74927 | -45.37917 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f9f7572-47e8-3492-b8d8-ae20388a6c6d | -5.10854 | -43.16726 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32fccb45-38ae-3f3b-b9c7-3218d8827a3b | -11.10123 | -44.75989 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df7de94-817e-3e11-80d5-69fb116ac34a | -10.87427 | -45.23549 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ca01f0b-0d69-3ab0-a135-1cc536b79bde | -10.68545 | -47.17788 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d38e78d-c0b7-3800-831b-d23854562877 | -7.7424 | -50.30062 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README40.md)
