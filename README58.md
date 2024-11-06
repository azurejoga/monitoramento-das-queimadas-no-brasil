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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15636b7d-0bac-3ee3-a957-be43b43ef1d7 | -6.10376 | -43.9717 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0516d413-0184-31ca-bab4-f0490e8de60a | -3.66783 | -50.22217 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bf312be8-1291-3013-9b41-2156f39dac36 | -6.48679 | -44.67886 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| fea964f7-be5b-3bc7-8f91-6dbca0225c73 | -3.95419 | -48.15293 | 2024-11-06 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f52a7fe1-1e52-3a0a-82e3-70ed0c7eca1c | -4.59792 | -44.04028 | 2024-11-06 05:12:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f086265e-1e3c-383d-bbaa-0a060c111d75 | -4.35168 | -46.53005 | 2024-11-06 05:12:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e8907935-3cd3-3abb-905f-873571a708b8 | -6.12012 | -43.98314 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 29d7c373-7434-3c43-a08e-3546cd98171b | -4.69355 | -45.64995 | 2024-11-06 05:12:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59e2b475-c8ac-357f-8401-d1a408f4e2c9 | -4.12978 | -43.59015 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 010d9ffd-2fed-3a69-ad0f-270c13d75c37 | -2.84333 | -51.77823 | 2024-11-06 05:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| dabbac58-4d3d-38ad-94c8-ecb29e47091f | -3.3234 | -50.07627 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 897476b6-d9a0-3931-924b-fd8bc1f36ef3 | -6.50679 | -44.67009 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e24b2a77-211e-3b0c-98d4-3d63c6349221 | -6.26346 | -46.90069 | 2024-11-06 05:12:00 | AQUA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7e52a16f-6a8c-396c-93cb-4514a3dba540 | -6.12897 | -43.98445 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c40f7a61-1d9f-3c05-83c7-55c648608687 | -2.80823 | -52.92735 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2da58026-3c36-3e19-bea0-8914951507d8 | -4.36164 | -46.5317 | 2024-11-06 05:12:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e4270ebe-375b-3d3b-838c-6b284237768a | -2.45025 | -49.02628 | 2024-11-06 05:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 08e65d5e-32cd-3517-935f-8e1df85fa391 | -3.11831 | -51.10486 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 2ec0157d-8318-3ef3-9de4-e809e026ae9e | -2.93142 | -51.02867 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 152635df-632a-3dae-8bed-281eb478ddef | -2.91683 | -51.0264 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1af7df0d-3018-3c60-956a-7c617e1d9b60 | -2.84815 | -51.74783 | 2024-11-06 05:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3baa97e1-feff-3def-92a5-963c00f9ef29 | -3.0187 | -53.41253 | 2024-11-06 05:12:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dd41ca16-731a-3709-8a0f-922d61a1550e | -6.51572 | -44.6714 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2a2e4ba-7c52-3ef6-bffd-6c0018bdfb6a | -6.51435 | -44.68043 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ef7f1085-2bd0-3177-a71d-aa758b64ca0f | -2.92736 | -51.05517 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e3af0dd7-3d58-305f-a2f9-68dc3b2856df | -3.18902 | -50.57178 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8d5393bf-912a-3c0a-b75c-7ed5fbde9b09 | -6.48542 | -44.68791 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de81d188-6423-3a32-a755-a93afb38e4e2 | -3.60281 | -42.8577 | 2024-11-06 05:12:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d01b22ae-b618-38b2-849d-436ec8fe2f2b | -2.85879 | -51.78072 | 2024-11-06 05:12:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b55eacce-28aa-307d-99c0-4c2156e7d719 | -6.05216 | -39.43573 | 2024-11-06 05:12:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 40cc867d-b374-3669-b69a-f24ed399d56c | -2.94134 | -51.06505 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 408c6772-392f-3e78-9af5-7d9da9725d6d | -4.1311 | -43.58132 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 7a727350-aac0-3ab4-991e-f8c8e94514d3 | -5.12248 | -44.35615 | 2024-11-06 05:12:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67c98c1a-40f8-345a-88ee-12e0a095fa2e | -4.05389 | -46.93077 | 2024-11-06 05:12:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 74f758f8-9336-3fc1-a581-609dd8e58ceb | -2.91639 | -51.03398 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 59463e7e-89bf-3a52-a2dc-188095ffd482 | -5.56319 | -43.70142 | 2024-11-06 05:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f8fadd3-2bd8-3578-a738-9f00ffdabeac | -3.15745 | -50.20248 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 23e50208-e202-3747-a1d8-35b9ba7c0275 | -3.52858 | -50.35405 | 2024-11-06 05:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 07608921-0c0e-3a6d-90a7-c10825c8ddf7 | -4.06419 | -46.93234 | 2024-11-06 05:12:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ef9aeff2-a0c8-31eb-a0de-b4caa9561109 | -3.22302 | -50.35976 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| af780102-a774-31ab-b3d6-f0594e5d2952 | -6.1303 | -43.9756 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 82463b11-1ca4-343d-90fb-09fb81f05799 | -4.68203 | -46.38652 | 2024-11-06 05:12:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7c670589-9e2d-3aa9-98d6-f3e529769d04 | -6.12145 | -43.9743 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 855eb658-7809-3d14-9d2c-f579d7a7817f | -4.68028 | -46.39774 | 2024-11-06 05:12:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e347f9c6-ef7d-300f-ae2d-c0f0a4b47f0e | -6.48925 | -47.48655 | 2024-11-06 05:12:00 | AQUA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6949bc68-66bb-365b-b3a3-afdef22ac73e | -6.49649 | -44.67777 | 2024-11-06 05:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 332de85a-0a23-318b-9ce5-d021f114c194 | -3.96556 | -48.15449 | 2024-11-06 05:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 00e4462c-f4f2-3fe8-8881-9bb98e29a452 | -2.83933 | -49.47317 | 2024-11-06 05:12:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| ad838d8a-4a4d-3db9-b880-20397956d615 | -3.21462 | -50.37463 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c8e63a0a-eaca-31e6-bfb1-5c916626367c | -2.79872 | -51.49025 | 2024-11-06 05:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| fba9e9f0-8f15-3a1f-a3de-ae028f2c38b3 | -3.22839 | -50.3768 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| c43de39e-19a6-3b40-a96c-b3ba05153bf7 | -2.84245 | -49.45323 | 2024-11-06 05:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ec35b74d-9ca5-3cba-8a60-d9cc088fa06e | -0.97123 | -47.79718 | 2024-11-06 05:12:00 | AQUA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| cfab3321-9ab7-3308-b100-f2306bd515b1 | -6.13162 | -43.96676 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 147b8c41-7573-35d0-8ee2-08e6b527133e | -4.69511 | -45.63989 | 2024-11-06 05:12:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| efa4bb53-aa57-3581-9342-2d82e19efdca | -2.92673 | -51.06269 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| eba6ab13-8399-3ac5-aba4-cab484448412 | -3.15931 | -50.22058 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 96400862-8ef9-3914-92e3-740044f125b3 | -3.1189 | -51.09745 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 067a8a46-cb3f-3bac-a8eb-80873dd079e1 | -5.55435 | -43.70012 | 2024-11-06 05:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| cb530fdf-e61a-3ba3-ba60-8f74103646b5 | -6.05758 | -39.42807 | 2024-11-06 05:12:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5e377366-62c0-3c7d-9e47-f58f556ecb7f | -2.67256 | -51.8021 | 2024-11-06 05:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| fcffa9fb-ae14-306e-9a00-eb2927cf105c | -2.65727 | -48.56038 | 2024-11-06 05:12:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bde7902b-47a8-3b24-b23c-43c7ba029f88 | -3.96462 | -46.9747 | 2024-11-06 05:12:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7e35b380-b9ad-37d1-9700-2b19f46ce53b | -4.13995 | -43.58262 | 2024-11-06 05:12:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3350e92c-d01c-3864-9166-830c1a9fb370 | -3.13488 | -51.18987 | 2024-11-06 05:12:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 361ad7a7-d8b4-3c05-8483-1fa911d1f3ef | -6.50144 | -47.47609 | 2024-11-06 05:12:00 | AQUA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e3a20371-a23a-3e59-9fc4-46cf16f4b289 | -6.49114 | -47.4744 | 2024-11-06 05:12:00 | AQUA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 24409266-a7f2-3501-a705-c99a1e7c33a6 | -6.1126 | -43.973 | 2024-11-06 05:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 132d41fd-ca54-3150-925b-64774cbeddb6 | -6.49766 | -47.5004 | 2024-11-06 05:12:00 | AQUA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 417604e4-9d7b-3910-bb62-f19605de64eb | -6.93189 | -47.78453 | 2024-11-06 05:14:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 653fb4ff-1f39-31ff-a342-3d6ebe19f7fb | -8.50269 | -42.0996 | 2024-11-06 05:14:00 | AQUA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b4d1dc83-1570-36ce-80db-1b8a4e453a10 | -8.50411 | -42.08973 | 2024-11-06 05:14:00 | AQUA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 843cd09a-2649-3704-b326-3f1a041629cb | -6.93782 | -47.7787 | 2024-11-06 05:14:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0b629dcf-04c8-39c9-b4aa-312864050cdb | -9.89525 | -42.08891 | 2024-11-06 05:14:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8442c261-4a9f-3eb7-a4d2-9e0d0e31bdec | -10.04736 | -44.75944 | 2024-11-06 05:14:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9fdee5eb-3600-358d-a778-d863d283fcff | -23.93066 | -54.05544 | 2024-11-06 05:16:00 | AQUA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 0a835853-e65d-348f-81bc-c4c1e0be80b9 | -3.2348 | -50.3904 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ac9459cd-e726-3a64-bd10-f4c8095e5553 | -2.7243 | -54.1552 | 2024-11-06 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 2c52098c-06b7-32cb-863d-ba7c218d6499 | -2.9186 | -51.047 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 647552a7-7807-3897-9761-2eb18ebc26e0 | -3.1617 | -50.2038 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 1f8b2d26-8b69-3d65-bd33-1c32789d9204 | -2.8423 | -51.7735 | 2024-11-06 05:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 42937830-ae4c-3026-be5d-6711b6af7e97 | -3.5446 | -47.3855 | 2024-11-06 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 0005e26c-86f0-3bf6-bcd0-16b7a780942c | -4.1246 | -43.5833 | 2024-11-06 05:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d939aae7-6638-342d-b58e-34d837cfc27e | -6.5094 | -44.6847 | 2024-11-06 05:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ab333333-61a4-3421-a191-17810c94837c | -3.0212 | -53.281 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a1e75109-48a1-3006-a4d0-01255e081082 | -2.8608 | -51.7731 | 2024-11-06 05:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 54a096aa-b11e-3423-b0c8-c00e46befb0e | -3.0397 | -53.2603 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 60ae2217-879f-39da-b655-177058069d81 | -2.4457 | -49.039 | 2024-11-06 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 29141455-78ed-3acc-98f1-cfe46465b8f5 | -3.9669 | -48.1716 | 2024-11-06 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 0d13cf0b-2f84-335f-9686-dcdbd30739d4 | -3.967 | -48.15 | 2024-11-06 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f907c615-b674-3bc2-a7ae-bf23419ec62b | -3.0396 | -53.2805 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5020ab70-923d-3335-b47c-05d0ceed24b4 | -2.8506 | -49.4744 | 2024-11-06 05:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c77c27d1-96df-33d5-a025-7a9b0ee2f384 | -3.0023 | -53.4434 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5e925cd0-0d4b-371e-ae68-d86e5df65fd3 | -6.5012 | -47.5033 | 2024-11-06 05:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 18b0682c-a73a-34f0-b64f-7d99a4023cb2 | -6.4906 | -44.6862 | 2024-11-06 05:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4e83dbf3-3909-3de3-a126-1feaed587a73 | -3.0207 | -53.443 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9abf9802-65ab-34f8-8b64-935e1df8a9d5 | -3.2349 | -50.3695 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9d2ad490-6d24-333e-8bc4-a1cfaa23c6fe | -6.5014 | -47.4813 | 2024-11-06 05:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 601e4c87-2c5c-36cc-9605-63673422a4fb | -2.9371 | -51.0465 | 2024-11-06 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 67d12002-2096-3ea7-b13a-d74b30c969b8 | -3.0207 | -53.4227 | 2024-11-06 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |


[Clique aqui para ver as próximas entradas](README59.md)
