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
| 522dbf58-5367-3c05-a174-f46e56897017 | -2.7553 | -52.633999 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1709e2-4af6-39ee-b743-f1c15c851a9b | -2.9684 | -49.091702 | 2024-11-18 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7439faa-9506-38ec-b987-a1ed74c529f5 | -10.5128 | -36.747799 | 2024-11-18 00:09:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7615fe6e-7e46-3d43-a2b9-50ad6298c4d9 | -5.6066 | -36.875 | 2024-11-18 00:09:00 | METOP-C | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 81a3db26-ed33-3e51-b8f1-4eeba6dd03e1 | -9.288 | -46.198502 | 2024-11-18 00:09:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac70520-60b2-3ca5-81a6-4bdf3c6acf6d | -4.3876 | -44.7206 | 2024-11-18 00:09:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4c6541-f37f-35d9-b7fc-0e4b2b758703 | -10.1134 | -36.366199 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3387ac1-20e5-3f7a-91dd-b7f2fbaa9e63 | -2.9725 | -49.1101 | 2024-11-18 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd9ec39-e998-3e2d-8fd5-556c3ea0d3c7 | -2.4096 | -45.7411 | 2024-11-18 00:09:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea8a417-8f04-399c-91c5-7176ae69b512 | -3.2675 | -43.761101 | 2024-11-18 00:09:00 | METOP-C | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 819a6c59-e3bf-3780-8980-16233fa7647b | -5.5618 | -46.4174 | 2024-11-18 00:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03c3cde4-1f18-3789-8508-494eaa31d634 | -5.2498 | -44.074501 | 2024-11-18 00:09:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 366f26c2-cc73-3884-a738-18734b6a91bd | -3.2266 | -45.5401 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b28a1705-761a-39a8-acc4-410b91583463 | -2.5683 | -51.707401 | 2024-11-18 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c3a5ae-199f-3df1-b238-6072260b11a2 | -2.6516 | -46.222 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98bd4c71-2f80-306c-9b92-3044efb6b593 | -2.6418 | -46.224098 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6ec06f0-f2c5-3de9-b2d0-0fef10f2d1ba | -4.9457 | -44.507401 | 2024-11-18 00:09:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90fc8fc8-2e6a-3749-bc5e-9be2a4cf37f7 | -3.157 | -46.6007 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 034fe151-3f82-39d1-b4c4-3ee855c4c2b0 | -5.9501 | -48.0653 | 2024-11-18 00:09:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82a1bcb4-2aed-3a7a-b349-9ed0cc97e764 | -5.4827 | -43.2757 | 2024-11-18 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6154f0e3-3e1c-3bd0-8af5-bb974522478a | -3.3436 | -45.604198 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6e69ff9-409b-378d-bde8-f27dd072716f | -2.6257 | -46.834801 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0004bb2e-9765-3c9a-9197-88e6e493ec5f | -5.3289 | -40.902802 | 2024-11-18 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d318ccf4-3676-3c45-a2b7-f7b0d619fcd4 | -2.7506 | -52.567902 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cde6912-267f-3a3b-846d-820d53db7e68 | -2.1688 | -46.4006 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d253b2bf-94ef-34a8-a2df-bd09c42b9038 | -5.9403 | -48.067299 | 2024-11-18 00:09:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e04c1088-2007-35f8-a29a-c70dc700195c | -7.7077 | -45.666599 | 2024-11-18 00:09:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1791363f-99e9-3cb3-96ef-b9daae1c7cd5 | -4.3454 | -45.865898 | 2024-11-18 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a82b872-0dab-3d12-bf5f-86f23bcaee4a | -3.2661 | -46.1731 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd19526-27a5-3c8a-978c-5da23dfac953 | -2.5621 | -51.679901 | 2024-11-18 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63cbd41e-2d1a-39ee-a18a-706cd9956d34 | -3.3179 | -45.9925 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9c0513d-4b95-3a6f-9ea5-2ee64c49fbf0 | -10.1115 | -36.358398 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2983b23e-156d-32d3-abd4-478b73b540c2 | -2.1138 | -45.3423 | 2024-11-18 00:09:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aea5bbc-d160-3d25-aeef-6d57389a38ee | -4.8154 | -44.474998 | 2024-11-18 00:09:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8be56527-681f-3bae-ba61-868295285b1c | -3.746 | -45.935398 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1724ef49-1cc8-3fb6-ac37-b586543c1395 | -3.038 | -44.338501 | 2024-11-18 00:09:00 | METOP-C | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15f3f550-2732-3138-a941-71dcf222f9cd | -3.3183 | -46.223202 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35a98ce8-54b6-37f0-a71c-c7a4da39e776 | -2.8537 | -51.762501 | 2024-11-18 00:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59a1a19-71d6-3b22-b49e-0964b0e87e0e | -3.1759 | -45.451698 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8baf482e-1975-3d99-943c-f9232d1a83cc | -4.9857 | -44.318001 | 2024-11-18 00:09:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 347e4d22-afe5-355c-a6df-1918ffab2ac7 | -3.3019 | -45.738499 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f16a7e2-453e-3bc5-90ec-87c5f0d0041f | -4.3479 | -45.877499 | 2024-11-18 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6a4879-3b6f-3a46-a5c2-8bfdc0d4c668 | -10.5111 | -36.740299 | 2024-11-18 00:09:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80800203-b50d-3765-8342-f1670e17efe1 | -2.8319 | -46.658501 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38de98ae-9aba-3177-8a57-aa8879bd56e0 | -2.5717 | -51.677799 | 2024-11-18 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac18ebc-34a6-3ea1-a034-c082b191bf61 | -10.1097 | -36.350601 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4fee4a0-9eb3-324b-a718-8fe17ad32621 | -6.1653 | -42.925598 | 2024-11-18 00:09:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4cb6be5d-4ba0-35d7-87cc-dd7698e4abda | -3.7485 | -45.9468 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca6b2ea-5f98-3172-ae68-79cc347c21e7 | -5.9463 | -48.048 | 2024-11-18 00:09:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e73b8bde-0a32-3776-bde2-67d6ad260d8e | -10.1036 | -36.368599 | 2024-11-18 00:09:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| baf2875e-f907-3da3-abd7-b0bfa2dcb842 | -6.7497 | -34.9902 | 2024-11-18 00:09:00 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 161ac10e-4abd-356a-ac72-d80ef958c5e8 | -4.559 | -45.628502 | 2024-11-18 00:09:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 296f8297-7f9c-3d7c-8d6a-cb87b40c3038 | -6.5288 | -35.188599 | 2024-11-18 00:09:00 | METOP-C | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48dd2510-3b61-3e6a-b6be-39c0f01cfa97 | -2.8221 | -46.660702 | 2024-11-18 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd95a18a-eb01-3552-b448-b7d3e7d92ec5 | -4.3898 | -44.7304 | 2024-11-18 00:09:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 878cbcbc-3339-3948-b920-850e773c82c7 | -4.676 | -41.1138 | 2024-11-18 00:09:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e70c118e-312e-31e9-b6a1-e11bbe5a6ca8 | -1.2715 | -51.708302 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c124b0-942b-30aa-8d88-aa322d92c4b9 | -5.3273 | -40.895901 | 2024-11-18 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7127f07c-15e5-3d3d-baa7-ac1c6a52149f | -5.5107 | -41.067501 | 2024-11-18 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18d77f6b-bcd6-3b1f-9d25-cabefd104b3d | -5.5647 | -46.430599 | 2024-11-18 00:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0311b2c6-523b-387f-ab4d-de020971c682 | -1.7506 | -45.688202 | 2024-11-18 00:09:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa3cd4e8-e083-31a9-bb10-09c8eeecbebc | -4.4896 | -46.377998 | 2024-11-18 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 397e063f-a520-3381-9db9-cb686493d022 | -6.7423 | -35.002499 | 2024-11-18 00:09:00 | METOP-C | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1722fcec-0522-3d16-bc19-9d14de872917 | -5.5025 | -41.076801 | 2024-11-18 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c18ddce9-6262-3cce-8123-f8b9bfee9853 | -7.393 | -42.762402 | 2024-11-18 00:09:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c8c1ecd-8533-3dfe-b21f-6ce950cd56ec | -4.1563 | -43.916901 | 2024-11-18 00:09:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 537b7260-c076-3dbf-9c57-0f1975a3c9b2 | -7.0965 | -39.293598 | 2024-11-18 00:09:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 18322939-5747-3f58-8d18-50071118f271 | -6.3928 | -44.7444 | 2024-11-18 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1d10e3-ca32-3ca6-8e65-ea27d66a75b3 | -1.2908 | -51.704102 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3821e99e-30db-3733-8d76-849ec53470a2 | -6.3294 | -39.6828 | 2024-11-18 00:09:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b3bfbebc-506e-3a93-9241-e72f71dd94b7 | -5.6732 | -42.702099 | 2024-11-18 00:09:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba8872fe-1891-3e69-a580-38c2c6f3c18f | -4.0355 | -45.487598 | 2024-11-18 00:09:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c03b6d4-3484-3c37-ac37-7bc077395ee9 | -9.0749 | -40.5196 | 2024-11-18 00:09:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2d1c6591-f13b-3cab-b051-d6f366117521 | -3.1668 | -46.598598 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffb81539-9b8a-3b4d-b554-e15916ccfb78 | -3.2635 | -46.1614 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ced1aeac-60da-35de-8c84-64251262a36e | -1.2811 | -51.7062 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 757e853e-44ff-3539-99d7-4b6f1a8cea90 | -2.4617 | -45.608101 | 2024-11-18 00:09:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44068bf2-3ff4-303d-a7dd-6da8569ab1a4 | -2.1635 | -46.377399 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca712788-05cf-3fcb-b1c4-26bb8c972243 | -2.6706 | -46.169701 | 2024-11-18 00:09:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e15014c-29bb-3ac3-8349-34ad47ed0370 | -7.6479 | -35.335999 | 2024-11-18 00:09:00 | METOP-C | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b1041db6-dd66-377b-9212-9350660623ca | -4.7745 | -46.463299 | 2024-11-18 00:09:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc88d5e0-e1b4-34ed-9fbd-d7126aff5c39 | -4.2017 | -44.027401 | 2024-11-18 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6692d9db-e4c7-33dd-9247-1b64ccc25268 | -3.323 | -46.015301 | 2024-11-18 00:09:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9e9ad7c-3f35-3648-8f2c-720250a54546 | -1.8925 | -46.4491 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447d9de1-6c2d-33cb-ae3e-e196e2218b0d | -4.8021 | -42.215801 | 2024-11-18 00:09:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf161a3f-370a-3559-8ab5-d993d427bcdc | -3.1834 | -45.439201 | 2024-11-18 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68fb6b33-41c5-3708-9d43-e3dbca3585eb | -8.8748 | -40.821499 | 2024-11-18 00:09:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6ecbf031-0340-3578-a181-cced19f53949 | -4.9878 | -44.327499 | 2024-11-18 00:09:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0a147d-2ec6-3784-8bd9-9756ebf706d7 | -6.3905 | -44.733898 | 2024-11-18 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47db387f-fc16-3b12-9d00-8514e611387c | -2.2211 | -46.4505 | 2024-11-18 00:09:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7b021e-4303-3f2e-b548-1c73704ccb54 | -5.1334 | -44.335701 | 2024-11-18 00:09:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f0d73c7-6a8d-3edb-a501-ccba357120f8 | -5.1355 | -44.3452 | 2024-11-18 00:09:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8782caae-4276-3ff7-b59f-7659ded42e5a | -7.705 | -45.653999 | 2024-11-18 00:09:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 868689f9-2a02-3282-bdd8-39a7568d8eb6 | -2.6685 | -46.2062 | 2024-11-18 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd161eba-c461-34f1-82ec-69ee0eccf439 | -7.6501 | -35.3452 | 2024-11-18 00:09:00 | METOP-C | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6aa696f2-6447-33fe-83c4-1c3c6c53d8cb | -3.7861 | -46.023399 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7d9d83-7d42-359c-9a38-82ccb30190ef | -7.052 | -35.2183 | 2024-11-18 00:09:00 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bcfd218-414d-336b-9937-6c46d66d72ac | -1.2968 | -51.7304 | 2024-11-18 00:09:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffce9c4a-049a-3b31-ad0e-51a2d9bead73 | -3.7558 | -45.9333 | 2024-11-18 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d158f8b-4ea6-3966-b53e-f5cd3f38439d | -2.7314 | -52.572102 | 2024-11-18 00:09:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
