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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c60df06a-b8b5-39d6-ab5a-ab380e48447c | -7.3066 | -35.83582 | 2024-10-25 15:33:00 | NPP-375 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1979125f-d00b-3aaf-9201-93521935d96f | -6.89934 | -35.50441 | 2024-10-25 15:33:00 | NPP-375 | CUITEGI | PARAÍBA | Brasil | 2505204 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0b31ad95-67e7-3523-8e34-d8193d3b90f8 | -6.83209 | -35.30822 | 2024-10-25 15:33:00 | NPP-375 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0317ee64-8b63-33c1-a166-bd4162873693 | -6.82829 | -35.30877 | 2024-10-25 15:33:00 | NPP-375 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 27c57f46-17ac-303f-b2c4-4b6ebae7b617 | -7.85589 | -35.58535 | 2024-10-25 15:33:00 | NPP-375 | JOÃO ALFREDO | PERNAMBUCO | Brasil | 2608107 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 979696c3-3836-31fa-a326-d891854a87af | -7.82248 | -35.57507 | 2024-10-25 15:33:00 | NPP-375 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3688dc71-94a9-3ca2-8a53-dbf653febe9c | -7.43441 | -35.87571 | 2024-10-25 15:33:00 | NPP-375 | QUEIMADAS | PARAÍBA | Brasil | 2512507 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fa8f463e-bb34-36b3-bd28-7d103bdcbef1 | -7.03881 | -35.86259 | 2024-10-25 15:33:00 | NPP-375 | ESPERANÇA | PARAÍBA | Brasil | 2506004 | 25 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 9d036cf1-4c6f-3eb5-9d71-e0d24a588cd5 | -7.03557 | -35.86809 | 2024-10-25 15:33:00 | NPP-375 | ESPERANÇA | PARAÍBA | Brasil | 2506004 | 25 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 6e954bf7-8a07-3efc-9af7-b7f751d57c0e | -6.80965 | -35.7093 | 2024-10-25 15:33:00 | NPP-375 | SOLÂNEA | PARAÍBA | Brasil | 2516003 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 48a0d1cd-5a25-346f-a70a-c79449f5183d | -7.88113 | -35.42778 | 2024-10-25 15:33:00 | NPP-375 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 26b62594-f12c-3b95-b212-c7b085dbe459 | -7.03951 | -35.86755 | 2024-10-25 15:33:00 | NPP-375 | ESPERANÇA | PARAÍBA | Brasil | 2506004 | 25 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 2c9d4a65-a6ca-3de8-a6c1-f65d99024c9e | -6.90004 | -35.50919 | 2024-10-25 15:33:00 | NPP-375 | CUITEGI | PARAÍBA | Brasil | 2505204 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0ce54156-5370-3845-aeb9-9e71a9699d2e | -7.81882 | -35.57736 | 2024-10-25 15:33:00 | NPP-375 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d61b2c19-3473-34fc-bc25-89033ee237ec | -6.50863 | -35.72613 | 2024-10-25 15:33:00 | NPP-375 | ARARUNA | PARAÍBA | Brasil | 2501005 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 992a26a4-e357-3552-9d34-90278ac815c6 | -7.70339 | -35.02683 | 2024-10-25 15:33:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1a92e11d-ef69-3ffc-a42c-2c5b9b636c1e | -7.69895 | -35.02281 | 2024-10-25 15:33:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 4fab2b04-e230-3683-b3b0-38d8a809b53f | -7.69584 | -35.02801 | 2024-10-25 15:33:00 | NPP-375 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| f3a3d7b2-5fc7-386d-9510-e9523f7a95cc | -7.62679 | -34.9219 | 2024-10-25 15:33:00 | NPP-375 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d50e69e7-461c-3ff8-9b3e-99b0f537fee6 | -7.22833 | -35.12119 | 2024-10-25 15:33:00 | NPP-375 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| efc3e11b-cff4-3748-8db4-6c3c56fdfe66 | -6.97032 | -35.1958 | 2024-10-25 15:33:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 75f1b0fd-f70c-331e-bdfd-44ab1fda91c4 | -8.39049 | -36.21223 | 2024-10-25 15:33:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7772a4f4-429d-33ce-90bd-9b42968b7dec | -8.33227 | -36.12381 | 2024-10-25 15:33:00 | NPP-375 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84dac4ff-a77a-35f3-b957-65496c71a252 | -9.06633 | -35.90854 | 2024-10-25 15:33:00 | NPP-375 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 126c3e15-0732-3bf2-9f8c-b16dd55944d7 | -8.47997 | -35.18346 | 2024-10-25 15:33:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| 65201d0e-05d7-3570-a1e4-17d37dbd1633 | -8.47927 | -35.17861 | 2024-10-25 15:33:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 1cd57877-6137-3f1e-8dd1-186aedc64839 | -8.62634 | -36.15312 | 2024-10-25 15:33:00 | NPP-375 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b07e63b-e9c4-334a-8402-3cca003eae7a | -8.62275 | -36.15736 | 2024-10-25 15:33:00 | NPP-375 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| f85711c6-a551-3e0d-8953-3ba30ad5db84 | -8.4761 | -35.18399 | 2024-10-25 15:33:00 | NPP-375 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7baa0d10-2b43-3fa7-abff-a4077275d046 | -8.62327 | -36.16101 | 2024-10-25 15:33:00 | NPP-375 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 192b24e1-aeb4-391b-b42a-e352afc5707d | -8.62223 | -36.15371 | 2024-10-25 15:33:00 | NPP-375 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e748d9fe-e8b2-3421-8d50-51f9db23576d | -8.18111 | -35.38028 | 2024-10-25 15:33:00 | NPP-375 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c7851926-5f90-380b-93bc-ead39aae2fe3 | -7.97802 | -35.27354 | 2024-10-25 15:33:00 | NPP-375 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ea397dd6-ec83-3491-96d4-c0cdc766b539 | -8.17725 | -35.38098 | 2024-10-25 15:33:00 | NPP-375 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2a9591e0-4f89-3bf4-b28c-dabc10f8d387 | -7.9793 | -35.27046 | 2024-10-25 15:33:00 | NPP-375 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7bacda90-afb7-3d39-99b7-540edab1c9f8 | -9.96123 | -36.4553 | 2024-10-25 15:33:00 | NPP-375 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5d007c49-1a36-3502-a811-80c20ddea5b0 | -9.6564 | -35.86917 | 2024-10-25 15:33:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| b0bb7a63-6f9d-3bff-96ca-c7b2d493bc3f | -9.65587 | -35.86543 | 2024-10-25 15:33:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| a11e4cd0-715b-3d78-a869-3eabbdb12f33 | -9.65535 | -35.86172 | 2024-10-25 15:33:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| a6270f44-9b63-3d3a-b2ca-2c2a680b5353 | -9.65231 | -35.86977 | 2024-10-25 15:33:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| bd7184d2-a26c-3569-a2b5-7683b8b17f0b | -9.65178 | -35.86601 | 2024-10-25 15:33:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| eb1d94a4-9d31-3493-96f2-bce2f4df4fe1 | -9.49742 | -36.11763 | 2024-10-25 15:33:00 | NPP-375 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dc37869f-d1d4-3ee7-ad6d-b42e121a41ad | -10.31053 | -36.51528 | 2024-10-25 15:33:00 | NPP-375 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4544538c-2c4d-3092-91c5-2dac4fb60c64 | -9.45629 | -35.53141 | 2024-10-25 15:33:00 | NPP-375 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5cc73464-51c3-3f3d-af8d-3aa74086dbbe | -9.45331 | -35.98368 | 2024-10-25 15:33:00 | NPP-375 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3673da45-0cea-3271-9287-b130cd144dd8 | -6.1234 | -36.74806 | 2024-10-25 15:33:00 | NPP-375 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1cd366f5-bcf2-3777-8d37-b3eb0faa1f3e | -7.50276 | -36.71466 | 2024-10-25 15:33:00 | NPP-375 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5fde3dc2-f5d5-3eda-9728-59d933bbef5a | -7.34814 | -36.46853 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO CARIRI | PARAÍBA | Brasil | 2514008 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ae26b61-e44e-3a0a-b86f-6e3f3062cb34 | -7.31616 | -37.25777 | 2024-10-25 15:33:00 | NPP-375 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 904a0b60-eae3-3eed-a93a-4bb6071fd34b | -6.98677 | -36.71186 | 2024-10-25 15:33:00 | NPP-375 | JUNCO DO SERIDÓ | PARAÍBA | Brasil | 2507804 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b9423741-4917-3601-8a55-6b95abc05cd9 | -7.33777 | -37.38258 | 2024-10-25 15:33:00 | NPP-375 | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 48bdb034-812a-300b-a8e7-eeae7f1778b9 | -7.3334 | -37.38327 | 2024-10-25 15:33:00 | NPP-375 | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 08d91fe1-7b75-397c-bc8b-66508d1279b2 | -7.25539 | -37.24075 | 2024-10-25 15:33:00 | NPP-375 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 673765e9-f625-337d-a44f-5c21913b190f | -6.66976 | -36.66461 | 2024-10-25 15:33:00 | NPP-375 | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 74f12481-09af-3a8c-bad7-29f4c1c6d003 | -7.46408 | -36.80627 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd7a452d-86a0-35d6-9995-d60487e25e5b | -7.19388 | -37.17873 | 2024-10-25 15:33:00 | NPP-375 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c2e976e2-2b48-3302-ad6f-757bf2097043 | -6.66922 | -36.6609 | 2024-10-25 15:33:00 | NPP-375 | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d9efb723-74a9-3f2d-a7c0-4675109aff35 | -7.59323 | -36.27807 | 2024-10-25 15:33:00 | NPP-375 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f45ec143-8c71-35ef-9dcd-06450da13a29 | -7.59031 | -36.27913 | 2024-10-25 15:33:00 | NPP-375 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5dabdb97-0a6c-3e92-8698-4ab73a5bfb37 | -7.39426 | -37.13985 | 2024-10-25 15:33:00 | NPP-375 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 63bcbb01-cad5-3e27-b3f9-4ff00788064c | -7.39212 | -37.1395 | 2024-10-25 15:33:00 | NPP-375 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| be402362-e60a-3f66-9f3e-56bfbbbfb460 | -7.19447 | -37.18304 | 2024-10-25 15:33:00 | NPP-375 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ebd43a9f-969b-30ba-83e0-3ef77701ef20 | -8.35767 | -36.41344 | 2024-10-25 15:33:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f558e9f7-cc42-35f9-8deb-24f7a0f7541d | -9.12116 | -36.80685 | 2024-10-25 15:33:00 | NPP-375 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9a03bc75-5e83-3fc0-a661-8fd7b0b02456 | -8.66997 | -37.09781 | 2024-10-25 15:33:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4f6c1e9b-8730-3bca-903f-efdfb04909d6 | -8.63794 | -36.3248 | 2024-10-25 15:33:00 | NPP-375 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| aed0f1ef-be53-31d5-a1d7-115abc001c11 | -8.56303 | -37.6599 | 2024-10-25 15:33:00 | NPP-375 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 17d65df2-baa4-37a1-9178-55524a62b34b | -8.3551 | -36.41468 | 2024-10-25 15:33:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 26e18142-8b50-34c1-b718-6192d8840b36 | -8.66954 | -37.09702 | 2024-10-25 15:33:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5c911d96-0c4c-3c10-b747-52e7eee1d0ac | -8.50171 | -37.10822 | 2024-10-25 15:33:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cc8c976-68d0-3ec8-b4d8-836866bec4b2 | -8.40798 | -36.7103 | 2024-10-25 15:33:00 | NPP-375 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d8ba404d-a4c7-398f-bbb1-5b0c4fb81ff8 | -9.69294 | -37.3458 | 2024-10-25 15:33:00 | NPP-375 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ec5b0217-3579-3ffb-8e69-a2f13d9fda53 | -9.69234 | -37.3412 | 2024-10-25 15:33:00 | NPP-375 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 43dc658b-2cf0-3de3-b2c0-bfd7cf239041 | -9.58951 | -36.70137 | 2024-10-25 15:33:00 | NPP-375 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 15674089-b7b9-3ad8-bad1-ba6a810fb4d5 | -9.58519 | -36.70199 | 2024-10-25 15:33:00 | NPP-375 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e998510d-63a7-3879-b285-aad0031f6dea | -10.55511 | -37.99611 | 2024-10-25 15:33:00 | NPP-375 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d7d65def-773a-363d-8b40-7db6fe971bcf | -10.22645 | -36.82324 | 2024-10-25 15:33:00 | NPP-375 | PROPRIÁ | SERGIPE | Brasil | 2805703 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2dd85311-b140-357a-aeee-2450c09a5cd6 | -9.41328 | -37.95977 | 2024-10-25 15:33:00 | NPP-375 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8a686296-3f7e-3764-8e64-dd33903472cb | -11.15212 | -37.23483 | 2024-10-25 15:33:00 | NPP-375 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3a033eaa-9b7e-3a14-bc01-137cd5440be6 | -11.11374 | -37.3641 | 2024-10-25 15:33:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| eca73c6e-a6b5-3928-9c07-98cdb1191438 | -7.009 | -40.12158 | 2024-10-25 15:33:00 | NPP-375 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 344adb2d-afbf-3741-b659-356498bb7d99 | -11.11312 | -37.35935 | 2024-10-25 15:33:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| dd4cfe3b-fcda-3c99-bd84-5d7947919f3c | -11.1125 | -37.35461 | 2024-10-25 15:33:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| b75cb4e9-b84a-346c-9daa-2c3d20a15785 | -11.10911 | -37.36471 | 2024-10-25 15:33:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| dca7fd95-e1d1-30cd-83bb-ba4eee9c47eb | -11.10788 | -37.35523 | 2024-10-25 15:33:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 63bbfea6-3774-3681-8ccb-e42d64e3e4bf | -4.89264 | -38.43459 | 2024-10-25 15:33:00 | NPP-375 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4432cebd-d05b-39b1-a4fb-c80d18da5bda | -4.88823 | -38.43319 | 2024-10-25 15:33:00 | NPP-375 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 4b836ec6-2b9e-3c8d-8a75-c4a6a6fb6fcd | -6.42384 | -38.52601 | 2024-10-25 15:33:00 | NPP-375 | POÇO DANTAS | PARAÍBA | Brasil | 2512036 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 230a8db8-4f58-320c-9579-a6d0e0bf0bd3 | -6.35278 | -38.57676 | 2024-10-25 15:33:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 127f58f1-3df9-3c9b-ade1-4a8ba96fab2d | -6.29623 | -38.07516 | 2024-10-25 15:33:00 | NPP-375 | PILÕES | RIO GRANDE DO NORTE | Brasil | 2410009 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb9a9b2f-bfc4-3ecf-b1ad-c73878b2a09e | -6.33096 | -37.72509 | 2024-10-25 15:33:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| aa542d3c-4bc3-3eea-9ec0-af988ec3bca7 | -6.28967 | -38.51977 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7886a74-376a-3a11-84a6-59b8a7833f15 | -6.28755 | -38.5185 | 2024-10-25 15:33:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c8398bd3-bcbb-36ef-a27c-4bc19a4aeea7 | -6.50404 | -38.16004 | 2024-10-25 15:33:00 | NPP-375 | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 28.3 |
| bde84584-b365-330e-a7ea-72995a417ff5 | -6.33037 | -37.72082 | 2024-10-25 15:33:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 25554cd9-6194-3a07-8542-2afef4712826 | -6.02903 | -38.05959 | 2024-10-25 15:33:00 | NPP-375 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 6cd35fbb-02d1-3748-882e-990e3d223b5f | -6.45328 | -38.49796 | 2024-10-25 15:33:00 | NPP-375 | JOCA CLAUDINO | PARAÍBA | Brasil | 2513653 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d1781ed6-a3b8-322f-88c1-f3d667983e08 | -7.84683 | -37.97508 | 2024-10-25 15:33:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f4e9c878-867e-310b-b96f-ee09465bc602 | -7.84221 | -37.97556 | 2024-10-25 15:33:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 82373f00-99fe-3ee4-aaad-ae8067b45e76 | -7.78979 | -37.89501 | 2024-10-25 15:33:00 | NPP-375 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README123.md)
