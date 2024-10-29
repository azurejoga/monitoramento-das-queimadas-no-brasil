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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e5af9d-b856-3e81-a386-e7a3934666a4 | -11.72101 | -48.35998 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c28fa28-813b-31e2-af0d-81e86d128a79 | -11.24678 | -47.90147 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58c9f56b-7f52-3f27-9799-aa434cd422af | -11.24638 | -47.9047 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9f8f8f0-8f4f-3430-abc2-23a1df1efde8 | -11.24598 | -47.9079 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ab05b17-fff5-3088-83e1-90c4e0f9fba1 | -11.24155 | -47.90064 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c390594a-49e0-387b-879b-f911613fbc0a | -11.24115 | -47.90386 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cca0848-e392-33c3-952a-a48a948ff097 | -11.24075 | -47.90708 | 2024-10-29 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1101285d-6283-3067-943e-555b2e90ee2e | -11.01194 | -48.67223 | 2024-10-29 05:04:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 896bc367-34c4-3f21-840e-71a724a3916c | -6.39277 | -49.58514 | 2024-10-29 05:04:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 450d3500-a2ee-3ed5-8942-d08c13bce8e1 | -6.38844 | -49.58435 | 2024-10-29 05:04:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8cf7ff4-7504-36a9-8f18-5f3972ce5243 | -7.10106 | -48.38016 | 2024-10-29 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f501b479-bbdf-3701-9e66-c7830fafa3b7 | -7.10041 | -48.38401 | 2024-10-29 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2508f8-d1b9-39b6-914a-edad77c26a7b | -8.84038 | -49.8567 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5756fdb-2ee4-3596-a2e7-4bed12cc21c4 | -8.83979 | -49.86102 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ed3847f3-6001-3328-92a1-c9fc555d8207 | -8.812 | -49.67942 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7c56be-385d-36a4-a825-b7c0bc5fd325 | -8.81137 | -49.6839 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34956557-f763-3c72-93ca-c1e2448dd61e | -8.75131 | -49.78842 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae2af407-a654-3b65-8dd9-7f4f1c60cce7 | -8.74748 | -49.78332 | 2024-10-29 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf3d2b0a-20a2-388d-a65e-3ee3e4d56a62 | -8.53837 | -49.71227 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d54871f-8ffb-3078-b72b-5af2c7ac9275 | -8.53629 | -49.70996 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ea36aca-c206-3b35-aebc-3fb9966c73ee | -8.48647 | -49.4463 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7953d3c7-90cb-38e0-aade-94f7890c675b | -8.04654 | -49.65684 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca406974-43c1-38d2-95dc-e6bac3556da5 | -9.86833 | -49.68934 | 2024-10-29 05:04:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5abf7d2-b83b-3582-8ba8-fc6f66ece55b | -9.8677 | -49.69398 | 2024-10-29 05:04:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6f27872-4000-3136-a206-794ea9aa4c1a | -10.23639 | -49.69068 | 2024-10-29 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c21286bd-f06b-3083-992f-b49f8d159c7a | -10.23627 | -49.68768 | 2024-10-29 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8c8aa2f-5d46-3a4b-8350-49e134db104e | -10.23247 | -49.68532 | 2024-10-29 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 706bb556-7d9e-3702-a941-23f4e1962a9a | -10.23182 | -49.69004 | 2024-10-29 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1b36c99-d8a8-37af-863e-66906d5caaca | -11.18022 | -49.86552 | 2024-10-29 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 784920c3-80dd-3a14-a8de-6d6157007c3d | -12.35125 | -49.93338 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8248986-5671-37fd-9f94-7edd221f2aa0 | -12.34945 | -49.92654 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 953b658f-55f0-3f81-a4ca-b913fd795c10 | -12.34879 | -49.93147 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0c7e3b3-6282-3d21-8ca9-9a50cd568a77 | -12.34813 | -49.93636 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7490ba34-baf8-3beb-bcc5-1d0bf7384204 | -12.34786 | -49.92281 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5aa2c899-0ace-3f83-b07d-7c30fa7eaca9 | -12.34724 | -49.92776 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a2541a8c-ae3d-31d0-ad8f-394f86d1a28d | -12.34661 | -49.93268 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 63773361-23a9-3b7e-afd9-8f3160bae372 | -12.34599 | -49.93759 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ee21fed0-96d3-3b7b-87a8-199fcb917931 | -12.34548 | -49.92094 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed15451a-8cf0-3f94-8bc5-5a120daa5736 | -12.34481 | -49.92587 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| be28d640-c46d-3838-8d65-60ea7e9a91c4 | -12.34415 | -49.93077 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f663ad56-c41a-329e-9114-d7f2ae9f6adf | -12.34384 | -49.91722 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bef1be4d-219c-3ab2-b0aa-acd5bfb73b15 | -12.3435 | -49.93567 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbeaa968-2967-3aa2-8357-0b5a95349366 | -12.34322 | -49.92213 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0e307b55-41eb-3469-9120-8473be1e12c7 | -12.3426 | -49.92706 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 49fbf7d2-d8dd-3e72-b65f-618ad04dfff3 | -12.34198 | -49.93198 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 867ce201-5607-3abf-928f-e723bfd0b41e | -12.34136 | -49.93689 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f828be69-e60d-3f3c-8a47-016f6d84c43a | -12.34084 | -49.92027 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c6040f4c-b4b6-397a-846b-74e529d49371 | -12.34018 | -49.92517 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c6ad29f9-3837-31a6-97a1-41f52b4fc57c | -12.33953 | -49.93008 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a5000525-ac0b-38fd-b384-669df9e46c12 | -12.33887 | -49.93497 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3ac6e773-285b-3255-846c-99c98de3dbb0 | -12.33821 | -49.93988 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a551eb0-cefe-3c69-a12b-d248a1d85de1 | -12.3362 | -49.9196 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a1bc83d-10ec-38aa-b397-b1bc5022521a | -12.33555 | -49.9245 | 2024-10-29 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb53fe74-0ff8-3220-b961-ae70939929e7 | -6.05714 | -51.15625 | 2024-10-29 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92921d39-b8de-308e-aa24-094a3158d8a1 | -6.21539 | -50.85085 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e88f9a0-84a0-3310-8a30-bb475df45c03 | -6.2146 | -50.85603 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d543244b-bb5c-3f1c-b398-aac41df4acab | -6.21256 | -50.85191 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a5528a2-75a9-31e4-b100-bc59bb83356c | -6.21141 | -50.85023 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fb0d414-dfe1-3978-bfc5-000b378d16c8 | -6.2046 | -50.85061 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d995da3e-0c9f-3140-b5f2-5a4656505d65 | -6.20344 | -50.84898 | 2024-10-29 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f08d4a6b-fec9-3909-865f-78abca54b5f2 | -9.33979 | -50.6543 | 2024-10-29 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29735209-e15b-361f-acc4-7a2a48089b88 | -9.24975 | -50.71435 | 2024-10-29 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef9ddd7d-4cd3-3e87-8216-836cdfc81de8 | -12.09753 | -52.48108 | 2024-10-29 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 567b170d-459e-3648-9157-ae469d52329c | -12.09681 | -52.48609 | 2024-10-29 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd89fa5a-cd22-3bf6-a7f0-241cb0bcf546 | -12.09363 | -52.48051 | 2024-10-29 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 449df512-00ea-33be-8abd-8d12c41f512a | -12.09291 | -52.48552 | 2024-10-29 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f3a2bb8-e52a-39bc-9772-6af8a1107bd3 | -12.0922 | -52.49051 | 2024-10-29 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a99578a6-7e83-3f02-b4ed-ba486c3572a0 | -11.21595 | -51.64485 | 2024-10-29 05:04:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc24386c-ea5a-3a9c-95e6-758436357156 | -11.21545 | -51.64844 | 2024-10-29 05:04:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a358358a-36fb-3bc6-893d-46e0b7d00831 | -5.72955 | -51.45253 | 2024-10-29 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e1386da-d55e-3420-996b-d9260e2fa451 | -5.72885 | -51.45722 | 2024-10-29 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eedd2fe1-8faa-3ce8-aa7d-07375196214a | -6.26671 | -51.70124 | 2024-10-29 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05fd8ea3-079d-377e-b36e-b73d9d47e040 | -6.26292 | -51.7007 | 2024-10-29 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba18aca1-208f-3d76-95c6-21de0af25a72 | -6.26223 | -51.70527 | 2024-10-29 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0947d808-35fb-327e-982e-6917e0dae8fe | -6.17095 | -53.58529 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e45463b-f15a-3444-b2fd-6685c1ccf7a0 | -6.1675 | -53.58479 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dfdbc10-d72c-3eee-aa3a-754c5444b778 | -9.89423 | -54.80421 | 2024-10-29 05:04:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962c068c-96cf-3897-bc7d-4566f538f0f6 | -9.84145 | -54.80724 | 2024-10-29 05:04:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3cb7912-6036-3900-9fe3-0f773c14a603 | -9.83804 | -54.80676 | 2024-10-29 05:04:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e6bfdc9-54b6-3269-9527-4e586a8aa7a3 | -9.47592 | -54.52805 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d5f9aff7-f9e0-3f0b-accd-3c3dcf8b5882 | -9.47249 | -54.5275 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f60121-abab-3b37-87b5-12abe6141e93 | -9.38337 | -54.81313 | 2024-10-29 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94cd9814-e4c0-3a0c-b772-0c7bb5b9e268 | -10.66996 | -54.43997 | 2024-10-29 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d263605a-590c-363c-aa7b-f788a1924629 | -10.41396 | -55.07457 | 2024-10-29 05:04:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e69e8507-0327-3446-8f2c-dedd5ff833c6 | -10.33917 | -55.01777 | 2024-10-29 05:04:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3a4bf1f-8339-317e-9a1e-76ad9ba5e937 | -10.33915 | -55.01779 | 2024-10-29 05:04:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd2bf4f0-6520-3e5e-8ae4-27324433e8a4 | -10.10572 | -53.64346 | 2024-10-29 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b620658-fc1b-30b2-aeee-43264d545e03 | -10.10215 | -53.64292 | 2024-10-29 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 006b040f-7096-3587-baeb-a282dc1678c7 | -10.03466 | -54.33178 | 2024-10-29 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3903ed-638a-3994-956f-5e18562d01c7 | -10.03119 | -54.33126 | 2024-10-29 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55a07e7b-3e2d-3d7e-9a22-7041a462ca44 | -10.02772 | -54.33076 | 2024-10-29 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13eded72-0504-3643-8a9a-140ebe9f21e3 | -10.02715 | -54.33459 | 2024-10-29 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3660e4cd-7981-32cb-bb53-5c61ce705228 | -11.89775 | -54.80103 | 2024-10-29 05:04:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf66ac0-f9c0-3117-b2e9-5217aa6039b1 | -11.89429 | -54.8005 | 2024-10-29 05:04:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2887d8ae-9c68-3410-b606-7479c09dde2d | -11.76125 | -55.45657 | 2024-10-29 05:04:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e11d894d-af4c-3139-96c2-c3e33c86c0df | -11.76069 | -55.46024 | 2024-10-29 05:04:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73c89f2c-96f4-3a18-be1c-e93f09565dee | -11.76013 | -55.46392 | 2024-10-29 05:04:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac0e8909-a288-37a6-aea8-cc492653d4cc | -11.55709 | -54.47392 | 2024-10-29 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f727e36-c5ce-3a08-9eb9-271797e70f8a | -11.39571 | -55.08684 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4948e7f-535a-3f4b-940d-6b705ebbf637 | -11.3923 | -55.08632 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README93.md)
