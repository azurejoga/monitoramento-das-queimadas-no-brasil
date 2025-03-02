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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd014067-fc13-3527-aec1-7439f01953c5 | 0.7703 | -60.55187 | 2025-03-02 04:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7dd4a7f7-98fb-3b6e-aec3-a0488663d22b | 0.97152 | -60.53065 | 2025-03-02 04:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac408081-7b79-3645-9379-3caf7bdcffbf | 0.96478 | -60.53164 | 2025-03-02 04:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f3d2894-a98e-3364-af07-ddc9501b8ba7 | 1.32313 | -60.43894 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0fa18e79-a33d-3bd1-87e0-b87a8bdc1435 | 1.32125 | -60.42706 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9958af03-b5bc-36d9-90db-8f6e20c5283f | 2.58398 | -60.62666 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b44e7946-db5e-36a7-8076-8646b5ec6595 | -9.23033 | -45.02654 | 2025-03-02 04:40:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 62728c62-655e-366c-a920-5bf6f15ba99f | -12.84543 | -43.83008 | 2025-03-02 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 69ebeb95-fe31-3142-9f30-d09d84638927 | -12.85071 | -43.8258 | 2025-03-02 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2093e03d-31c4-39b0-b622-bca7c666ca76 | -10.92591 | -44.08514 | 2025-03-02 04:40:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b34254ca-2ef0-34db-a7b9-dd7270448e17 | -12.85007 | -43.83072 | 2025-03-02 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4ed22b66-fa98-3d0e-bff4-8bc8da15f307 | -12.84607 | -43.82515 | 2025-03-02 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b0c9406-de1c-34e5-a923-453210cc5f64 | -11.4514 | -52.92041 | 2025-03-02 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c9b0ed-2f53-3920-b139-9ee2b7b0fd7d | -13.97208 | -45.58213 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7240ff7-db26-3835-b011-9ec8a04d9b70 | -13.97943 | -45.59114 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdaad2ff-22c8-33e9-be82-86aa4d2a330c | -13.99721 | -45.58574 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290d4508-b0e4-3232-aedf-b131ddea8241 | -13.97157 | -45.58603 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da638bec-8b94-3271-8312-c722e5263dd9 | -14.0014 | -45.58632 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 086b1ff2-ccbb-3a5b-884f-e627fd025c8e | -13.99826 | -45.57788 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85717c71-4305-37a9-bb50-bcef62b73ed2 | -17.67291 | -54.15961 | 2025-03-02 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fef1639-8388-38e7-a79d-8524fd4501ae | -13.97994 | -45.58725 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07f39e52-46cd-33ed-8182-66dc1d5dfda9 | -13.99878 | -45.57396 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0933060-a089-3d88-9439-e30977c45bd0 | -13.788 | -44.33431 | 2025-03-02 04:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2376f3b-d903-37a0-839e-48d89c13f3c7 | -17.33163 | -53.73449 | 2025-03-02 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 091a0f2e-95ba-31de-8e9c-c154c1b8a659 | -13.9993 | -45.57004 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5407177-1837-3ece-ac5c-73f16b017f65 | -17.67225 | -54.16351 | 2025-03-02 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b91cccfd-e411-3a4e-b91f-9e1330301c35 | -13.9726 | -45.57822 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb965b7-fbc9-300b-bd79-c962562b236a | -13.97627 | -45.58274 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b6da82-0dce-3305-93de-38fd3d3c491f | -13.99774 | -45.58181 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2289a209-1930-345e-ae8f-534547875225 | -13.98046 | -45.58335 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce9546bf-7a58-3b97-91d7-19e2bc635656 | -13.98097 | -45.57944 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c7ee217-2dea-343b-9e20-02e8a42c4f85 | -14.0056 | -45.5869 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75b90fdc-0dcc-3bc8-bf05-37c779cd02b9 | -13.78908 | -44.33262 | 2025-03-02 04:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e922c81e-720a-38bf-8815-07cc8d6f964a | -14.00245 | -45.57847 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 546676ee-9280-356a-b3a1-cac4b471dce9 | -14.85529 | -46.7938 | 2025-03-02 04:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27bf3024-9aad-345b-bb91-5ae79ea3c3cc | -13.97576 | -45.58664 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5623ce0-e6a9-3e03-8f3e-bb2c50d07253 | -14.00088 | -45.59024 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 301e230e-8ae6-350b-b218-d9ce5947ff6f | -14.00297 | -45.57456 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c278a3a-31c8-31ea-b72f-17a81712eb55 | -14.00036 | -45.59415 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 024c1dd1-b4c0-36ed-a65b-c959c5c1904a | -13.97891 | -45.59504 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a0938df-d519-38e2-80d1-e8e35c00e830 | -17.67634 | -54.16028 | 2025-03-02 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0502070-16e5-3253-beae-903d9fe23362 | -14.00507 | -45.59082 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e71a9a00-0ba3-3d8a-b77c-851b0a3d606a | -14.00193 | -45.5824 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05c9ca5f-ebda-3b5f-a3cd-8290a81b9b29 | -13.97678 | -45.57883 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35928f80-a39d-3abc-a918-f4f47e92b912 | -14.00455 | -45.59473 | 2025-03-02 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3b8b718-684c-3cd9-9588-e146e73e076b | -17.67568 | -54.16418 | 2025-03-02 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 302147a4-69c6-32c5-9727-0c3b5769c68b | -15.85347 | -54.12401 | 2025-03-02 04:42:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 029cad1b-f7ba-363c-bd17-719e0613de10 | -12.85177 | -43.81905 | 2025-03-02 04:44:00 | AQUA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 69aa551c-753b-3eee-ae95-f22d20b625f1 | -23.3385 | -46.77256 | 2025-03-02 04:44:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9142910-81ec-3b56-b89d-ba8ae5150b8b | -22.99265 | -43.50973 | 2025-03-02 04:44:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b45091a9-733e-3759-ab1d-99ffd75e91a3 | -20.88426 | -54.79116 | 2025-03-02 04:44:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9819e54c-04d4-3d17-96b8-01789300ce01 | -22.83915 | -51.05726 | 2025-03-02 04:44:00 | NPP-375D | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3d56309-9b55-374e-b4fe-edb0e0c1ef19 | -20.91691 | -56.54279 | 2025-03-02 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9cf6e36-0ca9-33e5-9164-c56ade780ad8 | -22.65864 | -44.78039 | 2025-03-02 04:44:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ec272753-eba2-3725-9519-443f8535d761 | -22.65929 | -44.77422 | 2025-03-02 04:44:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4c70a51a-01a0-3499-9228-ca5a2b8bddc7 | -23.6889 | -51.84359 | 2025-03-02 04:44:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a09f473-bf56-332a-9782-be5da4bd432b | -20.39237 | -49.11343 | 2025-03-02 04:44:00 | NPP-375D | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4c8d625a-b651-32ed-ad1d-5efac53ed2a9 | -24.75165 | -48.87498 | 2025-03-02 04:44:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eeca0612-d047-3a91-b116-72c324bccb52 | -22.99805 | -43.51048 | 2025-03-02 04:44:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c86cbc61-a55b-3593-8c8c-09b02fd59554 | -24.24381 | -50.7405 | 2025-03-02 04:44:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 68f5d075-ce9b-3634-9639-36dbf38c0637 | -20.99677 | -51.79266 | 2025-03-02 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 84f6d11b-1bc2-3930-8147-567e9bcda0ad | -20.91864 | -56.54536 | 2025-03-02 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2cab95c7-3062-31af-8c79-b495d413e718 | -22.53925 | -48.8137 | 2025-03-02 04:44:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83e071f8-361f-34bf-b487-cb52135ad238 | -20.76225 | -46.76734 | 2025-03-02 04:44:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6c83c79e-fb44-387a-88d9-f47e332c78ed | -20.76514 | -46.77032 | 2025-03-02 04:44:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2644c0e-6b7f-3fc3-ade1-2ad7ec44585f | -22.32796 | -42.73856 | 2025-03-02 04:44:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ff234418-ee4b-37f6-9e54-907880273358 | -21.20713 | -48.55541 | 2025-03-02 04:44:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96832b10-9f41-3995-ae49-bf99e1fcaf73 | -20.88019 | -54.79443 | 2025-03-02 04:44:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d28b93af-32fe-3105-b8e0-353d52b55d0b | -20.91611 | -56.54733 | 2025-03-02 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c56af7c-6c9c-304f-a90c-4098635cfa15 | -20.47847 | -53.67475 | 2025-03-02 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a208d7f9-66c0-3da7-a8af-474c4db63f43 | -22.32233 | -42.73792 | 2025-03-02 04:44:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ca17c07c-8c35-37b2-b879-26e927f479f0 | -23.40304 | -46.5584 | 2025-03-02 04:44:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34e24fbd-5b4e-3a19-83b7-23367e6e0233 | 0.6646 | -60.30786 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ee19b7-f079-3fc4-8458-95a527d580e8 | 3.57529 | -60.17974 | 2025-03-02 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 091790fb-aedc-348b-849c-fae4f8c53fb5 | 4.30813 | -61.05286 | 2025-03-02 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aee07196-83a1-395e-a7cc-4f4273615b23 | 1.5889 | -59.96429 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 169967d4-9257-3c67-b914-fad4146fc9a3 | 3.00331 | -61.19505 | 2025-03-02 04:59:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc7a52ed-741f-35e0-9f15-8f592bf1fe63 | 1.42701 | -60.80325 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b322dcb-d32e-3ece-ba9c-6f56eb3881d5 | 2.00452 | -60.55859 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f065e3f-b01f-30b1-97f1-5475ee02ba46 | 1.31441 | -60.43252 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f8472907-c80f-3f0f-addc-583fb5b69170 | 0.9684 | -60.52487 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a561b50-ebac-36ca-8c4f-5643b36c4908 | 0.13411 | -60.4011 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c1ac79b-20b2-32c6-bb67-4b092a3275df | 0.9602 | -60.53059 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a3de35b-6c22-36ed-96fc-84c764c20efc | 0.85771 | -60.44835 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 259d3b4f-a6d3-3183-9c0d-0f521550edf3 | 3.90649 | -61.70618 | 2025-03-02 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 090aefe2-2800-318d-8082-5d83a00a78f3 | 0.97387 | -60.52723 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3ac63d-1b9c-36a2-af36-f9801f475d5d | 0.97014 | -60.53226 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fec1c71-02c3-3881-be00-57722801fd46 | 0.96906 | -60.52922 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fa9493f-d0d3-3129-b78a-af2267c545d0 | 3.84046 | -59.79136 | 2025-03-02 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceed3709-7a79-36a6-a4a3-428f2542250f | 1.03508 | -59.56711 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb110e43-d3f9-3d2f-bf04-103cd165394b | 0.96571 | -60.53291 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a123f198-1c91-3ce4-8cef-c5d9a64b55fc | 1.94216 | -60.3898 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b418e514-8a52-3157-ad32-ea0cdb2bd7e4 | 0.6981 | -59.96778 | 2025-03-02 04:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f408e608-bb9a-353a-93e9-671994cb2175 | 1.79128 | -60.66651 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c662b007-51b2-39bf-a642-d25194a483d3 | 2.18664 | -61.84832 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6162e682-3870-3891-9a01-ff164c809bb1 | 0.1391 | -60.40458 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5115db5d-8393-3f58-841b-eff453c83dff | 1.93775 | -60.39076 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9e2a5393-7bcf-3059-bcd4-0e709af9ae7b | 1.31553 | -60.06625 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b97f08b-cd12-3508-b765-a363d4719f7c | 0.13476 | -60.40525 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c33d09f-aa36-3e05-8aac-8b7935616c9f | 0.87586 | -60.24722 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
