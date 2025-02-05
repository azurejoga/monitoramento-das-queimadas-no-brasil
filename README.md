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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a61b0c18-8bfe-3dd5-a4b5-0a4c9d7f8ccf | 3.601 | -61.4184 | 2025-02-05 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f073020e-0153-3c6c-8501-e065dac96d97 | 3.5827 | -61.4187 | 2025-02-05 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| cf224e54-fc98-313e-a549-952f8ee238b5 | -9.85908 | -37.27694 | 2025-02-05 00:05:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d5585ac5-6c14-3467-b434-a29cecb06fe2 | -11.82939 | -41.22639 | 2025-02-05 00:05:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| c3f3ff6b-273e-3c8e-8d86-346ecdea986a | -9.85025 | -37.27822 | 2025-02-05 00:05:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 33.9 |
| ebe1bfdf-e665-35fc-836e-3d5aec5c57aa | -10.62585 | -37.03547 | 2025-02-05 00:05:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c441f786-7fee-3f7d-920c-248115c2b7a2 | -10.67222 | -37.09571 | 2025-02-05 00:05:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 21f9ada8-5484-3537-9605-5024d9c7481e | -11.82878 | -41.23256 | 2025-02-05 00:05:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 0c9ef399-155c-39fe-8403-348294f1acfa | -10.67345 | -37.10466 | 2025-02-05 00:05:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 3128f2de-0176-3306-ac7f-343e678ae6ec | -9.36942 | -35.96218 | 2025-02-05 00:05:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f15944c7-c0bf-380c-ad21-55f1db7799da | -8.69494 | -37.19766 | 2025-02-05 00:05:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6011cd2d-0407-34ea-b28b-669bf70510ac | -10.62461 | -37.02653 | 2025-02-05 00:05:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 1fd26f9e-4ba1-3837-93d2-701186bc176c | -15.64505 | -39.19016 | 2025-02-05 00:05:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 7094198e-fe0d-354f-b641-9139cdb74412 | -10.68229 | -37.10338 | 2025-02-05 00:05:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0645791e-4b90-3687-bcae-63e0b07c4c56 | -7.05394 | -44.3873 | 2025-02-05 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 273e3931-45ad-301b-8f48-c9e63b5dc8f1 | -7.04061 | -44.38839 | 2025-02-05 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cc1b2cd1-d620-3045-97a9-c16eef1884f0 | -7.04331 | -44.40993 | 2025-02-05 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 161eb0c4-7aea-3ae9-9db6-7f55130f7d1a | 3.5827 | -61.4187 | 2025-02-05 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 97.8 |
| cabadf22-53c6-316d-ad23-869ce487efb5 | 3.5826 | -61.4376 | 2025-02-05 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a6d805c8-8100-3fcb-94d0-c849c5178e7d | 3.601 | -61.4184 | 2025-02-05 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1bf6cbed-76f9-3668-9dbc-382d29a2f88c | 3.6009 | -61.4373 | 2025-02-05 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5be12b34-dff1-3b6c-8514-67c391aa06a0 | -11.5849 | -44.8423 | 2025-02-05 00:17:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96181b9e-f866-3688-b50d-15353bbcdf5c | -11.0327 | -45.0448 | 2025-02-05 00:17:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88194307-0d76-3f10-855f-5c4890fc797f | -9.8525 | -37.257 | 2025-02-05 00:17:00 | METOP-B | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 0b8569e7-ab94-3ee4-9fa7-a37e233ff261 | -12.5407 | -48.304798 | 2025-02-05 00:17:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf7a283-962a-37e7-933c-8b36ce0026e5 | -11.048 | -42.738201 | 2025-02-05 00:17:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 760b1a47-59c6-3b54-8721-a1e0af858815 | -7.0558 | -44.386398 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 149d88f7-6111-3b99-aaa2-ee1d71fc4fb9 | -7.046 | -44.388599 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6cb4425-50e4-329d-b9e2-63ae1d2d5fea | -7.062 | -44.3685 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 601b0092-cdd6-3d99-8468-c54762a3621b | -11.5865 | -44.8494 | 2025-02-05 00:17:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32bbd72b-45df-3421-a94d-3e88fc47c6db | -7.0638 | -44.376301 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26c8ae53-4a03-386a-906c-5b39bd7a188b | -7.054 | -44.378601 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55264249-c0c1-32cc-82fd-9042cd13af0b | -10.6831 | -37.0812 | 2025-02-05 00:17:00 | METOP-B | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f713539e-687d-3dca-9339-5500e2a2369d | -22.9235 | -43.717098 | 2025-02-05 00:17:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0478973-a821-3e5f-8d82-954eb5cbfed6 | -20.243799 | -40.216202 | 2025-02-05 00:17:00 | METOP-B | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 726778d7-927d-3a2a-a2ac-fb24c99358b8 | -7.0478 | -44.3964 | 2025-02-05 00:17:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf4a9747-1062-3739-8f89-cbd4d91e3c96 | -10.6735 | -37.083698 | 2025-02-05 00:17:00 | METOP-B | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66013aa4-1d14-3b23-a57c-b9d6b1894fe7 | -12.5423 | -48.312801 | 2025-02-05 00:17:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd1f68dd-1347-3040-9e38-063c844ddb88 | 3.5827 | -61.4187 | 2025-02-05 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 92673675-09f8-33fb-a91a-0018a1a362c1 | 3.6009 | -61.4373 | 2025-02-05 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 05719d68-f060-32b4-9daf-87b9017a5fb2 | 3.601 | -61.4184 | 2025-02-05 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a57c6049-d209-35a6-b5f9-a3bd7a0392fc | 3.5826 | -61.4376 | 2025-02-05 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 394f33c0-fff8-315e-b7c0-e65c4f518769 | 3.601 | -61.4184 | 2025-02-05 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 019d930d-57f5-3069-94d9-14dd841f0725 | 3.6009 | -61.4373 | 2025-02-05 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0f5f38ac-98f4-3234-b6c2-9ac2d958d925 | 3.5827 | -61.4187 | 2025-02-05 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 0f1c1985-18c9-34e6-9fd2-af74a8eb54e6 | 3.5826 | -61.4376 | 2025-02-05 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7b6a73c2-7167-352a-812d-e3d855cbc5e4 | 3.601 | -61.4184 | 2025-02-05 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ebfd1c39-6639-3507-86d7-39019fd67f18 | 3.5826 | -61.4376 | 2025-02-05 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e19009a9-3225-3984-9701-eeaeb7f25f88 | 3.5827 | -61.4187 | 2025-02-05 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f7210be8-ab6f-3a56-960b-252188f6c35f | 3.6009 | -61.4373 | 2025-02-05 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 38580840-c4e6-33fd-a6de-501827a4e8bd | 3.6009 | -61.4373 | 2025-02-05 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 95eacfad-2181-3443-a1e7-61184f051ba7 | 3.5827 | -61.4187 | 2025-02-05 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d6df0f33-fbfa-340c-94d4-a56aefe1a7b6 | 3.601 | -61.4184 | 2025-02-05 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f1cb6cf4-dffc-3c82-aa42-4fce0ef4578c | 3.5826 | -61.4376 | 2025-02-05 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ddbb969c-8ea9-31dd-beb4-649ef76922d8 | 3.601 | -61.4184 | 2025-02-05 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bf55987f-cdaf-3389-b046-ca17631214b3 | 3.5826 | -61.4376 | 2025-02-05 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fc0485bd-9517-3c9d-8d09-e962a2f42100 | 3.5827 | -61.4187 | 2025-02-05 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5a64ad1a-9672-3cca-96c6-bafdca06a680 | -29.401699 | -52.020302 | 2025-02-05 01:09:00 | METOP-C | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0b4d48f-0e8a-3d73-9648-8e610894e8e2 | -29.403299 | -52.028301 | 2025-02-05 01:09:00 | METOP-C | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cdcbb225-4a25-32bd-bf0c-59f9197a1b49 | -29.7794 | -50.570999 | 2025-02-05 01:09:00 | METOP-C | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d8ec549-5c57-35af-8efa-3206838e577a | 3.601 | -61.4184 | 2025-02-05 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 4707df2a-83c3-325d-9ed3-05cc1409d095 | 3.5826 | -61.4376 | 2025-02-05 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0a9c24d3-e318-34ec-a2d5-0e0c4cfeb6f3 | 3.5827 | -61.4187 | 2025-02-05 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 47bc7ec4-ea6f-32dc-8208-16208152e703 | 1.1228 | -60.516899 | 2025-02-05 01:11:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 74fd16fb-195e-382c-809d-183511e3a1ed | 3.5818 | -61.431 | 2025-02-05 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf5edb8-9d33-332f-8ceb-563209d2c6f2 | 1.3766 | -60.8018 | 2025-02-05 01:11:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fd91140f-3ca3-38a4-bf03-c10ef899b05c | 1.3784 | -60.793999 | 2025-02-05 01:11:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ccaa33f3-d0bd-3560-b879-004614b86039 | 3.5047 | -60.293999 | 2025-02-05 01:11:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8efee77e-6900-3d5d-be04-bd3e27d8d051 | 3.5836 | -61.4231 | 2025-02-05 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f58ed30d-9450-3f7f-a095-8fa89876daa6 | 3.5063 | -60.2868 | 2025-02-05 01:11:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 122e1c59-2dba-3610-92d8-cd1b60930099 | 3.5855 | -61.4151 | 2025-02-05 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb25e25-7089-363a-bbf6-abda262f1d0e | 3.5827 | -61.4187 | 2025-02-05 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f970c1a3-b258-3205-a5cb-ad7d4cf77114 | 3.5826 | -61.4376 | 2025-02-05 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d1cd8f91-6da3-3f84-9bfa-2988a319b879 | 3.5827 | -61.4187 | 2025-02-05 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ecc3171c-5144-3574-928b-72ab08ef6108 | -21.07382 | -56.39645 | 2025-02-05 01:41:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f3e5548b-ab34-3337-b11b-5b0621b599f9 | 1.38063 | -60.80323 | 2025-02-05 01:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 86ddb1bb-0b08-3b2f-96ca-587afd100c34 | 3.51719 | -60.29657 | 2025-02-05 01:47:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| db309828-a015-31f9-814c-c27b60010c18 | 1.3906 | -60.80462 | 2025-02-05 01:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 79ae391c-07c5-3028-89d7-1e00b1939a29 | 3.58679 | -61.42429 | 2025-02-05 01:47:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8a5e0e4c-3f50-37a8-8895-4365b7152370 | 3.58528 | -61.4355 | 2025-02-05 01:47:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f9fe3120-862a-358d-8f12-f665768d81e7 | 4.36642 | -60.32828 | 2025-02-05 01:47:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e564e32e-a390-3562-bd9c-c9f8e99a45bf | 3.59665 | -61.42564 | 2025-02-05 01:47:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ac76e148-c4f4-3de0-8685-53a3ca42f524 | -5.48902 | -35.55145 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c8e9ad5a-2f6d-3724-aeb4-bfac6a9238b4 | -5.49586 | -35.55278 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18158746-8277-3d6f-87ed-3c8b76e280df | -5.48791 | -35.55764 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9403f26d-b679-3a22-ae0a-190957104edd | -5.48927 | -35.55154 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e3144b56-54b7-3356-b65d-b0061729398b | -5.49013 | -35.54531 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8caffaf6-4039-3e28-843a-82fa363e2370 | -5.48812 | -35.55772 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c088fb25-3868-3c69-a173-b20f54864c97 | -5.49042 | -35.54537 | 2025-02-05 02:49:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ddf2b84c-64e4-3dcc-902c-16d57d61cbcd | -7.04512 | -44.39483 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbae6f69-35d6-377f-98df-03c54cd02f09 | -8.84931 | -36.52134 | 2025-02-05 03:42:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10028888-be6d-3e1f-aba2-45e398bdbc24 | -6.41753 | -35.64613 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0c5d0db0-a535-34d5-bdf7-5f55362a6670 | -7.12955 | -38.77932 | 2025-02-05 03:42:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8aee254-9d73-3610-ae90-3c388da66648 | -7.0434 | -44.40472 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5759a54-d4ee-3504-bb5f-fcef9e3c23a8 | -7.05729 | -44.38129 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21c7166e-6509-3f85-9f9c-3992fe8ef48f | -9.4735 | -35.93182 | 2025-02-05 03:42:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a74d810b-64cc-36ee-bdc2-6e0f2a6f688f | -6.97791 | -42.99147 | 2025-02-05 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 43cd775b-7e90-3040-8f14-63700544e463 | -6.41038 | -35.64856 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d485abca-34e3-3d86-a3ad-48225fc3ad95 | -6.41423 | -35.64561 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b238ac12-adc6-34f9-a5da-a1413ef9be34 | -6.38275 | -43.66805 | 2025-02-05 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
