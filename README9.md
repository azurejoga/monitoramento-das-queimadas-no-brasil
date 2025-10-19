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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 125021f8-fdd9-3fa0-8cf9-4a266a937ce2 | -4.14678 | -47.65938 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13909b35-8551-312d-ac9d-d7ce8f943462 | -8.43018 | -44.15329 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8ac2a67-f8c7-34ef-96f5-9f4e83ff4e1a | -7.44381 | -42.69662 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c9886fc-00ff-3fc3-a891-2d29a1a02130 | -5.21732 | -43.3722 | 2025-10-19 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaac2e1f-9b06-35cd-acbf-f35bf67dac55 | -4.28662 | -45.4838 | 2025-10-19 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9c8cade-74a8-3a9a-8010-05ef67c84b39 | -7.19703 | -42.20863 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ab40547e-763f-39a2-96d8-f2f7b1d80f91 | -6.96649 | -39.64311 | 2025-10-19 03:42:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a6eb24f-5a3c-3db1-86af-dfbb3b2990fb | -8.02797 | -43.9217 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebd0306e-16a3-3d37-855a-9a83d297b2ed | -7.05422 | -41.83509 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bd3ebc37-9a2e-3d52-b95e-dc06c3ff37f4 | -4.59018 | -46.5173 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28b0387-47c9-3e04-abe7-0332ca7bf2f9 | -8.61838 | -40.19334 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1b9327b0-f7cb-3e5f-a411-e38685031034 | -5.36728 | -44.94318 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe0d5a96-9a1a-35f4-aa60-e3fb47a89fe6 | -5.41781 | -40.88997 | 2025-10-19 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7615ef43-19d8-3f97-a17a-c0d63b2ce341 | -6.97235 | -47.45661 | 2025-10-19 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbfd2367-23e9-3bc9-a7db-fbf9153f4ab2 | -5.78009 | -42.72459 | 2025-10-19 03:42:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 10e4b6c8-5d99-3ceb-9990-92fa8e16be54 | -7.22993 | -41.17276 | 2025-10-19 03:42:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 645d5b57-52bb-3e31-90e9-b256c88c5a28 | -9.33445 | -46.11304 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1247933b-3c93-3ba9-a7a5-1000e9c19b4e | -5.17546 | -46.10762 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 116192c1-35b1-31b5-8080-17c5b6a1ea2b | -6.96502 | -39.63976 | 2025-10-19 03:42:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fed2963a-f8f7-319c-a99d-58fe6016fbfe | -6.42024 | -43.9205 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdb5d227-c6ec-3f97-a4a0-59cdd8b1a84a | -8.4709 | -39.51046 | 2025-10-19 03:42:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 466fbbb5-52b7-365b-83ec-ad21fd2cf113 | -5.36192 | -47.21149 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 9f7a42a7-d4ee-3ee5-b208-aeca0396126b | -5.36789 | -45.27914 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef757cab-bf06-35b3-93b6-66f74842f22c | -10.15549 | -42.20906 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5edadf92-6125-39d4-8471-c6380d02c0ce | -9.23017 | -46.06104 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1dee6a8d-6e2a-3f43-9956-9ccc3092d416 | -8.56845 | -48.5169 | 2025-10-19 03:42:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0dbe4d9b-1a8e-39d2-b08c-e1af73f7f114 | -7.31179 | -42.47021 | 2025-10-19 03:42:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 82b38c3d-2518-3089-b2d7-4f455db9b6a0 | -7.19971 | -42.18625 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a84f02d8-4558-377f-a494-816093b9ab9d | -4.91812 | -45.98798 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69b713e7-e4d2-3eb9-845b-92993eff06d9 | -7.31263 | -42.46536 | 2025-10-19 03:42:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 275ee7e3-a4d7-38c2-9e2a-984c41da0f23 | -4.9198 | -45.98435 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a573f63-5d77-37d1-ac02-a931565fbc96 | -8.61715 | -41.52776 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| da6a3a0a-f0b9-36d8-8755-2bcc34eed977 | -5.36928 | -45.27625 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39778b07-defe-32d5-8ad3-94beed5fca3c | -7.19085 | -42.21717 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fdf9db8f-1c09-3702-8092-a35e40f0d8ee | -4.3094 | -43.01936 | 2025-10-19 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ee3189a-9d8b-34b0-946a-8edde5dd6d19 | -5.60988 | -42.73839 | 2025-10-19 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 523f3619-5840-3151-8ab6-ecfa3700cd17 | -4.58647 | -46.29805 | 2025-10-19 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ae3a871-0e2b-36fb-82d6-8a40b84dc884 | -6.02328 | -41.92225 | 2025-10-19 03:42:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e425fb9a-2e01-3b29-8f40-fb243447a03d | -5.36204 | -47.21204 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d37195ac-5e32-3f25-9def-18b256be1995 | -8.6059 | -40.19628 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c15b2f2d-8ef7-3f12-8733-b1af7cfd0750 | -6.06615 | -44.52058 | 2025-10-19 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40863cff-ad45-3958-b465-b7c44816eeed | -7.19658 | -42.20486 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 73de2ddd-41c5-3446-aa59-823fa96449f1 | -7.44595 | -46.84127 | 2025-10-19 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f8c02b-4ba9-301c-9a5d-355c6613c32d | -7.41246 | -40.07976 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d746a4af-df79-3b29-a1bf-2c8b33e017a8 | -5.64648 | -44.80833 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ed448f73-2828-3030-aa99-6391b7e32d14 | -5.16855 | -46.11122 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9407145e-6aa3-3766-b2f3-333104704f2c | -8.2456 | -44.00285 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69d42623-d2e4-353a-ae8b-bd278288d723 | -5.33871 | -44.71342 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0309eb2-d16e-3a0e-9b26-3d66a23f0c79 | -9.66293 | -44.5563 | 2025-10-19 03:42:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af9e9842-3b53-3db2-bac6-9e43ce5f02db | -8.60673 | -40.1913 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 492ca024-2731-395b-845e-fe4ae484d7b7 | -5.31079 | -44.84835 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6783367b-fc5d-316c-bf9c-ea147443e380 | -7.44197 | -42.69333 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c6505a5-fb13-3357-955a-e1aeb8fa2d47 | -4.42099 | -40.16883 | 2025-10-19 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 56e17ae1-373a-31c5-9174-2a93f9a535f0 | -5.36857 | -45.28023 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9759403a-9894-3097-9c5f-ba3a3c496e53 | -4.23835 | -44.68724 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c203a5f-f2d5-3495-9c30-27958765a61c | -8.25012 | -44.00675 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7360aea0-c79e-33e1-a42f-b76ad0e85adb | -8.44382 | -44.16496 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee0f0304-3cca-3cf4-bdd5-19d36d276565 | -8.23764 | -43.98916 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2bda380-111f-35f8-b00a-ec14b1c91a2c | -7.15964 | -42.36726 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b0a1b576-99f7-36a6-8b5f-cd6cf1ef2b0d | -7.09791 | -42.20691 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 680c7a05-01ea-3d9e-a0cb-10f7b4d65fc1 | -9.7509 | -43.95966 | 2025-10-19 03:42:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88f3b1a3-754a-35e5-bc1a-c98ad24641d5 | -4.98473 | -43.84872 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2887ee46-8d36-35ea-b951-7421f784c77a | -7.15705 | -42.38184 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ce59418d-03e2-3447-b2c0-2f2dab34401d | -4.41789 | -43.97175 | 2025-10-19 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ef41e5c-60ab-38a1-b1be-13b01a3c3033 | -4.93173 | -43.40871 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c93f70e-6d51-3553-8545-74dc216b5c1d | -10.16413 | -42.2106 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6a04150b-3c7f-3628-82e6-9f5365ce7706 | -5.09927 | -47.79918 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8faeb6db-d814-3ef4-8da3-3024271a8658 | -4.59654 | -46.51802 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52237f2-af88-3175-8551-84d9d00b6d5d | -5.34149 | -46.06545 | 2025-10-19 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7437c569-a6ec-3131-b84e-f9161e79491c | -7.27879 | -42.30723 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c4264ee0-d0e8-3e9b-955a-9043ffc0fd6c | -5.46693 | -44.89049 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5e5d7c2-0514-3639-938a-0916d33860ed | -5.71333 | -43.82426 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64a42f5f-9755-3672-88b3-6d613c34fb6a | -9.21958 | -46.05495 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f9928b5-22a6-3391-a108-15861f67fdf9 | -7.1954 | -42.2179 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c34df05c-7622-3145-9190-2d8a83395765 | -8.43675 | -44.14585 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e689696-dafa-381c-a9d9-7b3db7b11d33 | -8.43573 | -44.15156 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3cd2086d-22d2-30b9-afb4-c6d722313f75 | -5.30918 | -45.00863 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2c82213-7d62-3589-9e73-0b3a95fe3040 | -7.16501 | -42.36454 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ebdd5a68-c61b-3c66-bc35-61bf4afa4842 | -4.82039 | -38.65905 | 2025-10-19 03:42:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4ec5a7c4-4e62-3934-a4ac-c5232b685dac | -5.30583 | -44.84364 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4811ef5f-4a59-3885-96b4-dcd00767ac59 | -7.19621 | -42.21328 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fcd12052-78f0-3862-abcc-6e8df079e60c | -9.67879 | -44.5561 | 2025-10-19 03:42:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd26a444-e9cb-38be-baf6-4bf02cca4b9a | -6.96117 | -39.63913 | 2025-10-19 03:42:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cfa3498-0885-354d-a22f-323680840f0e | -9.10714 | -43.20699 | 2025-10-19 03:42:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 687c6a38-ef41-3e7b-9b96-474d63bd1bbc | -5.4074 | -44.06002 | 2025-10-19 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5955ba9f-6538-347a-8b9d-3e64c8c83a1e | -5.10358 | -47.79906 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cc943584-2fe5-393d-8d02-57ffaf227edb | -7.76767 | -42.48085 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 64b55d62-20cc-3f8d-b7d6-76148b1161d2 | -6.43627 | -43.92027 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2fd44d3-00b5-3196-a277-0a29d39eb966 | -4.45845 | -43.23161 | 2025-10-19 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eb5bd5c-c148-3f3a-b48c-e49d5980dc85 | -9.21311 | -46.05807 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e5e7b49-6ddf-3145-a273-3bf6ea7d1510 | -9.2294 | -46.06506 | 2025-10-19 03:42:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbe494c6-d99c-3d20-88d4-1a79dacbda21 | -7.42199 | -40.07095 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4ed0e18e-3ef7-32e3-b350-e949c28e2594 | -5.64577 | -44.80776 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 173f7689-1db4-30cc-b315-e6a066523ff4 | -7.3251 | -47.25446 | 2025-10-19 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5547886-6c5e-3563-8e7a-ca8da2035a59 | -5.30075 | -45.07726 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fa63967a-4463-3940-ac8d-828fcf68d76a | -5.40684 | -44.06328 | 2025-10-19 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2902c308-5400-303c-8ff3-0e1c538d6429 | -7.20112 | -42.20566 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15d7af8f-b1da-3e18-85fe-96079a6d7ce4 | -5.55153 | -44.95626 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 800b3c6d-29d9-311e-be9a-fe8ce7435568 | -4.83409 | -43.02052 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e4ca77e8-0592-30be-a096-3b6143447fff | -5.64744 | -46.58327 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README10.md)
