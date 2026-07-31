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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 814b5b88-e2fe-3fb8-84ca-863023f726ca | -22.24501 | -56.70411 | 2026-07-31 05:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa335003-6c6a-32b3-8578-c49a63c7fd51 | -21.38148 | -56.835 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f1dc07a-8154-3f95-8ca2-98d760c07a80 | -21.04194 | -48.46756 | 2026-07-31 05:21:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30f53fa1-8404-3c82-80da-7771bc11b228 | -21.04153 | -48.47191 | 2026-07-31 05:21:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d065984d-b665-3b55-ae5e-a56a2d732ebc | -20.11189 | -50.74358 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7e5be68a-b822-3742-aa22-1098fa45793d | -22.16101 | -56.0219 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 36.1 |
| e463ebe1-a4ba-3a56-840a-110e649b547e | -19.0187 | -56.42214 | 2026-07-31 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 808576b3-364d-3e64-9b9b-099750bf8262 | -20.11621 | -50.75032 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 94b92c76-1012-3295-bd26-3b04e6172ba2 | -20.59003 | -57.24263 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efc2da43-61ce-3a07-be6f-704eeb543568 | -22.16471 | -56.02235 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 36.1 |
| aa7e5e63-8c41-32e6-8304-df3a65d567c2 | -21.37854 | -56.8303 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c82437ed-25c0-35da-82a8-07814142bd88 | -21.04612 | -55.82708 | 2026-07-31 05:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a3a1ab9-1c11-3ed3-aaf8-1a7b30f10064 | -22.21257 | -56.05766 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b3925fe-78ff-337a-b3f6-008cd2d33f31 | -22.16164 | -56.01722 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a321175d-385f-3a12-bf70-c18a6fb0da3e | -21.663 | -56.33058 | 2026-07-31 05:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2269a059-563a-3971-a51a-060b211f7883 | -20.11585 | -50.74826 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8abb24d1-8487-3ad1-b5bc-8ad1de12b48e | -21.29203 | -56.13923 | 2026-07-31 05:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fc1f333-6c16-3ce6-bb09-95b854dd6c8c | -22.15794 | -56.01676 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7714b483-0987-3d81-8e50-2cda0269a9c1 | -22.16227 | -56.01254 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7804a12d-1ba2-390b-b52b-10dfbc7e347c | -20.56993 | -57.25957 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2c92ad3-f125-36ad-bbdf-e83c280c3a2d | -21.385 | -56.83557 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a68392-7e34-3d0f-9076-1d1e8285f8ad | -20.6129 | -57.30319 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8009369a-5ef8-3cc1-bb93-19aa9bc56a63 | -19.02917 | -57.50415 | 2026-07-31 05:21:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d141f352-db3f-3057-b01b-e8cfb5d80fb9 | -20.57337 | -57.26018 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31e22ec-c23a-3ab5-be05-e83a0ac0b0c8 | -20.11124 | -50.74955 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 1177fe1a-fed1-3272-a5db-cc25a24ed3e1 | -22.19424 | -56.02665 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e826f39c-e054-3a0d-96fd-713025ff6a92 | -20.32557 | -58.08574 | 2026-07-31 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a123a229-eadd-3a75-8a13-2afe17324d6c | -22.16534 | -56.01769 | 2026-07-31 05:21:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 16209b64-4b39-39a8-aca1-7c2f344a85d3 | -20.51663 | -57.15001 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feb6c975-9ef7-3a88-b41f-e186e4689b69 | -20.56936 | -57.26352 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b04185ab-1f94-303b-8e1c-9c941bf53f4c | -20.1109 | -50.74751 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| aedc4422-7322-36f3-a27f-a6b3c2cc99fc | -21.38853 | -56.83614 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99ff5123-8549-3c09-9950-b98012cf0082 | -21.38091 | -56.83908 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd78b4a2-5f6a-3711-b498-682ca7f49497 | -20.11685 | -50.74433 | 2026-07-31 05:21:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6e787988-5c3f-3595-8cbf-4045bfb7ef68 | -20.61348 | -57.29924 | 2026-07-31 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7e1448e-afc0-399e-a585-49750a5bc6da | 1.10735 | -60.51487 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a855ea55-69dd-36f8-ae17-81fbe8393076 | 1.10129 | -60.51934 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 078879e5-83a3-352c-af48-9d81b4bdd7ca | 1.09912 | -60.50563 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa7de43-df8c-302b-9c90-03dc25b1428a | 1.1035 | -60.51197 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6878640f-4fca-361b-8767-194b26cede57 | 1.09857 | -60.5022 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3d9d12-4521-32b9-8474-fa4bea0f461a | 1.09803 | -60.49878 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2775d07f-df79-3ff6-81a2-e0c151f1549a | 1.09799 | -60.51986 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5faee3b6-d990-3a11-a073-a9dfdd2b7505 | 1.09749 | -60.49535 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 422fc9c1-f551-341b-8716-aaf41a956cfe | 1.10296 | -60.50854 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ccfdb05-55db-3c5d-9346-32ce0b8669b1 | 1.09473 | -60.49929 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45985fcd-a287-3990-a48a-db5e484f5203 | 2.51794 | -60.64437 | 2026-07-31 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55d48d8b-9a94-37a3-a732-923734254b64 | 1.09966 | -60.50906 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 875bd592-8e6c-33e3-8c8d-e6d84f4c7b83 | 1.10242 | -60.50512 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4124f9f8-fac1-32d9-beb2-de2733d31e6e | 1.10405 | -60.51539 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 226b70b2-c135-3650-af2a-1efa9fa58076 | 1.09582 | -60.50615 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd3db564-9e4e-33f3-aecf-33934ba64a2e | 1.09527 | -60.50272 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c93145-6094-3f4d-81a7-93e0755b0a50 | 1.1002 | -60.51249 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63ca4c70-cce2-3ef7-81d1-b0f6858acc8c | 0.90672 | -60.53622 | 2026-07-31 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 104db244-222e-362f-8e79-7dfed36541ea | 2.51848 | -60.6478 | 2026-07-31 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 338c3353-c37c-3134-b105-c9b4865c652a | 1.1068 | -60.51145 | 2026-07-31 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a1e2582-4da3-3230-b686-1e1f2c823098 | -3.04718 | -48.74863 | 2026-07-31 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2324dfd5-5d09-3e54-a31a-12a052be7859 | -3.11493 | -47.90615 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c10859b0-08d5-3a74-80d8-b0ce4291d2d9 | -3.0307 | -59.16513 | 2026-07-31 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95741f70-420c-3564-a670-a97117fba0be | -3.96343 | -48.1274 | 2026-07-31 05:33:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fefd5e96-834b-393a-b34d-ee897c026e5b | -3.14943 | -60.35095 | 2026-07-31 05:33:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b532a2b9-bda6-33cb-a4eb-329abe6122ef | -6.55635 | -55.15751 | 2026-07-31 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f5642e9-09f5-3e2a-8ec0-27a6f5aa4041 | -3.11098 | -47.90604 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aac5df4d-7510-3a80-ab25-fe9d6d063b5a | -6.17848 | -55.52911 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac920d50-5a02-36c2-9d2d-6283efbe6f06 | -3.71162 | -51.17574 | 2026-07-31 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e991d7f9-dddb-35fd-9343-71277ae0f0b7 | -6.55563 | -55.16241 | 2026-07-31 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7e1f839-9486-3fa3-a09c-cc429b37a2b1 | -7.27401 | -64.78313 | 2026-07-31 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 356e59a8-44bf-362a-8720-225b31d1d076 | -4.27727 | -48.19801 | 2026-07-31 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 769373b5-653d-39c2-9ae3-bdf16e7f2fd0 | -6.17396 | -55.52843 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffccf08e-b532-3574-a4b4-2bce01e53043 | -4.21788 | -56.04891 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb78bd54-b3c2-3c8d-8f6b-a44d1108056b | -6.55525 | -56.54068 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 389e3186-18ab-37c3-8818-1bd1c7ffccbf | -3.71101 | -51.17984 | 2026-07-31 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6302d45a-bec9-3178-acd5-92d7adc8a4ef | -3.11391 | -47.91331 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c0827f12-d250-381d-a44a-b31b95d93b02 | -4.27294 | -48.19601 | 2026-07-31 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e49df2b9-03f7-3cc4-9081-7d3799ea925f | -3.11805 | -47.9072 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbbda4a5-6de2-3958-8009-b030b1d3d173 | -7.73243 | -55.34164 | 2026-07-31 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5afded71-647f-3381-aca9-0d0d30f71097 | -3.11699 | -47.91427 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e31884a9-7908-382b-84ed-58839ddbdbcf | -3.89242 | -59.07283 | 2026-07-31 05:33:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfc689d4-5455-3150-ba20-15a77d0d6f58 | -6.18818 | -55.52593 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7105b49a-8008-32f1-99e5-1aafe873177e | -7.73711 | -55.34231 | 2026-07-31 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b366d82-a0c2-3f23-a081-3ab087dcc54b | -2.88807 | -48.01657 | 2026-07-31 05:33:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7c5441-3d27-31c0-9c48-4038e0fd3a72 | -6.18887 | -55.52125 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 863bf4ba-eb75-3fc9-8cde-f5d20aa03f72 | -4.27018 | -48.19707 | 2026-07-31 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ef6da3a-5456-3942-a5fd-c3506cb8c6a1 | -6.17914 | -55.52458 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24544954-faf9-3a49-a9f0-1761a38d6a7e | -3.10992 | -47.91314 | 2026-07-31 05:33:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89d99684-99ab-311a-b356-985778085ad0 | -0.19908 | -60.76703 | 2026-07-31 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d17b8f9e-822d-376f-967d-46e23b2cb4d7 | -7.73449 | -55.34459 | 2026-07-31 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba79483-6113-301f-a95f-c09e43c6dbe3 | -1.78005 | -55.50543 | 2026-07-31 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae0c2bda-9b70-37af-9cda-734496455684 | -6.18298 | -55.52985 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 869c3ca1-f429-3079-9dc6-dd9481f72799 | -3.05036 | -48.74356 | 2026-07-31 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54eca61f-8ae6-3067-a044-bf989acd312a | -4.71914 | -55.99454 | 2026-07-31 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35dfec4f-5bd8-3661-9271-2a181db065a3 | -3.04811 | -48.74256 | 2026-07-31 05:33:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e34faad-3265-3721-974e-bcca7a72a106 | -7.27268 | -64.78152 | 2026-07-31 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38c2f869-abdb-3fd9-88dd-f857c8b5182e | -6.561 | -55.15827 | 2026-07-31 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69e8e788-3f7d-3ba9-87a1-d5495bafbe94 | -2.8951 | -48.0176 | 2026-07-31 05:33:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e421f88-2038-31e1-abd9-4b6785d1d648 | -3.96587 | -48.13144 | 2026-07-31 05:33:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 31a39924-96ba-35c3-98bc-3848309d9d2a | -1.73283 | -55.84394 | 2026-07-31 05:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e328862a-aed1-3a4b-972d-2cf2a3f2c0ca | -4.27193 | -48.20285 | 2026-07-31 05:33:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 50ac3f01-912d-333d-af7d-b17b9957b584 | -6.55582 | -56.53676 | 2026-07-31 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c02971e3-7354-376c-96e2-7b826c62964a | -7.73517 | -55.33958 | 2026-07-31 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8baf7c-71f6-3cc8-8d75-f273c8e302f4 | -3.96687 | -48.1247 | 2026-07-31 05:33:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README14.md)
