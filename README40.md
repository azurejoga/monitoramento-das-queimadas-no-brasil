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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67247dc5-a106-332c-baa8-ebeb86504f7d | -2.14441 | -46.41496 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0466683f-c62c-3d6e-8019-eb483e93c47f | -1.20623 | -51.78321 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2805d1c3-1f74-3e2a-9dff-d16bc5785efb | -3.53591 | -50.25746 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77644eeb-da13-3e6a-803b-815695fa9962 | -0.94847 | -51.72764 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8a4e64b-319d-3a37-9229-9af5f523d188 | -2.6825 | -46.21193 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a2a8be1-15c4-31ea-9137-a6d107847646 | -1.22802 | -47.35964 | 2024-11-17 04:29:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 729fd78b-e8e0-3462-b0c2-8aaffc448734 | -2.18702 | -48.26034 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bba1a1de-b808-37ec-bad3-cc873ad96d27 | -2.57308 | -49.07845 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70080fba-ebde-372a-ab65-9d51cda31451 | -2.39542 | -47.92756 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0818d89-7ec9-3076-a430-cb8e18d9910f | -5.62717 | -46.36321 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 458f83dc-02b4-33c4-b889-a3bca236b7a1 | -2.67362 | -46.20344 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2c0e528-b513-3538-84b9-310329e912f0 | -3.52895 | -50.2657 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e31e771-a70e-300b-9fc2-b7fbf8e3fda1 | -5.17963 | -38.00157 | 2024-11-17 04:29:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ff4cbe9-0477-334c-9893-bc7813a55a19 | -2.19089 | -48.38931 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8958e62c-4660-3825-ae61-1692545341f4 | -2.07048 | -48.53693 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60885dfc-2387-3f2a-b0b5-c8bae073d2db | -3.51446 | -49.94386 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2365d786-11e6-3124-97f3-e9ac7b0f2dba | -1.83068 | -46.59463 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19e8dbb9-4741-3e71-8bcd-ac0718053d2c | -2.29564 | -49.12947 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 623275a5-1b98-3657-b7c0-270596781d52 | -3.89101 | -45.91556 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9914647c-8a03-3d1e-81ea-dfcf41906ed6 | -3.5351 | -50.51365 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9da4e72f-3b8f-3911-91c4-edba6ac9e113 | -2.65924 | -46.20834 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5037a423-ba55-399b-b17c-7dc62d3a8071 | -4.39579 | -50.49892 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d50ea4b1-eb18-3cdf-b3c1-801117cef172 | -2.34879 | -49.12172 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 676518bb-cee4-35a3-9701-70462e691eb8 | -2.1652 | -48.90915 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdd7aa72-394e-35df-8a1f-34dd6f66a45e | -2.23081 | -53.61511 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0025395-5e88-33aa-bc88-28189b72ba56 | -2.16741 | -49.25403 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04602e14-b082-37c7-8db6-b00aca3fb976 | -4.21573 | -47.22207 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7117e1f6-8ee1-3d49-be37-48a140e7925b | -3.53154 | -50.24923 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ae2af5be-2139-3c04-aeec-9cc210e1c9bd | -1.54954 | -53.09914 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bb70821-de92-3e32-9a93-e261f4a4c843 | -3.68924 | -50.11786 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2073651-c375-37b7-b39d-540dd9503355 | -2.13671 | -48.88941 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a0a3f4-62c8-3535-9ef6-5850942be911 | -2.79735 | -52.99768 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282483a3-778c-3c3a-ae6a-e2c2d4931bac | -6.98717 | -39.65892 | 2024-11-17 04:29:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cf589cd-86c7-3d79-a1bb-45855d399490 | -3.62332 | -50.21688 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cb5d227-07ae-32e7-a6a6-5d9b7d9981d2 | -0.88145 | -51.72866 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e8168a2-3931-310c-865b-a5007376f444 | -3.27627 | -53.01339 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca7dc6d8-565b-3143-9975-1cb9f8c0467c | -2.22587 | -46.82574 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 072eeafd-8424-34e3-bf95-48daa1fa4fc2 | -4.15758 | -48.60035 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1485a040-5473-39e9-8e33-eed27c173539 | -3.84982 | -46.63156 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f41ad5c-6d62-3015-9fbc-3fd1c2aef620 | -6.93593 | -42.81104 | 2024-11-17 04:29:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbedfd5c-6e1e-3cf8-b1cf-42951feacb61 | -3.34774 | -46.43278 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ab74d3b-1cfe-3022-a252-0fb2fb65fb6b | -6.47419 | -47.50966 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17800faf-b799-33e8-b1c5-e00042244036 | -7.51826 | -40.5864 | 2024-11-17 04:29:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a62af43-66a1-3126-861d-bc314fcffc9b | -4.28125 | -48.20847 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1a29e10-b5b2-3875-a97d-f8b4c77b58fd | -1.74088 | -47.98383 | 2024-11-17 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ed2b70e-be6b-37ff-9e4d-7aa945bbaad2 | -3.50158 | -42.1952 | 2024-11-17 04:29:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 85ccc0b5-1633-3a44-8406-8a6876b572e5 | -4.21627 | -47.21864 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e50ade-3636-3d21-ade6-0a7113b62a5a | -4.84161 | -44.48677 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9925527c-5ca2-39c8-9f78-f376122476cf | -6.82169 | -46.77979 | 2024-11-17 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f3a6dec-bc23-372e-b8d0-98f72ac35cff | -2.22672 | -48.36893 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19515329-bb01-3b1c-a98a-edf5b9d24aba | -4.2533 | -48.53199 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a71d9571-8b75-3184-a313-17c8f3122acf | -2.2323 | -53.6061 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eeaab57e-7289-3ca2-991a-aea2a50305ff | -6.81834 | -46.77927 | 2024-11-17 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3d4080b-fdae-3212-978b-676c10727f42 | -2.22267 | -48.41613 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b376b6c-6997-38cc-9d89-150a28ca77b6 | -3.99693 | -53.74164 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb96aa5d-8d46-36eb-83a7-1c763793c8cd | -1.95814 | -47.83754 | 2024-11-17 04:29:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808d58fa-1470-3421-90ff-b701fa4202f2 | -2.66751 | -46.19894 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b07c2678-8e89-3741-a014-f6a7d209fcd7 | -3.5403 | -50.45837 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b524de69-62b7-3624-b80e-8d575834d592 | -3.88401 | -46.60845 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8ab834a-0e9d-37ca-a115-a575a7a1434a | -1.29046 | -51.96297 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 28c7f442-4c2f-34b6-adcf-397e304a08f3 | -3.84659 | -51.39338 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a409411d-796c-3ff1-9f19-60d8d9322daa | -2.40192 | -48.45171 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 547f1ea8-c848-3e23-9b66-01f42bd3c202 | -3.03967 | -45.75577 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34417933-859e-35db-923d-9f4641ad6bfb | -2.13664 | -46.39964 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b46863f-1556-3ed3-b694-963aacde87c7 | -1.21728 | -51.7923 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6e7679c-2065-320c-8785-59327246b8d9 | -4.04973 | -44.7653 | 2024-11-17 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f9ec49b-ac13-3077-9f7f-5ea6db03bce5 | -3.79498 | -51.37458 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b257e65-5ef3-35b1-a655-32a44f891ea4 | -0.95252 | -51.72828 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf935277-e3fc-328d-8779-7543c3f01d7b | -2.39653 | -47.94209 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a617c94-ddb0-3f08-ab19-9e053133326d | -2.26054 | -48.28629 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83b80d40-f13d-3d73-92ef-f4ae623a70ca | -2.64376 | -46.15576 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 256eed5f-3f58-302e-904b-74ed57802165 | -2.68909 | -46.69066 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968c3e19-4209-3dd5-8c90-a9af41a54c1d | -3.0925 | -45.17424 | 2024-11-17 04:29:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c076549a-bc71-30b8-9d43-d76170b7839e | -3.24106 | -46.44081 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92b7321c-9298-3e25-93de-cf13a9f3f46e | -3.23666 | -46.44721 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3808b5c-2d64-3ec0-9f5d-d0f5dbc529a0 | -3.12232 | -45.89913 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f67f301-6700-3fdc-b9c5-b30790af0dce | -3.46257 | -44.53966 | 2024-11-17 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91377f02-b983-3846-baee-002b1df86286 | -4.22481 | -50.67485 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85be0226-1454-38a3-9f9d-c61c4e9bf96a | -2.30087 | -49.13354 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71f338a9-887e-3345-9704-a9521ae95407 | -1.99145 | -48.52449 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db36151d-44cd-3329-bce2-5e72727b40f7 | -4.23568 | -41.93106 | 2024-11-17 04:29:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 428ef924-7ea9-349f-8730-ffdf21800156 | -3.81314 | -51.38291 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc3bbf9-ab91-3467-88e9-1a08964a1d6c | -4.43659 | -50.54367 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8e3a240-3116-30da-9c5f-41dda98d1567 | -2.18752 | -48.38878 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af89e1b9-1609-368c-b4bd-5201d581eec3 | -0.9023 | -51.72831 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 459dee29-d6c8-31d4-af02-cd9eba9e53a4 | -1.83434 | -46.59527 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3e9e870-4796-3dac-8b2e-5459a7df951b | -4.55699 | -43.20605 | 2024-11-17 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b6c1d94-88a1-32b0-9519-6797c9a2e6f1 | -3.9181 | -46.52103 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1a3635b-7929-3859-ac95-54005de78a05 | -4.10164 | -46.10411 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c66e45a1-a7bc-3bbb-a411-1853d2031a8f | -3.67339 | -50.10309 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfab36ac-499f-348e-a7f7-5372c92444e6 | -2.11183 | -48.29979 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b4f3e47-9c56-3b70-aec4-e94ab0cc9a61 | -2.11578 | -46.42464 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977a10d2-bd2c-3660-b002-f02a836c5f0f | -4.47026 | -45.6639 | 2024-11-17 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c121d3e3-d919-391d-b626-6643e2359fcd | -3.79498 | -46.02449 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fd437ab-d876-3081-99a7-74da3fcd98b1 | -2.16871 | -48.77681 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ae7edc-dc90-363d-a68a-6a3199736907 | -1.13401 | -51.68412 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18f8c12b-5751-36c4-8079-a1e6af9a720f | -1.815 | -45.56822 | 2024-11-17 04:29:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e750d7d-d139-3966-bef0-045290e2b204 | -3.09176 | -51.31326 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7533e2f4-1a27-34c9-8318-32a6f89367b0 | -2.58415 | -47.57231 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b2c880f-dfad-35ec-ac70-def9eb9c205a | -0.4058 | -51.62771 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
