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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffbf3d23-750f-38fb-9df4-87460166f72b | -9.9692 | -45.3565 | 2026-09-28 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 495.4 |
| faf47caf-0f5d-3323-a55d-e775e3e1c71b | -11.0241 | -49.7088 | 2026-09-28 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1d7fca04-85d1-3f2f-ba1a-b293b4702de1 | -10.8532 | -54.0916 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9ce73f60-f721-3e26-9fd0-3422c56c8f8b | -11.0991 | -54.0285 | 2026-09-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| a1548d61-8130-30b0-bffa-9df24e84a740 | -11.5352 | -47.3678 | 2026-09-28 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 87859cf1-ec8e-300b-a4cb-0ae28928137c | -11.4173 | -51.3948 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 7112f20f-44e3-30c4-92df-1d522a4aba1e | -7.4869 | -44.5751 | 2026-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8b521112-6dbd-356f-87b7-4eda7e5cc6ec | -13.6866 | -56.6131 | 2026-09-28 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c974abbb-d18d-331c-946c-bb5856dbcd43 | -6.1599 | -52.8929 | 2026-09-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0657f9f4-f377-34ac-9141-1b185ebfed22 | -8.6171 | -54.6126 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 201b4b67-3f09-309a-a06c-720cdabd5982 | -10.207 | -49.9684 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 23efb088-e285-31b0-96cb-8f37e2157aef | -12.2311 | -50.3643 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e444e7d5-cfe1-39cf-bbc7-631d9353d4a3 | -6.3489 | -45.7848 | 2026-09-28 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3d0eca30-afd2-3112-aaf9-88070ece7ea4 | -12.3088 | -50.2688 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 48c99c96-7245-3ea3-8f9d-fea7701247a8 | -7.5057 | -44.5733 | 2026-09-28 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 8957732a-72cc-3ff5-8688-918ce86d47ed | -10.1095 | -50.2135 | 2026-09-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6a86b164-b452-3e7c-9571-71afbaa60efa | -10.4234 | -53.8014 | 2026-09-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7d6b0c90-fc37-330e-ab5a-649e67bccfca | -10.7114 | -60.7505 | 2026-09-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 29a26ed7-8b76-353f-800e-6f322980292b | -8.6451 | -45.3489 | 2026-09-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 75106223-f269-34f6-ab33-cda31ca1951a | -11.0761 | -51.4097 | 2026-09-28 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b4498b8e-4ebd-3e58-8c86-340653ef2492 | -12.206 | -50.7531 | 2026-09-28 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 03710cc5-dafc-35cb-8042-bd7d927730a7 | -12.8061 | -54.0048 | 2026-09-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 6b224a78-d9ec-3b52-9b98-9c04fb210a4d | -9.9266 | -60.7171 | 2026-09-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ee0bc619-5e09-3be2-a8b1-2d7eae9a0f1d | -13.4325 | -57.061 | 2026-09-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fe0a6402-0856-3e81-865b-73c8b42f08a3 | -9.7874 | -44.8289 | 2026-09-28 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| d162e2cc-18b7-37ef-ac3b-0565cf27bbd2 | -8.2807 | -54.7158 | 2026-09-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 715942a3-a295-3d96-bce4-726a89fccc74 | -11.5815 | -50.5261 | 2026-09-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9cec7003-1128-365c-9559-103aea9a8472 | -15.4003 | -47.9035 | 2026-09-28 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3848539b-962e-3d20-9785-bd55894ae4b3 | -11.6793 | -44.5246 | 2026-09-28 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ef5aeea5-fe1a-32d4-9817-5cfb74488a94 | -10.2565 | -50.5185 | 2026-09-28 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| a71de305-ba18-36e9-a30e-84feda74b64d | -10.4043 | -53.8236 | 2026-09-28 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 72cc5047-c7e6-3fcd-93f4-6b3f2e5881c9 | -13.3436 | -51.3401 | 2026-09-28 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c7c89563-35d5-33cc-92af-66fd4f8fdb73 | -11.1183 | -54.0062 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1560a53c-b491-31a4-b8aa-1d6653668a1e | -9.4813 | -46.3646 | 2026-09-28 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 9ac733ea-0c55-31ac-9148-181e357e99f8 | -10.8001 | -57.2007 | 2026-09-28 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5017a98c-6849-3a3d-a464-26340c8dae0e | -12.6878 | -45.0192 | 2026-09-28 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 99b47756-fb39-3705-ac3c-e5b0cc3ff780 | -10.7726 | -48.7399 | 2026-09-28 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e980cb63-2f37-3250-86a3-ea54c3039dbf | -10.8375 | -57.2178 | 2026-09-28 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dfaeedff-711f-36d5-805f-1fa933922835 | -8.3608 | -45.4695 | 2026-09-28 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c09f23f5-9927-3214-a907-087bea6ac68a | -11.0235 | -54.0354 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 11e8a375-7854-39ff-9686-c87cd3bdb6d7 | 1.2613 | -50.6845 | 2026-09-28 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 26fdc1cf-7fe9-3aaf-b9c4-d2d477af9752 | -9.9976 | -50.1179 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| bc4a3670-5fdc-3efe-b9b1-57b370424866 | -12.3085 | -50.2904 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 92e5973b-f674-3af1-92f2-1e9bce058df7 | -10.7677 | -60.7279 | 2026-09-28 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 953ffe4a-245e-3e05-8f61-ccc9ed4eeb65 | -16.6424 | -48.4724 | 2026-09-28 14:50:00 | GOES-19 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0291398e-e844-335c-a0ae-4684706a5dfc | -10.4229 | -53.8424 | 2026-09-28 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 856359af-63ca-30e5-b4a5-5dab470a1201 | -11.2158 | -44.7778 | 2026-09-28 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 529fad46-ac31-38a3-94e5-532662d10130 | -7.449 | -44.6016 | 2026-09-28 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c340719d-7aa9-3b53-a4fe-698e5fd99cd9 | -15.3998 | -47.9261 | 2026-09-28 14:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| ed4f4b1b-c492-3260-9b3e-32585b289e5d | -10.7916 | -48.7377 | 2026-09-28 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 431c3f8c-6709-3290-a70b-e3776338790e | -11.5815 | -50.5261 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ab207d73-5098-31f4-adbd-b620bb9f22e9 | -11.9244 | -50.4866 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 460007e2-1b1d-307a-8799-93f88a4ab6ee | -12.1869 | -50.7553 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d0658ff7-f1c5-34b2-b897-87589c1a7f05 | -10.4046 | -53.803 | 2026-09-28 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1bb28495-2a2a-3083-b700-3b6709afd205 | -12.2248 | -50.7722 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3765d0d7-3303-311e-927d-9917bfe3a3de | -7.4869 | -44.5751 | 2026-09-28 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6906babc-3ec2-336f-a75d-d81bd5ce2e60 | 0.3035 | -51.4389 | 2026-09-28 14:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d84ef8e7-cd5d-37fe-9c20-cabca979becb | -10.2254 | -50.0093 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 22cfbb31-36f5-3355-902c-2cae40c74fef | -11.3739 | -43.3972 | 2026-09-28 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| d7d71b12-c3c3-3642-a57b-2c7ba1193fde | -12.206 | -50.7531 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| ec577e75-1daf-3541-8c15-e39d72af566a | -9.206 | -45.7642 | 2026-09-28 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 201d72c4-0c1f-3c60-ac03-f4437ec80a72 | -10.8185 | -57.2391 | 2026-09-28 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 46281f30-92c5-3ffb-a980-4e77862d88fc | -11.9593 | -50.6965 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a1e3a5a5-8d5c-3443-a614-f46c0f5203d4 | -12.2063 | -50.7316 | 2026-09-28 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0bee8c36-9656-3b14-b95e-25b8fcb4ccc6 | -9.4999 | -46.385 | 2026-09-28 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| f125b71c-fad3-346b-af3a-07ca85b1cadf | -8.5984 | -54.6139 | 2026-09-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cdb1e99f-14cf-3ec1-aece-ba886549ee90 | -10.2565 | -50.5185 | 2026-09-28 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 123a3817-58cd-3c41-9fee-a92de655f1b9 | -10.7115 | -60.7312 | 2026-09-28 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| fae27f49-1570-3b51-8f41-10ce043397cf | -7.4974 | -55.0256 | 2026-09-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 864e5673-dbaf-3124-bbb8-9e06fc33183d | -12.6263 | -47.3075 | 2026-09-28 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| dae91c82-1121-3935-bd1e-60163b6dc7a2 | -11.7831 | -51.0365 | 2026-09-28 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 25a42223-f54f-3263-8695-b1c5c35c955a | -11.8672 | -50.4933 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 29861caf-3bbc-39ec-aeaa-d6c5b693b575 | -10.2065 | -50.0113 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 99cec4a1-8f22-3c7f-94b4-2e82e641d320 | -11.0422 | -54.0542 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8cd146e1-f908-39f2-952e-6574735d3ef1 | -10.2446 | -49.986 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c1b7673c-0efd-3dc9-993f-5c1339d3222c | -11.8478 | -50.517 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a3dd3c23-114a-3e08-a0f4-c93df89df863 | -10.1284 | -50.2116 | 2026-09-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 8a36de9e-8ff9-3817-8c17-8fabc112f77b | -8.2291 | -45.4602 | 2026-09-28 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 5cd24f52-4b65-3aed-9819-64e0095b338f | -13.6866 | -56.6131 | 2026-09-28 14:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 9a350d35-fa7f-3c33-b1a2-f9af143183b4 | -11.7122 | -50.6822 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b167f10e-8bbf-30fc-a9de-519985760207 | -11.6941 | -50.6202 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 15cbc449-f1bd-3445-8c70-b9e12d2f7e90 | -11.924 | -50.5081 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| bbb68193-fde3-3c66-a6e4-92f03cfd7cea | -7.7086 | -44.92 | 2026-09-28 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5142a5a7-954f-377b-a960-ee950544ad39 | -11.809 | -50.5642 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3ab76ac5-32cc-328f-8b8d-7ffbe2f5a9ee | -9.0838 | -61.4499 | 2026-09-28 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2b07a39d-23d9-3cce-8a83-9ed6a618d748 | -12.4351 | -44.1497 | 2026-09-28 14:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 235.0 |
| fa61c642-a8ae-32c7-ac41-fcc096151d4b | -10.4237 | -53.7809 | 2026-09-28 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4ecc49f1-6439-38df-b011-f90588c4a118 | -8.5982 | -54.6341 | 2026-09-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 75949974-deae-3327-8cf4-5470afeaf057 | -15.1847 | -46.141 | 2026-09-28 14:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 62e56589-8f0e-3d37-be98-d42f833338dc | -10.6094 | -53.9902 | 2026-09-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ec761daf-3d9e-3206-b193-b8b2e3deb9d5 | -15.0984 | -54.7189 | 2026-09-28 14:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| def5eeb5-8649-342c-ac7d-f222768a3131 | -10.8187 | -57.2192 | 2026-09-28 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c50af7a1-f7bb-3268-a96f-d3fb44897705 | -10.7064 | -44.4317 | 2026-09-28 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3b787eed-1254-3d50-9f6c-e93eeaefc07c | -11.5161 | -47.3703 | 2026-09-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 5079ca40-e68d-339b-98b4-230c97396d42 | -17.2931 | -44.5157 | 2026-09-28 14:50:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 8d28721b-c943-36bc-aef6-21cb4bf857b5 | -8.6451 | -45.3489 | 2026-09-28 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| dbb14c6b-15da-32e5-bcdd-313fb90b97de | -10.8191 | -57.1795 | 2026-09-28 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7adc88ca-92c2-3d46-b853-cad94a8bbf43 | -9.7874 | -44.8289 | 2026-09-28 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 9458ae86-131a-33ea-b2d9-06546f70da0b | -11.0764 | -51.3885 | 2026-09-28 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| dc68b3ae-0089-3dff-8d2f-dcc7fbeb5ea8 | -13.1803 | -48.5409 | 2026-09-28 14:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |


[Clique aqui para ver as próximas entradas](README82.md)
