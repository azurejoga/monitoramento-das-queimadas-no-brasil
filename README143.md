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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1df20a96-c656-3146-93dc-091b3992e174 | -2.9723 | -57.214 | 2026-09-22 14:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0e100789-2dc2-3ccc-9191-87769ce3fd5a | -3.3138 | -59.4472 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cd8a5166-656e-367d-ae41-249af88e864c | -3.0717 | -61.2764 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 21842c21-0baa-340a-a157-240585f7d49c | -10.3919 | -50.2702 | 2026-09-22 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5272493a-abff-3323-844e-48127c42dab0 | -6.8032 | -59.1693 | 2026-09-22 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 907d86f2-4a9d-3893-8b1c-75bce636d8f3 | -3.3136 | -59.5046 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 31838667-888d-3b3a-94b4-faa4f48def23 | -6.7989 | -43.9008 | 2026-09-22 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8857552d-b0eb-3f0b-b43d-f571df7752f5 | -6.3013 | -59.9771 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fee9597b-9e81-3bea-a64e-a6c82ba08a5d | -3.2396 | -53.9417 | 2026-09-22 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 0f7c0adf-e36c-3e17-b644-d475a6e710a6 | -2.9326 | -58.3397 | 2026-09-22 14:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c9b3058d-3109-303e-b895-eccd1e021daf | 2.2187 | -50.8769 | 2026-09-22 14:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6dbcef17-210b-388f-91a3-1d63adf54325 | -6.7463 | -59.4416 | 2026-09-22 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9abafab4-f8fd-35ab-8984-e26a6ba6bf98 | -9.6111 | -43.9243 | 2026-09-22 14:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 302.9 |
| 1706ccd3-f837-3c5a-8b45-34165f0fa4d8 | -6.7776 | -47.8981 | 2026-09-22 14:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b4c24667-b433-36af-8897-78e6e20432be | -3.4049 | -59.5794 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f87c4fd6-c5d1-3ca4-ab06-8fd1418870cb | -10.7073 | -50.7064 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 96214ef5-b179-3df9-bf50-9544f77cdd26 | -3.405 | -59.522 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 205.2 |
| a2789bcb-804f-3bcf-9767-0e0db8c46b08 | -3.7364 | -58.8818 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cb1ee507-4ed9-3760-b9d8-281faf510709 | -7.1555 | -47.4751 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 687d8f93-7905-3053-b17f-8b994314dcfd | -3.6065 | -59.4413 | 2026-09-22 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dbfb5c64-2878-3da7-8d70-2c67a6614f98 | -7.0619 | -47.4826 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e8eaf323-e0cc-3e66-a9e9-005f4e1fe67a | -5.5717 | -42.7414 | 2026-09-22 14:50:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 4080ad1f-e939-39c2-a48b-4ef3163a7c25 | 3.5482 | -60.6623 | 2026-09-22 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5624fc79-7afb-311d-ae13-e5e0b3ae57f6 | -9.8665 | -45.8918 | 2026-09-22 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7202578f-e8fa-33ff-95d2-c71860f4692d | -11.44 | -47.3579 | 2026-09-22 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 6b8c94af-4f02-32ad-8dc5-deba53c2ee1f | -9.6006 | -45.9456 | 2026-09-22 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b1ae2ba3-f4fb-390f-ac16-cd7ba62fe599 | -6.0993 | -59.9076 | 2026-09-22 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0b548992-5622-307b-8110-4af4034c18f1 | 3.9356 | -59.568 | 2026-09-22 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 43ca8757-48bf-3c54-84a0-f2dcbef2ecff | -7.0661 | -45.2521 | 2026-09-22 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0cec76cd-8caf-3fe4-9c2b-ff5efd40ffde | -3.3358 | -58.1384 | 2026-09-22 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7fe6bef6-66fa-3f53-a8e9-2bc6abd63a60 | 3.0196 | -60.1017 | 2026-09-22 14:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 39f1e6bf-23e9-33ac-af87-98b117d27a53 | -3.3183 | -57.8677 | 2026-09-22 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 61efdf24-9164-3c5f-b793-c7ef02221f72 | -11.6793 | -43.4684 | 2026-09-22 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ff59621b-4f68-382e-9a37-edfb738d09ba | -6.7591 | -47.8777 | 2026-09-22 14:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9ffe25ba-5eca-3276-8f76-da17e02f9d87 | -6.1111 | -57.6645 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 44b6931a-2499-3eaa-9f7c-2e9b42cc7cd5 | -7.0352 | -44.6396 | 2026-09-22 14:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 9011532e-217d-3492-aa0c-2b1a2f331e74 | -4.64 | -42.0976 | 2026-09-22 14:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| 9632a846-fb59-3c28-b3ce-7a2f9e82c445 | -10.7632 | -50.7644 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| e1227822-2ad0-3799-b3be-13bfd0859841 | -6.2399 | -41.6394 | 2026-09-22 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 168.0 |
| 66c1e6ad-ba11-391a-9f80-78841e2c7bb9 | -3.3645 | -61.0257 | 2026-09-22 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 06a6046d-8ab2-3b33-9f6e-f313d0bc6694 | -12.2726 | -50.1441 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 92fbe391-c506-355f-abc3-75213e5423c3 | -3.0358 | -54.4085 | 2026-09-22 14:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 13b7c387-fb0b-3cdf-b589-4b16b852de5c | -8.7706 | -45.8567 | 2026-09-22 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b8997f14-18b3-3c3e-bd86-76f139f410b0 | -2.4206 | -58.2712 | 2026-09-22 14:50:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7bbfea0f-1cdd-390d-903b-b1e55f0fb96e | -8.7456 | -44.8815 | 2026-09-22 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8b9db4ab-4ad6-39f8-8c25-2da7f862b362 | -10.5745 | -46.7521 | 2026-09-22 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2af018d1-b902-380e-8cda-6712499d1c53 | -9.9516 | -53.9844 | 2026-09-22 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 88a0f703-0bac-3e62-a9a3-3473e5a33c37 | -9.8676 | -54.8249 | 2026-09-22 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 449af175-472b-3c18-8a98-98adb5becc9c | -2.5687 | -57.5135 | 2026-09-22 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f1058684-87fd-3534-b8ae-ca82e1c72e2f | -3.3867 | -59.5415 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9e5356b8-4247-342d-b13e-6cdab09829f6 | -8.7912 | -44.301 | 2026-09-22 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bbdcc569-9b6e-33de-bb84-4006e7ed492a | -10.11 | -46.0888 | 2026-09-22 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 940a9203-37a9-3347-b9f1-ed1d10e4548e | -11.1563 | -51.0839 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| bc7200f1-174a-33f9-bfd6-0d8b4a456416 | -3.3867 | -59.5223 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| aca67308-2ff4-3bbd-8797-98fa664cc4c1 | -10.6889 | -50.6658 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8b03cf0e-7c79-3187-812c-5dbb4b29a489 | -10.7626 | -50.8069 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ccd5bb58-e766-32bf-99f9-456d3347b173 | -6.9683 | -47.4899 | 2026-09-22 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 99bc6b5a-94ac-335f-a12f-d27b9cc33eb6 | -3.1719 | -57.832 | 2026-09-22 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4d6de981-4765-3903-a709-7706b9d24802 | -3.4634 | -58.329 | 2026-09-22 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3119fa22-34b7-39c7-ac11-9b899a6c30e1 | -12.3293 | -50.1802 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 355.2 |
| 9498ef5a-34f8-3d1f-b99b-0799f51b9d6d | -10.7466 | -50.5959 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 24fe0dad-b9c8-35d8-95c3-132e7818a8de | -10.6875 | -50.7722 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 15ee4265-9673-33dd-960a-4643bcf9c809 | -12.853 | -50.8885 | 2026-09-22 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 79651c82-64ed-3386-b021-67f4ada896d5 | -6.295 | -57.735 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| a19a434a-745e-309b-a98f-0176e7ac5a27 | -10.3126 | -50.5554 | 2026-09-22 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 709aa785-c34a-3a8d-a41f-51db0aab6371 | -3.3309 | -59.8673 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6f7f22ba-09fc-39ae-91bb-f8cfc02c0905 | -6.2394 | -41.6875 | 2026-09-22 14:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 7bd59591-ee3d-3784-8e3a-8cf13524fad0 | -5.841 | -53.5205 | 2026-09-22 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dd1c3014-0dee-3b26-9397-5cc87b7c8d4f | -3.3492 | -59.867 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 59c80077-5cdb-3a01-870b-f5a2cf9844d2 | -8.3764 | -47.2802 | 2026-09-22 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e31b11c1-b11a-354c-9570-d5c7970bddbf | -9.6108 | -43.9477 | 2026-09-22 14:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| a27ce4af-455c-321d-953c-45b8d3774335 | -11.8559 | -49.979 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6e146eeb-4745-33cd-aec8-c88d095fe0d7 | -3.3493 | -59.8479 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5dab2c81-5e4b-3c41-b9a3-9419f42ec25e | -6.8985 | -41.6976 | 2026-09-22 14:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 200.8 |
| 525ace3c-e5ed-3124-b9ea-17fcc2b8f577 | -3.4599 | -59.54 | 2026-09-22 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 4efe1bf9-3918-33db-b040-25c5e9dbdc61 | -8.845 | -45.9391 | 2026-09-22 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f4c95d8e-4ef0-317f-8dcf-d8ab8d521241 | -2.5492 | -58.0179 | 2026-09-22 14:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 129f3bfa-920f-38f2-84ff-336a8212c75d | -3.8279 | -58.899 | 2026-09-22 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fbaedfa5-0ee0-322a-88de-51d5e50dda6c | -10.7437 | -50.8089 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 163.1 |
| ee8bab63-866d-31f8-aff1-8807ce34fb64 | -11.156 | -51.1051 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| e79642e5-5fc3-3f23-ac4a-c4181a6d3c09 | -12.8526 | -50.91 | 2026-09-22 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ea1524e0-a2e5-3ea1-bed9-8046b5644583 | -3.3 | -57.8681 | 2026-09-22 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.3 |
| adb1a3d2-e06c-304c-956d-c47583cd6a1f | -4.0925 | -62.0874 | 2026-09-22 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 511dde7c-47b7-3b42-809f-50a3db179206 | -12.3105 | -50.161 | 2026-09-22 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 2911c3a7-3bb8-3fe6-a1e8-c16f7364f1be | -3.7673 | -60.7339 | 2026-09-22 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 786bf773-b977-34d6-9967-07a5f115b506 | -8.4985 | -57.6075 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| eb7c271d-d008-3183-ab70-e70d10a3888b | -2.9723 | -57.1945 | 2026-09-22 14:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a10df048-db38-37f6-8cfd-b41ed63aaaa7 | -10.4539 | -51.3038 | 2026-09-22 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5a80824f-c208-3d51-9d6e-aa24f8bad37e | -2.9525 | -57.72 | 2026-09-22 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 068a7f0e-9635-3a12-9138-5d9b3fe71f2e | -3.1901 | -57.8898 | 2026-09-22 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8d162e7d-8b8b-346a-9a21-3403412541f2 | -10.8008 | -50.7817 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 297aa76e-47a2-3eff-b22a-2dda5f7b95bb | -8.4799 | -57.6085 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| de8e93e5-4293-3bc7-bf8a-cbec56993210 | -10.6878 | -50.751 | 2026-09-22 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 27f99351-7527-3c16-a1dc-c1eb2c90e1b2 | 3.7681 | -60.468 | 2026-09-22 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 62572419-1558-3cb2-bedf-059cebce089a | -6.0924 | -57.7043 | 2026-09-22 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| bba39a88-e6a6-3803-b384-5c1584b7f186 | 3.9534 | -59.7206 | 2026-09-22 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5648587f-4967-30ce-a3e2-6f64b708ce5b | -6.7963 | -47.8967 | 2026-09-22 14:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d50e1b22-ce5e-3118-bf90-176d8b89afc1 | -5.2913 | -55.9487 | 2026-09-22 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 889c59d5-3f7d-3dcd-9454-33d046f7ee46 | -10.4541 | -51.2827 | 2026-09-22 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f1633380-0eef-3262-9a43-930c32960715 | 4.1314 | -61.2945 | 2026-09-22 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |


[Clique aqui para ver as próximas entradas](README144.md)
