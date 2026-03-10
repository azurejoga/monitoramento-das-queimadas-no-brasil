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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6713250a-6109-32d0-8a18-31ca6ff3688e | -11.58031 | -38.25156 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15aa88df-6ef4-36d3-b79c-8ceba4098bc1 | -11.57634 | -38.25089 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a529531d-bfef-350a-bcde-90f79b17e597 | -9.5732 | -40.59668 | 2026-03-10 03:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16c9e420-9a58-31cc-bc12-2741c3a09df4 | -15.72775 | -41.43922 | 2026-03-10 03:34:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d50a5685-7573-3792-928e-895473933993 | -12.27472 | -43.50028 | 2026-03-10 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc6e1842-ebbb-3d7a-8014-6c8a7ed8fd81 | -16.05856 | -42.48522 | 2026-03-10 03:34:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b72d0b6-2156-3eb3-b375-a574168e6386 | -15.7323 | -41.44007 | 2026-03-10 03:34:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1d374fcf-3aa5-3087-a3d2-a49498f1d993 | -16.06132 | -42.48781 | 2026-03-10 03:34:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c11a77-b1b5-308a-ba97-9865ec717840 | -16.0564 | -42.48722 | 2026-03-10 03:34:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a02eeadb-3e21-38b8-92a5-1ad9d94c6907 | -12.27567 | -43.50135 | 2026-03-10 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52eae60b-d71b-3c53-a4e1-b4fda10543cf | 2.7267 | -60.3726 | 2026-03-10 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1eb96ef3-5090-3f5e-bd31-38af6212607d | 2.7085 | -60.3729 | 2026-03-10 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c6b8327a-fef5-331b-836e-cf169e1991ac | 2.7267 | -60.3726 | 2026-03-10 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c0577ad2-370d-326d-b5a8-b1ab80ee9925 | 2.7085 | -60.3729 | 2026-03-10 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b7834861-7baa-30b6-a45d-a1cafbcc11d9 | -5.05315 | -37.41504 | 2026-03-10 04:19:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9798334-4a09-342a-b14b-6b6c776f13c7 | 2.7267 | -60.3726 | 2026-03-10 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 07b6e6f8-ef56-344c-a464-4a426ba0cdde | 2.7085 | -60.3729 | 2026-03-10 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e6b80e33-28d1-3071-a029-762334a0e28d | -10.74437 | -38.78929 | 2026-03-10 04:21:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b3e97c3-baa9-3291-bb02-029ce28ba9b9 | -13.55921 | -44.68736 | 2026-03-10 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5bd47eb-335a-385d-ae3d-8f9dec6b0729 | -12.24449 | -44.19764 | 2026-03-10 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68532477-d6a3-3ebc-9664-157283797a02 | -8.38832 | -44.06543 | 2026-03-10 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4125a214-9c08-362b-8022-491125c8c244 | -8.39221 | -44.0624 | 2026-03-10 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 542d4acc-1350-3a6e-843b-f8ab9ddbf8ab | -10.20848 | -36.24025 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a23a2ecb-fd18-33ed-bcdb-c6b814d02c1b | -10.20309 | -36.23953 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b8c7539d-7b55-3f39-9c56-e921514412ff | -10.20804 | -36.24376 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91a7b7db-4349-35e8-863b-4de6f1fa5cbb | -10.06011 | -36.267 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 67e5c5fb-9e7a-3870-9093-ec2d6c391ffe | -10.06253 | -36.2655 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c2702f93-7706-32d2-87ed-423ac190f036 | -8.44365 | -45.13014 | 2026-03-10 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55e5c4e2-c16c-3edc-a931-92fd429b32ff | -10.74498 | -38.78477 | 2026-03-10 04:21:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db7cd1a5-b8ca-3cc4-a508-35b89a2cbca6 | -12.27512 | -43.49954 | 2026-03-10 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20591a17-8043-32b8-baa0-cf2823adb317 | -9.57458 | -40.59719 | 2026-03-10 04:21:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad7afa49-93b4-3af9-ab46-9b1d9dd1c1bb | -10.06208 | -36.26892 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c80da91-33c9-3ead-98ac-210ddfc73199 | -11.57797 | -38.24812 | 2026-03-10 04:21:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 37d94dcc-3ed2-3488-922d-42ad66006e8e | -13.55866 | -44.69108 | 2026-03-10 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0dfd012-5297-3472-83e9-bfe503c1a704 | -10.20265 | -36.24302 | 2026-03-10 04:21:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 867d899e-5a37-33d1-9d9f-c6cd002cc116 | -17.96736 | -45.38438 | 2026-03-10 04:23:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9761d35d-a17a-31cf-897d-955771ce9769 | -15.73356 | -41.44173 | 2026-03-10 04:23:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c6b5e4b3-d66b-3f7f-8046-fc1e9d8082ad | -14.92104 | -47.12609 | 2026-03-10 04:23:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.0 |
| fcc77f84-20b7-3a68-b093-44040a4462dc | -15.28894 | -43.0621 | 2026-03-10 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9690d60a-9267-3e23-99f9-eb7175ffa64f | -15.28717 | -43.06474 | 2026-03-10 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.6 |
| cc114bd7-6960-3b40-9235-4d098a1d1360 | -16.06096 | -42.48251 | 2026-03-10 04:23:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 367b94d8-301a-36f6-83b5-690821ec97de | -15.72994 | -41.43739 | 2026-03-10 04:23:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c41c3a1f-10d4-364e-a7e1-814cffc80455 | -15.28829 | -43.06661 | 2026-03-10 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b61a9d8d-a472-3dd6-8c92-78e8e609ce06 | -16.06031 | -42.48734 | 2026-03-10 04:23:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac4bb63-a1ca-352f-ad5f-f6f99e271e80 | -15.28459 | -43.06607 | 2026-03-10 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fa7a920c-1124-3c0a-8b06-0a98ac5958f4 | -15.28524 | -43.06156 | 2026-03-10 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b485fb66-f56c-32bd-bcd8-19573b098c49 | -26.67339 | -49.77182 | 2026-03-10 04:25:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| cb06cdd8-e8b7-32a9-b164-db24a1efe636 | -26.66948 | -49.77504 | 2026-03-10 04:25:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 45205de2-e6ec-39aa-b78d-e57e44257fee | 2.7267 | -60.3726 | 2026-03-10 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| af8d4104-bfe7-3072-9cc2-94bdefe72d26 | 2.7085 | -60.3729 | 2026-03-10 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f7a33fc3-1c11-3c2e-aa24-b6cc5cb64741 | 2.7268 | -60.3536 | 2026-03-10 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8bcd7e47-dcf6-3e46-af95-75323c853e90 | 2.7267 | -60.3726 | 2026-03-10 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ffb9d2fc-d329-36ba-8314-d306971710a2 | 2.7085 | -60.3729 | 2026-03-10 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ac4645a2-0fb1-3126-b8c0-2e01f1a34529 | 2.72073 | -60.37987 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 144798c9-8e6e-3ba0-b15b-0330b15e05fe | 2.73171 | -60.36834 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73c276e2-9f19-3a1e-a526-83779577ef29 | 2.73096 | -60.36346 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5be83ee9-a34d-3181-a3c5-0e3f05fadd76 | 2.72698 | -60.37902 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d6ccc034-bbcc-396d-ae64-74d3776f1dfb | 2.72357 | -60.37344 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f2dbd1b-a741-36fc-a74d-c5d9472dd54d | 2.72287 | -60.3686 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 00c0f6e2-3967-38c1-ba90-580ef7cc7891 | 2.72838 | -60.36277 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d17ea3fb-d22b-3769-892b-5ea9c1ceaa95 | 2.71876 | -60.38412 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a293c643-3f8b-32ba-9159-d710ac9c890e | 2.70594 | -60.25312 | 2026-03-10 04:51:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 693f7335-6060-322e-847d-c08deef59ca9 | 2.72909 | -60.36764 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9eb1b666-ed84-3bb6-9514-8c24c2f3cfc7 | 2.67346 | -60.62037 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 177e11bc-1639-3e9d-ae21-8435ef69f14a | 2.72623 | -60.37415 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6dc9bde4-9e67-39dc-8877-d083c9fcaa34 | 2.66713 | -60.62134 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89674f28-dae0-309d-8b64-0873c7191795 | 2.70701 | -60.2493 | 2026-03-10 04:51:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76862456-e3b9-347a-9bb4-3b3c368a6344 | 2.72148 | -60.38477 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 74786c46-1ac8-3f56-99af-9ceba8bdd926 | 2.70524 | -60.24831 | 2026-03-10 04:51:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c04d9fac-dac6-39e1-9bb4-0a8d92c65ec6 | 2.72981 | -60.37251 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4bab9ae1-5cee-3c8c-863f-f0f2b1d949f1 | 2.72474 | -60.36446 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 125c4da4-d5af-3eca-9cf9-5ef8bffde4dd | 2.72429 | -60.3783 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3e287311-0438-3a75-b94f-4b1bddc873bb | 2.72548 | -60.3693 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cafa65e7-3348-3a0f-a54b-8a99aca79ef7 | 2.71734 | -60.37439 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67659a4a-f4fd-37c4-a44b-bd2d37f27dfe | 2.71925 | -60.37024 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 09a5a207-43be-3076-a4a9-de58db458720 | 2.71525 | -60.38574 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb8f5541-8f77-3825-83c5-83f98ce2e22b | 2.725 | -60.38317 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b3178585-9091-344c-b0ac-84871ab91a4f | 2.71999 | -60.37505 | 2026-03-10 04:51:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8cfbd7ee-0991-38cd-96cd-f465bdce2613 | -9.477 | -46.09136 | 2026-03-10 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1815c55f-9389-3b60-9df2-0ed41def1759 | -9.46969 | -46.08236 | 2026-03-10 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95e5b292-8b94-394a-9ef5-698ce5c9a1b9 | -9.47278 | -46.0908 | 2026-03-10 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 282b5a36-576c-3099-b0ca-45854058138a | -9.46914 | -46.08628 | 2026-03-10 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac7c04e3-37b2-32b4-a5bb-bf9bc109b368 | -9.4739 | -46.08296 | 2026-03-10 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b95bae01-7807-30a9-ad89-f896d0b85e5a | -15.27949 | -43.06234 | 2026-03-10 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d36ae943-781f-3fa6-8a20-ae620b965cf4 | -15.27907 | -43.06615 | 2026-03-10 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b05df37-3c09-3e6b-941b-5e6dcfb6ec75 | -15.2851 | -43.06296 | 2026-03-10 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1392c1f-0e3d-3012-bbbc-37010a519144 | -15.28468 | -43.06675 | 2026-03-10 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9027e584-759c-383f-9a83-f136ddb05fea | -28.91881 | -51.33439 | 2026-03-10 04:57:00 | NPP-375D | ANTÔNIO PRADO | RIO GRANDE DO SUL | Brasil | 4300802 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63dd0a5d-c92a-3665-b144-63ccb8ae6630 | 2.7267 | -60.3726 | 2026-03-10 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6f919dc6-1dd5-3837-9554-9048bdfb5160 | 2.7085 | -60.3729 | 2026-03-10 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8534aebc-d8c4-38b0-9978-e554fe332e8b | 2.7267 | -60.3726 | 2026-03-10 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9d4e6f4e-deee-3adb-a064-be23b6969c7e | 2.98921 | -60.01933 | 2026-03-10 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d44a49c-c1b8-3d1c-a2b9-f908b2ae1733 | 4.37512 | -60.89122 | 2026-03-10 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05d209c9-0ce4-377e-89c9-65a3ed2e56e8 | 4.37453 | -60.88734 | 2026-03-10 05:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5db86b0-f96f-377d-9c82-39d785655a0f | 2.6129 | -60.58601 | 2026-03-10 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7168dc05-132a-3efe-b404-c94941e74257 | 2.71571 | -60.38337 | 2026-03-10 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0c6476e7-6c1a-38bb-9414-fc5a51861651 | 2.72266 | -60.37519 | 2026-03-10 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65fa4743-bd9e-326b-98cc-30cd4123bec7 | 2.7117 | -60.384 | 2026-03-10 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4b2271e9-9d6f-321d-95a3-21a07becb1f4 | 2.60885 | -60.58665 | 2026-03-10 05:10:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e15491a4-87fa-371f-84e1-fa3412773a23 | 3.37129 | -60.20793 | 2026-03-10 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
