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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c13e65b8-1f1e-3200-b0a7-1f311b4b8f0d | -6.71967 | -44.55038 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db706ee7-5f07-3d85-9ed1-86d418b1921d | -6.71903 | -44.55454 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 078f2f69-44f4-3ded-a4e4-9cb9bedca3a8 | -6.7154 | -44.55387 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c310a800-760e-32d9-9617-ce86e67ffe97 | -6.66435 | -44.5458 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37e37f63-7198-3195-acec-d692a8e66d74 | -6.58187 | -44.29786 | 2024-10-04 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7e1d271-d03a-30ae-abe3-22548d9816a7 | -6.51872 | -44.50099 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5464af01-ee83-35af-baf9-075c9696cd91 | -6.6249 | -43.75294 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f955e247-982e-3493-a68c-d67ab3e3cad7 | -8.68792 | -45.25009 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4634d8-edda-3e25-a7a6-09f55ea0d21d | -8.6871 | -45.24718 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a690836-5df2-3a1c-8e11-fa6df8042706 | -8.68647 | -45.2513 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d177903-49eb-317f-8c7c-18b81c0ac635 | -8.68431 | -45.2496 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68507bbc-25d0-3a27-ba68-13e92cbd38b8 | -8.68311 | -45.25779 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 055d1026-5c70-342d-a85a-5b42d18574db | -8.68251 | -45.26183 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cebd1008-f539-36a7-b00d-2e059c5e1e79 | -8.68162 | -45.25896 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4b86c42-83f0-38bb-9515-6709153ce709 | -8.68101 | -45.263 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67b72329-b567-3160-801b-bd36bdfb1e19 | -8.67891 | -45.26133 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea5f0daa-84d1-3db8-b3e3-1d3fdc1ecfdd | -8.6774 | -45.2625 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6722397-f752-3547-bb17-08e72459667e | -8.34903 | -44.77255 | 2024-10-04 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88900700-0faf-3b8f-a8f0-680e5026dfcb | -8.29938 | -45.4759 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19d9a000-34db-344d-9745-84897c9660d2 | -8.29877 | -45.47994 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3883da2a-6969-39ee-8523-7b0cb71de6ef | -8.29707 | -45.46721 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41fd7abc-38b8-3c8a-841d-57ad16235f11 | -8.29646 | -45.4712 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db132be2-1b24-33c2-9763-6cf1eddcfd0e | -8.28834 | -45.4287 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6547d724-b619-37a5-b161-53fbe7f851a1 | -8.27948 | -45.41498 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9af0b30-ac87-38e8-9293-f81a1a177fdd | -8.22717 | -44.36919 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e21e9b2c-c18e-36e6-92b5-4bd3bda50af0 | -8.22651 | -44.37365 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3759561a-b18b-3b43-9d53-e30f45735057 | -8.22585 | -44.37812 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a654a85-897b-355d-b9b0-62b29456ea85 | -8.1843 | -44.39999 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10db74d5-1b7c-355d-9f79-e2ad66e6140f | -8.16993 | -44.39347 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac0abff3-edc1-3c6f-91a4-35a67c9f4e42 | -8.16928 | -44.39795 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9028f262-41d2-38da-a076-59dad930b034 | -8.16882 | -44.39559 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60935047-c327-393b-92a0-8a0e73b242ab | -8.16814 | -44.40004 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91b02dcb-e0e9-32da-bf28-6a840ad41ed5 | -8.16489 | -44.40189 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bd65602-d1a2-30e9-a370-bbb8f3343a06 | -8.16439 | -44.39952 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23e09ffa-cfec-379e-bd1e-d93e0d85f13a | -8.16049 | -44.40584 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e130102-74d0-39f4-a4b8-c09cfc091ee4 | -8.13551 | -44.80966 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77613dde-87e3-3536-ab0c-bb95b2cadcea | -7.85725 | -45.35217 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f746abd-572a-3b5f-8ffa-ae24da34519f | -7.85664 | -45.35619 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec31f1bd-2fcc-392d-8e02-bd7920758f96 | -7.85611 | -45.33553 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55147e42-9e27-3e80-83bf-dd44399d85fe | -7.85604 | -45.3602 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 729d483d-1662-3390-8c8c-626acc398097 | -7.8543 | -45.34761 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2df9fed2-cf2e-38e8-b716-90ed4fafb4a7 | -7.85369 | -45.35163 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69e17833-c4d8-354a-b1c8-39aeb03b52eb | -7.85309 | -45.35564 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1693c20d-d734-302a-852c-65feae1fd062 | -7.85249 | -45.35966 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6c8ed89d-a89c-31ea-b4b0-286861e2cc13 | -10.755 | -45.60357 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17e13e0c-5f3b-3101-9e59-bc242888faf8 | -10.75203 | -45.59859 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0d41fee-7f4a-397f-8bb9-b9d4c08b2ae7 | -10.75267 | -45.59425 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 429852e1-4a37-3370-95c7-25bebb780722 | -10.74906 | -45.59359 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9afee156-1ac3-39dd-b199-26bb1d672f80 | -10.74781 | -44.62543 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce8d0ed8-ec1b-39fb-b158-4b6c15f68045 | -10.74399 | -44.62486 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93ff8f8a-50a5-39b0-b872-133b8623de21 | -10.7395 | -44.62905 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1441376-77ee-3332-92a9-eab27b38c526 | -10.73882 | -44.6338 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47e23687-960c-337a-b016-6365ed0d0c6b | -10.62471 | -45.20392 | 2024-10-04 04:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40df2e16-1378-31c7-9132-61b91fc3a8bc | -10.62405 | -45.20834 | 2024-10-04 04:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73409799-0762-3908-bce7-61247b7da7d5 | -11.52604 | -44.91244 | 2024-10-04 04:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eddea29b-f489-3e58-a042-8a8aefdb9709 | -11.14698 | -45.03332 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3dfc477-9891-31ac-9359-a53dedda8815 | -11.14632 | -45.03786 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4d6c36-9de1-3fa8-acf2-6c162b7260b0 | -10.80002 | -45.60434 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ec912f5-4574-383a-98a3-3716a6bc4705 | -10.79954 | -45.58196 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d06fae60-5d89-3a9d-92d4-6f34e43e59e6 | -10.81027 | -45.61026 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4bb64535-33ef-3146-9858-6bf95ab8dcf7 | -10.80603 | -45.61394 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f49eff54-a57d-3620-b649-8f3971304675 | -10.80665 | -45.60971 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 11f7b3e2-ca23-3107-9bdf-d368fb53cd97 | -10.80303 | -45.60916 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f2efba5-b673-3b24-b270-934ec6e07646 | -10.80066 | -45.59991 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b36224ef-eb89-31ae-9e26-29e88477d74c | -10.89712 | -45.92737 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac8f249c-ce0d-3f81-a73e-f3d1ea330110 | -10.80364 | -45.6049 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 06719c2a-f027-35c0-93cd-83d4bbe7db5e | -10.80016 | -45.57769 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2e75eb3-a8c7-3012-9c72-2b830543e39c | -4.70196 | -45.87753 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2708b9b4-2a21-38f2-ab2f-f9b3bb680099 | -4.69119 | -45.87605 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 0bd7b112-014f-3c98-a0b2-eb8416ac012e | -4.68723 | -45.87916 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 0d9203c7-f7ed-36eb-9305-fccde27f6d2a | -4.68384 | -45.87864 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 29a9d312-fd19-3d7e-9fbc-5846e544d571 | -4.68327 | -45.88226 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 6d1add12-b699-341d-9063-d843f9d2a9a4 | -4.68271 | -45.88586 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4275330f-b139-32fc-ab1a-c5316d25a9c2 | -4.67988 | -45.88173 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 561f6d14-1fce-34ce-9d22-814f9e825981 | -4.67763 | -45.8739 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 38ff1a0f-bbc3-37be-8b24-e07947d5cca8 | -4.67706 | -45.87756 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a6451524-9be6-3cb0-bb70-ad1d936a96fc | -4.67649 | -45.88118 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ffe2c568-f494-3b7d-b18d-5c4c5a70bdd5 | -4.67593 | -45.88477 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d14a4c-11f5-3551-85b1-9cad23e5bc90 | -4.67424 | -45.87334 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 377b5da2-3562-3b37-91ce-af5ea1aea100 | -4.67367 | -45.87699 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 35c5051f-5685-3651-87ce-ce391cd9ef27 | -4.67254 | -45.88423 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba3d225-2095-3981-ac9c-e660ea37dba4 | -4.67085 | -45.8728 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba9ce8a9-8295-3638-af21-279942bbde2c | -4.66972 | -45.88006 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83723706-df25-3c2a-a400-3455b061419a | -4.59933 | -45.75094 | 2024-10-04 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d304f261-7310-3f22-8aa0-ef7e46130eb2 | -4.55442 | -45.65823 | 2024-10-04 04:32:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 431b0e1a-dbeb-33cb-a384-6602179c4f6d | -4.40951 | -45.3788 | 2024-10-04 04:32:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da3bddfc-1a41-393c-9768-746d0debc55b | -4.86705 | -45.77677 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7938a165-dbf2-3c36-8441-1172168a4a60 | -4.80832 | -45.79742 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c74e1f65-c3d8-3244-8858-14be2eb0245c | -4.70535 | -45.87806 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d02b532-6758-3ed3-8525-90fce7041b0d | -4.69062 | -45.87968 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8a2c36cf-045b-3859-8fea-6b45825bc43b | -4.6878 | -45.87554 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 913b7800-37bb-3d8e-ac27-f95c50ac78b5 | -4.68666 | -45.88279 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 95f7e365-d9ce-3efd-9148-64656d76006e | -4.68441 | -45.875 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 95ad665e-c667-3223-9c45-287f922ae688 | -4.68102 | -45.87445 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3e865b3d-de6e-31f9-9100-6a98e9bba419 | -4.68044 | -45.87811 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| fabf38a3-55d2-3c51-bbac-7c639136a898 | -4.67932 | -45.88531 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d31928a-cd92-36f1-b30a-27772b4554b5 | -4.67311 | -45.88062 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0fe5ffff-4e6a-348b-96dc-d14d67986cfa | -4.67029 | -45.87643 | 2024-10-04 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2639328-f4b4-3614-aaff-89a0bc2ffcde | -4.4697 | -45.93117 | 2024-10-04 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1be90b9-79f8-3f2f-97e0-0e59aba50b42 | -4.40607 | -45.37827 | 2024-10-04 04:32:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README98.md)
