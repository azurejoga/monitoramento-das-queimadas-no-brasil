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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1219c286-8733-36e4-8d1d-8d75ba9b4abb | -3.39243 | -52.48512 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| df74b383-3903-3a11-ae41-9d56c752f83a | -4.7575 | -44.3367 | 2024-11-21 00:26:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39505c54-61e9-3202-8774-cb970b195bd8 | -4.08825 | -46.47245 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1031f974-1e10-3273-8ac1-de16d782e6d7 | -2.34735 | -45.67676 | 2024-11-21 00:26:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 1009c140-82b7-35d2-9da9-380bad82d2ee | -2.24218 | -46.82325 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 95a2de4b-5dd8-3454-a915-c8d2dfcf2014 | -5.62492 | -43.95502 | 2024-11-21 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 98150bc3-fe26-313f-803e-2a8e012ca4b3 | -4.18495 | -43.93764 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb5137b6-3f7d-38a1-923c-a647d84dcb26 | -4.58344 | -48.02731 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 246.4 |
| 8c9287e9-2f9a-3f48-9463-e01d547b9158 | -3.36608 | -50.189 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 7a9b2044-351f-3e65-94d0-5f504487b9d4 | -5.45102 | -43.23568 | 2024-11-21 00:26:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d05deb39-6976-3f1f-b633-b96b843768d5 | -7.3331 | -46.39123 | 2024-11-21 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c61f3c08-fdf5-3d74-8a10-724c17af20b4 | -4.39016 | -45.59479 | 2024-11-21 00:26:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| dbde4401-efba-3ba9-942e-3a6aa3e37565 | -3.25098 | -50.56727 | 2024-11-21 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| cdc7ee39-d3a6-3591-8228-8de1b5f3a7c9 | -6.89313 | -42.47073 | 2024-11-21 00:26:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d0141c25-f12f-3ab1-bec7-e74e0b8dbebb | -2.76684 | -52.12084 | 2024-11-21 00:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 214.9 |
| ac4b4f09-bd27-3644-bf60-aca1f62823d2 | -4.16081 | -42.02696 | 2024-11-21 00:26:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 5b4d0473-d303-37ca-be16-686cf4f18ca3 | -2.85657 | -45.82714 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dc137782-f221-3006-a527-d020f567f177 | -6.66063 | -39.24357 | 2024-11-21 00:26:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 828a2afe-f3d8-3098-9559-73b4c8b3d20a | -5.24146 | -42.64444 | 2024-11-21 00:26:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cec0d54b-01d0-3027-9d1b-b150ea0a15c1 | -3.35367 | -49.50748 | 2024-11-21 00:26:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8fe7f8f5-1b68-308e-9622-2cec10763f87 | -2.89934 | -40.38138 | 2024-11-21 00:26:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 694d1266-8be9-324b-adbb-3d89c8ceac66 | -6.30195 | -45.34157 | 2024-11-21 00:26:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9524a577-96f0-3361-8294-c22e6de27267 | -3.46306 | -50.00622 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| ea172295-3ae8-3d97-8215-426e7ca1dad4 | -5.49473 | -43.95808 | 2024-11-21 00:26:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8f38740-176b-3f98-9b4b-77a58f3c209d | -3.3003 | -49.20473 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e001d8e5-613c-35fa-a8ca-e238cd101849 | -6.18404 | -43.40555 | 2024-11-21 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 23a40e5f-b9c9-3022-bf9d-a2b1de6aba09 | -4.13753 | -47.74065 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2b83000a-5843-38d3-97e2-ef7f0501e1ef | -4.372 | -46.09849 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 08700317-849b-3233-aa44-24e0a501780c | -2.69236 | -46.25436 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8d3df8ea-4514-35f4-96e9-cbeec61891ba | -1.04197 | -51.74633 | 2024-11-21 00:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6752bc1c-67a3-3fca-8b04-e39987c91651 | -5.00541 | -44.80007 | 2024-11-21 00:26:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 22ada547-515d-374c-b396-ed3052159ccd | -2.45503 | -47.03183 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| cd3f161e-662e-3ddd-95e2-83360c30da21 | -4.07818 | -49.29482 | 2024-11-21 00:26:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| fbf3f834-a41e-3d52-a21b-8b65d9512671 | -4.50797 | -47.94136 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d03f33e2-8f46-3daa-9a88-3b806c548c3e | -3.39211 | -52.48973 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| aff16c30-411d-3816-9ac0-8737cf1069f8 | -3.75579 | -45.96957 | 2024-11-21 00:26:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a84b1b8b-a1d8-37d4-b1b4-750cfcd0eafb | -6.82851 | -46.76875 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 97e91b61-4d8c-3751-a20a-f4f18c6bde02 | -4.72631 | -43.25109 | 2024-11-21 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c78cf944-2498-3411-9513-1888abfc977d | -4.15958 | -42.01814 | 2024-11-21 00:26:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 65dc8864-b030-3d5e-bb1f-a0d4462304ce | -3.2482 | -50.56109 | 2024-11-21 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 976ece43-6260-32ad-a730-fca603151429 | -4.31622 | -48.08168 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 663e2869-4972-3f7e-a2da-39d7271f1c3e | -5.44848 | -45.58464 | 2024-11-21 00:26:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b79cf67a-d971-3921-81f1-5969ee9d2dfd | -3.00036 | -51.3132 | 2024-11-21 00:26:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 79caa176-d092-3384-b2b0-1c8c7668d7c6 | -5.95281 | -44.23862 | 2024-11-21 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3c37061a-4c1a-3b6e-a12a-5a5a0caf0dd7 | -6.8246 | -46.79198 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 524557dd-526f-3d9d-b085-c1d2cb7a39bd | -5.08262 | -47.94504 | 2024-11-21 00:26:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| cc2ca6ee-a653-37b9-b67e-b683d1e7abb2 | -5.41364 | -46.43938 | 2024-11-21 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 23a9f102-0b21-3ddf-b19e-4a012484d98b | -3.27749 | -50.21313 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| ab8b80ee-f60d-341d-bb4e-e31d4eb2b53a | -4.47927 | -44.75493 | 2024-11-21 00:26:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 28364bce-a42e-3512-9b6a-93cf5affd1ed | -7.40371 | -42.76807 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7b3f80e0-63c5-32b5-8afb-5185fb7cbb49 | -4.51671 | -45.25668 | 2024-11-21 00:26:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a5db4ca8-2f9b-3e13-8f93-95fb60cb522b | -3.74008 | -45.85431 | 2024-11-21 00:26:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 572a161f-f723-35b2-b0ef-27a0f950af47 | -3.46059 | -43.41788 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a7977439-f424-3403-b34f-3fb865ba092d | -3.78041 | -44.06497 | 2024-11-21 00:26:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 21aa72c4-96c4-386a-aaf3-88d105d7f978 | -4.50448 | -47.92908 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8f791a3b-ae65-38ec-aa14-6d6d190b062d | -3.29018 | -49.18847 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 87bebf0c-aa12-3b68-86b1-0819ae84c1d4 | -6.63877 | -47.34529 | 2024-11-21 00:26:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1cf5a1b8-34e0-3ad2-bbc4-e247693f4c9c | -3.47094 | -43.4259 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1aed39e6-ddfe-3062-a2f8-6d4e4e937c58 | -3.27568 | -48.80703 | 2024-11-21 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 79d6bb37-9421-3931-ba64-8b6abf525166 | -4.24377 | -46.10067 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 75fbd6ea-3382-33d2-89e3-ff91cc7a6c96 | -2.89214 | -46.7 | 2024-11-21 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 465fa353-084b-3efb-9892-beb7d889b28e | -4.39755 | -47.72396 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0714d724-88c4-3e56-889c-3fc9b6e4bc5b | -6.21425 | -44.83088 | 2024-11-21 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5a06bd1-4e25-3f94-8bdb-8fe934adab47 | -7.33144 | -46.40207 | 2024-11-21 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5749b367-9530-34a9-a55a-e4b4149568c5 | -5.10124 | -43.16478 | 2024-11-21 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 15517c50-bfa4-3839-b694-5535cadea2f0 | -2.64276 | -46.20793 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b937cf8f-d37a-3dae-84de-d705f188dbe8 | -6.65151 | -41.98978 | 2024-11-21 00:26:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 04ab214a-9ec6-31fe-8125-9c775285d18d | -3.12392 | -45.07839 | 2024-11-21 00:26:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 63abf0a1-4d10-31b2-9d13-31a2d34dada4 | -4.14059 | -47.73396 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 00266f74-b628-35bb-a9c7-6dc56572c4b1 | -2.32542 | -45.66777 | 2024-11-21 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e1797545-efbd-35e3-9324-3d86dcf962de | -4.99925 | -45.28765 | 2024-11-21 00:26:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a7f8d4f7-02ca-3276-82e8-899b78552e0a | -3.81022 | -52.36457 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 64705723-d430-3a0b-9ab6-83fbf8bbd049 | -3.36638 | -50.19577 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 4e4aa03f-c34a-34ff-9409-95a63a543dc7 | -6.82237 | -46.77513 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 91143e66-65f7-3ec6-98d8-e7f9a20a39d5 | -4.43693 | -48.29992 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0c7e4bc3-5938-3478-96c2-3e148e91ecc9 | -3.30047 | -50.37902 | 2024-11-21 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e2114409-d39c-3ce5-8f7b-d0c4f2167977 | -1.73963 | -52.06814 | 2024-11-21 00:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 874d7e98-93ce-3a07-81fd-81b6a6fc57f2 | -2.85431 | -46.68269 | 2024-11-21 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5d4c3d3d-0065-383a-a78d-58747ea2bc08 | -5.72104 | -44.80381 | 2024-11-21 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5ef50f2-653b-339b-97c6-384449506610 | -3.45933 | -43.40862 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a28e5f3e-d165-3ae5-834e-76df2cf58946 | -3.38653 | -52.4488 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 196.6 |
| eb800221-de29-3510-a731-dfe529842102 | -2.9334 | -43.13578 | 2024-11-21 00:26:00 | TERRA_M-M | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d98ddef3-7b51-367a-9f12-2c7c0d718780 | -5.94371 | -46.19775 | 2024-11-21 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9403a2fa-dc36-327d-b6c6-5e2f96ae15b0 | -3.36949 | -52.44581 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 536d9e26-296c-3314-858a-ef7abd1307f1 | -4.25375 | -49.08709 | 2024-11-21 00:26:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b43a7065-a7c7-3f77-804f-6e0140bfdd19 | -3.17525 | -44.02504 | 2024-11-21 00:26:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5093042b-c877-33fe-8986-119bc3c5b211 | -1.96427 | -48.38657 | 2024-11-21 00:26:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ebcf7ef6-6bd4-357e-9880-5865e1fdb0de | -4.3404 | -46.13624 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| adfaa8b1-eec1-3f70-b49b-a5c0610f3331 | -3.29935 | -50.37413 | 2024-11-21 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| faccdf2e-d6ef-38ea-8435-e166524df587 | -4.55556 | -48.01138 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 6f4cfb47-587f-312f-ada0-2fdc87413baa | -4.25045 | -43.81242 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 201e5996-8904-33a1-a984-9caddc849006 | -3.80863 | -47.8036 | 2024-11-21 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7779f326-dcda-3bb0-93fa-f8c11afbd507 | -4.10594 | -43.82463 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d03cc44-c0d2-34e4-a1b5-a6a35a5da113 | -1.23719 | -47.35577 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8819483f-d528-35c7-a335-b5dd9991de51 | -3.24099 | -45.5652 | 2024-11-21 00:26:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1bf3194f-7917-302c-b5f0-f627d9a2bad3 | -2.56836 | -45.20863 | 2024-11-21 00:26:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 39ba51f5-6571-3f34-a038-66ab07a1d5ff | -6.57469 | -47.87179 | 2024-11-21 00:26:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d74fb45d-6b7c-3041-b4c1-5778f1709d06 | -3.12202 | -45.44321 | 2024-11-21 00:26:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7cbb8abb-6f1a-3654-b002-634adcaa0982 | -4.48075 | -44.76597 | 2024-11-21 00:26:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f99aed40-8ac9-3615-a710-636f5008c34f | -3.23241 | -45.57856 | 2024-11-21 00:26:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |


[Clique aqui para ver as próximas entradas](README4.md)
