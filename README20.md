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
| c54d919b-5fd3-30c9-ab3a-2853e7b6db9f | -5.97571 | -43.93605 | 2025-10-09 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e80ba29a-34fe-390e-8cae-a8231da9c9ca | -6.72744 | -42.85936 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 47425c8f-687b-3a7a-9d4a-ef5593e50d45 | -8.53325 | -46.2146 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| eef20ee2-3017-3e75-acbb-fed68a4be218 | -8.61731 | -45.12226 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5859a1d-8149-36fd-bebc-eda5cd51bcc7 | -6.65642 | -41.99416 | 2025-10-09 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 28d9f1bc-dcbd-3739-884c-6dd3acd085a5 | -8.62395 | -45.13446 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b6fe84-ef5c-358f-bf41-36d6b3f6b9fc | -6.45718 | -44.5744 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d27470b4-f873-3f6a-b4c3-4ca73aa23093 | -9.19306 | -43.12252 | 2025-10-09 03:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f73ddbeb-7b35-3d0b-a2f6-d823c23c5a9d | -8.17187 | -43.32369 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ce06d766-5b87-39bf-bb77-53866e54699b | -5.33281 | -45.51183 | 2025-10-09 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 324c19df-3c27-3158-998e-31e9c1605298 | -7.63576 | -45.23567 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d887139c-1fba-3fbb-97d3-a87980a22c68 | -7.52814 | -42.98188 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 699ae995-93ed-3655-8daa-467b3db8989d | -5.8052 | -44.6792 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a1ff1dd7-2159-3a65-8547-4416d03c08f3 | -5.4007 | -40.99529 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 33506210-d2b3-3795-b242-5643e3d1942f | -6.46189 | -44.5796 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6ef038-555b-306f-aa79-f0f77b545c6e | -3.30201 | -42.0951 | 2025-10-09 03:57:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daf9fb93-eaa5-3968-8d1d-b096b44f107e | -9.22297 | -47.85199 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 768cca65-10e7-3534-bd42-e682a2bfef63 | -8.19808 | -43.35871 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aa5af47e-93ae-374a-af4b-167bf9238b6f | -6.32203 | -37.62644 | 2025-10-09 03:57:00 | NPP-375D | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa4e70bb-d818-35ce-985a-62b038ced21d | -6.68628 | -46.3021 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 86e4fcb1-c1e1-31f1-ab7c-2fa1999575a1 | -6.74466 | -42.82722 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f03315f7-2bb7-30ee-a090-a9a12f48b467 | -7.45624 | -43.02816 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29eb4b72-0130-3a8b-9099-7dda6e94dd06 | -3.39031 | -50.14555 | 2025-10-09 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07c685d3-135a-33fc-b1b0-1874f6940381 | -8.60637 | -45.10744 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf3e888b-9248-3fd7-93a4-9e22dbe38e7a | -10.09319 | -40.89212 | 2025-10-09 03:57:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 06a7502e-fe7e-3688-82cd-130565f7c2ae | -7.29426 | -41.97052 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dba280c8-d32a-3494-a2dd-078a06ebb6d1 | -7.48568 | -43.11506 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e55bddc-bdf8-3ef7-842b-94025b3ae510 | -8.72073 | -47.10204 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5dee86b-f614-3046-b7e9-3c52395ece8e | -8.49584 | -46.22649 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| afe1bf9a-d569-343f-97ad-90c31b655112 | -7.66914 | -42.57949 | 2025-10-09 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 12118c09-02a1-3b3d-9914-48d080251520 | -7.1444 | -42.1804 | 2025-10-09 03:57:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d747c34-7c4c-3cf6-a8ca-a66cd3ea1fe3 | -2.37823 | -47.70969 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55642dd7-64da-3293-94e3-7cc2eb7908b7 | -7.4019 | -42.1008 | 2025-10-09 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d5141ed-88b7-3d5a-9025-8b6279e7d04d | -3.30229 | -42.09337 | 2025-10-09 03:57:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b34af4c-d5ef-38e2-98e7-3b93080dbc30 | -4.01091 | -43.28388 | 2025-10-09 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddcd05fe-14e7-3a52-b30c-d5175e85a2c1 | -7.01541 | -42.74678 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 14ee3f95-a314-34ca-afde-485e9fee2e40 | -7.43193 | -44.56239 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbf31d80-dc13-3abb-b866-5bb220bd288d | -7.99319 | -44.47124 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 451cfec2-fc97-3dfe-a2d1-e1d3a1f23d58 | -7.66836 | -42.5841 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 07fcbb2e-33ee-3bd3-9b1e-a81c53b799cc | -3.58581 | -49.35268 | 2025-10-09 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25582591-fa5d-376d-855f-5bcbd6bfd506 | -7.73625 | -42.40946 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 481fd37c-6453-3a32-a53e-9d7fc906fa06 | -6.28196 | -44.30316 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a780a25-1ab9-3b8b-bc90-be6bc2621530 | -6.42027 | -47.22707 | 2025-10-09 03:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b1adb3-bb03-3152-8b77-efb78d3b91d2 | -6.4568 | -44.58307 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c01e975-af84-3f21-afbd-f15dd33c75db | -9.09133 | -47.95558 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8808d153-ca1a-3ff9-9058-900e6313ed8e | -3.10463 | -47.79899 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d9eee0d-6967-3ada-9664-b5ef07733b1f | -4.84473 | -42.76707 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9c0cdfe8-9404-391d-8f0f-41102a8d33d2 | -6.51059 | -44.14633 | 2025-10-09 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e15dc601-d1b5-3b5b-9109-7a06c9a3f9bd | -7.29792 | -41.97115 | 2025-10-09 03:57:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80a54ce0-52a7-3a23-8196-7b7d35fa837c | -5.74039 | -47.46847 | 2025-10-09 03:57:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62640b5f-b524-3233-b648-a0a391a138c0 | -5.48528 | -42.88943 | 2025-10-09 03:57:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f749242-b672-3915-99c6-6c70187f6655 | -4.84076 | -42.76639 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 35b28f72-b091-3dea-923e-2a5485ee0850 | -2.37719 | -47.7158 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4f551c8-c56e-3310-b4da-1c340ddbd4e9 | -8.13047 | -47.24916 | 2025-10-09 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2dc2aba-21ac-3ecb-86e9-1445be7ca82d | -3.74186 | -39.95473 | 2025-10-09 03:57:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38cb8faf-afd0-3042-90f9-4f65d983edaa | -5.1351 | -37.55966 | 2025-10-09 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 464d50f9-9640-3bee-bc89-67e1a803fb44 | -7.03423 | -41.96252 | 2025-10-09 03:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 75ecc1a1-5332-3c52-b124-04aa28550a1b | -8.18339 | -43.32856 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fae4eade-7dd2-39c2-bf7c-eae0f82039c1 | -2.3833 | -47.71476 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcc68058-4372-372b-a34f-aec546e0fefa | -7.15993 | -39.43243 | 2025-10-09 03:57:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26c2896c-6655-37b1-8935-7284d76b7321 | -7.20298 | -45.49321 | 2025-10-09 03:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 034453c4-f6b3-3389-a420-232ddd9b22c9 | -8.19447 | -43.33271 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 24320ce7-101d-39c6-97e1-e8f203a9ba60 | -4.72307 | -42.94696 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ac71ea1-c0f8-3060-b1ca-7e1f58ee1a25 | -9.22219 | -47.85639 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31e89eba-d8f6-3323-8b34-ef740f0549ba | -7.4609 | -43.0257 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ff9d55ee-e67a-31dd-8e34-c327408a5db0 | -8.53894 | -46.20999 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| a625ebfb-a24d-3e41-af60-c58dee93c980 | -4.84785 | -42.77287 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 06f47598-a532-32b0-9bd5-33c7cf8660a3 | -7.77575 | -42.40242 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f72f8d24-58a0-3459-877f-723451a1d4e0 | -4.51192 | -38.82522 | 2025-10-09 03:57:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dce5d49-5589-32f7-8b36-ff62150a0dc4 | -10.19622 | -44.563 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5823f97-c7a0-3ce7-bea5-a0acf420c22e | -8.51558 | -46.22475 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 046bb411-1a6f-336b-8537-5fa4514703e9 | -8.6757 | -43.91926 | 2025-10-09 03:57:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e012c1d-09a6-3de9-b781-a452b1fa2a5b | -7.36514 | -47.05196 | 2025-10-09 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d5475e0-2ce6-3b9c-8937-ad82ba3d0b31 | -9.97132 | -46.31897 | 2025-10-09 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eadb17f-a56b-342c-896a-5b7dcc8314a6 | -5.71827 | -44.82453 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290a6db5-b098-3b98-b7c1-370e7fc9dff0 | -8.54746 | -46.21657 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bd8c29f-5346-3beb-a874-4d5337be5f32 | -8.19363 | -43.33762 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 00a8c014-74a2-3a3e-980e-6a35f50f9d82 | -5.84647 | -44.35451 | 2025-10-09 03:57:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e92392cc-3947-3e77-a4d3-a5c57715835c | -7.2906 | -41.96989 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9f738c5-db00-329f-89c3-3e189a2bf44e | -8.54658 | -46.22144 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de082598-9cfc-3f38-8b90-d97dc2a2ddeb | -5.97992 | -43.93676 | 2025-10-09 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5acc02bb-3ba0-31fe-bdf1-a8688f52daff | -9.78657 | -47.75031 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ed34950-e19f-309b-b384-fcf9de5c8358 | -9.09656 | -47.9566 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b33e9158-1517-3a7a-822c-45a1fbca43d9 | -6.79559 | -50.48748 | 2025-10-09 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fa4d927-1ab4-317e-b250-2f70bec74bf7 | -5.40201 | -40.98713 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c812f34-ed2b-3b7c-a609-f877195468b3 | -5.2056 | -37.62778 | 2025-10-09 03:57:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 67721f54-bd23-385e-bad3-a4affde30e90 | -7.77691 | -44.0426 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a28f722f-91d1-3063-b0b5-fda6e10b0cd3 | -3.09894 | -47.01623 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 112c4493-691d-330a-b821-315a41b7d489 | -7.77276 | -42.39733 | 2025-10-09 03:57:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b663dd6-c46a-3294-934a-5f325f55e323 | -7.77343 | -44.03819 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e82d13f5-75dd-360d-b57f-ac835ab4fd2e | -7.41623 | -42.98106 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d0cc412-03a0-3d4e-aac7-81f1638c43f6 | -7.70642 | -42.38158 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b1b8e86-d8ec-3f0b-b958-a135cae09f12 | -7.78102 | -42.41703 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b50c4fbb-c43d-3261-b59d-1455d564e431 | -7.99307 | -43.89704 | 2025-10-09 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91ca27d8-b2f0-364b-8ae5-ac647857f731 | -4.33932 | -49.8893 | 2025-10-09 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9bf1983-5526-3ea4-837e-729d0eed9d68 | -8.73411 | -41.66011 | 2025-10-09 03:57:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9f7ab4cf-e78e-3276-aa57-3f6fdb53ff68 | -7.76105 | -44.03622 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6c284421-cbc0-39de-9547-880a207d8253 | -6.27769 | -44.30227 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57daf194-f3a4-3f52-bec3-d59e1bd0e7d9 | -5.2393 | -45.39608 | 2025-10-09 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69c71c16-c015-3e95-ad44-7e01affe1ec9 | -8.15441 | -43.33337 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
