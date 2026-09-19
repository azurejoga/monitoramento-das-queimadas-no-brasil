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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 004d58d5-50e3-3781-a7cc-c86f015de5a1 | -5.33459 | -48.98688 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e27b2370-4ac2-34a0-ad74-63189676ef59 | -5.762 | -57.45344 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5c214ef-ac73-3fcf-a3e3-3b6465b7e531 | -8.75999 | -46.91742 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c0dbb95-6163-3840-8c01-9bfdc0d9c83a | -6.63405 | -51.25221 | 2026-09-19 04:38:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98900314-53ee-3719-90aa-eae8e4d3764a | -3.73716 | -54.64227 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d4db9d5-8f4e-3a3b-818d-35efa39b3ba5 | -6.96351 | -42.56116 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dee8fd0f-c8cb-3f25-811b-133a46b2c612 | -7.69128 | -46.08515 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24ece265-8095-3078-93bf-5c45447820ae | -3.73023 | -54.65092 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1cdc16e-5f10-36a2-b56e-0ddb0840c50c | -7.64744 | -46.10329 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca870946-a548-3c0a-bfda-b05821f6e63c | -5.88843 | -52.08898 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3644b644-4051-348c-b37e-c887cce7f55b | -7.66635 | -46.13493 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3163d19a-1bb4-3b39-ac1c-b7beb2985132 | -7.77312 | -44.87134 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b2519c8-3195-33c6-9980-00eddf0f1f20 | -2.8233 | -50.47598 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f40f26c2-7dad-3bc8-9024-e9ca2d623633 | -5.86398 | -52.05175 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 600a2660-6384-3ec9-b7ce-48a5e50fec9d | -7.22471 | -44.22464 | 2026-09-19 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b15b8d-cb98-3dc5-80c5-10949c7c1216 | -8.46805 | -47.0064 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 340343d5-e6a2-3422-b03d-7becd4cdb306 | -3.37438 | -50.45781 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 877b2c5e-026c-3dce-abe9-c1d49971869f | -4.11224 | -49.06807 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8d7fbb8-1f16-3a37-86be-c55ad864ec3a | -3.23486 | -46.94342 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f2542a6-952d-3358-a6d6-faf2ef150452 | -4.53446 | -54.93381 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c25b485-385e-3022-bc04-4080e4a35ac9 | -6.01144 | -51.79925 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2cd29bf-fe49-3720-b7e6-2f2cb8ea19a9 | -7.86862 | -45.15577 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb0bf7be-09a9-3e96-bfe5-fbf34d7a7916 | -3.23653 | -46.9547 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| be5c5582-63b0-3d15-8d30-4ce964781b35 | -3.36637 | -50.45649 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d41833-fca0-3157-8fc9-479fae2cd662 | -3.33038 | -50.11725 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21e0c049-bbf2-3d3a-87b0-e3db3775e4c7 | -3.55463 | -50.29084 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a3294c5-efc5-3729-a5df-c7fee494bdd6 | -3.64273 | -49.96859 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e3fb6a-a362-385d-9841-5b7f014ec643 | -4.71396 | -55.69337 | 2026-09-19 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 401eff40-2b17-33c1-83a8-cb31fa187571 | -1.0966 | -48.05818 | 2026-09-19 04:38:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00c2f65f-3cb9-3cf5-982e-881bed8bc800 | -6.33289 | -55.27973 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a808d1-6607-33ab-a937-5c046ba73bf5 | -8.12488 | -44.82494 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83891ce2-6080-324d-892f-f29cb6997245 | -8.47094 | -44.68116 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e70be4a2-d9d7-3bd9-8ddd-e02aa9d63916 | -6.02287 | -45.35672 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 310f08c3-4119-3b77-8901-d6332b68ba84 | -8.43958 | -45.74764 | 2026-09-19 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8408aacf-4ff6-3fcc-b1fd-a81fe8503692 | -1.19439 | -54.21793 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fcc4024-c752-3c06-bccf-424ee8f64cc8 | -5.23121 | -47.5647 | 2026-09-19 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ea1d9d-c435-3645-a942-4652454e05e9 | -8.77107 | -46.91204 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efba6710-8f77-3b33-9275-8a326c32c96b | -7.82024 | -46.63845 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6a2d458-633b-31e8-a2d0-7582eaf9178c | -8.12469 | -44.83332 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59c56fa2-1380-3328-82f2-266e54cb28eb | -8.37972 | -47.20405 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0a95a37-8a92-3110-985b-e6b5e97a9712 | -7.38145 | -46.15808 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c56b34a-6485-3549-909d-d97acd5304e7 | -8.76054 | -46.91393 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13137ac5-b5c2-3763-9328-9c0c0df2f4a1 | -5.57778 | -42.73273 | 2026-09-19 04:38:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c5a504a9-5cae-37f6-b89d-3f059fb948a5 | -8.86425 | -45.93053 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4746a27-6f35-32a4-810f-a407cf756ed4 | -1.5831 | -54.4281 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3717b092-d941-3a6d-82b1-b05e15fad861 | -5.89777 | -53.56749 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a6a4e77-40e3-3f5c-af2b-a49323d51b48 | -3.37509 | -50.45348 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed818861-41b5-3871-9ae7-0cf002c6db1c | -3.75912 | -51.14203 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce915c86-41fa-300c-b5ef-77e1ec2a299a | -2.8285 | -50.46952 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a10536b3-247b-30d8-8e05-c2aed42cb16d | -7.69464 | -46.10718 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3893bd6-e171-3205-a9cd-25fc94731d7b | -1.18903 | -54.21703 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e97bf8df-4fe2-326a-99ec-8ab652a57850 | -1.19638 | -54.21925 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae93484c-16fa-35ac-b2c3-9c7656e93281 | -6.57951 | -44.15667 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 600a5053-998c-3d46-af1a-bc5709d9ce66 | -2.29401 | -48.59451 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9296b8fa-75f3-3fbc-bfa5-8fc7502a2bf0 | -3.23315 | -46.95417 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b07a3dc4-e367-3158-ae52-9dec64ab3e33 | -5.74191 | -57.60194 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b5f47c-5b5a-3f73-9aa4-9a393f1d5cdb | -1.49522 | -54.97398 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837d35ac-7330-3308-a199-1a3c9da576e5 | -8.85027 | -44.91885 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c9ec388-f1e5-3ad9-8f86-2fa446cdfa65 | -3.47258 | -54.6942 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19c3ae57-bb5c-37d2-a33c-ec9781b336e8 | -6.08563 | -44.30184 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 954b02f5-45e8-3938-8fe3-626a76e196cc | -2.82271 | -50.47955 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68a6e611-5801-3d78-a2d6-e7000ba0db2a | -3.85253 | -50.0077 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9419d399-22d2-3b09-a20d-a0f07d8bb317 | -3.36708 | -50.45217 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cbee00d-7fea-3ebb-adc5-1040d082708c | -2.89887 | -57.80544 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d831eff7-9d22-3dfd-bcf5-a2bccc5c3d34 | -6.00944 | -49.17036 | 2026-09-19 04:38:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b89a9b-d0b2-32a6-9bd9-3f95bac43c9f | -2.66497 | -49.48182 | 2026-09-19 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4e0fa73a-45ec-31f0-a50e-1e23c81b7781 | -6.78198 | -46.46536 | 2026-09-19 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552a8171-5bac-3a28-9b7c-476d3da2e703 | -5.06808 | -44.85332 | 2026-09-19 04:38:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d27eaad-3dcb-3a2a-b628-10f2ecd26ff3 | -3.37677 | -50.4432 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37deefaf-0249-3101-8c15-8218220f3696 | -6.00369 | -51.79395 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27cd19dc-6013-3465-aac9-a7d1a568c2f5 | -6.36715 | -58.31187 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e614d6e5-1624-34f0-b9ce-d044342953a4 | -1.96247 | -54.69505 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 233e3e7a-f69c-38bc-8c27-5ed3d77a0391 | -8.36523 | -47.25203 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 249dcf22-f4a5-3307-a9c2-abb6cf73f56a | -3.48351 | -49.5093 | 2026-09-19 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d57943eb-57b8-36b8-8bae-cf33b62efad6 | -2.14449 | -50.90318 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c391ab5-b8b2-3e2f-ba9f-03675d320053 | -3.95272 | -49.04132 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2858fb5d-b185-358a-a53d-ff1570d93484 | -6.58298 | -44.15719 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0804728a-c6e1-3b8f-a49c-63c38dff36a1 | -7.7604 | -46.73604 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f66d8337-b89b-3335-8d52-a67412c459d8 | -2.82157 | -50.46117 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7d279284-f9ba-31e9-94de-e627c494eac7 | -7.41042 | -49.84696 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b6c157d-5df6-3235-9c11-cdff38fbd551 | -2.39051 | -48.52638 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cdbadf3-20be-35ba-980f-f98fe9ac72a6 | -2.89712 | -54.1868 | 2026-09-19 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a81e77d-f2df-3cd7-a79b-aef1d121a592 | -7.67134 | -46.12499 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6b5c8af-44da-3329-933f-7d97a5cf4c19 | -4.35781 | -47.78238 | 2026-09-19 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c167372b-8d2d-31cb-a265-4423e427df71 | -1.96792 | -54.69603 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89eff5b2-1a2c-30ae-912e-67c06ffba7af | -3.02045 | -51.1937 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10dcb428-b3cc-3996-aabe-34d7be06cf7c | -8.8131 | -46.94387 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f75ba559-0f5d-31e0-825b-cf0119c273bb | -6.08849 | -44.30613 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aecbc82-d296-3e0a-92f4-85fd96cc1eef | -6.98582 | -42.1869 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b6fab2bf-75bf-3d6e-a1ff-3d5378361a9b | -5.92997 | -53.52142 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93eb623-f029-3e2d-9c21-117bc93cf476 | -6.35988 | -58.28534 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d5d7ad-031d-3625-a2a4-fd1111448e41 | -2.81462 | -50.47823 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79b20a87-9789-36a9-81ef-84b40a3d027e | -2.90542 | -57.80661 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3acbc9f-5f54-312d-89f0-37ee21efa574 | -8.68052 | -45.42878 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dd8ef56-6881-3ed3-98eb-3a887dc2dabc | -7.86606 | -50.22786 | 2026-09-19 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcac24ec-9620-37ac-9b70-e93f36d21bcf | -7.65077 | -46.10382 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b149c44e-ca5d-3f0e-8146-a7ec11522e9e | -4.48909 | -55.48685 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 003fc43b-9dab-3e15-ae86-e4d178172610 | -8.57344 | -47.2607 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00ac6215-71ce-39dc-8764-8c3a58798a9f | -2.39118 | -48.52222 | 2026-09-19 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74c5f9b1-e405-330d-8510-90ad6c37df6e | -8.29296 | -46.8533 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README48.md)
