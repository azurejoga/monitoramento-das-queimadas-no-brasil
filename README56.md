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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2792f070-29d6-3c84-9497-572388aee049 | -6.85297 | -41.70144 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0c8665c2-1f98-3bf5-82a1-b0116deaadf1 | -6.85238 | -41.70511 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3eb0e5ab-ea35-3ded-952a-460cc3ce9baa | -6.85135 | -41.68985 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ee1d79ab-c016-3454-9645-d8d745045839 | -6.84855 | -41.68562 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d8cedf99-2fae-3721-9157-26ac5de63c7e | -6.8484 | -41.70823 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f403be12-156f-3274-abf7-b46da5418a19 | -6.84515 | -41.68505 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d134af98-fe9b-3824-923b-86ef6f1e37a4 | -6.84501 | -41.70766 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 216ba11e-e227-3e69-a1c5-3b5befce1cd1 | -6.83302 | -41.80399 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c176d95-7cdf-3771-81ad-74033b4e8be1 | -6.83243 | -41.80767 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34e31b73-c43c-313c-b63e-405b810e16b2 | -6.82621 | -41.80285 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3834195c-d2ef-38ef-b4a8-be7a6e9aad81 | -6.8194 | -41.80171 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c372e6f9-6a65-3273-861f-7ea55b6f2184 | -6.80662 | -40.99018 | 2024-10-07 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a36258d5-03d3-3370-bad9-fb986de47c8f | -6.80329 | -40.98965 | 2024-10-07 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8b250ca-a03f-3fb1-b95e-db96d707eb15 | -6.7018 | -40.88367 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2c2a2056-216e-3419-a9e8-a1c287b2d94a | -6.70124 | -40.88718 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 11e43e72-99a9-36e6-9697-59063a474ba6 | -6.69847 | -40.88314 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d733bbbe-2455-3ab8-84a0-cf085ada7d0d | -6.69792 | -40.88665 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b812b12d-c837-35ed-af10-a19b69663bc9 | -6.66462 | -40.88127 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fe3e35d-1e85-37d2-a1c2-e42777f3d61c | -6.65851 | -40.87668 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d4a22e27-a0c1-3cbe-ad84-a66a446ae14d | -6.65684 | -40.88721 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76f46958-abb6-3fe7-b9a6-cc46cde05b0c | -6.65628 | -40.89073 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f027693-ead1-38b5-a9b4-1d8aac4f9069 | -6.65519 | -40.87614 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07dc2086-1c7c-343d-8696-7526ae0fb29b | -6.65463 | -40.87965 | 2024-10-07 04:00:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd8d5cc8-3d55-3367-bb4e-57472c3c7e18 | -6.48314 | -41.95197 | 2024-10-07 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 01accb35-ba61-3de3-be90-bb849d7a09db | -6.48254 | -41.95571 | 2024-10-07 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7fe78fb3-2cc8-393a-8f0d-3b70f1b63dbc | -8.42043 | -41.94725 | 2024-10-07 04:00:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfd7bda4-b205-309c-8fd8-ed8d1708f7cf | -10.22181 | -42.39142 | 2024-10-07 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c44654c0-8e7d-3492-aa46-ca4d3ccdc929 | -10.22122 | -42.3951 | 2024-10-07 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca8f4df6-94af-3aa1-9703-9b4df3037e97 | -6.43947 | -42.93886 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8adc9311-6608-3148-b24f-4851bd7b5d1a | -6.29199 | -43.45777 | 2024-10-07 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f5b565d-4305-3b02-b4b5-84a4d9d667e7 | -6.28517 | -42.90284 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 073cc6b7-05bf-3382-b93c-f0c5ead0d82f | -7.78082 | -43.11037 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c80cdfe9-7672-3645-a688-216db70b1098 | -7.77845 | -43.0805 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2544c640-3952-372b-819c-5646db13377f | -7.77794 | -43.10561 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 15327d2a-699d-36a6-99ee-f569e5ad829f | -7.77777 | -43.08458 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c232a777-19dc-353b-993b-1304482555cc | -7.77726 | -43.10976 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 830853fd-ceb8-3436-a696-9e5e9524633b | -7.7771 | -43.08867 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e8458d6-b72e-326a-9dd6-1877745716b0 | -7.7742 | -43.08407 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9872a650-2e8f-339f-bfae-0ea6e4ef300f | -7.74993 | -43.08103 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 790e4959-1cf4-3f3c-9573-7a172c149e4f | -7.74637 | -43.08045 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f185b07-7571-3bd2-9852-bb348ae97e55 | -7.74102 | -43.04585 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e221df20-9313-325d-a38c-c54f6d50a6e5 | -7.73681 | -43.04933 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1c4c2df8-42a3-3488-ba66-071aba5651b2 | -7.73414 | -43.06572 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11a3a8df-099a-3888-bd00-deaefde85908 | -7.73347 | -43.06989 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a5ef50c5-e6af-3438-8151-d337b451fc8e | -7.73325 | -43.04874 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3fbb3f41-8559-3627-9ccb-027bba9adcf6 | -7.73259 | -43.05281 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7285fd84-6680-3b4b-a449-e21574c2389f | -7.73193 | -43.0569 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 04bf2866-bd00-3f1e-85a8-426c4b0cfae2 | -7.73126 | -43.06101 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3d988858-d875-3275-89c9-2eff622e201a | -7.73058 | -43.06516 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 25c67096-94d2-3c27-8b47-94a2e379dae9 | -7.7299 | -43.06933 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 32862c47-eac5-367c-949c-faa3a4631496 | -7.72923 | -43.07345 | 2024-10-07 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0251e47-30b6-3355-b3fb-3f25e3bc2319 | -7.64971 | -42.96168 | 2024-10-07 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2bf849e3-4e37-330c-af47-23477a2d7d56 | -7.94783 | -42.46241 | 2024-10-07 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 99f33565-15b0-3c96-b4f0-be0ccdd56f86 | -7.94721 | -42.46624 | 2024-10-07 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 793256b4-e1b3-3014-9b23-0e45f858f654 | -7.93053 | -42.45959 | 2024-10-07 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11e73413-dcda-3476-a3f6-1a096455041a | -7.92707 | -42.45906 | 2024-10-07 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6e8c559-106c-32f3-ab9c-290cd49b45af | -7.65842 | -42.42393 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb85730f-a7f8-3613-9ab1-f665b5b99e11 | -7.65559 | -42.41957 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92a5b2be-f2fc-3607-a536-f48d985aa9d5 | -7.65336 | -42.4196 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1874f4cb-0654-33fe-8452-8e391ca7e1bf | -7.65212 | -42.41899 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6455117c-c34f-3803-8e21-9cf533c10f47 | -7.65051 | -42.41521 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5624f747-b845-385e-a022-e182540745d2 | -7.64772 | -42.48906 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 05a05365-9dff-3855-9e97-39df5b310e4e | -7.64708 | -42.4929 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fdc197b9-1227-3615-8e3e-732c18d0946e | -7.64645 | -42.49675 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6ef4d18b-c8c7-38ee-82bd-1dfed63932f8 | -7.64582 | -42.50061 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d21cf5ed-75b1-349f-8a4f-df55340a4e4a | -7.64518 | -42.50447 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a630ae1c-298d-3b38-b364-837f803991e2 | -7.64488 | -42.48466 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a8928b74-a1f9-390d-9126-8a540ede8e30 | -7.64454 | -42.50834 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 85cfd81b-7f5e-3a05-b457-52db4c111f2c | -7.64425 | -42.48849 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 94b417b2-22eb-39c7-b663-3a91539e2d9a | -7.64358 | -42.41408 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e40f33a5-2649-3c52-b2e4-762739664fb9 | -7.64107 | -42.50777 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1c0866b4-5bab-309d-a561-0e0c4495a04b | -7.64043 | -42.51164 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0089c541-fc3a-3969-a094-f1dd7ac0901a | -7.64012 | -42.41349 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 86144023-fa28-3f27-82e7-7af24d2f0f14 | -7.63921 | -42.50792 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e6c5d1d3-9b08-357c-9791-e09f85277967 | -7.63859 | -42.5118 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4f61697c-68de-30de-813d-a2fa686da088 | -7.63696 | -42.51107 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 739c8f69-4836-3e73-9718-aeb31f074ada | -7.63512 | -42.51123 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 80ee7c03-7c81-3829-8b4c-1b869fc4552f | -7.6345 | -42.5151 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 247400ea-b7b4-38e9-a469-932a748e4109 | -7.63388 | -42.51899 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5756034c-9fdc-38c4-bd90-a1313a14bc56 | -7.63326 | -42.52287 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 78c2d1fa-253a-3f24-beca-dc86cc2e6cbd | -7.63259 | -42.41616 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff44669c-4d4f-3d64-bea9-39fdcca81964 | -7.63102 | -42.51453 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bd84ad19-a3e0-31c1-a6ee-2b3e6fda53cd | -7.6304 | -42.51841 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4dc82a81-e405-3ef0-847b-9289bb0fe017 | -7.62978 | -42.52229 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0c4e8ea2-d10a-3304-9c87-65932ce149a4 | -7.62912 | -42.41562 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 124ae15e-61b5-36ee-8906-77c8771b5ace | -7.62755 | -42.51395 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 50915873-81bd-37a9-bb2b-9430cd00a6f4 | -7.62693 | -42.51783 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dcb3e62b-ddbb-394b-b2d0-adaec9fc4045 | -7.6263 | -42.52171 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 31e56f78-3f72-3c31-9c18-8ec8342503fe | -7.62532 | -42.50564 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2ffda614-3e47-32b9-9929-f742507e9e40 | -7.6248 | -42.44247 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8645651c-f17d-383d-9c0e-1f419dd31013 | -7.6247 | -42.50951 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03e6730d-65f7-317d-81b6-f736c98c598e | -7.62443 | -42.42272 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a6daada1-39ce-3bd8-ba2a-e7e4535ea19f | -7.62407 | -42.51337 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ea49a9fc-4d50-3317-8e71-8e6f9ecc3138 | -7.62381 | -42.42653 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73bf37a3-d7d2-36a8-9988-022d16f74870 | -7.62195 | -42.43804 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d319fbce-49f5-3889-8c17-68dc48fe93ae | -7.61998 | -42.51667 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c1d164e6-f59f-3018-ac37-aeeb08fed752 | -7.61849 | -42.43748 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ddbfb888-e28b-3ad8-9246-10147b5592fd | -7.61713 | -42.51221 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 45a69ca4-b955-3722-addb-16e8963ee88b | -7.61588 | -42.51995 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e7e13d06-3ab4-3b1a-b589-4654c4925572 | -7.6144 | -42.44078 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README57.md)
