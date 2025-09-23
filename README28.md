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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 287a010c-3077-32b0-891f-a2b721468dfd | -11.9296 | -43.4288 | 2025-09-23 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6aab387e-e4b7-3dba-a73f-1764887b9748 | -8.5182 | -44.952 | 2025-09-23 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 19742872-26b4-3bf1-9b04-0228562ee2b7 | -9.1671 | -43.1588 | 2025-09-23 12:50:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| 7dfc1417-d418-353a-b6b0-24dd03a81e30 | -8.5371 | -44.9499 | 2025-09-23 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 19f77626-b28c-3cac-84f6-affb30955f6e | -11.5229 | -43.6344 | 2025-09-23 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| de1e3b06-80f6-3a04-88d3-00979b9ddfbd | -8.5182 | -44.952 | 2025-09-23 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bf3952ca-8cdc-3ec3-856b-7272a051af85 | -9.1671 | -43.1588 | 2025-09-23 13:00:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| bf2bbf10-41c9-3b57-b918-3b221faa77b0 | -10.313 | -45.2219 | 2025-09-23 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 846d1450-6935-3ebc-8f72-d4207e9882b8 | -8.2803 | -44.3801 | 2025-09-23 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 190.0 |
| fdc6acb1-af9b-3475-8d53-e6ff881dc02e | -8.8081 | -43.0845 | 2025-09-23 13:00:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| e7a05b69-8707-3643-aa5a-53ab68f3a966 | -8.5179 | -44.9749 | 2025-09-23 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 80c10a5d-3796-341c-8ce9-e78e77f3dde4 | -7.3493 | -38.859 | 2025-09-23 13:00:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 92.7 |
| bc3a7c07-ef31-3969-8b46-7127dbe37d8b | -12.0462 | -43.3626 | 2025-09-23 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e4a9752f-4579-32a6-a324-7c659aba6895 | -11.9104 | -43.4319 | 2025-09-23 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7bfadfab-5d49-31bb-9b19-52312bf2daa0 | -12.8879 | -44.6378 | 2025-09-23 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 70e5c9c0-794d-3f65-a836-3bb61e3f7b3f | -8.8084 | -43.0608 | 2025-09-23 13:00:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| d0200ca0-a7a5-3bea-b3d3-48b536846e91 | -11.9108 | -43.4081 | 2025-09-23 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6ef6451a-a460-37fc-9a9c-c720cc521c9a | -10.313 | -45.2219 | 2025-09-23 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a469d933-56b0-36f4-bb8b-dceccc3ddaef | -11.9301 | -43.405 | 2025-09-23 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c4b9cf8a-18c2-36f0-ab57-51f7b94cc1a5 | -12.8879 | -44.6378 | 2025-09-23 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| dfa63bd6-a345-3141-b628-97d641f62b51 | -7.3493 | -38.859 | 2025-09-23 13:10:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 91.8 |
| dc94a01e-ff0a-375a-9bb2-b4048878935f | -11.9104 | -43.4319 | 2025-09-23 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| fd9c6571-047c-3e31-bfe5-4af70e6ff8ed | -11.9296 | -43.4288 | 2025-09-23 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| cc715f21-8fbb-38ff-b4db-f972bcfaead0 | -11.4674 | -43.5248 | 2025-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e57cbf7f-c4ac-3d87-bc6c-594d665384e6 | -8.2803 | -44.3801 | 2025-09-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 84b852b0-d3d2-3c0d-9125-67b5cf9c632d | -8.3981 | -39.9116 | 2025-09-23 13:10:00 | GOES-19 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 85.8 |
| dbe0187c-a985-3cf5-b1f3-8e07b50a0d42 | -11.9108 | -43.4081 | 2025-09-23 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f3dc2eb6-89f4-3134-8d7b-b4c801be4b72 | -9.1671 | -43.1588 | 2025-09-23 13:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| dd0bf004-e313-3847-b94e-ff503beb1e51 | -6.1224 | -44.004 | 2025-09-23 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 5feb52d0-26d9-33fc-aa38-f182540915e9 | -11.5041 | -43.6136 | 2025-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5f21c5fa-8d6a-3d3c-99c2-d2f905c56ce3 | -8.5179 | -44.9749 | 2025-09-23 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e4101020-b44a-32d3-8832-20ed1c5eea14 | -8.8084 | -43.0608 | 2025-09-23 13:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| ab6c65d0-abcb-32f9-a521-39fccbe03df5 | -11.5421 | -43.6314 | 2025-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 00db26e8-5040-301d-994e-d94f812cba88 | -11.4482 | -43.5277 | 2025-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cc28df41-3d45-3006-83ad-9401740e7f18 | -8.5182 | -44.952 | 2025-09-23 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e6621dcd-10f5-3c8b-bb2e-6c7ace5f9573 | -11.5233 | -43.6107 | 2025-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 873bbdbb-f7d9-34c2-9a58-dbb8c4263198 | -11.9301 | -43.405 | 2025-09-23 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| f123455c-257e-33de-9bbd-160f159a5b09 | -8.2803 | -44.3801 | 2025-09-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a9a5d215-903e-3800-9eb8-8c057c652b03 | -11.9104 | -43.4319 | 2025-09-23 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 46840351-6be9-3b29-8bde-00c836c4a14d | -8.5182 | -44.952 | 2025-09-23 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d247f17a-1698-362c-8328-e60e957460af | -8.5371 | -44.9499 | 2025-09-23 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9b049cb4-88e6-34ea-a160-bc6ff93637f8 | -8.5179 | -44.9749 | 2025-09-23 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| f56c1d04-0467-3959-a6f3-2bf05b2995f2 | -9.1671 | -43.1588 | 2025-09-23 13:20:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| 2e9c589f-9fca-3539-8557-97ee628e0306 | -11.9108 | -43.4081 | 2025-09-23 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 8033873f-9d7a-34cd-ad80-614a908293b3 | -13.2535 | -43.752 | 2025-09-23 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 365e3554-9978-3675-a007-3c3aa95af0ca | -11.9296 | -43.4288 | 2025-09-23 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 39e337b5-3359-328c-bfbe-41b92ec20d12 | -6.1224 | -44.004 | 2025-09-23 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a5bafd05-6131-3ffb-b7f6-ab984763b88b | -10.313 | -45.2219 | 2025-09-23 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 0059d567-c909-3d83-a9ee-5afb23a32474 | -11.4482 | -43.5277 | 2025-09-23 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 91edaeb2-f1be-382d-b63d-8b4c75088700 | -8.8285 | -44.343 | 2025-09-23 13:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 36387948-bcb9-3a78-9425-630dfa28c854 | -11.9104 | -43.4319 | 2025-09-23 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| ce1d2ef7-1810-31b4-87a4-b5c316569c6e | -6.1224 | -44.004 | 2025-09-23 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1d17968d-a536-37da-9bff-0be4eff029cc | -9.1671 | -43.1588 | 2025-09-23 13:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| ada6bb99-a73f-30ee-9e7f-d7f9fffde987 | -8.5182 | -44.952 | 2025-09-23 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 235cb832-757c-3c83-abb3-e6ddca6b43bf | -8.2803 | -44.3801 | 2025-09-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| f6017b61-9c95-35e0-a3fd-7cc600e21b68 | -10.313 | -45.2219 | 2025-09-23 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 83395018-0660-3b82-8ac8-c0249ec823e9 | -11.9301 | -43.405 | 2025-09-23 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 7a57994b-875a-39e7-8a00-f653281ba701 | -13.2535 | -43.752 | 2025-09-23 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 8c42f7d2-929e-313b-b9fe-e8691f4498ad | -6.3539 | -43.3583 | 2025-09-23 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8bb3e0c1-53dc-3616-b77c-7261207e8a46 | -10.8319 | -46.0889 | 2025-09-23 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| cb978aef-8bb0-38f0-8b66-c36c6ec50e8c | -11.9108 | -43.4081 | 2025-09-23 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 15826299-9b15-3cbe-9bca-d587cf7ff748 | -8.5179 | -44.9749 | 2025-09-23 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.1 |
| d8210525-4d8f-3da2-9738-a9688793aa34 | -7.3493 | -38.859 | 2025-09-23 13:30:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 94.5 |
| e09e1cb0-f6f7-3838-b392-420d7785ac38 | -7.5859 | -42.5828 | 2025-09-23 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 6eb33c0c-c69d-3da5-9a39-7a890d85b114 | -11.9296 | -43.4288 | 2025-09-23 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 2a44ea7e-6f81-3c1d-adfa-9d420c410088 | -8.8084 | -43.0608 | 2025-09-23 13:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 592ab397-03db-3a2d-bcf2-53fb659a77a9 | -11.9301 | -43.405 | 2025-09-23 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6ab15c52-616d-3d31-9eda-a387d3e8be13 | -6.1224 | -44.004 | 2025-09-23 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a53f2786-a36b-3682-a0e7-9e39882cd563 | -8.5185 | -44.9291 | 2025-09-23 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f5abaa72-e6b5-3300-bf31-533e18028e57 | -11.4041 | -44.9359 | 2025-09-23 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| f7b1f00f-4fe4-389c-9b32-b41bc6dfa3db | -13.2535 | -43.752 | 2025-09-23 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 520cdb2e-30a4-305e-8ef9-3b9388628e98 | -12.0771 | -44.7898 | 2025-09-23 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 58284522-4098-31f9-986c-96c27c5a88b7 | -11.4233 | -44.9331 | 2025-09-23 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f65754bd-cef0-3973-a173-44741751c13b | -8.2803 | -44.3801 | 2025-09-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 2ee9d6f2-51e3-3caf-9c76-9b681e7f3964 | -10.8319 | -46.0889 | 2025-09-23 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f372478c-5f03-305d-8bb6-5fff2c3a7537 | -11.9493 | -43.4019 | 2025-09-23 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c80baff8-a0e9-3e3d-a3e2-dce2967af4d5 | -11.9296 | -43.4288 | 2025-09-23 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e05aafea-76bc-345e-a591-cb8c4aa2744f | -8.8084 | -43.0608 | 2025-09-23 13:40:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 3b800595-dbd1-3b5e-85a6-da8396ac9f9d | -11.6442 | -44.3434 | 2025-09-23 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 59429c76-ebfb-3613-8164-d917e43ec2ac | -3.8002 | -41.6947 | 2025-09-23 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| b315b53b-39f9-3406-8b69-46045ef81b38 | -11.9108 | -43.4081 | 2025-09-23 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 65445aaf-27f3-36bb-8509-d7d699934b4e | -11.9104 | -43.4319 | 2025-09-23 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e887aa60-68d4-3105-89b9-43233785e85d | -8.8285 | -44.343 | 2025-09-23 13:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6528d88c-a250-3469-9de3-4097fb201a23 | -11.4041 | -44.9359 | 2025-09-23 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7fb6875c-eb33-3d76-a4ce-e72f26f0a8a3 | -11.9108 | -43.4081 | 2025-09-23 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| d24fce7e-6348-3c69-939c-a00e59fd840a | -11.4037 | -44.959 | 2025-09-23 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 65ef15ba-e350-3f79-b7fa-91a849e65157 | -9.1937 | -45.2886 | 2025-09-23 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f35c7ea6-d796-3f38-b5cc-0518c5bbe4d3 | -8.8609 | -46.1625 | 2025-09-23 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 738ed64c-8e4b-3057-9e62-737de194dacf | -11.9301 | -43.405 | 2025-09-23 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 9333bde0-b768-3f27-b9e1-c9e0a9ac54bb | -11.6639 | -44.3171 | 2025-09-23 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| d9a7ec4a-cbb7-32f9-bca9-f996d26ef0f6 | -12.1348 | -44.7809 | 2025-09-23 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 573d0fe4-8acf-3dfa-afc6-57f982f9d960 | -8.2803 | -44.3801 | 2025-09-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3a342ff5-c9e6-33c4-81fb-fa9b483db961 | -11.6643 | -44.2937 | 2025-09-23 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fafc9b87-6fce-3a54-bc14-e3e1ae7375b1 | -11.6826 | -44.3376 | 2025-09-23 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| bf772d28-aca3-36a5-ac34-442a8148037f | -8.8851 | -45.7541 | 2025-09-23 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 030b5259-f25b-3a36-a539-40dfc51e6f0c | -11.9296 | -43.4288 | 2025-09-23 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 8ef51d9f-24b7-30f5-8be6-be86bb560b65 | -11.4862 | -43.5456 | 2025-09-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| db36f6ab-7b01-3c00-8706-11c893c97938 | -8.9588 | -44.4898 | 2025-09-23 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 48c215a1-eec9-3f2d-b65a-4f4cb24cabcc | -7.5859 | -42.5828 | 2025-09-23 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| ec9b5a45-adc5-3f69-96e1-2eaf47c83d1a | -8.8057 | -46.0558 | 2025-09-23 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |


[Clique aqui para ver as próximas entradas](README29.md)
