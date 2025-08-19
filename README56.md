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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3230464-4c8d-392d-b56f-20c6453e5d18 | -12.9925 | -45.202 | 2025-08-19 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 60822b8f-2aec-33db-bdc4-3cc354c1ef4c | -6.9339 | -43.5868 | 2025-08-19 11:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 1e1305ca-2f41-3ae7-b6c9-5350aacd1961 | -6.9715 | -43.5833 | 2025-08-19 11:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4b859188-56e9-358a-bdbf-7aca4b13b7e3 | -7.6777 | -45.9647 | 2025-08-19 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 00519d57-984f-3db9-924f-57b1584febee | -12.9925 | -45.202 | 2025-08-19 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| fb8fe0a6-5a44-36c8-b0a7-4b71a1949866 | -13.0119 | -45.1988 | 2025-08-19 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 95401edf-89d8-3998-a193-f436e6d116dc | -6.9339 | -43.5868 | 2025-08-19 11:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| c68cce59-278c-3f26-8098-8567bf3bbeb8 | -12.993 | -45.1787 | 2025-08-19 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| d548a2a6-737a-353a-962f-1705440a894c | -6.9715 | -43.5833 | 2025-08-19 11:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| bde0af6b-69dd-3a41-a5be-43cbb5335bb4 | -13.8752 | -45.5179 | 2025-08-19 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e1e9c4e7-5f52-3a71-a388-ec9dcca3b376 | -7.6777 | -45.9647 | 2025-08-19 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 0d7456d7-21f0-3266-80cc-32dd3d161057 | -6.9715 | -43.5833 | 2025-08-19 11:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d07a1c45-5ad9-3c97-82e6-f4c335834cb1 | -13.8752 | -45.5179 | 2025-08-19 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 20f5b651-65c4-3563-928a-2be1f39b3b6a | -13.8748 | -45.5411 | 2025-08-19 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 72ea3a8d-34b4-3a7a-b308-c404d6b20c90 | -13.0119 | -45.1988 | 2025-08-19 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| a318886d-034e-3c8d-a1be-17c78bf7559d | -12.993 | -45.1787 | 2025-08-19 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 03bf7a41-922c-38a7-99b1-79264a12d9aa | -6.9339 | -43.5868 | 2025-08-19 11:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 55d9eebd-21d7-3066-b795-90d23cd9db05 | -6.5201 | -45.5013 | 2025-08-19 11:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fee727bb-3ef3-3984-a654-1f9894e6ccdf | -12.9925 | -45.202 | 2025-08-19 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5872d524-2af8-3a6c-ad3f-41cc871e7110 | -6.19933 | -42.52961 | 2025-08-19 11:34:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| d373c283-9381-394b-b7ad-2e2a54959240 | -5.92885 | -39.47215 | 2025-08-19 11:34:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 9db412a5-92a7-3827-94c5-b4a05e13e2fb | -5.4096 | -36.73068 | 2025-08-19 11:34:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 3bf5f37c-4f00-371f-b178-c2ed66362576 | -6.52223 | -45.47408 | 2025-08-19 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 836275c6-ef5b-3fb8-a0c1-3307758fa073 | -6.52481 | -45.48185 | 2025-08-19 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 58696aea-4a8c-3f04-b89b-58a97009513c | -6.92855 | -43.59818 | 2025-08-19 11:34:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a36f42fe-431c-37c3-a95b-7150d62d246c | -6.92899 | -43.60434 | 2025-08-19 11:34:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 5101fd26-7c18-3beb-a21d-cfac1efe7790 | -6.51819 | -45.5212 | 2025-08-19 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e7479ce7-852d-3de0-bb9b-73c8e978738a | -5.79443 | -43.62629 | 2025-08-19 11:34:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 92c7d696-dfbb-3467-8412-c46c1c12902c | -6.51591 | -45.51318 | 2025-08-19 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 07b52370-af19-3f3a-a39a-a7b9db79abc1 | -6.22754 | -39.14478 | 2025-08-19 11:34:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a31cfdd5-63d6-39cc-842e-a3bbd27634a5 | -6.19258 | -42.52256 | 2025-08-19 11:34:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 4d801b65-f470-3863-a877-7699ae46829d | -5.85179 | -39.37318 | 2025-08-19 11:34:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 23832466-b962-3d06-b979-1a8a38e2c55a | -6.30244 | -37.87767 | 2025-08-19 11:34:00 | TERRA_M-M | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 8d242e26-4b4a-3620-a884-25a32e82c2bd | -13.43283 | -39.9535 | 2025-08-19 11:36:00 | TERRA_M-M | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ee12ac5c-0229-3785-86a4-f8893c7616a4 | -13.15201 | -42.55215 | 2025-08-19 11:36:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| dcbf7430-c8bb-3070-9fed-8556144345fd | -16.1751 | -43.63047 | 2025-08-19 11:36:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 134956fd-5527-3c5c-9e27-15702dcd032e | -12.89292 | -46.09837 | 2025-08-19 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| b6450c09-7519-3887-b925-f27c401ba48c | -17.94679 | -40.21891 | 2025-08-19 11:36:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3617f656-24b8-3397-a9d9-e2408f27f474 | -18.10768 | -41.08649 | 2025-08-19 11:36:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 6a0bcdb2-c65d-38db-ad58-70f51aa6e391 | -12.99734 | -45.19798 | 2025-08-19 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 379.6 |
| ec72245f-1c4b-3465-aa47-0bd9fcd12f41 | -17.93304 | -44.36398 | 2025-08-19 11:36:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5f609844-ce68-30f6-b690-c006732c9db4 | -13.87642 | -45.51414 | 2025-08-19 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9768c306-a283-3569-ab01-ca47fc8af9f0 | -12.4776 | -43.20991 | 2025-08-19 11:36:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8ab30086-15b9-3941-b792-107ec3494bc6 | -12.88067 | -41.87883 | 2025-08-19 11:36:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 8d3c1191-d619-3f2f-9d38-3a224fb2bd73 | -16.63978 | -39.5272 | 2025-08-19 11:36:00 | TERRA_M-M | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 34e69883-977a-310f-8243-2a90cba7ef4f | -13.11466 | -42.06968 | 2025-08-19 11:36:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| fb12161a-7f65-3fa7-8e94-1386d67e7b89 | -13.87121 | -45.5428 | 2025-08-19 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 1771cc02-8ba1-331f-8835-847c4cf5f0fa | -13.87787 | -45.50721 | 2025-08-19 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| eb4f136b-53a9-3ddb-82bc-053e60f27378 | -13.13561 | -42.72821 | 2025-08-19 11:36:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 77516b24-2e8d-3301-aac6-dd5e11c08f32 | -13.87283 | -45.53614 | 2025-08-19 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| ccc75164-9a4c-3d80-a2f9-b43beae18e71 | -17.93328 | -44.37073 | 2025-08-19 11:36:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| faae1387-9fe5-39d0-bf14-cf976c8e7cfc | -18.37596 | -40.18203 | 2025-08-19 11:36:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bb88c360-2b5f-3cf7-8e75-4e221aced050 | -12.48097 | -43.1897 | 2025-08-19 11:36:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 84ddb996-bcd1-3b25-902d-46600b6e7b39 | -15.78194 | -39.34678 | 2025-08-19 11:36:00 | TERRA_M-M | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e78c2213-88be-31e1-8429-bc5c155cdccc | -12.99814 | -45.1909 | 2025-08-19 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 571.9 |
| eb25ea3a-fea1-354b-b56e-d22e0fb160f3 | -16.60711 | -39.61547 | 2025-08-19 11:36:00 | TERRA_M-M | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 9142c148-f922-35d7-ab83-bdedf4316588 | -7.6777 | -45.9647 | 2025-08-19 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 704f25fe-0bab-3b01-97b2-4a26cf636cbe | -6.9715 | -43.5833 | 2025-08-19 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 364f95e1-e5d2-3c84-b8e7-75eddad4df60 | -11.6048 | -46.6188 | 2025-08-19 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| dcbe4918-018a-388f-9c9e-49969277dbb1 | -6.9527 | -43.585 | 2025-08-19 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4136c1bc-8b4d-31bb-a1c3-4db4554785a8 | -13.8752 | -45.5179 | 2025-08-19 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4c0e84e5-97df-3d03-a52f-c2304077fd7c | -12.9925 | -45.202 | 2025-08-19 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 2c2599ba-cabb-3303-89b5-d2ad56b996cc | -13.0119 | -45.1988 | 2025-08-19 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 72115b34-e283-3527-8d5c-d30d72a5bd39 | -6.9339 | -43.5868 | 2025-08-19 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 313860f8-74e2-35f2-af00-3e3016c506cd | -12.993 | -45.1787 | 2025-08-19 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 673c1e09-1350-3842-be5e-7bbd4b4ff202 | -6.9715 | -43.5833 | 2025-08-19 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dbc37634-6d82-3d81-8467-098962c99133 | -7.6777 | -45.9647 | 2025-08-19 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 004279fa-fee1-333b-8de9-e8547047a843 | -12.993 | -45.1787 | 2025-08-19 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| eabb4f38-2e83-3ce7-bca5-c7d7e8799d9a | -12.9925 | -45.202 | 2025-08-19 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 50766302-84c3-3ab0-8f42-0174eaf5eee4 | -13.8752 | -45.5179 | 2025-08-19 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 43940f7f-59f1-386f-8cab-bafe73c947ed | -6.9527 | -43.585 | 2025-08-19 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2795c266-40be-35e8-a3ff-a94e46e88daf | -13.0119 | -45.1988 | 2025-08-19 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 308.7 |
| 9df0f060-d2bf-3806-9dc8-b82ca3c8e251 | -6.9339 | -43.5868 | 2025-08-19 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 14b9da23-a091-3426-aa56-2dfad99016b4 | -13.2563 | -50.8162 | 2025-08-19 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1c08a50e-1d86-3dd3-bde0-92bd5494d22b | -6.9715 | -43.5833 | 2025-08-19 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6045adbe-cc10-3e8a-8d75-98e496e932bb | -5.7887 | -43.6134 | 2025-08-19 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9bced843-5b04-3cee-8f0a-c08b6d5d5c6a | -7.1606 | -43.4956 | 2025-08-19 12:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 2b4be71f-b3d3-3618-8270-daa085260a8a | -12.993 | -45.1787 | 2025-08-19 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| c442e3a5-e069-385d-bc1d-1ca1aa7a4a6d | -6.9527 | -43.585 | 2025-08-19 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1def980c-74d2-3e10-ae11-0ef43f449cb9 | -12.9925 | -45.202 | 2025-08-19 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 6a829869-e25b-341a-a8f6-7e2f0b41ff4f | -13.8748 | -45.5411 | 2025-08-19 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4e1744a9-e70b-3e62-8b59-4e3b0c211bdd | -13.2755 | -50.8137 | 2025-08-19 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8517b7ec-e6f9-340d-813e-2bc9e52b59f5 | -13.2563 | -50.8162 | 2025-08-19 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| f315f18e-0b70-3434-b566-4c3fd299b20a | -6.5201 | -45.5013 | 2025-08-19 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 5b05f6cb-d8da-3d03-83be-704392f6c944 | -13.1555 | -54.9357 | 2025-08-19 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e9a3359f-7240-33ee-9829-5181094bc7bd | -13.0119 | -45.1988 | 2025-08-19 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 375.0 |
| cc62fe64-5b7b-3ce7-bdce-4c7bc6cafba0 | -7.6777 | -45.9647 | 2025-08-19 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 214c0475-5657-3de8-9c81-bd98f8dffd57 | -13.8752 | -45.5179 | 2025-08-19 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b0bb8091-c2b5-3278-be77-ce8fac77bbb6 | -6.9339 | -43.5868 | 2025-08-19 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f0fc2fac-2953-3b53-9992-7ed256840bb1 | -12.9925 | -45.202 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 21403e7c-c3d2-30d1-9b1a-fbc342c4e423 | -6.9339 | -43.5868 | 2025-08-19 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| fbe61bb4-5f44-33e1-9d94-3c18e381e3d4 | -6.9527 | -43.585 | 2025-08-19 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 735ecbd4-f024-372c-bb89-bd77dc65cb90 | -13.2755 | -50.8137 | 2025-08-19 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 4b6b651d-de30-316e-a567-4f3c9a7cb003 | -12.8984 | -46.0906 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 75aaf0af-bb99-3796-a392-295afb41438d | -5.7887 | -43.6134 | 2025-08-19 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1cb3263b-38bd-35c2-83da-72d166bbcba2 | -13.2752 | -50.8352 | 2025-08-19 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6dd7e03d-223a-365b-848c-24a97636f973 | -13.2567 | -50.7947 | 2025-08-19 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 45c04d81-ef7c-3b03-a751-47b599d0f351 | -12.8791 | -46.0936 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e680fbe0-7c92-38a7-92de-008b84c7dfb6 | -12.993 | -45.1787 | 2025-08-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.7 |
| d54641f1-dc9e-347f-b728-f820d36dd9ac | -6.9715 | -43.5833 | 2025-08-19 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |


[Clique aqui para ver as próximas entradas](README57.md)
