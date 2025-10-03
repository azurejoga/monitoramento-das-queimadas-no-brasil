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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb9431f1-4ec9-37fc-9a03-a228e097aae3 | -6.41404 | -43.84333 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a9cd910-a7a0-3372-9e7b-e4c805f9e28e | -6.13931 | -39.76334 | 2025-10-03 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 974adddf-3c78-309b-94ec-1066ff7d3e3e | -7.7596 | -46.24876 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8599015f-5643-302b-a967-e59d536e7076 | -7.77697 | -42.59187 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| c4e86d24-899e-3014-a93a-8327791e3d49 | -6.40937 | -43.93248 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c1dede4-6971-3a11-b714-2ac0b3a57dd6 | -5.32221 | -45.28239 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fec5687-9a3e-3c8a-b702-cfdd7b77718a | -7.77781 | -42.58704 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4fe4b093-b64b-3826-ab23-fe715bbb7226 | -7.80299 | -42.52335 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4662d048-ba32-3664-8733-2222ce969e81 | -7.75113 | -42.57752 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f3d0d5c4-7f66-3755-9475-09202a55115e | -6.55449 | -43.88595 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b240a9c1-89cd-3fe9-a8dd-5c3ac215c485 | -6.33273 | -43.8861 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0815cd46-c28f-3813-a5ff-18c696e24342 | -6.05474 | -44.61342 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 95986140-1d40-3416-a5e1-f0121566bdf2 | -6.70902 | -42.80384 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| efe3962c-f1df-32f3-916e-69674ebc728b | -5.17909 | -45.42068 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17dfe4a5-d4b7-3b52-a54c-494d9e474acf | -7.75863 | -42.58865 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| af932a5e-db2b-3351-9999-f1d478ad2601 | -7.75654 | -46.23265 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7ce4b34-4751-3376-a688-3bcd6dbdd254 | -6.80064 | -44.74687 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f7ddee5-3e95-300d-a2cd-17485d3426da | -6.34513 | -43.40279 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a91f8d9c-af56-3b99-9e24-a20152358276 | -5.47875 | -44.69475 | 2025-10-03 03:42:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 070cd789-4070-353f-86d9-b007a93d7b7b | -8.23161 | -39.028 | 2025-10-03 03:42:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cfee6d84-cad7-3cec-8d39-75e26917c45a | -4.66967 | -45.81455 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6087e5c-d69c-3e0d-96e6-706529b3ba79 | -6.05105 | -44.63476 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 175beb10-3ead-3d52-bf81-acf2d3856cc0 | -7.76442 | -42.55562 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| aeaf8c93-02c3-362d-9120-9be2c2e675e3 | -6.34464 | -43.40563 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5a23dff-c192-3dbf-8513-a4f726126d56 | -6.33168 | -43.89205 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf6f2766-24c9-3afa-9cf9-9ccee378766f | -3.93395 | -47.56631 | 2025-10-03 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6c17de2-5df7-320a-80ee-d755ff1d72ae | -6.0587 | -44.6325 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04b266fd-b11d-3e70-8de6-d4fd7a2553e1 | -6.35172 | -44.30158 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2875697c-4255-3c93-a7d4-29d0ade4abd0 | -6.19023 | -44.62717 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08586fdb-bc08-3b73-9ac7-c43df786818b | -7.79844 | -42.52248 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a7540513-6587-32db-aaf3-1d20a6c6dc3b | -4.66437 | -45.80947 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9bc30478-a23d-3446-a1d4-4da334a2f1c6 | -7.76317 | -42.53586 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9fbc2201-1cdc-3e89-b3c9-82c6b7258e8a | -6.72933 | -44.15111 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b6dd98c-a6b1-3414-915f-8aad9f4f600a | -6.22696 | -45.34874 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 552e4e77-c3c9-38e7-b056-9f5f9c28e250 | -7.7488 | -46.24181 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94cd94fd-02df-34e9-9458-5243648e89f3 | -6.05043 | -44.63835 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cb213c3-5a8a-3006-865f-d1672440ca9e | -5.17891 | -45.42387 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 173df470-3dea-3d8d-907b-f00a711e8c80 | -7.31048 | -45.25798 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bf37aee-893c-3574-b576-f73b6318fa0d | -6.3501 | -43.40363 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b5c6e6-325a-3b2f-96c0-1eb1dc375b75 | -6.22627 | -45.35267 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e33bcde9-5775-383d-9c1c-c083a7d9e313 | -12.94003 | -46.37798 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c81cc2db-2bde-3e14-b815-6feea6a82840 | -11.11737 | -47.86932 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1a06a264-0d23-323f-b4cf-8680d3658ba2 | -13.95859 | -48.0931 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03f2331b-7fe3-32a8-8cb1-9e081cc27d2f | -13.7834 | -47.55995 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dcf1c664-8931-375b-ba5e-51168f73824e | -14.22322 | -46.0923 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70d2b2b2-eb8e-3750-ba33-e00c10c9d3a3 | -14.11755 | -44.30983 | 2025-10-03 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f61a6522-213c-3ff4-937e-7d6819bdbff1 | -15.52691 | -46.80816 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df2cf898-7d7c-3b3c-a567-1df47250a49a | -12.62258 | -46.97745 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2905117f-df3f-3da4-a940-2075f2378b08 | -14.89697 | -46.97004 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aa69702-f674-35b4-a660-9f50d38a8657 | -13.67485 | -48.03131 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d440c4f3-37e8-35c7-991e-46d289d8da99 | -13.13293 | -47.89392 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e93a41b3-3242-3861-9d01-7743a6615863 | -13.29491 | -47.26529 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4a70800-a215-3dfe-b7ec-79991e1f0084 | -10.86635 | -46.66655 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 086b5126-08af-33d0-9be1-dad31e7f196f | -14.94562 | -46.89478 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83d2181e-b928-335c-8e2c-b68bb7117906 | -11.61726 | -45.0309 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9922962f-37b3-353d-a928-8f51d2f2ce28 | -11.49688 | -45.00938 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bb471d6-f612-3e0f-9902-954d9eaed6ad | -14.40275 | -46.14843 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a16eed3e-d964-37bb-b40e-7617373492fb | -14.93418 | -46.89612 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| acc4e70e-182b-361a-9eec-c2bdaadf83a1 | -15.30712 | -46.2822 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d190ab5-6c85-3aad-914e-ee14001afa52 | -11.55922 | -47.65308 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 997b3adb-7606-392d-8df4-260ee8522f7c | -11.45965 | -44.95683 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 456beb32-7f37-3c94-aa9b-07b0b7260bc3 | -15.34039 | -47.06639 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f98d35b-e742-335d-8d7a-adf007ede26c | -14.89563 | -46.97672 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6a5680b-0b52-31db-a363-9ea92f1c140e | -12.60845 | -46.96017 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd82ab68-72db-3810-82b3-d71f246e92af | -11.90846 | -46.27893 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c45be21-9855-392b-90cf-2eb09a3fdae3 | -8.65208 | -47.71439 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 243f645b-5485-3dc7-b864-b5c8fcfbc9b0 | -11.8569 | -44.96435 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6b27ddd-e75d-3b62-92ec-3b8bd56d8d31 | -11.77955 | -46.82749 | 2025-10-03 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35832a0e-abd0-391d-997d-8eea3f0fcb0c | -9.06696 | -46.65982 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3de8c6e2-ea78-34ae-baf5-89dd983e9e3b | -14.90032 | -46.84231 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4b5d7ed-e615-3fce-8f51-6fca51a955c5 | -16.3436 | -43.5202 | 2025-10-03 03:45:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c0ecf6-54b8-3b77-9a86-f577cbc42f81 | -13.68464 | -48.62922 | 2025-10-03 03:45:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44824623-5d72-3b94-acdd-a4f0799a3579 | -9.06377 | -46.65169 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a29996c-5648-3d41-b477-558e42ad69ee | -13.12683 | -47.89373 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f3603c63-26bf-3229-b3c7-a54770653478 | -12.20284 | -47.78455 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d9e14b04-e9fa-312f-9a8f-84e31dc68fbf | -14.93631 | -46.91352 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5012bac-47f3-34c6-91c8-d1e133be970a | -11.92111 | -46.27709 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| a1d4ef2d-4056-3201-bf69-26575f20a130 | -15.83504 | -42.62669 | 2025-10-03 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 222a5453-e60a-3712-acb6-e7abc0085f35 | -15.28245 | -47.91856 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1422827-ec26-3f57-8d65-db5d3f4a8c9d | -14.22773 | -46.09674 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d4b9878-3892-332e-b526-42fc09e6089c | -14.29586 | -46.02982 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb3e4c23-a27c-354b-9f45-9d51cba34a1f | -11.64118 | -45.06294 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 543a90ed-0a3e-31ae-a3c8-63845222b87e | -13.77693 | -47.53334 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b830da6f-6e11-3a37-9e9c-f15bf905fc06 | -14.69477 | -43.88705 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f1e85d8-555d-3a27-a01f-b122261b1dd2 | -14.62158 | -48.23039 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2ba5399-1c0b-3cea-971d-685b0868caaf | -14.67904 | -48.0703 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a0f925c-b6c1-33c9-a72d-b8803a2c3e71 | -12.37121 | -46.51303 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f66162b-8b61-398c-9168-2abace1feee1 | -14.46432 | -48.40474 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d1a8712-4128-37f5-8926-bb15acc58c14 | -11.48465 | -44.99073 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25762a4d-fa26-3ddd-844c-8e79c49a4239 | -14.87584 | -48.33602 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a49c02-201d-3520-8bac-3b524fc067e2 | -10.87932 | -47.82029 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41964768-2821-3323-a64d-a6104135036e | -10.87051 | -46.67572 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02709e0a-3310-3801-b58c-c2dc35979491 | -14.74904 | -42.46183 | 2025-10-03 03:45:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6446f8de-85fd-3f8e-b070-6eaaac176948 | -12.71507 | -48.57944 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78ebe0f7-c1ad-3c6c-a24c-60e88d67b1e9 | -13.97036 | -48.17479 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a282f37b-a320-3e2e-8996-80eec833e7b0 | -9.92651 | -43.71799 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4c88491-28e5-3f11-af8c-faed59212041 | -12.89895 | -46.90211 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a5db467-dc2b-3c17-9580-8ffebb0406ac | -14.98342 | -49.9654 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e898ab5-442e-32d8-9081-8ba2e3118ae6 | -9.94363 | -43.75932 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ffcef589-5e12-382a-a3f0-47e2a7c51c46 | -10.87148 | -46.67934 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README23.md)
