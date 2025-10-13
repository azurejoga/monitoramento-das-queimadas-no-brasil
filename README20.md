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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ead39d0-998a-344e-8425-db69f3bdfb71 | -6.76018 | -42.80887 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24d05173-5196-34c1-98f9-5e532a82705b | -6.77571 | -42.82282 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f590f87-939e-3fc1-87ee-0aef5e9c4a4c | -5.21854 | -50.95035 | 2025-10-13 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f71294b-f50e-3ca6-b6b8-5477d2772e15 | -7.74901 | -42.41271 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e29a565-ade1-30ce-be29-b0a981b10834 | -6.76295 | -44.65142 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0b9f610-5706-3086-8c5e-1a0cc9c70783 | -6.42479 | -42.54645 | 2025-10-13 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87e71135-218c-3ba9-9586-b37583fbab51 | -7.50019 | -44.62824 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7b2b70e6-91dd-32cd-bf9f-1d70348984fb | -7.70486 | -42.3692 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91671bdd-7d44-3cfc-9e7e-a45393441f80 | -7.49686 | -44.62772 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d029b817-275f-3a92-abdd-306e445c930f | -7.48954 | -42.15454 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cca78bbe-44b8-3fb4-ac32-a6d1bfc2a09c | -11.596 | -47.51575 | 2025-10-13 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3693c441-766e-3cc5-993d-bfd750dc5661 | -7.80969 | -42.41249 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 102fc254-d65d-3135-9672-0286549e6a86 | -11.43199 | -42.31257 | 2025-10-13 04:23:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41fe74b8-2e80-357c-a998-5efe746a3320 | -6.62952 | -44.65829 | 2025-10-13 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b3cb39e-a974-3b07-8443-2a4093e0a355 | -8.40007 | -45.05674 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0a489b9d-4cfe-30e1-92c4-7e779da67ffd | -6.9476 | -44.41987 | 2025-10-13 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6088239e-4488-3095-82c7-95851405a7fb | -7.33657 | -43.86379 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9295abb7-9270-3520-85b8-cf7786b50960 | -7.74486 | -42.41618 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0c1b7e6-9d57-3f04-8257-736e53bf545e | -9.26649 | -40.43584 | 2025-10-13 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c60ac85-9b03-39a0-80c5-daf22d5d01c0 | -7.6883 | -42.38305 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d9614f2b-d7c4-3458-9ed8-feb2820c0a1b | -10.81605 | -43.98584 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c9defd5-f4c9-3c49-9f99-bdf7ce608491 | -7.68515 | -42.57223 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd3d1db6-c9d5-3f5a-8302-5184eb0e2d20 | -7.4913 | -44.61969 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 45a36ffb-d334-32dc-b6ce-06e04202c424 | -7.5476 | -46.09333 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a6662cab-0205-3b8c-96bd-8efd9366dfcd | -6.72805 | -42.07233 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7c511b9d-7af2-39e9-a49b-8daa4b1da111 | -6.42363 | -42.55399 | 2025-10-13 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8b509621-772b-356e-b6aa-ab2e9cdbcf38 | -7.92079 | -47.21043 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc78117-b57b-31c5-900f-d92974c76873 | -7.48683 | -44.60467 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee665df7-3997-33f3-ba1c-16f063554708 | -6.73339 | -42.08497 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b9a1f771-5fde-353c-8942-6ed88776c48c | -6.74928 | -42.16401 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b105eca-f552-3f96-bf53-59fbfee31fea | -7.50955 | -44.59037 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80dd1aec-a6aa-3639-988b-a73ecd281339 | -8.45513 | -46.11479 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 468ac99d-f720-32af-ae96-8a16124e799a | -7.8834 | -44.45244 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f34dd1a4-4a98-3b08-b306-16a5be570b90 | -7.14125 | -42.50129 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da6bad2b-1472-34aa-a1b1-e4e6793a9560 | -8.45848 | -46.11533 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c65b1cf5-16ac-3770-8e02-8843c599d9a4 | -8.45007 | -46.1249 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e528ecf2-4c5e-3fbf-b133-dfb259611cb2 | -10.80865 | -43.98849 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 081fd29a-1db3-375a-a4bc-faae490734ae | -7.32462 | -44.75433 | 2025-10-13 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b4a6987-5754-3967-a149-4164af167d22 | -7.50746 | -45.83963 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40ffb07d-7935-30b3-a5e2-becc4aa7ad3d | -7.21299 | -39.90257 | 2025-10-13 04:23:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0504a126-9188-382a-8ead-b772b4737a10 | -6.73101 | -42.07675 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1a2e0656-4279-3e73-a413-49fa1e17e838 | -7.95046 | -41.69384 | 2025-10-13 04:23:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 89845c69-9a19-3e71-8fac-779154784d54 | -10.0381 | -43.80787 | 2025-10-13 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5aa76c8-1b68-3ffa-b45f-001a78e97f4c | -8.38567 | -45.06162 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a920631-e98d-3194-bdd2-a0e0c4fe2d58 | -7.75209 | -44.2048 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f0df556-b261-3efe-94b4-4b1579d5851e | -7.3213 | -44.7538 | 2025-10-13 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 245892ae-2de3-3be4-ab0c-35cfd7bb1ce0 | -6.82021 | -44.67092 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25c0b9ce-6d87-3d0b-9fb0-7a45ff254647 | -11.5926 | -47.51517 | 2025-10-13 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab7a7cc-4b46-3ec1-8b2e-26c6473eb1d2 | -6.78987 | -44.52386 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd562293-3dc0-3559-ad14-0d33788545d3 | -7.49631 | -44.6312 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 750952c1-63a9-3ca1-901d-22a74247747e | -7.51211 | -42.16504 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e379ed88-2935-36e7-b43f-565752c435cf | -7.67788 | -42.38248 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d962252e-442a-3518-825b-ac8c5965431a | -8.32599 | -46.24331 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed476c60-831f-3e7a-8a2d-373d52c7de6f | -7.49303 | -44.65208 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 918e4e49-237c-3999-92f1-27d46a67007d | -7.37681 | -44.07752 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a301acf5-1188-39de-b467-f0a20480f555 | -8.46233 | -46.13417 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4993cb7-5903-3792-91db-b6ed6da28461 | -7.49852 | -43.06467 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1fe88d7c-3a3d-3a51-9411-78451c61a5f8 | -7.13774 | -42.50073 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45bf324c-dcce-3b94-b0ee-011768787780 | -7.14299 | -42.51347 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff1b098e-6422-351e-99d9-43b6bf1d07aa | -8.23961 | -43.37401 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 648bb924-92c4-38c1-a926-0a61374bf497 | -10.80635 | -43.98052 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06cfb355-9167-387d-95a4-7b3be14a12d7 | -10.79664 | -43.97524 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a98a484-51fe-3b24-b823-3cbae9c3f5e0 | -10.80579 | -43.98424 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3de3401-ec25-35fa-a14d-40cd749c0da8 | -7.6895 | -42.37501 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e9c07189-eb10-3392-bed0-b22178b70a80 | -8.32714 | -46.23617 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1845d7-a1bb-381c-8fe4-8059ecf26f19 | -6.67659 | -46.02748 | 2025-10-13 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bda35b55-3ddc-3752-beab-faa6ca36a4e5 | -7.48382 | -42.75646 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b219bbbc-96d5-332d-bbef-94e2c10635c6 | -8.18233 | -43.31613 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9712ab8-d118-3c45-9f89-bd67fef7302a | -7.49311 | -42.15507 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 892b1996-3b64-3eb0-8df3-93f836410605 | -7.6564 | -42.56866 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b073219a-e59b-3102-805e-c16811709ace | -7.34781 | -44.08754 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b032157-1a33-39ca-9ebb-d099ef0ffca5 | -7.45676 | -42.03273 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87277cba-d86e-3de2-a8e2-f9278528f832 | -7.54703 | -46.0969 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c3124588-2c0f-3a28-8fce-ba7fd14690cc | -6.58569 | -44.38077 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c57b5a8e-1809-3f59-94e8-1c28ed2ad0a6 | -7.35224 | -43.85169 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 590e6b1d-4e0c-35ef-9449-89c6f1bc0962 | -8.47395 | -46.16895 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 231021d6-18d8-39ad-8a99-30145447c968 | -10.03172 | -45.69058 | 2025-10-13 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02a0f846-c3d7-3348-9d19-831b35080797 | -6.86123 | -42.16296 | 2025-10-13 04:23:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f2ee162-aff6-3474-9459-f96d5fd05694 | -10.14567 | -44.55592 | 2025-10-13 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602cce91-6ed2-399f-8207-e110d7df2ef2 | -7.49353 | -44.62719 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7a24dfde-ba62-33e4-a559-c7a2cbccae43 | -7.88006 | -44.4519 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76cca774-2ff5-329d-8b25-f4f472f45ff2 | -6.77225 | -42.8224 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bda87ea8-fc84-3581-8bb9-6c313b4bc96d | -7.64526 | -42.57099 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6678cc79-e2b4-3e04-8153-932570e363e5 | -7.35226 | -44.08099 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2789bcd-bafb-3d5a-b4fc-b8c0c271ec56 | -8.46126 | -46.11942 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 880fb317-da2a-361d-b860-c40926453311 | -6.70005 | -45.97587 | 2025-10-13 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a84228ca-9cf6-37be-a3ad-873002fdc756 | -8.46846 | -46.13879 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6aaf5f3-ad50-3179-94d7-4648f2005d23 | -8.45791 | -46.11888 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c73bd755-acd5-3c95-ba03-9bb43d894bb8 | -5.22299 | -50.95114 | 2025-10-13 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be16bfce-6895-3d18-b9f7-3ee433257f18 | -7.6901 | -42.37097 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41eb8814-36d4-3ad9-bdd1-543f1f659bbb | -6.5107 | -42.43292 | 2025-10-13 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e860c4cb-c412-39b9-9b2e-30437093c7e5 | -8.44672 | -46.12435 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c0f8929-cda4-3c02-8e15-84e4f3b0ed3e | -8.47744 | -46.12565 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cab0f528-4199-3c66-b729-bdea2a146b05 | -8.48213 | -46.24703 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c580bf0-e26c-3ec4-bb70-aecbd9e246be | -8.47409 | -46.12511 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10df1f6c-7441-3663-9b7a-9d931553447d | -8.46682 | -46.12759 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaa0872a-db99-3e54-9ee2-636168765b63 | -10.80237 | -43.98372 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a9d287-21be-32e7-96b1-786b7c18c58c | -7.70547 | -42.36515 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0085a1de-987d-3c08-8106-1f7a6f8c6fa9 | -10.15014 | -44.5493 | 2025-10-13 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 402d7dd7-77a9-38e8-b4df-0c64d90106e8 | -7.78245 | -44.05354 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
