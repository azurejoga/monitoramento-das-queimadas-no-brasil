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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d414882b-58c0-3e83-ba38-10b56aea6702 | -3.81724 | -50.7463 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d56ba3-c342-3ea9-84e4-6d25a746e573 | -3.23767 | -46.94754 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 210147be-262a-3dc8-9004-2b7845228ff7 | -1.62294 | -48.28706 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64bffa59-78c2-3771-8468-3583ae7a800a | -5.22334 | -49.30356 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a037c818-4718-3729-8ef6-88597187bf4c | -5.86608 | -52.05258 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda085c0-8f52-320b-8c73-18c69e7d7c01 | -7.63635 | -46.10868 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6866074-0307-3d12-b2f4-4118004cf19f | -7.76429 | -46.75447 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 04731285-fd46-3261-815e-5321e22468cb | -3.23372 | -46.95059 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 86b833fb-ba33-3944-8241-8997db38f24a | -5.47457 | -48.99669 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca62689c-d395-39c7-95e9-954438d4e4cd | -7.67412 | -46.12901 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d206718d-990b-34a6-9231-31d76954b18e | -5.73176 | -52.23794 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0adf5cc3-3ee6-36c0-80a7-0bbdd8a953a3 | -7.05585 | -42.06664 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a142b96-bfd9-36f7-a5df-699c5627247f | -3.42786 | -50.66441 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d0b42e1-5446-3423-962d-4a48b1abc630 | -4.54575 | -54.93194 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7536c00c-2a87-35df-8e06-77e7b8b7cf34 | -8.36653 | -45.65639 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0a4bfe2-a7ba-3515-9838-3e34379d158b | -3.00392 | -52.70566 | 2026-09-19 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 234cde3d-daad-343c-8a9b-4eadeb817944 | -7.20472 | -44.09935 | 2026-09-19 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f37a21d4-c71b-3a92-a68a-4f1a4f771112 | -8.86203 | -45.9448 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5971f7f6-331d-304b-a95f-cae453bbb1a5 | -4.06736 | -56.25182 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52363357-c21a-3ac5-a512-36ef96d02899 | -5.86815 | -52.04 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f15f2b75-1654-3f95-ac02-94b55942e4a7 | -8.46749 | -47.0099 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da64b511-ac3f-3622-9b39-0dad64df862c | -8.3697 | -47.224 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acd15e55-ab97-362c-b44c-59eb290f5604 | -7.88334 | -46.42692 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55f37623-4d81-379b-a13d-f493cf596bb9 | -9.0029 | -44.91854 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caf5ae5c-7272-3f62-8eaf-4b7b44e3af57 | -3.28737 | -44.68557 | 2026-09-19 04:38:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e87b051e-f346-3fa8-b3ec-32cc521275a0 | -6.6332 | -43.47818 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d0e617c-d99c-3f68-a210-0cefaef64b62 | -8.63715 | -47.53765 | 2026-09-19 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| befb6fd9-6a0d-3863-926f-f1cd411386fe | -8.35472 | -47.54248 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05c4f939-2168-3886-8792-4f05ae0dedbf | -8.76912 | -44.22925 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8deba9dd-65e8-39a1-9f6b-ecd2ddc276b7 | -6.31578 | -41.75914 | 2026-09-19 04:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0e01ede3-9360-30d8-aaa2-e8b12ab9cf5d | -3.8893 | -49.06161 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 159597e8-e64c-3301-b911-b55697425a64 | -5.6475 | -51.70401 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e8a830e-a14e-369b-9500-27859b7c6b2f | -2.89763 | -54.1837 | 2026-09-19 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89376a53-0159-3582-a385-b441ec2dd43f | -3.16833 | -48.60815 | 2026-09-19 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f22880d-c587-3a6a-a6e8-c0db4ccef871 | -2.64536 | -54.69193 | 2026-09-19 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97c7effd-0cda-3dde-94d3-731fa3908129 | -5.56273 | -48.45309 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b55f97-c023-374b-952f-781448b859f2 | -3.16472 | -48.60757 | 2026-09-19 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b44c01b8-5aa9-3bdd-b03d-b27b02c8a39f | -6.42105 | -46.19831 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe015fd1-f256-3936-ac37-bc82d8558f5b | -3.2371 | -46.95112 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3eae58fa-57ba-390a-b83d-7bb70de3ea58 | -3.3532 | -50.46143 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bfc98d7-39e2-3bda-8d5b-7edbfa655455 | -3.24105 | -46.94808 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1d1fe97-d635-3d4a-9ade-6849dac07573 | -7.86919 | -45.15211 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b489ef-bf6c-3a23-a2c3-6585f994c111 | -5.74968 | -57.58201 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e5974c1-dc80-3494-b619-3f39c16348e3 | -5.84649 | -49.86699 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09863320-69c5-3cf7-aff9-f62049c1dd68 | -2.81867 | -50.47888 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd3b91bc-e297-35e5-b678-1bc604ffe37e | -2.82792 | -50.47307 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c5b2efd-3da8-352a-a01e-f9e011e4fee2 | -2.82446 | -50.46886 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 030f3864-16cb-36a7-a3bf-e740d2fc7761 | -5.8796 | -53.61642 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be1d522-b3e8-39f4-8441-0ada5a09d821 | -7.09923 | -46.44831 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93387d80-66f5-3de7-bae4-108d81871dec | -7.36609 | -50.32964 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d5a3a15-b33e-3ad8-8d86-023095740402 | -5.86974 | -52.04391 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa29dc4-1d0e-3e3f-a973-3c09f67eaa20 | -6.78253 | -46.46189 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1664152a-8176-3107-a445-8efce2b90708 | -8.4774 | -44.53411 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e0670af-b1e0-3929-84d5-b62ee6178091 | -2.93382 | -51.06579 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf91d17-9747-3944-bb2d-cd7ba12f57c4 | -6.26814 | -41.67558 | 2026-09-19 04:38:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 23478a9b-0773-3a7b-b95e-8dd546311984 | -3.3658 | -50.45995 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72dfd3ec-a8c6-308c-8b6e-d7ff9fb3e155 | -8.29629 | -46.85383 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9343e6fa-7932-3e3d-b250-52b552f017b5 | -7.69075 | -46.11015 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d27b7bb-0ca6-3000-977c-05cb72c627a1 | -8.93401 | -44.39871 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4854d10-17fc-3cba-bedb-2dc0df6fab59 | -3.23258 | -46.95774 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc5c7bcf-75a5-31e4-9052-bcb4afab26a9 | -7.79424 | -44.84817 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4fb76f7-952f-320c-a063-42a373420c67 | -4.48848 | -55.49041 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf900a84-c3e8-3f49-85ae-2063f021a108 | -8.38221 | -45.64419 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e02fc56d-5c93-32bf-9d7e-d895373a069b | -7.05124 | -42.07094 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6520845-d275-3e31-aeef-eb1a97c0df80 | -4.80877 | -56.08287 | 2026-09-19 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1338746b-dc1d-3c66-b65c-6b63db0fa25f | -6.98653 | -42.18217 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3f9bfcc-d874-3156-86ab-b7faadf0287e | -8.45854 | -45.7142 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b8767e5-8cd0-3a69-aa3d-6a93bce6b3d1 | -3.35906 | -50.45086 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e742b07-1aa2-37fb-a6c9-3723002292a2 | -5.86684 | -52.06065 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1323f51-aa9f-3a0e-8b69-1c64693364cf | -6.7754 | -47.86552 | 2026-09-19 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf35b578-8132-3a74-8580-d9126b7e077c | -8.57288 | -47.26421 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29f7acf1-5455-3553-a689-e901d41c14d5 | -2.39481 | -48.5228 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209d1756-7242-3a2e-b2a4-1609565cce08 | -3.52151 | -50.80041 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee551e1-578f-3935-a662-9813ecdaa177 | -2.82504 | -50.46534 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 56e8259a-f474-3221-9548-bdedd358aebe | -3.03884 | -51.37487 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49d2eafa-3f8f-33b5-b1b3-e4114e40507f | -3.36122 | -50.46275 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc2fb6f8-9467-36f3-b2a6-59afb618334c | -6.32115 | -55.28439 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6a184b9-1e33-3c22-b8ef-ac32af74e5db | -7.09591 | -46.44778 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf01fe61-29d2-3222-aafc-94363e2d61ef | -6.99038 | -42.18276 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71588f26-fc9b-3611-a4c5-d16d30ccfcff | -3.75975 | -51.13828 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362cbca7-0148-3e02-acc9-23b0c14f1c94 | -3.43191 | -50.66509 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf5835b8-3396-3cc9-a877-d188ef1ec95e | -5.61722 | -45.2499 | 2026-09-19 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| f28b6a67-546d-3ed8-9876-4a6900ee3e86 | -5.84275 | -49.86642 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 807c99ed-ce83-3b1a-8e33-d507be8336a0 | -3.03456 | -51.37418 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e153fd23-a57d-366b-bc6a-85e322243bfe | -3.37277 | -50.44255 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ed34b2c-6b65-35fa-8616-2fba794be995 | -4.35841 | -47.77866 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0070d4f8-c041-3afe-9214-dd9a656a5762 | -2.82619 | -50.45828 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 093a81c8-5842-342f-a846-3517ed9f7885 | -7.43578 | -42.11436 | 2026-09-19 04:38:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29ec6f60-a490-3ecc-8438-5634b4ba2f81 | -5.99463 | -51.79649 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ad595bb-d2a5-3637-b4db-c74dfa3242fd | -5.86687 | -52.03508 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5627e18-8618-3c32-9cc9-1fcfb887c12f | -7.04508 | -55.44232 | 2026-09-19 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623dae40-886d-317a-bccc-da75c643c8a1 | -7.19899 | -47.88134 | 2026-09-19 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1768bb-b0d5-3a18-a0d1-2dab3e3a015c | -6.37095 | -58.2909 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dba3a4cd-4cfa-3e37-adb1-3387db19aa3f | -3.37193 | -50.44768 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c02878c9-850b-3d47-b2c2-adc214708f15 | -7.61021 | -45.42906 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22f04c8f-3ca0-33e7-b92d-49cd0b4a4d4a | -4.57295 | -42.94575 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43beb789-008a-3c4a-ad27-26b76976b57b | -5.33099 | -48.98631 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a73ce71-0f10-3d37-b440-96d830c72820 | -5.83659 | -52.09732 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a32607-bb33-3de1-872b-d84449200b5b | -5.99948 | -51.79329 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c961d82-64f3-3674-b91f-901eb5adf3e8 | -5.47098 | -48.99609 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README49.md)
