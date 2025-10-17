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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 696b25a7-de65-31e4-b34c-07f3b1e87b00 | -6.39522 | -41.89851 | 2025-10-17 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 00dc6f70-145b-3dfb-b0bb-1d4caa40cd77 | -9.08085 | -48.04081 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d6c99e5e-733e-3def-8613-17856a599754 | -9.35462 | -46.93282 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 094c0f15-0b43-3bbd-98e8-6120d11e2c22 | -9.05127 | -45.13747 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a967c6c9-7ce2-39e4-b8a7-5532a2cc01f8 | -8.40672 | -46.23447 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 01b16f66-35dc-33c6-9f85-f3b10ac1b864 | -8.23513 | -43.43218 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ab176381-824c-37cd-90e3-df3c565c7457 | -8.39256 | -46.25245 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9a8b93c0-caeb-3621-b65e-127a309b7d10 | -5.87757 | -44.83898 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 09ce2f3e-00c1-3c6c-96c0-4f8bbfc09ee7 | -9.05674 | -46.99052 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8d52e44a-a891-364a-8237-62d0dd1cce3f | -10.13659 | -44.58131 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f9f14021-d78a-3c28-ba1e-8592fa51fc5d | -8.31234 | -47.86386 | 2025-10-17 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8b8788ce-4cd3-3a04-ada9-2f37fe84d82c | -6.1834 | -44.32114 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ae583f04-7a1e-3a61-9d1d-29177b4a5415 | -8.25986 | -44.07331 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dd836e96-6c6f-3452-88a7-0f9071df7849 | -7.35763 | -42.96471 | 2025-10-17 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a5cbbe77-a508-32b7-bcc2-8bd7c0b92e0d | -10.10396 | -44.62 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 052ba088-a54b-32e0-953f-a610fd845b29 | -5.26483 | -44.21376 | 2025-10-17 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6040e14a-eb0f-36bf-a349-57857b6d7a58 | -7.66371 | -45.63442 | 2025-10-17 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 65e05c0f-4c80-3fd4-a170-a8753df710ca | -8.19967 | -43.96429 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39414b2b-ee1a-3ef5-b956-237d940ae96d | -10.89052 | -50.23678 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 7934a205-bdb3-3ad4-ab9f-52f6f6ae2fd0 | -5.86396 | -47.57823 | 2025-10-17 00:13:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9d7b0b4f-2843-34ec-93e4-140c57aea714 | -9.13214 | -46.63733 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e86f82d5-e427-32e8-ba1f-d1ce8047de55 | -10.1312 | -48.89756 | 2025-10-17 00:13:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 86198495-5b32-30d9-a5aa-46cc5e0e45fc | -6.94671 | -47.73349 | 2025-10-17 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 33a64e23-9929-3e89-81ba-c2587d0db9b4 | -8.26109 | -44.08218 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5eda8ebb-4c7d-3b3f-8bda-30321dd31b07 | -4.86443 | -44.4405 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 83b5069a-cd9a-3814-8f72-b05928d30e47 | -6.37472 | -43.57904 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2debd979-a83c-34d5-8923-1ff8fd4ae6cf | -8.32254 | -47.86245 | 2025-10-17 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8cc09ee-28cc-33cb-b4b1-eb17d0c461cf | -10.28344 | -44.04625 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1b351a3f-7705-3c77-9f0f-3714a3a1e6ea | -7.75926 | -42.48249 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9fe928cb-47d9-3e24-bc47-116c4c864645 | -7.47238 | -42.16984 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e20ab034-df76-3fa8-aa99-49dbd325c891 | -5.23511 | -43.79718 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b747452e-53d4-3a13-89e5-7e7b7b55c35d | -7.10931 | -44.74097 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 96669b08-b68b-335d-9742-3739fc97a353 | -8.08753 | -45.43245 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12bed916-1dd7-374b-bcee-708c4dbb133f | -7.94838 | -44.14553 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 9348def9-1d5c-369c-9812-8c4bf57c4639 | -6.5999 | -44.7957 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eace6192-80e7-3542-bc38-2029bb3e3e9c | -7.00656 | -42.00446 | 2025-10-17 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e7a95f55-c32f-3dce-9f70-9c4fb20a47ba | -8.41325 | -46.28403 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1f1ba6d0-439f-320f-ac4f-fff69f17c584 | -10.27216 | -44.0297 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| ca58c286-0f64-3937-b5f7-932541e05299 | -8.28349 | -43.38805 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b2926a59-109b-3fd4-b8e5-dd359f955841 | -5.50884 | -43.77719 | 2025-10-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0518c313-3245-3552-8804-197c26ed97f5 | -8.28222 | -43.37898 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8b67edc4-e3ac-3b81-a64b-92a834339f51 | -6.14328 | -44.22731 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b2ae63a4-b033-3e1c-b8b4-604bcd29d1d3 | -5.28619 | -47.9212 | 2025-10-17 00:13:00 | TERRA_M-M | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 06d39270-4dd5-359e-9791-a607c4a20449 | -8.16214 | -43.30946 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a4125eb4-ed77-3f73-b84d-36c17d19ea9d | -10.86165 | -44.42911 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b6b30be3-50f8-39a0-b870-04f238236e77 | -6.42253 | -44.71617 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9147933b-ff27-3da3-90f2-f0bcf135fe34 | -11.77077 | -51.15963 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| efde0ca6-374c-371d-91c3-5ab3233df092 | -10.49662 | -43.39657 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 05134307-cc26-3b35-88df-1f8f6747706f | -8.45102 | -44.1873 | 2025-10-17 00:13:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cc70f87-09e2-3ea0-acdd-42a9504dbe5a | -7.46165 | -42.66401 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f3f10f5e-5e92-37eb-8bee-a0fcccfa223d | -8.17108 | -43.30816 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c8ae5e34-4163-38ff-afa0-7e88b2343282 | -7.46788 | -42.13915 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8937adc5-d037-3cb6-b155-0f4938ff70e3 | -7.11813 | -44.73972 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 57b69d11-daee-37f7-9ebd-06101a539208 | -10.56559 | -43.61731 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0035633d-efe0-3894-9e0b-1a291ec78b04 | -7.7528 | -42.50341 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ded4c24e-ac5e-37a5-94c1-159d509d09af | -4.96454 | -44.96624 | 2025-10-17 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5ee7e62c-5aa7-3fb1-ac5d-08ff13f1f403 | -5.91169 | -45.34711 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fdbcad67-c5ea-3731-8e3c-c06bd753675c | -7.20164 | -45.48225 | 2025-10-17 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2d973d94-9f12-3c88-8a71-a31c2d1259a6 | -7.46646 | -42.16619 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 66b112e3-1430-30a6-a5b7-9ec4e3f5bb34 | -9.3449 | -46.9342 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9dd8feb-c608-3f4d-b217-19e29f6261e1 | -10.87531 | -50.21837 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3a5f121f-f59e-33b7-8073-5851780aea55 | -7.68188 | -44.62296 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da64a98d-b0f3-3104-a8df-48f3e5b068fb | -5.95042 | -43.18024 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 734db741-5d0c-3cf4-ae98-0f2e64138c7e | -6.07211 | -41.91939 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8f68e661-692e-34de-9fc9-824655329eb6 | -5.45841 | -41.02492 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f74f6b90-3fda-3fb2-8b9b-1be25a57ad35 | -8.55664 | -45.49577 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| af370b6f-979d-3fd6-9614-f219226bc022 | -6.14563 | -41.79175 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3504b03f-774f-307e-acc6-71e591649182 | -9.97756 | -47.00957 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cf48bfe3-10b7-3f73-b787-34e67503c36c | -8.35814 | -40.3358 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ed42198b-fdf7-3068-9779-2cb7b76caf2a | -9.17977 | -47.71191 | 2025-10-17 00:13:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3569d4c8-e8c4-3238-ac1c-05d7c001d8b2 | -6.57047 | -38.85541 | 2025-10-17 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 81fc371f-c616-36d0-b037-774805270c95 | -9.65092 | -48.72329 | 2025-10-17 00:13:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ed05e474-d6a5-3d0e-895e-29d92239803f | -7.46445 | -42.68337 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e6746522-7eed-36be-92cd-ede35f42621b | -7.45557 | -42.15733 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ddbdbb38-2b8b-3dec-a043-59b5ff060f14 | -7.48469 | -42.75888 | 2025-10-17 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f01efeda-6824-315a-807a-513774a05fbe | -5.74714 | -43.37564 | 2025-10-17 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8656df9c-92cd-3bfb-a619-f5676cd84da0 | -5.16498 | -45.21266 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e42fe653-807b-34e8-8444-439fb3a4d36a | -7.15812 | -46.53163 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8ab17e9d-bc59-39d7-90b1-2ea7b9c0569a | -11.19084 | -49.8024 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 106d157a-1b0a-347f-b01a-149781174b4b | -5.28769 | -47.93224 | 2025-10-17 00:13:00 | TERRA_M-M | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 8bb4a5d5-1425-39bb-97ef-aed641205a21 | -10.51038 | -43.41562 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f18dbf5e-f548-38db-808e-918f674a0232 | -5.88619 | -43.90233 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5b5e0a37-cb2d-3e8f-ae23-fa18673e5ee3 | -6.55556 | -42.9622 | 2025-10-17 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| de312768-676d-35be-bfc5-205f68874d8a | -10.76 | -47.87373 | 2025-10-17 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 79d38b73-72c1-3ca0-802c-2ec1cd3c2e69 | -8.47321 | -50.10245 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bb3a8535-d644-37bb-85c9-b5605c853223 | -10.50286 | -43.44118 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cea23f7d-b822-3596-aa51-df67635d8ff2 | -6.93356 | -45.14496 | 2025-10-17 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 643dc8f8-021a-3dc6-8280-524845ca2f53 | -7.62505 | -47.84059 | 2025-10-17 00:13:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| aa1eda74-6c71-319b-9cc0-8d6775e83505 | -10.57441 | -43.61604 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aaa25ca2-7953-3c4c-8709-e9462df61c7e | -6.74529 | -44.38504 | 2025-10-17 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2bd5cda1-21ee-3e12-8ddd-b140a5de2646 | -8.06715 | -45.41674 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5fae63bc-94a0-34cb-8ecb-542697b3caea | -4.3882 | -43.41237 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| df800cd7-eb1f-3d81-b014-8e84bd1df95f | -5.47632 | -44.66877 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 48342003-5007-3c02-97a6-f50ddcb6f142 | -4.48204 | -45.67231 | 2025-10-17 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| bf057c27-8ac5-342d-813a-e62b0ad35627 | -4.92965 | -47.07095 | 2025-10-17 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 94e96c52-b872-3574-b579-5eb08b32671b | -4.38685 | -43.40279 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1726443d-ac3e-3428-8937-ae4f9ddb6f18 | -8.45212 | -45.12888 | 2025-10-17 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3d769ef0-41fa-3a7b-8908-92c60c6e7a95 | -10.257 | -44.05005 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eab0958c-ef66-3459-8bab-b9f619eb165a | -4.82357 | -47.08792 | 2025-10-17 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 69f99d73-70b9-3215-a53e-7255d0eeba14 | -11.52153 | -49.15342 | 2025-10-17 00:13:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README6.md)
