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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af193755-8ec1-359a-ad24-c285afe6064f | -7.45982 | -49.74078 | 2026-06-05 04:42:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d589a7a4-7c3b-3b09-ae9b-ea11f5ee4a14 | -7.95647 | -46.84423 | 2026-06-05 04:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3955de42-d279-31e0-acb2-385764094de2 | -8.15246 | -47.43716 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12d0755a-f1ba-3aa7-8ce1-0d88b4b43e09 | -7.3556 | -49.82001 | 2026-06-05 04:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dae4a9b-c294-3812-b0ec-a669ea8c5517 | -8.24652 | -47.10091 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6daf8fa0-f791-31ff-8225-320033727ebf | -7.34348 | -49.83228 | 2026-06-05 04:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b003f2e-52ef-3a48-a41c-9d4340f51966 | -8.98004 | -47.9813 | 2026-06-05 04:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 313a2004-262c-3ad8-a1c0-31b6cb827372 | -7.34734 | -49.82934 | 2026-06-05 04:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12674a12-7b37-34b4-84a9-b187ef3afd90 | -8.05351 | -50.68311 | 2026-06-05 04:42:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b3277c4-477f-3b60-a759-81248d451968 | -8.35282 | -46.79855 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 104afdff-51b5-309d-9858-76e91cad0526 | -8.72779 | -47.98174 | 2026-06-05 04:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ecca759-945b-3211-b2be-a4e62e50a600 | -7.92085 | -46.18733 | 2026-06-05 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 788d3e77-b1d1-3ec9-a6c9-331e702db3b9 | -8.36719 | -46.80078 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94d46eb3-a320-3fe0-84c3-67b4e77bb72b | -8.40918 | -46.88743 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5de283c-4976-3df4-b7b7-b0b75f46aa31 | -8.24591 | -47.10489 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15a8466a-575b-33d7-bd30-2d5221382a2b | -9.28388 | -46.51208 | 2026-06-05 04:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8c88dde-cc60-3788-99eb-bc40ae29ffb2 | -8.37139 | -46.79731 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e03a90cd-fc7b-3c07-a950-ee62b0797f5a | -8.03354 | -46.97969 | 2026-06-05 04:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d64d879c-77a6-3598-9be1-1f10f4e57f8d | -8.39597 | -46.90204 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c146ac22-ac2b-3022-aef1-4893e5d6cfbc | -8.24236 | -47.10442 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ed96c2f-1ce2-3c78-a4a3-fc01447fedd1 | -7.35229 | -49.81948 | 2026-06-05 04:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b403e4dc-e385-3c9e-a4aa-330f5028fda4 | -8.05759 | -46.79614 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8079cd4c-2c46-3b14-82cf-a84eb947f3f0 | -8.76656 | -48.43755 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acc85de2-cf8d-3cbe-906e-70a75e1ae8b0 | -6.45567 | -43.97091 | 2026-06-05 04:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b948367-c426-302d-b369-2a006d493d1c | -7.64521 | -45.23053 | 2026-06-05 04:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7cce871-8653-32be-8950-9f18351d79ea | -8.72997 | -48.3312 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bd73e691-a215-3189-b9bd-cc854b49cc94 | -8.50017 | -50.29195 | 2026-06-05 04:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25ef5656-fc29-3f9b-b54c-6301b95bd2ba | -7.34679 | -49.8328 | 2026-06-05 04:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9c3332c-3f53-3ded-a96d-e87d88854763 | -11.27258 | -53.97362 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9cb9e4f-732f-3244-ad2d-dfd59c90bdb4 | -11.57764 | -54.57911 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a299afa4-acdc-329f-91f2-dc289d5765d2 | -12.8111 | -54.86397 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1818b581-6577-3308-aa8d-3e8dd8f1b593 | -10.93771 | -46.94022 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a62b370d-3492-3316-a63c-211653e242ae | -12.8119 | -54.8594 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 883ffa93-6283-30c8-926c-8fdfe4290768 | -12.73715 | -54.72972 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7d134c7-f55d-35e4-91c9-77f18f29f387 | -11.99796 | -45.34769 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d6dad5fa-872a-304d-b86e-7c1302dc9c15 | -11.06873 | -54.50962 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af973b87-42b9-32b3-a54a-e4bee6ae560c | -10.88196 | -46.99245 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2f26609-82a7-35c3-bfb7-dd6460806893 | -10.85681 | -53.74856 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab3ef9ec-829b-301d-a77d-53642ae1950f | -10.8416 | -53.7503 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd7a0f2d-489e-342c-9a7d-83f3f48acc2d | -11.56396 | -52.79675 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cd5db92-ed59-3c3f-ae55-02809d2c819a | -12.50309 | -46.34339 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 080b1666-f0d6-3629-a373-09e4cf055aa6 | -12.43915 | -58.48426 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f042d95-99cd-3c01-96f0-a484c56a1787 | -11.88543 | -57.8252 | 2026-06-05 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd7c98f7-98c9-3c00-bad0-002316b306c2 | -12.44199 | -58.469 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a3d7fe5-2739-3b5d-81b8-e2f4435b4b4f | -12.80095 | -54.87353 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b785ad-27c3-34ae-8e5d-d202701d3ce3 | -14.37498 | -45.55857 | 2026-06-05 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 242a1c89-8c14-3056-b27c-0be9b6a003b5 | -11.57016 | -54.5777 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c67f032-16d5-351f-938b-b4aadd9703c4 | -12.00041 | -45.35127 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef8da10f-ecb4-38e2-acde-65512cff6673 | -9.08063 | -50.61489 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f02a97a-3aa5-3c09-8f01-a3b60b4d2e09 | -11.54264 | -48.27297 | 2026-06-05 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0a51951-633a-367e-a715-83c65d273166 | -12.03085 | -45.89053 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aca39fd4-8828-3581-841b-ee66c232020f | -10.38637 | -49.44263 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60d399f0-6406-36dc-a40a-06d4e177d251 | -12.02759 | -45.88474 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baf6d6e8-6bf3-3080-9f33-a4ab6461ac16 | -11.04531 | -49.61575 | 2026-06-05 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b4f3fe-95b9-3823-bfac-e2eabd976bd9 | -12.80655 | -54.86785 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15dbc277-ad3f-3409-857c-7fa4aa93e024 | -14.0978 | -59.39325 | 2026-06-05 04:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43217104-e7a4-365c-b68c-29b9a9d29ddf | -9.90588 | -47.47933 | 2026-06-05 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1fae06a-22d2-3669-aa2c-0a46cd6df5f2 | -10.51953 | -42.36979 | 2026-06-05 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 11bcd4f2-4579-3bbb-99ea-615cb7ef624b | -12.23138 | -57.27108 | 2026-06-05 04:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32751bca-3dc9-34cb-ab22-f2479282b05d | -11.5558 | -52.80322 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d28717e-faf3-3e6b-b5e8-4bad6faac8be | -12.02847 | -45.88799 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b359d718-6127-3886-bb90-9cf11155c602 | -12.45147 | -58.47078 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1740d15f-7ee2-31d2-8717-7922c0ca381f | -12.03157 | -45.8853 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 428431ba-f4a5-3625-a572-9957f1853f46 | -12.52106 | -46.27653 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd19a69e-4bfc-3058-af03-9d68e5385e92 | -11.55988 | -52.79999 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bee92674-b7f7-321a-a02e-654db4c6e116 | -10.45546 | -46.42971 | 2026-06-05 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c81f818-cc65-3f6f-b50a-2240c37ecd22 | -11.0538 | -56.92366 | 2026-06-05 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50b227ee-3523-331e-a3e8-9fc8f26303a3 | -12.73184 | -54.73818 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f69f4268-a8cd-393b-bd05-2d2388c2f25b | -9.3746 | -50.54022 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 977be2cf-7029-3844-b0f6-986a4a7a2f14 | -12.73421 | -54.72455 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00728205-1cdb-333b-b3d7-3fbb0ef88783 | -15.31429 | -41.89506 | 2026-06-05 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49c82161-2282-3dc1-9184-db0c69fc5f60 | -12.73794 | -54.72519 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 325b9b28-df82-3e1a-b84a-aa0180e371bb | -11.56269 | -52.80441 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| adb3371a-0efb-3db3-9860-60d0a6d89784 | -12.02831 | -45.8795 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f5d63ec-e4fa-37dd-9e56-334459380b1b | -12.50432 | -46.34047 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ee538dc-4006-37cb-85a4-e6d98ceab76e | -15.31388 | -41.89861 | 2026-06-05 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95fa6e7a-5f8c-3cea-9094-662d3ee1f49f | -11.3835 | -47.81671 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2cafa76-53fb-3338-a077-af01d7a7e426 | -11.56855 | -54.58695 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b36202-6de8-380b-b82c-459f88c08120 | -13.51954 | -54.30707 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4745d21-9661-3f95-b568-06f341b8bb83 | -12.087 | -51.98993 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d6391fa-9a9c-3ddb-b60b-e7a67b4d08a9 | -12.52488 | -46.27517 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7651b303-0353-3652-84dd-66883a622f30 | -10.77048 | -54.10002 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e48aa474-9365-303a-8f7b-86603cd05c59 | -11.5467 | -48.26962 | 2026-06-05 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0501fd02-504d-3759-bd82-51a115e2e483 | -9.80913 | -48.23624 | 2026-06-05 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff273216-b5e8-3506-b84d-74ba61734a19 | -11.5739 | -54.5784 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0b0663a1-7f73-3b96-8bd7-a1712c4d6809 | -12.44011 | -58.47913 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8fb970ef-7feb-344c-9fe7-fd905f8fd022 | -11.38997 | -47.82185 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec2f197d-2ee2-31f0-94ab-99345b309571 | -12.45621 | -58.47166 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 323e1e05-d771-3d33-9f6e-3955801e0443 | -12.52417 | -46.28005 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a7c008-3dec-3bd6-8573-f08c1d920c78 | -12.06398 | -48.07362 | 2026-06-05 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90445aad-c65a-36ea-8f6e-ac647d3bd863 | -10.4036 | -49.44172 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b1c77b0-f525-3419-8501-4120dfa4eb35 | -10.84813 | -53.75579 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8fdd8b8-1477-3c2a-9011-a0cedaf9e91c | -9.1796 | -58.05811 | 2026-06-05 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3b66118-02b7-3085-8c97-84d0a4c896e9 | -9.7639 | -50.01355 | 2026-06-05 04:44:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a4de6e1-cc8f-3bbc-98da-c2da0ad8a064 | -12.92814 | -43.61878 | 2026-06-05 04:44:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfa9a955-7053-3415-a7dc-1cb2dc7873d5 | -13.51521 | -54.31069 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38a1efe8-589e-3d05-ab8b-3aa48387f78a | -11.33771 | -53.96544 | 2026-06-05 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2f9561-5bd2-35f1-88e4-fff2b45520e6 | -12.08976 | -51.99411 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c72f112e-fe14-3ef3-9561-d10f2f470002 | -10.93644 | -46.94901 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0467c9e-6ca6-3e5d-b916-bbf51b280467 | -13.52314 | -54.3077 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
