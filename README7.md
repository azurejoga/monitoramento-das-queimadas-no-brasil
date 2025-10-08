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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6945ffdc-0e7d-3444-9296-df79d7d7e4f4 | -11.29784 | -54.88572 | 2025-10-08 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 736587be-239a-3207-9e70-9bf770dee0b4 | -10.76065 | -52.77788 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f4045fb-077f-316f-8eb1-b032fff965d7 | -8.5157 | -46.28976 | 2025-10-08 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 59c082f3-123a-3c18-9bbc-7e620b0103ff | -9.89141 | -57.82703 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1607d6d0-a2bb-36f1-b7e6-9bf326078202 | -9.08289 | -47.95699 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7e4ba02b-1d97-3431-8e46-6bfae9b2f0ce | -10.41932 | -48.0935 | 2025-10-08 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8acf4119-c30b-3793-9840-ea633fde6015 | -11.99551 | -46.77171 | 2025-10-08 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7918bbe7-b5c5-3317-8375-516c13ef292c | -7.82135 | -46.72232 | 2025-10-08 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a1d7d357-90ce-3f1f-8b63-0c8a379cdad4 | -10.43119 | -51.62998 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dae884c0-73e2-31d6-aa3f-dff56adacc17 | -10.88816 | -51.03124 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a40922db-35c1-3b72-b49b-c833c44f9207 | -11.18116 | -54.90427 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 810c8847-8b92-3e1e-8311-edff23cc9a25 | -11.14094 | -54.88071 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 4574fb2b-5632-3f2b-91e1-6eadf8202b43 | -12.38852 | -51.13517 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ed397ffc-236a-34d7-b46d-26c385936280 | -9.63674 | -55.12707 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5f83b37c-338b-369d-9632-91db4913f19d | -11.68044 | -50.96883 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 14591e3a-46d0-33d8-994c-fc8bc4fa590b | -11.18471 | -49.78238 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cc71eacf-4f4c-32f1-ae61-3ce065190b1a | -10.89759 | -51.02978 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9325381a-3eda-3b9d-8e1e-4eef8e06c940 | -9.13363 | -50.05202 | 2025-10-08 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| caa3d247-ef6f-3e88-b0d1-e74ea2dd1dff | -12.3907 | -50.29665 | 2025-10-08 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1dba207d-9fb5-351f-928c-012d5b9cdb5b | -14.62625 | -52.48051 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9f96a44c-a3b1-3c6b-8c9b-35708367dfd7 | -10.23901 | -53.92596 | 2025-10-08 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| caf48536-1af8-3c2f-acfe-b6e1ccc992a8 | -11.6159 | -55.69277 | 2025-10-08 00:52:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b723aa3a-290f-39a7-9be2-2fbd7b09008c | -9.39169 | -59.42586 | 2025-10-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e722818c-935c-3030-9f46-7c4cd92cb0fd | -11.45221 | -50.20597 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8a6083ba-f7d2-3847-b7f3-178165c12773 | -14.71534 | -48.4208 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ddf34494-52c3-3ed3-bac4-362c6a45e843 | -9.18847 | -47.80505 | 2025-10-08 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 1897ac6b-b59a-3a23-b809-d607aaef009e | -8.4871 | -54.66869 | 2025-10-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00e942a7-93a1-3785-97a6-79c14b09bc72 | -12.18074 | -50.97508 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 28ab3ac8-512f-3818-af72-29a474d62c91 | -10.91645 | -51.02687 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8cf45713-e395-3c05-8893-e2001cb319ca | -10.94135 | -51.02722 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 049bce4d-c43d-322d-8dfc-d6d1363f1706 | -8.44886 | -54.71999 | 2025-10-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 836fec59-f09e-38b0-b538-4da6788a45e4 | -11.44404 | -50.21881 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| addc23b8-62e0-3f94-8466-2625d2bf7673 | -11.17857 | -54.88511 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 312.3 |
| c30aa7c1-4f3b-33db-a40d-69164b225d2d | -15.05766 | -57.18748 | 2025-10-08 00:52:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a41276fe-7d7f-307a-9637-19d5a43642d2 | -9.09784 | -47.97286 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 351120b0-df23-312c-8d39-31ab6646f290 | -11.13312 | -54.8915 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ba0c762a-4908-3cbf-8d8c-f11c6542b93c | -9.79735 | -47.73752 | 2025-10-08 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8ec441c9-9aff-388d-af1d-d2885fe24f2b | -7.7939 | -46.72656 | 2025-10-08 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 6724d7f0-e595-3eb0-b179-24fb90a13ed4 | -11.45386 | -50.21725 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 88b535ed-95fb-3848-8a31-fdd74e1efa64 | -13.22558 | -47.19839 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 733a1148-91c9-3527-a8fd-07d84e1db600 | -11.34804 | -44.89124 | 2025-10-08 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| cbea1345-52c4-3383-9ac1-225c137b6102 | -9.17988 | -46.91727 | 2025-10-08 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c296bc17-5bdc-3393-87ff-08d4d815a8ad | -7.80763 | -46.72447 | 2025-10-08 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0af611c1-1756-3e45-9a96-d64052b07398 | -13.81369 | -45.83311 | 2025-10-08 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8d541a3a-f0bb-3afa-81a5-16e0be1bafa5 | -14.69421 | -48.42411 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dac42fad-2608-3d82-bede-4421db6e2003 | -13.81341 | -45.81729 | 2025-10-08 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5ad3972e-8406-32c6-b34a-9fdc26db4e85 | -9.4531 | -56.65346 | 2025-10-08 00:52:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 17d73e00-ba46-384c-981f-cefc09f7a9fd | -11.45633 | -50.22247 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2b1201b3-2148-352a-a8e8-012a384ac21b | -11.11944 | -54.03862 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| f1ad4f1f-cce1-387a-978d-a33729fda56c | -9.67071 | -49.94398 | 2025-10-08 00:52:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 04036955-5b31-3230-b53f-28892fbd2d4b | -14.38604 | -46.02133 | 2025-10-08 00:52:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 72257106-fd7e-306d-9e7a-c6ea75aebfef | -13.2877 | -47.16305 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 06c17ff4-69ce-3734-9564-024146ed7d6e | -1.09743 | -53.69261 | 2025-10-08 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 45de47cd-cee1-35ed-ae68-711fafa9c4ac | -3.25792 | -50.12655 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2189d652-9d67-3e7e-80a6-3f937ce06ebf | -5.82188 | -46.75775 | 2025-10-08 00:54:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7040edac-a329-3eda-bb72-8e2e85420f28 | -3.38747 | -50.14753 | 2025-10-08 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 09297368-1e92-3155-8563-e8e423b4153c | -4.72995 | -45.82065 | 2025-10-08 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 694121ab-4935-3c6e-800a-d705885ee4a2 | -8.1532 | -54.84404 | 2025-10-08 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7df542fe-5e86-35f5-be90-6b19eb2047db | 0.93412 | -51.12014 | 2025-10-08 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d811516e-a68f-3c78-a8d7-2ba967c3c2b7 | -3.46114 | -50.09991 | 2025-10-08 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f5277b59-0e68-3443-bdc4-4c544d11172e | 0.93203 | -51.13485 | 2025-10-08 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 94c18360-dc33-3953-acbe-e0361b44f725 | 0.93386 | -51.12584 | 2025-10-08 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ca08aab2-a4cd-3eb3-a9a9-33c4b1c7a355 | -4.40162 | -49.77033 | 2025-10-08 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 97830c81-8e89-342a-a1eb-40c96247f6be | 0.93189 | -51.14059 | 2025-10-08 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| eb933d5e-eed1-3042-a726-3cf27e6e9d6f | -3.78611 | -49.42604 | 2025-10-08 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 998dcb37-3791-3a2e-8f07-f0cdaf8d440b | -5.12663 | -44.96572 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 0da477a3-b31d-3270-8df0-d176bbf63422 | -4.68329 | -45.82813 | 2025-10-08 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a9bb55a1-c324-3c9b-9755-1cd049592c74 | -4.85496 | -45.75631 | 2025-10-08 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 79f028f0-4fca-35a1-b341-ccf4ee80089b | -3.9251 | -53.4744 | 2025-10-08 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6a47034e-c142-3a4f-9fde-a26acc7ecd78 | -5.18041 | -45.14404 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e65621af-1b1d-3b90-9cb3-5144067c6b2c | -4.5088 | -46.36016 | 2025-10-08 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c32bceb8-e160-3a2c-bb3c-e36822418350 | -1.87396 | -55.16475 | 2025-10-08 00:54:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bbf0ccbd-94db-3764-9385-a21852422390 | -6.41809 | -47.2328 | 2025-10-08 00:54:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 7306d657-07e1-3d6c-a893-bfd4559cd392 | -4.92509 | -48.54495 | 2025-10-08 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a6fe410f-db90-3be6-a7ca-0763a0a067f6 | -3.57327 | -49.44141 | 2025-10-08 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 93d96073-835a-3266-9e6b-59f7384bb184 | -2.47553 | -54.05461 | 2025-10-08 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83e7dce8-c13b-3d19-8f02-bb9d86404c1b | -4.69286 | -45.86246 | 2025-10-08 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 02349b85-984f-3e8e-9182-8c961f7307fb | -3.08221 | -50.58361 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a8833c74-9dd0-3ccc-b504-a00104db467d | -4.25757 | -48.55347 | 2025-10-08 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 32906f78-58a4-31e1-b6ef-111697e5dc4a | -4.68806 | -45.85794 | 2025-10-08 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e4bdb9a3-d634-342e-b179-413eb53aef6b | -3.79411 | -49.44756 | 2025-10-08 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9172920c-bf7f-3ccc-8734-6c8620b8d4ea | -5.40344 | -46.22251 | 2025-10-08 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8b52c045-d2ae-321c-9aa6-243252c312bb | -4.49375 | -46.36206 | 2025-10-08 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 10fff7fe-3350-30b2-9159-7bee66984b7e | -5.13711 | -44.96926 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 528.0 |
| 129f0a6d-99ef-3338-a659-1c78cb9ae7d2 | -4.13791 | -47.65491 | 2025-10-08 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f27d8936-e424-34e0-aa45-8ef365bd80a9 | -3.23234 | -46.79514 | 2025-10-08 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| d559ba2e-8ff3-36ff-8d84-d727f2374b61 | -3.11006 | -47.80598 | 2025-10-08 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7cac659e-ff5c-3dff-8924-4da6b785bf6e | -2.88491 | -50.72333 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| d4e9cd4d-8a31-3969-a5e3-d3f16d1d21bf | -3.09315 | -50.58206 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c811f1ed-c4c8-3901-9cd5-3978f4e62884 | -2.88691 | -50.73703 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a9848252-e05a-3395-9a7d-49facfed81ba | -2.51715 | -51.93216 | 2025-10-08 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 90f2de98-9590-34a6-9d77-8770f29fe829 | -3.79175 | -49.43085 | 2025-10-08 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 359c6b5d-74be-39ee-8855-2fa8254ca6bb | -5.81798 | -46.73252 | 2025-10-08 00:54:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e15de8eb-b2e6-330d-a09f-7ecd3fde5910 | -4.49505 | -46.36826 | 2025-10-08 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 68fdc183-bb29-3b43-88e1-ecb6f36ab37b | -3.26922 | -50.12491 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f69b927c-f95e-38c4-983d-f5711da7ccb7 | -3.73294 | -50.4737 | 2025-10-08 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6029fa39-80c8-3235-92b8-bb7e8cb8f8f4 | -3.78862 | -49.44278 | 2025-10-08 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bbf49f19-75e7-3329-846f-b5869848c925 | -3.21884 | -49.36217 | 2025-10-08 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 821a6733-34b8-30e2-aac4-f009b07a6dbb | -4.09115 | -48.04852 | 2025-10-08 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 73aa08b6-6381-38cf-9b10-8699c1e26a75 | -3.24679 | -46.78756 | 2025-10-08 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |


[Clique aqui para ver as próximas entradas](README8.md)
