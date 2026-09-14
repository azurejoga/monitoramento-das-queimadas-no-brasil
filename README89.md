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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c30ff1-a9a1-3d86-be08-9241bd7bc1c5 | -7.16046 | -42.1025 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 283118bf-5803-37e2-ac4d-5bee380c0547 | -7.47126 | -45.97002 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bd6cb4ad-f4b4-311b-923f-6fded89f3d3f | -6.62241 | -41.67937 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ee5e1489-32d5-3c66-9d3b-ff86c51e2791 | -7.09362 | -42.12161 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 93bd333c-8048-338d-9612-c9d02a7c9299 | -8.96824 | -44.38989 | 2026-09-14 15:48:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 54681042-2054-3337-925a-f21c24bfa3bd | -3.36401 | -39.13242 | 2026-09-14 15:48:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f4675eb-5daa-35ce-9f0d-4d564bc443ea | -6.62419 | -41.67988 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ffc208cb-df18-3868-b33d-b0d4b12a6102 | -7.16621 | -42.10514 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2d29219b-32c9-344e-89a6-5990617d98aa | -4.61926 | -41.39311 | 2026-09-14 15:48:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 911b2447-2f97-354a-adf4-33e38e8efdd0 | -3.61233 | -38.95727 | 2026-09-14 15:48:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ef004241-cb0a-33ed-b92f-e66cacc17dab | -5.41061 | -42.21935 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a44df209-6985-31bf-a53f-dc67a52cb28b | -6.15864 | -45.18462 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 44883822-36a2-367a-b429-9f6edd2e8d36 | -5.41493 | -42.22247 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9fd624fe-e8db-3c14-9643-335da1b1b070 | -5.81832 | -42.73731 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0f7d2737-80e0-3a2e-b066-ca750c1bc007 | -8.80367 | -45.89373 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dbc45f33-3c8a-31fd-a1ee-e1ab5de14671 | -9.86055 | -46.00013 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 20710777-d0c8-3fbc-942e-e4487410a345 | -3.74156 | -40.39597 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ad661f70-244d-3714-9b8a-af31525d710f | -6.66417 | -43.65321 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5381ca84-16a7-3bf6-9901-e77d4b099e8d | -8.21249 | -43.79215 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8acdce78-4e58-3078-bba7-69c200b86778 | -7.11969 | -41.8026 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f1701def-ae3a-394f-bc7f-9fd2653f8352 | -6.32876 | -44.17803 | 2026-09-14 15:48:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a1e670fe-762f-3632-8d47-c24044e9ee39 | -7.10116 | -41.78248 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 825558ff-b7e7-33e5-bfff-9135342f1a5a | -9.22498 | -44.80362 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28d7784f-900b-39d5-aea6-c763874ec756 | -8.49121 | -44.57755 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6389a24b-b014-3a32-9282-6a78d6f8ce9b | -7.32957 | -41.43045 | 2026-09-14 15:48:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 135250ad-ce6d-31c5-b64a-188d459ff153 | -6.26425 | -42.66969 | 2026-09-14 15:48:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a8a864cb-2b40-3bc0-b9f4-47e53b461992 | -6.24361 | -45.96106 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eb9024bc-b0a5-3580-8633-b8646310d2e3 | -5.41538 | -42.22556 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 774d84fd-4d52-3db8-abc6-259d73947806 | -3.93331 | -42.99004 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 007be7dd-7957-33e5-ba0d-e41b2df70e4f | -7.10192 | -42.10385 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 78819cb6-2361-3ae4-af71-4fa2f64b076d | -8.42478 | -44.75652 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 90ce4148-8a31-3881-9181-6d79b7518556 | -8.36201 | -44.82488 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a7322e15-8696-38ef-8ac6-216e2a4a1f9f | -5.81316 | -38.31904 | 2026-09-14 15:48:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 080c1082-d281-3be8-bac6-f5dcf70fdad0 | -8.83044 | -45.88451 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f43eaeb7-ac83-30d4-8bcf-779f6195bea6 | -8.58879 | -44.48697 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c82889da-3d13-3739-84fe-e04ce2a593a7 | -6.42232 | -41.55567 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 718c8617-445d-343a-9c07-41690cba82ca | -7.56407 | -41.84393 | 2026-09-14 15:48:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1ac21669-bed5-33fc-802b-36c00377a45d | -6.57893 | -45.31393 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4f709938-f0e8-3dd6-8f8a-1d93a321621b | -7.15739 | -42.11962 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7340e47d-304d-34da-a09e-d2c5c34c8d1f | -6.70448 | -43.14721 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a2746ef-3c7b-391e-863d-5ee0b91020fe | -3.96144 | -43.11067 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9f575479-bd0f-366d-a6bd-206d674ee205 | -7.02091 | -44.62658 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 14fa256c-c358-365f-982e-166b2e481090 | -8.05044 | -43.75896 | 2026-09-14 15:48:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 79ea5b34-1735-3d38-aabf-2b91504630ef | -3.66404 | -40.56842 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c33aa363-145a-3e63-9667-cc68d73400b9 | -9.84508 | -45.98908 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc24a827-983e-36a3-9c0d-19cb8ce5843c | -9.59192 | -41.69677 | 2026-09-14 15:48:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a8675c40-a792-3b65-b11b-a6a1694f1b20 | -6.70398 | -43.1434 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c66d975-eb88-3f05-8f24-87a20e209106 | -8.41779 | -44.75264 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8535895-3957-3c03-a031-51d8905a5dc4 | -8.30859 | -36.31065 | 2026-09-14 15:48:00 | NOAA-20 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 155330fe-6633-3a55-8ee3-4f4b00a6da3d | -5.09161 | -42.8946 | 2026-09-14 15:48:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55560ae4-7372-3a71-8def-93eba0b5d3f8 | -8.23268 | -36.66542 | 2026-09-14 15:48:00 | NOAA-20 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bb10f20e-aad4-3ac5-b947-e1a82a7870bc | -7.08654 | -43.53839 | 2026-09-14 15:48:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3610fa7e-f126-3c6b-bd6d-5befe6685639 | -7.4905 | -44.88491 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 269776d3-8a84-3cc6-9a3a-2a0b524a1216 | -7.0964 | -41.78624 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 6d13ee54-ae94-3b70-a7af-432da530f840 | -6.6334 | -45.12749 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7bbc0279-9c9f-3928-b259-de4956f2f6a5 | -8.83718 | -45.88255 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0f97c71a-c45e-3e1b-a474-63c9b02e6357 | -8.12024 | -44.0549 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efe7d569-0d5b-3188-a2f9-85b0820b7dd3 | -6.66391 | -43.65093 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f3e777a-6f33-3f35-8b6a-c40174eebe70 | -5.41448 | -42.21936 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 72e7298e-6f2d-3c46-b513-6d5464d1cadb | -7.1986 | -46.13822 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f3aa1ef2-b489-38ab-b906-bdd21cad4171 | -8.12063 | -44.0522 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 55b00087-cf36-305a-8d58-7b31695e16c6 | -7.09407 | -42.12482 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bec42f3f-3c12-3ac5-859f-08dd9a80f0b2 | -8.42626 | -44.7538 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e14ab5de-f875-35d6-bf77-916233f35481 | -9.50573 | -45.48689 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 60db6978-46ca-38b2-840c-ee707f5869b4 | -7.33281 | -41.4256 | 2026-09-14 15:48:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0f329d13-088d-30ae-909f-66f84336ab37 | -8.99911 | -39.9847 | 2026-09-14 15:48:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c415fd8e-99d3-358a-83ba-a0209a0ccf59 | -7.5593 | -41.84799 | 2026-09-14 15:48:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fcb94f34-822f-3fde-b73a-4f8a7031328f | -4.72107 | -42.27617 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 030e249f-d76f-34bd-ac09-4227426426c5 | -6.77046 | -42.75065 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| aadd5b9e-cc0b-305d-9da1-d060066e0887 | -7.4337 | -38.98275 | 2026-09-14 15:48:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 26874605-a737-34ea-a387-995e6471cd73 | -7.19784 | -46.13215 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a7bc2822-e5d1-3b2c-9451-2145d74969cc | -7.0147 | -44.62749 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| da4199bc-1533-3ebc-82f6-dc794e936481 | -8.57621 | -44.48859 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 62be3036-6650-31e2-abbe-2d387aed0e07 | -7.09122 | -41.78687 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 2db7c2f6-b240-3036-b8a7-a1a5315d268d | -8.63211 | -44.44817 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3d987dc0-b6ff-3dca-bb58-3aea19305b0a | -7.16665 | -42.10841 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 42c5e46c-e587-33e8-9e14-8f7145295935 | -8.82958 | -45.87749 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc455562-c14b-3948-8e9e-dc62dabb5ce5 | -9.50649 | -45.49324 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f52ee8d0-90b6-39d4-abfd-a8e2c9d60da9 | -6.42272 | -41.55861 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 890b2273-19b7-3e3c-9693-006a69c73b66 | -6.67226 | -41.66431 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 71b89bc1-1868-3524-8a87-39cb8e2d1189 | -6.33858 | -45.54401 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23d8f0b2-09a2-30c0-b243-cb71be44d980 | -7.10145 | -42.1038 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7dd20d4f-77f5-3c6d-8a46-2f27cf94d052 | -7.08699 | -42.11261 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 402be668-c422-3745-bfb3-72c8695ed695 | -7.48156 | -44.88604 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e0ce85d2-311f-35d0-9edf-2be9f3b44980 | -6.56713 | -45.31934 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e6137cdc-8126-3814-b38b-e53bc165738e | -4.00557 | -43.26403 | 2026-09-14 15:48:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7fc3f8c3-48eb-3fa9-98c8-f68bacbe9785 | -4.99957 | -42.38407 | 2026-09-14 15:48:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8a223344-9189-39a3-a831-8bc0adaed5ee | -6.76967 | -42.75015 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9170b19e-24a6-3c2d-be20-7b626d382816 | -7.48405 | -44.88504 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44a8d19b-b5d5-3c5d-83a4-124907ba3ad9 | -6.38105 | -44.87699 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0c3b0cb0-3cd1-36c6-a215-322787cec645 | -7.09064 | -41.82185 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 09707623-71eb-31ee-adc0-39934fe1928a | -7.13226 | -42.09281 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 567e2cc4-d7f2-357a-987e-1a12f46d3ba6 | -8.21853 | -43.79166 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 25186520-2c50-3d50-931c-44443c5001c5 | -9.99516 | -45.88803 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 83031b18-df0c-38ad-b91e-5221d7af2c71 | -9.02166 | -45.08395 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f3f3586b-fcdb-3454-8f81-8302d256ca98 | -4.45765 | -39.35169 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 5a7a2281-9dba-3926-9c51-7ab54486daa2 | -6.26225 | -41.95115 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1a749f12-8174-3302-8649-fc86209f3d02 | -8.3955 | -42.21793 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b9ab4701-1b3e-35eb-a519-9a463249cd89 | -7.47811 | -42.12001 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d8683dc6-88d2-358a-b619-b524bb54630c | -6.15935 | -45.18999 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README90.md)
