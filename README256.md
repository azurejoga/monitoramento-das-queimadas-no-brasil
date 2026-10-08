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

## Dados Diários - Página 256

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de9a75bc-1398-3f73-a7ac-c8ae67a24942 | -18.9787 | -44.45808 | 2026-10-08 16:16:00 | NPP-375 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0bb0510d-e8e1-3d63-81ce-89ad35a6faea | -15.95726 | -41.10358 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 82a84aa4-df61-3b51-9628-cf613c525474 | -18.33875 | -42.38159 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d4ada176-1eaa-3833-a483-dbb85de4ac60 | -14.96962 | -41.52044 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 9679d38c-3c64-392f-8520-57900359a880 | -15.54449 | -43.16939 | 2026-10-08 16:16:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8c52c8e5-4bfd-3524-bbde-821969a92c6b | -16.58827 | -46.75533 | 2026-10-08 16:16:00 | NPP-375 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 35014342-1fb8-35d7-8ea3-4caedf6a2ee3 | -15.62662 | -40.12583 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ff624ad5-814f-3c91-aaca-84f9d4432402 | -14.49471 | -40.71789 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 17f17456-fb9a-3871-8858-5d5b608513b2 | -14.82079 | -39.40516 | 2026-10-08 16:16:00 | NPP-375 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| bf538131-7d1d-3c48-828e-49c67879d2c2 | -16.68616 | -42.51982 | 2026-10-08 16:16:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0a5c17d-8486-34e3-8f5a-3b1961a16a55 | -15.10301 | -49.66426 | 2026-10-08 16:16:00 | NPP-375 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f77f6dc4-62cc-30a5-9ac9-6c3ca29dd2a4 | -18.05408 | -44.57417 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c315377d-2eb9-3cd0-814c-24d8a79e8480 | -15.21523 | -46.01799 | 2026-10-08 16:16:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f431856b-22d6-3406-bb7d-efe26d3244ac | -14.37187 | -39.84219 | 2026-10-08 16:16:00 | NPP-375 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 06a8650a-c087-31c8-804c-12455a6193bb | -14.27042 | -40.39193 | 2026-10-08 16:16:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 83.5 |
| ddb450ae-6375-3d57-96a7-eec851b746bc | -18.13213 | -42.06514 | 2026-10-08 16:16:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7ccc94b4-b111-39be-aa97-d35373bc6ad6 | -17.07205 | -45.40584 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 08bba3a8-efb1-3d45-9845-f9d1b3c4e81a | -15.16898 | -48.22746 | 2026-10-08 16:16:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55de5e18-3f5a-34c2-8b91-08070f526575 | -15.85725 | -40.79705 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e0619ace-46ee-34d5-af8c-22f19d9a973a | -18.81127 | -41.88931 | 2026-10-08 16:16:00 | NPP-375 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2e002cb6-86d3-31bc-9139-123e05fcc8d1 | -14.85052 | -40.79218 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 835bfbc1-2f5e-3aaa-8139-b3baee158fad | -14.06869 | -40.33581 | 2026-10-08 16:16:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 05e05cef-f334-35ab-81e0-18337c48a654 | -15.53232 | -40.62616 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a64dac57-ca0f-3dc7-8d80-9c4a7717cad9 | -14.41128 | -41.28925 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 77af7083-fc6c-35fa-9e77-cfcd7f543137 | -15.95814 | -40.82899 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ad1332a6-ad0d-3283-970c-acffbe4aba74 | -15.02139 | -42.26702 | 2026-10-08 16:16:00 | NPP-375 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff700406-dc16-3799-be68-55a1ba5730ec | -14.45435 | -41.23409 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 45ae8c6b-4375-3529-9a08-38f8740a185a | -14.41 | -41.28002 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c524613d-6007-3b5c-b8a4-a3a91623c989 | -15.82482 | -40.48396 | 2026-10-08 16:16:00 | NPP-375 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| e65d4fcc-4e2c-3ca1-9cc7-d9fcd0965f0f | -16.11155 | -40.79392 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 991f0331-cef1-34da-9b4f-af6a0bcc8aed | -18.97098 | -45.59666 | 2026-10-08 16:16:00 | NPP-375 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4c34969-70e6-3eb9-af36-3df37992fc53 | -13.6908 | -39.93321 | 2026-10-08 16:16:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b00d4843-e95f-3efa-b966-aa695eece6c0 | -18.05175 | -44.56866 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80214a8b-8c11-3adb-bd5f-3ecc24f5b6d2 | -15.16647 | -48.22917 | 2026-10-08 16:16:00 | NPP-375 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5bc3084e-5077-33e5-97e8-9c4a2a364ffe | -19.07767 | -48.65042 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b6fe52e3-5ba0-3fbc-9f8f-7fe9d9475204 | -14.97238 | -48.18993 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df1b1100-80a9-39fe-88f2-51d6c6066f50 | -16.63362 | -45.5122 | 2026-10-08 16:16:00 | NPP-375 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8a15756-d096-3b18-872b-ab0b1b149d15 | -15.08888 | -41.35578 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 5b3af5df-c262-3462-ba18-0f1df2e26699 | -14.75375 | -47.13865 | 2026-10-08 16:16:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 943565f0-5779-3a44-b03d-c2bb01d2d73b | -17.11183 | -41.35304 | 2026-10-08 16:16:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| d40119bb-14e5-31b7-af19-f8db69cf2b40 | -14.43358 | -40.81028 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 806567c4-7b39-33da-b797-47e0d58c3bfd | -16.14963 | -43.1162 | 2026-10-08 16:16:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c70d59f0-b9c3-3681-b35f-6928e2040be0 | -17.06692 | -40.02071 | 2026-10-08 16:16:00 | NPP-375 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 2e505864-3aab-3dd1-9a49-88572adaba9e | -15.47794 | -40.49726 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d7190592-697d-35a8-87ee-7f8825e4ba5a | -15.70323 | -40.59589 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 49632deb-b7ba-3620-b0b1-ad39c5d9d802 | -17.10643 | -42.16024 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e1dfef5f-f954-3b6a-8e62-96b369d54886 | -17.45223 | -45.05943 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5dc317da-32b9-3d77-8641-1c7c7d478200 | -18.0519 | -44.59778 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 13c78bc9-1076-3f6e-b2c8-e96e8a134a60 | -15.47887 | -41.00763 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 7c79e694-4865-3e14-a145-4964a08deef5 | -16.56361 | -44.16603 | 2026-10-08 16:16:00 | NPP-375 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8d99fb8e-858b-3ce9-855d-df716c4633c5 | -15.04367 | -40.23995 | 2026-10-08 16:16:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4317f834-1f0b-3a85-b480-5aafe9c715fa | -17.40617 | -42.89922 | 2026-10-08 16:16:00 | NPP-375 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f138a07f-bd71-3ef1-a57e-27679e35194a | -14.54831 | -41.38885 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 42d6eea1-a89a-35bc-8a2d-bf9bc5ea410e | -19.64152 | -42.05243 | 2026-10-08 16:16:00 | NPP-375 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 28da63b1-326e-322e-803f-986762bdcd18 | -15.71198 | -41.02014 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 28207cc9-437a-3b74-a6c2-4329f920795d | -14.8468 | -47.26676 | 2026-10-08 16:16:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b5724e2-806f-315f-bb78-ccf4a8704054 | -15.70214 | -41.79023 | 2026-10-08 16:16:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| be837765-12bd-3115-bec3-ab3dc8462d70 | -14.86215 | -40.87633 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 2ea5cbe9-819f-3add-b333-d3eee1d0297b | -17.02972 | -41.05994 | 2026-10-08 16:16:00 | NPP-375 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6e52312f-d913-383d-896b-ef4a60e4feaf | -14.75934 | -39.81329 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 24aeedff-5523-39ed-83a1-7d30a34940be | -14.40755 | -41.28988 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8b3bfa96-c251-3bce-92f4-34f26f06e19b | -18.22803 | -47.32895 | 2026-10-08 16:16:00 | NPP-375 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 697bbd95-15fa-31c8-ab1e-c86a7a759d2f | -16.14711 | -43.74607 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f96b27d1-8e58-3641-9d2a-85dcd53e6b11 | -20.58392 | -48.45848 | 2026-10-08 16:16:00 | NPP-375 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 634a313d-bbb9-318f-8b41-e92cce7ee462 | -15.82644 | -45.3999 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f128679d-0efb-3560-807b-d44f95be83e2 | -14.68146 | -43.12691 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 179dc220-dbae-32b0-be54-d230cc0904dc | -16.9534 | -40.05648 | 2026-10-08 16:16:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6f9f0ca9-cf37-31da-9f36-8f3acca67b9d | -14.5059 | -40.37847 | 2026-10-08 16:16:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 76054593-0c4f-31a1-bca9-30d33969c065 | -14.67447 | -40.80644 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| aaafbdb3-3b1e-3576-882b-634e3b8dbe13 | -15.43024 | -42.3079 | 2026-10-08 16:16:00 | NPP-375 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 75fdc1a7-5abd-3074-8262-8bd9a4ed2cdd | -14.26606 | -40.70149 | 2026-10-08 16:16:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 366592d2-f7c4-3497-b912-79e49f5a7c4e | -15.96409 | -41.43288 | 2026-10-08 16:16:00 | NPP-375 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6b2cab36-ef48-33df-b4cd-3d5640fc7423 | -15.62938 | -43.29913 | 2026-10-08 16:16:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1c08e4ab-d3df-35ac-93c7-ae69ed3df63e | -15.65564 | -47.83047 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cfdc15c-b789-3b94-905e-ded906588cbc | -15.79225 | -44.68699 | 2026-10-08 16:16:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1c70a548-2c42-3526-9e3a-cdddee44acff | -14.53893 | -41.7748 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 2b72ee4e-255b-3fc4-8450-3af21ab4c752 | -18.28697 | -42.24208 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| 4d0700a1-5607-3e69-b20e-56f4b3feb0fb | -16.21122 | -40.16829 | 2026-10-08 16:16:00 | NPP-375 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7512a777-f608-3cb0-bd34-a238d4437d8e | -14.53508 | -41.7754 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d751657b-3be7-36fb-b6d2-e627f651808f | -15.12805 | -41.38865 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 223.7 |
| 75f8a215-f1b7-3065-b83a-5c353538a3aa | -18.13167 | -42.06145 | 2026-10-08 16:16:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 94f1fa43-60f1-37ea-9c10-b3e9c3f4f244 | -18.27791 | -42.6225 | 2026-10-08 16:16:00 | NPP-375 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 2c344c59-a243-3e32-ac43-e6f031cd8953 | -14.97279 | -48.19388 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8d0b4021-e0e6-3b4f-931b-d2547a479616 | -19.06387 | -48.64011 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 753a78f4-0542-3a9d-ad27-916e3bee177a | -14.46921 | -40.72122 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 1cf88672-a81e-336c-8a1b-03b53834a513 | -16.37157 | -39.80415 | 2026-10-08 16:16:00 | NPP-375 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| aba022cc-b8b6-35a3-a826-fa7d1a82ce69 | -15.98641 | -38.91882 | 2026-10-08 16:16:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bca134df-b1d8-3beb-8e19-9c5186f2ed4e | -16.01014 | -40.64571 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c3df6029-3ce2-3bdd-81fe-9b22a97188a0 | -15.95349 | -41.10413 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| a5fb02c9-752c-340f-84da-ea69d7d317ac | -16.83202 | -41.0429 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 87103c4e-cae5-374c-95c1-926180744a5d | -17.10343 | -41.34938 | 2026-10-08 16:16:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6a07bdcf-b3b6-3558-a626-477389a0de5e | -16.19509 | -44.57145 | 2026-10-08 16:16:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 90231067-3f9b-3790-966c-f8c5b34d13bd | -14.99485 | -44.05888 | 2026-10-08 16:16:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 77d6ef37-4af0-3e2f-b87d-7a06df1f6150 | -14.40691 | -41.28522 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f7d84062-55ce-3acd-be33-d57e767599f8 | -16.97629 | -41.23273 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 42539c56-ef13-3089-a148-2dd6d6e9c8ce | -15.77108 | -40.33823 | 2026-10-08 16:16:00 | NPP-375 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9a49bf11-01da-3539-84eb-bc13c8db3608 | -16.97051 | -41.21884 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| c1b0a261-f61d-3c22-a01f-519b71434f3e | -14.26306 | -42.4393 | 2026-10-08 16:16:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ef5452a4-3674-315b-aa91-f334476c01df | -17.02908 | -41.97625 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f5c97c15-b42c-3045-97d9-eff76801f40b | -15.64338 | -42.42014 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README257.md)
